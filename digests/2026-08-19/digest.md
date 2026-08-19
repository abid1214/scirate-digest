# SciRate Daily Digest — 2026-08-19

The top 10 papers on [SciRate](https://scirate.com/) today.

## 1. Non-CSS Quantum Code Embedding

[arXiv:2608.16995](https://arxiv.org/abs/2608.16995) · [SciRate](https://scirate.com/arxiv/2608.16995)

*Andrew C. Yuan, Nouédyn Baspin*

**TL;DR** — This work lifts the chain-complex ("cone") machinery that underpins CSS surgery, weight reduction, and Euclidean (Layer-code) embeddings to *arbitrary* stabilizer codes, by replacing the CSS complex $X\to Q\to Z$ with a **symplectic complex** $S\xrightarrow{\sigma}P\xrightarrow{\hat\sigma}\bar S$ in which $P$ is an $\mathbb{F}_2$ symplectic space and $\hat\sigma$ is the symplectic adjoint. The central object (Thm. "symplectic embedding", ~2 pages) is a height-2 cone with a *defect map* $p$; when $p=0$ the construction is exactly "measure a set of mutually commuting Paulis," yielding non-CSS logical measurement (e.g. $Y$-type), non-CSS qLDPC surgery, non-CSS Layer codes and non-CSS weight reduction without ad hoc local Clifford tricks.

**Key contributions**
- A symplectic-complex generalization of the CSS cone framework of Phys. Rev. A 113, 022438; commutation of stabilizers becomes $\hat\sigma\sigma=0$, and measurability of an ancilla connectivity map $g:X^A\to P^D$ becomes $\hat g g=0$ (defect $p=0$).
- Non-CSS logical measurement algorithm with an explicit readout formula: the logical outcome is $\langle \hat g\,\tilde e(P^D)\,|\,\bar{\mathcal X}^A\rangle+\langle \delta^A x^A\,|\,p\,\mathcal X^A\rangle$, i.e. a $p\neq 0$ correction term absent in the CSS case.
- A unified non-CSS code gadget: *one* set of check qubits $Q(S^D)$ initialized in $X$, $O(1)$-depth CNOT circuits for the $X$-sector $\sigma_X$ plus CZ circuits for the $Z$-sector $\sigma_Z$, measured in $X$; readout $\hat\sigma^D\tilde e(P^D)+e(\bar S^D)$.
- Detailed CSS/non-CSS parallel derivations showing the only difference between "high-level" (ideal) and circuit-level measurement is the check-qubit initialization error $e(\bar S)$ appearing as a measurement error.
- Claimed straightforward generalization of qLDPC surgery, Layer codes (optimal 3D Euclidean embedding) and quantum weight reduction to non-CSS inputs.

**How it works** — CNOT (control ancilla, target $X$-sector) and CZ (targeting the $Z$-sector) conjugation act on the symplectic vector of Paulis as the block-lower-triangular matrix $\begin{psmallmatrix} I&&\\ g&I&\\ &\hat g&I\end{psmallmatrix}$ — precisely a height-2 cone with $p=0$. Error propagation and the residual stabilizer group are then read off algebraically: after measurement the state is stabilized by $\operatorname{im}\sigma^D\cap\ker\hat g+\operatorname{im}g$ with physical error $e(P^D)+\ell(P^D)$ mod logicals. Fault tolerance is argued by building a spacetime fault complex over $T\ge d$ rounds and applying Gottesman's generic min-weight correction.

**Why it matters** — Most high-rate qLDPC codes and many bias-tailored/XZZX-style codes are non-CSS, and $Y$-type logical measurement is needed for a full Clifford+ gate set; this removes the CSS restriction from the main compilation-level tools. Relevant to anyone designing surgery schedules, weight-reduced codes, or 3D-local embeddings.

**Caveats** — The visible source contains no numerics, no distance-preservation theorem, and no threshold simulation; the threshold is asserted generically. The ancilla is assumed to have no internal logicals ($\ker\delta^A=\operatorname{im}\delta^A$) and to be qLDPC/low-overhead; measurements are assumed perfect and gadgets $O(1)$-depth. Overhead (qubit count, LDPC-ness of the resulting non-CSS deformed codes) is not quantified in the retrieved text, and the main theorem itself was truncated from the excerpt.

## 2. Quantum simulation of slow analytic time-dependent Hamiltonians

[arXiv:2608.17653](https://arxiv.org/abs/2608.17653) · [SciRate](https://scirate.com/arxiv/2608.17653)

*Chenhao Zhao, Yinan Li, Dong An*

**TL;DR** The authors give a Floquet-based algorithm for "slow" Hamiltonians $\widetilde H(t)=H(t/T)$ with analytic (or Gevrey) $H$, achieving query complexity $\widetilde{\mathcal O}(\alpha T+\log(1/\varepsilon))$ — additive rather than the multiplicative $\alpha T\log(1/\varepsilon)$ of truncated Dyson — while keeping additional gate overhead polylogarithmic in $1/\varepsilon$ (though quadratic in $\alpha T$). The enabling technical tool is an explicit periodic Gevrey extension of $H(s)$ from $[0,1]$ to a 2-periodic function, with matching Fourier-decay and Floquet-truncation bounds.

**Key contributions**
- A constructive periodic extension: a Gevrey-$\tau$ Borel-lemma construction $F_\tau(x)=\sum_k \frac{H^{(k)}(1)}{k!}x^k\chi_\tau(R_kx)$ (and analogously at $s=0$) that matches *all* derivatives at both endpoints, yielding a $C^\infty$, Gevrey-$\varrho$ ($\varrho=\sigma+\tau-1$) periodic Hamiltonian agreeing with $H$ on the physical interval. Explicit derivative bounds $\lesssim C(32e^{\sigma-1+1/e}D)^n(2C_{\tau,2})^{n-1}(n!)^{\varrho}$ are proved.
- Fourier-coefficient decay and a Lieb–Robinson-type bound for Gevrey (not analytic) periodic Hamiltonians, extending Mizuta–Fujii's analysis, which only covered exponentially decaying modes; this gives the Floquet-space truncation order $l_{\max}$.
- Complexity: $\widetilde{\mathcal O}(\alpha T+\log(1/\varepsilon))$ queries, $\widetilde{\mathcal O}((\alpha T+\log(1/\varepsilon))^2\log(1/\varepsilon))$ extra gates; for control Hamiltonians $H(s)=\sum_j\alpha_j(s)M_j$ only block encodings of $M_j$ are needed and the gate overhead drops to $\widetilde{\mathcal O}((\alpha T+\log(1/\varepsilon))^2)$.
- Gevrey class $1\le\sigma<2$: $\widetilde{\mathcal O}((\alpha T+\log(1/\varepsilon))^\sigma)$ queries — an explicit regularity/complexity trade-off.
- Combined with optimal LCHS, slow analytic semi-dissipative ODEs are solved with $\widetilde{\mathcal O}(\frac{\|u_0\|}{\|u(T)\|}\alpha T\log(1/\varepsilon))$ queries, a quadratic improvement in precision dependence over Low–Somma.

**How it works** Extend $H$ periodically (Step 1), Fourier expand and lift to the infinite-dimensional Sambe/Floquet space with $\mathscr H_{\rm eff}=\sum_l|l\rangle\langle l|\otimes(\widetilde H_0-l\omega)+\sum_{l,m}|l\rangle\langle l+m|\otimes\widetilde H_m$, truncate at $l_{\max}=\Theta(\alpha T+\log 1/\varepsilon)$ (analytic case) using the Gevrey Lieb–Robinson bound, block-encode the truncated (periodic-boundary) effective Hamiltonian by LCU over Fourier modes, and run QSVT for $e^{-i\mathscr{H}_{\rm eff}T}$; approximate translation symmetry plus oblivious amplitude amplification recovers $|\psi(T)\rangle$ with $O(1)$ success amplitude. Fourier coefficients are obtained from quadrature on $H'$ plus endpoint-derivative data (general case) or computed classically (control case).

**Why it matters** It answers, for a restricted but physically relevant class (adiabatic/annealing-style control paths), whether additive query scaling can coexist with polylog-in-$1/\varepsilon$ gate counts — a gap left open by the concurrent transducer-based result of Chen et al., which is query-optimal for Lipschitz Hamiltonians but has $\mathrm{poly}(1/\varepsilon)$ gate overhead.

**Caveats** The input model is nonstandard: HAM-T for $H'(s)$ plus block encodings of endpoint derivatives $H^{(k)}(0),H^{(k)}(1)$ up to order $\widetilde{\mathcal O}(\log\alpha T+\log 1/\varepsilon)$ — so this is not a strict improvement over HAM-T results. Regularity constants $C,D,\sigma,\tau$ are treated as $T,\varepsilon$-independent constants and could hide large prefactors. Gate overhead is quadratic in $\alpha T$, worse than Dyson's linear scaling. The "nearly additive" bound reflects $\varrho\to1^+$ only in a limit (the extension is never analytic). No numerics; locality/commutator structure is not exploited.

## 3. Nearly Sample-Optimal Estimators for Quantum Rényi and Tsallis Entropies

[arXiv:2608.18070](https://arxiv.org/abs/2608.18070) · [SciRate](https://scirate.com/arxiv/2608.18070)

*Kean Chen, Qisheng Wang*

**TL;DR** Two new estimators close the remaining sample-complexity gaps for quantum Rényi entropy (all non-integer α) and Tsallis entropy (0<α<1), matching Wang's recent lower bounds up to polylogs. For 0<α<1 the cost is O(d^{1+1/α}/ε^{1/α} + d^{1/α−1}/ε²) (Rényi) and O(d^{1+1/α}/ε^{1/α} + d^{2−2α}/ε²) (Tsallis), improving on the previous O(d^{2/α}/ε^{2/α}); for non-integer α>1 the Rényi cost is O(d²/ε^{1/α} + d^{1−1/α}/ε²), improving O(d²/ε²).

**Key contributions**
- A first-order (tangent-line) estimator of F_α(ρ)=tr(ρ^α) for 0<α<1 built on Bures χ²-accurate tomography rather than weak Schur sampling.
- A new two-sided inequality: for σ ⪰ (d/n)I, 0 ≤ (1−α)tr(σ^α)+α tr(ρσ^{α−1}) − tr(ρ^α) ≤ (d/n)^{α−1} D_{χ²}(ρ‖σ), proved via concavity plus a Taylor-integral bound on the Hessian of A↦tr(A^α) with dominated convergence.
- Proof that regularizing the tomography output as σ = ρ̂ + (2d/n)I gives D_{χ²}(ρ‖σ) = O(d²/n).
- A Richardson-extrapolation scheme over batch sizes for α>1: bias of Hayashi pure-state estimation on random purifications expands in Beta-moments μ_j(s), which are cancelled by k=⌈α⌉−1 batches.
- Completes Table 1: tight (up to polylogs) sample complexities across all α for both entropy families.

**How it works**
For 0<α<1: run χ²-Bures tomography (Piroli–Styliaris–et al.-style guarantee) on n samples, form σ = ρ̂ + (2d/n)I, compute (1−α)tr(σ^α) classically, and estimate α tr(ρσ^{α−1}) by measuring m fresh copies in σ's eigenbasis (outcome value s_J^{α−1}). Bias is O(d^{α+1}/n^α) from the χ² inequality; variance is controlled by second-moment bounds on s_J^{α−1} that split into cases α≤1/2, α>1/2 (additive), and α>1/2 (relative, using tr(σ^α) ≲ F via Hölder). Choosing n ≍ d^{1+1/α}/ε^{1/α} and m per regime gives the stated bounds.
For α>1: convert copies of ρ into i.i.d. copies of a Haar-random purification |ψ⟩ (conjugate-symmetry channel), apply Hayashi's covariant POVM to a batch of s copies. The outcome coefficient matrix is √(1−T)M + √T G with T ~ Beta(d²−1, s+1) and G uniform on the orthocomplement sphere; a Schatten-norm Taylor expansion yields E[tr(ρ̂^α)] = F + Σ_j c_j μ_j(s) + O(F(d²/s)^α). Batch sizes s_ℓ = 2^ℓ m with coefficients solving Σa_ℓ=1, Σa_ℓμ_j(s_ℓ)=0 kill the leading terms; variance O(F²[d^{1−1/α}/m + (d²/m)^{2α}]) then gives relative error θ ≍ ε and hence additive Rényi error.

**Why it matters** Rényi/Tsallis entropies underpin entanglement quantification, quantum thermodynamics, and property testing; the α<1 regime in particular was off by a factor d^{1/α−1}/ε^{1/α}. The Bures-χ² tangent-line technique is a reusable recipe for estimating concave spectral functionals from tomography, and the Richardson/Beta-moment cancellation is a clean tool for debiasing pure-state estimation.

**Caveats** Constants blow up as α→1⁻ (e.g. (1−α)^{−(2α−1)/α}) and as α→integer for α>1 (k grows, coefficient conditioning); only non-integer α>1 is covered for Rényi. Estimators are fully collective/entangled-measurement (tomography, Hayashi POVM, purification channel) with no stated time complexity. Success probability is constant (0.98/24/25) — median amplification would add log factors. Bounds still leave polylog gaps, and the α>1 Tsallis and integer-α cases are inherited from prior work.

## 4. Quantum Circuit for General Unitary: Improved T-count via Block Flattening and Dilation

[arXiv:2608.17846](https://arxiv.org/abs/2608.17846) · [SciRate](https://scirate.com/arxiv/2608.17846)

*Pei Yuan, Shengyu Zhang, Wei Zi*

**TL;DR** The paper gives a Clifford+T synthesis scheme for an arbitrary classically specified $n$-qubit unitary with worst-case T-count $O(2^{5n/4}L^{5/8}\log 2^n)$, where $L=n+\log(1/\epsilon)$, improving the previous best $\tilde O(2^{4n/3})$ (Tan) and narrowing the gap to the $\tilde\Omega(2^n)$ lower bound to $\tilde O(2^{n/4})$. The trick is to treat $U$ as one block-encoded object: randomized sign diagonals "flatten" all $b\times b$ blocks, Halmos dilations of the normalized blocks are packed into a single SELECT, and QSVT maps the resulting uniform singular value $1/\rho$ exactly to 1.

**Key contributions**
- *Simultaneous block flattening*: for any $U\in\mathrm U(d)$ there exist Boolean phase oracles $D_1,D_2$ with $V=H_dD_1UD_2H_d$ satisfying $\|P_IVP_J^\dagger\|\le O(\sqrt{b/d}\log d)$ for **all** $D^2$ block pairs.
- A *block-dilation SELECT* turning all normalized blocks into a single uniformly-controlled unitary, yielding a block encoding of $V$ with normalization $\rho=Dg=O(\sqrt{d/b}\log d)$ while each dilation acts only on $2b$ dimensions.
- *Robust one-point oblivious amplification*: a degree-$Q=\Theta(1/c)$ QSP polynomial with $P(c)=1$ exactly, plus perturbation analysis showing $\|A_{\rm amp}-V\|=O(Q^2\delta)$ and clean-input error $O(Q\sqrt\delta)$.
- Extension to multiplexed unitaries $\sum_x|x\rangle\langle x|\otimes U_x$ via a *single* pair of sign diagonals flattening all branches at once.

**How it works** Stage one flattens entries: a random Rademacher diagonal $D_2$ makes $\max_{pq}|(UD_2H_d)_{pq}|=O(\sqrt{\log d/d})$ (Hoeffding + union bound), bounding row norms of each column slab by $\mu=16(b/d)\ln 2d$. Stage two applies a second random diagonal $D_1$ and Tropp's rectangular matrix Rademacher bound to control every block's operator norm, failing with probability $<2^{-7}$. Normalized blocks $C_{IJ}=V_{IJ}/g$ are contractions, dilated by Halmos to unitaries and packed into a $(2r,k+1)$-UCU; Hadamards on the block-label registers plus a swap give $J_0^\dagger WJ_0=V/\rho$. Tan's UCU compiler implements one query in $O(d\sqrt L+b^2L)$ T gates; $O(\rho)$ QSVT queries give total $O(\sqrt{d/b}\log d\,[d\sqrt L+b^2L])$, minimized at $b=d^{1/2}L^{-1/4}$.

**Why it matters** Fault-tolerant compilers pay almost exclusively for T gates; this is the first improvement in the leading exponent for generic unitary synthesis since Tan, and it shifts the paradigm from recursive cosine–sine products to block-encoding + QSVT.

**Caveats** Ancilla cost balloons to $O(2^n\sqrt L)$ clean qubits (vs. $O(d^{2/3}L^{1/3}+L)$ for Tan) — this is a space–T tradeoff, not a strict improvement. Results hold only for $L\le d$. Finding the sign diagonals requires randomized classical preprocessing with certified numerical verification of $D^2$ block norms, explicitly excluded from the resource count. No numerics or constant-factor analysis; the $\tilde O(2^{n/4})$ gap to the lower bound remains open.

## 5. Lie-Algebraic Classical Simulation of Bosonic Systems Beyond Gaussian Dynamics

[arXiv:2608.17094](https://arxiv.org/abs/2608.17094) · [SciRate](https://scirate.com/arxiv/2608.17094)

*Adelina Bärligea, Timothy Heightman, Jakob S. Kottmann, Antonio Acín*

**TL;DR** The paper extends Lie-algebraic (g-sim) classical simulation to bosons by replacing the dynamical Lie algebra with an *observable-seeded reachable operator module* — the smallest space containing the observable that is invariant under commutation with the circuit generators. Whenever this module has polynomial dimension and input overlaps are accessible, mean values, fixed-order/multi-time/OTOC correlators and reverse-mode gradients are exactly computable in polynomial time, recovering Gaussian optics as a special case and covering genuinely non-Gaussian dynamics (Kerr, cross-Kerr, pair hopping) at bounded photon number.

**Key contributions**
- Reachable-module simulability criterion (Thm. 1): exact evaluation ⟨O(θ)⟩ = wᵀe^{θ_L A_{k_L}}···e^{θ_1 A_{k_1}}e^in with D×D matrices, D = dim V(O); no Fock cutoff, moment closure, or perturbative truncation. The usual poly-dimensional DLA condition is recovered only when O ∈ 𝔤 and is shown sufficient but not necessary.
- Three finiteness mechanisms for bosons: (i) Gaussian degree preservation, dim V(O) ≤ binom(2n+m, m) for degree-m quadrature polynomials (m=1,2 reproduce mean/covariance propagation, valid for *non-Gaussian* inputs given accessible input moments); (ii) photon-number sector confinement, d_{n,N}=binom(N+n−1,N)=Θ(n^N), giving dim V ≤ O(n^{2N_max}) with arbitrary interaction strength and poly depth; (iii) a multi-mode nilpotent polynomial-phase family with cubic-and-higher generators.
- Negative result specific to bosons: a finite-dimensional generator algebra does *not* guarantee a finite observable orbit (e.g. Kerr acting on â on the full Fock space).
- Controlled perturbative hierarchy for squeezing: parity-resolved photon-number bands of depth k reproduce number-conserving dynamics through order 2k+1, leading error at O(λ^{2(k+1)}), sharpened via photon-number-tail bounds for squeezed vacua; error orders confirmed numerically.
- Numerics: operator spreading/OTOCs on interacting chains up to 400 modes, repulsively bound doublon band with flux-reversed edge motion, differentiable control validated against finite differences on lattices up to 9×9, depths 1–8.

**How it works** Heisenberg-picture propagation is done entirely in a finite real operator space: pick a basis of V(O), express ad_{H_k} as matrices A_k, and contract the observable coefficients against input overlaps Tr[B_α ρ_in] through matrix exponentials. Correlators follow from expanding each Heisenberg-evolved factor in its own module and contracting against ordered input-moment tensors E^in; gradients from differentiating the same matrix product.

**Why it matters** It clarifies that bosonic classical simulability is a property of the (dynamics, observable) pair rather than the Hamiltonian alone, giving a unified taxonomy that reconciles Gaussian tractability with boson-sampling hardness (which lives in growing-order coincidence observables) and supplies exact benchmarks for non-Gaussian CV devices.

**Caveats** Outputs are mean values/fixed-order correlators, not samples or full distributions. Efficiency hinges on unstated-cost primitives: accessible restricted generators and input overlaps/moment tensors, which may be nontrivial for realistic non-Gaussian inputs. Sector results require N_max = O(1) and ρ_in supported in the retained sectors; squeezing extension needs explicit analyticity assumptions and is only asymptotically controlled. Domain/unboundedness issues are handled by assuming a common invariant domain.

## 6. Hardware-Aware Compilation and Execution of Bivariate Bicycle Codes on Neutral-Atom Systems

[arXiv:2608.17023](https://arxiv.org/abs/2608.17023) · [SciRate](https://scirate.com/arxiv/2608.17023)

*Jason Ludmir, Aditya Ranjan, Nicholas S. DiBrita, Jason Han, Tirthak Patel*

**TL;DR** Park-n-Ride is a compiler/execution model that maps bivariate-bicycle (BB) qLDPC code primitives — idle syndrome rounds, shift automorphisms, in-module and inter-module logical measurements, T-injection — onto zoned neutral-atom arrays while respecting AOD non-crossing, blockade and zoning constraints. Its central techniques are a columnar module layout with three subzones, a torus-periodicity-based decomposition of shift automorphisms into parallel monotone "rolls" plus a staggered resync sweep, and spectral-seriation placement of modules; the latter cuts estimated end-to-end runtime ~18% and transport-induced atom-loss exposure ~41% versus arbitrary placement at up to 113 gross-code modules (~32.5k physical qubits).

**Key contributions**
- A hardware-aware module/zone abstraction: compute columns of stacked BB modules, each split into idling, bridge-interaction, and shift/measurement subzones, with a per-module "logical processing unit" holding bridge and ancilla rows.
- Direction-agnostic shift-automorphism scheduling: $T(\Delta i,\Delta j)=\mathrm{Roll}_i\circ\mathrm{Roll}_j$ with each roll realizable as a width-$k$ or width-$(N-k)$ strip move, so a column head fixes shared directions and all modules move monotonically in parallel; residual offsets from heterogeneous shift magnitudes are removed by a sorted-residual sweep with staggered SLM drop-offs (moves = number of distinct residuals ≤ #modules).
- Interval-coloring bridge scheduler for joint measurements: pairs become column intervals, greedy coloring into disjoint rounds, then lockstep ±1 column micro-steps to a midpoint rendezvous, guaranteeing non-crossing.
- Spectral (Fiedler-vector) seriation of the joint-measurement interaction graph into column-capacity blocks; plus a 24-substep wrap-class-partitioned idling stabilizer schedule and a per-column T-factory queueing model.

**How it works** A BB-native tableau becomes a dependency DAG, layered for maximal module-disjoint parallelism, then split into shift/measurement sublayers; modules move only within their column between subzones. Runtime is estimated analytically from AOD distances (55 µm/µs), 100 µs SLM↔AOD trap switches, 0.8/2.0 µs two-/one-qubit pulses, with module footprint 120×60 µm and column extent 4.3 W_mod.

**Why it matters** Most qLDPC compilation work is code-theoretic or superconducting-centric; this is one of the first concrete motion schedules for BB-code logical operations under AOD ordering constraints, showing that shifts are essentially free (no two-qubit gates, error curve orders of magnitude below others) while syndrome/measurement cycles dominate, and that placement can substitute for column capacity (spectral@cap-6 beats arbitrary@cap-10).

**Caveats** No prior-art baseline exists, so all comparisons are internal placement heuristics. Results come from an analytic timing estimator, not circuit-level noise simulation; the logical-error curve uses a toy oracle decoder ($\Pr[\mathrm{Binom}(N_{\rm ref},q)\ge 5]$). Measurement time is zeroed by construction, and the two-gross scaling claim (<0.1% runtime increase despite doubled module height) is asserted from re-analysis rather than recompilation. Benchmark circuits are synthetic (10 ops/module, 25% joint measurements), and magic-state distillation is abstracted to a single-server queue.

## 7. A Complete Classification of Complex Hadamard Matrices of Order Six

[arXiv:2608.18053](https://arxiv.org/abs/2608.18053) · [SciRate](https://scirate.com/arxiv/2608.18053)

*Mateo Cárdenes Wuttig, Joseph Tindall*

**TL;DR** The authors claim to close the long-open order-six complex Hadamard classification by showing that *every* $6\times6$ CHM is equivalent to a dephased matrix possessing a "finite-corner witness" — a $3\times3$ corner whose two complementary-block fixed-Gram fibers are finite — so that the entire class set is generated by Szöllősi's dilation from finitely many algebraic solves. The engine is a cubic Gram invariant $\tau_{\rm r}=(XX^\dagger)_{12}(XX^\dagger)_{23}(XX^\dagger)_{31}$ that flips sign between complementary blocks, plus a trichotomy showing infinite fibers force $XX^\dagger=3I$, $\mathrm{Re}\,\tau_{\rm r}<0$, or an embedded $2\times2$ Hadamard block.

**Key contributions**
- A monomial-invariant $\mathrm{Re}\,\tau_{\rm r}$ with the identity $\mathrm{Re}\,\tau_{\rm r}(X)=\mathrm{Re}\,\tau_{\rm c}(X)$ (proved via equal spectra of $XX^\dagger$, $X^\dagger X$ and the $3\times3$ determinant expansion).
- **Infinite-fiber trichotomy** for invertible $X\in\mathbb T^{3\times3}$, obtained by a division-free elimination that retains common-root branches normally lost by cancellation.
- **Corner routing**: since $BB^\dagger=6I-EE^\dagger$ gives $\tau_{\rm r}(E)=-\tau_{\rm r}(B)$, swapping column/row triples always produces a corner with both fibers finite — the global step missing from Szöllősi's method, proving his conjecture.
- **Fourier-block alternative**: one Hadamard $3\times3$ block forces all four; a three-point Fourier/convolution argument ($\hat\alpha_j\hat A_j=0$) forces either $2\times2$ reducibility or all-cubic-root row *and* column, routing into Karlsson/Tao.
- Finite-corner witnesses for the whole Karlsson family, via exact resultants and a Bernstein positivity certificate.

**How it works** Haagerup's identity is rederived from residual coordinate pairs, giving two polynomials $\Phi_H,\Gamma$ quadratic in $y$; eliminating $y^2$ yields $\mathcal A(x)+\mathcal B(x)y=0$ with $\mathcal A=x(|R|^2-|T|^2)\kappa_S(x)$, $\kappa_S=2\bar Sx^2-(|S|^2+3)x+2S$. Unit-modulus forces $QQ^\#=|\delta|^2\kappa_S^2$; case analysis on $s=|S|$ (Möbius sums, root locations $r_-<s<1<1/s<r_+$) yields the trichotomy. For Karlsson, six corners on the affine-Fourier boundary are shown to have no common zero (245 resultants → 25 first-phase conditions → 18 branches excluded), the nondegenerate chart uses non-vanishing $|u|+|v|\le\sqrt2<\sqrt3$, and a $t\mapsto1/t$ reciprocal symmetry ($A(1/t,p)=SB(t,p)D$) plus exact dyadic de Casteljau subdivision (degree $16\times8$, ten boxes, all Bernstein coefficients positive) kills the residual $R$.

**Why it matters** Relevant to MUB existence in dimension six, balanced six-mode interferometry, and the defect/family structure of CHMs; it converts an open classification into a terminating algebraic procedure and validates the dilation approach.

**Caveats** The result is *conditional on two published inputs* (Karlsson's $H_2$-reducible completeness, Szöllősi's cubic-root criterion); it certifies finiteness/reconstructibility rather than exhibiting a new closed-form list, so it is unclear whether unknown families are ruled out. Substantial reliance on computer algebra with only a partial Lean audit ("precise boundary" acknowledged). Source is truncated before the reconstruction-geometry proofs; the quadratic+cubic claim excludes Tao's matrix and one Karlsson representative.

## 8. Computationally Efficient Optimization of Per-Qubit Clifford Deformation for Non-uniform Biased Noise

[arXiv:2608.17870](https://arxiv.org/abs/2608.17870) · [SciRate](https://scirate.com/arxiv/2608.17870)

*Won Joon Yun, Andrew Nemec, Jonathan M. Baker*

**TL;DR** Chameleon is a decoder-free compiler for choosing per-qubit single-qubit Clifford frames (the $6^n$ "Clifford deformation" space) under spatially non-uniform biased noise. It scores a frame by a Bhattacharyya upper bound on the failure probability of low-weight *ambiguity operators* (logical coset representatives), then minimizes this surrogate with cross-entropy search, cutting frame-selection time for the [[72,12,6]] BB code from ~1.2 days to 3.1 minutes while reducing worst-axis logical error rate by up to ~19% (surface) over the best prior baseline.

**Key contributions**
- An analytic, decoder-free surrogate: for an ambiguity operator $\ell$, $\Pr[\text{fail}]\le\prod_{q\in\ell}\gamma(r_c^q(F))$ with $\gamma(r)=2\sqrt{r(1-r)}$, derived from $\Pr(e)\le\sqrt{\Pr(e)\Pr(e\oplus\ell)}$ on the failure indicator plus factorization over independent per-qubit noise. Cost per operator drops from $O(2^w)$ to $O(w)$.
- Class scores $U_c(F)=\sum_{\ell\in\mathcal{A}_c}\Gamma_\ell(F)$ supporting either worst-axis memory objective $\min_F\max(U_X,U_Z)$ or single-axis objectives (e.g. magic-state prep).
- Offline, noise-independent ambiguity-set LUT reused across calibration maps; exhaustive up to weight $W=d+2$ for geometric/small BB codes, randomized Gaussian elimination + translation orbits for BB72 ($W=d+10$).
- Two-stage CEM: Bernoulli search over $\{I,H\}^n$ (3,000 candidates), then categorical search over all six frames, warm-started, deployed only if it beats binary by $\tau=20\%$.
- A Type-A/Type-B failure taxonomy separating information-theoretic decoding ambiguity from decoder suboptimality (approximate decoders reach ~86% Type-B).

**How it works** Frames only permute each qubit's $(p_X,p_Y,p_Z)$ as presented to the code, so distance, qubit count, and rounds are unchanged; only the presented marginals $r_{X},r_{Z}$ change. Minimizing $U_c$ is equivalent to maximizing a *weighted* distance $-\log\Gamma_\ell=\sum_q -\log\gamma$ on the most vulnerable logical confusions—explaining why the greedy per-qubit "local rule" of Tiurev et al. fails (it underperforms undeformed CSS in 27% of 1,756 instances).

**Why it matters** Calibration-aware deformation was previously gated by Monte-Carlo decoding in the loop; a microsecond-to-millisecond surrogate makes recalibration-rate adaptation feasible and is code-agnostic (surface, color, BB). Relevant to anyone building FTQC compilation stacks on transmons with heterogeneous bias.

**Caveats** Surrogate fidelity is bias-dependent: $\rho=0.34$ (surface) on low-bias IBM Miami vs 0.89–0.98 on Willow. Gains over the *best prior baseline* are modest and sometimes negative (color $d5$ Berlin −3%, BB36 Willow −3%, BB18 Miami −2%); large numbers (up to +357%) come from the synthetic $\eta=10$ field. Evaluation is mostly phenomenological; circuit-level (Si1000 with biased idling) yields only 5.2% mean gain vs CSS. Metric is Type-A LER, excluding decoder-induced failures. The bound sums operators independently (no correlation/double-count correction) and relies on incomplete, heuristically enumerated ambiguity sets for large qLDPC codes. Step-3 full-frame refinement is essentially inert on real devices, which have no $Y$-dominant qubits.

## 9. No extension of the Quantum Tensor Product admits a Superposition principle

[arXiv:2608.17572](https://arxiv.org/abs/2608.17572) · [SciRate](https://scirate.com/arxiv/2608.17572)

*Vincenzo Fiorentino, Kuntal Sengupta*

**TL;DR** The paper gives a Hilbert-space-free, operational definition of superposition in Generalised Probabilistic Theories: an extremal state is a superposition of a subset of a maximally perfectly-discriminable (MPD) set if it is probabilistic on the corresponding outcomes of a maximally-distinguishing extremal (MDE) measurement whose probabilities sum to one. From this they distill three "superposition principles" (complete, uniform, mutual) and prove that, for quantum subsystems obeying the no-restriction hypothesis, no non-signalling composition strictly larger than the quantum tensor product satisfies mutual superposition — singling out the quantum tensor product operationally.

**Key contributions**
- A *relational*, statistics-only definition of superposition applicable to any GPT (contrasted with Aubrun et al.'s non-simpliciality notion and D'Ariano et al.'s infinite-extremal-set requirement); maximality of the discriminable set is shown necessary via a qutrit counterexample.
- Three inequivalent principles — complete (every extremal state is a superposition), uniform (relative to *any* MPD set), mutual (superposition is symmetric/reciprocal) — shown not to form a hierarchy, using purpose-built toy theories GPT-1 (uniform+mutual, not complete) and GPT-2 (uniform only).
- Main theorem: any $\mathcal{S}_{Q1,2}\subsetneq \mathcal{S}\boxtimes\mathcal{S}\subseteq \otimes_{\max}$ fails mutual superposition; corollary: no strict extension satisfies all three principles plus no-restriction.
- Transfer lemma: existence and complete superposition carry from one subsystem to any non-signalling composite whenever operational dimension is multiplicative; uniform superposition also transfers under "outcome sharpness" of MDEs.
- Entanglement (any composition strictly above the minimal tensor product, with multiplicative operational dimension) implies superposition; converse false. Preparational uncertainty (disjoint deterministic sets of two MDEs) implies complete superposition, and under sharpness, uniform; uncertainty is recast purely in superposition language.
- Classification table across classical, quantum, GLT, Boxworld (superposition exists only via the PR box, no stronger principle), Spekkens' toy theory (satisfies all three), and $n$-gons, with an odd/even parity gap: even $n$-gons fail uniform superposition; strong uncertainty only in the $n\to\infty$ (real qubit) limit.

**Why it matters** Provides a device-independent handle on "superposition" for gravity-witness and indefinite-causal-order experiments where the notion is currently Hilbert-space-bound, and adds a superposition-based principle to the list of axioms (information causality, local tomography, etc.) that rule out post-quantum composites.

**Caveats** The composition theorem presupposes *quantum* subsystems plus the no-restriction hypothesis; no single-system reconstruction is offered. Superposition is defined only for extremal states, and MDEs are assumed informationally complete. Multiplicativity of operational dimension is an extra assumption that fails already for pentagon composites. Finite dimensions only; the key proofs sit in the (here truncated) appendix. The $n$-gon parity asymmetry and a principle-level characterisation of strong uncertainty remain unexplained.

## 10. A Simple Algebraic Proof of the PCP Theorem

[arXiv:2608.17429](https://arxiv.org/abs/2608.17429) · [SciRate](https://scirate.com/arxiv/2608.17429)

*Prashanth Amireddy, Amik Raj Behera, Srikanth Srinivasan, Madhu Sudan, Sophus Valentin Willumsgaard*

**TL;DR** The paper gives a self-contained algebraic proof of the PCP theorem (3-COLOR has a poly-size PCP with O(log n) randomness and O(1) queries) that uses no PCP composition, no robustification/PCP-of-proximity machinery, and no invocation of NP-completeness inside the verifier — only code concatenation, interpolation, and polynomial multiplication. The enabling new ingredient is a "set-multilinear encoding" of univariate polynomials that turns the lines-table of a low-degree test into a constant-degree multivariate object, so it can itself be tested and self-corrected with O(1) queries after concatenation with a low-degree Hadamard (long) code.

**Key contributions**
- A composition-free algebraic PCP: the only alphabet-reduction mechanism is code concatenation (in Goldreich's terminology, at most "0.5 compositions" for the lines oracle).
- Set-multilinear encoding: a degree-$d$ univariate $P$ is mapped to a set-multilinear (hence total-degree-$c$) polynomial in $c\cdot m_1$ variables, $m_1=\lceil d^{1/c}\rceil$, by writing exponents in base $m_1$: $Y^k \mapsto X_{0,k_0}\cdots X_{c-1,k_{c-1}}$. Evaluation is recovered via the moment map $\Phi_{c,m_1}(\lambda)=((\lambda^{j})_j,\dots,(\lambda^{jm_1^{c-1}})_j)$.
- Full pseudocode for both the verifier and the honest (completeness) prover, each ~1 page, given field/polynomial arithmetic — proposed as an operational measure of "simplicity".
- Fixes the randomness bottleneck in Goldreich (ECCC 2025), which achieved $n^\varepsilon$ randomness, by combining the new encoding with the sumcheck-free vanishing-certificate approach of the authors' STOC 2026 paper.

**How it works** Start from the BFL/ALMSS-style atomic PCP: 3-coloring reduces to low-degree testing of O(1) many $m$-variate polynomials over $\mathbb{F}_q$ ($m,d,q=\mathrm{polylog}\,n$) plus a "vanishes on $H^m$" check. The sumcheck is replaced by Combinatorial Nullstellensatz: $P|_{H^m}\equiv 0$ iff there is a single vanishing-certificate polynomial $\mathcal{M}_P(\mathbf X,\mathbf Y)\in\mathbb{I}(\mathbf Y)$ of degree $\le\deg P$ with $P(\mathbf X)=\mathcal M_P(\mathbf X,Z_H(\mathbf X))$, reducing everything to one extra $2m$-variate low-degree test. The obstruction to concatenation is the lines table $f_{\mathrm{lines}}:\mathbb F_q^{2m}\to\mathbb F_q^{d+1}$, whose symbols are $\mathrm{polylog}\,n$ bits — long-coding them would give quasi-polynomial proofs. Instead each line-polynomial is stored in set-multilinear form; testing it only requires a constant-degree test (Rubinfeld–Sudan, using $\zeta$ of order $c+1$ in $\mathbb F_q^\times$, char 2, so all coefficients $\eta_i=1$), and passing the test only guarantees closeness to *some* degree-$\le c$ polynomial, which pulls back to univariate degree $O(cd)$ — weaker than needed but sufficient for soundness. Field symbols are then reduced to bits by degree-$r$ Hadamard/long codes ($2^{\binom{t}{\le r}}$ bits, $t=O(\log\log n)$), with the key lemma that $\mathrm{Had}_1[P\circ f](\mathbf a,L)=\mathrm{Had}_r[f](\mathbf a,\Lambda_{P,L})$, letting constant-degree relations (needed for NP-hardness) be checked with O(1) bit queries.

**Why it matters** Removes the conceptually heaviest layer (composition-preparation: bundling, parallelization, assignment testers, Cook–Levin encoding of the outer verifier) from algebraic PCPs. Of pedagogical value for courses, and of practical interest to anyone implementing PCP-based proof systems, since the honest prover reduces to standard multivariate interpolation/evaluation.

**Caveats** Constants: the line-point test needs $q>Cd^3$ and the analysis is for small $\delta$; the soundness constant $\gamma$ is not optimized and query complexity is a (likely large) unspecified constant. The degree guarantee from the set-multilinear test is $O(cd)$ rather than $d$; the authors note this could be tightened but deliberately do not. "Simplicity" is argued by page-count of pseudocode rather than any formal metric, and the low-degree test still needs an auxiliary oracle. The truncated source omits the final soundness accounting, so end-to-end parameter tracking isn't verifiable here.
