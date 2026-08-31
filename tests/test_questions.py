from scirate_digest.questions import is_question, parse_issues


def _issue(number=1, title="Q: what is a qubit?", body="context here",
           labels=(), user="abid1214", pr=False):
    d = {"number": number, "title": title, "body": body,
         "labels": [{"name": n} for n in labels], "user": {"login": user}}
    if pr:
        d["pull_request"] = {"url": "x"}
    return d


def test_title_prefix_detected_case_insensitive():
    assert is_question(_issue(title="Q: why is the sky blue"))
    assert is_question(_issue(title="q:   lowercase works too"))
    assert not is_question(_issue(title="Bug: scraper broken"))


def test_question_label_detected():
    assert is_question(_issue(title="anything", labels=["question"]))


def test_pull_requests_ignored():
    assert not is_question(_issue(title="Q: looks like a question", pr=True))


def test_parse_strips_prefix_and_truncates():
    issues = [
        _issue(number=7, title="Q: What limits tetron qubits?", body="x" * 5000),
        _issue(number=8, title="chore: unrelated"),
    ]
    qs = parse_issues(issues)
    assert len(qs) == 1
    assert qs[0]["number"] == 7
    assert qs[0]["title"] == "What limits tetron qubits?"
    assert len(qs[0]["body"]) <= 1200
    assert qs[0]["author"] == "abid1214"


def test_parse_caps_question_count():
    issues = [_issue(number=i, title=f"Q: question {i}") for i in range(10)]
    assert len(parse_issues(issues)) == 2


def test_only_answered_questions_are_closed():
    """A question the episode never reached must stay open for next time."""
    from scirate_digest.questions import filter_answered

    script = (
        "Maya: Before the papers, some mail. Ada asks about decoder latency.\n"
        "Sam: Great question, Ada — the short answer is streaming decoders.\n"
    )
    queued = [
        {"number": 1, "title": "how do decoders keep up", "author": "ada"},
        {"number": 2, "title": "what limits photonic interconnect fidelity",
         "author": "bob"},
    ]
    answered = filter_answered(script, queued)
    assert [q["number"] for q in answered] == [1]


def test_answered_detected_without_author_credit():
    """Falls back to the question's distinctive wording."""
    from scirate_digest.questions import answered_in_script

    script = ("Sam: On tensor network decoders and how they handle "
              "correlated noise across syndrome rounds…")
    q = {"number": 3, "title": "tensor network decoders correlated noise",
         "author": "a listener"}
    assert answered_in_script(script, q)


def test_unanswered_question_is_not_closed_by_stray_words():
    from scirate_digest.questions import answered_in_script

    script = "Maya: Today's papers are about quantum codes and decoders.\n"
    q = {"number": 4, "author": "carol",
         "title": "photonic interconnect fidelity budgets in modular machines"}
    assert not answered_in_script(script, q)
