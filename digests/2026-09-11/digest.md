# SciRate Daily Digest — 2026-09-11

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Lifted surgery: Fast processing with QLDPC codes

[arXiv:2609.11723](https://arxiv.org/abs/2609.11723) · [SciRate](https://scirate.com/arxiv/2609.11723)

*Lucas Berent, Lawrence Z. Cohen, Armanda O. Quintavalle*

**TL;DR** The paper constructs explicit, practical auxiliary systems for *fast* (constant-round) code surgery on Abelian group-algebra QLDPC codes by restricting the surgery chain map to be linear over the group algebra itself — i.e., taking a second copy of the code as the ancilla and using module-linear maps between them. Using the canonical idempotent block decomposition of the group algebra, the space of admissible surgery maps becomes blockwise computable, and the authors find distance-preserving, weight-≤11 maps for every rank-1 and rank-2 Z-measurement on a [[90,8,10]] radial code, with circuit-level simulations showing logical performance comparable to standard surgery using 10× fewer syndrome rounds.

**The big picture** Error-corrected quantum computers built from high-rate codes can store information cheaply, but performing logical operations on that information is slow: each measurement must be repeated many times, proportional to the code distance, to protect against faulty measurements. Recent theory showed that a cleverly chosen helper code can collapse this to a constant number of repetitions, but no one knew how to build such helper codes in practice without blowing up the qubit count. This work shows that if the base code already has a group symmetry — as most leading candidate codes do — one can simply use a second copy of the code as the helper, and the symmetry reduces the search for valid couplings to a small, tractable computation. The result is fast, parallel, individually addressable logical measurements at essentially no extra space cost, which directly attacks the runtime bottleneck for slow-clock platforms like neutral atoms and trapped ions.

**Key contributions**
- Block decomposition of group-algebra chain complexes and the induced decomposition of the *lifted surgery algebra*, with an algorithm to enumerate all valid maps blockwise (kernel of a linearised commutator map over F₂).
- Full characterisation of addressability: measured logical sets must split across idempotent blocks and be G-invariant; field blocks are "fine"/"completely fine" (all submodules addressable), non-field blocks require an Ext-type liftability condition.
- Structured subfamilies: *scalar surgery* (multiplication by a ring element; closed on Koszul complexes, so the merged code is again Koszul, extending K(a,b) to K(a,b,c)), *diagonal surgery* (useful when differential entries are zero divisors), and *lifted product surgery* built from chain pairs on each tensor factor (recovering/extending the hypergraph-product scheme of Chang et al. with single-qubit addressability).
- Explicit distance-preserving instances: all rank-1/rank-2 Z-measurements on [[90,8,10]] (weight/degree ≤ 11), all rank-1 on [[198,8,16]] (≤ 14), plus two-block group-algebra examples — demonstrating that prior systolic-expansion requirements are sufficient but not necessary.
- Generalised *bridging* for joint measurements of inequivalent logicals across code blocks.
- Practical implementation: symmetry-reduced ILP gate scheduling, and decoding of dense detector matrices via sparsification plus correlated decoding.

**How it works** Surgery is framed as a mapping cone of a chain map f: D→C; fast surgery requires a degree-3 term supplying meta-checks so single-round syndrome errors are correctable. Setting D = C and demanding R-linearity, the long exact sequence identifies the measured subspace as im f∗¹ and residual logicals as ker f∗⁰ (killed by appending auxiliary X-checks). Equivalence classes of maps implementing the same measurement are then searched for low check weight and preserved distance.

**Why it matters** This is the first broadly applicable recipe for fast surgery on the bivariate-bicycle/radial/lifted-product families underlying proposed architectures, and it removes the space–time trade-off that made earlier fast-surgery constructions academic. Anyone designing QLDPC compilers or atom/ion architectures should read it.

**Caveats** No asymptotic guarantees on sparsity or distance preservation — these are verified case-by-case numerically; addressability is fundamentally limited to G-invariant, block-aligned subspaces (R-linearity cannot mix blocks or split orbits); demonstrations are small (n=90, 198, k=8) and rank-2 optimisation was done only for the smaller code; fault tolerance relies on the compacted-distance argument of Cowtan–Browne rather than a fresh proof; merged-code checks can be dense enough to need a bespoke decoding pipeline.

## 2. Sample-optimal learning of stabilizer states

[arXiv:2609.10974](https://arxiv.org/abs/2609.10974) · [SciRate](https://scirate.com/arxiv/2609.10974)

*Rebecca Chang, Matthias C. Caro, Martin Larocca, Maxwell West*

**TL;DR** The authors pin down the exact leading constant in the sample complexity of learning an unknown $n$-qubit stabilizer state: $n+\lceil\log_2(1/\delta)\rceil-3 \le L_\delta(n) \le n+\lceil\log_2(1/\delta)\rceil+4$ for $\delta<1/8$, i.e. the coefficient of $n$ is exactly 1. The upper bound is constructive via a polynomial-time ($\tilde O(n^5)$) algorithm based on Fourier analysis over $\Upsilon \cong \mathbb{Z}_4^n\times\mathbb{F}_2^{\binom n2}$, yielding as a corollary Clifford unitary learning from $2n+\lceil\log_2(1/\delta)\rceil+4$ forward queries.

**The big picture** Stabilizer states are the workhorse states of error correction and classical simulation, and it has long been known that identifying one takes a number of copies growing linearly in the number of qubits. What was not known is the precise constant in front of that linear scaling — existing protocols spent roughly two to three copies per qubit, and no matching lower bound existed. This work closes the gap to an additive constant of seven, showing that just over one copy per qubit is both necessary and sufficient, and that this optimum is reachable by an efficient algorithm. The same technique immediately gives the best known query count for identifying an unknown Clifford operation using only forward calls.

**Key contributions**
- Matching upper/lower bounds on stabilizer learning sample complexity to within an additive 7, with optimal dependence on both $n$ and $\log(1/\delta)$.
- An explicit poly-time algorithm (time $O(n(n+\log(1/\delta))^4)$) saturating the bound, a constant-factor improvement over Bell sampling ($3n$, or $2n$ with a joint sign readout, shown in an appendix).
- Clifford learning from $2n+\lceil\log_2(1/\delta)\rceil+4$ forward queries, beating Low ($2n+1$ forward *plus* $2n$ inverse) and Skaras–Ginsparg ($4n+3$); $n$-dependence proven optimal.
- A new proof template: abelian-group Fourier analysis on the geometrically uniform orbit, plausibly generalizable to other learning problems via a $G/H$ + $\mathbb{C}[H]$ two-stage decomposition.

**How it works** (i) Apply a random Clifford and non-destructively test whether the $t$-copy computational-basis support has full affine rank; this succeeds with probability $p_n>1/3$ (Lemma 2), and rank-deficient states are rejected with certainty, so failed trials can be uncomputed and retried ($r=\lceil 3\ln(40/\delta)\rceil$ trials). Full-rank states are exactly the $\Upsilon$-orbit $D_{\alpha,\beta}|+\rangle^{\otimes n}$. (ii) Compute the $\Upsilon$-character label $h(\mathbf{x})=((|\mathbf{x}_j|\bmod 4),(\mathbf{x}_j\cdot\mathbf{x}_k))$ and coherently compress each isotypic fiber $|\mathcal F_h\rangle\mapsto|0^{nt}\rangle$; this is the technical core, proved via a Witt-type extension theorem of Wood plus prefix-counting with Gauss elimination and stabilizer inner products. (iii) An inverse QFT over $\Upsilon$ returns $(\alpha,\beta)$ with probability $\ge(1-2^{1-s})^2/(1+4/(2^{s-1}-1))$ for $t=n+s$. (iv) Classical tableau reconstruction in $O(n^3)$. The lower bound uses the pretty-good-measurement formula for geometrically uniform ensembles, expressing optimal success as the squared Hellinger overlap $A(p^{(t)},u)^2$, then builds a parity-based witness $f$ with $\mathbb{E}_{p^{(t)}}f=\sqrt z$, $z=2(2^n-1)2^{-t}$, forcing $P_{\rm err}\ge\frac18\min\{1,2^{n-t}\}$.

**Why it matters** Settles a clean, long-open constant in quantum learning theory; the $O(1)$-per-qubit tomography of Clifford channels is directly relevant to benchmarking and to cloning stabilizer states with explicit constants.

**Caveats** The algorithm requires fully coherent collective measurement on all $\sim n$ copies — far more demanding than Bell sampling's 2-copy coherence; whether coefficient-one is achievable with bounded coherence is open. A constant gap of 7 remains between bounds, the lower bound needs $\delta<1/8$, and for exponentially small $\delta$ the Clifford query count can exceed Low's $4n+1$. Optimality of the compression circuit depth/ancilla count is unresolved.

## 3. Local decoders for fault-tolerant quantum computation and translation-invariant stabilizer codes

[arXiv:2609.11457](https://arxiv.org/abs/2609.11457) · [SciRate](https://scirate.com/arxiv/2609.11457)

*Nathaniel Selub, Aditya Bhardwaj, Ethan Lake*

**TL;DR** The authors build a two-dimensional fault-tolerant quantum computer in which *every* ingredient — quantum gates, classical decoding, classical communication, control — is geometrically local with constant resource density per site, the first such construction based on topological codes below four dimensions. The engine is a new cellular-automaton decoder for the surface code that uses O(1) classical bits per site, runs continuously through state injection, lattice surgery, transversal readout and gates, and preserves logical information for time stretched-exponential in distance. They additionally prove that *every* translation-invariant topological Pauli stabilizer code — including fracton codes — is locally decodable under phenomenological noise.

**The big picture** Today's roadmaps for surface-code machines quietly assume a big conventional computer off to the side, fed by ever-growing bundles of wires, doing the error-correction math fast enough to keep up. As the machine grows, that classical side grows faster than the chip can accommodate, in bandwidth, speed, and footprint. This work shows the entire error-correction job can instead be done by a uniform sheet of tiny, fixed-size classical processors sitting next to the qubits, talking only to their neighbours, while the machine performs arbitrary computations — so a logical qubit needs only one modest input/output wire, and error correction could in principle live on-chip at cryogenic temperatures.

**Key contributions**
- First local decoder for 2D topological codes with *constant* classical bits per site (prior art needed at least polylog).
- A unifying decoding principle: each defect emits three quadrant-filling "messages"; defects then march monotonically toward the bottom-left corner of their error cluster's bounding box, never leaving it, and annihilate there by charge neutrality.
- Rigorous thresholds: code capacity gives logical error O((p/p\*)^{L^α}) with average decoding time O(log^η L); phenomenological noise gives failure probability T·O((p/p\*′)^{L^{α′}}). Numerical threshold ≈1.1% for the translation-invariant streaming surface-code decoder under bit-flip + measurement noise.
- A complete Clifford+T architecture: a line of *folded* surface-code patches (fold-transversal H avoids patch rotation), lattice-surgery CNOTs, magic- and Y-state distillation, with injection proven to give O(p) logical error; plus a proof that constant-density bounded-bandwidth wiring suffices.
- Proof that all translation-invariant topological Pauli stabilizer codes admit local decoders — the first local decoders for fracton codes, despite immobile excitations.

**How it works** Cluster-decomposition/renormalization arguments (Gács–Harrington style) show errors organize into well-separated clusters at every scale; the corner-attraction rule provably resolves each cluster within its own bounding box in parallel, so no global information is needed. Phenomenological decoders are *streaming* (process syndromes on arrival, no windows), using poly(log log L) bits/site translation-invariantly, or O(1) bits/site hierarchically at the cost of translation invariance. Code-capacity versions also run asynchronously via a local Lindbladian using marching-soldiers synchronization.

**Why it matters** This closes a conceptual gap — whether the *classical* infrastructure of fault tolerance can itself be scalable — and could substantially cut wiring and latency overhead for superconducting and quantum-dot platforms. It also broadens the class of quantum memories known to support stable non-equilibrium phases.

**Caveats** Classical hardware is assumed noiseless throughout; the phenomenological constructions are synchronous discrete-time (asynchronous extension only conjectured); circuit-level noise is handled only by appeal to standard reductions. The 1.1% threshold is below global matching decoders, memory time is stretched-exponential rather than exponential, and the exponents α, α′ are not optimized. The constant-density streaming decoder sacrifices translation invariance, and the general-code result does not yet yield constant density.

## 4. Strong Converse for Quantum Capacity via a Fully Quantum Blowing-Up Lemma

[arXiv:2609.11771](https://arxiv.org/abs/2609.11771) · [SciRate](https://scirate.com/arxiv/2609.11771)

*Salman Beigi, Marco Tomamichel*

We prove an exponential strong converse for quantum communication through every finite-dimensional memoryless channel: at any fixed rate above the quantum capacity, the entanglement-transmission fidelity of every code decays exponentially with the number of channel uses. The proof has two main ingredients. First, a fully quantum blowing-up lemma converts a low-fidelity code into a high-fidelity code, with a loss in the number of transmitted qubits controlled by the projective tensor norm of the orthogonal projection on the image of the Stinespring dilation of the channel across the receiver--environment bipartition. Second, a low-degree polynomial construction approximates the tensor power of this projector with exponential accuracy while controlling its projective norm, providing the approximation needed for the blowing-up argument.

## 5. A Near-Quartic Separation Between Certificate Complexity and Quantum Query Complexity

[arXiv:2609.11664](https://arxiv.org/abs/2609.11664) · [SciRate](https://scirate.com/arxiv/2609.11664)

*Andris Ambainis, Jānis Iraids, Martins Kokainis*

**TL;DR** The authors build a total Boolean function on Θ(n³ log² n) bits with certificate complexity C ≥ n(⌈n/2⌉+1) = Ω(n²) and bounded-error quantum query complexity Q = O(√n log³ n), i.e. Q = Õ(C^{1/4}). Since C = O(Q⁴) holds for all total functions, this pins down the optimal exponent at 4 (previously only known to lie in [2,4], with OR giving the quadratic lower end). The new ingredient over prior approximate-degree separations is an actual quantum algorithm, built from variable-time search for a source in a tournament on input blocks.

**The big picture** Certificate complexity — how many input positions you must reveal to convince someone of the answer — is one of the basic combinatorial handles on Boolean functions, and it controls how deterministic, randomized and quantum query costs relate to one another. It has been known for decades that a quantum algorithm can be at most a fourth-power faster than the certificate size, but the best known example only achieved a square. This work exhibits a function where the fourth power is essentially achieved, closing the gap up to logarithmic factors and completing one of the last missing entries in the table of maximal separations between query and combinatorial complexity measures for total functions.

**Key contributions**
- A total function with a near-quartic certificate-versus-quantum-query separation, tight up to polylogs.
- A redesign of Pabbaraju's DNF-based partial function: pairwise bijections between blocks are replaced by *n* fixed position lists, chosen probabilistically so that the total prefix length bound ∑ⱼ mⱼ(S) ≤ 8n holds *simultaneously* for every S with |S| ≥ n/3 (exponential-moment Markov bound with base 5/4, plus a union bound over 2ⁿ sets).
- A quantum algorithm for the underlying partial function using O(√n log² n) queries, via variable-time search applied to source-finding in an input-defined tournament.
- A compact cheat-sheet certificate-description format (prefix-count fields, cumulative prefix lengths) yielding O(n) checks of O(log n) queries each.

**How it works** Each input is n blocks of n bits; a satisfied unambiguous DNF term (i,S) designates a block, and the partial function H returns ⋁_{p∈S} y_i(p). Comparing first-hit indices m_{ij} vs m_{ji} orients a complete digraph whose unique source is the designated block. A Bernoulli sampling test with s_n = O(log n) positions per block classifies blocks dense/sparse, guaranteeing (w.p. ≥ 11/12) that comparisons only occur between blocks with >n/3 ones, so the prefix-sum lemma applies and gives max_i ∑_j θ_{ij}² = O(n log n) for comparison costs θ_{ij} = ⌈c₀√(Δ_{ij} log n)⌉. FindSource maintains a list W and repeatedly runs Ambainis–Kokainis–Vihrovs variable-time search over candidates U(W); martingale-style estimates give E[R] = O(log n) rounds and E∑_v t_v(W_end)² = O(n log² n), fixing T₂ = Θ(√n log n). Cheat-sheet totalization plus robust address recovery (O(r) uses of the H-circuit, r = Θ(log n)) yields Q(F_n) = O(rT_H + √(nr) log n).

**Why it matters** Settles a longstanding open question and confirms that certificate complexity cannot be used to prove anything better than D = O(Q⁴)-type relations through this route. Relevant to anyone working on query-complexity measure separations, cheat-sheet constructions, or variable-time quantum search.

**Caveats** Polylogarithmic slack remains (log³ n in Q). The position lists are obtained nonconstructively by the probabilistic method, so the function is not fully explicit. The function is a highly engineered cheat-sheet gadget with no independent interest; the technique says nothing directly about R vs C or D vs R. Most supporting lemmas (membership-circuit implementation, candidate-set estimates, classification test) live in appendices that are truncated here.
