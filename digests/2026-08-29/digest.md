# SciRate Daily Digest — 2026-08-29

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Tight Bounds for Purity and Product Testing from Partial Transposition

[arXiv:2608.27217](https://arxiv.org/abs/2608.27217) · [SciRate](https://scirate.com/arxiv/2608.27217)

*Oren Akresh, Jacob Beckey*

**TL;DR** The authors prove that any PPT-BOTH (positive under partial transposition on every subset of copy registers) two-outcome measurement distinguishing *n* copies of a Haar-random pure state from *n* copies of the maximally mixed state achieves bias at most n(n−1)/2d, giving an Ω(√d) sample lower bound for purity testing — quadratically stronger than Harrow's Ω(d^{1/4}) and matching the learning-tree bound. The same telescoping argument gives bias O(n²/d) for bipartite product testing, improving Ω(d^{1/8}) to the optimal Ω(√d), and both bounds are saturated by known nonadaptive single-copy protocols.

**The big picture** Learning properties of an unknown quantum state is far cheaper if you can measure several copies jointly, but experiments almost always measure one copy at a time, possibly choosing each measurement based on earlier outcomes. Proving that such adaptive one-copy strategies genuinely need many samples is technically hard, so people often enlarge the strategy class to a mathematically convenient superset — at the risk of proving something much weaker than the truth. Here it is shown that, for testing whether a state is pure and for testing whether a bipartite state is unentangled, this convenient relaxation costs nothing asymptotically: the resulting bounds already match what the best single-copy algorithms achieve, and the proof uses only elementary symmetry facts rather than heavy statistical machinery.

**Key contributions**
- Tight PPT-BOTH bias bound |tr[M(σ⁽ⁿ⁾ − τ_d^⊗n)]| ≤ n(n−1)/2d for all d, n ≥ 2, hence Ω(√d) purity testing (and estimation) lower bound.
- ε-dependent version: Ω(√(d/ε)) samples, recovering Gong et al.'s learning-tree result.
- Ω(√d) for two-party product testing under PPT-BOTH, a quartic improvement over Harrow's Ω(d^{1/8}), matching the tree-formalism bound and the O(√d) nonadaptive algorithm of Beckey et al.
- First examples where the PPT relaxation of adaptive single-copy measurements preserves optimal dimension dependence; no requirement d ≫ n (unlike approximate-orthogonality arguments).

**How it works** Write Δ = σ⁽ⁿ⁾ − τ_d^⊗n as a telescoping sum of "single-depolarization" terms D_m(σ⁽ᵐ⁾) = σ⁽ᵐ⁾ − σ⁽ᵐ⁻¹⁾⊗τ_d tensored with maximally mixed registers. Using tr[XY] = tr[X^Γ Y^Γ] and the fact that PPT-BOTH forces M^{Γ_m} to be a valid effect, the bias is bounded by ½Σ‖D_m(σ⁽ᵐ⁾)^{Γ_m}‖₁. Expanding Π_m by isolating the last site gives Π_m = (1/m)(Π_{m−1}⊗I)(I + Σ_i P((im))); partial transposition maps each transposition to d·(maximally entangled projector) Ψ, and [Π_{m−1}⊗I, Ψ_m] = 0 makes the product positive, yielding ½‖·‖₁ ≤ (m−1)/(d+m−1). Product testing follows by a bipartite telescoping in which Alice's and Bob's symmetric-subspace states are depolarized separately, plus triangle inequality against τ_{d²}^⊗n (where the purity bound with d → d² contributes only O(n²/d²)).

**Why it matters** Provides a simple, dimension-restriction-free toolkit for adaptive single-copy lower bounds, relevant to shadow-tomography-style separations, mean-field certification, and the QMA(2) question (an efficient LOCC product tester would collapse QMA = QMA(2)). The elementary proof also makes the tightness of the PPT relaxation itself interesting: it is not always loose.

**Caveats** Product testing is handled only for k = 2 and constant ε (the "far" ensemble relies on Haar concentration of the largest Schmidt coefficient, valid for large d); no ε-dependent product-testing bound is given. The bounds are asymptotic-order statements — PPT and LOCC may still differ in constants or in other tasks. Whether the technique extends to stabilizer testing, where it currently falls short of the optimal Ω(n), remains open, and the ε-dependent purity bound's optimality in ε is not established beyond matching prior work.

## 2. Conditional contraction coefficients and their applications to quantum networks

[arXiv:2608.27171](https://arxiv.org/abs/2608.27171) · [SciRate](https://scirate.com/arxiv/2608.27171)

*Christoph Hirche, Ian George, Theshani Nuradha, Mark M. Wilde*

**TL;DR** The paper introduces *conditional* contraction coefficients, which admit an arbitrary quantum reference system but subtract off the distinguishability already present in that reference, thereby avoiding the triviality of naive tensor-extended coefficients without imposing the equal-marginal restriction of complete contraction coefficients. The main structural result is that for Umegaki relative entropy this coefficient coincides exactly with the contraction coefficient of the conditional mutual information (and it suffices to take a *binary classical* system in the CMI optimization), completing a four-way ladder of coefficients (no reference / product reference / equal marginals / arbitrary marginals) matched to (cq-MI / MI / MI-with-reference / CMI).

**The big picture** Data processing says noise can only destroy distinguishability; contraction coefficients quantify how much is destroyed, and they underpin bounds on mixing times, memory lifetimes, privacy, and capacities. Existing versions either ignore side information entirely or artificially force the two compared states to look identical on the side system, which is unnatural in networks where correlations are distributed. This work supplies a version that handles arbitrary side information by crediting the distinguishability the side system already carries, and shows it is exactly the right quantity to describe contraction of conditional correlations, with clean composition, tensorization, and network bounds.

**Key contributions**
- Definition of conditional contraction coefficients, conditional SDPI constants, conditional expansion coefficients, and relative (channel-vs-channel) versions; ordering η ≤ η^p ≤ η^c ≤ η^cond ≤ 1.
- Equivalence theorem: η^cond_D = η_CMI = η_cqCMI = η_2cqCMI; parallel theorem giving η^c_D = η_MIR (MI with a reference having product CR marginal); and η^p_D = η_MI.
- Improved Doeblin bound: η^cond_𝔻(N) ≤ 1 − α₊(N) for any jointly convex divergence — strictly stronger than prior complete-coefficient bounds; recovers a known CMI bound as a corollary.
- Trace-distance conditional coefficient is attained by orthogonal state pairs; explicit (classical) example with η^cond_{E_γ} > η^c_{E_γ}, showing the notions genuinely differ.
- Tensorization of the CMI (and MI) SDPI constants; approximate tensorization for relative-entropy SDPI constants, exact for generalized depolarizing channels at their fixed point.
- Applications: quantum extension of the Polyanskiy–Wu network bound η_MI(R∘M) ≤ η_R η_MI(M) + (1−η_R) η_MI(M_{A→B}); a new "replacing time" notion generalizing mixing time (asymptotically equivalent to mixing); quantum memory and QML limits.

**How it works** The technical engine is a perturbation argument: given a candidate state ρ_RA, one forms a binary classical mixture ρ_URA with fixed marginal σ_RA, defines φ(λ) = η·I(U:B|R) − I(U:B′|R), notes φ(0)=0, and evaluates φ′(0) using the standard vanishing of first-order relative-entropy derivatives at coincident arguments; this converts the two-point CMI inequality into the conditional divergence inequality. The reverse direction is the direct-sum property, so the results generalize to any divergence with direct-sum plus the derivative property (e.g. suitable f-divergences).

**Why it matters** It gives a computable-in-principle, SDP-upper-bounded handle on how noise degrades *conditional* correlations — the relevant object in networks, distributed protocols, and memories — and unifies previously scattered mutual-information contraction notions into one hierarchy.

**Caveats** Whether η_MI = η^c_D remains open (only ≤ is proven). Conditional expansion coefficients inherit triviality (=0) from known results for most divergences except trace distance. General tensorization of quantum SDPI constants still fails; only approximate/special-case results are given. Optimizations over unbounded reference dimension remain, and computability of η^cond beyond bounds is not resolved.

## 3. Lieb-Schultz-Mattis Constraints for Quantum Channels: A Spacetime-Duality View

[arXiv:2608.26266](https://arxiv.org/abs/2608.26266) · [SciRate](https://scirate.com/arxiv/2608.26266)

*Sarang Gopalakrishnan, Yu-Jie Liu, Tsung-Cheng Lu, Frank Pollmann, Yizhi You*

**TL;DR** — The paper recasts a repeatedly applied $d$-dimensional quantum channel carrying a mixed anomaly between a strong internal symmetry and a weak spatial symmetry as a $(d{+}1)$-dimensional mixed-state SPT wavefunction, via a spacetime (Choi + $t\!\leftrightarrow\!y$) rotation. Under this duality, temporal correlations of the channel map to strange correlators of the mSPT, and — the main conceptual claim — the *singular* spectrum of the channel transfer matrix $Q$ (i.e. eigenvalues of $Q^\dagger Q$), dual to the mSPT's operator entanglement spectrum, is the sharp anomaly diagnostic, not the Liouvillian eigenvalue spectrum.

**The big picture** — Anomalies in closed quantum systems forbid a unique, featureless, gapped ground state; extending this to noisy, dissipative systems has been hampered by the fact that the standard spectral diagnostic — degeneracies and gaplessness of the dissipative evolution operator — is generically present in any strongly symmetric open system, anomaly or not, so it cannot distinguish anomalous from ordinary dynamics. This work builds a dictionary in which running an open-system evolution forward in time is equivalent to moving across space in a one-dimension-higher mixed-state topological phase, so that the anomaly's consequences become boundary and entanglement statements about that higher-dimensional state. The payoff is a genuinely sharp signature: a new twisted correlation function that must decay slowly in time, and an entanglement-like spectrum of the evolution operator that cannot be trivial. This gives experimentalists and numericists a concrete, anomaly-specific observable for noisy dynamics rather than one contaminated by generic conservation-law effects.

**Key contributions**
- Explicit spacetime-duality dictionary (Table I): channel time evolution ↔ mSPT spatial transfer matrix under bulk projection; input/output states ↔ mSPT spatial boundaries; strong $S$/weak $G$ anomaly ↔ mSPT protected by strong $S$/weak $G$.
- The twisted Rényi-$N$ correlator $C(N)=\mathrm{Tr}[O^\dagger Q^N O Q^N]/\mathrm{Tr}[Q^{2N}]$ as a temporal probe, shown dual to the mSPT strange correlator; the LSM anomaly forbids exponential decay (so $C(N)\sim\mathcal{O}(1)$ or $\sim N^{-\alpha}$).
- Identification of the Liouvillian *singular* spectrum as the faithful anomaly diagnostic, dual to the mSPT operator entanglement spectrum; hence no unique dominant singular vector under an LSM constraint.
- A tensor-network (MPS/MPO) realization of the construction plus general formulation beyond spin-1/2 chains.

**How it works** — A single channel step in Stinespring form is Choi-vectorized and rotated so that input and output time slices become adjacent ladder columns ($L_{i-1}$, $R_i$, ancilla $A_i$). For the identity channel this is a stack of inter-column EPR pairs — precisely the coupled-wire fixed point of a 2d SPT protected by $\mathrm{SO}(3)\times T_x$, since each spin-1/2 wire is LSM-anomalous but each two-wire column is not; boundary wires remain anomalous. Adding the symmetric, $\mathrm{SO}(3)$-neutral ancilla coupling keeps the SPT phase; tracing out ancillas gives $\rho^{\rm mSPT}$ with strong $\mathrm{SO}(3)$, weak $T_x$. Projecting bulk columns onto onsite EPR pairs stitches blocks into $N$ channel steps, so $\mathrm{Tr}[Q^N]$ is an overlap with a trivial reference product state — exactly the strange-correlator setup.

**Why it matters** — Relevant to open-system topological order, dissipative state preparation, and NISQ-era diagnostics: it supplies an anomaly probe immune to the trivial degeneracies enforced by CPTP plus strong symmetry, and connects Liouvillian singular values to a well-understood entanglement classification.

**Caveats** — The dictionary assumes local, translation-invariant, Stinespring-dilatable channels with $\mathrm{SO}(3)$-neutral ancillas; the arguments lean on the (heuristic) coupled-wire/WZW path-integral identification of LSM anomalies with SPT boundaries. TRNC is a Rényi-type, non-linear-in-$\rho$ quantity, so experimental access requires replicas or post-selection-like overhead. Whether the constraint yields true long-range versus quasi-long-range temporal order, and the exponent $\alpha$, is left channel-dependent; the visible source truncates before the numerical evidence.

## 4. Quantum cellular automata and invertible phases of matter

[arXiv:2608.26456](https://arxiv.org/abs/2608.26456) · [SciRate](https://scirate.com/arxiv/2608.26456)

*Corey Jones, Nikita Sopenko, Ryan Thorngren*

**TL;DR** Working with quasi-local algebras whose *local* von Neumann algebras are infinite-dimensional, the authors prove that for any uniformly locally finite metric space $X$ the group of QCA over $X\times\mathbb{Z}$, the (super) Brauer group of invertible quasi-local algebras over $X$, and the group of invertible phases over $X\times\mathbb{Z}$ are all isomorphic — in sharp contrast to the finite-dimensional on-site setting, where the QCA→phases map is neither injective nor surjective. They then use chiral conformal nets ($c=\tfrac12$ Majorana, $(E_8)_1$) to produce explicitly non-trivial Brauer classes, hence non-trivial invertible states and QCA on $\mathbb{Z}^2$, and build a $K$-theoretic $\Omega$-spectrum realizing Kitaev's conjecture.

**The big picture** Two long-standing classification problems in many-body physics — which short-range-entangled phases of matter exist, and which strictly locality-preserving discrete dynamics are genuinely non-trivial — have stubbornly refused to line up with each other. This paper shows that the mismatch is an artifact of insisting on finitely many degrees of freedom per site: once one allows infinitely many, the two classifications become literally the same group, and both are computed by a third, purely algebraic object built from the boundary. The authors then import chiral conformal field theories, which are expected to live on the edges of chiral phases, as concrete generators, giving the first rigorous non-trivial examples in two spatial dimensions. This also suggests a criterion for when a continuum field theory admits a genuine lattice realization, tied to its gravitational anomaly.

**Key contributions**
- Definition of (super) invertible quasi-local algebras over uniformly locally finite metric spaces with infinite-dimensional local algebras, and their Brauer group under bounded-spread isomorphism.
- Theorem A: $\mathrm{QCA}(X\times\mathbb{Z})\cong \mathrm{Br}(X)\cong \mathrm{IP}(X\times\mathbb{Z})$, bosonic and fermionic in parallel; the new ingredient is a *boundary quasi-local algebra* attached to an invertible state (a rigorous bulk–boundary correspondence). The QCA↔Brauer half generalizes Haah's invertible-subalgebra argument.
- Theorem B: $K$-theory of the symmetric monoidal category of invertible quasi-local algebras with bounded-spread isomorphisms gives $K_n(\mathcal{Az}(\mathbb{Z}^{d-1}))=\mathrm{IP}(\mathbb{Z}^{d-n})$ for $0\le n\le d$, $K_{d+1}=\mathbb{R}/\mathbb{Z}$, zero above — an algebraic model of the Kitaev spectrum.
- Theorem C/Corollary D: discretized Majorana and $(E_8)_1$ nets are invertible with non-trivial classes in $\mathrm{s}\mathrm{Br}(\mathbb{Z})$, $\mathrm{Br}(\mathbb{Z})$; hence $\mathrm{IP}(\mathbb{Z}^2)\cong\mathrm{QCA}(\mathbb{Z}^2)\neq 0$.
- Theorem E: for any rational conformal net, the discretized Longo–Rehren (diagonal CFT time-slice) extension is bounded-spread isomorphic to $\mathrm{Mat}(\mathbb{Z})$ — an "extended split property" giving lattice degrees of freedom.

**How it works** Quasi-local algebras are treated as functors from bounded subsets to von Neumann superalgebras with supercommutativity; morphisms are locally normal bounded-spread maps, and everything is shown to be functorial in the coarse category, so discretization $\mathbb{Z}^d\hookrightarrow\mathbb{R}^d$ is canonical. Technical backbone: super versions of the Ge–Kadison tensor-splitting theorem (via Klein transform), slice maps detecting tensor subalgebras, and split/quasi-split properties. Theorem A is assembled from three maps (boundary algebra of a QCA, generalized shift, boundary algebra of a state). Non-triviality invariants come from chiral central charge / orbifold anomaly arguments.

**Why it matters** It removes a structural obstruction in the classification program, shows chiral ($c_-\neq 0$) phases *can* be prepared by cellular automata and by commuting (unbounded) local Hamiltonians when on-site spaces are infinite-dimensional, and links operator-algebraic CFT to lattice topological order in a computable way. Relevant to condensed-matter theorists, AQFT researchers, and QCA/quantum-information theorists.

**Caveats** Invertible states are assumed strictly zero-correlation-length (circuit-preparable together with inverse); the general existence of such representatives is conjectural. $\mathrm{IP}(\mathbb{Z}^2)\cong\mathbb{Z}$ generated by $E_8$ remains a conjecture, as does non-triviality for all $c\neq 0$ (proved here only for $c$ not divisible by 3, with the general case deferred). Extended split property is established only in $1+1$ dimensions; whether conjecturally non-trivial 3d QCA trivialize after stabilization is open. Physical interpretation of infinite-dimensional on-site Hilbert spaces as "free" ancillas is a modelling choice.

## 5. Randomness can be certified in energy-constrained semi-device-independent scenarios

[arXiv:2608.27357](https://arxiv.org/abs/2608.27357) · [SciRate](https://scirate.com/arxiv/2608.27357)

*Shashank Kumar Ranu, Lewis Wooltorton, Alastair A. Abbott, Omar Fawzi*

**TL;DR** The authors build an NPA-style semidefinite hierarchy for energy-constrained prepare-and-measure scenarios in which the preparation and measurement devices may share arbitrary pre-distributed entanglement, giving the first *certified* (upper) bounds on the adversary's guessing probability rather than heuristic seesaw lower bounds. Their dimension-independent relaxation certifies strictly positive min-entropy for energy parameter ω ≲ 0.18 (ω ≲ 0.27 with a qubit-source assumption), resolving affirmatively the open question of whether randomness survives entangled attacks in this setting.

**The big picture** Semi-device-independent randomness generators that assume only a bound on the energy (e.g. mean photon number) of the transmitted states are attractive because they are fast and experimentally cheap, but all existing security proofs assumed the sender and receiver boxes share only classical correlations. Recent work showed that an eavesdropper who secretly entangles the two boxes can generate stronger-than-classical correlations and eat into the certified randomness, leaving open whether any randomness at all can be guaranteed. This paper supplies a rigorous, dimension-free certification technique showing that a nonzero amount of private randomness does survive such attacks, over a useful range of energies and with meaningful tolerance to noise. That restores a security foundation for a whole family of practical photonic random number generators.

**Key contributions**
- First *certified* lower bounds on extractable min-entropy in the energy-constrained prepare-and-measure setting with pre-shared entanglement between devices and a purifying adversary.
- A technique to handle a measurement acting jointly on the message and the device's entangled share: block-decompose the POVM in a source basis, keep the low-energy subspace explicitly, lump the rest into one auxiliary operator with dimension-free "sandwich" relations.
- Same machinery repurposed to give certified *upper* bounds on the maximal entanglement-assisted correlator, an outer approximation of the correlation set complementing known explicit strategies.
- Noise robustness and a fixed-source-dimension variant (qubit/qutrit source, unbounded measurement and Eve systems) that nearly matches published seesaw upper bounds.

**How it works** Bob's projective POVM Π^b_{SM} is expanded as Σ|s₁⟩⟨s₂| ⊗ Π^b_M[s₁,s₂]; the blocks act on M alone and hence commute with source operators, restoring an NPA-compatible commuting structure. The obstruction is projectivity, which couples blocks through a sum over all d basis states. The fix: retain only the {|0⟩,|1⟩} sub-block operators (A, B, C plus source operators P, Q, T) and collapse everything else into a single Hermitian F obeying O₁FO₂ = 0 for all O₁,O₂ ∈ {P,Q,T,T†} — sixteen degree-3 relations valid for every d ≥ 2. Projectivity of the full element N is then imposed only at moment level via localizing matrices (conservatively truncated). Two moment matrices Γ⁰, Γ¹ are linked by no-signalling equalities ⟨O⟩₀ = ⟨O⟩₁ for all ME-monomials up to degree 2ℓ; energy (⟨P⟩ₓ ≥ 1−ω) and the correlator threshold I_corr ≥ 4√(ω(1−ω)) are linear constraints. Level ℓ = 2 is needed since the objective ⟨I − N − Z + 2NZ⟩₀ contains degree-3 monomials; solved with ncpol2sdpa/MOSEK.

**Why it matters** Energy-constrained SDI QRNGs already have MHz–GHz implementations; this closes a genuine security gap left by entanglement-based attacks. The construction is also of independent methodological interest: it shows how to run NPA when one party's measurement acts on both the message and its own entangled subsystem, likely reusable for other SDI and prepare-and-measure cryptographic tasks.

**Caveats** Bounds are single-round, i.i.d., min-entropy only — no finite-size proof (though the authors note Brown–Fawzi–Fawzi should drop in for von Neumann entropy). The certified threshold ω ≈ 0.18 is far from the seesaw upper bound ω ≈ 0.32, and the gap may be relaxation slack (weakened moment-level projectivity, ℓ = 2 only, truncated localizing constraints) rather than real attacks. Results hold for arbitrarily large finite dimension but not infinite-dimensional systems — the natural photonic setting. Only two inputs, one binary measurement, equal energy bounds ω₀ = ω₁, and the commuting-operator relaxation replaces the tensor-product model.
