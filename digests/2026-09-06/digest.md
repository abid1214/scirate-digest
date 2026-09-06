# SciRate Daily Digest — 2026-09-06

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Fractalizing spacetime: Floquet codes with fractonic excitations that are immobile in space and time

[arXiv:2609.03703](https://arxiv.org/abs/2609.03703) · [SciRate](https://scirate.com/arxiv/2609.03703)

*Juliette Soule, Dominic J. Williamson*

**TL;DR** The authors extend Yoshida-style "fractalization" — the polynomial/linear-cellular-automaton (LCA) trick that turns a toric code into Haah-like fracton models — from spatial directions to the time direction of a Floquet code, by fractalizing the Raussendorf–Bravyi–Harrington (RBH) cluster state that encodes the (2+1)D toric-code memory. Choosing three algebraically independent LCA polynomials for the two spatial and one temporal direction yields a code whose syndrome defects cannot be moved in *any* spacetime direction without branching, i.e. a "spacetime type-II" fracton Floquet code with no string-like spacetime logical faults, exponentially long logical response periods, and (claimed) superlinear timelike fault distance.

**The big picture** Fracton phases are famous for excitations that cannot move through space without paying an energy cost, which makes them attractive as self-correcting memories. Existing dynamical (Floquet/measurement-based) codes, despite their time-periodic structure, all realize spacetime phases equivalent to ordinary static codes. This work shows how to build genuinely dynamical phases with no static counterpart, in which errors are frozen in time as well as in space — meaning a single fault cannot silently propagate forward through the circuit, and the memory's logical response repeats only after a number of cycles growing exponentially with system size, an extreme form of time-crystalline order.

**Key contributions**
- A definition of fractalization *in time*, via fractalizing the spatial direction of a cluster state that plays the role of a computational history.
- Constant-depth *local adaptive* circuits (CNOT ladder → measurement gadget + Pauli feed-forward) implementing LCA update rules that would naively need linear depth; noted parity obstruction splitting the channel into even/odd charge sectors under periodic boundaries.
- Fault-tolerant version: transversal application across a stack of code blocks, giving a fractalized RBH cluster state with explicit CSS polynomial matrices, fractalized 1-form and global symmetries, and a Floquet schedule (surface-code checks at integer steps, fractalizing CNOTs at half steps).
- Identification of the spacetime type-II condition: excitation polynomial 1+f(w)x + 1+g(w)y + 1+h(w)z; mobility in direction n₁x̂−n₂ŷ−n₃ẑ exists iff f^{n₁}=cg^{n₂}h^{n₃}. Explicit independent triple f=1+w+w², g=1+w+w³, h=1+w²+w³ at L=2^l.
- Tensor-network appendix tracking measurement-outcome byproduct operators to the final timeslice for arbitrary outcomes.

**How it works** Everything is done in the F₂[x,y,z,w]-polynomial (Laurent) representation of CSS stabilizers; fractalization substitutes x→f(w)x etc., adding a "layer" coordinate w. Because f(w)^{2ⁿ}=f(w^{2ⁿ}), single-site seeds generate self-similar Sierpinski-like histories with cycle lengths inside an exponentially growing envelope. In MBQC language, measuring the a-sublattice column teleports logical information one step forward *while* applying the LCA; the fractalized RBH state is thus a fault-tolerant history state whose time evolution is the LCA acting on a stack of surface codes.

**Why it matters** Relevant to anyone designing Floquet/dynamical codes or worrying about timelike distance: a no-strings rule in the time direction directly attacks measurement-fault propagation, potentially cutting the number of syndrome rounds needed. It is also a concrete construction of a dynamical topological phase with no static equivalent, and of a time crystal with exponentially long period.

**Caveats** The superlinear fault-distance and threshold claims are asserted, not computed — no decoder, no numerics, no explicit distance scaling law. Algebraic independence of the example triple under periodic boundaries is stated without proof. Boundaries in spacetime, self-correction, and non-CSS generalizations are left open; the continuum-limit "time crystal" may not correspond to any physical periodic Hamiltonian, as the authors note. The source's figures (essential to the circuit gadgets) are unpopulated, so several constructions are hard to verify from the text alone.

## 2. Resource-adaptive distributed fault tolerance with very noisy Bell pairs

[arXiv:2609.03048](https://arxiv.org/abs/2609.03048) · [SciRate](https://scirate.com/arxiv/2609.03048)

*Moritz Schmidt, Martin Moureau, Benjamin Rodatz, Boldizsár Poór, Elie Mounzer, Linnea Grans-Samuelsson*

**TL;DR** The authors extend the ZX-calculus "fault tolerance by construction" framework to distributed QEC where inter-module links are Bell pairs whose error rate is a fractional power of the on-chip rate (typically the cube root). They show that "fault-improving" a distribution edge recovers entanglement distillation as a special case but also yields more flexible dynamical protocols, that integrated (joint) decoding halves the required distillation distance relative to separate decoding, and they synthesize resource-adaptive distributed weight-4 and weight-6 stabilizer circuits benchmarked in Stim under SI1000 noise for distributed surface- and color-code memory and lattice surgery.

**The big picture** Building a large quantum computer by linking many small chips means error correction must run across links that are far noisier and slower than operations inside a chip. The usual answer is to purify the shared entanglement first, then do error correction on top, but this is wasteful because the purification is designed without knowing what the surrounding code actually needs. This work treats the link noise as just another fault to be budgeted inside the whole circuit, deriving how much protection each link really needs — often much less than the standard recipe — and turning that into concrete circuits that can be traded off against a chip's available spare qubits and its rate of entanglement generation.

**Key contributions**
- Formalizes distribution edges with per-Pauli improvement targets; fault tolerance requires suppressing hook errors (Z-type, propagating to two data qubits) to weight ≥2 and readout errors (X-type) to weight ≥1, giving outer/inner improvements of 2m and m for Bell noise p^{1/m}.
- Shows integrated decoding needs only half the distillation code distance of separate decoding — a direct reduction in Bell pairs.
- Explicit distributed circuits for weight-4 (2-2 split) and weight-6 (3-3 and 4-2 splits) stabilizers via fault-equivalent ZX rewrites, with Pauli-web analysis identifying which detecting regions each edge sits in.
- *Context-aware* improvement: in the surface code, hooks parallel to the seam are benign, allowing e.g. Z(1, m) instead of Z(m, 2m); in lattice surgery the readout-error constraint returns for the seam plaquettes.
- A connectivity-constrained variant using one Bell-pair channel and two ancillas per QPU per plaquette on a square grid.

**How it works** Improvement strategies span fully parallel (ED, distillation-like), partially sequential (V2) and fully sequential (V1) repetition schemes, plus Steane/QPC-code distillation; sequential schemes cost idle time, which shifts logical curves upward even when asymptotic slopes are correct. Numerics use noisy Bell pairs modelled as two-qubit depolarizing at p^{1/3}, Tesseract (short-beam) for integrated decoding, 10⁷ shots (10⁶ for color code, 10¹⁰ for postselected d=2).

**Why it matters** It gives hardware architects a quantitative, code- and context-dependent Bell-pair budget rather than a one-size-fits-all distillation overhead, relevant to superconducting-module and networked-ion architectures.

**Caveats** Simulated slopes for d=7,9 exceed expectations, attributed to a "waterfall" regime plus large variance; expected asymptotic slopes for under-improved [[6,4,2]] configurations are not observed at accessible p. An unexplained X/Z asymmetry appears in the (nominally symmetric) color-code memory. Distributed circuits break matchability, forcing a slower search-based decoder run in a reduced-accuracy configuration — decoder scalability is untested. Most simulations assume unrestricted connectivity near QPU boundaries; the constrained version shows a clear threshold degradation, reaching only ~10⁻³ at the milder p^{1/2} Bell noise. Bell-pair generation rate and latency are not modelled dynamically.

## 3. Energetic Costs of Subspace Quantum Error Correction

[arXiv:2609.03825](https://arxiv.org/abs/2609.03825) · [SciRate](https://scirate.com/arxiv/2609.03825)

*Jakub Czartowski, Felix C. Binder*

**TL;DR** The paper treats the syndrome register of an active QEC cycle as a Maxwell-demon memory whose periodic reset carries an unavoidable Landauer cost, and derives a four-level hierarchy of that cost — von Neumann entropy of an effective syndrome state built from the Knill–Laflamme structure, entropy of the decoded error label, of the raw parity record, and of the separately-erased parity bits. For stabiliser codes under independent depolarising noise it shows that label-level cost is reduced at leading order by weight-two normaliser elements (code degeneracy), while bit-level cost scales with stabiliser check weight, giving an entropic argument for low-weight (qLDPC-style) checks; explicit formulas are given for the five-qubit, Steane, generalised Shor, and rotated surface codes.

**The big picture** Error correction works by moving disorder out of the protected quantum data and into a classical record of what went wrong. That record cannot grow forever, so it must be wiped between rounds, and wiping information has a thermodynamic price. This work asks how large that price is and shows it is not fixed by the usual code parameters alone but by the joint structure of the code, the noise, and the way the record is stored — with substantially different costs depending on whether one keeps raw measurement bits or a compressed diagnosis.

**Key contributions**
- Construction of an *effective syndrome state* from the KL conditions plus the noise Kraus operators, whose von Neumann entropy lower-bounds the erasure work; entropy-optimal syndrome choices are those that diagonalise it.
- A measurement inefficiency ratio quantifying the gap between projective readout entropy and the coherent bound; saturation via unitary (measurement-free) recovery.
- Treatment of *uncorrectable* noise as a state-conditioned syndrome contribution, with input-independent operator-norm bounds — and the observation that no state-independent optimal error basis then exists.
- Leading-order label entropy for stabiliser codes: a term reduced by the sizes of single-qubit degeneracy classes, readable directly off weight-two normaliser elements.
- Bit-level entropy per check, showing high-weight checks are entropically more expensive, plus a bit-level inefficiency measure.

**How it works** In a KL-diagonalised basis the recovery is projections onto rotated code copies; the syndrome distribution is the computational-basis diagonal of a rotated effective density matrix, immediately giving the vN-entropy bound. For depolarising noise below the single-error-dominance threshold, label entropy is expanded to first order in the per-Pauli rate. Bit-level entropy follows from the odd-parity probability for a weight-w check. Concretely: Shor codes gain an entropy reduction scaling faster than qubit number, surface codes only linearly (from boundary weight-two checks), Steane and five-qubit codes not at all. However, plotted against a logical-failure proxy, rotated surface codes need less total erasure work than Shor codes.

**Why it matters** Provides a principled, code-structure-resolved accounting of the one genuinely irreversible ingredient of QEC, and a new (if small) axis — syndrome-memory entropy — along which to compare code families; relevant to anyone thinking about cryogenic/control budgets or thermodynamics of computation.

**Caveats** Idealised reversible-erasure limit; only near-device syndrome memory is counted, excluding decoder hardware, gates, and control. Analysis is leading order in the error rate, single-round (multi-round temporal correlations in the record are deferred), assumes orthogonal error sectors in the main text and independent local Pauli noise. Absolute costs are order kT per nat and per round are order p log p, so practical significance versus hardware overheads is not established.

## 4. Robust Hamiltonian engineering with subensemble control

[arXiv:2609.03045](https://arxiv.org/abs/2609.03045) · [SciRate](https://scirate.com/arxiv/2609.03045)

*Wenjie Gong, Matteo Votto, Soonwon Choi*

**TL;DR** This work formalizes pulsed Hamiltonian engineering in the intermediate regime between fully global and fully site-local control, where a handful of independently addressable subensembles are driven in parallel. The authors prove that deciding engineerability is NP-hard in the qudit dimension (via reduction to separability), yet supply a computable majorization-based necessary condition, a constructive sufficient condition (any target reachable up to overall rescaling whenever intra-subensemble interaction matrices are traceless), efficient LP/evolutionary sequence-design methods, and error-robust sequence constructions — demonstrated by generating two-mode spin squeezing in dual-species cavity and Rydberg tweezer systems.

**The big picture** Many quantum simulation and sensing platforms cannot address individual particles, but can drive a few distinguishable groups — different defect orientations, atomic species, or masked subregions — independently. This paper asks precisely what interactions such coarse-grained control can synthesize, and shows it is dramatically more than uniform global driving, while still being fundamentally constrained because the pulses that reshape couplings between groups inevitably also reshape couplings inside them. Along with the theory, the authors give practical recipes for designing pulse sequences that survive realistic control errors, and show these unlock entangled states useful for simultaneously sensing multiple parameters that global control alone cannot produce.

**Key contributions**
- Hardness: subensemble engineering with two groups subsumes the two-qudit separability problem (NP-hard in local dimension); for qubits it maps, via Fano representation, to the still-open "mixture of local unitaries" interconversion problem for two-qutrit states — strictly harder than LOCC characterization.
- Necessary condition: eigenvalue majorization of the block matrix assembling intra- and inter-group interaction matrices; extends to a family of 2ⁿ−n−1 conditions for n groups.
- Sufficient condition: if intra-group interaction matrices are traceless, any target with traceless intra-group parts is reachable up to a rescaling factor — proved by 2-design-based selective decoupling applied group-wise.
- Sequence-length bound O((nd)²), plus a guarantee that any pulse set generating a toggling-frame 4-design makes linear programming succeed whenever a solution exists (explaining why icosahedral sets work).
- Universal symmetrization recipes giving quadratic suppression of amplitude and frequency errors (reflected sequences with −θ and 2π−θ), plus analytic handling of pulse-width errors, with residual "squared" terms absorbed by LP-retuned spacings.

**How it works** Pulses act on interaction matrices as orthogonal conjugations, so the engineered Hamiltonian is a convex combination of rotated natives with block-diagonal rotations — the block structure is exactly what obstructs universality. The invariant that cannot be changed is the trace (Heisenberg component) of intra-group couplings; everything else is reachable, recasting design as maximizing rescaling factors.

**Why it matters** Provides a rigorous toolbox for NV ensembles, dual-species ion/atom arrays, and detuning-masked tweezers. The application engineers two-axis two-spin twisting from one-axis twisting (achieving optimal J̃ = J/3, saturating the necessary bound), yielding two-mode squeezing robust to 3% amplitude/frequency errors up to N = 80, and ~4 dB in a 4×5 dipolar array.

**Caveats** Everything is leading-order Floquet–Magnus; interaction matrices are assumed position-independent and native Hamiltonians 2-local. The necessary condition is not sufficient (it ignores the block-diagonal constraint). Numerics reach only modest sizes, and pulse errors destroy Heisenberg scaling even with robust sequences — squeezing is scalable but not ideal.

## 5. Redesigning quantum theory

[arXiv:2609.03333](https://arxiv.org/abs/2609.03333) · [SciRate](https://scirate.com/arxiv/2609.03333)

*Matthew B. Weiss*

**TL;DR** — This dissertation develops the QBist program that quantum theory is Bayesian probability plus extra "nonclassical coherence" conditions, and pushes it to a reconstruction: starting only from a minimally deformed law of total probability tied to a reference measurement, plus a minimally deformed rule for multiplying random variables, one is forced into a Euclidean Jordan algebra and hence (after further restriction) finite-dimensional complex quantum mechanics. A practical corollary is a theory-agnostic self-testing protocol certifying that a reference measurement's conditional-probability matrix comes from a complex projective 3-design (and *t*-designs for *t* ≥ 3).

**The big picture** — QBism claims quantum mechanics is not a new physics of waves and particles but ordinary personal probability theory, augmented by a single extra consistency rule that connects a gambler's bets on a hypothetical, informationally complete "reference" experiment to their bets on everything else. The advance here is to derive that extra rule, and then the entire geometry of quantum state space, from the demand that the deformation of ordinary probability be as gentle as possible — the resulting structure is encoded entirely in the table of conditional probabilities characterizing the reference measurement itself. This matters because it converts an interpretive stance into a genuine axiomatic reconstruction, and it yields something operationally useful: a way to certify that a laboratory measurement device really implements a highly symmetric, theory-independent benchmark measurement.

**Key contributions**
- A uniqueness theorem: the only commutative, bilinear, permutation-equivariant, unital one-parameter deformation of the pointwise product of random variables has a specific two-term form, with the deformation parameter fixed by compatibility with the coherence inner product.
- Reducing "higher moments of an observable are computable from its reference-valuation powers" to power associativity, hence (via Jordan–von Neumann–Wigner) to the Jordan identity, expressed as explicit polynomial constraints on the reference matrix entries / structure coefficients.
- A variance-style uncertainty-principle characterization of valid reference probability distributions, equivalent to positive semidefiniteness of an operator that simultaneously implements the Jordan product.
- Self-testing of complex projective *t*-designs (*t* ≥ 3) that, unlike frame-potential arguments, certifies existence of a Hilbert space representation.
- (Earlier chapters) equivalence of the QBist framework with GPTs, and a coherentist criterion for when a scenario admits classical explanation.

**How it works** — Assuming the reference matrix is symmetric with constant diagonal and admits a Born matrix of the form scalar-plus-uniform, its spectrum collapses to three values and the diagonal is fixed by rank. The deformed product is projected onto the column space, shown self-adjoint and formally real; imposing the Jordan identity via full third-order polarization (checkable on basis columns) yields a Euclidean Jordan algebra. Koecher–Vinberg then gives a homogeneous self-dual cone identifying states with effects, and the JvNW classification narrows the possibilities to real/complex/quaternionic/octonionic Hermitian matrices or spin factors.

**Why it matters** — Relevant to quantum foundations and reconstruction programs, and to anyone doing SIC/design-based tomography or randomized benchmarking who wants device-independent certification of design measurements.

**Caveats** — Several structural assumptions (symmetry, constant diagonal, the specific Born-matrix ansatz, "fewest terms" simplicity) are motivated but not derived. Ruling out the real, quaternionic, octonionic, and spin-factor branches requires additional postulates; the source is truncated before that argument, and the reconstruction is described by the author as "modest." Robustness of the self-testing claim to experimental noise is not addressed in the visible material.
