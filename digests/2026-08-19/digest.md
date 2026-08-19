# SciRate Daily Digest — 2026-08-19

The top 10 papers on [SciRate](https://scirate.com/) today.

## 1. Non-CSS Quantum Code Embedding

[arXiv:2608.16995](https://arxiv.org/abs/2608.16995) · [SciRate](https://scirate.com/arxiv/2608.16995)

*Andrew C. Yuan, Nouédyn Baspin*

**TL;DR** The paper lifts the chain-complex ("cone") formalism for CSS codes to arbitrary stabilizer codes by replacing $\F_2$ chain complexes with *symplectic complexes* $S\xrightarrow{\sigma}P\xrightarrow{\hat\sigma}\bar S$, where $P$ is the Pauli space with symplectic form $\Lambda$ and $\hat\sigma=\sigma^\top\Lambda$, so that $\hat\sigma\sigma=0$ *is* the stabilizer commutation condition. A single embedding theorem (Thm. on symplectic embedding, ~2 pages) then transports cone-based constructions — qLDPC surgery, Layer codes / Euclidean embedding, quantum weight reduction — to non-CSS codes without local Clifford tricks.

**Key contributions**
- Symplectic-complex formalism for arbitrary stabilizer codes, with a notion of chain map $g$, its symplectic adjoint $\hat g$, a "defect map" $p$ measuring failure of $\hat g g=0$, and height-2 cones as merged/deformed codes.
- Direct non-CSS logical measurement (e.g. $Y$-type) via cone construction, replacing the ad hoc local-Clifford-conjugation route; the CSS cone is recovered as a special case.
- Generalizations of qLDPC surgery, Layer codes (3D Euclidean embedding) and weight reduction to non-CSS inputs, previously restricted to CSS.
- Explicit low-level circuit implementations and a spacetime fault complex giving a threshold statement.

**How it works** A stabilizer code is encoded as $\sigma:S\to P=Q_X\oplus Q_Z$ with syndrome map $\hat\sigma$; a CSS code splits into the usual $\partial,\delta$. Measuring a commuting set $g:X^A\to P^D$ requires $\hat g g=0$ (defect $p=0$); the merged code is $\mathrm{cone}(g)$. Circuit-level: one check qubit per stabilizer initialized in $X$, then CNOTs implementing the $X$-sector $g_X$ and CZs implementing the $Z$-sector $g_Z$; the combined propagation matrix is exactly the lower-triangular $\begin{pmatrix}\mathrm{id}&&\\ g&\mathrm{id}&\\ &\hat g&\mathrm{id}\end{pmatrix}$, so physical errors map $e(P^D)\mapsto e(P^D)$, $e(\bar X^A)\mapsto \hat g e(P^D)+e(\bar X^A)$ — i.e. errors on check qubits become measurement errors, just as in CSS syndrome extraction. Logical readout is $\langle \hat g\tilde e(P^D)|\bar{\mathcal X}^A\rangle+\langle\delta^A x^A|p\,\mathcal X^A\rangle$, the second term being the genuinely non-CSS correction. Fault tolerance follows from $T\ge d$ repeated rounds plus min-weight decoding on the spacetime complex.

**Why it matters** Most modern logical-gate machinery (surgery ancillas, weight reduction, 3D layer-code embeddings) is CSS-only, forcing non-CSS codes (or $Y$-type logicals of CSS codes) through Clifford deformations that can destroy LDPC structure or geometry. A uniform symplectic framework makes these constructions plug-and-play, of interest to anyone designing qLDPC architectures, fault-tolerant compilers, or non-CSS code families.

**Caveats** The visible material is mostly formal/appendix; the truncated source doesn't expose the concrete parameter claims for non-CSS Layer codes or weight-reduction overheads, nor numerics. Ancillas are assumed to have trivial internal logicals ($\ker\hat\sigma^A=\im\sigma^A$), transversal init/measurement is idealized, and thresholds are asserted via the standard Gottesman argument rather than simulated. Whether resulting deformed codes remain LDPC with good distance in general is not settled here.

## 2. Quantum simulation of slow analytic time-dependent Hamiltonians

[arXiv:2608.17653](https://arxiv.org/abs/2608.17653) · [SciRate](https://scirate.com/arxiv/2608.17653)

*Chenhao Zhao, Yinan Li, Dong An*

**TL;DR** The paper gives a Floquet-based quantum algorithm for "slow" Hamiltonians $\widetilde H(t)=H(t/T)$ with analytic (Gevrey-1) $H(s)$, achieving query complexity $\widetilde{\mathcal O}(\alpha T+\log(1/\varepsilon))$ — additive rather than multiplicative in time and precision — while keeping additional gate overhead polylogarithmic in $1/\varepsilon$ (quadratic in $\alpha T$). The enabling technical tool is an explicit smooth *periodic Gevrey extension* of $H$ off $[0,1]$, built from a Gevrey cutoff and a quantitative Borel lemma, together with matching Fourier-decay and Floquet-truncation bounds.

**Key contributions**
- A constructive periodic extension $\hat H(s)$ on $[0,2]$ matching all derivatives at the seam ($\hat H^{(n)}(0)=\hat H^{(n)}(2)$), using $F_\tau,G_\tau$ built from endpoint Taylor data damped by scaled cutoffs $\chi_\tau(R_kx)$; explicit derivative bounds show $\hat H\in G^{\varrho}$ with $\varrho=\sigma+\tau-1$.
- Quantitative Gevrey Borel lemma with explicit constants ($|f^{(n)}|\le 4CC_{\tau,1}(32e^{\sigma-1+1/e}D)^n(2C_{\tau,2})^{n-1}(n!)^{\sigma-1+\tau}$) and a Gevrey-$\tau$ cutoff with explicit derivative growth.
- Fourier-coefficient decay and a Lieb–Robinson-type bound for Gevrey (not analytic) periodic Hamiltonians, giving Floquet truncation order $l_{\max}$; existing analytic-case analysis (Mizuta et al.) does not apply since the extension cannot be analytic (identity theorem).
- Complexities: general case $\widetilde{\mathcal O}(\alpha T+\log(1/\varepsilon))$ queries, $\widetilde{\mathcal O}((\alpha T+\log\frac1\varepsilon)^2\log\frac1\varepsilon)$ extra gates; control Hamiltonians $H=\sum_j\alpha_j(s)M_j$ need only block encodings of $M_j$ (coefficients computed classically) and $\widetilde{\mathcal O}((\alpha T+\log\frac1\varepsilon)^2)$ gates; Gevrey-$\sigma$ ($1\le\sigma<2$) degrades to $\widetilde{\mathcal O}((\alpha T+\log\frac1\varepsilon)^{\sigma})$ queries.
- Combined with optimal-scaling LCHS: slow analytic semi-dissipative ODEs solved with $\widetilde{\mathcal O}(\tfrac{\|u_0\|}{\|u(T)\|}\alpha T\log\frac1\varepsilon)$ queries, a quadratic improvement in $\log(1/\varepsilon)$ over Low–Somma for time-dependent $A$.

**How it works** After extension, Fourier expansion plus Floquet embedding maps the problem to a time-independent effective Hamiltonian on an enlarged index space; subexponential Fourier decay lets one truncate at $|l|\le l_{\max}=\widetilde\Theta(\alpha T+\log\frac1\varepsilon)$, block-encode via LCU (with the $\mathscr H_{\rm LP}$ ladder term normalized by $l_{\max}\omega$), and apply QSVT. Approximate translation symmetry in a $4l_{\max}$ space plus oblivious amplitude amplification restores $\Theta(1)$ success amplitude.

**Why it matters** It is the first construction to combine near-additive query scaling with polylog-in-$1/\varepsilon$ gate overhead for non-periodic time-dependent simulation — complementary to the concurrent transducer result (optimal queries for Lipschitz $H$ but $\mathrm{poly}(1/\varepsilon)$ gates). Relevant to adiabatic/annealing schedules, quantum control, and ODE solvers.

**Caveats** The input model is nonstandard: HAM-T for $H'(s)$ plus block encodings of endpoint derivatives $H^{(k)}(0),H^{(k)}(1)$ up to order $\widetilde{\mathcal O}(\log\alpha T+\log\frac1\varepsilon)$; not an improvement under standard HAM-T. Regularity constants $C,D$ (and the cutoff index $\tau>1$, which must approach 1 to recover near-linear $l_{\max}$) are treated as $T,\varepsilon$-independent and hidden in $\widetilde{\mathcal O}$. Gate cost is quadratic in $\alpha T$, worse than truncated Dyson. Restricted to the adiabatic-like regime $t/T=\mathcal O(1)$; $\sigma\ge2$ Gevrey classes are excluded.

## 3. Nearly Sample-Optimal Estimators for Quantum Rényi and Tsallis Entropies

[arXiv:2608.18070](https://arxiv.org/abs/2608.18070) · [SciRate](https://scirate.com/arxiv/2608.18070)

*Kean Chen, Qisheng Wang*

**TL;DR** Two new estimators close the remaining sample-complexity gaps for quantum Rényi entropy at all non-integer orders and for Tsallis entropy at $0<\alpha<1$, matching Wang's recent lower bounds up to polylogs. E.g. for non-integer $\alpha>1$ Rényi drops from $O(d^2/\varepsilon^2)$ to $O(d^2/\varepsilon^{1/\alpha}+d^{1-1/\alpha}/\varepsilon^2)$, and for $0<\alpha<1$ from $O(d^{2/\alpha}/\varepsilon^{2/\alpha})$ to $O(d^{1+1/\alpha}/\varepsilon^{1/\alpha}+\cdots)$ — a large polynomial improvement.

**Key contributions**
- A new tangent-line/Bures-$\chi^2$ inequality: for $\sigma\succeq \tfrac{d}{n}I$, $0\le (1-\alpha)\tr(\sigma^\alpha)+\alpha\tr(\rho\sigma^{\alpha-1})-\tr(\rho^\alpha)\le (d/n)^{\alpha-1}\mathrm D_{\chi^2}(\rho\|\sigma)$, turning $\chi^2$-accurate tomography into a low-bias $\mathrm F_\alpha$ estimator.
- Proof that regularizing the PSTW $\chi^2$-tomography output as $\sigma=\hat\rho+\tfrac{2d}{n}I$ gives $\mathrm D_{\chi^2}(\rho\|\sigma)=O(d^2/n)$.
- For $\alpha>1$: a bias expansion of the plug-in estimate $\tr(\hat\rho^\alpha)$ from Hayashi's covariant pure-state POVM applied to random purifications, in Beta-distribution moments $\mu_j(s)$, plus Richardson extrapolation across $k=\lceil\alpha\rceil-1$ geometric batch sizes to cancel all but an $O(F(d^2/s)^\alpha)$ remainder.
- Methodologically, both estimators avoid weak Schur sampling, unlike all prior Rényi/Tsallis estimators.

**How it works** *($\alpha<1$)* Spend $n=\Theta(d^{1+1/\alpha}/\varepsilon^{1/\alpha})$ copies on $\chi^2$-tomography, then $m$ further copies measured single-copy in the eigenbasis of $\sigma$, with outcome value $s_J^{\alpha-1}$, estimating $\alpha\tr(\rho\sigma^{\alpha-1})$; the deterministic term $(1-\alpha)\tr(\sigma^\alpha)$ is computed classically. Bias is controlled by the $\chi^2$ bound; the variance analysis splits at $\alpha=1/2$ (where $\mathbb E[X^2]\le O(d(d/n)^{2\alpha-1})$) versus $\alpha>1/2$ ($O(d^{2-2\alpha})$ additive, $O(d^{1/\alpha-1}F^2)$ relative), explaining the two different $\varepsilon^{-2}$ terms for Rényi vs. Tsallis.
*($\alpha>1$)* Purify $\rho$ randomly, measure batches with Hayashi's POVM; the estimate $\hat M_T=\sqrt{1-T}M+\sqrt T G$, $T\sim\mathrm{Beta}(d^2-1,s+1)$, drives a Schatten-norm Taylor expansion whose even terms give $\mu_j(s)$; combining $Y_{s_\ell}$ with coefficients solving $\sum a_\ell\mu_j(s_\ell)=0$ leaves bias $\le \tfrac14\theta F$ and variance $\le \theta^2F^2/100$ with $\theta=1-e^{-(\alpha-1)\varepsilon}$.

**Why it matters** Fills the last major gaps in the sample-complexity landscape of quantum entropy estimation (see their summary table), and the Bures-$\chi^2$-tomography-plus-tangent-correction recipe looks reusable for other concave/smooth spectral functionals.

**Caveats** Constants are $\alpha$-dependent and blow up as $\alpha\to1^-$ (factors like $(1-\alpha)^{-(2\alpha-1)/\alpha}$) and are unspecified as $\alpha$ approaches integers; only constant (0.98 / 24/25) success probability is proved; polylog gaps to lower bounds remain; both algorithms require collective measurements on $\Theta(n)$ copies and time complexity is not discussed; Tsallis for $\alpha>1$ is not addressed (already settled elsewhere), and integer $\alpha$ is excluded.

## 4. Quantum Circuit for General Unitary: Improved T-count via Block Flattening and Dilation

[arXiv:2608.17846](https://arxiv.org/abs/2608.17846) · [SciRate](https://scirate.com/arxiv/2608.17846)

*Pei Yuan, Shengyu Zhang, Wei Zi*

**TL;DR** The paper gives a Clifford+$T$ synthesis of an arbitrary $n$-qubit unitary with worst-case $T$-count $O(d^{5/4}L^{5/8}\log d)$, where $d=2^n$ and $L=n+\log(1/\epsilon)$, improving Tan's $O(d^{4/3}L^{2/3}+dL)$ whenever $L\le d$. The trick is to stop decomposing $U$ into a product of simpler gates and instead build a *single* block encoding of the whole matrix, using randomized sign diagonals to flatten all sub-block norms, Halmos dilations packed into one SELECT, and QSVT to undo the normalization.

**Key contributions**
- **Simultaneous block flattening**: two Boolean $\pm1$ phase diagonals $D_1,D_2$ and Hadamard transforms give $V=H_dD_1UD_2H_d$ with *every* $b\times b$ block satisfying $\|P_IVP_J^\dagger\|=O(\sqrt{b/d}\log d)$ — a uniform bound over all $D^2=(d/b)^2$ blocks, not just typical ones.
- **Block-dilation SELECT**: all $D^2$ normalized blocks are unitarily dilated (Julia–Halmos) and compiled jointly into one $(2r,k+1)$-uniformly-controlled unitary, yielding a block encoding of $V$ with subnormalization $\rho=Dg=O(\sqrt{d/b}\log d)$ while each selected unitary acts on only $2b$ dimensions.
- **Robust one-point amplification**: a QSVT polynomial of degree $Q=\Theta(\rho)$ that maps the single singular value $1/\rho$ *exactly* to 1, with an explicit perturbation analysis ($\|A_{\rm amp}-V\|=O(Q^2\delta)$, clean-input error $O(Q\sqrt\delta)$).
- Appendix extension: one common sign pair flattens an entire multiplexed family $\{U_x\}$ simultaneously, improving multiplexed-unitary $T$-counts over direct application of Tan's compiler.

**How it works** Flattening is proved by a two-stage randomization: Hoeffding + union bound over $d^2$ entries makes all entries $O(\sqrt{\log d/d})$ (bounding row norms of column slabs by $\mu=16(b/d)\ln 2d$), then Tropp's rectangular matrix Rademacher bound controls each $b\times b$ block spectral norm, union-bounded over all block pairs. Tan's UCU compiler costs $O(d\sqrt L+b^2L)$ per SELECT query; with $O(\rho)$ queries the total is $O(\log d\,[d^{3/2}b^{-1/2}\sqrt L+d^{1/2}b^{3/2}L])$, balanced at $b_\star=d^{1/2}L^{-1/4}$.

**Why it matters** This is the first improvement to the generic worst-case $T$-count exponent since Tan, narrowing the gap to the $\tilde\Omega(d)$ lower bound of Gosset–Kothari–Wu from $d^{1/3}$ to $d^{1/4}$. Relevant to anyone working on fault-tolerant compilation, magic-state budgeting, or block-encoding-based algorithm design.

**Caveats** Ancilla cost is $O(d\sqrt L)$ clean qubits — substantially more than Tan's $O(d^{2/3}L^{1/3}+L)$; the space–$T$ tradeoff is not explored. The sign diagonals are found by classical randomized search with certified block-norm evaluation, explicitly excluded from the resource count. The error metric only constrains behavior on the clean-ancilla input subspace. The bound holds only for $L\le d$; outside that regime Tan's construction is used. The improvement is asymptotic and carries a $\log d$ and constants ($C_{\rm flat}=16\ln2$) that matter at practical $n$. Authors acknowledge LLM assistance in manuscript preparation, claiming independent verification of all proofs.

## 5. Lie-Algebraic Classical Simulation of Bosonic Systems Beyond Gaussian Dynamics

[arXiv:2608.17094](https://arxiv.org/abs/2608.17094) · [SciRate](https://scirate.com/arxiv/2608.17094)

*Adelina Bärligea, Timothy Heightman, Jakob S. Kottmann, Antonio Acín*

**TL;DR** The paper generalizes Lie-algebraic ($\mathfrak g$-sim) classical simulation to bosons by replacing the dynamical Lie algebra with an *observable-seeded reachable operator module* $\mathcal V(O)$ — the smallest real operator space containing $O$ that is invariant under $\mathrm{ad}_{H_k}$. Whenever $\dim\mathcal V(O)=\mathrm{poly}(n)$ and input overlaps are accessible, expectation values, fixed-order/multi-time/OTOC correlators, and reverse-mode gradients are computed exactly by finite matrix algebra — recovering Gaussian optics and extending to non-Gaussian dynamics such as bounded-photon Kerr and pair-hopping.

**Key contributions**
- A simulability criterion stated on $\mathcal V(O)$ rather than on the DLA: $\langle O(\bm\theta)\rangle = \bm w^\top e^{\theta_L A_{k_L}}\cdots e^{\theta_1 A_{k_1}}\bm e^{\mathrm{in}}$, with no Fock cutoff or moment closure. The usual DLA condition is the special case $O\in\mathfrak g$ and is shown to be sufficient but not necessary (e.g. linear observables under Gaussian dynamics need only $2n+1$ dimensions vs. $\mathcal O(n^2)$ for $\mathfrak g_{\rm Gauss}$).
- Three finiteness mechanisms: (i) degree preservation under quadratic Hamiltonians, giving moment modules of dimension $\binom{2n+m}{m}$ valid for *non-Gaussian inputs* provided the input moment tensor is available; (ii) photon-number sector confinement, $d_{n,N}=\binom{N+n-1}{N}=\Theta(n^{N})$, making self-/cross-Kerr, number-diagonal, and pair-hopping dynamics exactly simulable at arbitrary coupling and poly depth for $N_{\max}=\mathcal O(1)$, with $\dim\mathcal V\le d_{n,\mathcal S}^2$; (iii) a multimode nilpotent cubic-and-higher "phase" family.
- A sharp negative result absent in spin/fermion settings: a finite-dimensional bosonic generator algebra can still produce an infinite-dimensional observable orbit — simulability is a property of the (dynamics, observable) pair.
- A perturbative hierarchy for squeezing: parity-resolved photon-number bands of depth $k$ reproduce number-conserving observables to order $2k+1$ in the squeezing amplitude, leading error $\mathcal O(\lambda^{2(k+1)})$; confirmed numerically.
- Numerics: operator spreading/OTOCs on interacting chains up to 400 modes, doublon (repulsively bound pair) band with flux-reversed edge motion, differentiable control on lattices to $9\times9$, depths 1–8.

**How it works** Heisenberg-picture propagation is restricted to $\mathcal V(O)$; the generators act as $D\times D$ real matrices $A_k$ obtained from structure constants (for bosons read off the symplectic form $-\Omega$ plus Leibniz), and the circuit becomes a product of matrix exponentials contracted against observable coordinates and input overlaps $\mathrm{Tr}[B_\alpha\rho_{\rm in}]$. Correlators use ordered input moment tensors $\mathrm{Tr}[B^{(1)}_{\alpha_1}\cdots B^{(m)}_{\alpha_m}\rho_{\rm in}]$.

**Why it matters** It cleanly separates the mean-value problem from sampling: results are fully consistent with boson-sampling and Gaussian-boson-sampling hardness (which lives in high-order coincidence observables) while carving out exactly tractable non-Gaussian regimes. Relevant for benchmarking CV devices, variational bosonic ansätze, and cold-atom/photonic transport studies.

**Caveats** Efficiency hinges on unstated-in-general assumptions: efficient access to restricted generator matrix elements, observable coordinates, and input moments — these can be the bottleneck. Sector-confinement results require $N_{\max}=\mathcal O(1)$ and input states supported on those sectors; costs scale as $n^{2N_{\max}}$. The formal exponential/adjoint identity presumes a common invariant domain (unbounded-operator subtleties). Squeezing control needs explicit analyticity assumptions; only asymptotic error orders are established. No general algorithm is given for deciding whether $\mathcal V(O)$ is finite.

## 6. Hardware-Aware Compilation and Execution of Bivariate Bicycle Codes on Neutral-Atom Systems

[arXiv:2608.17023](https://arxiv.org/abs/2608.17023) · [SciRate](https://scirate.com/arxiv/2608.17023)

*Jason Ludmir, Aditya Ranjan, Nicholas S. DiBrita, Jason Han, Tirthak Patel*

**TL;DR** Park-n-Ride is a compiler/architecture co-design that maps bivariate-bicycle (BB) qLDPC code primitives — idles, shift automorphisms, in-module and inter-module logical measurements, T-injection — onto zoned, AOD-based neutral-atom hardware while respecting non-crossing transport, blockade, and zoning constraints. Its main lever is spectral-seriation placement of code modules into compute columns, which cuts estimated end-to-end runtime by 17.9% vs. arbitrary placement (4951→4066 ms) and expected transport-induced atom-loss events by 40.7% (21.9→13.0) on schedules with up to 113 gross-code modules (~32.5k physical, 1356 logical qubits).

**Key contributions**
- A columnar compute-zone layout: each column stacks modules with idle / bridge-interaction / shift-measurement subzones plus a per-module "logical processing unit" holding bridge and ancilla atoms, so nearly all motion is column-local and AOD-legal.
- A shift-automorphism scheduler: torus shift T(Δi,Δj) = Roll_i ∘ Roll_j, exploiting periodicity (four equivalent direction choices) so all modules in a column adopt the column head's direction and roll in parallel; residual offsets from heterogeneous shift magnitudes are removed by a monotone resync sweep with staggered SLM drop-offs (number of moves = number of distinct residuals).
- Spectral (Fiedler-vector) seriation of the joint-measurement interaction graph into a 1D column ordering, plus a hub-centric greedy and arbitrary baseline.
- An interval-coloring bridge scheduler: each joint-measurement pair spans a column interval; greedy coloring into rounds of disjoint intervals, then lockstep ±1 column micro-steps to a midpoint rendezvous guarantee non-crossing Bell-pair formation.
- Sensitivity models for readout latency, per-distance/per-transfer atom loss, and per-column single-server T-factory queueing.

**How it works** A BB-native tableau is turned into a dependency DAG, topologically layered for maximal module-level concurrency, then split into shift/measurement sublayers; idling modules run a fixed 24-substep wrap-aware stabilizer extraction schedule (10 cycles per measurement sublayer). Timing is estimated analytically (55 µm/µs shuttling, 100 µs trap switch, 0.8 µs CZ, 12×6 cell modules at 10 µm pitch, column width 4.3·W_mod).

**Why it matters** It is a concrete systems-level bridge between qLDPC logical-algorithm interfaces (Tour de Gross-style automorphism + measurement instruction sets) and reconfigurable atom arrays, showing placement quality can substitute for hardware (spectral at capacity 6 beats arbitrary at capacity 10) and that syndrome cycles, not shifts, dominate error.

**Caveats** No prior-art baseline is compared against; all "runtimes" come from an analytic estimator, not circuit-level simulation or hardware. Logical error is a crude oracle-decoder binomial (failure at ≥5 faults), not decoded Monte Carlo. Measurement time is deliberately zeroed to expose transport differences. The claim that two-gross scaling changes runtime by <0.1% despite doubled module height deserves scrutiny, as does the T-factory study, which injects synthetic requests into fixed schedules.

## 7. A Complete Classification of Complex Hadamard Matrices of Order Six

[arXiv:2608.18053](https://arxiv.org/abs/2608.18053) · [SciRate](https://scirate.com/arxiv/2608.18053)

*Mateo Cárdenes Wuttig, Joseph Tindall*

**TL;DR** The authors prove that every order-six complex Hadamard matrix (CHM) is equivalent to a dephased matrix possessing a *finite-corner witness*: a 3×3 corner whose two complementary fixed-Gram fibers are finite, so the whole matrix is recoverable by solving a finite algebraic system. This supplies the missing global step in Szöllősi's dilation method and proves his conjecture — outside Karlsson's three-parameter H₂-reducible family and Tao's isolated S₆⁽⁰⁾, every class is algebraically reconstructible from a corner.

**Key contributions**
- A cubic Gram invariant τ_r(X)=(XX†)₁₂(XX†)₂₃(XX†)₃₁ (and its column analogue), with the identity Re τ_r = Re τ_c for any 3×3 unimodular X, proved from equality of spectra of XX† and X†X.
- An **infinite-fiber trichotomy**: if an invertible X∈𝕋^{3×3} has an infinite normalized fixed-Gram fiber, then XX†=3I₃, or Re τ_r(X)<0, or X contains a 2×2 Hadamard block.
- A **corner-routing** argument: since complementary blocks satisfy BB†=6I−EE†, off-diagonal Gram entries flip sign, so τ_r(E)=−τ_r(B); one of the two corners must have positive invariant, hence finite fibers in both directions.
- Complete resolution of the Fourier-block case (some 3×3 block is Hadamard) into Karlsson ∪ Tao.
- Computer-certified finite-corner witnesses for the entire Karlsson family, including its degenerate seams.

**How it works** Singularity of a 3×3 corner forces two equal rows/columns and, via a triangle-inequality equality case, a 2×2 Hadamard submatrix — so outside Karlsson's family all corners are invertible. Haagerup's trick, rederived from residual coordinate pairs, gives two polynomial relations Φ_H, Γ; eliminating y² yields 𝒜(x)+ℬ(x)y=0 with 𝒜=x(|R|²−|T|²)κ_S(x), κ_S(x)=2S̄x²−(|S|²+3)x+2S. Unit-modulus forces |ℬ|²=|δ|²|κ_s|² on 𝕋; unique factorization of QQ^# = |δ|²κ_s² splits into monomial, Möbius (double-root), and unit-circle-root cases, each yielding one trichotomy branch — the common-root branch being retained rather than cancelled. The Fourier-block case reduces unimodularity of the forced block D=−(1/3)FD_wF†D_vF to a cyclic convolution α∗A=0, whose four Fourier allocations force cubic-root rows and columns, invoking Szöllősi's criterion. Karlsson witnesses use 245 exact resultants, a reciprocal half-angle equivalence t↔1/t swapping the two Möbius orientations, and a tensor Bernstein/de Casteljau positivity certificate (degree 16×8, ten dyadic boxes).

**Why it matters** Order six is the first dimension where continuous families and an isolated point coexist; the gap has blocked progress on MUBs in dimension 6 and on six-mode balanced interferometers. A branch-complete, finite reconstruction procedure gives a rigorous computational handle on the full space.

**Caveats** The result is conditional on two published inputs (Karlsson's H₂ classification, Szöllősi's cubic-root criterion). Parts are computer-assisted; the Lean audit covers only an explicitly delimited boundary. "Classification" here means finite incidence/reconstructibility — extracting an explicit list of classes still requires solving the resulting quadratic–cubic systems, and two classes (Tao's matrix, one Karlsson point) evade the generic four-phase reconstruction. Only the supplement was available for review.

## 8. Computationally Efficient Optimization of Per-Qubit Clifford Deformation for Non-uniform Biased Noise

[arXiv:2608.17870](https://arxiv.org/abs/2608.17870) · [SciRate](https://scirate.com/arxiv/2608.17870)

*Won Joon Yun, Andrew Nemec, Jonathan M. Baker*

**TL;DR** Chameleon is a decoder-free compiler that picks per-qubit Clifford frames (single-qubit Pauli-axis permutations) for spatially non-uniform biased noise by minimizing a Bhattacharyya-style analytic upper bound on the "Type-A" (ambiguity-driven) logical error rate. It cuts frame-selection time for the [[72,12,6]] BB code from ~1.2 days to 3.1 minutes while reducing worst-axis LER by up to ~21–32% over the best prior baseline on Willow-derived noise maps, and by >100% on strongly biased synthetic maps.

**Key contributions**
- A per-qubit decomposable surrogate for LER: for an ambiguity operator ℓ (a nontrivial logical Pauli), Pr[failure] ≤ ∏_{q∈ℓ} γ(r_c^q(F)) with γ(r)=2√(r(1−r)), derived by replacing the ML-decoding indicator with √(P(e)P(e⊕ℓ)) and factorizing over independent per-qubit noise. Cost per operator drops from O(2^w) to O(w).
- Reusable, code-only ambiguity LUT: enumerate all logical representatives up to weight cutoff W (W=d+2 for surface/color/BB18/36; W=d+10 with randomized Gaussian elimination + BB translation orbits for BB72), amortized across all calibration maps.
- Two-stage cross-entropy-method search: Bernoulli {I,H} binary search (3,000 evaluations), then warm-started categorical search over all 6 frames, deployed only if it beats the binary frame by τ=20%.
- Separation of Type-A (ambiguity/ML-irreducible) vs Type-B (decoder-suboptimality) failures; the paper targets and reports Type-A LER only. Exact MWPM shows 0% Type-B; approximate decoders reach ~86%.
- Objectives for both worst-axis memory (min max{U_X,U_Z}) and single-axis workloads (magic-state prep: LER_Z 0.34×–0.67× vs two-axis optimization).

**How it works** Frames only permute (p_X,p_Y,p_Z) per qubit, leaving the code, distance, and syndrome schedule intact. U_c(F)=Σ_{ℓ∈A_c} Γ_ℓ(F) is a weighted-distance objective: −log γ acts as a per-qubit edge weight, so minimizing U raises the effective weighted distance of the most fragile same-syndrome confusions — which is why the greedy local rule (suppress each qubit's dominant axis) fails, underperforming CSS on 27% of 1,756 instances.

**Why it matters** Practical calibration-aware deformation was previously gated by Monte Carlo decoding in the loop; a microsecond-per-candidate surrogate makes recompilation faster than calibration drift, and it is code-agnostic (surface, color, BB qLDPC). Surrogate–LER Spearman ρ reaches 0.89–0.98 on Willow. On 332 real device-placed patches, 79% improve (median 5.2%).

**Caveats** Mostly phenomenological noise; circuit-level Si1000 gives only 5.2% average gain (biased idle only). Surrogate fidelity degrades on weakly biased devices (ρ=0.34 on Miami surface code). Color and BB gains over the *best* baseline are marginal or negative in several rows (e.g., BB36/Willow −3%, color d5/Berlin −3%); large gains concentrate on synthetic η=10 fields. Full-frame refinement is currently useless on real transmons (no Y-dominant qubits). Bound is loose (independent Pauli noise, no correlations/crosstalk), and the CDSC comparison assumes an idealized 1 μs/shot decoder.

## 9. No extension of the Quantum Tensor Product admits a Superposition principle

[arXiv:2608.17572](https://arxiv.org/abs/2608.17572) · [SciRate](https://scirate.com/arxiv/2608.17572)

*Vincenzo Fiorentino, Kuntal Sengupta*

**TL;DR** — The authors give a Hilbert-space-free, prepare-and-measure definition of superposition in Generalised Probabilistic Theories: an extremal state is a superposition of a subset of a maximal perfectly-discriminable (MPD) set if it is probabilistic over exactly those outcomes of the corresponding maximally-distinguishing extremal (MDE) measurement. From this they distil three "superposition principles" (complete, uniform, mutual) and prove that mutual superposition fails for *every* non-signalling composition of quantum systems strictly larger than the quantum tensor product — singling out ⊗ operationally, given quantum subsystems.

**Key contributions**
- A relational, statistics-based definition of superposition applicable to any GPT, requiring *maximality* of the discriminable set (a qutrit example shows non-maximal PD sets give spurious attributions).
- Three inequivalent structural principles (complete/uniform/mutual), shown *not* to form a hierarchy via two constructed toy theories (GPT-1 admits uniform+mutual but not complete; GPT-2 only uniform).
- Main theorem: no state space strictly between the quantum tensor product and the maximal tensor product of two quantum systems admits mutual superposition; with the no-restriction hypothesis, no strict extension satisfies all three principles.
- Transfer lemmas: if the composite's operational dimension is multiplicative, existence and complete superposition inherit from *one* subsystem; uniform superposition inherits under "outcome sharpness" of MDEs.
- Entanglement (any composition strictly above the minimal tensor product) implies superposition; converse false. Preparational uncertainty implies complete superposition and, under outcome sharpness, uniform superposition — and can itself be recast purely in superposition terms.
- Classification table: classical theory and GLT have no superposition; Boxworld has superposition (PR box is a superposition of four separable states discriminated by an MDE) but no stronger principle; Spekkens' toy theory satisfies all three principles and strong uncertainty (via equivalence-balance) — so superposition is not a quantum/classical dividing line.

**Why it matters** — Proposals to test non-classical gravity and indefinite causal order rest on "superposition" as a primitive; this supplies a theory-independent operational handle. On the reconstruction side, it adds a physically motivated principle that fixes the composition rule, complementing information-causality-type constraints.

**Caveats** — The composition result assumes quantum subsystems, no-restriction hypothesis, and finite dimension; single-system quantum structure is not derived. Several results presuppose multiplicativity of operational dimension (false in general — pentagon compositions are a counterexample) and outcome sharpness. Superposition is defined only for extremal states. Odd behaviour appears in polygon models, where a state can be a superposition of a set while remaining perfectly distinguishable from some members, and even/odd $n$-gon parity produces an unexplained gap. Proofs sit in an appendix that is truncated here.

## 10. A Simple Algebraic Proof of the PCP Theorem

[arXiv:2608.17429](https://arxiv.org/abs/2608.17429) · [SciRate](https://scirate.com/arxiv/2608.17429)

*Prashanth Amireddy, Amik Raj Behera, Srikanth Srinivasan, Madhu Sudan, Sophus Valentin Willumsgaard*

**TL;DR** The paper gives an algebraic proof of the PCP theorem (3-COLOR ∈ PCP[O(log n), O(1)]) that eliminates PCP composition entirely, replacing it with plain code concatenation. The enabling technical idea is a new "set-multilinear" encoding of univariate polynomials that makes the lines-table low-degree test verifiable with O(1) *bit* queries without blowing randomness up to quasi-polynomial. Verifier and honest prover each fit on roughly one page of pseudocode.

**Key contributions**
- A composition-free algebraic PCP: no robustification/parallelization/bundling, no PCPs of proximity, and — notably — no invocation of Cook–Levin or NP-completeness of an auxiliary problem inside the verifier construction.
- The set-multilinear encoding $\Psi_{d,c,m_1}$: a "set-multilinearized inverse Kronecker map" sending a univariate degree-$d$ polynomial to a set-multilinear (hence total degree $\le c$) polynomial in $c\cdot m_1$ variables, $m_1 = \lceil d^{1/c}\rceil$, with $\Psi(P)(\Phi_{c,m_1}(\lambda)) = P(\lambda)$ for an explicit moment-curve-like map $\Phi$.
- Observation (building on Goldreich ECCC 2025 and the authors' STOC 2026 paper) that the lines table was the sole obstruction to reducing constant-symbol-query algebraic PCPs to constant-bit-query ones by concatenation.
- Fully explicit pseudocode for both verifier and completeness prover (App. A), plus a characteristic-2 refinement of the Friedl–Sudan local characterization where all coefficients $\eta_i = 1$ when $\zeta$ has order $c+1$.

**How it works** Start from the BFL/ALMSS-style atomic reduction: 3-coloring on $n$ vertices reduces to checking that O(1) $m$-variate polynomials over $\mathbb F_q$ ($q=2^t$, $t=O(\log\log n)$) have degree $\le d = \tilde O(\log^2 n)$ and vanish on $H^m$; following Ben-Sasson–Sudan and ABSSW, vanishing is certified by a *single* extra $2m$-variate "vanishing certificate" polynomial $\mathcal M_P$ (Combinatorial Nullstellensatz), so only low-degree tests remain. Field-valued proof symbols are concatenated with a degree-$r$ Hadamard (long) code over $\mathbb F_2^{\binom{t}{\le r}}$ — degree $r>1$ is needed so that nonlinear relations like $Y^3-1$ can be read off via a single query using a precomputed $\Lambda_{P,L}$. The lines-table entries, being $d\log q = \mathrm{polylog}\,n$ bits, cannot afford long-coding; instead each line polynomial is stored as the evaluation table of its set-multilinear image, tested merely as a degree-$\le c$ polynomial (constant queries, Rubinfeld–Sudan) and self-corrected via the $\zeta$-based interpolation identity. Passing the test only guarantees closeness to *some* degree-$c$ multivariate $\widetilde P$, which pulls back to a univariate of degree $O(cd)$ — a weaker but sufficient conclusion for soundness.

**Why it matters** Pedagogically significant: composition and composition-preparation are the bulk of the conceptual load in ALMSS/BGHSV/Ben-Sasson–Sudan; removing them makes the algebraic route teachable and makes the *honest prover* (arguably the most natural complexity measure of a PCP) explicit. Relevant to anyone teaching or implementing algebraic PCPs/IOPs.

**Caveats** The low-degree test still needs an auxiliary proof oracle, which the authors concede might count as "0.5 compositions" in Goldreich's sense. Soundness $\gamma$ is an unspecified small constant; parameters are not optimized (they deliberately accept the weaker $O(cd)$ degree bound). Analysis leans on ALMSS's line-point test (requiring $q > Cd^3$) as a black box, and "simplicity" remains an informal, page-count-based claim. The provided source is truncated before the final PCP assembly and parameter accounting.
