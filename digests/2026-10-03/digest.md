# SciRate Daily Digest — 2026-10-03

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Polynomial-time additive-error estimation of output probabilities for shallow quantum circuits

[arXiv:2610.02146](https://arxiv.org/abs/2610.02146) · [SciRate](https://scirate.com/arxiv/2610.02146)

*Matthew Coudron, Michael J. Gullans, Jon Nelson, Joel Rajakumar, Shi Jie Samuel Tan*

**TL;DR** The authors give a deterministic classical algorithm that estimates the output probability of any constant-depth, bounded-fan-in quantum circuit with *arbitrary* connectivity to additive error ε in poly(n, 1/ε) time, removing the quasipolynomial n^{O(log n)} barrier of Bravyi–Gosset–Liu and the geometric-locality restriction of earlier polynomial-time results. The key move is an inclusion–exclusion decomposition that separates a small set of "bad" (non-peaked) output bits, handled by brute force, from the "good" bits, handled by a black-box cluster-expansion FPTAS expanded around the peaked computational basis state rather than the maximally mixed state.

**The big picture** Shallow quantum circuits are the main testbed for unconditional and conjectured quantum advantage, and a basic question is how hard it is classically to compute the probability of a specific measurement outcome to the same accuracy a quantum device would achieve with a modest number of repetitions. A decade of work chipped away at this, first for circuits laid out on two-dimensional grids, then for general grids and finally for arbitrary wiring but only at quasipolynomial cost. This paper closes the gap: for any fixed depth and gate size, the task is classically efficient regardless of how the qubits are connected. That removes one of the more natural candidate advantage tasks for shallow circuits — estimating a single outcome probability, which is more verification- and error-mitigation-friendly than sampling — from the list of plausibly hard problems.

**Key contributions**
- poly(n, 1/ε) deterministic additive estimation for depth-d, k-local circuits with arbitrary connectivity (previously n^{O(log n)}).
- A clean exact identity: P(0ⁿ) = Σ_T (−1)^{|T|} P(0_B, 1_T) · P(0_{T'}), where T ranges over good-bit sets whose connected components in the light-cone overlap graph touch the bad set B, and T' = [n] \ N_G[B ∪ T].
- A truncation bound showing the sum can be cut at |T| ≤ |B| + ⌈log₂(1/ε)⌉, via an entropy-style count of connected attachments (≤ 2^{|B|+s}(eK)^s) against decay τ^{s/(K+1)}.
- Generalization beyond circuits: any binary-variable distribution on a bounded-degree strong dependency graph with an exp(|S|)-time small-set oracle.
- Corollary: additive estimation of |⟨0ⁿ|U†(⊗Aᵢ)U|0ⁿ⟩| in poly time.

**How it works** Mark bit i "bad" if P(1ᵢ) > τ = (e²(2K+1))^{−(K+1)}, with K ≤ k^{2d} the max degree of the light-cone overlap graph. A pigeonhole/coloring argument over K+1 independent color classes shows P(0ⁿ) ≤ ε unless Σᵢ P(1ᵢ) < (K+1)log(1/ε), hence |B| = O(log(1/ε)). Then B ∪ T has size O(log 1/ε), so exact brute-force light-cone evaluation costs 2^{O(log 1/ε)} = poly(1/ε). The residual factor P(0_{T'}) is a marginal entirely on good bits, where every single-bit failure probability sits below the Mann–Waite threshold, so their cluster-expansion FPTAS gives relative error η in poly time; the appendix makes the log-truncation order m = ⌈log(2n/η)⌉ and connected-subgraph enumeration explicit.

**Why it matters** It sharpens the boundary of shallow-circuit advantage: outcome-probability estimation, unlike sampling, is now classically easy in full generality, so advantage claims must rest on sampling, relational problems, or depth/adaptivity. It also illustrates a useful template — doing cluster expansion around a peaked basis state instead of the identity — likely reusable elsewhere.

**Caveats** The constants are brutal: the ε-exponent scales as C_K(k^d + log K)log K with C_K = (K+1)[e²(2K+1)]^{K+1} and K ≤ k^{2d}, i.e. doubly exponential in depth, so this is asymptotic rather than practical. Additive estimates of individual probabilities need not form a normalized distribution; polynomial-time *sampling* for arbitrary-connectivity peaked shallow circuits remains open, as does recovering the sign or phase of general expectation values. Exact arithmetic is assumed, as in prior work.

## 2. Near-Optimal Ground-State Preparation without Controlled Hamiltonian Evolutions

[arXiv:2610.00520](https://arxiv.org/abs/2610.00520) · [SciRate](https://scirate.com/arxiv/2610.00520)

*Dhrumil Patel, Steven T. Flammia, Raul Garcia-Patron*

**TL;DR** The paper gives the first generic ground-state preparation algorithm that queries the Hamiltonian only through uncontrolled forward/backward time evolution, achieving Õ(α_H/(γ√η)) queries — matching the known lower bound (which holds even with controlled evolution) up to logs. The key primitive is a "SWAP echo": sandwiching e^{-iHτ}⊗e^{+iHτ} on two system copies between two controlled-SWAPs exactly realizes e^{-i Z_q ⊗ (H_A - H_B) τ}, converting a *control on the Hamiltonian* into a *control on a SWAP*.

**The big picture** Most near-optimal quantum algorithms for finding ground states require the ability to turn the Hamiltonian's time evolution on and off coherently, conditioned on an ancilla qubit. On analog and hybrid analog-digital simulators, and in early fault-tolerant settings, that kind of coherent control is expensive or simply unavailable, while plain evolution under the engineered Hamiltonian is native. This work shows that the extra control buys nothing asymptotically: by running two copies of the system and comparing their energies interferometrically, one can prepare ground states with the same optimal cost using only ordinary evolution forward and backward in time.

**Key contributions**
- The SWAP echo primitive: an exact, control-free implementation of qubit-conditioned evolution under the difference Hamiltonian D = H⊗I − I⊗H, plus a classical energy shift via a single-qubit phase rotation.
- A Laurent-QSP "soft energy comparator" of degree O((α_H/γ+1)log(1/ζ)) that flags, with error ζ, whether the candidate register's energy is lower than the anchor's by at least γ — without ever estimating either energy.
- Two algorithms, SD (fresh copies, Õ(α_H/(γη)) queries, Õ(1/η) copies) and CSD (coherent U_ψ access, Õ(α_H/(γ√η))), the latter matching Somma–de Wolf's Ω(α_H log(1/ξ)/(γ√η)) lower bound.
- Extensions to ground-state property and energy estimation with explicit complexities.

**How it works** With shift s = −γ/2 and τ = π/(4(2α_H+γ/2)), all phases θ_ab = τ(E_a−E_b−γ/2) stay in [−π/4,π/4], so y = sin(2θ) monotonically encodes the energy difference with separation Δ = sin(τγ) ≥ γ/(2(2α_H+γ/2)). Laurent QSP applied directly (not controlled) to the shifted SWAP echo realizes a polynomial approximation to a shifted error function, giving witness probability ≤ ζ when E_b ≥ E_a and ≥ 1−ζ when E_a−E_b ≥ γ. Because the ground state admits no lower-energy witness, it is absorbing; any excited anchor is flipped with probability ≥ η(1−ζ) by the candidate's ground-state component alone. SD uses M = O(1/η) trials per stage and R = O(log(1/(ηξ))) stages (per-stage contraction factor 43/64); CSD replaces the measure-and-retry loop with Yoder-type fixed-point amplitude amplification, costing O(1/√η).

**Why it matters** It cleanly settles whether controlled Hamiltonian evolution is necessary for optimal GSP, and gives a concrete recipe for analog/hybrid platforms (Rydberg arrays, trapped ions, optical lattices) where only native evolution is available. The SWAP-echo trick is likely reusable wherever controlled evolution is the bottleneck.

**Caveats** Two full system registers (2n qubits) plus ancillas, and coherent SWAPs between them, are required — nontrivial on exactly the analog hardware motivating the work. Known lower bounds on α_H, γ, η are assumed; the γ-margin comparator does not resolve excited-state spacings, and the analysis of general (non-eigenstate, mixed) anchor states rests on the monotone tracking bound rather than the idealized pairwise picture. GSEE is claimed to not need a gap promise in general, but the route here goes through GSP, which does; the truncated source leaves the GSPE/GSEE measurement assumptions unverified here. Input-state copy complexity Õ(1/η) for SD is not claimed optimal.

## 3. Clifford-hierarchy stabilizer formalism with applications to twisted quantum doubles

[arXiv:2610.00464](https://arxiv.org/abs/2610.00464) · [SciRate](https://scirate.com/arxiv/2610.00464)

*Christopher Fechisin, Kieran Cooney, Mathi Raja, Victor V. Albert, Dominic J. Williamson, Kyle Kawagoe, Seth Musser*

**TL;DR** The paper defines the $X\mathcal{C}^{(k)}_d$ ("xkcd") stabilizer formalism — stabilizer groups generated by Pauli-$X$ strings times multi-qudit *diagonal* gates from level $k$ of the Clifford hierarchy on prime-dimensional qudits — and proves a structure theorem: every uniquely-stabilized state is a uniform superposition over an affine-linear subspace of $\mathbb{Z}_p^n$ decorated by a diagonal phase sitting exactly one level *higher* ($k+1$) in the hierarchy. Applying this, they show all twisted quantum doubles $\mathcal{D}^\omega(\mathbb{Z}_p^n)$ with $\omega$ a product of type-III cocycles are realizable with mere Clifford ($k=2$) stabilizers, conjecture that type-I/II twists require level $p$, and give a deterministic qudit magic-state preparation protocol via code switching.

**The big picture** Recent fault-tolerance proposals evade the no-go theorem forbidding protected non-Clifford gates in two-dimensional topological codes by switching through intermediate codes whose stabilizers are not Pauli operators. Until now these constructions were ad hoc, with no general theory of what such codes can express. This work supplies that theory for a natural, group-closed family of beyond-Pauli stabilizers, and uses it to rank topological phases by how "non-Clifford" their stabilizers must be — finding, counterintuitively, that some phases hosting non-abelian anyons are cheaper to write down than purely abelian ones.

**Key contributions**
- Definition of the $X\mathcal{C}^{(k)}_d$ group $G^{(k),n}=\{X(\mathbf v)D[f]\}$, closed under multiplication even though level $k>2$ of the hierarchy is not a group; strictly generalizes XS and XP formalisms (qubits, on-site phases) to qudits and multi-site diagonal gates, and is strictly more structured than monomial stabilizer codes.
- Structure theorem (Thm. 1): $|\psi\rangle\in\Psi^{(k),n}_G$ iff $|\psi\rangle\propto\sum_{\mathbf x\in\mathbb{Z}_p^\ell}e^{2\pi i\varphi(\mathbf x)}|\mathbf x, M\mathbf x+\mathbf c\rangle$ with $D[\varphi]\in\mathcal{C}^{(k+1)}_d$ — a direct generalization of the Dehaene–De Moor normal form for Pauli stabilizer states. Plus an explicit algorithm returning this canonical form from the stabilizer group.
- Constructive proof that type-III-twisted doubles $\mathcal{D}^\omega(\mathbb{Z}_p^n)$ are Clifford-stabilizer realizable ($k=2$ is tight, since non-abelian anyons exclude $k=1$), and Conjecture: $k=p$ otherwise.
- Deterministic (vs. probabilistic in the qubit case of Davydova et al.) logical magic-state preparation on two qudit toric codes via $X\mathcal{C}^{(k)}_d$ measurement.

**How it works** Diagonal hierarchy elements are parameterized as $D_m[f]$ with $f$ a polynomial over $\mathbb{Z}_p^n$, level $=(m-1)(p-1)+\deg f$ (Cui–Gottesman–Krishna). The classification proceeds by showing the diagonal subgroup $D_H\trianglelefteq H$ is normal; the wavefunction support $V_\psi$ is exactly the mutual $+1$ eigenspace of $D_H$ (a "flatness" condition generalizing lattice-gauge zero-flux constraints), and the coset transversal $H/D_H$ is in bijection with $\mathbf v\in\mathbb{Z}_p^n$, forcing $V_\psi$ to be affine-linear. The level shift follows from the fact that finite differencing $\Delta_{\mathbf e_i}\phi$ lowers hierarchy level by one — conjugating $X$ by $D[\phi]$ produces a level-$k$ stabilizer from a level-$(k+1)$ phase.

**Why it matters** Gives a Haah-style classification program a concrete foothold beyond Pauli stabilizers, a practical test for whether a given wavefunction (e.g. a candidate topological ground state) is an $X\mathcal{C}^{(k)}_d$ state and at what minimal $k$, and a resource-theoretic ordering of TQD phases by stabilizer non-Cliffordness relevant to code-switching cost. Relevant to anyone designing non-Clifford logical gates or classifying commuting-projector models.

**Caveats** The $k=p$ half of the main conjecture is unproven (evidence only); the classification is for uniquely-stabilized states (higher-dimensional codespaces, i.e. codes on a torus, are handled only by adding logicals to $\mathcal{S}$); results are restricted to prime $p$ and to abelian gauge group $\mathbb{Z}_p^n$; and no error-correction properties (distance, thresholds, decoders) of $X\mathcal{C}^{(k)}_d$ codes are developed here.

## 4. Adaptivity is all you need: Optimal stabilizer learning using just single-copy measurements

[arXiv:2610.02031](https://arxiv.org/abs/2610.02031) · [SciRate](https://scirate.com/arxiv/2610.02031)

*L. Bittel, J. Eisert, W. Gong, A. A. Mele, L. Schatzki*

**TL;DR** The paper gives a polynomial-time adaptive single-copy algorithm that learns an arbitrary *n*-qubit stabilizer state from Θ(*n*) copies, matching the Bell-sampling optimum and eliminating the previously conjectured quadratic penalty (Ω(*n*²) for non-adaptive single-copy strategies). The same adaptive "diagonalization" subroutine yields a sample-optimal Θ(*n*+1/ε) single-copy stabilizer tester, a tolerant tester with Θ(*n*+ε₂/(ε₂−ε₁)²) complexity, the optimal memory–sample tradeoff Θ(*n*−*k*+1/ε) with *k* memory qubits, and an *O*(*n*2^*r*) learner for states of stabilizer nullity *r*.

**The big picture** A basic question in quantum learning is whether you must hold two copies of a state in a quantum device at once to identify it efficiently, or whether measuring one copy at a time suffices. For the most important family of quantum states — those underlying error correction and benchmarking — the best known single-shot strategies needed quadratically more experimental runs than the two-copy approach. This work shows that simply letting the choice of each measurement depend on the outcomes of all previous ones recovers the full two-copy advantage with no quantum memory at all, making optimal identification and verification feasible on hardware that cannot store states coherently.

**Key contributions**
- Θ(*n*+log(1/δ)) single-copy adaptive exact learner, explicit constants: *T* ≈ 2*n*+O(√(*n*log1/δ)), 2*T*+1 copies, *O*(*nT*²) time; extends to prime qudit dimension.
- Tolerant learner valid for mixed ρ with *F*_stab(ρ) > √(2/3), outputting a stabilizer within additive ξ of the optimum.
- Optimal single-copy tolerant tester, closing the gap from the prior *O*(*n*/ε) bound; plus a matching Ω(*n*+ε₂/(ε₂−ε₁)²) lower bound via an explicit one-qubit family.
- Optimal memory–sample tradeoff Θ(*n*−*k*+1/ε): sub-linear testing requires storing nearly the entire state.
- *t*-doped Clifford states learnable with *n*2^{*O*(*t*)} single-copy measurements, improving prior work.

**How it works** The algorithm maintains a Clifford *C* and tracks *D*(φ), the space of *Z*-type stabilizers of *C*|ψ⟩. Measuring two copies in the computational basis and XORing gives *u* uniform on *D*(φ)^⊥, which is exactly the *X*-projection of the stabilizer group, so some (*u*,*v*) is a stabilizer. A CNOT fan-out *F_u* from the pivot bit maps it to (*e_i*,*v*′) while provably zeroing the pivot coordinate of every pre-existing diagonal stabilizer; a random choice between *H_i* and *H_i S_i* then converts it to *Z*-type with probability ½. The codimension *r* is a monotone Markov chain with success probability (1−2^{−*r*})/2, so E[rounds] < 2*n*+4, with geometric-sum tail bounds. For mixed/approximate inputs, *r* can also increase; the analysis uses a birth–death chain with drift μ = 3*f*₀²/2−1, maps it through the expected-hitting-time potential *g* to get unit drift with increments ≤13.5/μ, and applies Kötzing's drift concentration. Testing filters candidates with global-Clifford shadows, using the ≤1/√2 pairwise stabilizer overlap plus Gershgorin to show at most six survive. Memory-assisted testing uses partial Bell sampling with controlled-Pauli Cliffords *W*_{α,j}, then the six-copy routine of Iyer et al. on the residual *k* qubits.

**Why it matters** Removes the main practical obstacle (coherent two-copy access) to optimal stabilizer characterization, relevant to QEC code verification, benchmarking, and magic-state-resource estimation. It is also a rare clean provable separation between adaptive and non-adaptive single-copy quantum learning.

**Caveats** Tolerant learning requires *known* *f*₀ > √(2/3) ≈ 0.816 — a fairly high fidelity promise, not a true "constant-vs-constant" tolerance. Constants are large (1458/μ² in the round budget, 13.5/μ increments). Low-nullity learning has exponential 2^*r* overhead with only constant-accuracy claims per the abstract framing, and uses random Clifford tomography on the logical subsystem. Testing optimality is stated for ε ≤ 1/5 and constant confidence.

## 5. The stationarity test: a framework for learning quantum many-body systems from their thermal states

[arXiv:2610.01074](https://arxiv.org/abs/2610.01074) · [SciRate](https://scirate.com/arxiv/2610.01074)

*Thiago Bergamaschi*

**TL;DR** — The paper introduces a single, conceptually simple primitive — "guess a Hamiltonian, then measure whether the sampled state is a fixed point of the Chen–Kastoryano–Gilyén detailed-balanced Lindbladian associated with that guess" — and shows it suffices for rigorous Hamiltonian learning. This yields the first structure-learning algorithm for non-commuting lattice Hamiltonians from Gibbs states at *all* temperatures, the first parameter-learning algorithm from thermal *metastable* states, and a thermodynamic-limit refinement of the recent metastable area law. Sample complexity is $e^{\mathrm{poly}(\beta)}\beta^{-2}\cdot O(\eta^{-2}\mathrm{polylog}(1/\eta)\log n)$, optimal in $n$ and near-optimal in $\eta$.

**The big picture** — Inferring which interactions govern a many-body system from measurements of its equilibrium state is a basic inverse problem, but until now rigorous algorithms either assumed the interaction graph was already known, or required high temperature, or assumed nature hands you a perfectly equilibrated sample — which is computationally implausible at low temperature. This work reframes learning as a test of stationarity under a quantum thermalization dynamics: if the state does not visibly drift under the dynamics generated by your guess, your guess must be right. Because any state evolved for polynomial time under such a thermalizing dynamics becomes approximately stationary, the framework also shows that whatever "nature" actually prepares in polynomial time already contains enough information to recover the interaction strengths, even when it is statistically far from true equilibrium.

**Key contributions**
- The stationarity test as a unified learning primitive; trivial completeness via detailed balance, with soundness supplied by Fisher-information arguments.
- First structure learning (recovering the interaction graph *and* coefficients) for lattice Hamiltonians at arbitrary $\beta$ from Gibbs states, with $O(\log n)$ samples and $n^{\mathrm{poly}(\beta)}$ time.
- First parameter learning from $\epsilon$-locally metastable states, valid down to an accuracy plateau $\eta_{\mathsf{thr}}=\mathsf{z}_\beta\epsilon$.
- New technical tools: an approximate convexity bound $\beta^2\|[\mathbf{A},\mathbf{H}-\mathbf{G}]\|^2_{\rho_H}\lesssim \mathsf{FI}+\text{err}$, and a Lipschitz continuity bound $\|\mathcal{L}^\dagger_{\mathbf H,a}-\mathcal{L}^\dagger_{\mathbf G,a}\|_{\infty\to\infty}\lesssim\sum_\gamma|g_\gamma-h_\gamma|e^{-\Omega(\mathrm{dist})}$.
- Area law $\mathsf{I}(A:\bar A)_\sigma\le 2\beta\|\partial_A\mathbf H\|+e^{\mu|A|}\epsilon^\lambda$, removing the system-size factor of prior work.

**How it works** — Feeding $\mathbf O=\mathbf H-\mathbf G$ into the test computes the quantum Fisher information of $\rho_{\mathbf H}$ relative to $\rho_{\mathbf G}$, expressible (following BCV25) as a weighted integral of commutators of operator-Fourier-transformed jumps with $\mathbf H-\mathbf G$. Dirichlet-form comparison converts these filtered commutators back to bare local commutators, giving soundness. Learning proceeds by iterative "accuracy bootstrapping": at scale $\eta_r=2^{-r}$, exhaustively perturb the guess by local clusters of radius $\ell\sim\mathrm{poly}(\beta)$ (Lipschitz continuity makes $\ell$ independent of target accuracy), keeping the invariant $\Gamma_{G^{(r)}}\subseteq\Gamma_{\mathbf H}$. Sample optimality comes from splitting each test into a quasi-local "baseline" at radius $\mathsf{R}\sim\log\eta^{-1}$, estimated in parallel via a coloring schedule and median-of-means, plus a strictly local correction obtained from Pauli classical shadows on constant-size RDMs. For metastable inputs, where $\log\sigma$ need not be local, convexity is re-proved directly for the test using BCV25's approximate detailed-balance functional.

**Why it matters** — It unifies Hamiltonian learning with the quantum Gibbs-sampling/optimal-transport toolkit, replacing SDP hierarchies and bespoke identifiability equations with a physically transparent criterion, and removes the unrealistic exact-equilibrium input assumption. Relevant to quantum learning theorists, Gibbs-sampler analysts (the convexity bound was conceived as an attack on modified log-Sobolev inequalities), and anyone calibrating thermal quantum devices.

**Caveats** — Results require lattice (bounded-degree, $\mathsf{D}$-dimensional, polynomial-growth) geometry; constants scale as $e^{\mathrm{poly}(\beta)}$ and structure-learning runtime is $n^{\mathrm{poly}(\beta)}$, far from the $\tilde O(n^2)$ classical state of the art. The metastable accuracy plateau $\mathsf{z}_\beta\le\beta^{-1}e^{\mathrm{poly}(\beta)}$ is severe at low temperature, and no matching lower bound is given. Structure learning from metastable states is left open, and the area law's additive term is exponential in $|A|$ (expected to be near-tight given BCV25's counterexample). Concurrent independent work reportedly obtains similar metastable-state results.
