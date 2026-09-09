# SciRate Daily Digest — 2026-09-09

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Quantum lower bounds for convex optimization and real matrix-vector query problems

[arXiv:2609.05679](https://arxiv.org/abs/2609.05679) · [SciRate](https://scirate.com/arxiv/2609.05679)

*Andrew M. Childs*

**TL;DR** This paper introduces the *determinantal witness method*, a quantum lower bound technique for continuous (real matrix-vector) query problems, and uses it to prove that quantum convex optimization with evaluation and membership oracles requires Ω̃(n) queries — matching the known Õ(n) quantum algorithm and capping the quantum speedup over the Õ(n²) classical bound at quadratic. Along the way it gives Ω(n/log n) bounds for computing the trace, |det|, and a column of the inverse, and Ω(n) for the sign of the determinant, in the matrix-vector query model.

**The big picture** Quantum algorithms were known to solve general convex optimization with roughly a square-root fewer oracle calls than the best classical methods, but the best matching lower bound was much weaker, leaving open the possibility of a far larger quantum advantage. Proving lower bounds here was blocked by the fact that the standard polynomial method is built for discrete inputs, whereas these problems have continuous, real-valued inputs. The paper supplies a new technique tailored to continuous linear-algebraic queries — replacing polynomial degree with matrix rank, and orthogonality to low-degree polynomials with a measure whose Fourier transform vanishes on low-rank inputs. The upshot is that the existing quantum optimization algorithms are essentially optimal, and the speedup over classical methods is at most quadratic even when gradients are available for free.

**Key contributions**
- Structural lemma: any measurement probability of a t-query algorithm with phase oracle e^{2πi yᵀAx} is the Fourier transform of an A-independent complex measure supported on matrices of rank ≤ 2t.
- Dual-witness framework (Lemma 3): a measure ξ = ξ₀+ξ₁ with ξ̂ vanishing on rank ≤ 2t and good correlation with the target Boolean function lower-bounds failure probability by (|∫D dξ| − ‖ξ₁‖₁)/‖ξ₀‖₁.
- Explicit witness construction via the Cayley operator det(∂_X) applied to Schwartz functions: Fourier transform picks up det(M), hence vanishes on rank ≤ n−1; minors give lower rank thresholds.
- Concrete bounds: trace Ω(n/log n); sign(det) Ω(n) (constant-gap, no log loss); |det| Ω(n/log n); first column of A⁻¹ to inverse-polynomial accuracy Ω(n/log n), extended to positive definite matrices and hence to constrained convex optimization over the unit ball.

**How it works** For the trace, a product-of-bumps witness kills all non-identity permutations, leaving a central binomial correlation ~1/√n. For the determinant, taking b = Gaussian density gives β ∝ det(X)γ(X), whose correlation with sign(det) is ½E|det A|. For |det|, the squared Cayley operator yields q(X) = det(∂_X − X)²1 = det(X)² + lower order, and Cayley's identity gives E[q²] = E[q·det²] = (n+1)!n!, with a Cauchy–Schwarz/threshold-averaging argument producing correlation Ω(n^{−9/2}) — boosting converts the tiny gap to Ω(n/log n). Inversion uses a Schur-complement block structure, a minor-based witness on the interior block, the Capelli identity plus Gaussian integration by parts (with care about singular matrices), and Gaussian random-matrix estimates.

**Why it matters** It closes a longstanding gap in quantum convex optimization and resolves several open questions from prior work on matrix-vector queries over finite fields, now over the reals. The technique itself — a rank-analogue of the dual polynomial — may transfer to other continuous-input query problems.

**Caveats** Hardness of optimization is shown only for very small error, O(n⁻⁴⁹); the determinant-magnitude bound is for an unspecified n-dependent additive error; several bounds lose a log factor to boosting; and rank testing over the reals remains open.

## 2. Computing 256-bit elliptic curve discrete logarithms in 26 days on a fault-tolerant trapped-ion quantum computer with 20,000 qubits

[arXiv:2609.05625](https://arxiv.org/abs/2609.05625) · [SciRate](https://scirate.com/arxiv/2609.05625)

*Thomas Häner, Felix Tripier, Jacob Young, Michael Naehrig, Andrii Maksymov, Safwan Alam, Dmitri Maslov, Matthew Parrott et al.*

**TL;DR** IonQ presents an end-to-end, architecture-specific resource estimate for solving the 256-bit ECDLP on `secp256k1` (Bitcoin's curve) with Shor's algorithm: ~1450 logical qubits and ~40 million Toffolis, compiled down to measurement schedules on their "Walking Cat" trapped-ion architecture, yielding 19,397 physical qubits and 25.7 days of runtime at ~63% success. The headline enablers are a fast CCZ magic-state factory with depth-one injection (31× faster CCZ execution), CliNR-accelerated Cliffords, parallel non-overlapping cat measurements, and a cheaper loss-correction protocol — plus a rigorous, confidence-bounded failure analysis of the approximate modular arithmetic.

**The big picture** Estimates of the quantum resources needed to break elliptic-curve cryptography have historically been dominated by surface-code overheads on superconducting hardware, giving figures in the millions of physical qubits and long runtimes. This work argues that a trapped-ion machine with low physical error rates, all-to-all connectivity, and application-tailored compilation could get the physical qubit count down to roughly twenty thousand while keeping the runtime under a month. Just as important, the authors do not stop at logical gate counts: they compile every component into hardware-legal schedules and prove — rather than assume — that the aggressively approximated arithmetic circuits still let the algorithm succeed. For anyone tracking migration timelines for elliptic-curve cryptography, this shifts where the hardware bar sits.

**Key contributions**
- Full compilation of an optimized version of Schrottenloher's point-addition circuits to physical measurement schedules obeying architectural constraints, with manual layout and integrated routing.
- An "Eastinthillation" CCZ factory: Eastin synthillation applied to eight T states from zero-level distillation in the [[6,2,2]] code, giving 555.75 POCs average depth per accepted state, ~15.9% restart rate, logical error ≲9.4×10⁻¹⁰, 319 physical qubits per factory (4 factories sustain the stream).
- A rigorous failure-probability analysis of approximate arithmetic, valid with confidence ≥1−2⁻¹²⁸.
- Overhead reductions: improved loss correction, CliNR ancilla recycling, cat-state provisioning matched to peak measurement parallelism.

**How it works** Double-scalar multiplication uses 16-bit windows over masked lookup tables with a random initial point offset, which eliminates controlled-on-zero logic and makes exceptional-case probability negligible (<2⁻²⁴⁸). Arithmetic exploits the pseudo-Mersenne prime 2²⁵⁶−c: comparisons are replaced by top-bit inspection, carries truncated at 65 bits, phase-repair comparisons at 32 bits. The authors count failing inputs exactly for addition/subtraction/negation/square-subtraction (per-operation failure ~2⁻²⁶ to 2⁻³⁰) and bound the binary-gcd in-place multiplication/division by Monte Carlo (21 failures in 10⁶ samples → Clopper–Pearson bound 1.49×10⁻⁴). A change-of-measure argument (at most four curve-point pairs per coordinate-difference pair) transfers uniform-input bounds to circuit-realistic inputs, giving per-point-addition failure ≤1.2×10⁻³ and total ≤3.35×10⁻², with success degrading as (√P₀ − 2p_f)².

**Why it matters** This is the most hardware-concrete ion-trap estimate for a cryptographically relevant Shor instance, and it makes the failure analysis auditable rather than heuristic — a gap in essentially all prior work (including a missed fourth exceptional case in Roetteler et al.).

**Caveats** Everything rests on the Walking Cat architecture's assumed physical error, transport, and cat-measurement parameters from a companion paper; no such machine exists. The gcd-circuit bound is empirical, not proved. Several arguments (e.g., r−1 < p) are specific to `secp256k1`. Runtime assumes continuous operation with no calibration or drift overhead, and 63% is a single-run success probability.

## 3. No information transmission through quantum channels above capacity

[arXiv:2609.08998](https://arxiv.org/abs/2609.08998) · [SciRate](https://scirate.com/arxiv/2609.08998)

*Hao-Chung Cheng, Marco Tomamichel*

**TL;DR** The authors prove exponential strong converses for both unassisted quantum (entanglement-generation) and classical communication over arbitrary finite-dimensional memoryless quantum channels: above the (regularized) capacity, fidelity and success probability decay exponentially in the number of channel uses. The technical key is showing that the regularized sandwiched Rényi capacities converge to the ordinary capacities as the Rényi order tends to one, established via new integral representations of Rényi coherent information and Rényi Holevo quantity plus a Leung–Smith telescoping/continuity argument.

**The big picture** For classical channels it has long been known that the capacity is a sharp threshold: below it errors vanish, above it they are forced to one. For quantum channels, the analogous statement had resisted proof in general — the capacity formulas require regularization over many channel uses, and existing arguments only covered special channel families (degradable, entanglement-breaking, dephasing) or assisted settings. This work closes the general case, showing that quantum channel capacity is a genuine phase transition point rather than merely a boundary beyond which vanishing error is impossible; attempting to communicate above capacity fails catastrophically, not partially. That legitimizes capacity as the operationally meaningful limit even for users willing to tolerate large error.

**Key contributions**
- Integral representations expressing the order-α sandwiched Rényi coherent information and Rényi Holevo quantity as averages, over a tilt parameter u ∈ [0, s_α] with s_α = (α−1)/α, of ordinary entropy differences H(B)−H(E) and mutual information I(X:B) on "tilted" states.
- Uniform (dimension-local) bounds showing tilted states violate the per-use Stinespring support constraint by only O(u²) — explicitly ≤ 2u²(√dim B + (dim B)^{u/2}√dim E)² — independent of block length, input correlations, and ensemble size.
- Asymptotic continuity of the regularized Rényi capacities at α → 1 for both quantum and classical communication, with an explicit finite-block continuity modulus.
- Exact strong-converse exponent formulas, E_sc = sup_{α>1} (α−1)/α · [r − Rényi capacity of order α], including a previously missing achievability proof for entanglement generation.

**How it works** The Arimoto route gives, for any α>1, F_eg ≤ 2^{−n(α−1)/α[r − Q̃_α]}, so one needs a *fixed* α>1 with Q̃_α below the rate — per-block continuity is insufficient since the required α could drift to one. Using Hayashi–Tomamichel's envelope/fixed-point results, the derivative in s of the optimized Rényi conditional entropy equals H(B)−H(E) of a tilted state whose marginals are exactly the optimizing operators; integrating gives the representation. Tilted states need not live in the Stinespring image, so the authors project system pairs B_iE_i back one channel use at a time, replacing the rejected weight; each step changes the state by trace distance δ = O(α−1), and conditional-entropy continuity bounds the entropy change using only dim B_i. Summing telescopically yields a correction linear in n whose per-use value vanishes as α ↘ 1.

**Why it matters** This settles a long-standing open problem in quantum Shannon theory and completes the sharp coding transition picture, matching known error exponents below capacity. The integral-representation-plus-local-repair technique is likely reusable for other regularized Rényi quantities and converse problems.

**Caveats** The exponent formulas remain regularized and hence not computable for nonadditive channels; evaluating them concretely is left open. Nothing is asserted exactly at rate equal to capacity. Results are restricted to finite dimensions, memoryless channels, unassisted codes; quantum statements are phrased for entanglement-generation fidelity (other criteria follow up to a factor of two). The continuity modulus, while explicit, is presumably far from tight, and the source here is truncated before the full projection/continuity proofs, which merit careful independent checking.

## 4. Low-Depth Random Unitaries without Ancillae

[arXiv:2609.06528](https://arxiv.org/abs/2609.06528) · [SciRate](https://scirate.com/arxiv/2609.06528)

*Zhenyu Du, Siyuan Cheng, Xiongfeng Ma*

**TL;DR** The authors construct multiplicative-error approximate unitary $k$-designs on $n$ qubits with *zero* ancillae at depth $\widetilde O(k)(\log(n/\epsilon))^{1/\delta}$ on $\delta$-dimensional lattices and $\widetilde O(k)\log\log(n/\epsilon)$ with all-to-all connectivity — optimal in $n$, near-optimal in $k$, matching prior ancilla-heavy constructions that needed $\omega(n)$ (sometimes $kn\cdot\widetilde O(\log\log n)$) extra qubits. A general "exactification" lemma then converts any sufficiently accurate ensemble into an *exact* $k$-design by classical reweighting alone, giving ancilla-free exact designs at depth $O(n^{1/\delta}k\log^2 k)$ and $O(k\log k(\log n+\log k))$ — an exponential gate-count improvement over prior exact constructions.

**The big picture** Random quantum circuits that mimic truly random dynamics up to a fixed number of statistical moments underpin shadow tomography, randomized benchmarking, metrology readout, and studies of scrambling. Recent breakthroughs made such circuits extremely shallow, but only by borrowing large numbers of fresh helper qubits — often more than the system itself — which is a fatal cost on real devices and an unsatisfying theoretical accounting. This work removes the helper qubits entirely while keeping the optimal shallowness, by having the circuit recycle its own idle qubits as scratch space and restore them exactly. It also shows that a shallow circuit whose randomness is merely very good can be turned into perfectly random behaviour just by tweaking how often each circuit is drawn, with no change to the quantum hardware.

**Key contributions**
- A sharpened moment bound for the Hadamard–diagonal ensemble: TPE error $\le 9r^4/2^m$ for $r\le 2^{O(m)}$, replacing a previous factorial-in-$r$ dependence. Proof lifts the projector product to a symmetric-group block matrix, bounds off-diagonal blocks by $d^{-\ell(p)/2}$ via $\mathbb F_2$ rank counting, and identifies the rank-$r!$ Haar sector by singular-value variational arguments.
- Replacement of $2^m$ ideal random phases by $s=\Theta(m)$ hashed phases, reducing the moment-matching condition to a randomized multiset-equality (hash-sum) test with error $\exp(-\Omega(m/\log k))$.
- Ancilla-free implementation via *catalytic computation*: idle system registers serve as dirty workspace, with a dedicated compiler for catalytic composition of the arithmetic.
- Architecture-tailored hashing: random $\mathbb F_{2^s}$ polynomials ($\lambda_a z$, $\mu_0z+\mu_1z^2+\mu_2z^4$) for $\delta$-D depth $O(m^{1/\delta})$; constant-rate/distance linear codes with $O(\log m)$-depth catalytic XOR networks for all-to-all. A quadratic layer ($w=\Theta(\log k)$ random bit products) supplies the needed nonlinearity.
- Exactification lemma: $\max\{\lambda_k,\lambda_{2k}\}\le 1/(32d^{4k})$ implies a reweighting $\omega(U)\in[3/4,5/4]$ yielding an exact $k$-design (hence also an exact *strong* $k$-design).

**Why it matters** Space–time cost is now simultaneously optimal for design generation across all finite-dimensional and all-to-all architectures, tightening resource estimates for classical shadows, thrifty shadow estimation, higher-order randomized benchmarking, and nonlinear-observable protocols. It also extends the recently reported complexity-driven Fisher-information transition to closed, ancilla-free systems.

**Caveats** Sampling the exactified distribution takes exponential classical time — the exact designs are quantumly but not classically efficient. Guarantees are for multiplicative error and $\widetilde O(k)$ hides logs; the $n$- and $k$-dependences remain multiplicatively coupled (unlike the decoupled 1D result of Liu et al.). Non-Clifford/magic cost and depth for physically natural brickwork circuits are untouched; the catalytic scheme needs a constant number of registers of size $\Theta(\log nk)$, so small-$n$ regimes and the $m=O(\log k)$ regime are handled separately (random Pauli rotations).

## 5. From Bits to Qubits: The Theory and Practice of Quantum Data Encoding

[arXiv:2609.08058](https://arxiv.org/abs/2609.08058) · [SciRate](https://scirate.com/arxiv/2609.08058)

*Xiao-Ming Zhang, Arthur G. Rattew, Bujiao Wu, Georgios Styliaris, Xiaoming Sun, Bálint Koczor, Xiao Yuan*

**TL;DR** A comprehensive review (RMP-style) of how classical data gets loaded into quantum computers, unifying the four dominant access models — state preparation, unitary synthesis, QRAM, and block encoding — with their circuit-size/depth/ancilla and non-Clifford resource tradeoffs, plus dedicated treatments of structured data (sparse vectors, Boolean functions, tensor-network states). Its most opinionated contribution is a refined resource taxonomy for quantum memory based on *per-query opportunity cost* (active / weakly passive / strongly passive / quantum-passive classical-active / "practically passive"), which sharpens exactly when data loading destroys the speedup it was meant to enable.

**The big picture** Almost every quantum algorithm that claims to beat classical computing on real-world data must first get that data into the machine, and this step is frequently more expensive than the computation itself. This review consolidates two decades of scattered results — from amplitude-encoding circuits to lookup tables used in chemistry and cryptanalysis resource estimates — into a single accounting framework, and argues that the right currency is not runtime but the total physical resources (energy, control electronics, classical co-processing, error correction) consumed per memory access, because those same resources could have run a parallel classical algorithm instead. It then maps which loading problems are genuinely cheap: data with structure, such as sparsity, low entanglement, or a compact functional description. The upshot is a checklist for anyone claiming end-to-end quantum advantage on classical data.

**Key contributions**
- A unified survey of encoding models with explicit space–time tradeoffs and fault-tolerance (T/Toffoli) costs, not just asymptotic gate counts.
- Extension of the active/passive QRAM dichotomy into a finer taxonomy, including "weakly passive" ($o(N)$ but super-polylog), "quantum-passive classical-active," and "practically passive" (asymptotically active but with DRAM-comparable constants).
- Clarification of overloaded terminology (QRACM/QRAQM/CRAQM, QROM vs. QROAM vs. qLUT, SWAP-QRAQM = QRAG), and the memory-vs-compute-region split now appearing in high-rate-code architectures.
- A list of open challenges, e.g. whether a strongly passive QRAM is fundamentally impossible, and why a rigorous no-go must formally penalize absurd one-time precomputation ($\tilde O(2^{n(n-1)/2})$ unrolled correction tables).

**How it works** The review threads a resource-accounting argument through concrete constructions: fan-out circuit QRAM ($O(\log^2 N)$ depth, $O(N)$ parallel gates, $O(N\log N)$ qubits, reducible to $O(\log N)$ depth); unary iteration (T-count $4N-4$ vs. $6N-4$ for naive SELECT); QROAM's $O(\sqrt N)$ T-count against the $\tilde\Omega(N)$ total-gate lower bound; bucket-brigade's exponentially decaying router entanglement, which yields polylog error scaling per query but still forces physical error rates $o(1/\sqrt N)$ for search-type algorithms. It highlights the adaptive distillation–teleportation protocol that evades the $d=\Omega(\sqrt N)$ teleportation no-go by classically rewriting the table between $n$ rounds, achieving polylog quantum but $\tilde O(N)$ classical cost with $\Omega(2^{n/2}/\mathrm{poly}(n))$ wire density. Structured-data sections cover sparse state preparation, Boolean-function oracles, and compiling MPS/PEPS/TTN/MERA into circuits.

**Why it matters** Dequantization results already removed many claimed exponential speedups; opportunity-cost arguments threaten remaining polynomial ones for QSVT-based linear algebra on unstructured data. Anyone doing resource estimation, QRAM hardware design, or quantum machine learning should read the memory taxonomy before quoting query complexities.

**Caveats** The central lower bounds are imported from prior work and inherit its assumptions — the $\tilde\Omega(N)$ gate bound does not cover dynamic/measurement-conditioned circuits (conjectured but unproven), and the teleportation no-go assumes data-independent purification channels. "Practically passive" is defined by comparison to DRAM specifications rather than by a clean model, and the review is a synthesis, not new technical results.
