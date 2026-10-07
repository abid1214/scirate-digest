# SciRate Daily Digest — 2026-10-07

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Entanglement manipulation and magic area-laws

[arXiv:2610.08727](https://arxiv.org/abs/2610.08727) · [SciRate](https://scirate.com/arxiv/2610.08727)

*Rafael A. Macedo, Rafael Chaves*

**TL;DR** The paper imports the recent entanglement-dominated (ED) / magic-dominated (MD) dichotomy into the setting of area-law states and shows the split survives: area-law ED states obey an *area law for non-stabilizerness* (measured by the entropy-subtracted stabilizer Rényi entropy), while faster-than-area growth of subsystem magic certifies MD, where entanglement estimation, distillation and dilution remain provably hard even under the area-law constraint. The authors then define a "stabilizer regime" — equivalence under finite-depth circuits doped with only $o(\log n)$ non-Clifford gates — as the restricted notion of phase that preserves both area laws and efficient entanglement manipulation.

**The big picture** Ground states of locally interacting systems are famously "entanglement-cheap": the entanglement of a region grows only with its boundary. But the other key resource for quantum advantage — the degree to which a state escapes classical simulability by stabilizer methods — typically grows with the volume, even in such structured states. This work shows that area-law states therefore come in two sharply different flavours: those whose magic is also boundary-limited, which behave almost like error-correcting codes and permit efficient protocols for converting entanglement into Bell pairs and back; and those whose magic is extensive, for which these conversions are computationally intractable. The upshot is a refined notion of a quantum phase in which stabilizer structure, not just entanglement structure, is the protected feature — relevant because decoders for topological codes rely on exactly that structure surviving perturbations.

**Key contributions**
- Theorem: no state-agnostic, sample-efficient protocol achieves constant-factor entanglement estimation ($\le 1/3$ relative error), distillation ($M_+/S \ge c$) or dilution ($M_-/S \le C$) uniformly over area-law MD states with $S(\psi_A)=\omega(\log n)$.
- Bound $\tilde M_2(\psi_A) \le \nu(\psi)$ for all subsystems, yielding: ED + area law $\Rightarrow \tilde M_2(\psi_A)=O(|\partial A|)$; $\tilde M_2(\psi_A)=\omega(|\partial A|)$ $\Rightarrow$ MD.
- Closed formula for $\tilde M_2(\psi_A)$ for nullity-$\nu$ states in terms of "bad generator" expectation values, computable in $O(4^\nu n^3)$.
- Definition of the *stabilizer regime* ($o(\log n)$-doped FDQCs preserving entropy scaling) and proof that it preserves ED-ness and both area laws.

**How it works** The hardness proof adapts Gu et al.'s ensemble-distinguishing argument by embedding Haar-random states on $\mathrm{poly}\log n$-qubit blocks into the $D$-dimensional lattice via sphere packing, so the resulting family is genuinely area-law yet still indistinguishable to efficient protocols. The magic area law is a structural consequence: $\tilde M_2 = M_2 - S_2$ is faithful for the mixed-stabilizer free set, is bounded by the global nullity, and ED means $S=\omega(\nu)$, which combined with $S=O(|\partial A|)$ pins $\nu = o(|\partial A|)$. The stabilizer-regime stability uses the fact that perturbing a local stabilizer Hamiltonian by $p$ Pauli terms gives ground-state nullity $\le p$.

**Why it matters** It gives an operational meaning to "magic area law" — it is exactly the signature of efficiently manipulable entanglement — and suggests an ED-to-MD transition inside a single conventional phase, detectable numerically as the perturbation count crosses the logarithmic scale. Relevant to error-correction, tensor-network, and resource-theory communities.

**Caveats** Theorem 2 is essentially a corollary of the nullity bound plus definitions, and is one-directional: MD does not imply super-area magic growth. The hardness result does not apply in $D=1$ (MPS admit efficient tomography), the very case where most magic numerics exist. Definition 2 assumes the stronger $\alpha=0$ (Schmidt-rank) area law, an explicit assumption rather than a theorem. The $t=o(\log n)$ doping threshold is acknowledged as somewhat arbitrary, the entropy-scaling-preservation clause is needed to exclude disentangling circuits, and no numerical evidence for the proposed ED/MD transition is presented.

## 2. Pauli Flat Quantum States Mimicking Maximal Magic

[arXiv:2610.07172](https://arxiv.org/abs/2610.07172) · [SciRate](https://scirate.com/arxiv/2610.07172)

*Paweł Cieśliński*

**TL;DR** The author defines *Pauli flat* states — N-qubit states whose expectation values on all 4^N−1 non-identity Pauli strings have identical magnitude γ — generalizing the correlation structure of the maximally magical T state (N=1) and Hoggar state (N=3), which are the only pure examples (existence of such pure states is equivalent to a Pauli-covariant Weyl–Heisenberg SIC fiducial, known to exist only for N=1,3). Mixed Pauli flat states exist for every N (any γ ≤ 1/√((4^N−1)(2^N−1)) works), and a tailored stabiliser-norm witness shows that γ > 1/(2^N+1) certifies non-stabiliserness; explicit SDP-constructed examples with genuine magic are given for N=2 (γ=1/3) and N=4 (γ≈0.0673), while the best N=5 state found (γ≈0.0293) falls just short of the magic threshold.

**The big picture** Stabiliser states — the classically simulable ones — have a very rigid signature in Pauli measurements: a few correlations are perfectly sharp and the rest vanish. The most "magical" states known sit at the opposite extreme, spreading their correlations perfectly evenly across every possible Pauli measurement, but such perfectly flat pure states only exist in one and three qubits. This work asks what happens if purity is traded away, finds that perfectly flat correlation profiles can be built for any number of qubits, and shows that some of them still lie outside the classically simulable set while others only mimic the signature without carrying any real computational resource. The practical warning is that certifying magic from an apparently flat Pauli spectrum alone can be misleading unless purity is also pinned down.

**Key contributions**
- Definition and existence proof of Pauli flat states for arbitrary N, with an explicit positivity-safe bound on γ and a trivial-stabiliser bound γ ≤ 1/(4^N−1).
- A geometric magic witness W = Σ r̃_i P_i with stabiliser bound 2^N−1 (since any pure stabiliser state has at most 2^N−1 nonzero Paulis), yielding the clean criterion γ > 1/(2^N+1) ⇒ outside STAB; shown equivalent to stabiliser-norm/reduced-robustness conditions.
- Explicit states: the N=2 family (γ ∈ (1/5,1/3], the optimum being a local-Clifford image of the Hoggar two-qubit marginal) and SDP-optimized N=4, N=5 states with full sign vectors tabulated.
- Characterization of their other resources: N=2 state is PPT-entangled-detectable (negativity ≈0.18) but *not* CHSH-violating (T singular values 2/3,2/3,1/3; max CHSH 4√2/3≈1.88); N=4,5 states entangled across all bipartitions but with no detected genuine multipartite entanglement (PPT-mixer monotone) and no violation of 2- or 3-setting Pauli-only Bell inequalities.
- Relaxed pure states where unequal Paulis are forced to zero: recovers T, LLY/MUB and Hoggar fiducials for N=1,2,3, and finds |s₄⟩ ∝ (−3,1,…,1) with 135 equal nonzero Paulis (SRE 1.79 vs. conjectured max ≈2.11–2.14) and a |s₅⟩ with 496 (SRE 2.39 vs ≈2.8).

**How it works** Flatness fixes the state to ρ = 2^{−N}(1 + γ Σ r_i P_i), so the only freedom is the sign vector r and the scale γ. Maximizing γ subject to ρ ⪰ 0 is an SDP for each r, equivalently minimizing the largest eigenvalue of the Pauli Hamiltonian Σ r_i P_i; the hard part is the 2^{4^N−1} search over sign vectors. The witness ratio η_S = γ(4^N−1)/(2^N−1) then flags magic when >1.

**Why it matters** The construction cleanly separates "flat Pauli spectrum" from "non-stabiliserness," which is relevant for anyone estimating SRE-like magic from partial Pauli sampling, and supplies a maximally-correlated counterpart to the known entangled states with vanishing sector lengths — useful for sector-length entanglement criteria and informationally-complete measurement design.

**Caveats** The sign-vector optimization is heuristic, so the reported γ values are "best found," not optimal; whether magic-carrying Pauli flat states exist for all N remains open (N=5 gives η_S=0.966, i.e. magic undetected rather than proven absent, so the headline "mimicking" claim rests on a one-sided witness). Purity collapses rapidly with N (0.135 at N=4, 0.059 at N=5), limiting operational usefulness. GME and nonlocality conclusions are numerical and restricted (PPT-mixer relaxation; ≤3 Pauli settings per party), and the relaxed pure states are stated as numerically found with no optimality proof.

## 3. No-Disturbance-without-Uncertainty generates the Quantum set in the simplest Bell scenario

[arXiv:2610.08749](https://arxiv.org/abs/2610.08749) · [SciRate](https://scirate.com/arxiv/2610.08749)

*Ravishankar Ramanathan*

**TL;DR** The paper proves that the "No-Disturbance-without-Uncertainty" (NDWU) criterion of Sun–Zhou–Yu, imposed with a *single* measurement-overlap parameter shared across all steered preparations, carves out a (non-convex) set whose convex hull is exactly the full eight-dimensional finite-dimensional quantum set Q(2,2;2,2) — marginals included, not just the four-dimensional correlator set characterized by Tsirelson–Landau–Masanes. The proof is constructive (Bloch-vector assemblage + purification) and extends to any scenario where one party has two binary settings and the other has arbitrarily many settings/outcomes; it also yields a one-parameter family of second-order cone programs that computes the exact quantum value of any linear Bell functional in these scenarios.

**The big picture** A long-standing goal in quantum foundations is to single out the correlations achievable in nature using a physically meaningful principle rather than the usual hierarchy of semidefinite relaxations. Here a principle saying that a sharp measurement cannot disturb a later incompatible measurement more than the product of two uncertainties allows is shown — once one also allows parties to share classical randomness — to reproduce precisely the quantum correlations in the simplest Bell experiment, including the single-party statistics that earlier characterizations left out. As a practical dividend, finding the quantum maximum of any Bell expression in this setting collapses from an infinite hierarchy of optimizations to a scalar scan over a family of conic programs.

**Key contributions**
- Resolution of the open question in Sun–Zhou–Yu: every behavior satisfying common-overlap NDWU is quantum, and the hull equals Q₂₂₂₂ (one-sided NDWU already suffices: conv(A_A) = conv(A_B) = conv(A_Y)).
- Explicit demonstration that the raw NDWU sets are non-convex and do not even contain all local behaviors (mixing deterministic points needing overlaps c = +1 and c = −1); convexification is essential.
- Carathéodory/Fenchel argument: eight pure-two-qubit "sharp" points suffice for any quantum behavior (compactness + path-connectedness of the parameter space CP³ × (S²)⁴).
- Exact Bell optimization as max over c ∈ [−1,1] of an SOCP, with the constraint written as a second-order cone on (q − cp, sp) versus s·t.
- Extension to Q(2,2;n,**m**) via the Panahi–Wolfe qubit reduction; coarse-grained binary NDWU as an outer approximation for more outcomes.
- Separation result: the pure-two-qubit set is strictly inside A_Y (explicit local family P^(r), r ∈ (2/3, 1/√2)).

**How it works** Given NDWU with overlap c_B, choose Bob directions n̂₀ = ẑ, n̂₁ = (s_B,0,c_B). The quadratic v₀² + v₁² + c² − 2c v₀v₁ ≤ 1 is then *exactly* the statement that the vector reproducing the two steered averages has Bloch norm ≤ 1. Subnormalized operators τ_{a|x} = P(a|x)(I + r⃗·σ⃗)/2 are positive; no-signalling forces Σ_a τ_{a|x} = ρ_B independent of x, i.e. a valid assemblage. Purifying ρ_B and defining Alice's POVM as the transpose of ρ_B^{−1/2} τ ρ_B^{−1/2} (Schrödinger–HJW) reproduces P. The converse uses Naimark dilation, Jordan's lemma and Masanes' extremal theorem to write Q₂₂₂₂ = conv(Q^sharp) ⊆ conv(A_Y).

**Why it matters** It supplies the first (partly) information-theoretic characterization of the *complete* CHSH-scenario quantum body, going beyond generalized Information Causality which recovers only the correlator boundary. The SOCP reformulation is a genuinely usable tool for device-independent certification in 2-input/binary-output settings, replacing NPA-level reasoning with a 1-D scan.

**Caveats** The common-overlap requirement — that c depend only on the measurement pair and not the preparation — is a strong, arguably already quantum-flavored assumption, and its derivation (Lemma 1) presupposes repeatability and outcome-only post-measurement states; much of the proof's force comes from the quadratic being literally a qubit Bloch-ball condition, so the "principle" is close to an operational restatement of qubit steering. The criterion is not closed under shared randomness, which is physically awkward since randomness should be free. Results cover the finite-dimensional tensor-product set only (commuting-operator case untouched), require one party restricted to two binary settings, and no intrinsic multi-outcome/multi-setting version of the principle is given.

## 4. Black Hole Radiation Decoding in the Haar Random Oracle Model

[arXiv:2610.07124](https://arxiv.org/abs/2610.07124) · [SciRate](https://scirate.com/arxiv/2610.07124)

*Ezekiel Cochran, Atul Mantri*

**TL;DR** The authors prove that recovering a single qubit of infalling information from Hawking radiation in the Haar-random oracle model requires Ω(2^|H|) queries to the black-hole unitary — exponential in the size of the remaining black hole — even for decoders with controlled and coherently selected access to the unitary, its inverse, conjugate, and transpose. The bound is tight: a specialized Uhlmann-transformation decoder using only forward and inverse queries achieves O(2^|H|) queries, and the technique yields EFI pairs and bit commitments relative to a *public* Haar oracle plus a tight linear rank lower bound for Uhlmann transformation.

**The big picture** The firewall paradox hinges on whether an outside observer can quickly extract a qubit's worth of information from old Hawking radiation; a longstanding conjecture is that this is computationally hard, which would protect the smooth horizon. Previous hardness arguments relied on unproven complexity assumptions or on restricted forms of access to the evaporation dynamics. Here the hardness is established unconditionally in an idealized model where the dynamics is a perfectly random unitary that the decoder may query in every allowed direction, and the number of required queries is pinned down exactly, matching a known decoding algorithm. As a bonus, the same randomness that makes decoding hard is shown to be a usable cryptographic resource: a publicly known scrambling dynamics suffices to build commitments without any secret key.

**Key contributions**
- A trace-distance bound between the real radiation state and the maximally mixed state after q queries: ≤ (25+24√2)q/2^|H| + 36(q+1)²/2^{n/8} for all four query types; ≤ (12+3√2)q/2^|H| for forward-only.
- Hence Ω(min{2^|H|, 2^{n/16}}) queries for any constant Bell-fidelity advantage over the trivial 1/4; also holds for decoders succeeding on only a constant fraction of oracles.
- A matching O(2^|H|) forward/inverse decoder (specializing Utsumi et al.'s Uhlmann algorithm with an oracle-independent rank cutoff), fidelity ≥ 1 − 2·2^{(|H|−|R|)/2} − ε.
- A tight Ω(r) preparation-query lower bound for Uhlmann transformation on a fixed-target family (|R| = 15|H|), tolerating squared-fidelity error 1/8 and all four query types — improving on prior cube-root/near-linear bounds and extending them past the forward/inverse barrier.
- EFI pairs, statistically binding bit commitments, and a direct keyless qubit commitment (send R, later reveal H) in the public Haar-oracle model.

**How it works** Haar queries are replaced by Ma–Huang/Schuster et al. path-recording partial isometries (V, V†, V̄, V̄†) that log input–output pairs in hidden left/right relation registers, at approximation cost O(q²/2^{n/8}). The real and mixed recording experiments differ only in *where* the challenge pair (x₀, (r,h)) sits: inside the oracle record, or in an isolated register. A non-isometric insertion map J moves it, with J†J = I + Σ where Σ sums transpositions. Two error terms are bounded: (i) the "forgetting" error ‖K_φ‖₁ ≤ q/2^|H|, exploiting that the decoder cannot touch H so its amplitudes are independent of h, with at most q recorded pairs to confuse the challenge with; (ii) the commutator of J with each query, controlled by insertion/deletion estimates for the explicit creation maps A, B, Ā, B̄ and a hybrid argument over q steps. Controlled queries are reduced to uncontrolled ones via Tang–Wright and phase invariance; selected queries cost a factor 4.

**Why it matters** This converts the Harlow–Hazeldine-style complexity argument from a conditional statement into an unconditional, quantitatively optimal query bound in a model that permits the strongest reasonable oracle access — closing a gap flagged by the strong-PRU literature, where conjugate access is known to break some forward/inverse-secure constructions. For quantum cryptographers, it gives clean Haar-oracle-relative EFI and commitments with no secret key, plus the first linear-in-rank Uhlmann lower bound robust to all four access types.

**Caveats** The lower bound holds only for |H| ≤ n/16 (the 2^{n/16} cutoff is an artifact of the path-recording approximation, not believed fundamental), requires |R| ≥ |H|, and crucially assumes the decoder's circuit and auxiliary state are chosen *independently* of the sampled U — a non-uniform decoder tailored to a specific unitary is not excluded. Haar randomness is an idealization of real black-hole dynamics; transfer to efficiently implementable strong designs/PRUs is sketched but needs the design order and access model to cover challenge preparation plus 4q+1 calls. The matching upper bound is stated for |R| ≥ |H|+1 and asymptotic |H|.

## 5. Energy-constrained two-way capacity bounds for noisy Gaussian channels

[arXiv:2610.08786](https://arxiv.org/abs/2610.08786) · [SciRate](https://scirate.com/arxiv/2610.08786)

*Stefano Pirandola*

**TL;DR** This paper derives a single closed-form, energy-dependent weak-converse function 𝓕_{τ,v}(N) that upper bounds the two-way quantum, entanglement-distribution, private and secret-key capacities of thermal-loss, noisy-amplifier, and additive-noise bosonic channels under an unconditional mean transmitted-photon constraint. The bound vanishes exactly on the entanglement-breaking boundary (v ≥ τ), recovers PLOB as N → ∞, and at N = 1 beats the best previous (minimum of Gaussian squashed-entanglement and PLOB) bounds by 31–41% in the worked examples.

**The big picture** Fundamental limits on quantum communication and key distribution over optical channels are usually stated assuming unlimited transmitter power, but real senders have an energy budget, and the known finite-energy upper limits are loose once the channel adds excess noise. This work extends a channel-simulation technique — replacing each channel use by a fixed entangled resource consumed by local operations and classical communication — from the idealized noiseless-environment case to genuinely noisy channels, and evaluates the entanglement of the resulting noisy resource exactly. The payoff is a single formula that interpolates between zero capacity for very noisy channels and the known infinite-energy limits, tightening the benchmark against which practical repeaterless protocols are judged.

**Key contributions**
- A unified converse function covering all three phase-insensitive noisy Gaussian families, valid for arbitrary adaptive protocols with unbounded quantum memories and two-way classical communication.
- Exact evaluation of the relative entropy of entanglement of the mixed photon-sector resource states, with proof that a condensate-twirl separable state is the optimal comparison, plus product additivity on finite tensor products.
- Operational proof of concavity/monotonicity of the bound (not read off the formula), enabling averaging over per-use energies x_i.
- An exact integral identity for the residual gap to the hashing rate: 𝓕 − I_hash = ∫_t^{min(N,y)} log₂[(L−z)/z] dz > 0.
- Finite-error rate bounds: (1−ε)log₂d ≤ Σ𝓕(x_i)+h₂(ε) and (1−e)²log₂d ≤ Σ𝓕(x_i)+h₂(2e−e²).

**How it works** The channel is factored as 𝓛_a followed by 𝓐_{G,0}; its action on a maximally entangled state within a fixed total-photon-number sector defines the resource J_{s,m}. A ladder operator C_± = Σ r_i b_i block-diagonalizes the conditional states, giving explicit eigenvalues H_h(z) with z = τ/[(1+v−τ)v] > 1 exactly in the non-entanglement-breaking region. Concentration of the sector labels (K/s → y, H/s → t, the smaller root of t(L−t) = τN(N+1)) yields the per-mode entanglement density 𝓕. A block inequality using phase-covariant pinching costs only g(s(τx+v)) = o(s); a replica argument over independent copies of a single fixed input eliminates that overhead, and telescoping along the protocol plus concavity converts per-use energies into the budget N.

**Why it matters** It supplies a common, physically meaningful finite-energy benchmark for repeaterless CV-QKD and quantum communication over thermal and amplifier channels — the regimes actually relevant to free-space and satellite links — and demonstrates that keeping the energy constraint inside the simulation resource converts otherwise energy-blind entanglement bounds into sharp converses.

**Caveats** This is a weak converse only; the author explicitly notes that public vacuum dilution under an unconditional mean-energy constraint blocks inferring a strong converse, and exact strong-converse thresholds remain open. A quantitative gap to achievability persists (e.g. 0.24 vs 0.37 bits for the thermal-loss example), and hashing is not claimed optimal. The proof is modular on a companion work's simulation, truncation, and privacy-test machinery. No finite-blocklength refinement, and only unconditional mean-photon-number constraints are treated.
