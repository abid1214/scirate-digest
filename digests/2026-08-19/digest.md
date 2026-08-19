# SciRate Daily Digest — 2026-08-19

The top 10 papers on [SciRate](https://scirate.com/) today.

## 1. Non-CSS Quantum Code Embedding

[arXiv:2608.16995](https://arxiv.org/abs/2608.16995) · [SciRate](https://scirate.com/arxiv/2608.16995)

*Andrew C. Yuan, Nouédyn Baspin*

**TL;DR** This paper lifts the chain-complex ("cone") formalism for CSS code constructions to arbitrary stabilizer codes by replacing $\mathbb{F}_2$ chain complexes with *symplectic complexes* $S\xrightarrow{\sigma}P\xrightarrow{\hat\sigma}\bar S$, where $P$ carries a symplectic form and $\hat\sigma$ is the symplectic adjoint. A single embedding theorem (Thm. 4, ~2 pages) then makes qLDPC surgery, Layer-code Euclidean embedding, and quantum weight reduction go through for non-CSS input codes, including genuinely $Y$-type logical measurements without local Clifford tricks.

**Key contributions**
- A symplectic-complex reformulation of stabilizer codes in which $\ker\hat\sigma/\operatorname{im}\sigma$ is the logical space and commutation of a measurement $g:X^A\to P^D$ is exactly the condition $\hat g g=0$ (with a "defect map" $p$ measuring failure).
- Generalization of the height-1/height-2 cone to the non-CSS setting, giving a uniform notion of code deformation, merge, and embedding.
- Non-CSS logical measurement (Sec. 3 / App. B): ancilla + relative connectivity gadget for arbitrary Pauli logicals, i.e. $Y$-type surgery on the same footing as $X$/$Z$.
- Non-CSS Layer codes and non-CSS quantum weight reduction, previously available only for CSS inputs.
- Explicit low-level circuit-level derivations: syndrome extraction and logical measurement algorithms with tracked physical/measurement errors, plus spacetime fault complexes for thresholds.

**How it works** The stabilizer group is encoded as a map $\sigma:S\to P=Q_X\oplus Q_Z$ with $\hat\sigma=\sigma^\top\Lambda$; commuting checks means $\hat\sigma\sigma=0$, so a stabilizer code *is* a length-2 symplectic complex. Cones over symplectic chain maps then produce deformed codes exactly as in CSS surgery. At the circuit level, an ancilla register is initialized in the $X$ basis and coupled to data by CNOTs implementing $g_X$ and CZs implementing $g_Z$; the joint Clifford acts on the symplectic space as the lower-triangular matrix $\begin{psmallmatrix}I&&\\ g&I&\\ &\hat g&I\end{psmallmatrix}$, which is precisely the height-2 cone with vanishing defect. Measuring out ancillas yields readout $\hat g\,\tilde e(P^D)+e(\bar X^A)$, so measurement errors are identified with $Z$-sector physical errors on check qubits; the logical outcome is $\langle \hat g\tilde e|\bar{\mathcal X}^A\rangle+\langle\delta^A x^A|p\mathcal X^A\rangle$. Ancillas are required to have no internal logicals ($\ker\delta^A=\operatorname{im}\delta^A$), and the Cleaning Lemma is used to decompose $\ker\hat\sigma$.

**Why it matters** Non-CSS codes (e.g. XZZX, twisted/Floquet-adjacent constructions, magic-state-friendly codes) have lacked the systematic homological toolkit that CSS codes enjoy; this removes the CSS restriction from surgery, 3D layer-code embeddings, and weight reduction in one stroke. Relevant to anyone designing fault-tolerant logical gadgets or LDPC architectures.

**Caveats** No numerics or simulations; overhead constants for non-CSS surgery/weight reduction aren't compared quantitatively to the CSS case in the visible text. Threshold claims are asserted via the standard Gottesman spacetime-fault-complex argument rather than proven with explicit distance/decoder analysis, and decoding on symplectic fault complexes (non-bipartite, mixed $X$/$Z$) may be harder in practice. CZ gates are required in the gadget, and ancilla acyclicity assumptions carry over.

## 2. Quantum simulation of slow analytic time-dependent Hamiltonians

[arXiv:2608.17653](https://arxiv.org/abs/2608.17653) · [SciRate](https://scirate.com/arxiv/2608.17653)

*Chenhao Zhao, Yinan Li, Dong An*

**TL;DR** — For Hamiltonians of the "slow" form $\widetilde H(t)=H(t/T)$ with $H$ analytic (or Gevrey) on $[0,1]$, this paper builds an explicit periodic Gevrey extension of $H$ so that Floquet embedding + QSVT applies, yielding $\widetilde{\mathcal O}(\alpha T+\log(1/\varepsilon))$ queries with only $\widetilde{\mathcal O}((\alpha T+\log(1/\varepsilon))^2\log(1/\varepsilon))$ extra gates. This is the first algorithm with simultaneously (nearly) additive query complexity and polylogarithmic-in-$1/\varepsilon$ gate overhead, at the price of a nonstandard input model (access to $H'$ and endpoint derivatives).

**Key contributions**
- A constructive periodic extension: $H$ on $[0,1]$ is glued on $[1,2]$ using Borel-type series $\sum_k \frac{H^{(k)}(1)}{k!}x^k\chi_\tau(R_kx)$ and $\sum_k\frac{H^{(k)}(0)}{k!}x^k\chi_\tau(R_kx)$, matching all derivatives at $s=1$ and at the periodic seam, with Gevrey index $\varrho=\sigma+\tau-1$ (proved via a Gevrey-$\tau$ cut-off with explicit derivative bounds $|\chi^{(n)}|\le C_{\tau,1}8^nC_{\tau,2}^{n-1}(n!)^\tau$ and a quantitative Gevrey Borel lemma).
- Fourier-coefficient decay (subexponential, $\sim e^{-c|m|^{1/\varrho}}$ rather than exponential) plus a Lieb–Robinson-type bound for the truncated Floquet effective Hamiltonian, giving explicit truncation orders $l_{\max}$ — the analysis in Mizuta–Fujii does not apply since the extension cannot be real analytic (identity theorem).
- Complexities: analytic case $\widetilde{\mathcal O}(\alpha T+\log(1/\varepsilon))$ queries; control Hamiltonians $H=\sum_j\alpha_j(s)M_j$ need only block encodings of $M_j$ (coefficients computed classically) with gate overhead $\widetilde{\mathcal O}((\alpha T+\log 1/\varepsilon)^2)$; Gevrey $1\le\sigma<2$ gives $\widetilde{\mathcal O}((\alpha T+\log 1/\varepsilon)^\sigma)$.
- Combined with optimal-scaling LCHS: slow analytic semi-dissipative ODEs solved in $\widetilde{\mathcal O}(\tfrac{\|u_0\|}{\|u(T)\|}\alpha T\log(1/\varepsilon))$ queries, a quadratic improvement in $\log(1/\varepsilon)$ over Low–Somma for time-dependent coefficients.

**How it works** — After extension to a $2T$-periodic $\widetilde H$, Floquet theory gives a time-independent $\mathscr H_{\rm eff}$ on $\{|l\rangle\}\otimes\mathscr H$; truncate to $|l|\le l_{\max}$, block-encode via LCU over Fourier modes (coefficients obtained from quadrature on $H'$ plus endpoint derivative data, or classically for control Hamiltonians), simulate with QSVT, and recover $|\psi(T)\rangle$ using Mizuta's approximate-translation-symmetry trick plus oblivious amplitude amplification. Since $T$ is one (half-)period, the "$t/T=O(1)$" regime needed for optimality holds automatically.

**Why it matters** — Relevant to adiabatic/annealing-type dynamics and control problems where near-optimal, high-precision, gate-efficient simulation is desired; complements the concurrent transducer result of Chen et al., which attains optimal queries for Lipschitz $H$ but with $\mathrm{poly}(1/\varepsilon)$ gate overhead.

**Caveats** — Not an improvement in the standard HAM-T model: the general result needs HAM-T for $H'$ plus block encodings of $\widetilde{\mathcal O}(\log(\alpha T/\varepsilon))$ endpoint derivatives. Gevrey constants $C,D$ (and $j_{\max}$) are treated as $T,\varepsilon$-independent constants; $\tau\to1^+$ hides polylog blow-up in constants. Gate overhead is quadratic in $\alpha T$, worse than truncated Dyson's near-linear scaling. Relaxing "slow" to an integral bound on $\widetilde H'$ and removing derivative oracles remain open.

## 3. Nearly Sample-Optimal Estimators for Quantum Rényi and Tsallis Entropies

[arXiv:2608.18070](https://arxiv.org/abs/2608.18070) · [SciRate](https://scirate.com/arxiv/2608.18070)

*Kean Chen, Qisheng Wang*

**TL;DR** Two new estimators close the remaining gaps in the sample complexity of estimating quantum Rényi and Tsallis entropies from copies of an unknown $d$-dimensional state. For $0<\alpha<1$ they give $O(d^{1+1/\alpha}/\varepsilon^{1/\alpha}+d^{1/\alpha-1}/\varepsilon^2)$ (Rényi) and $O(d^{1+1/\alpha}/\varepsilon^{1/\alpha}+d^{2-2\alpha}/\varepsilon^2)$ (Tsallis) — a large improvement over the previous $O(d^{2/\alpha}/\varepsilon^{2/\alpha})$ — and for non-integer $\alpha>1$, $O(d^2/\varepsilon^{1/\alpha}+d^{1-1/\alpha}/\varepsilon^2)$ Rényi, improving on $O(d^2/\varepsilon^2)$. All match Wang's (2026) lower bounds up to polylogs.

**Key contributions**
- Optimal-up-to-polylog upper bounds for all remaining open regimes (non-integer $\alpha$), completing the table of quantum Rényi/Tsallis sample complexities.
- A new "one-step" linearization inequality: for $\sigma\succeq \tfrac{d}{n}I$, $0\le(1-\alpha)\tr\sigma^\alpha+\alpha\tr(\rho\sigma^{\alpha-1})-\tr\rho^\alpha\le (d/n)^{\alpha-1}\mathrm D_{\chi^2}(\rho\|\sigma)$ (Bures $\chi^2$), proved via concavity of $A\mapsto\tr A^\alpha$ and a Daleckii–Krein/Taylor-with-dominated-convergence argument.
- A bound $\mathrm D_{\chi^2}(\rho\|\hat\rho+\tfrac{2d}{n}I)=O(d^2/n)$ for the regularized output of Bures-$\chi^2$ tomography.
- A Richardson-extrapolation estimator built on Hayashi's covariant pure-state POVM plus random purification, with an explicit bias expansion in Beta-distribution moments.
- A methodological shift: these estimators use tomography/pure-state estimation rather than weak Schur sampling, which all prior estimators relied on.

**How it works** For $\alpha<1$: run $\chi^2$-tomography on $n$ samples, set $\sigma=\hat\rho+\frac{2d}{n}I$, compute $(1-\alpha)\tr\sigma^\alpha$ classically, and estimate $\alpha\tr(\rho\sigma^{\alpha-1})$ by measuring $m$ fresh copies in $\sigma$'s eigenbasis and averaging $s_J^{\alpha-1}$. Bias is controlled by the inequality above ($O(d^{\alpha+1}/n^\alpha)$); variance by careful $\mathbb E[X^2]$ bounds ($\le O(d(d/n)^{2\alpha-1})$ for $\alpha\le1/2$, $O(d^{2-2\alpha})$ or relative-error $O(d^{1/\alpha-1}F^2)$ for $\alpha>1/2$). For $\alpha>1$: convert $\rho^{\otimes s}$ into copies of a random purification, apply Hayashi's POVM; the estimate's coefficient matrix is $\sqrt{1-T}M+\sqrt T G$ with $T\sim\mathrm{Beta}(d^2-1,s+1)$. Schatten-norm Taylor expansion yields $\mathbb E[Y_s]=F+\sum_{j\le k}c_j\mu_j(s)+O(F(d^2/s)^\alpha)$ with $k=\lceil\alpha\rceil-1$; running $k+1$ batches of sizes $2^\ell m$ and taking a linear combination annihilating $\mu_1..\mu_k$ leaves only the $O((d^2/m)^\alpha)$ remainder.

**Why it matters** Settles a decade-old gap for spectral property testing/estimation; the $\varepsilon$-dependence $\varepsilon^{-1/\alpha}$ (rather than $\varepsilon^{-2/\alpha}$ or $\varepsilon^{-2}$) is a genuinely new phenomenon, and the extrapolation-over-batch-sizes trick may transfer to other nonlinear spectral functionals.

**Caveats** Constants are $\alpha$-dependent and blow up as $\alpha\to1$ (e.g. $(1-\alpha)^{-(2\alpha-1)/\alpha}$) and with $\lceil\alpha\rceil$; both estimators require highly entangled collective measurements plus classical post-processing (matrix powers, small linear system). Integer $\alpha>1$ Rényi and $\alpha>1$ Tsallis were already known; polylog gaps remain, and no attempt is made at optimizing success probability beyond $\approx0.98$ or at time complexity.

## 4. Quantum Circuit for General Unitary: Improved T-count via Block Flattening and Dilation

[arXiv:2608.17846](https://arxiv.org/abs/2608.17846) · [SciRate](https://scirate.com/arxiv/2608.17846)

*Pei Yuan, Shengyu Zhang, Wei Zi*

**TL;DR** The authors give a Clifford+$T$ construction for arbitrary $n$-qubit unitaries with worst-case $T$-count $O(d^{5/4}L^{5/8}\log d)$, where $d=2^n$ and $L=n+\log(1/\epsilon)$, improving Tan's $O(d^{4/3}L^{2/3}+dL)$ whenever $L\le d$. The trick is to stop decomposing $U$ into a product of simpler unitaries and instead build a *single* block encoding of the whole matrix, then strip the normalization with QSVT; the gap to the $\widetilde\Omega(d)$ lower bound shrinks from $d^{1/3}$ to $d^{1/4}$.

**Key contributions**
- *Simultaneous block flattening*: for any $U\in\mathrm U(d)$ there exist Boolean sign diagonals $D_1,D_2$ with $V=H_dD_1UD_2H_d$ satisfying $\|P_IVP_J^\dagger\|\le 16\ln 2\sqrt{b/d}\log(2d)$ for *all* $d^2/b^2$ blocks at once.
- A "block-dilation SELECT": all $D^2$ normalized blocks are Julia–Halmos-dilated to $2b\times 2b$ unitaries and packed into one uniformly controlled unitary, yielding a block encoding of $V$ with subnormalization $\rho=O(\sqrt{d/b}\log d)$.
- A robust one-point oblivious amplification lemma: a degree-$Q=\Theta(1/c)$ QSP polynomial with $P(c)=1$ exactly (built from $(-1)^mT_Q(\beta x)$ plus the Gilyén et al. real-to-complex completion), with error propagation $\|A_{\rm amp}-V\|=O(Q^2\delta)$ and clean-input error $O(Q\sqrt\delta)$.
- An analogous result for multiplexed unitaries $\sum_x|x\rangle\langle x|\otimes U_x$, where one sign pair flattens all branches simultaneously.

**How it works** Flattening uses two rounds of concentration: Hoeffding on entries of $UD_2H_d$ (giving row-slab coherence $\mu=16(b/d)\ln 2d$), then Tropp's rectangular matrix Rademacher bound on $\sum_\ell\eta_\ell a_\ell z_\ell^\dagger$ for each block pair, with a union bound over $D^2$ pairs. Because the encoded operator is $V/\rho$ with $V$ unitary, *every* singular value equals $1/\rho$, so a single-point QSVT response suffices, costing $O(\rho)$ queries. Tan's UCU compiler implements one SELECT query in $O(d\sqrt L+b^2L)$ $T$ gates; total $O(\sqrt{d/b}\log d\,[d\sqrt L+b^2L])$, minimized at $b=d^{1/2}L^{-1/4}$.

**Why it matters** Non-Clifford count is the dominant fault-tolerant cost; this is the first improvement to the generic exponent since Tan, and it demonstrates that block-encoding/QSVT machinery — usually used for Hamiltonian-type tasks — beats product decompositions for raw unitary compilation.

**Caveats** The ancilla cost is large, $O(2^n\sqrt L)$ clean qubits (vs. $O(d^{2/3}L^{1/3}+L)$ for Tan), so this is a space–$T$ tradeoff, not a strict improvement; the flattening signs require randomized classical preprocessing with certified numerics, excluded from the accounting. The error metric only constrains the clean-input subspace. The Markov-inequality step is applied to a complex-valued $P$ (constant factor at most). Regime restricted to $L\le d$; the multiplexed appendix is truncated in the source. AI assistance in preparation is disclosed.

## 5. Lie-Algebraic Classical Simulation of Bosonic Systems Beyond Gaussian Dynamics

[arXiv:2608.17094](https://arxiv.org/abs/2608.17094) · [SciRate](https://scirate.com/arxiv/2608.17094)

*Adelina Bärligea, Timothy Heightman, Jakob S. Kottmann, Antonio Acín*

**TL;DR** — The paper extends Lie-algebraic ($\mathfrak{g}$-sim) classical simulation to bosons by replacing the dynamical Lie algebra (DLA) with an *observable-seeded reachable operator module* $\mathcal V(O)$: the smallest real operator space containing $O$ closed under $\mathrm{ad}_{H_k}$. Whenever $\dim\mathcal V(O)=\mathrm{poly}(n)$ and input overlaps are accessible, expectation values, fixed-order/multi-time/OTO correlators, and reverse-mode gradients are exactly computable in polynomial time — recovering Gaussian optics and extending to non-Gaussian inputs, bounded-photon Kerr/pair-hopping dynamics, and nilpotent cubic-phase families.

**Key contributions**
- Reachable-module simulability criterion (Thm. 1): $\langle O(\bm\theta)\rangle = \bm w^\top e^{\theta_L A_{k_L}}\cdots e^{\theta_1 A_{k_1}}\bm e^{\mathrm{in}}$ on a $D$-dimensional module; the DLA condition is the special case $O\in\mathfrak g$ and is sufficient but not necessary. Sidesteps the compact/semisimple assumptions of Somma et al., which excluded bosons.
- Three finiteness mechanisms: (i) Gaussian degree preservation, $\dim\mathcal V(O)\le\binom{2n+m}{m}$ for degree-$m$ quadrature polynomials (linear observables need only $2n+1$ vs. the $\mathcal O(n^2)$ ambient Gaussian algebra); (ii) photon-number sector confinement, $\dim\mathcal H_N=\binom{N+n-1}{N}=\Theta(n^N)$, giving module dimension $\mathcal O(n^{2N_{\max}})$ for arbitrary number-conserving nonlinearities at unrestricted coupling and polynomial depth; (iii) a multi-mode nilpotent polynomial-phase family with cubic-or-higher generators.
- A genuinely bosonic negative result: a finite-dimensional generator algebra does *not* imply a finite observable orbit (unlike spins/fermions) — e.g. Kerr acting on $\hat a$ on full Fock space.
- Controlled squeezing hierarchy: parity-resolved photon-number bands of depth $k$ reproduce number-conserving observables exactly through order $2k+1$ in squeezing strength; leading error $\mathcal O(\lambda^{2(k+1)})$, verified numerically.
- Numerics: operator spreading/OTOCs on interacting chains up to 400 modes, repulsively bound photon pairs with a topological doublon band and flux-reversed edge motion, differentiable control on $9\times9$ lattices, depths 1–8.

**How it works** — Heisenberg-picture propagation is restricted to $\mathcal V(O)$, whose generator actions are $D\times D$ real matrices $A_k$; the state enters only through overlaps $\Tr[B_\alpha\rho_{\mathrm{in}}]$ (or ordered moment tensors $E^{\mathrm{in}}_{\alpha_1\cdots\alpha_m}$ for $m$-point correlators). No Fock cutoff, moment closure, or perturbative truncation; only floating-point matrix exponentials.

**Why it matters** — It cleanly delineates that bosonic simulability is a property of the *dynamics–observable pair*, not the Hamiltonian alone, giving a unified language covering Gaussian optics, bounded-photon interacting lattices, and non-Gaussian gates — relevant for CV advantage claims, device validation, and variational bosonic ansätze.

**Caveats** — Only mean values and *fixed-order* correlators, not sampling or full outcome distributions, so boson-sampling hardness is untouched; the observable order is itself a resource. Efficiency requires $N_{\max}=\mathcal O(1)$ (cost $n^{2N_{\max}}$ degrades quickly) and efficiently computable input moments/restricted generators. Unbounded-operator subtleties are handled by assuming a common invariant domain; the squeezing hierarchy needs explicit analyticity assumptions. Active (number-changing) Gaussian operations break exact sector confinement.

## 6. Hardware-Aware Compilation and Execution of Bivariate Bicycle Codes on Neutral-Atom Systems

[arXiv:2608.17023](https://arxiv.org/abs/2608.17023) · [SciRate](https://scirate.com/arxiv/2608.17023)

*Jason Ludmir, Aditya Ranjan, Nicholas S. DiBrita, Jason Han, Tirthak Patel*

**TL;DR** Park-n-Ride is a compiler/architecture co-design that maps the BB-code (gross code, ⟦144,12,12⟧) logical instruction set — idles, shift automorphisms, in-module and inter-module joint measurements, T-injection — onto zoned neutral-atom hardware while respecting AOD non-crossing, Rydberg blockade, and trap-transfer constraints. Its three main mechanisms (spectral module placement, direction-agnostic parallel torus rolls with monotone resynchronization, interval-colored bridge scheduling) cut estimated runtime by ~18% and transport-induced atom-loss exposure by ~41% versus arbitrary placement on 32–113-module circuits.

**Key contributions**
- A columnar compute-zone layout: vertical "compute columns" of BB modules, each split into idling / bridge-interaction / shift-measurement subzones, with a per-module "logical processing unit" holding bridge and ancilla qubits above each module. Motion is confined within columns, largely sidestepping AOD crossing violations.
- Shift-automorphism scheduling exploiting torus periodicity: T(Δi,Δj) = Roll_i ∘ Roll_j, and each roll can move either a width-k chunk one way or a width-(N−k) chunk the other — four equivalent realizations. A column elects a head module, all modules adopt its directions, giving monotone (hence legal) parallel motion; residual offsets from heterogeneous shift magnitudes are removed by a sorted-residual sweep with staggered SLM drop-offs, costing at most #modules steps.
- Bridge-based joint measurement scheduler: pairs map to column intervals, greedy interval coloring gives disjoint rounds, and ±1 lockstep micro-steps toward interval midpoints guarantee non-crossing.
- Spectral seriation (Fiedler vector of the interaction-graph Laplacian) for module→column assignment, plus a per-column single-server T-factory queueing model.

**How it works** A BB-native tableau circuit becomes a dependency DAG, is layered for maximal parallelism, split into shift/measurement sublayers, and placed; a timing estimator sums AOD travel (55 μm/μs), 100 μs trap switches, and gate times (0.8/2.0 μs) per layer. Idling is a fixed 24-substep monotone stabilizer schedule; measurement sublayers cost ten idle rounds.

**Why it matters** qLDPC codes are moving from theory toward execution, and neutral-atom movement constraints are the binding practical issue. This is a concrete first attempt at end-to-end BB-code compilation for zoned atom arrays, and its error-attribution result — shift automorphisms are orders of magnitude cheaper than syndrome/measurement cycles — is a useful design signal.

**Caveats** Everything is a Python timing/error estimator; no Stim-level circuit simulation, no decoder, no threshold or logical-error-rate curves. The "logical error" figure uses a toy oracle decoder (failure if ≥5 faults, binomial). Measurement time is set to ~0 by design (real readout is O(10²) ms), and there are no baselines from prior work. Two-gross scaling changed runtime by <0.1%, which is suspiciously insensitive given doubled module height. Atom loss is a first-order λ ≈ p_dD + p_sS estimate, with no reloading/erasure handling.

## 7. A Complete Classification of Complex Hadamard Matrices of Order Six

[arXiv:2608.18053](https://arxiv.org/abs/2608.18053) · [SciRate](https://scirate.com/arxiv/2608.18053)

*Mateo Cárdenes Wuttig, Joseph Tindall*

**TL;DR** The authors prove that every order‑six complex Hadamard matrix (CHM) is equivalent to a dephased matrix possessing a "finite‑corner witness" — a 3×3 corner whose two complementary‑block candidate sets are finite — so that the whole class is recovered by a finite, branch‑complete algebraic dilation. This supplies the missing global step in Szöllősi's dilation method and proves his conjecture: outside Karlsson's three‑parameter $H_2$‑reducible family and Tao's isolated $S_6^{(0)}$, every class is obtained algebraically from a corner, generically by solving one quadratic and one cubic in each of the horizontal and vertical directions.

**Key contributions**
- A cubic Gram invariant $\tau_{\rm r}(X)=(XX^\dagger)_{12}(XX^\dagger)_{23}(XX^\dagger)_{31}$ for 3×3 unimodular blocks, with $\mathrm{Re}\,\tau_{\rm r}=\mathrm{Re}\,\tau_{\rm c}$ (proved from equality of the spectra of $XX^\dagger$ and $X^\dagger X$), invariant under all monomial operations.
- An **infinite‑fiber trichotomy**: if the normalized fixed‑Gram fiber of an invertible $X\in\mathbb T^{3\times3}$ is infinite, then $XX^\dagger=3I_3$, or $\mathrm{Re}\,\tau_{\rm r}(X)<0$, or $X$ contains a 2×2 Hadamard block.
- A **corner‑routing** argument exploiting $EE^\dagger+BB^\dagger=6I$, hence $\tau_{\rm r}(E)=-\tau_{\rm r}(B)$: the sign of the invariant flips under block exchange, so a corner with both side fibers finite always exists.
- A complete treatment of the Fourier‑block case, reducing it to $\mathcal T_6\cup\mathcal K_6^{(3)}$.
- Explicit finite‑corner witnesses for the entire Karlsson family, via exact resultant elimination and a Bernstein/de Casteljau positivity certificate.

**How it works** Singular 3×3 corners force a 2×2 Hadamard block (Lemma), so outside the $H_2$‑reducible sector all corners are invertible. Fixing a Gram matrix and eliminating between Haagerup's identity and its conjugate yields a linear eliminant $\mathcal A(x)+\mathcal B(x)y=0$ with $\mathcal A=x(|R|^2-|T|^2)\kappa_S(x)$; unit‑modulus forces $|\mathcal B|^2=|\delta|^2|\kappa_S|^2$ on the circle, and root‑allocation analysis (Möbius maps $m_r$, logarithmic‑derivative sums, the common‑root case $s=z=1$) produces the trichotomy. Finite corners then feed Szöllősi's forced completion $D=-CE^\dagger(B^{-1})^\dagger$, retained iff $D$ is unimodular. Nonvanishing of oriented leading sextic coefficients certifies finiteness.

**Why it matters** Order six is the smallest open case and the obstruction to settling MUB and interferometer questions in $d=6$; a certified finite reconstruction turns an infinite search into finitely many polynomial solves, giving a rigorous computational handle on the $d=6$ MUB problem and six‑mode balanced interferometers.

**Caveats** The result is conditional on two published inputs (Karlsson's $H_2$ classification, Szöllősi's cubic‑root criterion). It is a *finite‑incidence* classification — a certified finite reconstruction scheme — not a new closed‑form parametrization of the non‑Karlsson classes; whether the retained output contains anything beyond the known families is not settled here. Substantial parts (245 resultants, quotient‑ring tests, ten‑box Bernstein subdivision) rest on exact computer algebra, and the Lean formalization covers only a stated sub‑boundary. Source is truncated, so the Sec. IV geometry and audit scope could not be fully checked.

## 8. Computationally Efficient Optimization of Per-Qubit Clifford Deformation for Non-uniform Biased Noise

[arXiv:2608.17870](https://arxiv.org/abs/2608.17870) · [SciRate](https://scirate.com/arxiv/2608.17870)

*Won Joon Yun, Andrew Nemec, Jonathan M. Baker*

**TL;DR** Chameleon replaces decoder-in-the-loop search for per-qubit Clifford deformations with a decoder-free surrogate: a Bhattacharyya upper bound on the pairwise-confusion probability of low-weight "ambiguity operators" (logical representatives), which factorizes into one $2\sqrt{r(1-r)}$ term per qubit. Minimizing this with a cross-entropy method cuts frame-selection time for BB72 from ~1.2 days to 3.1 minutes while lowering worst-axis logical error rate by 13%/7%/4% on average (surface/color/BB) versus the best prior deformation baseline.

**Key contributions**
- An analytic, decoder-free LER surrogate $U_c(F)=\sum_{\ell\in\mathcal{A}_c}\prod_{q\in\ell}\gamma(r_c^q(F))$, derived from $\Pr(e)\le\sqrt{\Pr(e)\Pr(e\oplus\ell)}$ under independent Pauli noise; per-operator cost drops from $O(2^w)$ to $O(w)$.
- Reusable, code-only (noise-independent) ambiguity-set LUT with weight cutoff $W=d+2$ (geometric, small BB) or $d+10$ via randomized Gaussian elimination + BB translation orbits for BB72.
- Two-stage CEM search: Bernoulli over $\{I,H\}^n$ (3,000 evaluations), then categorical over all $6^n$ frames, warm-started, deployed only if the surrogate improves by $\tau=20\%$.
- Separation of "Type-A" (information-theoretic decoding ambiguity, $\lambda(e')\le\lambda(e_{true})$) from "Type-B" (decoder-suboptimality) failures; only Type-A is targeted/reported.
- Objective variants for worst-axis memory ($\min\max\{U_X,U_Z\}$) and single-axis workloads (magic-state prep gets $0.34\times$–$0.67\times$ LER$_Z$).

**How it works** The frame is a per-qubit $S_3$ permutation of $(p_X,p_Y,p_Z)$; only the CSS axis marginals $r_X=p_X+p_Y$, $r_Z=p_Z+p_Y$ matter for binary ($I/H$) frames, while full frames also reassign which physical rate lands on the shared $Y$ component. Because $-\log\Gamma_\ell$ is a weighted distance, minimizing $U_c$ raises the effective weight of the most vulnerable same-syndrome confusions — coordinating frames across an operator's support rather than greedily suppressing each qubit's dominant axis (the failure mode of Tiurev et al.'s local rule, which loses to CSS in 27% of 1,756 instances).

**Why it matters** Deformation is free (no qubits, rounds, or distance cost) yet must be recomputed per calibration map; a surrogate that ranks frames well (Spearman $\rho=0.89$–0.98 on Willow) makes recalibration-speed compilation feasible, and the method is code-agnostic (surface, 6.6.6 color, BB qLDPC).

**Caveats** Surrogate fidelity collapses on weakly biased devices ($\rho=0.34$ on IBM Miami surface code); several table entries show *negative* gain (color $d5$ Berlin $-3\%$, BB36 Willow $-3\%$). Results use phenomenological noise; circuit-level (Si1000, biased idle only) gives just 5.2% average. Reported LER is Type-A only, which excludes up to ~86% of failures for approximate decoders. The main CDSC baseline gets only 24 decoder-validated candidates. Full-frame refinement is inert on real transmon maps (no $Y$-dominant qubits); the 327% gain is synthetic. Bound is a union bound over a truncated operator set and ignores correlated/circuit-level errors.

## 9. No extension of the Quantum Tensor Product admits a Superposition principle

[arXiv:2608.17572](https://arxiv.org/abs/2608.17572) · [SciRate](https://scirate.com/arxiv/2608.17572)

*Vincenzo Fiorentino, Kuntal Sengupta*

**TL;DR** The paper gives a Hilbert-space-free, statistics-based definition of superposition in Generalised Probabilistic Theories: an extremal state is a superposition of a subset of a *maximal* perfectly-discriminable (MPD) set if it is probabilistic on the corresponding outcomes of a maximally-distinguishing extremal (MDE) measurement. From this it distils three inequivalent "superposition principles," and shows that the quantum tensor product is the largest composition rule for quantum subsystems satisfying the "mutual" principle — so no strict non-signalling extension (with the no-restriction hypothesis) admits all three.

**Key contributions**
- Operational, *relational* definition of superposition applicable to any GPT (contrasted with Aubrun et al.'s non-simpliciality reading and D'Ariano et al.'s infinite-extremal-state requirement); maximality of the discriminable set is shown necessary via a qutrit counterexample.
- Three principles — *complete* (every extremal state is a superposition), *uniform* (relative to every MPD set), *mutual* (superposition is reciprocal) — proven equivalent in quantum theory but non-hierarchical in general, witnessed by two constructed toy GPTs (GPT-1: uniform+mutual, not complete; GPT-2: uniform only).
- Main theorem: any $\mathcal{S}_{\mathcal Q_{1,2}} \subsetneq \mathcal S \subseteq \mathcal S_{\mathcal Q_1}\otimes_{\max}\mathcal S_{\mathcal Q_2}$ fails mutual superposition; corollary rules out all three principles simultaneously.
- Inheritance lemma: if the composite's operational dimension factorises ($d_1d_2$), existence and completeness pass from *one* subsystem to the composite; uniformity needs "outcome sharpness" of MDEs. Mutuality is the sole exception.
- Entanglement (any composition strictly above the minimal tensor product, with factorising operational dimension) implies superposition; the converse fails. PR box shown explicitly to be a superposition of four local deterministic boxes.
- Preparational uncertainty (defined as $\mathrm{Det}(\mathsf M)\cap\mathrm{Det}(\mathsf N)=\emptyset$) implies complete superposition, and under outcome sharpness is *equivalent* to a superposition statement between MPD sets.

**How it works** Standard finite-dimensional GPT machinery: compact convex state space, MDE measurements assumed informationally complete, operational dimension = size of an MPD set. Classification is by explicit computation across classical, quantum, GLT, Boxworld, Spekkens' toy theory, and regular $n$-gons; Spekkens' theory satisfies all three principles (via equivalence-balance), Boxworld only existence.

**Why it matters** Provides a candidate operational replacement for the tensor-product axiom in quantum reconstructions, and a theory-independent handle on "superposition" for proposed tests of gravitationally-induced entanglement and indefinite causal order, where "holding a mass in superposition" is currently formalism-dependent.

**Caveats** Subsystems must already be quantum — no single-system reconstruction. No-restriction hypothesis and outcome sharpness are load-bearing. Superposition is defined only for extremal states. The factorising-operational-dimension assumption fails in general (pentagon compositions). In $n$-gons a state can be a "superposition" of a set yet perfectly distinguishable from some members, and the odd/even parity gap in uniform superposition is unexplained. Finite dimensions only; proofs are in the (here truncated) appendix.

## 10. A Simple Algebraic Proof of the PCP Theorem

[arXiv:2608.17429](https://arxiv.org/abs/2608.17429) · [SciRate](https://scirate.com/arxiv/2608.17429)

*Prashanth Amireddy, Amik Raj Behera, Srikanth Srinivasan, Madhu Sudan, Sophus Valentin Willumsgaard*

**TL;DR** The authors give an algebraic proof of the PCP theorem (NP ⊆ PCP[O(log n), O(1)]) that uses no PCP composition, no PCPs of proximity/assignment testers, and no invocation of NP-completeness inside the construction — only code concatenation plus standard polynomial manipulation. The key new gadget is a "set-multilinear" encoding of univariate polynomials that makes the lines-table of a low-degree test itself constant-query testable over a small alphabet, removing the last obstacle to a composition-free construction. Verifier and honest prover each fit on roughly one page of pseudocode.

**Key contributions**
- A set-multilinear encoding SetML_{d,c,m₁}: a degree-d univariate P(Y) is mapped to a c·m₁-variate *degree-c* set-multilinear polynomial by writing each exponent k in base m₁ (k = Σ kⱼm₁ʲ ↦ X_{0,k₀}···X_{c-1,k_{c-1}}), with evaluation recovered via Φ(λ) = ((1,λ,…,λ^{m₁-1}),…,(1,λ^{m₁^{c-1}},…)). Since c is constant, the encoding is testable and self-correctable with O(1) F_q-queries.
- Observation (building on the authors' STOC'26 work and Goldreich ECCC'25) that low-degree testing — specifically the polylog-bit alphabet of the lines table — is the sole bottleneck preventing a concatenation-only PCP with O(log n) randomness.
- A fully composition-free PCP: constant-query low-degree test, local corrector, and zero-on-grid test all directly over F₂, assembled into a verifier for 3-COLOR.
- Explicit, self-contained pseudocode for verifier and completeness prover (Appendix), offered as the operational measure of "simplicity."

**How it works** The atomic PCP (from BFL/ALMSS, streamlined via Ben-Sasson–Sudan and the authors' earlier work) reduces 3-coloring on n vertices to (i) a constant number of low-degree tests on m-variate polynomials over F_q with m,d,q = polylog n, and (ii) a vanishing-on-H^m check, which via Combinatorial Nullstellensatz is turned into a single "vanishing certificate polynomial" and hence one extra low-degree test — no sum-check. All F_q-valued oracles are concatenated with a degree-r Hadamard (long) code over F₂^t, t = O(log log n), of length 2^{C(t,≤r)}, which is affordable and lets degree-r relations P(f(a)) be read with one query via a precomputed Λ_{P,L}. The lines table, whose entries are (d+1)-tuples over F_q (polylog n bits), cannot be long-coded without quasipolynomial blowup; instead each line polynomial is stored in set-multilinear form and tested only for total degree ≤ c. Soundness only yields closeness to *some* degree-c multivariate polynomial, whose pullback along Φ has univariate degree O(cd) — weaker than d, but sufficient for the ALMSS line-point test analysis (which needs q > Cd³).

**Why it matters** This is a plausible candidate for a teachable, one-lecture-sequence proof of the PCP theorem, and it clarifies conceptually that composition machinery was never essential to the algebraic route — concatenation suffices once low-degree testing is alphabet-friendly. Relevant to anyone teaching PCPs, and to proof-complexity/PCP practitioners interested in simpler honest-prover descriptions.

**Caveats** The ALMSS line-point low-degree test is used as a black box (its analysis is the remaining nontrivial import), as is Rubinfeld–Sudan. The authors concede the proof-oracle mechanism could count as "0.5 compositions" à la Goldreich. Soundness γ is an unspecified small constant; no attempt at optimizing query count, proof length, or soundness. "Simplicity" is measured by pseudocode length, which is subjective; source shown is truncated so the final parameter setting (d = Õ(log²n), choice of c, m) isn't fully verifiable here.
