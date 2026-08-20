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
    assert len(parse_issues(issues)) == 5
