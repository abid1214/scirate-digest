# SciRate Daily Digest — 2026-09-17

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Exact logical error rates for magic state cultivation

[arXiv:2609.18922](https://arxiv.org/abs/2609.18922) · [SciRate](https://scirate.com/arxiv/2609.18922)

*Kwok Ho Wan, Ainhoa Zapirain*

**TL;DR** The authors compute the acceptance and logical error probabilities of the $d=3$ and $d=5$ magic state cultivation circuits *exactly* — all fault orders, real $T$ gates rather than the $S$-gate sampling proxy — by combining Pauli propagation with binary tensor-network contraction in exact arithmetic, and give closed-form series in $x=p/(1-p)$ through order $x^{10}$. The exact results reproduce published Monte Carlo values within sampling error, and reveal that the nominal $d=3$ and $d=5$ circuits have fault distances of only 2 and 3.

**The big picture** Distilling the non-Clifford resource states that fuel a fault-tolerant quantum computer is expected to dominate its cost, so the failure rate of the small circuits that prepare and check those states is a load-bearing number in every architecture estimate. Until now those rates have come from Monte Carlo sampling, which is noisy at the low error rates that matter and typically substitutes an easier-to-simulate stand-in gate for the actual non-Clifford operation. This work replaces sampling with an exact symbolic calculation that accounts for every possible pattern of faults and uses the genuine non-Clifford gates, yielding error rates as exact numbers and as polynomial expansions in the noise strength. It also shows that both circuits tolerate fewer simultaneous faults than their nominal distance suggests, which directly downgrades the protection these building blocks provide.

**Key contributions**
- Exact (not sampled) acceptance and logical error rates for the Clifft and SOFT cultivation circuits at $d=3,5$, including all fault orders, at several circuit-level noise strengths.
- Analytic series expansions of the logical error rate in $x=p/(1-p)$ to order 10.
- Simulation with actual $T$/$T^\dagger$ gates rather than the $S$-gate proxy used in sampling-based studies.
- Identification of reduced fault distances $d_{\text{fault}}=2$ and $3$, explaining distance degradation seen in companion work (concurrently found by Chan et al.).

**How it works** Depolarising covariance ($\mathcal N_{1,p}(V\rho V^\dagger)=V\mathcal N_{1,p}(\rho)V^\dagger$) lets noise adjacent to the $T$ layers be commuted into the Clifford block, where every fault is a Pauli and the whole internal fault pattern collapses to a single data Pauli $P(\boldsymbol u,\boldsymbol z)$ before the exit layer. The acceptance amplitude for a fixed incoming error and fault pattern becomes a Gauss sum $\mathcal G=2^{-m}\sum_h i^{f(h)}$ over the $2^m$ masks of $C^\perp$, with $f$ quadratic mod 4; polarising $f$ gives a symmetric binary matrix $M$, so $|\mathcal G|^2$ is either 0 or $2^{-\operatorname{rank}M}$ according to consistency of $Mh=b'$ — a pure bit count ($4\times4$ at $d=3$, $10\times10$ at $d=5$). Averaging over internal faults is done by a tensor network: the $Z$-error index is Fourier transformed so CNOTs act identically on the $X$ mask and the dual variable, each depolarising channel becomes a small kernel, and one open contraction (with incoming labels free) fills the response tables $F_A,F_B$; stages are then joined to get $A(p),B(p)$. The network is evaluated twice — modular arithmetic at rational $p$ for exact fractions, and truncated polynomials for the series. Results are cross-checked against a coherent $2\times2$ code-restricted matrix computation and a 13-qubit state-vector simulation across all one- and two-site Paulis plus random cases.

**Why it matters** Anyone budgeting magic-state factories now has exact, noise-free reference numbers and low-order coefficients against which samplers and decoders can be validated, plus a warning that cultivation's effective fault distance is below nominal. The Gauss-sum/bit-count machinery is a reusable tool for exact analysis of small non-Clifford postselected circuits.

**Caveats** The covariance trick is specific to depolarising (identity-plus-full-depolarisation) noise and explicitly fails for biased or purely dephasing channels, so the method does not transfer to general noise models. The calculation assumes an ideal encoded input to each stage and the specific circuits/detector conventions of the two source papers; at $d=5$ the response tables reach $2^{19}$ entries, so scaling to larger distances is unclear. Series truncation at order 10 limits extrapolation to very small $p$, and the reduced fault distances are established for these circuits only, not for cultivation in general.

## 2. Diagnosing and Restoring the Degraded Fault Distance of Magic State Cultivation

[arXiv:2609.17706](https://arxiv.org/abs/2609.17706) · [SciRate](https://scirate.com/arxiv/2609.17706)

*Tim Chan, Armands Strikis, Zhu Sun, Zhenyu Cai*

**TL;DR** — The known gap between T-state and S-state magic state cultivation is explained: Pauli hook errors inside the final double-check circuit get rotated by the physical T gates into *coherent Clifford* errors (tensor products of H₊/H₋/Z), which map the colour code to a *different* stabiliser code whose codespace partially overlaps the original — so postselection accepts a logically wrong component instead of rejecting it. This drops the fault distance of distance-3 (-5) T cultivation to 2 (3), whereas S cultivation keeps 3 (5). Adding a small number of Z flag qubits to the double check restores O(p⁵) pre-escape scaling, giving 4.9× lower logical error at p=10⁻³ for 1.36× more attempts (12.4× at p=5×10⁻⁴ for 1.17× cost).

**The big picture** — Cultivation is the leading resource-efficient way to prepare the non-Clifford resource states that fault-tolerant quantum computers need, and because simulating it exactly is expensive, the community has benchmarked it using a Clifford stand-in circuit. Those benchmarks were systematically too optimistic: the real protocol suppresses errors less strongly than intended, and the gap widens as hardware noise improves. This work identifies the culprit — errors that stop being simple bit- or phase-flips once they pass through the non-Clifford gates, and therefore slip past postselection — and shows that a handful of extra check qubits recovers the intended error suppression. Beyond fixing the protocol, it is a cautionary tale about validating non-Clifford circuits with Clifford proxies, and a template for reasoning about coherent error propagation.

**Key contributions**
- Analytic diagnosis of the long-standing T–S discrepancy; fault distance shown to be exactly 2 and 3 for MSC-3 and MSC-5 double checks (exhaustive enumeration, not sampling).
- A general theorem for the trivial-syndrome (acceptance) probability of any mixed logical state in any Pauli stabiliser code hit by any Clifford error: zero if the transformed group contains a negated stabiliser, else 2⁻ˢ times a signed sum of Pauli coefficients, with s = rk⟨G ∪ E†GE⟩ − (n−k).
- An O(n³ + N_α k²) algorithm evaluating this via tableau composition and an explicit F₂ phase form χ(u); a corollary recovering stabiliser-state fidelity 2⁻ˢ.
- An O(n) fidelity criterion for T states in hexagonal colour codes: fidelity is 1 or 0 according to whether the Clifford error commutes with the transversal logical H₊.
- Concrete Z-flagged distance-3 (2 flags) and distance-5 (13 flags) double checks with fault distance 3 and 5, validated by SymFT Monte Carlo (fitted slopes 3.8 → 5.1).
- Note that the original MSC circuit measures the logical H₋ representative, and that varying ancilla count cannot fix the distance.

**How it works** — Faults are tracked as (detector signature, residual effect) pairs so residual Paulis can be propagated through the T layer, yielding coherent errors; the acceptance/fidelity results then convert each malignant configuration into an exact contribution to the post-selected logical error rate. Flags were designed to catch the four malignant 2-fault X-hook configurations at d=3, and at d=5 by placing Z flags along the GHZ (un)encoding tree (leaf flags pruned, flag lifetimes minimised) since 601+3 sub-distance-5 malignant configurations preclude case-by-case design.

**Why it matters** — Resource estimates built on Clifford-proxy cultivation benchmarks are optimistic and should be revisited; the fix is cheap in qubits and rejection overhead, and the acceptance-probability machinery is reusable for any postselected non-Clifford gadget.

**Caveats** — The flagged circuits are 2D-local but not nearest-neighbour (existing gates become next-nearest-neighbour), so they are explicitly a proof of concept rather than a hardware-ready layout. Simulations stop before the escape stage; end-to-end relevance relies on a high decoder-confidence threshold regime. At d=3 the flags are essentially break-even. Analysis assumes circuit-level depolarising noise and noiseless stabiliser readout in the theory sections.

## 3. Query-Optimal and Gate-Efficient Lindbladian Simulation

[arXiv:2609.18757](https://arxiv.org/abs/2609.18757) · [SciRate](https://scirate.com/arxiv/2609.18757)

*Boyang Chen, Minbo Gao, Xinzhao Wang, Shuo Zhou*

**TL;DR** The authors give a Lindbladian simulation algorithm whose query complexity, O(τ + log(1/ε)/log(e + log(1/ε)/τ)) with τ = (α_H + α_B²)t, is *additive* in evolution time and precision, matching the known optimal Hamiltonian-simulation lower bound (recovered by setting the jump operators to zero). Gate count is linear in the query count up to polylog factors and only logarithmic in the number of jump operators, and the result extends to Lipschitz time-dependent Lindbladians.

**The big picture** Simulating open quantum systems — dissipation, decoherence, thermalization — has long cost more than simulating closed-system dynamics: previous general-purpose algorithms paid a multiplicative penalty, so that higher accuracy made the whole time-evolution cost grow. This work shows that dissipative Markovian dynamics is, asymptotically, no harder to simulate than unitary dynamics in the black-box access model: the cost of accuracy simply adds to the cost of time, which is provably the best possible. Beyond closing this theoretical gap, the algorithm is also cheap in elementary gates, so it plugs directly into ground-state preparation, Gibbs-state preparation, and differential-equation solvers built on dissipative evolution, improving their complexities.

**Key contributions**
- First general Lindbladian simulator with additive time/precision query scaling, improving on Li–Wang's O(τ log(τ/ε)/log log(τ/ε)) and removing structural assumptions (e.g. ΣL†L ∝ I) used in prior additive-scaling results.
- A one-query "Cayley-type" transducer for a rational CPTP step, obtained by replacing iH with K = iH + B†B/2 in the Hamiltonian Cayley transducer, with the U_B and U_B† oracle branches supplying jump output and dissipator.
- A catalyst-removal analysis: an annihilating polynomial p(ζ)=ζ²(1+ζ²) for the δ→0 private block, plus monotonicity of the step-index register and orthogonality of distinct Kraus-label strings, yields ‖F_q(S₁₁)‖ ≤ (C₀τ/q)^q, independent of the number of Trotter-like steps J.
- A gate-efficient implementation: compressed Kraus-label storage (positions/values of only O(q) nonzero labels, since each transducer call changes at most one label) combined with interval-wise rotation factorization; Õ(q) gates versus Õ(mq³/ε) in concurrent work.
- Downstream improvements for semi-dissipative linear ODEs, detailed-balance Gibbs sampling, and Lindbladian ground-state preparation.

**How it works** One step of length δ is replaced by an exactly CPTP Padé/resolvent channel with Kraus operators N_δ = (I−δK/2)R_δ and √δ L_k R_δ, incurring diamond error 10τ²/J. J such Stinespring isometries are composed into a single one-query transducer via sequential composition; running the reuse circuit with a zero private input instead of the catalyst gives W_J − P_N = S₀₁g_N(S₁₁)Γ, and an LCU over reuse lengths N ≤ 20q with ℓ₁ norm exactly 2 kills the error to (C₀τ/q)^q√τ. Oblivious amplitude amplification for isometries then uses ≤60q queries.

**Why it matters** It settles the joint time–precision query complexity of general Lindbladian simulation and makes the transducer framework a practical, gate-efficient primitive for open-system algorithms.

**Caveats** Optimality is established only against the Hamiltonian lower bound (B = 0); no lower bound justifies the α_B² normalization, so whether dissipative strength must enter quadratically is open. The model requires a Hermitian block encoding of H and a projected unitary encoding of the *stacked* jump operator. J must be Ω(τ²/ε), which enters gate counts polylogarithmically, and gate complexity carries an ℓ_ε² factor. The stated m-dependence in the main theorem (logarithmic) sits somewhat awkwardly with the Õ(mq) claim in the related-work comparison.

## 4. Logarithmic-depth quantum simulation of boson sampling

[arXiv:2609.18907](https://arxiv.org/abs/2609.18907) · [SciRate](https://scirate.com/arxiv/2609.18907)

*Changhun Oh*

**TL;DR** Boson sampling with an arbitrary $m$-mode interferometer and $n\le m$ single photons can be sampled to total-variation error $\epsilon$ by a Clifford+$T$ qubit circuit of depth $O(\log(m/\epsilon))$ and polynomial width (arbitrarily close to $m^2$ qubits for fixed inverse-polynomial accuracy), with arbitrary connectivity and a single terminal measurement. The construction dilates the interferometer to $4m$ modes where it factors *exactly* into six quadratic shears, then dilutes each mode over $K$ submodes so that a constant local Fock cutoff ($s=1$, i.e. one qubit per submode) suffices. Consequently boson sampling sits inside $\mathsf{QNC}^1$-type shallow quantum computation, and associated promise decision problems land in $\mathsf{BQNC}^1$.

**The big picture** Boson sampling is the flagship proposal for quantum advantage with photons, and its optical circuits are deep — many sequential layers of beam splitters. It has been unclear how much *sequential* quantum processing is really needed to reproduce its output statistics on a qubit machine. This work shows that a polynomial number of qubits buys enough parallelism to compress the whole task into only logarithmically many gate layers, so the believed classical hardness of boson sampling coexists with an extremely shallow qubit implementation. That places a concrete upper bound on the quantum complexity of a model widely used to argue for quantum advantage, without weakening the hardness conjectures themselves.

**Key contributions**
- Exact six-shear dilation: embedding $U=X+iY$ into a real orthogonal $O_U$, then into $R_U=\begin{psmallmatrix}0&O_U^{\mathsf T}\\O_U&0\end{psmallmatrix}$, a real symmetric involution with zero diagonal and unit norm; three shears realize $e^{-i\pi R_U/2}=-iR_U$, three more the fixed input encoder.
- A mode-dilution argument with a rigorous dynamical truncation bound $\|\Psi_{\rm tr}-\Psi_{\rm id}\|\le C_s(n+4m+2s+8)^{(s+3)/2}K^{-s/2}$, covering photons transiently created by individual (non-passive) shears, not just output leakage.
- Log-depth parallel compilation of each truncated shear, and a $\mathsf{BQNC}^1$ upper bound for $\mathsf{NC}^1$-recognizable output events with constant promise gap.

**How it works** Zero diagonals in all six shear coefficient matrices make local truncation *exactly* the compressed Hamiltonian $\hat P\hat H\hat P$, so no diagonal self-terms are corrupted. Uniform $K$-port splitters are conjugated through each shear (coupling $A_{ij}/K$), diluting occupation; a Duhamel argument reduces the error to weighted leakage along the ideal trajectory. Each truncated shear is diagonalized by a *fixed*, $U$-independent local basis change $\mathcal W_s$; the resulting phase depends only on eigenvalue-label histograms, computed by carry-save arithmetic in $O(\log K)$ depth and applied via Moore–Nilsson CNOT-tree fanout. With $s=1$, $K=O(m^4\epsilon^{-2})$, $b_A=O(\log(mK/\epsilon))$, and KMM synthesis at $\delta=\epsilon/3G_{\rm rot}$, depth stays logarithmic since synthesis cost is paid once per parallel stage. $U$ enters only as input bits — no instance-dependent decomposition — giving logspace uniformity.

**Why it matters** Anyone reasoning about quantum advantage hierarchies, the (non)universality of linear optics, or bosonic-to-qubit encodings should note that optical depth and simulation depth are decoupled. It also gives a clean, uniform recipe for compiling passive interferometers into shallow qubit circuits.

**Caveats** Arbitrary connectivity and CNOT-tree fanout are essential; geometric locality would add depth. Width is generous in the base case ($O(mK)\sim m^5\epsilon^{-2}$ at $s=1$); the near-quadratic corollary needs $s>(3+2c)/(\alpha-2)$ with constants hidden in $O(\cdot)$ growing with $s$. Only single-photon Fock inputs are treated (not Gaussian boson sampling), approximation is inverse-polynomial rather than exact, and no separation from universal quantum computation or lower bound on depth is established.

## 5. Continuous variable distributed quantum sensing in integrated photonics

[arXiv:2609.19092](https://arxiv.org/abs/2609.19092) · [SciRate](https://scirate.com/arxiv/2609.19092)

*Bethany Puzio, Oliver M. Green, Joel F. Tasker, Jonathan Frazer, Tamzin Ellis, Benjamin D. J. Sayers, Rachel N. Clark, Alex S. Clark et al.*

*Summary unavailable (Error code: 500 - {'type': 'error', 'error': {'type': 'api_error', 'message': 'Internal server error'}, 'request_id': 'req_011Cf97EriuqeZTTTdN1iAw8'}).*

Distributed quantum sensing is an emerging application of quantum networking, where entangled probe states are employed to sense combinations of delocalized parameters with enhanced precision relative to using separable states. Squeezed states of light are a prime resource for experimental demonstrations of entanglement-enhanced sensing, because they can be generated and entangled deterministically. Existing distributed quantum sensing experiments have been fundamentally limited in scalability due to their bulk-optic architectures. Meanwhile, integrated photonics provides a scalable and compact platform for quantum sensors. Here we demonstrate entanglement-enhanced sensing of linear functions of four phase shifts in an integrated photonic circuit. We find an entanglement-enhanced precision of 0.199(16) dB below the shot noise limit compared to 0.041(18) dB for separable states. A four-mode entangled state is generated on-chip with entanglement verification and phase sensing also performed on-chip with an array of four integrated homodyne detectors.
