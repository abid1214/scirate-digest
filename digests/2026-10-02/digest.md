# SciRate Daily Digest — 2026-10-02

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Multivariate Quantum Signal Processing

[arXiv:2610.01125](https://arxiv.org/abs/2610.01125) · [SciRate](https://scirate.com/arxiv/2610.01125)

*Guang Hao Low*

**TL;DR** This paper extends quantum signal processing from one block-encoded matrix to many simultaneously-accessed, noncommuting, nonnormal ones by recasting query algorithms as multiport infinite-impulse-response filters: each oracle becomes a Cayley-transformed "load" attached to a known unitary junction, and the composite transfer function is analytic and contractive on the polydisk by accretivity alone — no diagonalization required. A complete characterization of achievable transfer functions plus an "analytic clock shaping" theorem converts these transfer functions into finite circuits with logarithmic error dependence, yielding per-oracle query complexities of the quasinorm form (Σⱼ√(Cⱼλⱼ))² + O(‖C‖₁log(1/ε)) for multi-term Hamiltonian simulation, linear systems, ODEs, ground states, and generalized eigenvalue problems.

**The big picture** Most quantum algorithm design assumes a single oracle whose cost is counted uniformly, but real problems — a Hamiltonian split into chemically distinct pieces, a system with fast and slow degrees of freedom, streaming sensor data — involve several access routines of wildly different cost and importance. This work gives a systematic design language, borrowed from classical multiport filter and scattering theory, in which each access routine is a port of an interconnected network, is queried at its own rate, and contributes to the total cost in proportion to the square root of its cost times its influence. The payoff is that cheap, dominant terms can be queried often and expensive, weakly coupled ones rarely, with provable uniform error guarantees instead of heuristic splitting.

**Key contributions**
- A transfer-function/IIR formalism for multivariate, noncommuting block encodings, with contractivity proved from accretivity of a Schur-complement "load" rather than spectral decomposition.
- Analytic clock shaping: horizon N = O(|t|Σⱼ rⱼλⱼχⱼ + maxⱼκⱼrⱼ log(1/ε)) from an analyticity radius ζ ≈ 1/(64(r\*+τ)) plus controlled exterior growth; a nuclear-norm-2 clock and oblivious amplitude amplification give near-unity success at exactly qⱼ = 3⌊(N−1)/rⱼ⌋ calls.
- A delay-allocation lemma proving the integer query schedule is within a factor 4 of the quasinorm optimum, with an explicit constructive schedule and a geometric-program version that also optimizes gate cost.
- Finite realization by a cascade of J Cayley stages (J only enters gate count logarithmically, via address width), accurate on the whole length-N Toeplitz block, not merely at the evaluation point.
- Downfolding: balanced congruence (sector scales set to response bounds, optimal by AM–GM), an M-matrix "comparison matrix" giving blockwise response bounds ‖QᵢX‖ ≤ Σₖ(M⁻¹)ᵢₖhₖ from scalar norm data, and sensitivity ‖ΔH_eff‖ ≤ Σⱼλⱼχⱼηⱼ licensing coarse (cheaper) oracles for weakly responding sectors.

**How it works** Each Hermitian-unitary block encoding is inserted through a marker variable zⱼ; delays zⱼ = z^{rⱼ} set query rates. Closing internal sectors by feedback performs the Schur complement exactly (invertibility of K suffices), and the operator Schwarz/Carathéodory bound ‖S(z)‖ ≤ Λ₀(1+|z|)/(1−|z|) controls impulse coefficients.

**Why it matters** This resolves open per-oracle complexities for multi-term simulation, gives Θ(√d‖H‖_{1→2}t) for sparse simulation, and supplies a principled cost model for downfolded electronic-structure Hamiltonians and multiscale graph data.

**Caveats** All guarantees are conditional on classically known promises — gaps Δ, coupling bounds, response bounds ρᵢ, conditioning κⱼ — whose computation is separately costed. Constants are large (radii 1/64, error budgets ε/49152). Internal-sector contributions still carry λ_K/Δ rather than the physical h_K/Δ. Verification of the full framework from the available source is partial.

## 2. Polynomial-time classical and quantum simulation of quantum impurity models

[arXiv:2610.02167](https://arxiv.org/abs/2610.02167) · [SciRate](https://scirate.com/arxiv/2610.02167)

*Jiaqing Jiang, Nathan Ju, Ojas Parekh, Chaithanya Rayudu, Andrew Zhao*

**TL;DR** The authors give unconditional classical algorithms that compute the ground-state energy of a quantum impurity model (constant-size interacting impurity + arbitrary free-fermion bath of $n$ modes) to additive error $\delta$ in $\mathrm{poly}(n,\delta^{-1})$ time, and the partition function / Gaussian-observable expectations at inverse temperature $\beta$ in $\mathrm{poly}(n,\beta,\delta^{-1})$ time — improving Bravyi–Gosset's quasipolynomial bound and giving the first rigorous thermal guarantee. Complementarily, they show that estimating nonequilibrium Green's functions of time-dependent impurity Hamiltonians is $\mathsf{DQC}_1$-complete at infinite temperature and $\mathsf{BQP}$-complete at finite temperature.

**The big picture** Impurity models — a few strongly interacting particles coupled to a large non-interacting environment — are the computational engine inside embedding methods like dynamical mean-field theory, and proposals for quantum-enhanced electronic structure often target exactly this subproblem. This work settles their complexity for equilibrium quantities: they are provably easy classically, at any temperature, with no assumptions about bath geometry, gaps, or coupling strength. That removes any hope of exponential quantum speedup for the static part of the impurity solver, while simultaneously proving that the dynamical, out-of-equilibrium quantities these methods also need are as hard as universal quantum computation — so if quantum advantage exists here, it lives entirely in the real-time dynamics.

**Key contributions**
- Polynomial-time classical ground-energy algorithm (previously quasipolynomial).
- First rigorous polynomial-in-$\beta$ thermal simulation, beating the generic exponential/subexponential $\beta$ scaling of MPO and sign-problematic CT-QMC bounds.
- A "compression lemma": the ground state (and the thermally gapped part of the Gibbs state) has $1-\delta$ weight on a subspace of dimension independent of impurity interaction and hybridization strength.
- A quantum Gibbs-state preparation algorithm with $\mathrm{poly}(n,\beta,\delta^{-1})$ gates.
- $\mathsf{DQC}_1$- and $\mathsf{BQP}$-completeness of nonequilibrium Green's functions, via a new $q\to q+1$ mode encoding of circuits into fermions.

**How it works** The core is a *bandwise Krylov basis*: partition the bath single-particle spectrum into logarithmic bands $[\omega_\ell,2\omega_\ell)$ (à la NRG), block-Lanczos-tridiagonalize within each band, and absorb the first Krylov shell of each band into an "enlarged impurity." This yields a 1D chain of blocks of size $\le 2m$ in which the enlarged-impurity/residual-bath coupling is bounded by $2\omega_\ell$ — removing the problematic $g/\omega$ ratio. Exponentially weighted occupation statistics $F_q=\sum e^{\text{dist}}\langle n_{i_1}\cdots n_{i_q}\rangle$ are then bounded by a recursion derived from $\langle a_j^\dagger[a_j,H]\rangle\le 0$ plus positivity of the weighted bath matrix, giving concentration on a small subspace that is diagonalized exactly. For thermal states, partial compression yields $H_{\mathrm{ref}}+V$ with $\beta\|V\|=O(\log n)$, making CT-QMC (classical) and quantum belief propagation (quantum) efficient. Hardness uses algorithmic cooling to distill near-pure qubits from thermal ones.

**Why it matters** It puts the decades-long empirical success of impurity solvers on rigorous footing, and sharply redirects quantum-advantage claims for DMFT toward dynamics.

**Caveats** Runtimes scale exponentially in impurity size $m$ (treated as constant), blocking extension to Hubbard-type extensive interactions; precision dependence is $\mathrm{poly}(\delta^{-1})$, not $\log$; polynomial degrees are unstated and plausibly large. Hardness is proven for time-dependent coefficients, not for equilibrium Green's functions of static impurity Hamiltonians. Polynomial quantum speedups for static properties remain open.

## 3. A provable quantum advantage for approximate optimization via decoded quantum interferometry

[arXiv:2610.02145](https://arxiv.org/abs/2610.02145) · [SciRate](https://scirate.com/arxiv/2610.02145)

*Maximilian J. Kramer, Elies Gil-Fuster, Benjamin D. M. Jones, Jens Eisert, Franz J. Schreiber*

**TL;DR** The paper proves an unconditional oracle (query-complexity) separation for *approximate* optimization achieved by Decoded Quantum Interferometry: on a family of balanced "folded OPI" instances built from folded Reed–Solomon codes with membership oracles for the acceptance sets, DQI attains expected score $(1+\sqrt{R(2-R)})/2$ using $M$ coherent queries, while any classical algorithm beating Prange's threshold $(1+R)/2$ by a fixed constant needs $\exp(\Omega(M/\log M))$ queries. A second construction, replacing unique decoding with complete list decoding plus Jo-style coherent fiber summation, pushes the achievable score to $1/2+\sqrt{R(1-R)}$ (and to exact search for $R>1/2$) on *typical* sampled instances.

**The big picture** Decoded quantum interferometry is a promising quantum optimization framework that beats all *known* classical heuristics on certain algebraic problems, but nobody had shown it beats *every* possible classical algorithm. This work supplies the missing proof in a black-box setting: by bundling the acceptance tests into blocks, borrowing the code family from a known exact-search separation, and sharpening the classical lower-bound argument from "find a perfect solution" to "find a good-enough solution", it pins down the exact score any efficient classical algorithm can reach and shows the quantum algorithm exceeds it. This is the first rigorous evidence that the interference-plus-decoding mechanism itself — not a repackaged Shor speedup — yields an optimization advantage.

**Key contributions**
- A common oracle model (per-block balanced membership oracles, $|\Sigma|=q^h=\exp(\Theta(M\log M))$) in which DQI, Prange, and a classical lower bound can all be stated.
- Verification that the DQI semicircle score law extends to *folded* predicates under membership-oracle access (stated but not proved in Jordan et al.).
- Extension of the Yamakawa–Zhandry classical hardness argument from exact search to approximation, via list recoverability plus a conditional binomial-tail bound and union bound.
- A beyond-DQI quantum algorithm using complete list decoding of the folded dual with coherent fiber summation, achieving $\alpha_{\rm fib}(R)$ on typical instances; exact search for $R>1/2$.

**How it works** Parameters: $h=M+2$, $N=hM$, $q=N+1=(M+1)^2$ (characteristic two), $K=\lfloor RN\rfloor$, $J=\lfloor K/h\rfloor$. The folded dual is a folded GRS code with block distance $\ge J+1$; choosing filter degree $\ell_M=\lfloor (J-1)/2\rfloor$ keeps $2\ell_M+1\le J$, so a degree-$\ell$ filter state requires only scalar Berlekamp–Massey unique decoding ($h\ell_M<(K+1)/2$ errors), applied coherently. With $\ell_M/M\to R/2$, the semicircle law gives $\alpha_{\rm Q}$. Prange picks accepted symbols in $J=\lfloor RM\rfloor$ blocks and interpolates; remaining blocks accept with probability $1/2$, giving $(1+R)/2$. Since $\mathrm{OPT}=1$ with doubly-exponentially high probability, score bounds transfer to approximation ratios.

**Why it matters** At $R=0.3$: classical $0.65$, DQI $\approx 0.857$, fiber method $\approx 0.958$. This closes (in the oracle world) the most-contested question about DQI and gives a clean template for arguing approximation hardness from exact-search oracle lower bounds.

**Caveats** It is a *query* separation in an oracle model, not a standard-model or time-complexity result; scalar OPI hardness remains open. The block alphabet is exponentially large, folding is essential, and the oracle interface deliberately forbids a unit-cost multiplexed block index — the separation is sensitive to this convention. The classical lower bound is distributional (uniform random half-size acceptance sets) and relies on the exact-balance promise. The beyond-DQI $\alpha_{\rm fib}$ guarantees hold only on typical sampled instances and do not constitute a proven separation; attainment of the endpoint for $R\le 1/2$ is not asserted.

## 4. One-Shot any Code

[arXiv:2610.02137](https://arxiv.org/abs/2610.02137) · [SciRate](https://scirate.com/arxiv/2610.02137)

*Andrew C. Yuan*

**TL;DR** Any CSS QLDPC code can be "lifted" by a renormalization-group-style gadget into a larger CSS QLDPC code that is genuinely single-shot: one round of (noisy) syndrome extraction plus a local, logarithmic-depth decoder suffices, with a decoder-independent constant threshold against jointly local-stochastic data and measurement noise and logical failure $O(Tn)\exp[-\Omega(m^\alpha)]$ over $T$ rounds for a block-size blow-up factor $m$. If the seed code already has a single-shot decoder with suppression $\Omega(n^\beta)$, the composite inherits the better threshold and multiplies suppression to $\Omega(m^\alpha n^\beta)$.

**The big picture** Fault-tolerant quantum memories normally need many repeated rounds of measurement to beat measurement errors; single-shot codes avoid this, but they are rare and usually constructed by hand with special expansion properties. This work gives a generic recipe: take any sparse CSS code you like, add a hierarchy of redundant checks built from short repetition codes, and the result decodes single-shot with a parallel local decoder and a threshold that does not depend on which decoder you use for the original code. It also shows that the single-shot property automatically implies passive self-correction, tying together two previously separate notions of robustness.

**Key contributions**
- A short proof that single-shot codes are self-correcting.
- A level map, built by alternating a construction and its transpose-dual so that both X and Z sectors acquire metachecks, turning $[[n,k]]$ into $[[nm,k]]$ while preserving LDPC-ness.
- A hierarchical "cleaning/descent" decoder with $O(\log m)$ parallel depth and a constant threshold $p_{\rm RG}$ for joint data + measurement local stochastic noise.
- A noise-transfer theorem: residual errors at the seed level are again local stochastic with rate $(p/p_{\rm RG})^{c\,\tilde\kappa^{-\ell}}$, enabling composition with any seed decoder and the multiplicative suppression enhancement.

**How it works** Each level glues local cones over a length-$m$ repetition code; homotopy-equivalence arguments reduce the layered complex to a simple column complex, so syndrome "cleaning" reduces to flux-matching on blocks. For $m=3$ the authors bound the relative coexpansions ($\zeta^{QX}\le 9/7$, $\zeta^{ZQ}\le 4/3$) and obtain a single-pass contraction $\kappa=4/9$, crucially below $1/2$ — the threshold needed (unlike prior self-correction work, where $\kappa<1$ sufficed) because measurement noise forces a "noisy contraction" $\kappa/(1-\kappa)<1$. A fill bound $c_f<3$ controls syndrome spreading. Failure analysis uses a three-time-slice "temporal RG graph", shows any failure requires a large connected witness cluster whose size is $\Omega$ of the number of top-level faults, and applies standard Gottesman-style cluster-entropy counting.

**Why it matters** This converts single-shot QEC from a property of special codes into a black-box transformation, with a strictly local, shallow decoder — relevant for real-time decoding bottlenecks and for architectures where repeated syndrome cycles are expensive. The enhancement result also offers a route to boost a code whose own threshold is worse than $p_{\rm RG}$.

**Caveats** The rate collapses: $k$ is fixed while qubits grow by $m$, and the suppression exponent $\alpha$ appears small (roughly $\log(1/\tilde\kappa)/\log(\text{per-level blow-up})\sim 0.1$ with $\kappa=4/9$), so overheads may be large in practice. No numerical value or simulation for $p_{\rm RG}$ is given, and the enhancement requires $\ell$ large enough that the transferred rate falls below the seed threshold. Structural hypotheses ($|x\wedge z|=2$, connected local graphs) are assumed, though claimed removable, and syndrome-extraction circuit-level noise is not treated — only phenomenological joint local stochastic noise.

## 5. Approximation theorems for fermionic Gaussian states

[arXiv:2610.01860](https://arxiv.org/abs/2610.01860) · [SciRate](https://scirate.com/arxiv/2610.01860)

*Amir-Reza Negari, Farzin Salek, Zoltán Zimborás, Aram Harrow, Patrick Hayden, Jens Eisert*

**TL;DR** The authors observe that the bona-fide condition for Majorana covariance matrices ($\mathbb{1}+iM\succeq 0$, hence $MM^T\preceq\mathbb{1}$) immediately implies a sharp "covariance monogamy" bound: for a region $A$ correlated with disjoint regions $B_1,\dots,B_k$, the cross blocks obey $\sum_i X_iX_i^T\preceq\mathbb{1}_A$, so the average $\|X_i\|_2^2\le 2m_A/k$. From this one-particle inequality alone they derive (i) a $\sqrt{2m/D}$ product-state approximation to ground-state energy and free energy of quadratic fermionic Hamiltonians on $D$-regular graphs, (ii) a finite Gaussian de Finetti bound $\|\rho_{A_1\cdots A_k}-\rho_A^{\otimes k}\|_1\le 4m_A(k-1)/n$, and (iii) $O(1/r)$ decay of conditional mutual information across a buffer, hence $O(r^{-1/2})$ recoverability.

**The big picture** A long-standing intuition in many-body physics is that when a degree of freedom is coupled to very many others, or when a state is symmetric under swapping many identical copies, the system behaves as if it had no correlations at all — mean-field theory becomes accurate. For free-fermion systems, all correlations live in a single matrix of two-point functions, and the mere requirement that such a matrix come from a genuine quantum state already caps how much correlation one region can share with many others. The paper shows that this elementary constraint, used directly, reproduces and sharpens three otherwise unrelated approximation theorems — mean-field energy bounds, de Finetti theorems, and approximate conditional independence across a spatial buffer — with short proofs and better rates.

**Key contributions**
- A sharp monogamy inequality for fermionic two-point functions, valid for arbitrary (non-Gaussian) physical states, with a saturating example for every $k$.
- Product-state energy bound $e_0(H)+\sqrt{2\log_2 d_{\rm loc}/D}$, improving Brandão–Harrow's $(d_{\rm loc}^2\log d_{\rm loc}/D)^{1/3}$ to $D^{-1/2}$ with only polylogarithmic local-dimension dependence; approximant can be taken pure and a parity eigenstate; extends to arbitrary (non-quadratic) even on-site terms.
- A finite-temperature analogue: the product of one-site Gibbs marginals is within $\sqrt{2m/D}$ of the free-energy optimum.
- A covariance-level fermionic de Finetti theorem whose limiting measure is a *point mass* — infinite exchangeability within the Gaussian class implies exact product structure.
- CMI bound $I(A:C|B_r)\le K/r$ for spatially clustering Gaussian states, plus Fawzi–Renner recoverability.

**How it works** Edge energies of a quadratic Hamiltonian are exactly linear in the covariance block, $\mathrm{tr}(\rho H_{ij})=-\mathrm{tr}(K_{ij}^TX_{ij})$, with $\|K_{ij}\|_1=\|H_{ij}\|\le1$; Cauchy–Schwarz plus monogamy and Jensen bound the average edge error. For de Finetti, graded copy-permutation symmetry forces all off-diagonal blocks equal and *antisymmetric*, so $M^{(n)}=P_+\otimes(M_A+(n-1)Y)+P_-\otimes(M_A-Y)$; admissibility of both sectors forces $\|Y\|_1=O(m_A/n)$, converted to trace distance via $\|\rho_M-\rho_{M'}\|_1\le\frac12\|M-M'\|_1$. The CMI result expands Gaussian entropies as traces of compressed Green operators and sums Green-function paths crossing the buffer.

**Why it matters** Clean, optimal-constant benchmarks for mean-field accuracy and extendibility hierarchies in free-fermion systems; relevant to Hartree–Fock-type variational bounds, matchgate/fermionic shadow tomography, and entanglement-of-modes theory under parity superselection.

**Caveats** The de Finetti theorem assumes the joint state is Gaussian and permutation-symmetrically extendible — strictly narrower than quantum de Finetti, which is what buys the point-mass conclusion. Product/separability notions are tied to a fixed mode partition and global ordering. The free-energy bound simply discards the entropy difference, so it is $\beta$-independent and presumably loose at high temperature. Most strikingly, exponentially clustering mutual information yields only $1/r$ CMI decay; whether the path expansion can be improved to exponential (as in recent Gibbs-state results) is left open. All statements are finite-mode; the thermodynamic/continuum limits are not treated.
