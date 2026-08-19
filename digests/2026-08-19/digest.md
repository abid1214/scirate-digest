# SciRate Daily Digest — 2026-08-19

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Ultrafast and high resolution spatial light modulation for cold atoms

[arXiv:2608.18071](https://arxiv.org/abs/2608.18071) · [SciRate](https://scirate.com/arxiv/2608.18071)

*Alexander Dennisovich Deters, Yanfei Li, Alexander Douglas, Markus Greiner, Aaron W. Young*

**TL;DR** — A "dispersive spatial light modulator" (dSLM) maps RF/optical frequency to 2D position by cascading a virtually imaged phased array (VIPA, fine resolution/small FSR) with a diffraction grating (coarse resolution/large FSR), so that fast telecom-style amplitude modulation becomes arbitrary 2D intensity patterning. The demonstrated device reaches ~12 ns rise time (>84 MFPS), 83×52 resolvable waists across the field of view (11×52 through a single 40 GHz Mach-Zehnder modulator), and 10⁻³ intensity homogeneity — orders of magnitude faster than DMD/LCOS and unconstrained by the outer-product limitation of crossed AODs.

**Key contributions**
- VIPA+grating architecture that converts >10 THz of available telecom bandwidth into 2D spatial resolution; static LCOS correction of VIPA polishing aberrations recovers diffraction-limited PSFs across the whole band (aberrations are nearly frequency-independent).
- Measured 10–90% rise/fall (single-pixel camera, 233 MHz detection chain, ~0.1 ns overestimate), continuous 2D motion: chirping within a VIPA FSR (y) and amplitude hand-off between tones spaced by one FSR (x), with resolution essentially preserved up to ~100 waists/µs.
- Arbitrary permutation/braiding of 5 spots in ~1.2 µs; argued sublinear-time arbitrary 2D permutations, enabling qLDPC codes incompatible with AOD routing.
- Adjacent spots are separated by ≥50 MHz (y) or ≥1 FSR (x), so interference time-averages away on atomic timescales → 10⁻³-level relative intensity control (three tones, RFSoC 14-bit drive).
- A concrete, numerically validated scheme for fully programmable square-lattice Hubbard models: base tweezers set μᵢ, interlaced barrier tweezers at ~1w₀ set t_ij, curvature tweezers at ~0.6w₀ set Uᵢ, optimized jointly; per-link Floquet drive phases (demonstrated for 4 spots with Δφ=π/5, π/2) generate arbitrary plaquette flux patterns.
- Scaling study: 15 mm air-gap, 60 cm VIPA with 4 nm RMS surface error (10 mm correlation length) + 10 GHz grating gives >1000×1000 waists; telecom modulator arrays + EDFA/TDFA sum-frequency generation to ~850 nm for Rb.
- Trick: a π phase jump extinguishes a spot faster than the VIPA transit time.

**Why it matters** — Speed is the binding constraint for Floquet engineering, local flux, quench protocols, and high-rate fault-tolerant routing. This decouples pattern complexity from modulator pixel count, replacing mechanical/liquid-crystal displays with mature, high-power, high-linearity RF-photonic hardware.

**Caveats** — No atoms yet; all results are optical bench characterization. Figures rely on post-processing equivalent to future optics: stitching FSRs/laser detunings, cropping carrier and negative sidebands (single-sideband modulation not available), and y-stretching for ellipticity. Throughput is only 5.8% (claimed >50% with custom optics). Sinc² PSF tails and finite MZM extinction force spot staggering and cap homogenization near 10⁻³ for only three tones; scaling homogeneity requires very linear, high-dynamic-range wideband RF. Modulation amplitude rolls off by ~50 MHz. The dispersion model is linear/orthogonal and will need nonlinear treatment at megapixel scale; x-axis moves incur intrinsic waist broadening √(1+d²/w₀²).

## 2. Nearly Sample-Optimal Estimators for Quantum Rényi and Tsallis Entropies

[arXiv:2608.18070](https://arxiv.org/abs/2608.18070) · [SciRate](https://scirate.com/arxiv/2608.18070)

*Kean Chen, Qisheng Wang*

**TL;DR** Two new estimators close the remaining sample-complexity gaps for quantum Rényi entropy at all non-integer orders and Tsallis entropy for α<1, matching Wang's recent lower bounds up to polylogs. For 0<α<1 the cost is O(d^{1+1/α}/ε^{1/α} + …), a large improvement over the previous O(d^{2/α}/ε^{2/α}); for non-integer α>1 the Rényi cost drops from O(d²/ε²) to O(d²/ε^{1/α} + d^{1-1/α}/ε²).

**Key contributions**
- Nearly optimal sample complexities: 0<α<1 — O(d^{1+1/α}/ε^{1/α} + d^{1/α-1}/ε²) (Rényi), O(d^{1+1/α}/ε^{1/α} + d^{2-2α}/ε²) (Tsallis); both collapse to O(d^{1+1/α}/ε^{1/α}) for α≤1/2. Non-integer α>1 Rényi: O(d²/ε^{1/α} + d^{1-1/α}/ε²).
- A new operator inequality: for σ ⪰ (d/n)I, 0 ≤ (1-α)tr(σ^α) + α tr(ρσ^{α-1}) − tr(ρ^α) ≤ (d/n)^{α-1} D_{χ²}(ρ‖σ) — a Bures χ²-controlled first-order (concavity) bias bound for tr(ρ^α).
- Shows the regularized tomography estimate σ = ρ̂ + (2d/n)I from Bures-χ² tomography achieves D_{χ²}(ρ‖σ) = O(d²/n).
- A Richardson-extrapolation analysis of Hayashi's covariant pure-state POVM combined with random purification, cancelling the leading bias moments of a Beta distribution.
- Methodological departure: both estimators avoid weak Schur sampling, the standard tool in prior work.

**How it works** For α<1: run Bures-χ² tomography (Pelecanos et al.) with n samples, regularize to σ, then compute the "linearized" surrogate (1-α)tr(σ^α) + α tr(ρσ^{α-1}); the first term is classical, the second is estimated by measuring ρ in σ's eigenbasis m times (X = s_J^{α-1}). Bias is controlled by the new inequality (O(d^{α+1}/n^α)), and variance by careful moment bounds on E[X²] (three regimes: O(d(d/n)^{2α-1}), O(d^{2-2α}), and a relative bound O(d^{1/α-1}F²)), then Chebyshev.

For α>1: random purification turns ρ^{⊗s} into copies of a Haar-random purification |ψ⟩; Hayashi's covariant POVM outputs |v⟩ whose coefficient matrix is √(1-T)M + √T G with T~Beta(d²-1,s+1) and G isotropic on M^⊥. The one-batch statistic Y_s = tr(ρ̂^α) has bias expandable as Σ_j c_j μ_j(s) + R(s) with |R(s)| = O(F(d²/s)^α), using a Schatten-norm Taylor expansion truncated at 2k, k = ⌈α⌉-1. Running k+1 geometric batch sizes s_ℓ = 2^ℓ m and solving a linear system for a_ℓ (Σa_ℓ=1, Σa_ℓμ_j(s_ℓ)=0) cancels all polynomial bias terms; variance per batch is O(F²[d^{1-1/α}/s + (d²/s)^{2α}]).

**Why it matters** Together with Wang (2026)'s lower bounds, the sample complexity landscape for tr(ρ^α)-based entropies is now settled to polylog factors across all orders (see the paper's summary table). The Bures-χ² bias inequality and the extrapolation-over-batch-sizes trick are reusable tools for estimating other nonlinear spectral functionals.

**Caveats** Constants are α-dependent and blow up as α→1 (e.g. (1-α)^{-(2α-1)/α}); the results are stated for fixed non-integer α, with integer α>1 Rényi handled by prior work. Success probability is constant (0.98/24/25), requiring median-of-means for high confidence. The estimators need collective measurements on all n copies (tomography, Hayashi POVM) and are not computationally analyzed; polylog gaps to the lower bounds remain. The truncated source omits proofs of the Schatten Taylor, isotropy, and Richardson-coefficient lemmas.

## 3. Quantum Geometric Tensor Preconditioning for Stable Training of Recurrent Neural Quantum States

[arXiv:2608.18065](https://arxiv.org/abs/2608.18065) · [SciRate](https://scirate.com/arxiv/2608.18065)

*Adil Attar, Amine M. Aboussalah, Mohamed Hibat-Allah*

**TL;DR** — Contrary to prior reports that RNN-based neural quantum states are incompatible with curvature-based optimizers, the authors show that minimum-step stochastic reconfiguration (minSR) trains GRU wave functions stably with just a constant Tikhonov shift plus momentum, beating Adam by orders of magnitude in relative energy error on 1D TFIM (N=200) and the 1D cluster state (N=100, E=−99.99(4) vs exact −100). In 2D (square-lattice Heisenberg and J₁–J₂ at J₂=0.5) minSR is only comparable to Adam, which the authors trace to a demonstrably more ill-conditioned loss landscape of the 2D MDRNN-style architecture.

**Key contributions**
- Empirical recipe making minSR stable for RNN NQS with only 100–200 samples on a single GPU: fixed λ (1D), λ ∝ 3×10⁻⁴‖𝒯‖^{2/3} or trust-region learning rate (2D), plus momentum on the SR update.
- Two propositions explaining RNN Fisher ill-conditioning in a linear-RNN/softmax model: (i) exact GL(d_h) hidden-basis gauge orbits with velocities ([X,W], XV, Xb, −UX, 0) lie in ker S for any sample set; (ii) recurrent amplification gives λ_max(S) ≳ χ₀N³/12 for a marginal mode (r=1) and ∝|r|^{2(N−1)} for expanding modes.
- A Markov-inequality bound on subsampled QGT error: ‖Q−Q̃‖_F ≤ (N_p/√N_s)√(V_avg/ε), i.e. error ∝ α⁻¹ with α=√N_s/N_p — validated numerically on 6×6 J₁–J₂ and used to justify that N_s ≪ N_p still yields a useful preconditioner.
- Loss-landscape visualization along the extremal eigenvectors of S showing the 2D Heisenberg convex basin is ~10× narrower than 1D TFIM.
- Negative results on damping: Levenberg–Marquardt λ diverges, diag(𝒯) preconditioning yields tiny updates, structural damping too costly; SPRING slightly underperforms plain minSR+momentum.

**How it works** — Standard autoregressive RNN/GRU ansätze (positive for stoquastic, complex-phase via πSoftsign for non-stoquastic), with the minSR identity moving the inversion into the 2N_s×2N_s sample space (cost O(N_s²N_p+N_s³)); the Jacobian assembly, not inversion, dominates memory. Comparisons are made at equal wall-clock time (500 s in 1D, 24 h in 2D), so Adam takes ~2× more steps.

**Why it matters** — Removes a widely cited obstacle to combining autoregressive NQS (perfect sampling, cheap) with natural-gradient/imaginary-time optimization, and suggests a practical hybrid: minSR at small sizes, Adam after transfer to large sizes. The gauge-degeneracy proposition is a clean structural explanation likely relevant to other recurrent/gated architectures.

**Caveats** — The propositions hold for a *linear* RNN with softmax head; the authors note GRUs need not possess the full GL(d_h) symmetry exactly, so the theory is motivational rather than governing the experiments. No point-group symmetries are imposed, so absolute accuracies (especially J₁–J₂=0.5, where V-scores fluctuate strongly) are not state-of-the-art. Results rely on extensive per-model hyperparameter search, including a heuristic ‖𝒯‖^{2/3} schedule. The attribution of 2D failure to combinatorial gradient-path growth in MDRNNs is an explicitly stated conjecture; GridLSTM/LeakyLP alternatives are untested. Reference energies and scaling beyond 10×10 are limited.

## 4. Long-time fermionic quantum transport with controlled full-state error using an adaptive reservoir-mode window

[arXiv:2608.18049](https://arxiv.org/abs/2608.18049) · [SciRate](https://scirate.com/arxiv/2608.18049)

*Mikhail Umanskii, Nataliya Arefyeva, Georgy Sultanov, Alexey Rubtsov, Evgeny Polyakov*

**TL;DR** — The paper extends "tape-recorder" coarse graining (a moving, time-dependent reservoir-mode window) from bosonic to fermionic transport, giving a nonperturbative bound on the *full* device–reservoir state infidelity incurred by each discarded outgoing mode. Numerically the active-mode count per lead saturates in time (5–6 modes at $r_{\rm cut}=10^{-4}$ out to $T=3000$) and grows only logarithmically as the threshold is tightened, enabling long-time simulation of an interacting, driven two-site quantum point contact benchmarked against HEOM, Landauer–Büttiker, and exact Floquet Green functions.

**Key contributions**
- Fermionic formulation: particle–hole mapping of the filled left lead to a quasiparticle vacuum, so both leads start from vacuum while preserving the mode-space light cone; anticommutation handled via the identity $E_-+E_+=\varepsilon$ so the bound needs *no* assumption on outgoing-mode occupation.
- Single-event infidelity bound $I\le\frac12[C_-^2+C_+^2]\,\varepsilon$, with $\varepsilon$ the mode's remaining integrated coupling weight and $C_\pm$ induced $L^2\!\to\!$Hilbert response norms of the truncated propagator; a crude unitarity bound gives $I\le (s-t_d)\|V\|^2\varepsilon$. Derived from an exact Duhamel identity, not perturbation theory.
- Empirical scaling: bulk active width $\propto 0.703\ln(1/r_{\rm cut})$; trajectory dimension $\sim M_{\rm alloc}^{N_{\rm qp}^{\max}}/N_{\rm qp}^{\max}!$ at fixed quasiparticle cutoff, so cost per trajectory is linear in time steps.
- Separate calibration of the reservoir representation: active-window contact spectral density matches the full 2000-site Lanczos chain to $7.9\times10^{-5}$ in normalized $L^1$ (vs $2.7\times10^{-2}$ at the cheaper transport-run parameters).

**How it works** — Each lead's contact orbital, freely propagated, defines wave packets $|\alpha(\tau)\rangle$; the positive operators $\hat\rho_\pm=\int|\alpha\rangle\langle\alpha|$ over elapsed/remaining intervals encode how much each mode has already coupled or can still couple. A recursive backward sweep over $\hat\rho_+$ fixes incoming modes and arrival times; forward propagation diagonalizes $\hat\rho_-$ restricted to the active subspace and ejects the least-future-coupled combination. The moving basis contributes an exact kinematic connection term $-\xi_{pq}\kappa_p^\dagger\kappa_q$. Removing an entangled outgoing mode is unraveled exactly by Monte Carlo sampling its occupation sector.

**Why it matters** — Provides an error criterion on the *full* state (not just device reduced density matrix) with a bounded, time-saturating mode window — attractive where HEOM's exponential bath decomposition fails, e.g. the flat band with algebraically decaying correlations, where finite $N_k$ HEOM stays unconverged but the method reproduces Landauer–Büttiker.

**Caveats** — The bound is per-event and grows as $(T-t_d)$; accumulation over many departures isn't bounded. Production runs use a fixed rank cap, not the threshold criterion, so convergence is empirical, as is $N_{\rm qp}^{\max}$. Restricted to noninteracting leads, spinless fermions, zero temperature, full-bandwidth bias, and a two-site device; extensions to interacting/multiterminal reservoirs are only sketched.

## 5. Dynamics of Majorana tetron qubits under quasiparticle poisoning

[arXiv:2608.18042](https://arxiv.org/abs/2608.18042) · [SciRate](https://scirate.com/arxiv/2608.18042)

*Sauri Bhattacharyya, Bernard van Heck*

**TL;DR** The authors derive a Bloch–Redfield master equation for a Majorana tetron (four MZMs on a charged island, $H_A = \tfrac{i}{2}\sum A_{ij}a_ia_j + 2Ua_1a_2a_3a_4$) tunnel-coupled to four normal leads, and obtain closed-form expressions for the steady state, parity-leakage rate and qubit decoherence rate at arbitrary $U/T$ and arbitrary Majorana splitting $\epsilon$. The central result is $\Gamma_{\rm e}=\tfrac{\Gamma_0}{2}[(1+e^{\beta(U-\epsilon)})^{-1}+(1+e^{\beta(U+\epsilon)})^{-1}]\simeq \Gamma_0 e^{-\beta U}\cosh(\beta\epsilon)$: the charging-energy protection $e^{-U/T}$ is progressively spoiled by the qubit energy splitting.

**Key contributions**
- Analytic dissipators in two regimes: "degenerate" ($\epsilon\ll\Gamma_0$), where the Bloch–Redfield equation collapses to a GKSL form with rates $\Gamma_{\rm e}=\gamma(-U)/2$, $\Gamma_{\rm o}=\gamma(U)/2$, and "secular" ($\epsilon\gg\Gamma_0$).
- Proof that, for the symmetric model $H_A=i\epsilon(a_1a_2+a_3a_4)+2Ua_1a_2a_3a_4$ with identical uncorrelated leads, the secular dissipator is *identical* to the universal Lindblad equation dissipator — all interference terms in $K_i^\dagger K_i$ vanish and the cross-Bohr-frequency recycling terms cancel upon summing over Majoranas in a canonical pair. This extends validity of the secular formulas down to $\epsilon\to 0$.
- Explicit rate equations, Gibbs steady states ($P_\infty=[\cosh\beta\epsilon-e^{-\beta U}]/[\cosh\beta\epsilon+e^{-\beta U}]$, $P_{12}^\infty=\sinh\beta\epsilon/[\cdots]$), and the observation that leakage amplitude $\sim e^{-\beta U}$ occurs at the *unsuppressed* rate $\Gamma_0=\Gamma_{\rm e}+\Gamma_{\rm o}$.
- An "extended zero-energy Andreev state" scenario: cross-correlated lead coupling $\gamma_{ij}=\gamma(\omega)(\delta_{ij}+\lambda\delta_{i1}\delta_{j2}+\lambda\delta_{i2}\delta_{j1})$ mixes even/odd coherences, turning exponential into bi-exponential decay with rates $\tfrac{1}{2}\Gamma_0(1\pm\kappa)$; notably $\Gamma_-\to\tfrac12\Gamma_{\rm e}$ at $\lambda=1$, i.e. delocalization *slows* poisoning-induced decoherence — a possible discriminant vs. genuine MZMs.

**How it works** Majorana operators are decomposed into 16 jump operators $A_{i,s}=\Pi_{\sigma'\tau'}a_i\Pi_{\sigma\tau}$ labeled by the four odd→even Bohr frequencies $U\pm\epsilon_{1,2}$. Crucially, the frequency *differences* $\delta_{ss'}$ contain only $\epsilon_{1,2}$, not $U$, so secularity is controlled by $\epsilon\tau_D\sim\epsilon/\Gamma_0$. Wide-band leads give $\gamma(\omega)=2\Gamma_0/(1+e^{-\beta\omega})$, with $\tau_B^{-1}\approx\pi T$ and Born–Markov validity $\Gamma_0\ll T$. Parity superselection $[\rho,P]=0$ eliminates most interference terms.

**Why it matters** Provides ready-to-fit time-domain formulas for parity-lifetime and coherence experiments in InAs–Al/Pb tetrons and quantum-dot Kitaev-chain analogues, quantifying exactly *how* protection degrades when $\epsilon\gtrsim T$ or $U\lesssim T$; also notes that coherent precession at $\epsilon_1\pm\epsilon_2$ may be visible in time domain even when unresolvable spectroscopically.

**Caveats** Weak-coupling Born–Markov only; Lamb shifts discarded; leads assumed gapless, wide-band, particle–hole symmetric, equal tunnel rates, thermal equilibrium. The secular/ULE analysis assumes $\epsilon_1=\epsilon_2$ and a degenerate odd sector; the ULE–secular equivalence may be model-specific. Intrinsic (above-gap) poisoning, charge noise/$1/f$ dephasing on $\epsilon$, and the general asymmetric case (left to numerics) are all excluded.
