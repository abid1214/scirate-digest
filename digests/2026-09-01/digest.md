# SciRate Daily Digest — 2026-09-01

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Neutral atom quantum computing

[arXiv:2608.30783](https://arxiv.org/abs/2608.30783) · [SciRate](https://scirate.com/arxiv/2608.30783)

*M. Saffman*

**TL;DR** A review chapter that lays out the physics of neutral-atom qubits — species selection, optical trapping, encoding, readout, single- and two-qubit gates — and benchmarks the state of the art against theoretical error floors. Notable quantitative threads: arrays have reached ~10⁴ trap sites (and >10⁵ with metasurface optics), coherence times of 12–40 s, and Rydberg-gate fidelity is bounded by a fundamental error floor set by the product of interaction strength and Rydberg lifetime, with the tight prefactor recently pinned down and improvable via a resonant two-level driving scheme.

**The big picture** Individual atoms held in arrays of laser traps have become one of the two or three leading candidate platforms for a large-scale quantum computer, having gone in a few years from proof-of-principle gates to thousands of qubits and early error-corrected logical qubits. This chapter assembles the underlying atomic physics — how atoms are cooled, trapped, encoded, read out and made to interact through highly excited electronic states — with a survey of the best numbers achieved to date and where the remaining bottlenecks lie. It is useful precisely because progress has been so fast that the performance landscape, and the theoretical limits it is approaching, are hard to track from individual papers.

**Key contributions**
- Unified survey of alkali (Rb, Cs) versus alkaline-earth-like (Sr, Yb) platforms, including the optical–metastable–ground (*omg*) encoding options and their measured coherence: T₂*≈3.7 s (¹⁷¹Yb nuclear spin), 3.4 s (⁸⁷Sr optical), versus tens of ms for alkalis; T₂ up to 40 s (⁸⁷Sr), 16.6 s (Cs bottle traps), T₁=119 s.
- Explicit Poisson-statistics treatment of state readout: ~8.5 detected photons for 10⁻⁴ error, hence ≳85–100 scattered photons, giving fundamental readout times of ~1 µs (¹S₀–¹P₁) to ~5 µs (alkali D2) — with a table of maximum scattering rates and t₁₀₀ per transition.
- Consolidated statement of the Rydberg entanglement error floor: ε = η/(Vτ_R), with η ≥ 2.09 tightened to η_min = 1+π/2 ≈ 2.57, and reduced to π/2 ≈ 1.57 using rank-2 driving that excites both qubit states at a Förster resonance.
- Comparative assessment of trap geometries (bright tweezers, bottle traps, few-micron-spacing lattices), including why bottle traps lose on power scaling (saddle points ~1/3 of radial depth) and why lattices may win beyond ~10⁴ sites.
- Discussion of magic, doubly and triply magic trapping, and ground–Rydberg magic conditions via the ponderomotive Rydberg polarizability.

**How it works** Standard perturbative light-shift theory sets trap depths, differential light shifts (U₁₀/U_g = ω_q/2Δ) and scattering rates (∝Γ²/Δ²), which together fix coherence-vs-power tradeoffs. Readout fidelity is derived from convolved Poisson count distributions with a threshold n_c, yielding closed-form incomplete-gamma expressions. Gates are treated via Rabi/Raman formalism for single qubits and via dipole–dipole/van der Waals Rydberg interactions with Förster defects for entanglement, comparing the original three-pulse blockade protocol (ε ∝ (Vτ_R)^(−2/3)) with time-optimal constant-Ω, modulated-detuning pulses that saturate the linear scaling.

**Why it matters** A reliable, quantitative reference point for anyone assessing neutral atoms against superconducting or trapped-ion hardware, and a clear map of which knobs (readout speed, Rydberg lifetime × interaction strength, trap power scaling) actually gate progress toward fault tolerance. The emphasis on coherence-to-measurement-time ratios >10⁴ is directly relevant to QEC cycle budgeting.

**Caveats** It is a review, not new research; the source is truncated before the error-correction and outlook sections, so those cannot be assessed. Quoted best numbers come from disparate experiments and are not simultaneously achieved in one machine. Fast-readout time estimates neglect heating and atom loss — the author notes the ¹⁷¹Yb 6.4 µs imaging demonstration in fact required several hundred µs including recooling. Quantum simulation, and molecular and lanthanide qubits, are largely out of scope.

## 2. Unconditional Certified Randomness without Structure

[arXiv:2608.31112](https://arxiv.org/abs/2608.31112) · [SciRate](https://scirate.com/arxiv/2608.31112)

*Andrea Coladangelo, Dakshita Khurana, Saachi Mutreja, Bhaskar Roberts, Joseph Slote, Avishay Tal*

**TL;DR** The authors give a non-interactive, publicly verifiable certified-randomness protocol in the quantum random oracle model, built on the Yamakawa–Zhandry (YZ) proof of quantumness, and prove *unconditionally* that any adversary making subexponentially many (up to 2^{o(λ^c)}, c<1/2) fully adaptive quantum oracle queries either fails verification or outputs a distribution with high min-entropy. This removes both previous crutches: the Aaronson–Ambainis conjecture and the restriction to o(log n) adaptive query layers (KRT). The technical core is a new "query-norm polytope" reprogramming argument plus a redesigned code and a biased oracle.

**The big picture** Certified randomness lets a classical, untrusted client extract provably fresh randomness from a remote quantum device, and it is one of the few near-term quantum applications with a clear commercial hook. Existing hash-based proposals were either only proven secure under an unproven complexity conjecture, or only against adversaries that make their queries in very few rounds of adaptivity — a serious gap, since a cheating device would naturally query adaptively. This work closes that gap, giving the first unconditional entropy guarantee against adversaries with essentially unrestricted adaptivity in the idealized-hash model, at the cost of a new code construction and a deliberately biased hash.

**Key contributions**
- Unconditional certified min-entropy in the QROM against arbitrarily adaptive provers with up to 2^{o(λ^c)} queries.
- The *query norm* (√query weight) as the reprogramming "currency", plus a *local stability* inequality: |w̃_u(h) − w̃_u(h′)| ≤ 2Q Σ_{v∈X} w̃_v(h).
- The **query-norm polytope**: recasting reprogramming as a purely geometric feasibility question, and a heavy-coordinate reprogramming lemma — protecting only C(k,2) coordinates leaves 2^{Ω(n)} reprogrammings each retaining k heavy coordinates (k = Θ(√n)).
- A modified YZ instantiation: folded Reed–Solomon of rate 1/(10√n) with low-agreement list recovery at agreement √n/5 and list size 2^{O(n^c log n)}, plus a p≈1/(40√n)-biased oracle to restore completeness.
- Complexity leveraging to any poly(λ) bits of certified min-entropy.

**How it works** Two claims are combined: (1) if a prover outputs a correct codeword with noticeable probability α, that codeword must be "heavily queried" on ≥0.9n coordinates — else reprogramming 2^{0.1n} subsets of light coordinates yields disjoint oracle/answer pairs and a counting contradiction; (2) a query-bounded prover cannot heavily query a codeword — a bipartite double-counting with left degree 2^{Ω(n)} from the polytope lemma and right degree bounded by list recovery. Because only Θ(√n) heavy symbols survive reprogramming, the code must list-recover at O(1/√n) agreement; the resulting low rate breaks dual-code decoding, repaired by biasing the oracle so the Fourier-basis error has O(√n) support. Counting becomes weighted, giving failure probabilities L(1−p)^{4n/5} = exp(−Ω(√n)).

**Why it matters** It cements a hash-based, hardware-light route to certified randomness (single round, classical verification) on unconditional foundations, and the query-norm polytope is a reusable tool for adaptive-adversary reprogramming in the QROM more broadly.

**Caveats** Security is only in the idealized QROM; the query bound is 2^{o(λ^c)} with c<1/2, not the natural 2^{Ω(n)}, and the base protocol certifies only o(λ^c) bits before leveraging (which blows up λ as h^{2/c}). The Θ(√n)-vs-Θ(n) gap in surviving heavy coordinates is left as an explicit open question. No treatment of noise tolerance, entropy accumulation over many rounds, or concrete resource costs; the YZ prover remains expensive.

## 3. Universal recovery in approximate quantum error correction

[arXiv:2608.28962](https://arxiv.org/abs/2608.28962) · [SciRate](https://scirate.com/arxiv/2608.28962)

*Dor Elimelech, Victor V. Albert, Alexander Barg*

**TL;DR** For the error-set formulation of approximate QEC introduced in the authors' companion work, a *single* recovery map suffices for the entire family of channels "controlled" by an error set. In the average-case (channel-fidelity) setting the optimal universal decoding error exactly equals the optimal channel-adapted AQEC error (a minimax argument), and in the worst case a universal decoder achieves error at most √ζ in the environment-leakage distance — a √2 improvement over the previous bound. The Petz map built directly from the error set (shown to coincide with the "polar" decoder) is an explicit universal recovery with average-case error bounded by the Knill–Laflamme Hellinger distance.

**The big picture** In exact quantum error correction, if a code corrects a given list of errors, then one fixed decoder corrects every noise process built from those errors — the decoder needs to know only what errors are possible, not which noise actually occurred. This adversarial, decoder-once-for-all structure was thought to break down when correction is only approximate, and most approximate-QEC theory has instead tailored a decoder to each specific noise channel. This work shows the adversarial picture survives: a single decoder, depending only on the error list and the code, protects uniformly against the whole family of noise processes built from that list, with quantitative guarantees on both worst-case and average-case performance, and with an explicit construction.

**Key contributions**
- Average case: ε*_dec(ℰ,Q) = ε*_opt(ℰ,Q) — universality is free; in particular a universal decoder with error ≤ ζ_H exists.
- Worst case: existence of a universal recovery with d_wc ≤ √ζ(ℰ,Q) for all ℰ-controlled channels; as a corollary the sufficient AQEC condition of the companion paper tightens from √(2ζ) to √ζ.
- Definition and analysis of an error-set Petz map (transpose channel of the non-TP map Σ E X E†, completed off supp Γ), proved identical to the polar decoder of Ma et al. — extending that construction beyond Haar/nondegenerate unitary settings.
- Uniform average-case bound d_ch ≤ ζ_H for the error-set Petz map over all ℰ-controlled channels, plus a suboptimality sandwich ζ_H/√(2M) ≤ ε*_opt ≤ ζ_H for HS-orthogonal unitary error sets.
- Worst-case bound for the Petz map, under the stronger constraint ‖C‖₂ ≤ 1 (strongly controlled channels), in terms of ‖√A_QEC − I⊗√(tr_K A_QEC/K)‖_∞.

**How it works** The average-case result is Sion's minimax applied to the bilinear channel fidelity F_ch(R∘N, id) over the compact convex sets of CPTP recoveries and of ℰ-controlled channels. The worst-case result lifts Kretschmann–Schuch–Werner–Wolf Stinespring continuity from channels to error sets: the Bény–Oreshkov superoperator is identified as the difference of the complementary map of the error-set noise map and a constant map with dilation V_λ; small diamond norm yields partial isometries J_ℰ, J_λ with ‖(I⊗J_ℰ)V_ℰ − (I⊗J_λ)V_λ‖_∞ ≤ √(2ζ), and R = J_λ†J_ℰ defines the decoder. Crucially, an ℰ-controlled channel has dilation (C⊗I)V_ℰ, and ‖C‖_∞ ≤ 1 lets the same R be pulled through, giving a channel-independent bound. The Petz analysis uses the polar decomposition of the error-synthesis operator S_{ℰ,Q}, so that tr_K√A_QEC controls fidelity and positivity of (1/K)tr_K A_QEC − (1/K²)(tr_K√A_QEC)² absorbs the C-dependence.

**Why it matters** It restores the full "code + distance ⇒ decoder" logic of stabilizer-style QEC to the approximate regime, so approximate code constructions (including the asymptotically good families of the companion paper) come with one fixed, error-set-defined decoder — relevant to anyone designing decoders for structured noise or studying AQEC bounds.

**Caveats** Worst-case Petz guarantees require the stricter Frobenius-norm condition ‖C‖₂ ≤ 1 (automatic only for HS-orthogonal unitary error sets), and are stated via an operator-norm KL distance rather than ζ. The worst-case existence proof is dilation-based and not obviously constructive. The average-case suboptimality gap of the error-set Petz map scales as √|ℰ|. Everything is finite-dimensional, and channel fidelity is a weaker (maximally-entangled-input) criterion than worst-case entanglement fidelity.

## 4. Theory of approximate quantum error correction and the error-set model

[arXiv:2607.22995](https://arxiv.org/abs/2607.22995) · [SciRate](https://scirate.com/arxiv/2607.22995)

*Dor Elimelech, Victor V. Albert, Alexander Barg*

**TL;DR** The paper shows that approximate QEC does admit an adversarial *error-set* model, contradicting the long-held view (quoted in the epigraph from Crépeau–Gottesman–Smith) that approximate codes have no sensible distance. The key device is the class of "$\mathcal{E}$-controlled" channels — those whose Kraus operators are combinations of a fixed error set with coefficient matrix of spectral norm at most 1 — for which a single code parameter gives uniform recovery guarantees; the framework is then instantiated via partition codes to yield the first asymptotically good code families for fermionic Majorana noise, 1D Rydberg-blockaded chains, and deletion errors.

**The big picture** In exact quantum error correction, protecting against a list of possible errors automatically protects against any noise built out of them, which is what gives codes a distance and lets one design codes without knowing the noise exactly. Approximate error correction, where recovery need only be near-perfect, had been believed to lose this structure, forcing analysis one noise process at a time. This work identifies the precise restricted sense in which the structure survives — a spectral bound on how the errors are mixed — and thereby recovers distance, the erasure/general-error equivalence, and asymptotic code families in the approximate setting, plus a general recipe for building such codes across atomic, bosonic, fermionic, and permutation-symmetric platforms.

**Key contributions**
- Definition of $\mathcal{E}$-controlled channels ($A_m=\sum_k c_{mk}E_k$, $\|C\|_\infty\le1$); shown representation-independent for linearly independent $\mathcal{E}$ and closed under convex mixtures.
- *Environment-leakage distance* $\zeta(\mathcal{E},Q)=\inf_\lambda\|\mathcal{B}^{\mathcal{E}}_{\lambda,Q}\|_\diamond$; $\zeta\le\varepsilon^2/2$ suffices for worst-case $\varepsilon$-AQEC of the *entire* controlled family; shown near-optimal in an example, with necessary converses for orthogonal-unitary and amplitude-damping sets.
- Average-case analogue: the Zheng et al. Petz-recovery figure of merit is reinterpreted as a normalized Hellinger distance from the QEC matrix $A_{\rm QEC}$ to the Knill–Laflamme space $\{I_K\otimes\lambda\}$; this distance is shown to be monotone under conjugation by contractions, which is exactly the passage from $\mathcal{E}$ to $\mathcal{E}$-controlled channels.
- Approximate distance for arbitrary indexed error-set families, and a quantitative two-way $2t$-erasure ↔ $t$-error equivalence (with dimension-dependent constants and square-root loss); subsystem variance is shown to bound $\zeta$ for erasures, tightening the AQEC/circuit-complexity link.
- Metric–error alignment hierarchy $\mathscr{L}_2\subset\mathscr{L}_1\subset\mathscr{L}_0$ classifying (Hilbert space, metric, noise) triples, with a table placing nine standard settings.

**How it works** For Hilbert spaces with basis indexed by a metric space, one picks a classical code $C$ with minimum distance $>t$ and partitions it into blocks whose uniform superpositions are the logical basis states. Level $\mathscr{L}_1$/$\mathscr{L}_2$ alignment makes the off-diagonal KL conditions automatic; the diagonal ones are met either existentially via Tverberg-type convex partition arguments (requiring $|C|\gtrsim K|\mathcal{E}_t|^{3-i}$, computationally infeasible) or approximately via random codes with arbitrary equal-size blocks, giving vanishing $\varepsilon$ whenever $K=o(|C|^{1/3}/|\mathcal{E}_t|^{2-2i/3})$.

**Why it matters** It restores channel-independent, distance-based design to AQEC, relevant to anyone building codes for bosonic, fermionic, or neutral-atom hardware where exact correction is unavailable, and it supplies non-stabilizer asymptotically good constructions in regimes previously served only by stabilizer/subsystem codes. The amplitude-damping result — that linearly many damping errors may be easier than general weight-$t$ errors — is a concrete new asymptotic separation.

**Caveats** No universal decoder is constructed: guarantees are existence-of-recovery-map statements per channel, not one decoder for the whole controlled family. Constants in the erasure↔error conversion and in the necessary conditions grow with dimension/error-set size, and there is a square-root loss from Bures→diamond norm. No general necessary-and-sufficient error-set criterion is obtained, and stabilizer AQEC remains open; the exact partition constructions are not practically computable.

## 5. Bosonic codes from compact phase spaces

[arXiv:2608.31156](https://arxiv.org/abs/2608.31156) · [SciRate](https://scirate.com/arxiv/2608.31156)

*David Roberts, Aaron Slipper, Alireza Parhizkar, Victor V. Albert, Mohammad Hafezi*

**TL;DR** The authors build single-mode-pair bosonic stabilizer codes whose phase space is a compact hyperbolic Riemann surface: the stabilizers are two-mode squeezing operators generating a cocompact Fuchsian group, and the code words are holomorphic k-differentials (automorphic forms), with dimension (2k−1)(g−1) from Riemann–Roch. For the genus-2 Bolza curve the logical gate group is the 48-element single-qubit Clifford group GL(2,𝔽₃), realized entirely by Gaussian operations — but a no-go theorem shows that non-amenability of the surface group opens a spectral gap (δ ≥ 0.337 rigorously, ≈0.45 numerically) in the stabilizer Hamiltonian, so no normalizable state, even approximately, can satisfy all stabilizers.

**The big picture** Continuous-variable quantum codes can be organized by the geometry of the phase space they live on: a sphere gives finite stabilizer groups and exact code states, a flat torus gives the familiar grid codes with arbitrarily good approximate states, and this work completes the classification by treating negatively curved, higher-handle surfaces. On such surfaces the code words become classical objects from number theory and the encoded gates can, in principle, realize any finite group using only two oscillators and Gaussian operations. The catch is that the same negative curvature that makes the symmetry structure so rich also makes the constraint set expanding rather than averageable, which provably rules out physical, finite-energy states satisfying all the constraints. This draws a sharp geometric dividing line for when phase-space stabilizer codes can exist at all.

**Key contributions**
- A general "phase-space stabilizer code" framework: compact coherent-state families, a rigid stellar/Majorana representation whose rank equals deg 𝓛, and Riemann–Roch as a topological Bohr–Sommerfeld rule (dim ℋ = r − g + 1).
- Explicit hyperbolic codes: 𝓗_Γ ≅ Γ(C, Ω^{⊗k}); the full weight tower generated from a weight-1 basis plus the Wronskian.
- Constructive genus-2 recipe: pants-decomposition Poincaré/theta series (3g−3 of them) rotated into the conic form Y² = XZ, fixing ω₀ = √X, ω₁ = √Z; for Bolza a single complex parameter λ ≈ −1.014 − 0.239i.
- Logical gates = Aut(C), Gaussian; Bolza → GL(2,𝔽₃) with explicit 2×2 logical matrices; via Greenberg's theorem any finite group is achievable in two modes.
- Spectral-gap theorem via Kesten non-amenability + weak containment in the regular representation, plus the amenability dichotomy corollary.

**How it works** Two bosonic modes carry the SU(1,1) discrete series (K₊ = a†b†), so the Poincaré disk is a bona fide phase space and Möbius stabilizers are two-mode squeezes. Stabilizer-averaging coherent states gives local frames that glue into a line bundle; invariance forces stellar functions to be automorphic. The gap proof bounds sup σ(M) ≤ ‖M‖ ≤ ‖M_λ‖ < 1 for the generator random walk. A circuit-QED implementation (two cavities, transmon, SQUID pump, dispersive χ) yields conditional squeezes and cross-Kerr; simulated conditional-kick dissipation converges for one generator (Re⟨D⟩: 0.03 → 0.97 in 500 rounds) but plateaus at O(1) energy for 2–4 generators, confirming the gap.

**Why it matters** It settles the existence question for hyperbolic bosonic codes, identifies amenability as the sharp criterion for approximate code words, and provides an infinite-dimensional analogue — stronger than NLTS — of expansion-based obstructions. Relevant to CV code designers, geometric-quantization theorists, and circuit-QED experimentalists.

**Caveats** The no-go concerns exact unitary stabilizers; energy-damped finite-energy analogues (à la Royer et al.) may evade it, and this is left open. The k=1 averaging diverges, λ and δ ≈ 0.45 are numerical/extrapolated from truncation, no distance or performance analysis against realistic loss/dephasing is given, and the required squeezing (~13 dB stabilizers, ~6.6 dB gates) plus Trotterized SU(1,1) synthesis is demanding.
