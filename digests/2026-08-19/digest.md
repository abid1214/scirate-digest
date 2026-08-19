# SciRate Daily Digest — 2026-08-19

The top 10 papers on [SciRate](https://scirate.com/) today.

## 1. Non-CSS Quantum Code Embedding

[arXiv:2608.16995](https://arxiv.org/abs/2608.16995) · [SciRate](https://scirate.com/arxiv/2608.16995)

*Andrew C. Yuan, Nouédyn Baspin*

**TL;DR** — This paper lifts the chain-complex ("cone") framework for CSS codes to arbitrary stabilizer codes by replacing chain complexes with *symplectic complexes* $S \xrightarrow{\sigma} P \xrightarrow{\hat\sigma} \bar S$, where $P$ is the $\mathbb{F}_2$ phase space with symplectic form and $\hat\sigma$ is the symplectic adjoint. The central object is a height-2 cone with a "defect map" $p$ that absorbs the non-CSS-ness; from it, qLDPC surgery, Layer-code-style Euclidean embedding, and weight reduction all carry over to non-CSS codes without local Clifford tricks.

**Key contributions**
- A general embedding theorem (Thm. 4.1, ~2 pages with proof) for arbitrary stabilizer codes phrased in symplectic-complex language.
- Non-CSS logical measurement: measuring any commuting set $g: X^A \to P^D$ (e.g. $Y$-type logicals) reduces to the condition $\hat g g = 0$, generalizing the height-1 cone used for $X/Z$ surgery.
- Non-CSS generalizations of Layer codes (3D Euclidean embedding) and quantum weight reduction, previously available only for CSS inputs.
- Explicit low-level circuit implementations and fault-tolerance analysis (spacetime fault complexes, $T \ge d$ rounds, min-weight decoding threshold) for both CSS and non-CSS syndrome extraction/logical measurement.

**How it works** — A stabilizer code is packaged as $\sigma: S \to P = Q_X \oplus Q_Z$ with syndrome map $\hat\sigma = \Lambda\sigma^\top$; $\hat\sigma\sigma = 0$ is exactly the commutation condition, so the "complex" condition is symplectic rather than $\partial^2=0$. Ancilla check qubits are initialized in the $X$ basis; a CNOT circuit built from the $X$-sector $g_X$ and a CZ circuit from the $Z$-sector $g_Z$ implement, in Heisenberg picture, the block-lower-triangular symplectic map $\begin{psmallmatrix}\mathrm{id}&&\\ g&\mathrm{id}&\\ &\hat g&\mathrm{id}\end{psmallmatrix}$ — i.e. precisely the height-2 cone with zero defect map. Physical errors propagate as $e(P)\mapsto e(P),\ e(\bar S)\mapsto \hat\sigma e(P)+e(\bar S)$, so transversal readout yields $\hat g \tilde e(P^D)+e(\bar X^A)$, and the deformed code is $\mathrm{im}\,\sigma^D\cap\ker\hat g+\mathrm{im}\,g$. For logical measurement of $\ell^\star(P^D)$, the outcome is $\langle \hat g\tilde e(P^D)|\bar{\mathcal X}^A\rangle + \langle \delta^A x^A|p\,\mathcal X^A\rangle$ — the second term is the genuinely new non-CSS contribution from the defect map, absent in the CSS case.

**Why it matters** — $Y$-type and general non-CSS logical measurements currently require ad hoc local-Clifford conjugation, which breaks LDPC structure or code symmetry; this gives a uniform, constructive recipe. Anyone building qLDPC surgery compilers, weight-reduction pipelines, or 3D-local code embeddings for non-CSS families (e.g. XZZX, twisted, or Clifford-deformed codes) should care.

**Caveats** — The source is heavily truncated: the main theorem's statement, the Layer/weight-reduction sections, and the fault-complex appendices are not visible here, so parameter overheads (distance preservation, qubit/check counts, weight bounds) could not be verified. Ancillas are assumed to have no internal logicals ($\ker\delta^A=\im\delta^A$) and $O(1)$-depth CNOT/CZ gadgets are assumed available. Thresholds are asserted via the standard Gottesman argument rather than numerically demonstrated; no simulations appear.

## 2. Quantum simulation of slow analytic time-dependent Hamiltonians

[arXiv:2608.17653](https://arxiv.org/abs/2608.17653) · [SciRate](https://scirate.com/arxiv/2608.17653)

*Chenhao Zhao, Yinan Li, Dong An*

**TL;DR** — For Hamiltonians of the "slow" form $\widetilde H(t)=H(t/T)$ with $H$ real-analytic (or Gevrey-$\sigma$), the authors build an explicit *periodic Gevrey extension* of $H$ on $[0,2]$ that matches all derivatives at the seam, then apply Floquet embedding + QSVT. This yields query complexity $\widetilde{\mathcal O}(\alpha T+\log(1/\varepsilon))$ — additive rather than the multiplicative $\alpha T\log(1/\varepsilon)$ of truncated Dyson — while keeping additional gate cost polylogarithmic in $1/\varepsilon$ (unlike the concurrent transducer-based optimal algorithm, whose gate cost is $\mathrm{poly}(1/\varepsilon)$).

**Key contributions**
- A Gevrey-class version of Borel's lemma with explicit constants: given $|a_n|\le CD^n(n!)^\sigma$, construct $f=\sum_j \frac{a_j}{j!}t^j\chi_\tau(R_jt)$ with $R_j=4e^{\sigma-1}D(j!)^{(\sigma-1)/j}$ realizing all derivatives, with $|f^{(n)}|\lesssim (32e^{\sigma-1+1/e}D)^n(2C_{\tau,2})^{n-1}(n!)^{\sigma-1+\tau}$.
- An explicit Gevrey-$\tau$ cutoff ($1<\tau<2$) with derivative bound $C_{\tau,1}8^nC_{\tau,2}^{n-1}(n!)^\tau$, $C_{\tau,2}=4e^{\tau+1}/(\tau-1)$.
- Fourier-coefficient decay and Lieb–Robinson/Floquet-truncation bounds for merely Gevrey (not analytic) periodic Hamiltonians, extending Mizuta–Fujii's analytic-only analysis.
- Complexity: $\widetilde{\mathcal O}(\alpha T+\log 1/\varepsilon)$ queries with $\widetilde{\mathcal O}((\alpha T+\log 1/\varepsilon)^2\log 1/\varepsilon)$ extra gates (general), $\widetilde{\mathcal O}((\alpha T+\log 1/\varepsilon)^2)$ for control Hamiltonians $H=\sum_j\alpha_j(s)M_j$; Gevrey-$\sigma$ ($1\le\sigma<2$) gives $\widetilde{\mathcal O}((\alpha T+\log1/\varepsilon)^\sigma)$.
- Combined with optimal LCHS, slow analytic semi-dissipative ODEs are solved with $\widetilde{\mathcal O}(\frac{\|u_0\|}{\|u(T)\|}\alpha T\log(1/\varepsilon))$ queries, a quadratic improvement in the $\log(1/\varepsilon)$ factor over Low–Somma.

**How it works** — $H$ is extended on $[1,2]$ by two Borel-type Taylor-with-cutoff tails $F_\tau(s-1),G_\tau(s-2)$ built from endpoint derivatives $H^{(k)}(1),H^{(k)}(0)$, giving a $C^\infty$ 2-periodic $\hat H$ of Gevrey index $\varrho=\sigma+\tau-1$. Fourier modes then decay stretched-exponentially, $\sim e^{-c|m|^{1/\varrho}}$, so the Floquet effective Hamiltonian can be truncated at $l_{\max}=\widetilde\Theta((\alpha T+\log1/\varepsilon)^\varrho)$; its block encoding (LCU over modes, plus the ladder/phase term) is fed to QSVT, with amplitude restored via approximate translation symmetry and oblivious amplitude amplification.

**Why it matters** — Adiabatic/annealing and control-pulse dynamics are exactly of the slow form; this is the first algorithm to get simultaneously near-additive queries *and* polylog-in-$1/\varepsilon$ gate overhead for a non-periodic time-dependent class.

**Caveats** — The input model is nonstandard: coherent access to $H'(s)$ plus block encodings of endpoint derivatives up to order $\widetilde{\mathcal O}(\log\alpha T+\log 1/\varepsilon)$; not directly comparable to HAM-T results. Gate cost is quadratic in $\alpha T$, worse than Dyson's linear. Regularity constants ($C_{\tau,2}\propto 1/(\tau-1)$, $D$, $\sigma$) are treated as $T,\varepsilon$-independent constants and blow up as $\tau\to1$, hiding a real tradeoff behind the $\widetilde{\mathcal O}$; $\sigma\ge2$ is excluded.

## 3. Nearly Sample-Optimal Estimators for Quantum Rényi and Tsallis Entropies

[arXiv:2608.18070](https://arxiv.org/abs/2608.18070) · [SciRate](https://scirate.com/arxiv/2608.18070)

*Kean Chen, Qisheng Wang*

**TL;DR** The paper closes the remaining gaps in the sample complexity of estimating quantum Rényi and Tsallis entropies from copies of an unknown $d$-dimensional state, giving estimators that match Wang's recent lower bounds up to polylogs: $O(d^{1+1/\alpha}/\varepsilon^{1/\alpha}+d^{1/\alpha-1}/\varepsilon^2)$ (Rényi, $0<\alpha<1$), $O(d^{1+1/\alpha}/\varepsilon^{1/\alpha}+d^{2-2\alpha}/\varepsilon^2)$ (Tsallis, $0<\alpha<1$), and $O(d^2/\varepsilon^{1/\alpha}+d^{1-1/\alpha}/\varepsilon^2)$ (Rényi, non-integer $\alpha>1$). This improves prior $O(d^{2/\alpha}/\varepsilon^{2/\alpha})$ and $O(d^2/\varepsilon^2)$ bounds, and notably departs from the weak-Schur-sampling paradigm.

**Key contributions**
- A new "one-step bias" inequality: for $\sigma\succeq \tfrac{d}{n}I$, $0\le (1-\alpha)\tr\sigma^\alpha+\alpha\tr(\rho\sigma^{\alpha-1})-\tr\rho^\alpha \le (d/n)^{\alpha-1}\mathrm{D}_{\chi^2}(\rho\|\sigma)$, i.e. the linearization error of $\tr(\cdot)^\alpha$ is controlled by the Bures $\chi^2$-divergence.
- Showing that the $\chi^2$-tomography of Padakandla–Sen–Tang–Wright, regularized as $\sigma=\hat\rho+\tfrac{2d}{n}I$, achieves $\mathrm{D}_{\chi^2}(\rho\|\sigma)=O(d^2/n)$.
- A Richardson-extrapolation estimator for $\alpha>1$ built on Hayashi's covariant pure-state POVM plus random purification, with a new bias expansion in Beta moments.
- Filling in Table 1: tight (up to polylog) complexities for all non-integer orders.

**How it works**
*Case $0<\alpha<1$:* run $\chi^2$-tomography with $n$ samples, form $\sigma$, compute $(1-\alpha)\tr\sigma^\alpha$ classically, and debias by measuring the observable $\sigma^{\alpha-1}$ (i.e., $m$ single-copy measurements in $\sigma$'s eigenbasis, outputting $s_J^{\alpha-1}$). The tomography inequality bounds the bias by $O(d^{\alpha+1}/n^\alpha)$; careful second-moment bounds on $s_J^{\alpha-1}$ (splitting at $\alpha=1/2,3/4$, using Hölder against $\sum_i s_i^\alpha$) give the variance, and hence relative-error control for Rényi vs. additive for Tsallis.

*Case $\alpha>1$:* map $s$ copies to $s$ copies of a Haar-random purification $|\psi\rangle=|M\rangle$ and apply Hayashi's POVM; the estimate satisfies $\hat M_T=\sqrt{1-T}M+\sqrt{T}G$ with $T\sim\mathrm{Beta}(d^2-1,s+1)$. A Schatten–Taylor expansion yields $\mathbb{E}[\tr\hat\rho^\alpha]=F+\sum_{j\le k}c_j\mu_j(s)+O(F(d^2/s)^\alpha)$ with $k=\lceil\alpha\rceil-1$. Running $k+1$ batches of sizes $2^\ell m$ and taking a linear combination annihilating $\mu_1,\dots,\mu_k$ kills the polynomial bias, leaving only the $(d^2/s)^\alpha$ remainder; variance is $O(F^2[d^{1-1/\alpha}/m+(d^2/m)^{2\alpha}])$.

**Why it matters** Rényi/Tsallis entropies underpin many quantum information tasks (channel capacities, magic/entanglement monotones), and their sample-optimal estimation was open for all non-integer orders since 2017. Beyond the bounds, the $\chi^2$-tomography + linearization template is likely reusable for other spectral functionals, and it shows tomography-based estimators can beat Schur-sampling ones.

**Caveats** Constants are $\alpha$-dependent and degenerate as $\alpha\to1$ (e.g. $(1-\alpha)^{-(2\alpha-1)/\alpha}$) and as $\alpha\to$ integers from above ($k$ grows, Vandermonde conditioning); integer $\alpha>1$ is excluded (already known). Polylog gaps to the lower bounds remain. Both algorithms need collective measurements on $\Theta(n)$ copies (full tomography / Hayashi POVM on $\mathrm{Sym}^s$), so they are not implementable incoherently, and computational cost is not discussed. Success probability is constant (2/3), requiring median amplification; $\varepsilon\le1$ and known $d$ are assumed. The source is truncated before the variance proof of the $\alpha>1$ one-batch lemma.

## 4. Quantum Circuit for General Unitary: Improved T-count via Block Flattening and Dilation

[arXiv:2608.17846](https://arxiv.org/abs/2608.17846) · [SciRate](https://scirate.com/arxiv/2608.17846)

*Pei Yuan, Shengyu Zhang, Wei Zi*

**TL;DR** The authors give a Clifford+$T$ compiler for an arbitrary classically specified $n$-qubit unitary with worst-case $T$-count $O(d^{5/4}L^{5/8}\log d)$, where $d=2^n$, $L=n+\log(1/\epsilon)$, improving Tan's $O(d^{4/3}L^{2/3})$ whenever $L\le d$. The trick is to block-encode the *whole* unitary at once — after randomly "flattening" its block norms — and to remove the subnormalization with a single QSVT amplification step; this narrows the gap to the $\widetilde\Omega(d)$ lower bound to $\widetilde O(d^{1/4})$.

**Key contributions**
- Simultaneous block flattening: two Boolean $\pm1$ phase diagonals sandwiched between Walsh transforms, $V=H_dD_1UD_2H_d$, make *every* $b\times b$ block satisfy $\|P_IVP_J^\dagger\|\le 16\ln 2\sqrt{b/d}\log(2d)$, proved by an entrywise Hoeffding bound followed by a matrix Rademacher (Tropp) bound with variance $\mu=16(b/d)\ln 2d$.
- A "block-dilation SELECT": all $D^2$ normalized blocks are unitarily dilated (Julia–Halmos) and packed into one uniformly controlled unitary acting on only $k+1$ target qubits, yielding a block encoding of $V$ with subnormalization $\rho=Dg=O(\sqrt{d/b}\log d)$.
- A robust one-point amplification lemma: since all encoded singular values equal $1/\rho$, an odd degree-$Q=\Theta(\rho)$ polynomial (complex completion of $(-1)^mT_Q(\beta x)$, with $P(1/\rho)=1$ exactly) maps them to 1. Perturbation analysis via polar decomposition + Markov's derivative bound gives $\|A_{\rm amp}-V\|=O(Q^2\delta)$ and clean-input error $O(Q\sqrt\delta)$.
- Appendix extension: a *single* sign pair flattens an entire multiplexed family $\{U_x\}$ simultaneously, improving multiplexed-unitary $T$-counts over direct application of Tan's compiler.

**How it works** Tan's UCU compiler implements the SELECT with $O(d\sqrt L+b^2L)$ $T$ gates; QSVT costs $O(\rho)$ queries, giving $O(\log d\,[d^{3/2}b^{-1/2}\sqrt L + d^{1/2}b^{3/2}L])$. Balancing at $b_\star=d^{1/2}L^{-1/4}$ produces the $5/4$ exponent. Signal phases cost $O(\rho(S_0+L))$ via multi-controlled Toffolis plus Ross–Selinger $R_z$; the sign diagonals cost only $O(\sqrt d)$.

**Why it matters** Non-Clifford count dominates fault-tolerant cost, and generic unitary synthesis is the canonical worst case. This is the first improvement over the recursive cosine–sine paradigm by abandoning product decompositions entirely, and it demonstrates that block-encoding/QSVT machinery — usually applied to sparse or structured Hamiltonians — can beat structural decompositions for *fully generic* data.

**Caveats** Ancilla use is large: $O(2^n\sqrt L)$ clean qubits (vs. Tan's $O(L)$ in the high-precision regime), so this is a strict space–$T$ trade. The flattening signs are found by randomized classical preprocessing requiring certified block-norm evaluation of a $d\times d$ matrix; this exponential classical cost is explicitly excluded. Results hold only for $L\le d$. The approximation model is the one-sided $\|\widetilde U J_0 - J_0U\|\le\epsilon$ criterion. Markov's inequality is invoked for a complex-coefficient polynomial bounded on $[-1,1]$, a step worth checking. No numerics; the improvement is asymptotic with a $\log d$ and unspecified constants. The authors note LLM assistance in manuscript preparation.

## 5. Lie-Algebraic Classical Simulation of Bosonic Systems Beyond Gaussian Dynamics

[arXiv:2608.17094](https://arxiv.org/abs/2608.17094) · [SciRate](https://scirate.com/arxiv/2608.17094)

*Adelina Bärligea, Timothy Heightman, Jakob S. Kottmann, Antonio Acín*

**TL;DR** The paper generalizes Lie-algebraic ("g-sim"-style) Heisenberg-picture classical simulation to bosonic systems by replacing the dynamical Lie algebra with an *observable-seeded reachable operator module* V(O) — the smallest space containing O closed under ad of the circuit generators. Whenever dim V(O) = poly(n) and input overlaps are accessible, mean values, fixed-order/multi-time/OTOC correlators and reverse-mode gradients are exactly computable in polynomial time, recovering Gaussian optics and extending it to non-Gaussian inputs, bounded-photon Kerr/pair-hopping dynamics, and nilpotent polynomial-phase families.

**Key contributions**
- Reachable-module simulability criterion (Thm 1): exact evaluation ⟨O(θ)⟩ = wᵀ e^{θ_L A_{k_L}}···e^{θ_1 A_{k_1}} e^{in} on a D-dimensional module, with no Fock cutoff or moment closure; the usual poly-dim DLA condition is recovered only as the special case O ∈ 𝔤 and shown to be sufficient, not necessary.
- Three finiteness mechanisms for bosons: (i) Gaussian degree preservation, giving moment modules of dim ≤ C(2n+m, m) (m=1,2 reproduce mean/covariance propagation, valid for non-Gaussian inputs given input moments); (ii) U(1) sector confinement at bounded photon number N_max = O(1), where dim H_{≤N_max} = Θ(n^{N_max}) and dim V(O_S) ≤ d²_{n,S} = O(n^{2N_max}), covering self-/cross-Kerr and pair hopping at arbitrary coupling and poly depth; (iii) a multi-mode nilpotent cubic-and-higher phase family.
- A sharp negative result absent in spin/fermion settings: a finite-dimensional bosonic generator algebra does *not* imply a finite observable orbit (e.g. Kerr acting on â).
- A controlled perturbative hierarchy for squeezing: parity-resolved photon-number bands of depth k reproduce number-conserving observables exactly through order 2k+1 in squeezing strength, leading error at order 2(k+1); numerically confirmed, with tail bounds for squeezed vacua.
- Numerics: operator spreading/OTOCs on interacting chains up to 400 modes, doublon topological band with flux-reversed edge motion, differentiable control experiments (depths 1–8, lattices to 9×9).

**How it works** Circuits are U(θ)=∏ e^{-iθ_ℓ H_{k_ℓ}}; observables are propagated in the Heisenberg picture. Using the Hermitian bracket ad_H(A)=i[H,A], one builds V(O) by nested commutation seeded at O (not at the generators), represents each ad_{H_k} as a real D×D matrix on a module basis, and contracts against input overlaps Tr[B_α ρ_in]. Fixed-order correlators contract m module expansions against an ordered input-moment tensor E^in; gradients follow by differentiating the matrix product in reverse mode. For Gaussian dynamics the module action is the affine symplectic map S(t)=e^{tΩG} augmented by the identity/displacement row; for number-conserving dynamics it is the block-restricted Hermitian algebra on ⊕_{N∈S} H_N.

**Why it matters** It cleanly separates simulability of *dynamics* from simulability of *observables*, giving a unified taxonomy that places Gaussian optics, bounded-photon interacting bosons, and CV universality on the same axis. Practically relevant for benchmarking bosonic/photonic hardware, for delimiting quantum-advantage claims (results are consistent with boson-sampling hardness since order is a resource), and for variational photonic circuits needing exact gradients.

**Caveats** Efficiency requires not just poly dim V(O) but efficiently accessible input overlaps/moments and generator action matrices — non-trivial for general non-Gaussian inputs. Bounded-N_max = O(1) is restrictive and complementary to the QMA-hard growing-particle-number regime; costs scale as n^{2N_max}. Squeezing is only handled perturbatively under explicit analyticity assumptions. Outputs are fixed-order mean values, not samples or full distributions, and the propagation assumes a common invariant domain for unbounded operators.

## 6. Hardware-Aware Compilation and Execution of Bivariate Bicycle Codes on Neutral-Atom Systems

[arXiv:2608.17023](https://arxiv.org/abs/2608.17023) · [SciRate](https://scirate.com/arxiv/2608.17023)

*Jason Ludmir, Aditya Ranjan, Nicholas S. DiBrita, Jason Han, Tirthak Patel*

**TL;DR** Park-n-Ride is a compiler/architecture co-design that maps the logical instruction set of bivariate-bicycle (BB) qLDPC codes — idle syndrome rounds, shift automorphisms, in-module and inter-module logical measurements, T-injection — onto zoned neutral-atom arrays subject to AOD non-crossing, blockade, and trap-transfer constraints. Its three core mechanisms (spectral module placement, direction-agnostic torus-roll scheduling with monotone resync, interval-colored bridge scheduling) cut estimated end-to-end runtime by ~18% versus arbitrary placement and transport-induced atom-loss exposure by ~41% on circuits of 32–113 gross-code modules (up to ~32.5k physical / 1.3k logical qubits).

**Key contributions**
- A columnar compute-zone layout: vertical compute columns holding stacks of BB modules, each split into idling / bridge-interaction / shift-measure subzones, plus a per-module "logical processing unit" holding bridge and ancilla rows. Motion is confined within columns, largely sidestepping AOD crossing violations.
- Shift-automorphism scheduling exploiting torus periodicity: $T(\Delta i,\Delta j)=\mathrm{Roll}_i\circ\mathrm{Roll}_j$, with four equivalent realizations per shift (move a width-$k$ strip or the complementary $N-k$ strip). Columns elect a head module whose direction all others adopt, making motion monotone and parallelizable; residual offsets from heterogeneous shift magnitudes are cleared by a sorted, staggered-dropoff resync sweep whose step count equals the number of distinct residuals.
- Bridge-based joint measurement: pairs are mapped to column intervals, greedily interval-colored into rounds of disjoint intervals, then advanced in lockstep ±1 column toward a midpoint rendezvous — guaranteeing collision-free, order-preserving AOD motion.
- Spectral seriation (Fiedler vector of the interaction-graph Laplacian) for module→column packing; a 24-substep wrap-aware idling stabilizer schedule; a per-column single-server T-factory queueing model.

**How it works** A BB tableau is turned into a dependency DAG, topologically layered into maximally parallel layers, split into shift/measure sublayers, placed into columns, and lowered to AOD moves. A timing estimator (55 µm/µs shuttling, 100 µs trap switch, 0.8 µs CZ, 10 µm pitch, 120×60 µm modules) sums per-layer transport, gate, and subzone-transition costs.

**Why it matters** Most qLDPC systems work stops at code construction or abstract logical circuits; this is one of the first concrete lowerings of BB-code logical operations to realistic zoned atom hardware, and it quantifies which primitives dominate (syndrome/measurement cycles, not shifts).

**Caveats** Everything is an analytic estimator, not circuit-level noise simulation: readout time is zeroed by construction, the logical-error curve uses a toy binomial "oracle decoder" (failure at ≥5 faults), and no threshold or decoder analysis is done. Benchmarks are synthetic (10 ops/module, 25% joint measurements, fixed correlation 0.35), with no prior-art baseline. The two-gross scalability claim (<0.1% runtime change) comes from rescaling existing schedules rather than recompiling, which is surprisingly insensitive. Magic-state distillation is entirely abstracted away.

## 7. A Complete Classification of Complex Hadamard Matrices of Order Six

[arXiv:2608.18053](https://arxiv.org/abs/2608.18053) · [SciRate](https://scirate.com/arxiv/2608.18053)

*Mateo Cárdenes Wuttig, Joseph Tindall*

**TL;DR** The authors prove that every order-six complex Hadamard matrix is equivalent to a dephased matrix possessing a "finite-corner witness" — a 3×3 corner whose two complementary candidate blocks form finite sets — so that the whole matrix is recovered algebraically by Szöllősi's dilation from four initial phases. This supplies the missing global step in the dilation method and proves Szöllősi's conjecture, reducing the classification of $N=6$ Hadamards to solving one quadratic and one cubic in each direction (except Tao's isolated matrix $S_6^{(0)}$ and one explicit Karlsson matrix).

**Key contributions**
- A cubic Gram invariant $\tau_{\rm r}(X)=(XX^\dagger)_{12}(XX^\dagger)_{23}(XX^\dagger)_{31}$ for $3\times3$ unimodular blocks, with $\mathrm{Re}\,\tau$ invariant under all monomial row/column operations and the identity $\mathrm{Re}\,\tau_{\rm r}=\mathrm{Re}\,\tau_{\rm c}$ (proved from equality of $\mathrm{tr}\,M^2$ and $\det M$ for $XX^\dagger$, $X^\dagger X$).
- An **infinite-fiber trichotomy**: an invertible $X$ with infinite normalized fixed-Gram fiber must satisfy $XX^\dagger=3I_3$, or $\mathrm{Re}\,\tau_{\rm r}(X)<0$, or contain a $2\times2$ Hadamard submatrix.
- A **corner-routing** argument turning this local statement into a global finite-corner witness, using $BB^\dagger=6I_3-EE^\dagger\Rightarrow\tau_{\rm r}(E)=-\tau_{\rm r}(B)$.
- Complete treatment of the Fourier-block case (all four $3\times3$ blocks Hadamard) and explicit finite-corner witnesses for the entire three-parameter Karlsson family, including its degenerate seams.
- Singular-corner lemma: any singular $3\times3$ submatrix forces a $2\times2$ Hadamard submatrix, hence $H_2$-reducibility.

**How it works** Haagerup's identity is re-derived from two "residual pairs" of entries, yielding two polynomials $\Phi_H,\Gamma$ quadratic in $y$; eliminating $y^2$ gives a linear eliminant $\mathcal A(x)+\mathcal B(x)y=0$ with $\mathcal A=x(|R|^2-|T|^2)\kappa_S(x)$, $\kappa_S(x)=2\bar Sx^2-(|S|^2+3)x+2S$. Infinitude forces $|\mathcal A|=|\mathcal B|$ on $\mathbb T$, so $QQ^\#=|\delta|^2\kappa_s^2$; unique factorization splits by $s=|S|$ into monomial ($s=0$, Fourier), Möbius ($0<s<1$, giving $\mathrm{Re}\,\tau<0$ via log-derivative sums of $p_u(z)=z^3-sz^2+usz-u$), and common-root ($1\le s\le3$, forcing $s=z=1$, hence a $(1,u,-u)$ row and a $2\times2$ Hadamard block) cases. Karlsson coverage uses exact resultants (245 pairwise), quotient-ring elimination, a half-angle reciprocal symmetry $A(1/t,p)=SB(t,p)D$, and a Bernstein/de Casteljau positivity certificate (degree $16\times8$, ten dyadic boxes) for the residual polynomial.

**Why it matters** Order six is the first dimension where continuous families and an isolated point coexist; its classification has been open since Haagerup (1997). A finite, branch-complete reconstruction procedure gives a rigorous framework for MUB existence in $d=6$ and for designing balanced six-mode interferometers.

**Caveats** The proof takes as black boxes Karlsson's $H_2$ classification and Szöllősi's cubic-root row/column criterion. Parts are computer-assisted (resultants, Bernstein subdivision) with only a bounded Lean audit; the "boundary of the Lean audit" is explicitly delimited. The result is a finite-incidence reduction — it certifies that each class is reachable, not an explicit new closed-form parametrization; the truncated source prevented checking the four-phase geometry section in detail.

## 8. Computationally Efficient Optimization of Per-Qubit Clifford Deformation for Non-uniform Biased Noise

[arXiv:2608.17870](https://arxiv.org/abs/2608.17870) · [SciRate](https://scirate.com/arxiv/2608.17870)

*Won Joon Yun, Andrew Nemec, Jonathan M. Baker*

**TL;DR** Chameleon replaces decoder-in-the-loop search for per-qubit Clifford deformation with a decoder-free surrogate: a Bhattacharyya upper bound on the probability that a low-weight "ambiguity operator" (a logical coset representative) causes a maximum-likelihood decoding confusion. Because the bound factorizes into one per-qubit term, scoring a candidate frame costs O(|L|n) instead of millions of Monte Carlo shots, cutting frame selection for the [[72,12,6]] BB code from ~1.2 days to 3.1 minutes while lowering worst-axis LER by 13%/7%/4% on average (surface/color/BB) versus the best prior baseline.

**Key contributions**
- Type-A vs. Type-B failure decomposition: only "true" ML ambiguity (λ(e′)≤λ(e_true)) is targetable by deformation; approximate decoders contribute up to ~86% Type-B failures, which are attributed to the decoder stack.
- Analytic bound Γ_ℓ(F)=∏_{q∈ℓ} 2√(r_c^q(1−r_c^q)), derived by replacing the indicator with √(P(e)P(e⊕ℓ)) and factorizing over independent per-qubit noise, reducing per-operator cost from O(2^w) to O(w).
- Reusable, code-only (noise-independent) ambiguity LUT; exhaustive up to W=d+2 for geometric/small BB codes, randomized Gaussian elimination plus BB translation orbits (W=d+10, 800 iterations) for BB72 where exact enumeration is PiB-scale.
- Two-stage cross-entropy search: 15×200 candidates over {I,H}^n, warm-starting a categorical CEM over the full S_3^n frame space, deployed only if it improves U by τ=20%.
- Objective variants for worst-axis memory (min max{U_X,U_Z}) and single-axis workloads (magic-state prep: 0.34×–0.67× LER_Z relative to two-axis optimization).

**How it works** Per-qubit frames permute (p_X,p_Y,p_Z), changing the marginals r_X=p_X+p_Y, r_Z=p_Z+p_Y presented to each CSS decoding class. Minimizing ΣΓ_ℓ is equivalent to maximizing a weighted distance −log Γ over the most vulnerable logical confusions, which requires coordinating frames across qubits in an operator's support — precisely what Tiurev et al.'s per-qubit local rule misses (it loses to undeformed CSS in 27% of 1,756 instances; global patterns lose in 29%).

**Why it matters** Deformation is free at the hardware level, and Willow calibrations show 43% of qubits with η>1.5. A calibration-refresh-speed compiler makes bias-adaptive frames practical for surface, color, and qLDPC codes alike; the surrogate is also a reusable code-analysis tool.

**Caveats** Surrogate ranking degrades badly on weakly biased devices (ρ=0.34 on IBM Miami, surface code). Gains over the best prior baseline are within noise or negative for color d5 and BB18/BB36 on real maps; the headline numbers lean on synthetic η=10 fields (up to +357%). Results are phenomenological; circuit-level (Si1000, biased idling only) gives just 5.2% average over CSS. Step 3 is dead weight on current transmons (no Y-dominant qubits). CDSC is given only 24 candidates in the main table, and LER is measured as Type-A only, which excludes the failure mode dominating approximate decoders actually deployed here.

## 9. No extension of the Quantum Tensor Product admits a Superposition principle

[arXiv:2608.17572](https://arxiv.org/abs/2608.17572) · [SciRate](https://scirate.com/arxiv/2608.17572)

*Vincenzo Fiorentino, Kuntal Sengupta*

**TL;DR** The authors give a theory-independent, prepare-and-measure definition of superposition in Generalised Probabilistic Theories: an extremal state is a superposition of a subset of a maximal perfectly-discriminable (MPD) set if it spreads its probability strictly between the corresponding outcomes of a maximally-distinguishing extremal (MDE) measurement. From this they derive three inequivalent "superposition principles" and show that, assuming the no-restriction hypothesis, no non-signalling composition of quantum systems strictly larger than the quantum tensor product satisfies the *mutual* superposition principle — singling out the quantum tensor product operationally.

**Key contributions**
- Operational, *relational* definition of superposition (Def. 1): $r\in\mathrm{Ext}[\mathcal S]$ with $e_j(r)\in(0,1)$ for all $e_j\in\mathsf M'\subseteq\mathsf M$ and $\sum_{\mathsf M'}e_j(r)=1$; maximality of the discriminable set is essential (a qutrit counterexample shows why).
- Three principles — complete, uniform, mutual — proven *not* to form a hierarchy, via constructed toy theories GPT-1 (uniform+mutual, not complete) and GPT-2 (uniform only).
- Classification table across classical, quantum, GLT, Boxworld, Spekkens' toy theory, regular $n$-gons; notably Spekkens' toy model satisfies all three principles (via the equivalence-balance principle), Boxworld only bare existence, GLT/classical none.
- Main theorem: any $\mathcal S_{\mathcal Q_{1,2}}\subsetneq \mathcal S_{\mathcal Q_1}\boxtimes\mathcal S_{\mathcal Q_2}\subseteq \otimes_{\max}$ fails mutual superposition; corollary: no strict extension admits all three principles plus no-restriction.
- Structural transfer lemmas: if the composite's operational dimension is $d_1d_2$, existence and complete superposition inherit from *one* subsystem (which may even be composed with a simplex — a genuine difference from Aubrun et al.'s non-simpliciality-based notion); uniform superposition inherits under "outcome sharpness of MDEs".
- Entanglement (any composition strictly above $\otimes_{\min}$, same dimension condition) implies superposition; converse false. Preparational uncertainty (disjoint deterministic sets of two MDEs) implies complete superposition, and uniform superposition under sharpness; existence/weak uncertainty are restated purely in superposition terms.

**How it works** Standard finite-dimensional GPT machinery (compact convex state space, dual effects, min/max tensor products), with operational dimension defined via MPD-set cardinality. Quantum superposition $|\psi\rangle=\sum_i c_i|\phi_i\rangle$ is recovered because $|c_i|^2=\mathrm{tr}[\Phi_i\Psi]\in(0,1)$ are exactly the MDE statistics. The maximality theorem exploits that a non-quantum extremal state in a larger composition cannot be reciprocally embedded in an MPD set containing the states it superposes.

**Why it matters** Provides a candidate operational axiom replacing the tensor-product postulate (given quantum subsystems), and a formalism-free notion of superposition relevant to gravitationally-induced-entanglement and indefinite-causal-order tests, where "holding a mass in superposition" currently lacks operational meaning.

**Caveats** Subsystems must be assumed quantum; no single-system reconstruction. Heavy assumptions: informational completeness of MDEs, no-restriction hypothesis, multiplicativity of operational dimension (which fails, e.g., for pentagon compositions), outcome sharpness. Superposition is defined only for extremal states. Odd behaviour in $n$-gons (a state can superpose a set yet be perfectly discriminable from members; even/odd parity gap in uniform superposition) is unexplained. Finite dimensions only; proofs are in a truncated appendix.

## 10. A Simple Algebraic Proof of the PCP Theorem

[arXiv:2608.17429](https://arxiv.org/abs/2608.17429) · [SciRate](https://scirate.com/arxiv/2608.17429)

*Prashanth Amireddy, Amik Raj Behera, Srikanth Srinivasan, Madhu Sudan, Sophus Valentin Willumsgaard*

**TL;DR** The authors give an algebraic proof of the PCP theorem (3-COLOR ∈ PCP[O(log n), O(1)]) that uses no PCP composition, no PCP-of-proximity/robustification machinery, and no appeal to NP-completeness inside the construction — only code concatenation, interpolation, and polynomial multiplication. The enabling technical idea is a "set-multilinear" re-encoding of univariate low-degree polynomials that makes the lines-table of a low-degree test locally testable and self-correctable with O(1) bit queries, removing the bottleneck that previously forced composition.

**Key contributions**
- A composition-free algebraic PCP: the verifier and the honest prover each fit in roughly one page of pseudocode (appendix), with the prover described purely via multivariate polynomial interpolation/evaluation.
- The set-multilinear encoding $\Psi_{d,c,m_1}$: a univariate $P$ of degree $<m_1^c$ is mapped to a *set-multilinear*, hence total-degree-$c$, polynomial in $c$ blocks of $m_1\approx d^{1/c}$ variables, obtained by writing exponents in base $m_1$ (a "set-multilinearized inverse Kronecker map"). Evaluation at $\lambda$ is recovered by evaluating at the explicit point $\Phi_{c,m_1}(\lambda)=((\lambda^{j m_1^{i}})_{j})_i$.
- Because $c=O(1)$, the encoding is tested by the plain Rubinfeld–Sudan degree-$c$ test with $c+2$ queries over $\mathbb{F}_q$, and self-corrected via $P(\mathbf u)=\sum_{i=1}^{c+1}P(\mathbf u+\zeta^i\mathbf v)$ where $\zeta$ has order $c+1$ (char-2 fields make all interpolation coefficients equal 1).
- Combination with a degree-$r$ Hadamard ("low-degree long code") over $\mathbb{F}_2^{t}$, $t=O(\log\log n)$, including the fact that $\mathrm{Had}_1[P\circ f](\mathbf a,L)=\mathrm{Had}_r[f](\mathbf a,\Lambda_{P,L})$, letting degree-$r$ algebraic relations be checked with O(1) bits.

**How it works** Start from the BFL/ALMSS-style arithmetization of 3-coloring, with the sum-check replaced by the single-extra-polynomial "vanishing certificate" $\mathcal M_P$ (from Combinatorial Nullstellensatz) of the authors' earlier work: everything reduces to one low-degree test plus constant-degree algebraic checks on O(1) queried values. The lines table $f_{\mathrm{lines}}:\mathbb F_q^{2m}\to\mathbb F_q^{d+1}$ is the only object whose symbols are too long ($d\log q$ bits) for direct long-code concatenation (which would give quasipolynomial proofs). Replacing each line polynomial by its set-multilinear encoding, then concatenating with the Hadamard code, yields O(1)-bit queries and O(log n) randomness.

**Why it matters** This is the most self-contained algebraic PCP route to date, plausibly teachable in a course, and it clarifies that low-degree testing (not composition per se) was the real obstruction; the explicit honest prover makes the *content* of a PCP proof legible.

**Caveats** The test only certifies proximity to *some* degree-$c$ multivariate polynomial, giving a univariate of degree $O(cd)$ rather than $\le d$ — enough for soundness here but a weakened guarantee. It still relies on the ALMSS line-point test (requiring $q>Cd^3$) and an auxiliary proof oracle, which the authors concede may count as "0.5 compositions" à la Goldreich. Constants (query count, soundness $\gamma$) are unspecified/small, and no improvement in proof length or parameters is claimed.
