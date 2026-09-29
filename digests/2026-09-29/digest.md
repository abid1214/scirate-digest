# SciRate Daily Digest — 2026-09-29

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. An Optimal Quantum Linear Systems Algorithm

[arXiv:2609.35660](https://arxiv.org/abs/2609.35660) · [SciRate](https://scirate.com/arxiv/2609.35660)

*Carlos Bravo-Prieto, Aram W. Harrow, Robin Kothari*

**TL;DR** The query complexity of the quantum linear systems problem in the sparse-access model is pinned down exactly as Θ(κ√d log(1/ε)), closing the gap between the two incomparable prior algorithms (O(κd log 1/ε) and κ√d(κd/ε)^{o(1)}) and the two partial lower bounds. The key algorithmic ingredient is an O(1)-query *exact* block encoding of an enlarged system whose inverse has norm O(κ√d); as a corollary, any N×N unitary can be implemented from entry queries with O(√N log(1/ε)) queries, resolving an open question of Berry and Childs.

**The big picture** Solving linear systems on a quantum computer is one of the oldest and most-cited quantum primitives, but for fifteen years nobody knew how its cost should scale jointly in the three natural parameters: how ill-conditioned the matrix is, how many nonzeros each row has, and how accurate the answer must be. Two separate algorithms each got two of the three parameters right, and two separate lower bounds each captured part of the hardness. This work shows that the true cost is exactly the product of all three contributions, via a new way of feeding a sparse matrix to a solver that avoids an internal search bottleneck, plus a lower bound showing that search hardness and history-state decay genuinely multiply. A striking side benefit is an optimal method for turning a table of a unitary's matrix entries into a circuit implementing it.

**Key contributions**
- Matching upper and lower bounds Θ(κ√d log(1/ε)) for sparse-access QLSP.
- An exact, unit-normalization block encoding of an enlarged matrix M with ‖M‖≤1, ‖M⁻¹‖≤5κ√d, whose inverse contains √d·A⁻¹, using O(1) queries.
- A constant-normalization (O(1),η) block encoding of any d-sparse Hermitian H with O(√d log(1/η)) queries.
- O(√N log(1/ε)) black-box unitary implementation, improving O(N^{1/2+o(1)}) and matching the Ω(√N) search bound.

**How it works** Upper bound: the standard construction writes A/√d = F†T, but implementing F itself encodes unstructured search (Ω(√d)). Instead, the product is split with an auxiliary vector (Tu = z, F†z = b), giving an N²+N-variable system L on only 2n+1 qubits with ‖L‖‖L⁻¹‖ = O(κ√d). Crucially, the enlarged system lets each state |ψ_ij⟩ = (|z⟩ + √d A_ij|r⟩)|i,j⟩ be normalized *individually* by q_ij = √(1+d|A_ij|²), yielding M = L·diag(Q⁻¹,I). The key lemma is ‖QT‖ ≤ √2 (columns of QT have disjoint support and column norms of A are ≤1), so readout of the bottom block succeeds with probability ≥1/3 and ‖M⁻¹‖ = O(κ√d). Then Costa et al.'s O(κ log 1/ε) block-encoded solver applies. Lower bound: a cyclic clock unitary (compute, idle, uncompute) whose A = (I−αU)/2 with α = 1−2/κ has ‖A⁻¹‖ ≤ κ and whose solution is a geometrically weighted history state; the idle window carries the circuit output with probability ≥ α^{4L}/3 ≳ √ε. Embedding XOR_R ∘ LR_D with R = Θ(κ log 1/ε), D = Θ(d), and invoking the Lee–Roland quantum XOR lemma converts the exponentially small advantage c^R into Ω(R√D).

**Why it matters** It settles the complexity of a benchmark primitive and, more practically, the √d-query constant-normalization sparse block encoding is a drop-in improvement for any QSVT-based algorithm where the α = d normalization currently costs a factor of √d in condition number or simulation time.

**Caveats** Only query complexity is analyzed; gate/ancilla overheads (the enlarged register, controlled rotations) are not tabulated, and the 1/ε-independent claim for the black-box unitary hides a log(1/ε). Lower bounds hold asymptotically for sufficiently large κ, d, 1/ε and rely on a promise-problem instance family; the upper bound uses Costa et al. as a black box and assumes known κ and Hermitian A (via dilation). A concurrent independent derivation of the same lower bound exists.

## 2. Optimal Quantum Algorithms for Ordered Search

[arXiv:2609.34293](https://arxiv.org/abs/2609.34293) · [SciRate](https://scirate.com/arxiv/2609.34293)

*Joseph Carolan, Andrew M. Childs*

**TL;DR** Two new quantum algorithms solve ordered search with $\frac{1}{\pi}\ln n + o(\log n)$ comparison queries, matching the Høyer–Neerbek–Shi adversary lower bound $\frac{1}{\pi}(\ln n - 1)$ to leading order. This pins the quantum query complexity at $\approx 0.221\log_2 n$ — a speedup factor of exactly $\pi\log_2 e\approx 4.53$ over binary search — closing a problem open since 1998 and confirming the adversary bound is tight here.

**The big picture** Finding an item in a sorted list is the textbook example of a problem where quantum computers help only by a constant factor, and for a quarter century nobody knew what that constant was. Progress had stalled because every good algorithm came from numerically optimizing one small fixed-size instance and then recursing, an approach that cannot converge to the true constant and that was already straining computational limits. The new work replaces numerics with closed-form analysis, producing algorithms whose query count provably meets the best known lower bound, so the optimal speedup factor is now known exactly. It also settles a long-standing speculation that the adversary method, rather than being loose here, gives the right answer.

**Key contributions**
- A simple zero-error continuum algorithm with expected cost $\frac{1}{\pi}\ln n + O((\ln n)^{3/4})$.
- An exact (worst-case, zero-error-with-certainty) algorithm via an analytic solution path for the Farhi–Goldstone–Gutmann–Sipser polynomial program.
- Consequently $Q_E(\mathrm{OSP}_n)=\frac{1}{\pi}\ln n + o(\log n)$; the adversary bound is tight, as conjectured by Childs–Lee.

**How it works** *Continuum algorithm:* work in $L^2(\mathbb{R})$; the oracle becomes a sign flip at the unknown transition point, implementable with one discrete query by computing/uncomputing the floor. Prepare a log-Gaussian packet centered at $\ln n + \ln^{3/4}n$ with log-width $\ln^{1/2}n$, then iterate $U_s=\mathcal{F}^\dagger O_0\mathcal{F}\,O_s$ — the unique nontrivial translation- and scale-invariant driver. On the even subspace the Mellin multiplier is $\tanh(\pi\omega)-i\,\mathrm{sech}(\pi\omega)$, with phase $\pi/2-\pi\omega+O(\omega^3)$: each query translates the packet by $\pi$ leftward in log-position, with cumulative error $O(t/w^3)$. Measure position after $\approx\frac{1}{\pi}\ln n$ steps; verify classically and repeat.

*Exact algorithm:* a one-parameter family of Laurent polynomials with coefficients $\sinh(\lambda(1-j/n))/\sinh\lambda$, nonnegative because it equals $\frac{1-r^2}{1-r^{2n}}|p_r(z)|^2$ with $r=e^{-\lambda/n}$, interpolates Fejér kernel ($\lambda=0$) to $1$ ($\lambda=\infty$). Since parity constraints allow only one reversal-component to move per query, a greedy rule pushes the symmetric/antisymmetric rates alternately as far as nonnegativity permits. Using compactly supported log-rate mixtures with quartically decaying edges and a determinant/periodization criterion, the log-rate advances by any $d<\pi$ per step; two final queries land exactly on $1$ once rates exceed $2n$.

**Why it matters** A canonical open constant is now determined, and the techniques — continuum/Mellin scale-invariance and analytic paths through nonnegative-polynomial cones — are plausible tools for other query problems where numerics-plus-recursion has plateaued.

**Caveats** Lower-order terms remain open ($O(1)$ vs. $o(\log n)$); the error-dependent constant for bounded-error algorithms is unresolved. Time complexity is unoptimized, with the exact algorithm requiring Fejér–Riesz factorizations. No concrete small-$n$ algorithms are extracted for comparison with prior numerical records.

## 3. From Simple Sources to Quantum Advantage: Homomorphic Polynomial Transduction via Relative Decoding

[arXiv:2609.35101](https://arxiv.org/abs/2609.35101) · [SciRate](https://scirate.com/arxiv/2609.35101)

*Zhong-Xia Shang, Daniel Stilck França*

**TL;DR** The paper reframes decoded quantum interferometry (DQI) and its Hamiltonian version as *polynomial transduction*: pushing an operator state of a degree-$D$ polynomial from an easy "source" algebra to a hard "target" algebra along a unital $*$-homomorphism $\pi$. The key new quantity is a *relative distance* $d_{\mathrm{rel}}$ — the lowest word degree at which source and target normalized traces disagree — with the sharp criterion that $2D<d_{\mathrm{rel}}$ is *equivalent* to exact preservation of all degree-$D$ operator inner products; since $d_{\mathrm{rel}}\ge d_{\mathrm{ord}}$, relative decoding can support filter degrees that ordinary DQI-style decoding cannot.

**The big picture** A family of recent quantum optimization algorithms works by building a state whose amplitudes are a polynomial filter of an objective function, using classical decoding inside the quantum circuit to clean up bookkeeping. This work shows that all of these are instances of one operator-algebraic primitive: prepare the polynomial in a simpler system that shares the same algebraic relations, then coherently carry it over to the hard system. Crucially, the decoder only needs to recover the operator, not which particular product of terms produced it, so relations already present in the simple system come for free — which relaxes the distance requirement that previously bottlenecked how sharp the filter could be.

**Key contributions**
- Intrinsic definition of $d_{\mathrm{rel}}$ and an if-and-only-if degree criterion ($2D<d_{\mathrm{rel}}$) for isometric transduction on the degree-$D$ filtration.
- Proof that $d_{\mathrm{rel}}\ge d_{\mathrm{ord}}$, with strictness exactly when all minimum-length target scalar-word relations are inherited; Pauli version: $d_{\mathrm{rel}}=\min\{|c|:c\in K_B\setminus K_A\}$ for relation codes $K_A\subseteq K_B$.
- Explicit families with $d_{\mathrm{ord}}=O(1)$ but $d_{\mathrm{rel}}=\Theta(n)$ plus efficient decoders.
- Modularization: pilot-state construction (with its multiplicities and commutation phases) is replaced by preparing a *source polynomial state*; nonuniform coefficients $\lambda_i$ are automatic.
- A no-go-flavored observation: whenever $2D+r<d_{\mathrm{rel}}$, the target expectation of $\pi(O_A)$ equals the source expectation — so low-degree observables need no transduction; advantage must come from *sampling*.

**How it works** A four-step coherent circuit: operator–Fourier transform $\mathsf F_A$ of the source guide into label amplitudes; compute $M(\alpha)$ and phase $c_\alpha$ (unit modulus and $M$ injective on $S_D$ by the distance condition); uncompute the source label with a clean reversible *relative* decoder $|Bc\rangle|0\rangle\mapsto|Bc\rangle|Ac\rangle$; apply $\mathsf F_B^{-1}$. Existence of $\pi$ for Pauli terms is characterized by matching symplectic commutation matrices, $K_A\subseteq K_B$, and matching relation phases. Optimal filters reduce to Rayleigh–Ritz on a Gram/objective pair; for polynomial guides this is the largest eigenvalue of a $(D{+}1)$-dimensional Jacobi matrix built from source moments $\tau_A(H_A^k)$, $k\le 2D+1$ (recovering the Dicke-state DQI guide for $H_A=\sum_i Z_i$).

**Why it matters** It gives a single algebraic lens covering DQI, HDQI, weighted/noncommuting variants, and extensions to Majorana, qudit and truncated bosonic algebras, plus a principled design knob (engineer $K_A$ to raise $d_{\mathrm{rel}}$). The sampling-vs-expectation dichotomy sharpens where advantage can plausibly live. Relevant to anyone working on decoded/structured quantum optimization or Gibbs-state preparation.

**Caveats** Efficiency is conditional on four separate assumptions (source state preparation, both operator–Fourier transforms, computable $M,c_\alpha$, and an efficient relative decoder) — no general construction is given. The advantage evidence is one instance family: a nonlinear pairwise OPI variant at $p=2053$ with a degree-50 guide giving *ideal* mean satisfaction $0.64313$ against a classical median best of $0.60666$ over ten instances with $\sim5\times10^6$ candidates per deep run — a ~3.6-point gap against heuristics, not a hardness argument, and reported for the noiseless, exactly computed quantum score rather than a simulated circuit.

## 4. Depth-Optimal Quantum Compilation

[arXiv:2609.34659](https://arxiv.org/abs/2609.34659) · [SciRate](https://scirate.com/arxiv/2609.34659)

*Francisca Vasconcelos*

**TL;DR** This paper gives the first end-to-end, catalyst-free constant-depth circuit for ε-approximating an arbitrary single-qubit gate, using H, T, and O(log(1/ε))-width generalized Toffoli gates (Fan-Out can be eliminated entirely), while proving a tight Θ(log log(1/ε)) depth bound in the bounded-arity model. It then leverages this to show that arbitrary single-qubit rotations *and* complex amplitudes are dispensable at constant depth for QAC-type decision classes, reducing the Parity ∉ QAC⁰ conjecture to circuits built only from H, X, and generalized Toffoli.

**The big picture** Standard results say any quantum computation can be rewritten using a small fixed set of gates, and even using only real numbers — but the known translations blow up circuit depth, which is the quantity that governs runtime on hardware and defines the shallow-circuit complexity classes. This work shows the translation can be made depth-preserving provided one is allowed multi-qubit gates acting on logarithmically many qubits, and that with only few-qubit gates a small but unavoidable depth penalty remains. As a consequence, several apparently distinct shallow quantum circuit families turn out to be identical, and a long-standing lower-bound conjecture is reduced to a much more rigid, combinatorially structured circuit form resembling a well-studied oracle-correlation problem.

**Key contributions**
- Constant-depth Rz(θ) synthesis via an approximate block encoding of ½Rz(θ) from a dyadic approximation (n₀−n₁ + i(n₂−n₃))/2^m ≈ ½e^{iθ/2}, followed by one round of robust oblivious amplitude amplification; O(log^{1+δ}(1/ε)) clean ancillae.
- Matching Ω(log log(1/ε)) lower bound for any fixed finite bounded-arity gate set (light-cone counting: exp(O((d+1)r^d)) achievable channels vs. Ω(1/ε) needed).
- Fan-Out elimination: polylog-width Fan-Out in constant depth from H + generalized Toffoli, via a specialized Grier–Morris nekomata preparation plus Rosenthal's nekomata→Parity reduction.
- Coherent O(log log(1/ε))-depth UQNC_f preparation of the Kim–Laakkonen reusable catalyst (which is exponentially close to a product state before a basis relabeling), amortized across the whole circuit.
- Depth-preserving real simulation using the Pauli-transfer (density-matrix Fourier) encoding; hardest case is generalized-CZ, handled by a randomized bucket-test that checks Y-eigenvalue agreement in constant depth.
- Structured Fourier / scalar Forrelation normal forms: acceptance bias = Φ_m(g_x) exactly, with nonlinear disjoint-block phases independent of x.

**How it works** The unifying trick is that all depth cost in the synthesizer reduces to (i) coherent interval comparison on m = Θ(log(1/ε)) address qubits and (ii) a reflection about |0^m⟩ — both constant-depth with wide Toffolis, O(log m) with CNOTs. For real simulation, encoding ρ by its Pauli coefficients makes conjugation by a gate a local real orthogonal map on 2r label qubits, so disjoint gates stay disjoint (unlike Aharonov's shared-ancilla realification, which serializes layers).

**Why it matters** Shallow-circuit complexity theorists get QAC[D] = UQAC[D] = HQAC[D] and a wide collapse of the Fan-Out/Threshold hierarchies over fixed real gate sets, plus a concrete new attack on Parity ∉ QAC⁰ via Fourier-growth bounds on structured constant-fold Forrelation. Compilation researchers get an explicit width–depth tradeoff for Solovay–Kitaev-style synthesis relevant to neutral-atom and T-depth-limited fault-tolerant architectures.

**Caveats** The constant-depth results require O(log(1/ε))-width generalized Toffolis, whose fault-tolerant cost is unaccounted for; real simulation preserves acceptance probabilities only (decision classes, not unitaries). Whether QNC_f⁰ = UQNC_f⁰ = HQNC_f⁰ is left open, so the Takahashi–Tani collapse over a fixed gate set holds only at depth Ω(log log n). Constants and ancilla overheads (log^{1+δ}) are not optimized.

## 5. Probing the classical complexity of quantum dynamics experiments

[arXiv:2609.31830](https://arxiv.org/abs/2609.31830) · [SciRate](https://scirate.com/arxiv/2609.31830)

*Thomas Schuster, Andreas Elben*

**TL;DR** The authors define the *reactivity function* $R_\tau(w)$ — the total contribution to a given expectation value $\mathrm{tr}(O\,\mathcal{C}(\psi))$ from Pauli paths of weight $w$ at time slice $\tau$ — as a complexity measure tailored to the new generation of "local information" classical simulators (sparse Pauli dynamics, influence-truncated tensor networks). Numerically, the maximum supported weight $w_*$ tracks $\log n_{\rm Pauli}$ (the SPD memory cost) remarkably closely across models, states, and times, and low reactivity provably implies efficient classical simulation, learning, and fast-forwarding. Crucially, because injected depolarizing noise acts as a Laplace transform on $R(w)$, smoothed features of the reactivity can be measured experimentally with constant sampling overhead — even in beyond-classical regimes.

**The big picture** Entanglement and magic have long been the standard yardsticks for how hard a quantum system is to simulate classically, but a wave of recent algorithms simulates expectation values accurately by keeping only local information, succeeding on systems that look hopelessly complex by those yardsticks. This work proposes a complexity measure that is a property of an entire experiment — initial state, dynamics, and measured observable together — rather than of a state or operator in isolation, and shows it predicts when those algorithms succeed. Most importantly, the quantity can be measured directly on hardware by deliberately injecting noise of varying strength and combining the outcomes, so an experiment can certify how far beyond cheap classical methods it actually sits.

**Key contributions**
- Definition of reactivity (time-sliced and global/space-time versions), unifying operator backflow, effective quantum volume (its first moment), and Boolean influence.
- Numerical demonstration that $w_*$ mirrors $\log n_{\rm Pauli}$ for SPD in the 1D MFIM ($N=51$) and 2D TFIM ($5\times5$) — notable since SPD truncates on coefficient magnitude, not weight. "Easy" cases concentrate below $w\approx4$; the hard TFIM state extends to $w\approx8$.
- Rigorous results: low mean-square reactivity ⇒ prediction from local randomized-measurement data and fast-forwarding of $\mathcal{C}_2\circ\mathcal{C}_1$, with $n^{\mathcal{O}(w_*)}$ samples.
- *Pauli path spectroscopy*: filter-function protocols (plus a coherent EPR-based variant giving exact $R_\tau(w)$ for infinite-temperature correlators via Fourier transform).

**How it works** Noise of rate $\gamma$ at slice $\tau$ gives $\sum_w e^{-\gamma w}R_\tau(w)$; direct inversion is ill-conditioned, so instead one measures overlaps $\sum_w h(w)R_\tau(w)$ with smooth filters $h(w)=\sum_\gamma h_\gamma e^{-\gamma w}$ (or discrete random weight-$k$ Pauli insertions, with kernel $\,_2F_1(-w,-k,-N;4/3)$). Sampling overhead is $X=(\sum|h_\gamma|)^2\sim e^{\mathcal{O}(w_*/\delta w)}$ — constant if the *relative* resolution is fixed. Chebyshev, analytic Bessel-based, and convex-optimized filters are compared; numerical filters win, with $X\approx100$ giving usable smoothed Heaviside filters up to $w_c=250$ at $N=500$.

**Why it matters** Gives experimentalists a scalable, hardware-native benchmark for "beyond local-information" complexity, replacing guesswork about whether a demonstration is classically spoofable; also relevant to error mitigation design.

**Caveats** The metric is admittedly spoofable by adversarial circuits, as are entanglement and magic. Numerical validation is limited to two Ising models and modest sizes where SPD converges (no observed support above $w\approx10$), so the $w_*$–$\log n_{\rm Pauli}$ correspondence is empirical, not proven. Only smoothed features of $R(w)$ are accessible, the choice of limiting time slice $\tau$ must be scanned, and detailed physics of the reactivity is deferred to a companion paper.
