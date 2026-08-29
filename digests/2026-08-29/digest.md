# SciRate Daily Digest — 2026-08-29

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Tight Bounds for Purity and Product Testing from Partial Transposition

[arXiv:2608.27217](https://arxiv.org/abs/2608.27217) · [SciRate](https://scirate.com/arxiv/2608.27217)

*Oren Akresh, Jacob Beckey*

**TL;DR** The authors show that the positive-partial-transpose (PPT-BOTH) relaxation — a convenient superset of adaptive single-copy (one-way LOCC across copies) measurements — already yields *asymptotically tight* Ω(√d) sample lower bounds for purity testing and for bipartite product testing, improving on the previous PPT-based bounds of Ω(d^{1/4}) and Ω(d^{1/8}) respectively. The proof is elementary: a telescoping "depolarize the last register" decomposition plus the identity that partially transposing a SWAP gives d times a maximally entangled projector.

**The big picture** Learning properties of an unknown quantum state is dramatically cheaper if you can measure many copies jointly, but hardware today mostly measures one copy at a time, possibly choosing later measurements based on earlier outcomes. Proving that such adaptive one-at-a-time strategies really do need many more samples is technically painful, and a popular shortcut — enlarging the strategy set to a mathematically friendly class defined by a transposition condition — was believed to give weaker, non-optimal bounds. This work shows the shortcut is actually lossless for two canonical tasks: checking whether a state is pure, and checking whether it is unentangled across a bipartition. The resulting proofs are short and use only standard symmetry facts, offering a reusable alternative to the heavier "learning tree" machinery.

**Key contributions**
- Bias bound |tr[M(σ⁽ⁿ⁾ − τ_d^{⊗n})]| ≤ n(n−1)/(2d) for *every* PPT-BOTH two-outcome measurement, hence n = Ω(√d) for purity testing — matching known nonadaptive single-copy protocols and the learning-tree bound.
- ε-dependent refinement: n = Ω(√(d/ε)), recovering the martingale-based result of Gong–Chen-type analyses.
- Product testing (k=2): bias ≤ O(n²/d), giving n = Ω(√d), a quartic improvement over the prior PPT bound Ω(d^{1/8}) and matching the O(√d) nonadaptive algorithm.
- First examples where the PPT relaxation preserves the *optimal* dimension dependence; bounds hold for all d, n ≥ 2, with no Schur–Weyl "stable regime" (d ≫ n) restriction.

**How it works** Write Δ = σ⁽ⁿ⁾ − τ_d^{⊗n} as a telescoping sum of single-depolarization operators D_m = σ⁽ᵐ⁾ − σ⁽ᵐ⁻¹⁾⊗τ_d tensored with maximally mixed states. Since tr[XY] is invariant under Γ_S and PPT-BOTH guarantees 0 ⪯ M^{Γ_m} ⪯ 1, each term is bounded by ½‖D_m^{Γ_m}‖₁. Splitting S_m into permutations fixing site m and those composed with a transposition (i m), and using P((im))^{Γ_m} = d·ψ_{i,m}, gives Π_m^{Γ_m} = (1/m)A_m(1 + dΨ_m) with [A_m, Ψ_m] = 0, so the pieces are positive and the trace norm is computed exactly: ½‖D_m^{Γ_m}‖₁ ≤ (m−1)/(d+m−1). Product testing follows by comparing both ensembles to τ_{d²}^{⊗n} and telescoping the A and B symmetric-subspace factors separately.

**Why it matters** Lower bounds against adaptive single-copy measurements underpin claims of exponential quantum advantage from coherent multi-copy access, and product-testing hardness bears on QMA(2) vs QMA. Having a two-page, symmetric-subspace-only route to these bounds lowers the barrier for extending them to new tasks and dimensions where tree analyses stall.

**Caveats** Product testing is treated only for k = 2 parties; the multipartite scaling is not addressed here. The lower bounds are asymptotic in d — constants and the exact bias/threshold trade-off are not optimized, and the ε-dependence for product testing is not derived. PPT-BOTH tightness is demonstrated for these two tasks only; the authors explicitly flag stabilizer testing (where the method has not yet closed the Ω(√n) vs Ω(n) gap) as open. The product-testing reduction relies on Haar concentration of the largest Schmidt coefficient, implicitly requiring ε in the constant regime.

## 2. Conditional contraction coefficients and their applications to quantum networks

[arXiv:2608.27171](https://arxiv.org/abs/2608.27171) · [SciRate](https://scirate.com/arxiv/2608.27171)

*Christoph Hirche, Ian George, Theshani Nuradha, Mark M. Wilde*

**TL;DR** The authors define a *conditional* contraction coefficient that allows arbitrary quantum reference systems by subtracting off the divergence already present in the reference marginals, thereby avoiding both the triviality of naive tensoring with the identity and the equal-marginal restriction of complete contraction coefficients. Their central result is that for Umegaki relative entropy this coefficient exactly equals the contraction coefficient of the conditional mutual information (with a binary classical "message" register already sufficient), and they parallel this with a "MIR" characterization of the complete coefficient. Applications include tensorization of CMI-SDPI constants, a quantum Polyanskiy–Wu network bound, and a new "replacing time" notion for quantum Markov semigroups.

**The big picture** When noise acts on part of a system, how much distinguishability survives depends on correlations with everything else that was not touched by the noise. Existing tools either ignore that side information entirely or only handle the artificial case where the untouched part is identical in the two scenarios being compared. This work builds a coefficient that handles arbitrary side information by discounting whatever distinguishability the side information already supplies, and shows it coincides with the natural information-theoretic quantity measuring how much correlation a channel destroys in the presence of a memory. That makes it the right object for networks, distributed protocols, and memory-lifetime bounds, where correlations with a reference are the whole point.

**Key contributions**
- Definition of conditional contraction/SDPI/expansion coefficients, plus relative (two-channel) versions, and the ordering η ≤ η^p ≤ η^c ≤ η^cond ≤ 1.
- A complete "map" of equivalences (Fig. 1): η_D = η_cqMI; η^p_D = η_MI; η^c_D = η_MIR; η^cond_D = η_CMI = η_cqCMI = η_2cqCMI.
- Doeblin upper bound η^cond_𝔻(𝒩) ≤ 1 − α₊(𝒩) for any jointly convex divergence — strictly stronger than the prior complete-coefficient bound and recovering a known CMI bound.
- Trace distance: the conditional coefficient is attained on orthogonal states; a classical example with hockey-stick divergence showing η^cond_{E_γ} > η^c_{E_γ} strictly.
- Exact tensorization of η_MI and η_CMI SDPI constants; approximate tensorization for relative-entropy SDPI, exact for generalized depolarizing at its fixed point.
- Network bound η_MI(ℛ∘ℳ) ≤ η_ℛ·η_MI(ℳ_{A→BD}) + (1−η_ℛ)·η_MI(ℳ_{A→B}), quantizing Polyanskiy–Wu.
- "Replacing time" generalizing mixing time, shown asymptotically equivalent to mixing.

**How it works** The core technical device is a perturbation argument: fix σ_RA, form a binary classical-quantum mixture ρ_URA with U having weight λ on ρ_RA and the complementary branch (σ−λρ)/(1−λ), and use the direct-sum property plus the vanishing first derivative of relative entropy at coincident arguments to show that the λ-derivative at 0 of ηI(U:B|R) − I(U:B′|R) reduces exactly to the conditional-relative-entropy contraction statement. This yields a three-way equivalence (binary classical U ⇔ arbitrary classical U ⇔ all states), stated for a general pair of channels ℳ, 𝒩, so it simultaneously covers relative contraction coefficients. The MIR variant repeats the argument under the constraint ρ_R^u = ρ_R^v, matching the equal-marginal condition of the complete coefficient. Convexity plus the replacer decomposition 𝒩 = (1−ε)𝒟 + εℛ_τ gives the Doeblin bound.

**Why it matters** Complete contraction coefficients require an unbounded reference optimization and an unnatural constraint; the conditional version is both more permissive and, via the CMI identification, operationally meaningful and tensorizing. Anyone working on quantum SDPIs, mixing times of Lindbladians, quantum memory lifetimes, differential privacy, or capacity bounds for relay-type networks now has a coefficient with clean composition and tensorization properties.

**Caveats** Whether η_MI(𝒩) = η^c_D(𝒩) is left open (Lemma 6 gives only ≤, though a separation is claimed later). Tensorization of relative-entropy SDPI constants is only approximate in general, exact in special cases; general quantum SDPI tensorization is known to fail. Conditional expansion coefficients inherit triviality (equal to zero) for most divergences other than trace distance. Computability is not addressed beyond the Doeblin SDP upper bound, and the reference-system dimension in the supremum remains unbounded for the coefficients not covered by the classical-register reductions.

## 3. Lieb-Schultz-Mattis Constraints for Quantum Channels: A Spacetime-Duality View

[arXiv:2608.26266](https://arxiv.org/abs/2608.26266) · [SciRate](https://scirate.com/arxiv/2608.26266)

*Sarang Gopalakrishnan, Yu-Jie Liu, Tsung-Cheng Lu, Frank Pollmann, Yizhi You*

**TL;DR** The authors use a spacetime duality to recast the transfer matrix (Choi-space Liouvillian) of a repeated $d$-dimensional quantum channel with a mixed anomaly between strong $S$ and weak $G$ symmetry as a $(d{+}1)$-dimensional mixed-state SPT wavefunction, with the channel's input/output states appearing as the mSPT's spatial edges under bulk projection. They introduce a twisted Rényi-$N$ correlator (TRNC) that maps onto the mSPT strange correlator, and argue that the *singular* spectrum of the transfer matrix — dual to the mSPT operator entanglement spectrum — is the sharp anomaly diagnostic, not the Liouvillian eigenvalue spectrum.

**The big picture** Lieb–Schultz–Mattis theorems say that certain combinations of symmetry and filling forbid a boring, unique, gapped ground state. Extending this logic to open, noisy quantum systems has been awkward: the natural spectral diagnostics used so far are degenerate or gapless for trivial reasons — trace preservation plus strong symmetry already forces steady-state degeneracy, and conserved densities already force slow hydrodynamic modes. This work reframes repeated noisy evolution by trading the time direction for an extra spatial direction, turning the dynamics into a static topological state one dimension higher, where standard boundary/anomaly reasoning applies. That yields two genuinely anomaly-sensitive dynamical fingerprints: a nonlinear temporal correlator that cannot decay exponentially, and a singular-value spectrum that cannot have a unique dominant vector.

**Key contributions**
- Explicit spacetime-duality dictionary (Table I) between anomalous $d$-dim channels and $(d{+}1)$-dim mSPTs: time evolution ↔ bulk-projected transfer matrix; initial/steady states ↔ spatial edges; TRNC ↔ strange correlator; singular spectrum of $Q$ ↔ operator entanglement spectrum.
- Definition of the TRNC, $C(N)=\mathrm{Tr}[O^\dagger Q^N O Q^N]/\mathrm{Tr}[Q^{2N}]$, with $O$ charged under strong $SO(3)$ (magnetization) or weak translation (VBS order parameter); Proposition I asserts it decays at most algebraically.
- Identification of the Liouvillian *singular* spectrum (spectrum of $Q^\dagger Q$) as the anomaly-faithful diagnostic, forbidden to have a unique dominant singular vector.

**How it works** One channel step is Choi-vectorized and rotated $t\!\to\!y$, giving a two-leg ladder "building block": input chain $L_{i-1}$, output chain $R_i$, and Stinespring ancilla $A_i$ entangled by a symmetric unitary $\hat U^{s,a}$. Stacking $N$ blocks gives a coupled-wire 2d state in which each column $L_i\oplus R_i$ is anomaly-free (the two wires carry conjugate $SO(3)$ representations) so the bulk gaps out, while dangling boundary wires retain the spin-$\tfrac12$ LSM anomaly. Tracing the ancillas yields $\rho^{\mathrm{mSPT}}$ with strong $SO(3)$, weak $T_x$; projecting bulk columns onto onsite EPR pairs re-stitches the blocks into $N$ channel applications. MPS/MPO tensor diagrams make the correspondence explicit, and contracting the doubled SPT with a trivial reference state reproduces $\mathrm{Tr}[Q^N]$, which is the bridge to the strange-correlator identity.

**Why it matters** It supplies a concrete, in-principle-computable dynamical signature of LSM anomalies in dissipative dynamics, and cleanly explains why prior Liouvillian-gap statements are not sharp. Relevant to anyone working on mixed-state topology, dissipative phase classification, or tensor-network simulation of channels.

**Caveats** The TRNC is a Rényi-2-type object, requiring multiple copies or postselection to measure. The argument inherits known weaknesses of strange-correlator diagnostics (long-range order is not guaranteed for all SPTs/reference states), and depends on the choice of trivial reference state $|\phi^{\rm tri}\rangle$. Whether strong symmetry survives or breaks to weak symmetry under the channel is deferred to an appendix and could alter the dual phase. The truncated source prevents assessment of the numerical evidence for the singular-spectrum claim.

## 4. Quantum cellular automata and invertible phases of matter

[arXiv:2608.26456](https://arxiv.org/abs/2608.26456) · [SciRate](https://scirate.com/arxiv/2608.26456)

*Corey Jones, Nikita Sopenko, Ryan Thorngren*

**TL;DR** Allowing infinite-dimensional local von Neumann algebras on each lattice site collapses three separate classification problems into one: for any uniformly locally finite metric space, the group of quantum cellular automata over X×Z, the Brauer group of invertible quasi-local algebras over X, and the group of invertible phases over X×Z are all canonically isomorphic. Taking K-theory of the symmetric monoidal category of invertible quasi-local algebras with bounded-spread isomorphisms then yields an Ω-spectrum of invertible phases of the kind Kitaev conjectured, and chiral conformal nets (c=1/2 Majorana, (E8)₁) supply explicit non-trivial classes, hence non-trivial invertible states and QCA in two spatial dimensions.

**The big picture** Lattice models of quantum matter are usually built with finitely many degrees of freedom per site, a convenient idealization that nonetheless makes the classification of locality-preserving dynamics differ awkwardly from the classification of short-range-entangled ground states, and blocks realization of chiral phases by commuting local terms. This work argues that the mismatch is an artifact of that idealization: once each site is allowed infinitely many degrees of freedom, cellular automata and invertible phases classify exactly the same thing, mediated by an algebra living on the boundary that encodes the anomalous edge. The authors then use rigorous algebraic quantum field theory — chiral conformal field theories realized as nets of operator algebras — to produce genuinely non-trivial examples in two dimensions, including one matching the famous chiral boson phase expected to generate the classification. This gives a concrete algebraic home for a long-conjectured organizing structure for invertible phases and a criterion for when a field theory can live on a lattice at all.

**Key contributions**
- Definition of (super) invertible quasi-local algebras over uniformly locally finite metric spaces with infinite-dimensional local algebras; a Brauer group Br(X) of stable classes under bounded-spread isomorphism.
- Theorem A: QCA(X×Z) ≅ Br(X) ≅ IP(X×Z), via a *boundary quasi-local algebra* of an invertible state (new) plus a generalization of Haah's invertible-subalgebra correspondence.
- Theorem B: K_n(Az(Z^{d−1})) = IP(Z^{d−n}) for 0≤n≤d, K_{d+1}=R/Z, 0 above — an algebraic Kitaev Ω-spectrum, alternative to Kubota's analytic proposal.
- Theorem C/Corollary D: discretized Majorana and (E8)₁ nets are invertible and Brauer-nontrivial, so Br(Z)≅IP(Z²)≅QCA(Z²) ≠ 0.
- Theorem E: the Longo–Rehren extension of a rational net discretizes to Mat(Z) ("extended split property"), so holomorphic nets are invertible.

**How it works** Quasi-local algebras are treated functorially over the coarse category, so discretization Z^d ⊂ R^d is canonical. Invertibility means A ⊗ Ã ≅ Mat(X) by a bounded-spread isomorphism. Technical machinery includes super-versions of Ge–Kadison tensor splitting (via a Klein transform), super slice maps, and split/quasi-split properties; the boundary algebra of an invertible state supplies the map IP → Br, and generalized shifts invert it. Notably, the boundary algebra is always locally infinite-dimensional even for spin-system states.

**Why it matters** It explains why finite-dimensional QCA classifications (shift QCA, 3d Haah-type automata) look unlike invertible-phase classifications: stabilization trivializes some and creates others. It also implies chiral (c₋≠0) phases admit commuting, possibly unbounded, local Hamiltonians, and suggests an anomaly-vanishing criterion for latticizability of QFTs.

**Caveats** Invertible states are assumed strictly finite-correlation (circuit-preparable with inverse); the conjecture Br(Z)≅Z generated by E8 is unproven; non-triviality is established via central charge not divisible by 3, with the general c≠0 case deferred; QFT results are (1+1)d only; whether conjecturally non-trivial 3d QCA survive stabilization is open.

## 5. Randomness can be certified in energy-constrained semi-device-independent scenarios

[arXiv:2608.27357](https://arxiv.org/abs/2608.27357) · [SciRate](https://scirate.com/arxiv/2608.27357)

*Shashank Kumar Ranu, Lewis Wooltorton, Alastair A. Abbott, Omar Fawzi*

**TL;DR** The authors build an NPA-style semidefinite hierarchy for the energy-constrained prepare-and-measure scenario in which the preparation and measurement devices may share arbitrary pre-distributed entanglement with a purifying eavesdropper. The key trick is to expand Bob's joint POVM on the message-plus-ancilla system into blocks in a fixed source basis, retaining an explicitly preserved low-dimensional block plus a single auxiliary operator obeying dimension-free "sandwich" relations. This yields the first *certified* (rather than heuristic/seesaw) lower bounds on min-entropy, strictly positive for energy parameter ω ≲ 0.18 with no dimension assumptions, and ω ≲ 0.27 assuming a qubit source.

**The big picture** Semi-device-independent randomness generators based on bounding the energy (mean photon number) of the transmitted states are attractive because they are fast and need only off-the-shelf optical monitoring, but until now their security proofs assumed the source and detector boxes shared only classical correlations. Recent work showed an adversary who secretly entangles the two boxes beforehand can do strictly better, undermining all previously certified rates and leaving open whether any randomness survives. This paper shows the answer is yes, by extending the standard toolkit for dimension-free bounding of quantum correlations to a setting where the usual separation between parties does not hold. That restores a rigorous security foundation for a practically important class of quantum random number generators.

**Key contributions**
- First certified upper bounds on the guessing probability in energy-constrained PM with pre-shared entanglement, valid for arbitrary finite dimensions of source, measurement ancilla, and Eve's system.
- A technique to handle a POVM acting jointly on the message and the receiver's ancilla within an NPA framework: block decomposition plus a lumped remainder operator with dimension-independent relations.
- Positive certified min-entropy for ω ≲ 0.18 (dimension-free) and ω ≲ 0.27 (qubit source, unbounded M), versus seesaw upper bounds positive to ω ≈ 0.32.
- Noise robustness: at ω = 0.05, positive rate down to correlator ≈ 0.50 vs ideal 0.87 (≈58%); at ω = 0.1, down to ≈79% of ideal.
- Certified *outer* bounds on the maximal entanglement-assisted correlator, closing in on the explicit-strategy inner bounds.

**How it works** Bob's projective POVM element Π⁰_SM is written as Σ|s₁⟩⟨s₂|⊗Π⁰_M[s₁,s₂]; blocks with s₁,s₂ ∈ {0,1} are kept as operators A, B, C (which commute with source operators P, Q, T), and everything else is lumped into F. Projectivity of the full element couples blocks through a sum over d, so instead one imposes N² = N at the moment/localizing-matrix level (restricted to O₁,O₂ ∈ {I,P,Q,T,T†} for tractability — a conservative truncation) together with the exact degree-3 relations O₁FO₂ = 0. Two moment matrices Γ⁰, Γ¹ are linked by no-signalling equalities ⟨O⟩₀ = ⟨O⟩₁ for all ME-monomials up to degree 2ℓ; energy and correlator constraints are single linear moment inequalities. Level ℓ = 2 is needed because the objective contains degree-3 monomials (e.g. PAZ); solved with ncpol2sdpa/MOSEK.

**Why it matters** Practitioners deploying photonic SDI QRNGs now have a security argument that survives the strongest known class of attacks. The block-decomposition trick is likely reusable wherever a measurement acts jointly on a transmitted system and an adversarially supplied ancilla.

**Caveats** Bounds are i.i.d./single-round min-entropy only — no finite-size proof. Restricted to finite dimensions, whereas photonics is naturally infinite-dimensional. A substantial gap remains between these lower bounds and seesaw upper bounds (0.18 vs 0.32), and the near-coincidence of qubit and qutrit source curves suggests much of the gap is relaxation slack (weakened projectivity enforcement, level ℓ = 2) rather than genuine higher-dimensional attacks. Equal energy bounds ω₀ = ω₁ are assumed throughout.
