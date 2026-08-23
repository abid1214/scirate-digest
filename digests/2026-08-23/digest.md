# SciRate Daily Digest — 2026-08-23

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Fast Algorithms for Stoquastic Spin Systems

[arXiv:2608.19489](https://arxiv.org/abs/2608.19489) · [SciRate](https://scirate.com/arxiv/2608.19489)

*Ryan L. Mann*

**TL;DR** This paper ports the fast classical polymer-model machinery (Chen et al.'s rapidly mixing polymer dynamics plus Blanca et al.'s subcritical-percolation graphlet sampler) to quantum stoquastic spin systems, obtaining near-linear-time sampling from the diagonal thermal distribution and near-quadratic-time partition-function approximation at high temperature. The key innovations are a notion of "κ-computable" polymer models (charging an exponential-in-polymer-size cost for evaluating quantum polymer weights) and "probabilistic" polymer models where weights are replaced by non-negative unbiased estimators, letting stoquasticity supply positivity. For Heisenberg models, Tóth's cycle representation and Aizenman–Nachtergaele's loop representation improve the temperature threshold.

**The big picture** Simulating thermal properties of quantum spin systems classically is expensive; existing high-temperature algorithms based on the cluster expansion run in polynomial time but with impractically large exponents, and recent quantum thermal-state-preparation algorithms are substantially faster, prompting a search for faster classical counterparts. For the important class of sign-problem-free (stoquastic) models — transverse-field Ising, ferromagnetic Heisenberg, bipartite antiferromagnetic Heisenberg — the authors show that the fast Markov-chain sampling methods developed for classical lattice models transfer essentially wholesale, because sign-freeness makes all the relevant expansion weights non-negative and hence samplable. The result is near-linear-time thermal sampling and near-quadratic-time free-energy estimation above a temperature threshold, narrowing the gap with quantum algorithms.

**Key contributions**
- κ-computable graphlet/subgraph polymer models: the graphlet sampler's expected cost is O(1) whenever the weight-decay exponent r exceeds the weight-evaluation exponent κ, and m^{O(1)}e^{(κ−r)m} otherwise; truncation at m = O(log(|G|/ε)) converts the deficit into an n^{κ−r} factor.
- Probabilistic polymer models: unbiased non-negative estimators of weights suffice for the rejection step, provided the estimator itself obeys the decay bound.
- Coloured polymer distribution formalism recovering the exact thermal spin distribution: sample a polymer configuration, then sample spins within each polymer from μ_γ and uniformly elsewhere.
- Applications: general stoquastic systems for β ≤ 1/(2e³d³Δ), improved to β ≤ 1/(e³d²Δ) via the probabilistic representation; plus ferromagnetic and bipartite antiferromagnetic Heisenberg models with better thresholds via cycle/loop representations.

**How it works** The abstract inclusion–exclusion (cluster/polymer) expansion of Tr[e^{−βH}] over connected edge subsets yields weights w_γ = (−1)^{‖γ‖}Σ_{T⊆E(γ)}(−1)^{|T|}Tr[e^{−βΣ_{e∈T}Φ(e)}]; stoquasticity (all off-diagonal *and* diagonal matrix elements non-positive after an identity shift) makes each Taylor term non-negative, so w_γ ≥ 0 and μ_γ is a genuine distribution. Weight decay w_γ ≤ (e^β−1)^{‖γ‖} follows from a Stirling-number count of surjective edge sequences. Naive evaluation costs 2^{‖γ‖}d^{3‖γ‖}, i.e. κ = log(2d³); the probabilistic version samples an edge sequence and traces a product, reducing κ to ≈log(d²). Setting r = κ (paying a factor e^κ in β) makes the sampler O(1)-time, and Chen et al.'s O(|G|log(|G|/ε)) mixing bound plus simulated annealing give the stated runtimes.

**Why it matters** It shows that for sign-free quantum models, high-temperature classical simulation can be as fast as for classical spin systems — near-optimal in system size — and demonstrates a general recipe (positivity ⇒ probabilistic polymer weights) that others can apply to further sign-free settings. The single polymer sampler is exact, so coupling-from-the-past perfect sampling is also available.

**Caveats** The temperature threshold scales as 1/(d²Δ), so it is restrictive for large local dimension or degree; only the diagonal (computational-basis) thermal distribution is sampled, not off-diagonal observables or the state itself; counting has ε^{−2} scaling; bounded-degree graphs and, for antiferromagnetic Heisenberg, bipartiteness are required; whether the Heisenberg loop/cycle improvements extend beyond spin-1/2 or to other stoquastic families is left open, as is closing the remaining gap to the best cluster-expansion temperature thresholds.

## 2. Disassembling qLDPC codes for depth-optimal parity-check circuits

[arXiv:2608.19917](https://arxiv.org/abs/2608.19917) · [SciRate](https://scirate.com/arxiv/2608.19917)

*Minh T. P. Nguyen, Maximilian Rimbach-Russ, Stefano Bosco*

**TL;DR** Syndrome-extraction scheduling for CSS qLDPC codes is recast as an edge-coloring problem with a mod-2 "properness" (no ancilla-to-ancilla contamination) constraint, and then *reduced* by quotienting the edge symmetries that the code's own construction (hypergraph product, group lift, tensor product) imprints on the Tanner graph. Solving the tiny quotient problem and lifting back gives an analytic interleaved circuit for Lifted-Product codes of CNOT depth Δ_A + 2⌈Δ_B/2⌉ — exactly the König lower bound Δ = Δ_A + Δ_B when either factor degree is even, and Δ+1 otherwise — and, for Quantum Tanner codes, depth-optimal circuits on every tested instance up to ~600 data qubits.

**The big picture** Good quantum low-density parity-check codes promise far cheaper fault tolerance than surface codes, but each round of error detection needs a schedule of two-qubit gates that is both as short as possible and free of a subtle cross-talk effect where one check's measurement corrupts another's. Finding such schedules is a hard combinatorial problem that has so far been solved case by case or by expensive solvers on the full code. The insight here is that the best codes are not arbitrary — they are built by repeatedly combining a few small ingredient graphs, and those construction steps leave symmetries that let you solve the scheduling puzzle once on the tiny ingredient and then copy the answer everywhere. This turns a large search into an analytic recipe, with provable near-optimality for two major code families.

**Key contributions**
- A general "disassembly" framework: choose a sequence of edge partitions inverting the code's construction operations, transport the incidence and properness constraints through each quotient, solve on the reduced graph, lift back.
- For LP codes (covering hypergraph-product, two-block group-algebra, bivariate-bicycle): a closed-form **sandwich schedule** (early/middle/late bands) with proof that depth Δ is achieved unless both factor degrees are odd, in which case Δ+1 (believed optimal).
- Analogous treatment for Balanced Product codes (in SM).
- For QT codes: an algebraic reformulation in which each X/Z check overlap is confined to a row or column of the base surface; a canonical row/column **orientation** assignment (halved rows and columns with opposite orientations) that automatically satisfies properness, plus CP-SAT on the reduced base graph.

**How it works** Each Tanner edge gets a CNOT-layer label; distinct labels at shared vertices (edge coloring, König bound Δ) plus the parity condition that the number of shared data qubits touched by X before Z is even. Under the group-lift partition the group coordinate collapses; the authors then impose a *stronger*, group-independent condition (each summand vanishes individually) so the schedule works for the whole family. For LP, further identifying horizontal edges with their conjugates under the hypergraph-product partition leaves only two admissible orderings, forcing the three-band sandwich; splitting Δ_B colors evenly between the outer bands is optimal.

**Why it matters** Interleaved, contamination-free schedules of provably minimal depth directly cut idling time and cycle duration for the qLDPC families now targeted by neutral-atom and superconducting roadmaps — and the recipe is analytic, so it scales to codes where solvers time out.

**Caveats** The strengthened per-term parity condition is sufficient, not necessary, so nothing rules out shorter group-specific schedules. All-to-all connectivity is assumed and no ancilla routing/flag overhead is modeled. Optimality for QT is empirical, not proved. Crucially, depth is the only objective: circuit-level distance and hook-error structure are not evaluated — the authors explicitly defer that search to future work.

## 3. Counterexamples to the fractional coloring conjecture for triply efficient shadow tomography

[arXiv:2608.20113](https://arxiv.org/abs/2608.20113) · [SciRate](https://scirate.com/arxiv/2608.20113)

*Jędrzej Stempin, Santiago Llorens, Felix Huber*

**TL;DR** — The authors refute Conjecture 13 of King–Gosset–Kothari–Babbush (PRX Quantum 6, 010336), which claimed that the anticommutation graph of the Pauli operators with expectation value at least ε in any state has fractional chromatic number O(1/ε²). Using the complement of the 7-cycle realized by seven 3-qubit Paulis and amplifying via lexicographic graph powers, they exhibit states forcing χ_f = Ω(ε^{−2.076}); more generally, *any* graph with independence number strictly below its β (commutation index) number yields a counterexample.

**The big picture** — Measuring many Pauli observables on an unknown quantum state efficiently reduces to grouping them into commuting families, and the fractional relaxation of graph coloring quantifies how few measurement settings suffice. A recent proposal conjectured that observables with large expectation values in a fixed state automatically admit very cheap fractional colorings, which would have delivered a shadow tomography protocol efficient in samples, runtime, and copies simultaneously for arbitrary Pauli sets. This work shows that hope is false: there are states whose large-expectation Pauli sets need strictly more colorings than the conjectured budget, and the obstruction is traced to a known gap between two graph invariants that measure classical versus quantum "compatibility." The door to efficient protocols is not closed, but the proposed shortcut is.

**Key contributions**
- Explicit counterexample family: the anti-heptagon C̄₇ realized by {ZZI, ZII, IXI, XII, XZX, YZZ, YYY}, whose Hamiltonian ground state gives |Tr(ρA)| = a = (1+2√2)/7 for all seven, with χ_f = 7/2 so χ_f·a² = (9+4√2)/14 ≈ 1.0469 > 1.
- Amplification via lexicographic powers: χ_f, α, β are all multiplicative, and the product state ρ_min^{⊗K} keeps |Tr(ρ_m A)| = a^m, so χ_f·ε² ≥ 1.0469^m → ∞.
- A scaling refutation: χ_f must scale at least as Ω(ε^{−2.07598}), from s < −log(7/2)/log a.
- Theorem B: for any G, χ_f(B_ε)·ε² ≥ 0.99/(1+m log N) · (β(G)/α(G))^m, so α < β suffices; proved with a harmonic-sum threshold-selection lemma applied to the sorted squared expectation values of the β-optimal state.

**Why it matters** — β vs. α gaps are exactly the phenomenon behind quantum advantage in noncommutative constraint satisfaction; here they are shown to directly obstruct a coloring-based tomography bound. Anyone working on Pauli shadow tomography, measurement grouping for VQE-style estimation, or graph-theoretic uncertainty relations should update.

**Caveats** — The refutation only moves the exponent from 2 to ≈2.076; the authors explicitly leave open whether some O(ε^{−κ}) bound holds, which would still give sample-efficient two-copy protocols. The counterexample states are highly artificial and require many qubits (register size grows like 7^m while ε = a^m, i.e. ε is inverse-polynomially small in n), so "experimentally interesting" Pauli sets may still be well-behaved. No attempt is made to optimize the seed graph for a larger β/α ratio. The authors state that GPT "Sol 5.6" derived both main theorems, with human verification.

## 4. PPT Entanglement with Correlated Catalysis: Monotones and Irreversibility

[arXiv:2608.20063](https://arxiv.org/abs/2608.20063) · [SciRate](https://scirate.com/arxiv/2608.20063)

*Jingsong Ao, Aby Philip, Alexander Streltsov*

**TL;DR** The authors give a general, checkable criterion — based on the generalized quantum Stein lemma — under which a regularized relative-entropy resource measure is strongly superadditive, and apply it to the PPT_k hierarchy of relaxed free sets. This yields the first family of additive, strongly superadditive (hence correlated-catalytic) monotones for PPT entanglement, settles the open problem of full additivity/strong superadditivity of the regularized PPT relative entropy, and shows that arbitrary correlated catalysts cannot restore reversibility of PPT entanglement manipulation: for the Wang–Duan state, the catalytic distillable entanglement is log₂(1+1/√2) ≈ 0.772 while the catalytic cost is exactly 1.

**The big picture** Entanglement can be converted between forms, but mixed-state conversions generally lose resource irreversibly: it costs more entanglement to make a state than can be recovered from it. A natural hope is that a catalyst — an auxiliary state that is handed back intact, and which may even end up correlated with the output — restores the lost efficiency. This work builds the missing toolkit of quantities that provably cannot increase under such catalytic assistance, without needing to know anything about the catalyst, and uses it to show that irreversibility survives even in the very permissive operational setting where all partial-transpose-preserving operations are free.

**Key contributions**
- A general lemma: if a family of comparison sets is compact, convex, permutation-invariant, contains a full-rank state, and is closed under tensor products both itself and in its positive polar, then its regularized relative entropy is strongly superadditive on correlated states.
- Every finite level of the PPT_k hierarchy (k=1 being the Rains set) satisfies these conditions, giving a family of correlated-catalytic monotones for PPT — none was previously known (only squashed entanglement and CEMI exist for LOCC).
- Proof that the regularized relative entropy relative to PPT_∞ = ∩ₖ PPT_k coincides with the regularized PPT relative entropy, thereby proving the latter fully additive and strongly superadditive.
- Strong catalytic irreversibility: E_d^cc = log₂(1+1/√2) < 1 = E_c^cc for ρ_v.
- Bonus: the regularized thauma is strongly superadditive and thus a correlated-catalytic magic monotone.

**How it works** Strong superadditivity is obtained operationally: the Stein-lemma characterization turns the regularized divergence into an optimal type-II error exponent for composite hypothesis testing; taking the product of the two marginal tests preserves vanishing type-I error (union bound, no product structure needed for the null), while polar-tensor-closure makes the support function submultiplicative, so exponents add. For PPT_∞, the authors use Lami–Mele–Regula's identification lim_k χ_k(σ) = 2^{E_c,exact}(σ), giving PPT_∞ = {tσ : t ≤ 2^{−E_c,exact(σ)}}; the associated divergence is the inf-convolution min_σ [D(ρ‖σ) + E_c,exact(σ)], which is lower-bounded by D_PPT^∞ via a dilution argument using ζ_M ≥ Φ_M/M. Additivity of exact PPT cost then gives tensor closure. Irreversibility follows by sandwiching: D_{PPT_1}^∞ bounds catalytic distillation above, D_PPT^∞ bounds catalytic cost below, and both equal the known non-catalytic rates.

**Why it matters** It closes a long-standing additivity question and gives resource-theory practitioners a mechanism for generating catalytic monotones in other theories (magic is an immediate example). It also sharpens the picture of when catalysis helps: correlated catalysis is powerful enough to trivialize many finite-copy constraints, yet cannot buy asymptotic reversibility even beyond LOCC.

**Caveats** The whole edifice rests on the recently re-established generalized quantum Stein lemma and on technical tensor/polar results in companion works (some dated 2026, i.e., forthcoming). Irreversibility is demonstrated on a single explicit state, and whether the PPT_k monotones plus D_PPT^∞ are a *complete* family for catalytic PPT conversion is open, as is the probabilistic-catalytic case. The claimed faithful additive LOCC monotones from convex combinations with squashed entanglement are asserted without detailed proof. An AI-assistance disclosure is included.

## 5. Rethinking Quantum Circuits

[arXiv:2608.19370](https://arxiv.org/abs/2608.19370) · [SciRate](https://scirate.com/arxiv/2608.19370)

*Steven Rayan*

**TL;DR** These are expanded lecture notes (Niels Bohr Quantum Summer School, Odense) that read a quantum circuit in four successive registers — operational, diagrammatic, fault-tolerant, and geometric — starting from bits and Deutsch/Grover and ending at hyperbolic quantum codes and superconducting devices that emulate negatively curved lattices. The later material reports original research from the author's group, and the notes close by asking how far those device experiments actually operationalize the ZX diagrams introduced early on.

**The big picture** Different communities mean different things by "circuit": a schedule of gates, a picture that can be rewritten as a proof, a noisy history that must be protected, or a graph that must be laid out on a chip. These notes argue that all four readings are useful but must be translated into one another rather than conflated, and they make the translations explicit for an audience assumed to know linear algebra and nothing else. The payoff is a route from elementary interference arguments all the way to curved-space hardware, with a careful accounting of which claims are theorems, which are model-dependent, and which are aspirational.

**Key contributions**
- A unified four-verb framing (think / draw / correct / geometrize) with a table pairing each viewpoint's primitive object, notion of evidence, and characteristic failure mode.
- Identification of a shared "mathematical spine" across all four: composition, tensor product, adjoint/folding (the Knill–Laflamme comparison operator as a folded pair of histories), quotient, and boundary — with the boundary theme linked to Atiyah-style field-theoretic axioms for spacetime error correction.
- A clean disambiguation of ancilla counting for non-unitary processes: Julia–Halmos block dilation (one ancilla, postselected) versus Stinespring dilation (minimum environment size = ⌈log₂ rank of the Choi matrix⌉; 0 for unitary, 1 for dephasing/amplitude damping, 2 for depolarizing).
- Original research reporting on hyperbolic codes and superconducting hyperbolic lattices, plus an explicit "evidence ladder" separating demonstrated linear normal-mode spectra from prospective nonlinear, entanglement, and repeated-syndrome-extraction milestones.
- Explicit anti-conflation warnings: a normal-mode spectral gap is not a code gap; adjacency is not quantum order; a locally undetectable error is harmless only if its closed difference is a boundary, not merely closed.

**How it works** Each formalism is introduced as a response to a concrete failure of the previous one. Reversible Boolean embedding motivates unitarity and phase kickback; matrices' opacity motivates compact closed string diagrams and ZX spiders; noiseless diagrams' silence about reliability motivates Knill–Laflamme and 𝔽₂-homological surface codes viewed as diagram operations; and abstract code graphs' silence about devices motivates hyperbolic cellulations compiled into resonator lattices, where incidence becomes coupling, nontrivial cycles become logical operators, and microwave ports become boundaries.

**Why it matters** Useful as a bridging text for geometers, device physicists, and QI theorists who need a common vocabulary, and as a rare statement of the epistemic status of curved-lattice hardware claims.

**Caveats** The available source is truncated after the first lecture, so the ZX, homology, and hyperbolic sections could not be assessed directly. The devices reported demonstrate controlled *linear* spectra only; Josephson nonlinearity, entanglement measurement, holographic correlators, and repeated syndrome extraction remain explicitly prospective. Pedagogical examples (three-qubit repetition code) are deliberately non-generic.
