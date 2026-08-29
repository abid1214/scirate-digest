# SciRate Daily Digest — 2026-08-29

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Tight Bounds for Purity and Product Testing from Partial Transposition

[arXiv:2608.27217](https://arxiv.org/abs/2608.27217) · [SciRate](https://scirate.com/arxiv/2608.27217)

*Oren Akresh, Jacob Beckey*

**TL;DR** The authors give an elementary proof that any PPT-BOTH measurement (a relaxation containing all adaptive single-copy protocols) distinguishing $n$ copies of a Haar-random pure state from the maximally mixed state has bias at most $n(n-1)/2d$, implying $n=\Omega(\sqrt d)$ for purity testing. The same telescoping-plus-partial-transpose argument gives bias $O(n^2/d)$ for bipartite product testing, hence $\Omega(\sqrt d)$ — quadratically and quartically stronger, respectively, than the previous PPT bounds ($\Omega(d^{1/4})$, $\Omega(d^{1/8})$) obtained via approximate orthogonality of permutation operators, and matching known nonadaptive single-copy upper bounds.

**The big picture** Learning properties of an unknown quantum state is far cheaper if you can measure many copies jointly, but real experiments mostly measure one copy at a time, possibly adapting each measurement to earlier outcomes. Proving that such adaptive strategies genuinely need many samples is technically painful, so people often relax to a larger, mathematically friendlier class of measurements — at the risk of proving something too weak. This work shows that for two canonical tasks — deciding whether a state is pure, and whether a bipartite state is unentangled — the relaxation costs nothing asymptotically, and the resulting proofs are short enough to fit on a page.

**Key contributions**
- Bias bound $|\mathrm{tr}[M(\sigma^{(n)}-\tau_d^{\otimes n})]|\le n(n-1)/2d$ for all PPT-BOTH $M$, valid for *all* $d,n\ge 2$ (no Schur–Weyl stable-regime restriction $d\gg n$).
- Tight $\Omega(\sqrt d)$ PPT lower bound for purity testing, saturated by nonadaptive single-copy protocols; first tasks where PPT relaxation preserves optimal dimension dependence.
- $\varepsilon$-dependent version: $\Omega(\sqrt{d/\varepsilon})$, recovering the learning-tree result of Gong–Aaronson-style analyses without martingale machinery.
- $O(n^2/d)$ bias for $k=2$ product testing, upgrading Harrow's $\Omega(d^{1/8})$ to the optimal $\Omega(\sqrt d)$.

**How it works** Write $\Delta=\sigma^{(n)}-\tau_d^{\otimes n}$ as a telescoping sum of "single-depolarization" operators $\mathcal D_m(\sigma^{(m)})=\sigma^{(m)}-\sigma^{(m-1)}\otimes\tau_d$. Since $\mathrm{tr}[XY]=\mathrm{tr}[X^{\Gamma_S}Y^{\Gamma_S}]$ and PPT-BOTH guarantees $0\preceq M^{\Gamma_m}\preceq\mathbb I$, the bias is bounded by $\tfrac12\sum_m\|\mathcal D_m(\sigma^{(m)})^{\Gamma_m}\|_1$. Splitting $\Pi_m$ into permutations fixing site $m$ versus transpositions $(im)$, and using $P_d((im))^{\Gamma_m}=d\,\psi_{i,m}$, gives $\Pi_m^{\Gamma_m}=\tfrac1m A_m(\mathbb I+d\Psi_m)$ with $[A_m,\Psi_m]=0$, so trace norms reduce to traces: $\tfrac12\|\cdot\|_1\le (m-1)/(d+m-1)$. Product testing decomposes $\rho_{\rm prod}^{(n)}-\rho_{\rm far}^{(n)}$ through $\tau_{d^2}^{\otimes n}$, applying the lemma on Alice's and Bob's symmetric-subspace factors separately.

**Why it matters** Provides a cheap, symmetry-based alternative to learning-tree lower bounds, useful wherever adaptivity blocks tree analyses; and shows PPT is a *sharp* proxy for adaptive single-copy measurements in these settings. Relevant to shadow-tomography practitioners and to complexity theorists, since efficient LOCC product testing would collapse QMA(2)=QMA.

**Caveats** Product testing is only handled for $k=2$ and constant $\varepsilon$; no $\varepsilon$-dependence tracked there. The PPT model treats each bipartite copy as one register, so it does not constrain LOCC *within* a copy. Tightness is asymptotic in $d$ only. Stabilizer testing remains open. Also flagged: ChatGPT was used as a stated "research collaborator" in deriving/refining results.

## 2. Conditional contraction coefficients and their applications to quantum networks

[arXiv:2608.27171](https://arxiv.org/abs/2608.27171) · [SciRate](https://scirate.com/arxiv/2608.27171)

*Christoph Hirche, Ian George, Theshani Nuradha, Mark M. Wilde*

**TL;DR** The authors introduce *conditional* contraction coefficients, which handle arbitrary quantum reference systems by subtracting the divergence already present in the reference marginals, removing the "equal marginals" restriction of complete contraction coefficients. Their central result is an exact identity: the conditional contraction coefficient of the Umegaki relative entropy equals the contraction coefficient of conditional mutual information, with a binary classical register sufficing for the optimization. They also prove trace-distance optimization reduces to orthogonal states, establish tensorization for CMI-based SDPI constants, and derive a quantum Polyanskiy–Wu network bound, a "replacing time" notion, and quantum-memory limits.

**The big picture** When noise acts on part of a system, how much of the correlation with the rest of the world survives? The standard tools for answering this ignore side information entirely, and the existing quantum fix requires the two states being compared to look identical outside the noisy subsystem — a restriction rarely met in practice. This work defines a coefficient that credits back whatever distinguishability lives purely in the side system, and shows it coincides exactly with how much conditional correlation a channel destroys. That makes it the right figure of merit for networks, distributed protocols, memory lifetimes, and mixing arguments where entanglement with a reference is unavoidable.

**Key contributions**
- New family: conditional contraction/expansion coefficients, conditional SDPI constants, and relative (two-channel) versions, all built from the "conditional divergence" $\mathbb{D}_A(\rho_{RA}\|\sigma_{RA})=\mathbb{D}(\rho_{RA}\|\sigma_{RA})-\mathbb{D}(\rho_R\|\sigma_R)$, with the ordering $\eta_\mathbb{D}\le\eta^p_\mathbb{D}\le\eta^c_\mathbb{D}\le\eta^\wedge_\mathbb{D}\le1$.
- Exact identity $\eta^\wedge_D(\mathcal{N})=\eta_{\mathrm{CMI}}(\mathcal{N})=\eta_{\mathrm{cqCMI}}=\eta_{\mathrm{2cqCMI}}$; a parallel result identifies $\eta^c_D$ with a marginal-constrained "MIR" quantity, and $\eta^p_D=\eta_{\mathrm{MI}}$, completing a four-column dictionary between divergence- and correlation-based contraction.
- Doeblin bound $\eta^\wedge_\mathbb{D}(\mathcal{N})\le 1-\alpha_+(\mathcal{N})$ for any jointly convex divergence — strictly stronger than prior complete-coefficient bounds, and recovering a known CMI bound.
- Trace-distance reduction to orthogonal inputs; an explicit classical example with $\eta^\wedge_{E_\gamma}>\eta^c_{E_\gamma}$, proving the hierarchy is strict.
- Tensorization of $\eta_{\mathrm{MI}}$ and $\eta_{\mathrm{CMI}}$ SDPI constants (notable since general quantum SDPI tensorization fails), plus approximate tensorization for relative entropy with exact results for generalized depolarizing channels at their fixed points.
- Applications: quantum Polyanskiy–Wu bound $\eta_{\mathrm{MI}}(\mathcal{R}\circ\mathcal{M})\le\eta_\mathcal{R}\eta_{\mathrm{MI}}(\mathcal{M}_{A\to BD})+(1-\eta_\mathcal{R})\eta_{\mathrm{MI}}(\mathcal{M}_{A\to B})$; "replacing time" as a reference-aware generalization of mixing time, shown asymptotically equivalent to mixing.

**How it works** The main equivalence theorem is a perturbation argument: embed $\rho_{RA}$ and $\sigma_{RA}$ in a binary classical-quantum family $\rho_{URA}$ with $\lambda$-weighted branches whose marginal is $\sigma_{RA}$, use the direct-sum property to expand $\eta I(U:B|R)-I(U:B'|R)$, and note that this function vanishes at $\lambda=0$, so its derivative must be nonnegative; the vanishing-derivative property of relative entropy kills the residual terms, leaving exactly the conditional-divergence inequality. The converse directions are immediate from direct-sum and from identifying $R'C\leftrightarrow R$, $\rho_C\otimes\rho_{R'A}\leftrightarrow\sigma_{RA}$. The Doeblin bound uses the erasure-degradability decomposition $\mathcal{N}=(1-\epsilon)\mathcal{D}+\epsilon\mathcal{R}_\tau$ plus convexity.

**Why it matters** CMI contraction governs distributed and network settings, recovery maps, and Markov-chain-like structures; having it equal a divergence-based coefficient makes it amenable to the whole SDPI toolbox (concatenation, convexity, SDP-computable Doeblin bounds). Relevant to anyone working on quantum Markov semigroups, memory lifetimes, differential privacy, or capacity bounds.

**Caveats** Whether $\eta_{\mathrm{MI}}=\eta^c_D$ remains open (only $\le$ is proven), and $\eta_{\mathrm{MI}}$ is shown to differ from ordinary relative-entropy contraction. Relative-entropy tensorization results are only approximate outside special cases. The optimizations still range over unbounded references (though the binary-$U$ reduction helps materially), expansion-coefficient analogues are frequently trivially zero, and the key equivalence leans on the direct-sum property plus the vanishing-derivative property, limiting the divergences to which it extends.

## 3. Lieb-Schultz-Mattis Constraints for Quantum Channels: A Spacetime-Duality View

[arXiv:2608.26266](https://arxiv.org/abs/2608.26266) · [SciRate](https://scirate.com/arxiv/2608.26266)

*Sarang Gopalakrishnan, Yu-Jie Liu, Tsung-Cheng Lu, Frank Pollmann, Yizhi You*

**TL;DR** The authors show that a repeated $d$-dimensional quantum channel carrying a mixed anomaly between a strong symmetry $S$ and a weak symmetry $G$ (an LSM-type constraint) is spacetime-dual to a $(d{+}1)$-dimensional mixed-state SPT, with the channel's time direction becoming a spatial direction. Under this map, temporal correlations of the channel — captured by a newly defined twisted Rényi-$N$ correlator — become the mSPT's strange correlator, and the singular-value spectrum of the channel transfer matrix $Q$ becomes the mSPT's operator entanglement spectrum. The upshot is that the *singular* spectrum of the Liouvillian, not its eigenvalue spectrum, is the sharp anomaly diagnostic.

**The big picture** In closed systems, anomalies forbid a featureless gapped ground state. Extending this logic to noisy, dissipative systems has been hampered by the fact that the usual spectral diagnostics — degeneracy or gaplessness of the dissipative generator — are already forced by symmetry and probability conservation alone, even with no anomaly at all. This work supplies a genuinely sharp replacement by rotating time into space: repeated application of a noisy evolution is reinterpreted as a higher-dimensional mixed-state topological wavefunction, so anomaly constraints on the dynamics become boundary-anomaly constraints on that wavefunction. The payoff is a concrete, measurable statement that anomalous open-system dynamics must retain long-lived temporal correlations rather than relaxing to something trivial.

**Key contributions**
- Explicit spacetime duality dictionary (Table I): channel time evolution ↔ mSPT transfer matrix under bulk projection; input/steady states ↔ mSPT spatial boundaries; strong/weak channel symmetries ↔ strong/weak mSPT symmetries.
- The twisted Rényi-$N$ correlator $C(N)=\Tr[O^\dagger Q^N O Q^N]/\Tr[Q^{2N}]$ as a temporal probe, proved dual to the mSPT strange correlator.
- Proposition I: for a spin-1/2 chain channel with strong $SO(3)$ and weak translation, $C(N)$ cannot decay exponentially — it is $\mathcal{O}(1)$ or $\sim N^{-\alpha}$.
- Identification of the *Liouvillian singular spectrum* (eigenvalues of $Q^\dagger Q$) as the anomaly-sensitive object, dual to operator entanglement of the mSPT; it cannot have a unique dominant singular vector.

**How it works** A single channel step is Choi-vectorized and Stinespring-dilated; the $t\!\leftrightarrow\!y$ rotation turns the input/output/ancilla into three wires of a ladder column. Identity evolution maps to inter-column EPR pairs; each column $L_i\oplus R_i$ carries conjugate $SO(3)$ representations and is anomaly-free, while dangling boundary wires retain the LSM anomaly — the standard coupled-wire route to a 2d SPT protected by $SO(3)\times T_x$. Entangling ancillas via a symmetric local unitary and tracing them yields an mSPT (MPO form given); projecting bulk columns onto onsite EPR pairs re-stitches the blocks into $N$ channel steps, with the two spatial edges realizing $|\rho_0\rangle\rangle$ and $|\mathcal{E}^N[\rho_0]\rangle\rangle$. Contraction with a trivial reference product state reproduces $\Tr[Q^N]$, making the strange-correlator/TRNC correspondence explicit.

**Why it matters** It resolves a genuine ambiguity in the open-system LSM literature — that Liouvillian gaplessness/degeneracy is generic for strongly symmetric CPTP maps — and replaces it with a diagnostic tied to operator entanglement, which is accessible in tensor-network simulation and, in principle, in replica-based experimental protocols. Relevant to anyone working on mixed-state phases, decoherence-induced SPT, or dissipative quantum simulation.

**Caveats** The construction assumes a strictly local, time-independent (stroboscopically repeated) channel with a translation-invariant product-state ancilla; the TRNC is a Rényi-$N$ (replica) quantity, so its experimental cost and its status under different Rényi indices deserve scrutiny. The bound is one-sided — it forbids exponential decay but does not distinguish among symmetry-breaking outcomes (including strong-to-weak SSB, deferred to appendices). Numerical support for the singular-spectrum claim is promised in Sec. III but the source here is truncated before those results, and generalizations beyond $SO(3)\times T_x$ are stated rather than developed in the visible text.

## 4. Quantum cellular automata and invertible phases of matter

[arXiv:2608.26456](https://arxiv.org/abs/2608.26456) · [SciRate](https://scirate.com/arxiv/2608.26456)

*Corey Jones, Nikita Sopenko, Ryan Thorngren*

**TL;DR** Working with quasi-local algebras whose on-site von Neumann algebras are infinite-dimensional type I factors, the authors prove that quantum cellular automata modulo circuits, invertible states modulo phase equivalence, and a Brauer group of invertible quasi-local algebras one dimension down are all the *same* abelian group. They use this to build a K-theoretic Ω-spectrum realizing Kitaev's conjecture, and to construct explicit nontrivial invertible states and QCA on the 2d lattice from the chiral Majorana and (E₈)₁ conformal nets.

**The big picture** Two classification programs for short-range-entangled quantum matter — one based on states, one based on strictly locality-preserving dynamics — have long been known to disagree: some automata act trivially on states, and some chiral phases (like a p+ip superconductor) are believed unreachable by any automaton. The paper shows this mismatch is an artifact of insisting on finitely many degrees of freedom per site; allowing infinitely many per site makes the two classifications coincide exactly, and simultaneously identifies both with an algebraic invariant living on the boundary. Chiral conformal field theories then supply the first explicit nontrivial examples in two spatial dimensions, and the framework suggests a criterion for when a continuum field theory can be put on a lattice at all.

**Key contributions**
- Theorem A: QCA(X×ℤ) ≅ Br(X) ≅ IP(X×ℤ) for any uniformly locally finite metric space X, bosonic and fermionic (super) versions in parallel.
- A new **boundary quasi-local algebra** attached to an invertible state — a rigorous bulk-boundary correspondence — giving IP ≅ Br (the QCA ≅ Br half generalizes Haah's invertible subalgebras).
- Theorem B: K-theory of the symmetric monoidal category of invertible quasi-local algebras with bounded-spread isomorphisms yields Kᵢ = IP(ℤ^{d−i}) for 0 ≤ i ≤ d, K_{d+1} = ℝ/ℤ, zero above — an algebraic model of the Kitaev Ω-spectrum.
- Theorem C/Corollary D: discretized c=1/2 Majorana and (E₈)₁ nets are invertible and Brauer-nontrivial, so Br(ℤ) ≅ IP(ℤ²) ≅ QCA(ℤ²) ≠ 0.
- Theorem E ("extended split property"): the Longo–Rehren extension of any rational conformal net discretizes to Mat(ℤ), so holomorphic nets are invertible.

**How it works** Quasi-local algebras are nets of separable von Neumann superalgebras over bounded subsets, with morphisms locally normal bounded-spread homomorphisms; invertibility means A ⊗ Ã ≅ Mat(X) = ⊗ B(ℋ). Functoriality under the coarse category makes discretization of continuum nets canonical. The isomorphisms are assembled from four maps: boundary algebra of a QCA, generalized shift, boundary algebra of a state, and QCA-applied-to-product-state. Technical machinery includes a super Ge–Kadison tensor-splitting lemma (via Klein transform) and a super slice-map property.

**Why it matters** It removes the QCA/state discrepancy, shows chiral (c₋ ≠ 0) phases admit commuting — though unbounded — local Hamiltonians and zero-correlation representatives once infinite-dimensional ancillas are allowed, and provides operator-algebraic invariants distinguishing 2d chiral phases. Relevant to topological-phase classification, QCA theory, and AQFT.

**Caveats** The conjecture Br(ℤ) ≅ ℤ generated by E₈ is unproven; nontriviality is established here only via the orbifold-anomaly/central-charge link (c not divisible by 3), with the general c ≠ 0 case deferred to future work. Whether conjecturally nontrivial 3d finite-dimensional QCA trivialize after stabilization is open. The extended split property is proved only for (1+1)d free fermions and rational diagonal CFTs; higher dimensions are conjectural. Invertible states are assumed strictly zero-correlation. Physical relevance of infinite-dimensional on-site Hilbert spaces is a modeling choice.

## 5. Randomness can be certified in energy-constrained semi-device-independent scenarios

[arXiv:2608.27357](https://arxiv.org/abs/2608.27357) · [SciRate](https://scirate.com/arxiv/2608.27357)

*Shashank Kumar Ranu, Lewis Wooltorton, Alastair A. Abbott, Omar Fawzi*

**TL;DR** The authors adapt the NPA hierarchy to energy-constrained prepare-and-measure scenarios in which the preparation and measurement devices may share arbitrary pre-distributed entanglement, obtaining the first *certified* (as opposed to heuristic seesaw) upper bounds on the adversary's guessing probability. The resulting min-entropy bounds are strictly positive for energy parameter ω ≲ 0.18 with no dimension assumptions at all (and ω ≲ 0.27 assuming a qubit source), settling affirmatively the open question of whether randomness can be certified against a fully quantum adversary in this setting.

**The big picture** Semi-device-independent random number generators based only on an energy (mean photon number) bound are attractive because they avoid both full device characterization and loophole-free Bell tests. But existing security proofs quietly assumed the preparation and measurement boxes share only classical correlations; recent work showed an eavesdropper who pre-distributes entanglement between them mounts strictly stronger attacks, invalidating those rates and leaving it unclear whether any randomness survives. This paper supplies a rigorous, dimension-free lower bound on the extractable randomness in the presence of such attacks, showing the answer is yes at low enough energies, and thereby restores a security foundation for a class of already-implemented fast QRNGs.

**Key contributions**
- First certified (not heuristic) lower bounds on min-entropy for the energy-constrained PM scenario with entangled devices.
- A technique for handling a measurement acting jointly on message system S and the device's entangled share M, where the energy constraint touches only S: block-decompose the POVM in a basis of S so the blocks act on M alone and commute with S-operators.
- A dimension-independent treatment of projectivity: retain the k=2 ground/excited subspace explicitly, lump all higher blocks into one auxiliary operator F, and impose only the "sandwich" relations O₁FO₂=0 plus moment-level N²=N, none of which reference d.
- Certified outer bounds on the maximal entanglement-assisted correlator I_corr(ω), narrowing the achievable-correlation set from above.
- Noise robustness: at ω=0.05 randomness persists down to ~58% of the ideal correlator; at ω=0.1 down to ~79%.

**How it works** Bob's projective POVM on SM is written as Π^b = Σ|s₁⟩⟨s₂|⊗Π^b_M[s₁,s₂]; keeping the {|0⟩,|1⟩} blocks A,B,C plus P,Q,T on S and dumping the rest into F yields N = PA + TB + T†B† + QC + F. Two moment matrices Γ⁰, Γ¹ (one per input) are built over {I,P,T,T†,Q,A,B,B†,C,F,Z} at NPA level ℓ=2 (needed since the objective ⟨I−N−Z+2NZ⟩₀ has degree-3 monomials). Alice's channel acting only on P gives no-signalling moment equalities ⟨O⟩₀=⟨O⟩₁ for all ME-monomials up to degree 2ℓ, linking the two matrices; the energy constraint is the linear condition ⟨P⟩_x ≥ 1−ω and the test statistic is 2⟨N⟩₀−2⟨N⟩₁ ≥ I_corr^exp, set to the classical-correlation maximum 4√(ω(1−ω)). Projectivity is enforced via localizing-matrix equalities ⟨O₁(N²−N)O₂⟩_x = 0, truncated to O₁,O₂ ∈ {I,P,Q,T,T†} (a conservative relaxation). Implemented in ncpol2sdpa + MOSEK.

**Why it matters** Practitioners deploying MHz–GHz photonic SDI QRNGs based on vacuum-overlap assumptions now have a security statement valid against the strongest known attack model, including unbounded-dimension side information. The block-decomposition trick is a reusable tool for any semi-DI setting where a constraint applies to a subsystem the measurement does not factorize over.

**Caveats** A substantial gap remains: certified rates vanish at ω≈0.18 (dimension-free) while seesaw attacks still permit positive entropy up to ω≈0.32 — part slack, part genuinely stronger attacks, unresolved. Bounds hold for arbitrarily large but *finite* dimension; the infinite-dimensional (true photonic) case is open. Analysis is single-round/i.i.d. min-entropy only; finite-round security and von Neumann rates (via Brown–Fawzi–Fawzi, suggested but not done) are future work. Only ℓ=2 and k=2 were computationally accessible.
