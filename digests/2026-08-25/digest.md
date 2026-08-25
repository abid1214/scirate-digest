# SciRate Daily Digest — 2026-08-25

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Universal equilibrium magic in quantum many-body systems

[arXiv:2608.22939](https://arxiv.org/abs/2608.22939) · [SciRate](https://scirate.com/arxiv/2608.22939)

*Soumyadeep Sarma, Tobias Haug, John Preskill, Wai-Keong Mok*

**TL;DR** The authors show that the nonstabilizerness (magic) of equilibrium pure states of chaotic many-body Hamiltonians — both mid-to-off-center energy eigenstates and late-time states from product initial conditions — is quantitatively reproduced by the *thermal Scrooge ensemble* built from the Gibbs state at the matching effective inverse temperature. This yields a closed prediction for stabilizer Rényi entropies: an infinite-temperature "Haar" plateau at $\widetilde M_\alpha \approx N$, and for $\beta\neq 0$ a thermal regime with $\widetilde M_\alpha \approx \widetilde M_\alpha(\sigma_\beta)$, giving magic density $(\alpha-1)^{-1}(1 - c_\alpha\beta^{2\alpha}+\dots)$ — so for $\alpha>2$ the fSRE density is *discontinuous* at $\beta=0$ in the thermodynamic limit.

**The big picture** Thermalization is usually a statement about local observables, while the "magic" that makes a quantum state hard to simulate classically is a global property of the whole wavefunction. This work argues that magic nevertheless becomes a thermodynamic quantity: for chaotic systems whose only conserved quantity is energy, the amount of magic in a typical equilibrium state depends on nothing but temperature, not on the initial state or microscopic details. The bridge is a "minimally informative" ensemble of pure states consistent with the thermal state, which appears to describe entanglement and magic alike — hinting at a single statistical framework for many-body quantum resources.

**Key contributions**
- Identification of the thermal Scrooge ensemble as the universal descriptor of the full Pauli spectrum (not just low-weight observables) of equilibrium pure states.
- Analytic two-regime formula for the Scrooge-averaged fSRE, with crossover $\beta_c \sim N^{-1/2\alpha} 2^{-N(\alpha-2)/2\alpha}$, i.e. exponentially shrinking Haar window for $\alpha>2$.
- High-temperature cluster expansion: $\ln\zeta_\alpha(\sigma_\beta)=\beta^{2\alpha}\sum_P|a_P|^{2\alpha}+O(N\beta^{2\alpha+1})$, so the leading correction is set by $c_\alpha$, the $2\alpha$-th moment of the Hamiltonian's Pauli coefficients — invisible to free energy (which sees $c_1$).
- Argument that high-temperature equilibrium states carry long-range magic and entanglement: local depth-$t$ circuits change $c_\alpha$ by at most $O(t^{d(\alpha-1)})$.
- Numerics: MFIM, $N\le 18$ (POLFED eigenstates, $Jt=200$ evolved product states, Chebyshev-sampled Scrooge states, HadaMAG for SREs), plus tensor-network Gibbs IPR up to $N=320$.

**How it works** Magic is read off the Pauli spectrum via $\zeta_\alpha=\sum_P|\mathrm{Tr}(P\rho)|^{2\alpha}$. Averaging over an unnormalized deformed-Haar approximation to Scrooge($\sigma_\beta$) gives a sum over $S_{2\alpha}$ permutation cycles in $t_m(P)=\mathrm{Tr}[(P\sigma_\beta)^m]$; careful case analysis on cycle type shows all non-identity permutations are suppressed by $D^{-1}e^{O(N\beta^2)}$ for $\alpha\ge3$ ($d_2=4$ because $k_1=0$ terms survive at $\alpha=2$). The puzzle of why a *canonical* ensemble captures a global quantity is resolved by locality: $\ln\zeta_\alpha$ is dominated by connected clusters of Hamiltonian Pauli terms of size set by the thermal correlation length, hence governed by subsystem ETH. Supplementary numerics confirm low-weight Paulis are thermal while high-weight ones remain Gaussian, and Lévy's lemma for GAP measures gives self-averaging of the *linearized* SRE (Lipschitz constant $\le 4\alpha$, $\|\sigma_\beta\|$ exponentially small).

**Why it matters** Provides a temperature-only prediction for a resource-theoretic quantity relevant to classical simulability, connects magic to thermodynamics in the same way entanglement entropy connects to thermal entropy, and supplies a diagnostic (deviation from Scrooge) for nonergodicity such as quantum many-body scars.

**Caveats** The Scrooge average is annealed, not quenched; self-averaging is proven only for the linearized SRE and shown numerically for fSRE. The deformed-Haar approximation requires low-purity $\sigma_\beta$, restricting rigor to sufficiently high temperature; the theory is expected to fail near thermal critical points and for nonlocal (e.g. GUE) Hamiltonians. The claimed $\alpha>2$ discontinuity cannot be verified directly at accessible $N$ — Fig. 4 uses an interpolating ansatz for $\zeta_\alpha$ rather than exact states. Convergence of the linked-cluster expansion uniformly in $N$ is assumed, not proven, and extensions to additional conserved charges or integrable (GGE) cases remain conjectural.

## 2. Satisfying Quantum Codes: Physics-Informed and Hardware-Aware Code Design with SAT Solvers

[arXiv:2608.23460](https://arxiv.org/abs/2608.23460) · [SciRate](https://scirate.com/arxiv/2608.23460)

*Ben DalFavero, William M. Watkins, Margarite L. LaBorde, Vincent Russo, Ethan Egger, Gregory Quiroz, Ryan LaRose*

**TL;DR** — The authors encode quantum stabilizer-code design (commutativity, error detection/correction via Knill–Laflamme, code extension from a fixed initial stabilizer set) as a Boolean satisfiability formula in CNF, prove the underlying decision problem is NP-complete by reduction from *k*-set cover, and then show off-the-shelf SAT solvers handle practically relevant instances — e.g. a $[\![100,50,4]\!]$ code in under five minutes of laptop CPU time, versus ~an hour for a recent multi-agent method. Applications include codes built on Fermi–Hubbard symmetries at 100 qubits and biased-noise surface-code variants with lower logical error rate than XZZX under maximum-likelihood decoding.

**The big picture** — Quantum error-correcting codes are still largely designed by hand, using mathematical elegance rather than the specific noise or connectivity of a given device or the symmetries of a given physics problem. This work recasts code design as a logical constraint-satisfaction problem, so that decades of engineering in industrial satisfiability solvers can be pointed at it directly. That makes it routine to grow an existing code, to build a code around conserved quantities of a target Hamiltonian, or to tailor one to asymmetric hardware noise — and the resulting tailored codes beat the best hand-designed biased-noise codes in simulation.

**Key contributions**
- First complexity-theoretic proof that quantum code *design* (not distance-finding) is NP-complete, via a reduction *into* code design from set cover — closing a gap where prior work only mapped code design onto NP-hard problems.
- A formal definition of *quantum code extension* (with/without "mutation" of boundary checks), a proof that distance-increasing extensions always exist (via concatenation, $m \le n(n-1)$), and a proof that bivariate-bicycle codes admit extensions without mutation.
- A complete CNF encoding covering commutativity, syndrome-nonzero-or-stabilizer detection (with slack variables for group membership), and pairwise Knill–Laflamme correction conditions; unified for discovery and extension.
- Empirical SAT–UNSAT phase transition in random code-design instances with order parameter = errors per stabilizer, plus a distance-3 phase diagram sitting between Gilbert–Varshamov and Singleton bounds — giving an empirical existence predictor in the contested region.
- Concrete new codes: bias-tailored Fermi–Hubbard codes with reduced undetected-error rates, and biased-noise surface codes outperforming XZZX.

**How it works** — Stabilizers are binary symplectic vectors; unknown check-matrix entries become Boolean variables. Commutation is the symplectic inner product (XOR clauses); detectability of error $\epsilon_j$ is $\bigvee_i \langle u_i,\epsilon_j\rangle$ OR'd with a slack-variable group-membership formula; correction replaces $\epsilon_i$ with $\epsilon_i\oplus\epsilon_j$ over all error pairs. Physics-informed design seeds the initial stabilizer set with Hamiltonian symmetries; hardware-aware design shapes the error set $\mathcal{E}$.

**Why it matters** — Relevant to anyone building codes for real devices with structured/biased noise or restricted connectivity, and to the QEC-automation community (RL-, game-theoretic-, and SAT-based searches), which now has both a hardness baseline and a substantially faster, more general tool.

**Caveats** — Memory scales as $\sum_{w<d} 3^w\binom{n+m}{w}$, so only low-distance codes or few added errors are tractable; the correction encoding is quadratic in $|\mathcal{E}|$. NP-completeness means worst-case blowup remains. Encoded rate/distance guarantees are only as good as the enumerated error set, and the reported advantage over XZZX is simulation-based under a specific ML decoder; circuit-level noise and decodability/syndrome-extraction cost of the discovered codes aren't visible in the available source.

## 3. Taming Spacetime Overhead and Design Complexity in Distributed Fault-Tolerant Superconducting Quantum Computation

[arXiv:2608.23159](https://arxiv.org/abs/2608.23159) · [SciRate](https://scirate.com/arxiv/2608.23159)

*Qinjing Yu, Ke Liu*

**TL;DR** The authors co-design a surface-code interface protocol that hides slow inter-chip operations behind a buffer-qubit layer, plus an end-to-end resource-estimation pipeline for modular superconducting FTQC. For RSA-2048 at intra-chip error 10⁻³, inter-chip error 10⁻², and inter-chip gates up to 25× slower, the distributed machine needs ~2.0M physical qubits and 4.4 days versus 1.26M / 3.4 days monolithic (d = 27 → 31), and this overhead is essentially independent of chip capacity from ~2.4k to ~170k qubits per module.

**The big picture** Building a useful error-corrected superconducting computer will almost certainly require wiring together many modest chips, but the links between chips are both noisier and slower than on-chip gates, raising the worry that modularity multiplies the cost or forces the whole machine to run on a slow, awkwardly synchronized clock. This work shows that if the extra latency and noise are absorbed by dedicated hardware right at the chip seams, the penalty stays local: the total qubit count and runtime rise only modestly and, crucially, barely depend on how big the individual chips are. That converts chip size from a delicate architectural parameter into an engineering choice that can be made on fabrication-yield, packaging, and wiring grounds.

**Key contributions**
- A "latency-decoupled" inter-chip syndrome-extraction circuit: a distance-preserving seam (2d−1 interface ancillas, unevenly split data qubits) plus a buffer layer of 4d−2 qubits that pre-generates Bell pairs concurrently with the intra-chip cycle, followed by one SWAP layer.
- A three-layer resource-estimation protocol (inputs → per-zone chip/code scan → aggregation) that separates computation and memory zones and treats interface noise as a distinct channel.
- Extension of the three-term interface/bulk/mixed logical-error ansatz to yoked surface codes with seams, with interface error amortized over inner patches.
- Quantitative demonstration of near scale-invariant spacetime overhead across two decades of module capacity and two physical error regimes (10⁻³ and 10⁻⁴).

**How it works** Inter-chip operations are confined to buffer qubits, so the seam cycle costs 1120 ns instead of 1000 ns regardless of η (vs. latency-dependent circuits, whose runtime grows roughly linearly with η, reaching 21.2 h/shot at η = 25 vs. 11.2 h). Because the interface cycle time is η-independent, seam patches don't form a slow clock domain, eliminating synchronization machinery; the stabilizer group is unchanged, so decoding complexity is unaffected. Circuit-level Stim-style simulations under a modified SI1000 model (interface gates at p_s, extra idle error η·p_b/10 during the SWAP layer) on d×2d patches with a central seam fix the ansatz constants; these feed a grid scan over (h, w, d) per chip against the Gidney RSA-2048 workload (1.1×10⁷ additions, 7.6×10⁶ lookups, 1.6×10⁶ phaseups, 131 active + 1280 idle logical qubits, 6 cultivation factories), with yoked codes optimized for memory code rate.

**Why it matters** It gives modular-hardware roadmaps a defensible cost target and shows that logical-level compilation tools built for monolithic surface codes largely transfer. Relevant to superconducting architects, FTQC compilers, and anyone estimating cryptographically relevant timelines.

**Caveats** Bell-pair generation is assumed to complete within one QEC cycle with fixed depolarizing error — no heralding, purification, or link-failure/rate modeling; γ = 10 and η ≤ 25 are stipulated. Error accounting conservatively assumes all seams are always active, but 12–38% of allocated qubits are unused slack, so both directions of bias exist. Only square, uniform chip geometries are scanned; the p_b = 10⁻⁴ memory numbers are extrapolated rather than simulated. Real-time decoding bandwidth, cryogenic wiring, and inter-module routing topology — the very constraints motivating modularity — are not costed, and qLDPC alternatives are explicitly excluded rather than compared.

## 4. Efficient Computation of QKD Key Rates without Semidefinite Programming

[arXiv:2608.23285](https://arxiv.org/abs/2608.23285) · [SciRate](https://scirate.com/arxiv/2608.23285)

*Bence Temesi, Antoine Gansel, Gereon Koßmann, Rene Schwonnek*

**TL;DR** The authors replace semidefinite programming in QKD key-rate computation with an iterative "candidate-and-certificate" scheme whose only expensive primitive is diagonalization of a d×d effective Hamiltonian. Each outer step is a Gibbs-state (information) projection onto the affine constraint set, solved by damped Newton in the n Lagrange multipliers; the certified lower bound is a single smallest-eigenvalue evaluation. Memory drops from O(d⁴)–O(d⁶) to O(d²), enabling real-time key-rate estimation on a Raspberry Pi 3 with runtimes orders of magnitude below workstation SDP/entropy-cone benchmarks.

**The big picture** Certifying that a quantum key distribution device really produces secret bits requires turning noisy measurement data into a rigorous lower bound on how little an eavesdropper knows — a hard convex optimization over quantum states that today needs heavy conic solvers on workstations. This work shows the optimization has a hidden thermodynamic structure: the optimal states at each step are equilibrium (Gibbs-like) states determined by only as many real parameters as there are measured constraints, so the whole computation collapses to repeated matrix diagonalizations plus a lowest-eigenvalue check. Because the resulting algorithm is tiny, fast, and produces a self-checking rigorous bound, security analysis can move from offline lookup tables to live, on-device computation inside embedded QKD hardware. That opens the door to adaptive protocol tuning against the certified rate itself, rather than against analytic approximations.

**Key contributions**
- Reformulation of the QKD relative-entropy minimization as an alternating scheme: linearize the objective at the current state, then perform an exact information (Gibbs) projection onto the affine feasible set, reducing the matrix-valued step to an unconstrained convex problem in n multipliers with analytic gradient (moment mismatch) and Hessian (BKM/Bogoliubov–Kubo–Mori covariance).
- SDP-free outer certificate: F* ≥ λ_min(G_σ + α·M) − α·m for any α, reusing the Gibbs multipliers; tight at a positive-definite optimizer (recovers Winick-type KKT conditions).
- Convergence theory: monotone descent, global O(1/k) rate with constant D(ρ*||ρ₀) ≤ −log λ_min(ρ₀); local geometric contraction θ^k in state and θ^{2k} in objective; interior-selection result when the optimizer set contains a full-rank state.
- Careful support compression of the pinching/preprocessing channels so all matrix logarithms are well defined, plus a Naimark block form for DM-CV protocols.
- Implementations: <100 lines of Common Lisp; Python (laptop) and Julia (Pi) versions; rational-arithmetic verification of the final certificate.

**How it works** Effective Hamiltonian H = log χ_σ − λ·M with χ_σ = e^{log σ − ∇F(σ)}/Z; minimizing g(λ) = log Z(λ) + λ·m enforces exactly tr(ρM_i) = m_i, so the projected state is automatically feasible and positive definite. One Newton step = one d×d eigendecomposition (reused for the Hessian) plus an n×n solve, giving O(d²) memory and O(d³) runtime per iteration.

**Why it matters** Benchmarks on the DM-CV QPSK, MUB, and overlapping-basis instances of González Lorente et al. reach ε_num ≤ 10⁻⁵–10⁻⁶ nats; a 16-QAM DM-CV run at d = 144/176 with 319 constraints is laptop-feasible in under four minutes per point and hints that 16-QAM beats QPSK and known analytic bounds. Relevant to QKD implementers, security-proof numerics developers, and anyone doing conic entropy optimization.

**Caveats** Restricted to trace-preserving maps — post-selection/trace-nonincreasing protocols are left to future work. The convergence analysis assumes exact inner solves; the paper explicitly notes that finite inner iterations break exact feasibility and that a feasibility correction plus inexact-outer analysis is still needed. Benchmark comparisons use different hardware, languages, and precision criteria, so they are not hardware-normalized speedups. The 16-QAM results use a hard photon-number cutoff without rigorous dimension-reduction correction. Rényi-entropy finite-size extension is only asserted, not demonstrated.

## 5. Sample-Query Interconversion of Block Encoding of Unknown Quantum States

[arXiv:2608.22470](https://arxiv.org/abs/2608.22470) · [SciRate](https://scirate.com/arxiv/2608.22470)

*Manaki Arihara, Mio Murao*

**TL;DR** The paper pins down the two-way cost of translating between sample access to an unknown state and query access to a unitary that block-encodes its density matrix. Implementing a single ε-accurate use of the block-encoding channel (and its inverse) provably needs Ω(1/ε) copies, matching the known Õ(1/ε) density-matrix-exponentiation + QSVT construction; conversely, recovering a rank-r, d-dimensional state from its block encoding needs Ω((α/λ_max)√(d/r)) queries — Ω(α√d) even for pure states, Ω(α√(rd)) worst case — with matching algorithms for (nearly) flat spectra.

**The big picture** Many modern quantum algorithms assume the input matrix is handed to you as a sub-block of a unitary, and a natural hope is that unknown quantum states supplied as physical copies can be freely turned into such black-box unitaries and back again, so that generic matrix-transformation machinery can be used for learning. This work shows the two resources are not interchangeable: turning copies into an accurate black-box unitary carries an unavoidable accuracy-dependent overhead, and going the other way — regenerating the physical state from the black box — carries a cost that grows with the dimension, exponentially in the number of qubits in the worst case. That establishes a genuine separation between learning properties of a state and being able to produce the state itself, and the same argument yields new lower bounds for two workhorse tasks, ground-state and thermal-state preparation.

**Key contributions**
- Ω(1/ε) copy lower bound for one-shot ε-accurate simulation of the block-encoding unitary channel and its inverse (α = Θ(1)), a regime not covered by prior Ω(Q²/ε) multi-query bounds.
- Ω((α/λ_max(ρ))√(d/r)) query lower bound for state recovery from block-encoding access, formulated over the fully general quantum-comb strategy space (arbitrary interleaving, forward and inverse queries).
- Matching O(α√(rd)) algorithm for rank-r projector states, and O((α/λ_max)√(d/r)) for spectra with condition number κ ∈ [1,2) (error ≤ κ−1), beating the Θ(d³/ε) tomography-based route.
- Joint Ω(1/(γΔ)) lower bound for ground-state preparation (previous bounds were only Ω(1/γ) or Ω(1/Δ) separately) and Ω̃(β√d) for Gibbs preparation at β ≳ log d — a *product* dependence, not just separate obstructions.

**How it works** The sample bound reduces to distinguishing diag(1/2±δ): a block encoding of ρ± is also one of the scalar 1/2±δ, and QSVT with a difference of two shifted sign-function polynomials (a "bump" of degree O(α/δ)) separates them in O(1/δ) queries; since discrimination needs Ω(1/δ²) copies (Pinsker + Helstrom), each channel use must cost Ω(1/ε) copies. The query bound reduces to unstructured search: a phase oracle with phases arcsin(λ_x/α) on a marked set S yields, via O(1) queries, a block encoding of ρ_S = Σ λ_x|x⟩⟨x|; measuring a recovered ρ̂ in the computational basis finds a marked element, so BBBV/Grover-type bounds transfer. Upper bounds apply the block encoding to half of a maximally entangled state and amplitude-amplify onto the ancilla-zero subspace, producing ρ²/Tr ρ² (exactly ρ for projectors).

**Why it matters** It delimits when QSVT-style "black-box" pipelines can be used for quantum learning, and warns that block encoding is not a free surrogate for state access. Relevant to anyone designing sample-to-query conversions, ground-state/Gibbs-state preparation algorithms, or claiming end-to-end speedups from block-encoded inputs.

**Caveats** Lower bounds are stated for α = Θ(1) and are worst-case; no matching upper bound is known for general (non-flat) spectra — the gap versus √ρ-based canonical purification constructions is explicitly open. The near-flat-spectrum algorithm only achieves error ≥ κ−1, so it does not give arbitrary accuracy. The hard instances for ground/Gibbs preparation are diagonal marked Hamiltonians with a specific overlap γ = 1/√d, and the Gibbs bound holds only for β ≥ log d. The tomography comparison uses the loose ‖X‖₁ ≤ d‖X‖_∞ bound, so the claimed advantage margin may be pessimistic for the baseline.
