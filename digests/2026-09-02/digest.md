# SciRate Daily Digest — 2026-09-02

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Depth-1 expanders on the unitary group and applications

[arXiv:2609.01605](https://arxiv.org/abs/2609.01605) · [SciRate](https://scirate.com/arxiv/2609.01605)

*Anurag Anshu, Shankar Balasubramanian, Jonas Haferkamp, Aram W. Harrow, Xinyu Tan*

**TL;DR** The authors construct a 16-element quantum expander on n qubits in which every unitary is a *depth-1* 1D circuit of Paulis/CNOTs (gap ≥ 1/(2·10⁸)), by observing that Kassabov's bounded-Kazhdan-constant generators of SL(3s;𝔽₂) map to single CNOT layers under the natural permutation representation. They then use it to build frustration-free 1D Hamiltonians with gap Θ(n⁻²) and volume-law ground-state entropy Θ(n) — i.e. S = Θ(Δ^{-1/2}), saturating the conjectured optimal frustration-free entanglement–gap tradeoff — plus a streaming test for volume-law states, and a degree-25 expander on SU(2ⁿ) whose gap is uniform in *both* the representation and the dimension.

**The big picture** Quantum expanders are small sets of unitaries that scramble any state toward the maximally mixed one as fast as truly random unitaries would, and they are workhorses for entanglement tests, complexity results, and counterexample constructions. Everyone assumed such objects need circuits of growing depth; here they are shown to exist at the absolute minimum depth — one layer of nearest-neighbour two-qubit gates on a line — by importing a known algebraic expander for invertible binary matrices. This minimal depth is what makes the construction embeddable into local one-dimensional Hamiltonians, resolving how much entanglement a frustration-free gapped chain can carry, and it also yields the first generating set for the unitary group whose mixing rate degrades neither with the moment order nor with the dimension.

**Key contributions**
- Depth-1, 1D quantum expander: 16 unitaries (6 supported on 3 qubits, 10 translation-invariant by period 3), explicit constant gap.
- A frustration-free 1D Hamiltonian family with Δ = Θ(n⁻²) and unique ground state with S = Θ(n), i.e. exponent α = 1/2 versus the previous best α ≈ 1/4 (Gottesman–Hastings) and 1/12 (Irani).
- A degree-25 expander on SU(2ⁿ) — one T, one T†, and depth-1 Clifford layers — gapped uniformly over all finite-dimensional irreps and all n; extended to all SU(d) with degree ≤5400, settling a conjecture of Lubotzky relayed by Bourgain. Gives ε-approximate k-designs in depth O(nk + log 1/ε), matching the 2^{Ω(nk)} cardinality lower bound.
- Single-pass streaming test for |Γ⟩ (and MPO-dressed variants) with O(Δ⁻¹log 1/ε) memory.
- Side results: an improved frustration-free area law S ≤ Õ(Δ_loc^{-3/4}) via Sherstov's robust polynomial AGSP; a counterexample MPO where a constant spectral gap still requires Ω(n) power iterations (so MLSI constant α ≤ log n / n).

**How it works** Under the representation g ↦ (|x⟩ ↦ |gx⟩), elementary matrices E_{i,j} of SL(n;𝔽₂) are exactly CNOTs; Kassabov's 14 generators of EL(3;Mat(s;𝔽₂)) built from the cyclic-shift A and rank-1 projector B become CNOT layers with disjoint supports, hence depth 1 after a qubit relabelling. The Kazhdan constant >1/400 gives a top-eigenvalue bound; the relation xyxyz = e among three involutive generators bounds λ_min ≥ −1+1/63. Adding single-qubit X and Z on qubit 1 promotes the CNOT design to a full quantum expander: the CNOT commutant is 5-dimensional (span of I, |0ⁿ⟩⟨0ⁿ|, |+ⁿ⟩⟨+ⁿ|, and cross terms), and X,Z shrink it, with the exact overlap (N−2)/(N−1) computed via a generalized eigenvalue determinant, then combined by the Harrow–Hastings mixing lemma. The Hamiltonian construction uses left/right chains with clock+data subchains applying U_i and U_i†, a modified Feynman–Kitaev domain-wall clock with identity padding, and a coupling term forcing maximal entanglement. For SU(2ⁿ), Aaronson–Gottesman normal form plus short-product/subgroup Kazhdan lemmas give a 23-element depth-1 Clifford generating set; convolving with the random-Pauli-rotation gap 15/16 and adding T, T† yields the uniform bound.

**Why it matters** This closes the frustration-free side of the entanglement–gap question (Conjecture: frustrated α = 1 remains open) and gives explicit, hardware-friendly design/expander constructions. The uniform-in-dimension SU(d) expander is the qualitative improvement over Bourgain–Gamburd that design theorists and free-probability/spectral-gap researchers have wanted.

**Caveats** The construction needs n = 3s (concurrent work of Liu et al. handles general n at constant rather than depth-1, on a line rather than a circle); the periodic boundary is used. Gaps are constants but tiny (≈5·10⁻⁹), and the SU(d) result inherits an unquantified κ₀ from short-product arguments. The extension of Lemma Clifford-expander to all n is stated only as an expectation. The Hamiltonian has Δ = Θ(n⁻²), not the conjectured Θ(n⁻¹) frustrated regime, and the proposed free-fermion route to amplify the gap failed due to clock-synchronization overhead. The improved area law is in terms of the *local* gap, not the spectral gap.

## 2. Verifiable quantum advantage in extremely low depth

[arXiv:2609.01448](https://arxiv.org/abs/2609.01448) · [SciRate](https://scirate.com/arxiv/2609.01448)

*Alexandru Gheorghiu*

**TL;DR** The paper constructs a single-round, classically verifiable proof of quantumness whose honest prover is a *single* shallow unitary circuit followed by one measurement layer — either log-log depth with 1- and 2-qubit gates, or constant depth with unbounded fan-in ($\mathsf{QAC}^0$). Honest quantum provers pass with probability $1-\mathrm{negl}(\lambda)$, while classical samplers running in $2^{o(\lambda)}$ time are capped at $3/4+\mathrm{negl}(\lambda)$, under a subexponential lattice-knowledge assumption plus a new "adaptive hardcore bit with carry predicates" strengthening of LWE.

**The big picture** We know shallow quantum circuits can do things classical computers apparently cannot, but until now those demonstrations were either unverifiable, verifiable only against similarly restricted classical opponents, or required the quantum device to measure mid-circuit and react to outcomes in real time. This work closes much of that gap: it gives a task where the quantum device just runs one very shallow circuit and measures once, and an ordinary classical verifier holding a secret can check the answer efficiently, with hardness against all subexponential-time classical algorithms. The price is a pair of non-standard lattice assumptions, one of which is of the "knowledge" type that cannot be efficiently falsified. If the assumptions hold, this is the shallowest known form of cryptographically verifiable quantum advantage.

**Key contributions**
- A $\mathbb{Z}_q$-ary, constant-locality randomized encoding of affine maps $\mathbf{v}\mapsto\mathbf{M}\mathbf{v}+\boldsymbol\eta$, generalizing the binary path-mask encoding of Gheorghiu (2026): two mask layers ($\mathbf{r}$ to kill input reuse across rows, $\mathbf{h}$ path masks to break each row's correction sum), with perfect privacy and unique randomness reconstruction.
- Compilation of the AGGM single-round proof of quantumness into $\mathsf{QNC}^0[\log\log]$ and exact $\mathsf{QAC}^0$, with no mid-circuit measurement or feed-forward, no random oracle, and polynomial width.
- Formulation of the *carry-predicate* adaptive-hardcore-bit assumption, with partial supporting evidence, plus a proof that it also implies key-mode indistinguishability between the claw-free and extractable modes.

**How it works** The prover superposes over branch bit, input, function noise, and both mask layers; evaluates the encoding (each symbol touches ≤3 source words, each source appears O(1) times); erases the noise register by a local reversible update (needed because the two claw branches differ in $\boldsymbol\eta$); then Hadamards and measures everything. Privacy plus randomness reconstruction collapses the post-measurement state to a two-term superposition over *extended* preimages (input, $\mathbf{r}$, $\mathbf{h}$), so the Hadamard measurement yields the usual equation $C=\mathbf{D}\cdot(\boldsymbol\zeta_0\oplus\boldsymbol\zeta_1)$. The $\mathbf{h}$-masks differ by $e_i+\sum_{j'\le j}A_{i,j'}s_{j'}$, so bitwise XORs produce *carry* terms nonlinear in the binary LWE secret (analogous to alternating-moduli "crypto dark matter") — hence the new assumption. Depth: $q$ has $L=\Theta(\log^2\lambda)$ bits, arithmetic on $L$-bit words costs $O(\log L)=O(\log\log\lambda)$; the $\mathsf{QAC}^0$ version uses Grier–Morris–Wu's exact polylog-size fan-out.

**Why it matters** It shows shallow circuits retain enough structure for *efficient white-box* verification, not just unverifiable sampling advantage, and identifies precisely which cryptographic obstacle (large modulus arithmetic) blocks a true $\mathsf{QNC}^0$ result. Relevant to anyone designing near-term verifiable-advantage or certified-randomness demonstrations.

**Caveats** Both assumptions are nonstandard: LK is non-falsifiable, and the carry-predicate AHCB is not reduced to LWE (only heuristic evidence). Neither implementation is genuinely $\mathsf{QNC}^0$ with bounded arity. Verification is private-coin/trapdoor-based; soundness gap is only $3/4$; noise robustness of the shallow circuit is not analyzed. A constant-modulus instantiation would need 2-to-1 invertible TCFs from LPN-like assumptions, which do not currently exist.

## 3. Exact learning of quantum noise with tensor networks

[arXiv:2609.00169](https://arxiv.org/abs/2609.00169) · [SciRate](https://scirate.com/arxiv/2609.00169)

*Nicola Pancotti, Vedika Saravanan, Krysta Svore*

**TL;DR** The paper recasts detector-error-model (DEM) calibration as a variational problem: fault-event probabilities are free parameters tuned by gradient descent to minimize the binary cross-entropy between a maximum-likelihood decoder's predicted logical-flip probability and the observed logical outcomes. Instantiated with an exact tensor-network decoder that yields analytic gradients, the method recovers, from a uniform initialization, noise models matching Google's independently characterized Sycamore DEM to within 2% in logical error rate on distance-3, 3-round surface-code data, and tracks synthetic drift online via warm starts.

**The big picture** Decoders only work as well as the error model they are handed, and obtaining that model normally requires dedicated characterization experiments that consume device time and go stale as hardware drifts. This work shows that the syndrome and logical-outcome records already produced by routine memory experiments contain enough information to fit the error model itself, by treating decoding performance as a training objective rather than a fixed evaluation. The authors prove the objective is not a heuristic: whatever minimizes it is the best possible decoder in an information-theoretic sense, and they demonstrate that the fitted model can be refreshed continuously as the machine changes, without pausing operation.

**Key contributions**
- A proposition establishing that the population minimizer of the cross-entropy over noise parameters is the true posterior, so a sufficiently expressive ansatz saturates the Bayes-optimal logical error rate — with the identifiability caveat that only the coset structure modulo silent faults (Hx=0, Lx=0) is recoverable.
- Analytic gradients of the loss through exact marginalization; for independent-fault ansätze the derivative reduces to a difference of two clamped logical-class probabilities.
- A tensor-network construction of the full pipeline (Tanner graph → copy tensors in the computational and ± bases, Hadamards on bonds, noise tensor attached to error legs, logical observable as an extra check row) that is exact and end-to-end differentiable.
- Empirical demonstration on Sycamore-derived DEMs and an online warm-started drift-tracking protocol.

**How it works** Syndrome legs are clamped, error legs contracted with |+⟩, and the free logical leg returns the two-component vector p(s,ℓ); the normalized ratio is the decoder's prediction. Training uses SGD, 500 iterations, 30k shots per batch, uniform initialization. Drift is modeled as Brownian motion in logit space (σ = 0.2, 0.3, 20 steps, 5 seeds); each step re-optimizes from the previous parameters and tracks the perfect-knowledge baseline closely.

**Why it matters** In-situ, decoder-integrated calibration removes a recurring experimental overhead and could feed real-time decoding pipelines with continuously refreshed weights, flagging when full recalibration is due. Relevant to QEC experimentalists, decoder developers, and anyone building noise-aware error mitigation.

**Caveats** Data are sampled *from* the characterized DEM, not raw hardware shots, so model misspecification on real devices is untested. Only distance 3 with 3 rounds; exact contraction cost is exponential in treewidth, and the proposed scalable extensions (approximate contraction, matching/BP/neural forward passes) are explicitly not demonstrated. Despite the correlated-noise claim, only an independent-fault ansatz is fit. The loss is non-convex in θ, learned parameters are decoder- and task-biased, and generalization beyond memory experiments to logical gates is not shown.

## 4. High-Rank Encoding Can Improve Approximate Quantum Error Correction

[arXiv:2609.00778](https://arxiv.org/abs/2609.00778) · [SciRate](https://scirate.com/arxiv/2609.00778)

*Bikun Li, Liang Jiang*

**TL;DR** The authors prove that for approximate QEC judged by entanglement fidelity, restricting the encoder to a partial isometry (pure logical → pure code states) can be strictly suboptimal, and they exhibit an explicit noise family — one logical qudit into two, with maximally mixed input — in which *every* optimal encoder has Choi rank ≥ d_L, maps pure logical states to mixed code states, and has entropy exchange log₂d_L, even arbitrarily close to perfect recovery. They also sharpen the Barnum–Knill–Nielsen rounding bound from Δ ≤ ε(1−ε) to a quadratic Δ ≤ (s⁻¹−1)ℓ_s(ε)² near ε→0, and show the optimized gap for their family saturates this ceiling asymptotically.

**The big picture** Almost all quantum codes are built so that each logical state is stored as a definite, pure physical state. It has been an open question whether this convention costs anything when perfect correction is impossible and one only asks for the best achievable fidelity. The answer here is yes: there exist noise processes for which the best possible encoding is intrinsically randomizing — the encoder must scramble a pure logical input into a mixed physical state — and no deterministic pure-state encoding can match it. The advantage is small but provably nonzero, survives small changes to the noise, and persists even in the near-perfect-correction regime, so it is not a fine-tuned artifact.

**Key contributions**
- A state-dependent rounding theorem: for any CPTNI encoder, fixed noise and decoder, one can construct a partial-isometry encoder losing at most (s⁻¹−1)ℓ_s(ε)² infidelity (s = smallest positive eigenvalue of the input state), quadratic near ε=0 with coefficient (s⁻¹−1)/4; tighter than the prior ε(1−ε) estimate at both small and large ε, and valid for CPTNI as well as CPTP.
- Lipschitz stability: |Δ_opt(N) − Δ_opt(N′)| ≤ 2‖N−N′‖_◇ (constant 1 for CPTP), so a positive gap is open in diamond norm.
- An explicit unital, U(d)-covariant channel family N_p with a certified global optimum F_opt = λ₁ = 1 − p/(d_L²−2), whose optimal encoder–decoder pairs are unique up to a logical unitary and necessarily high-rank for all p ∈ (0,1).
- Exact asymptotic gap coefficient κ = ((d_L−1)/4)·((d_L²−2)/(d_L²−1))², approaching the universal ceiling as d_L grows.
- The optimal encoder is an extreme point of the CPTP set (Choi's criterion), so the gain is genuine quantum encoder randomness, not a classical mixture — consistent with the objective being linear in the encoder's Choi matrix.

**How it works** The rounding proof picks the best Kraus branch of the encoder, polar-decomposes it, and converts a second-moment fidelity estimate into a first-moment one using ρ ⪰ sΠ_ρ. For the example, a dual certificate Z_p = λ₁I − J(N_p†) ⪰ 0 upper-bounds F_e(τ, D∘N_p∘C) by λ₁, saturated exactly when the composite B = C∘D is trace-preserving with support in ker Z_p; linear independence of the blocks (Q_p²)_{ij} makes this solution unique, forcing rank[B(I_C)] = d_L² and hence encoder rank ≥ d_L. The exact κ comes from rewriting the rank-one gap as a residual norm on a product of Stiefel manifolds, using the U(d_L)³ symmetry to reduce to a single canonical perfect pair, and computing the tangent-space minimum.

**Why it matters** It settles a structural question underlying essentially all code constructions: the pure-in/pure-out encoding convention is not without loss of generality for AQEC. This bears on how one should parametrize encoders in numerical biconvex encoder–decoder optimizations (which have historically found rank-one optima), and suggests encoder Choi rank as a possible resource-theoretic quantity. Of practical comfort, the penalty is at most quadratic in infidelity, so conventional codes lose little near good recovery.

**Caveats** The figure of merit is entanglement fidelity at a *fixed* input (the maximally mixed state), not worst-case or average pure-state fidelity; ε and the gap ~ ((d_L−1)/4)ε² are both small near p→0, so the advantage is second-order. The noise channel is reverse-engineered from the desired certificate rather than physically motivated, and requires d_C = d_L² and the fully mixed logical input; no criterion is given for which realistic noise favors high-rank encoding. Higher-order corrections to the gap at finite p are not determined, the analysis is finite-dimensional, and the general claim is existence, not a characterization.

## 5. A nonabelian anyon violates Haag duality

[arXiv:2609.01267](https://arxiv.org/abs/2609.01267) · [SciRate](https://scirate.com/arxiv/2609.01267)

*Daniel Wallick, Henrik Wilming*

**TL;DR** The authors prove that the ground state describing a single *nonabelian* anyon in a 2D topologically ordered spin system violates Haag duality for cone regions — equivalently, it violates uniqueness of purifications. The proof is a sector-theoretic dichotomy: for an irreducible superselection sector localized in a cone, the induced net of von Neumann algebras satisfies Haag duality *if and only if* the sector is abelian. Since a nonabelian anyon state is a gapped ground state of a commuting-projector (Levin–Wen) Hamiltonian, this disproves the conjecture that all gapped ground states obey *approximate* Haag duality, and — because approximate Haag duality is a phase invariant — exhibits gapped phases where Haag duality fails everywhere.

**The big picture** In systems with infinitely many degrees of freedom, a basic rule of finite quantum mechanics can break: two global pure states that look identical to one party need not be related by an operation performed only by the other party. This paper shows that the presence of a single quasiparticle with nonabelian exchange statistics is by itself enough to break that rule, even when the two regions in question are topologically trivial. Because the relevant algebraic condition is stable across a whole gapped phase of matter, it also identifies entire families of gapped systems where the standard locality axiom used in algebraic quantum field theory and in rigorous studies of topological order simply cannot hold — which in turn suggests the condition is a useful criterion for selecting "genuine vacuum" phases.

**Key contributions**
- A one-paragraph physical argument: split a non-vacuum charge off the nonabelian anyon, transport it into region A; the reduced state on B is unchanged, but any unitary in A commutes with a topological-charge projector that separates the two states, forcing zero overlap.
- A rigorous, model-independent theorem (DHR-style, adapting Doplicher–Haag–Roberts Lem. 2.2 to spin systems via Buchholz–Fredenhagen auxiliary algebras): assuming vacuum Haag duality, an anyon sector's net satisfies Haag duality ⟺ the sector is invertible/abelian.
- Concrete instantiation in Levin–Wen string-net models, using the recent classification of infinite-volume anyon sectors via infinite-depth string circuits and skein modules, plus the recently established vacuum Haag duality.
- Failure of quantum steering: a conditional expectation exists but fails the state-invariance condition exactly when the anyon is nonabelian, so pure-state steering is lost too.
- Failure of approximate Haag duality, disproving a standing conjecture and hence showing Haag duality fails at every point of certain gapped phases; noted analogy with violation of entanglement-bootstrap axiom A1 via topological entanglement entropy corrections.

**How it works** Sector-theoretically, a cone-localized sector ρ extends to normal maps ρ_Λ on R(Λ). Haag duality for the anyon net reduces to ρ_Λ(R(Λ)) = R(Λ), i.e., ρ_Λ being an automorphism, which is equivalent to ρ having an inverse under fusion — abelianness. The converse builds a candidate conjugate by extending ρ_Δ^{-1} to the auxiliary algebra and verifies transportability using zig-zag/interpolating cone sequences.

**Why it matters** Haag duality underlies rigorous derivations of the braided fusion category from a ground state, and is now central to discussions of non-invertible symmetries and entanglement structure. This result delimits where those tools apply and clarifies that superselection-sector states, though gapped and pure, are algebraically distinguishable from vacua.

**Caveats** The physical argument assumes RG fixed points with strictly localizable anyons and adiabatic transport without residual excitations; the general theorem assumes vacuum Haag duality, cone regions, dualizable sectors, and properly infinite algebras. It is still open whether approximate Haag duality is strictly weaker than Haag duality, and whether the claim that abelian-sector phases coincide with vacuum phases holds in general. Extension to nonabelian quantum doubles is stated as expected, not proven.
