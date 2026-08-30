# SciRate Daily Digest — 2026-08-30

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Quantum-Inspired Computational Fluid Dynamics for Transient Turbulent Compressible Flows

[arXiv:2608.26995](https://arxiv.org/abs/2608.26995) · [SciRate](https://scirate.com/arxiv/2608.26995)

*Shang Xian Matthew Lee, Melissa Kozul, Muhammad Usman, Martin Sevior, Matthew L. Sims-Goh, Richard D. Sandberg*

**TL;DR** — This work supplies the two missing arithmetic primitives (element-wise division and square root) for tensor-train (TT) representations of discretised fields, using Newton–Raphson iterations built from TT addition and Hadamard products, and uses them to build the first end-to-end quantum-inspired DNS solver for the *compressible* Navier–Stokes equations, including temperature-dependent viscosity via Sutherland's law. On a 32³ Taylor–Green vortex at Re=800 (Ma=0.8 and 0.1) it matches the classical HiPSTAR solver to <0.1% in kinetic energy and <0.6% in enstrophy until t≈15, drifting to 2.1–4.6% late in the run. A novel "simultaneous simulation" trick encodes multiple independent runs in one TT at only ~20% extra cost.

**The big picture** — Tensor-network methods borrowed from quantum many-body physics can compress fluid fields enormously, but until now they could only handle incompressible flow because dividing one compressed field by another, or taking a square root of one, had no efficient algorithm. Supplying those operations unlocks compressible flow — aerospace, aeroacoustics — where density and viscosity vary in space. The authors also show that many parameter variants of a design can be packed into a single compressed simulation for almost the price of one, which is exactly what industrial design sweeps need. The catch, quantified here, is that the compression degrades as turbulence intensifies.

**Key contributions**
- Newton–Raphson TT reciprocal (with an optimal second-order polynomial seed on a known value interval) and the first TT square-root algorithm; error metrics based on inner products/sums avoid decompression.
- First fully in-TT compressible DNS solver: RK4, 4th-order central differences, skew-symmetric splitting (48 extra terms), Sutherland viscosity; initialisation via tensor cross interpolation (χ=3) and post-processing (energy, enstrophy) all in TT format.
- Simultaneous multi-case simulation via an extra tensor leg: 140 s → 170 s for two cases vs 200% classically.
- A-priori bond-dimension study: χ grows as a power law in Re; χ peaks near t≈12 (peak enstrophy), reaching ~2700 at Re=1600 for σ_c=10⁻¹², ~500 at σ_c=10⁻⁶.

**How it works** — Fields live in a quantics/serial-ordered TT over 3 registers; derivatives are low-rank TT operators. Division reduces to iterated multiply-add; square root calls division. Multiplication uses delta-tensor TTS→TTO conversion plus Cholesky-Based Compression contraction (first reported use), giving O(Nχ⁴) time, O(Nχ³) memory. Density-matrix addition is used generally, but DMRG-like addition inside division for accuracy.

**Why it matters** — Removes the principal arithmetic blocker for quantum-inspired CFD and, more broadly, for any TT application needing nonlinear pointwise functions. Relevant to CFD practitioners, tensor-network methodologists, and quantum-algorithm researchers benchmarking against classical baselines.

**Caveats** — Only a triply periodic box; no walls or complex geometry yet. Test case is deliberately under-resolved (32³) and validation is against another solver, not a converged reference; late-time divergence is unexplained. Intermediate χ must be allowed up to 256 (vs the exact 128) for accuracy. No wall-clock comparison against HiPSTAR is reported, so no demonstrated speedup; the Re-scaling of χ suggests industrially relevant Reynolds numbers remain out of reach, and the target χ≈500 case could not be run due to memory. Simultaneous-simulation accuracy degrades relative to single runs. Concurrent independent work reports similar division/square-root algorithms.

## 2. Pseudodeterminism and MA != NP^BPP in Communication Complexity

[arXiv:2608.26425](https://arxiv.org/abs/2608.26425) · [SciRate](https://scirate.com/arxiv/2608.26425)

*Thomas Watson*

**TL;DR** This paper gives a clean white-box lifting proof that some two-party partial function has *zero-sided-error* randomized communication complexity O(log N) but pseudodeterministic (two-sided-error) complexity Ω̃(√N), strengthening the recent STOC 2026 separation, which only achieved a two-sided-error upper bound. The same iterative machinery then yields MA ⊄ NP^BPP (= N·BPP) in communication complexity, resolving an open question from Göös's "landscape" survey.

**The big picture** A pseudodeterministic algorithm is a randomized one that, on every input, almost always outputs the *same* canonical answer — a property that lets you amplify confidence but that can cost you exponentially more resources. The paper shows that in two-party communication there are problems solvable by an extremely cheap randomized protocol that never errs (it may only say "don't know"), yet any protocol that commits to a canonical answer on every input, valid or not, must exchange nearly a square root of the input length in bits. The same technique separates Merlin–Arthur communication from nondeterminism with a randomized oracle, which pins down another subclass of the communication polynomial hierarchy — an area where explicit lower bounds are scarce and close to the current frontier.

**Key contributions**
- ZPP ⊄ psP in communication complexity: the hard function is in RP and coRP simultaneously, matching the Ω̃(√N) bound of prior work with a qualitatively stronger upper bound and a simpler proof.
- MA ⊄ NP^BPP in communication complexity, answering an open problem; the query-complexity analogue was known, but no lifting theorem for these classes exists.
- Query-complexity lower bound proofs re-engineered to be "liftable" (existing simplest proofs are not), including a new argument showing that in the N·BPP setting the acceptance probability is automatically re-boosted from >1/3 back to ≥2/3 via nearby valid inputs.

**How it works** Both hard functions compose a simple outer function with the inner-product gadget on h = 100 log n bits. The outer functions are weight-threshold conditions on the two halves of z (e.g. f = 1 if |z_→| ≥ n/3 and |z_←| = 0; f = 0 if the roles swap). The proof runs an iterative process on a triple (current z, a "structure" of hardwired coordinates of width w, a balanced rectangle R), using the packing lemma of Göös–Pitassi–Watson (with a small tweak to remove a stray log n) to boost the density of 1-inputs by passing to structured subrectangles. Each iteration is "safe" (√n bits flipped in the left half, potential k rises by ≤ d+13) or "unsafe" (k drops by at least half the increase in w). Since k ≥ 0, w stays ≤ 0.02n, so hardwiring never blocks progress; after √n/3 safe iterations z becomes a 0-input, contradicting the maintained 1-density invariant. For MA, a preprocessing phase fixes Merlin's witness (paying a 2^{-d} density loss, absorbed by amplifying to error 0.01·2^{-d}), and the iteration alternates between the slice R_z (to keep the right half all-zero) and the nearby valid slices R_{z^J} (where pseudodeterminism has bite).

**Why it matters** Relevant to anyone working on communication lower bounds, lifting, or the structure of the communication polynomial hierarchy; MA sits just below AM and S₂P, where no ω(log N) explicit bounds are known. The paper also flags concrete next targets: BPP ⊄ NP^RP, BPP ⊄ RP^RP, NP^BPP ⊄ NP^RP (the latter two open even in query complexity).

**Caveats** Both results are for *partial* functions (promise problems), and no general lifting theorem for psP or NP^BPP is obtained — the arguments are bespoke and tied to the inner-product gadget with logarithmic-size blocks. The lower bound is Ω̃(√N), not near-linear, and the constants (d = 0.01√n, error 0.01) are hand-tuned rather than optimized. The separations do not by themselves say anything about time-complexity analogues.

## 3. How quantum is quantum geometry?

[arXiv:2608.26269](https://arxiv.org/abs/2608.26269) · [SciRate](https://scirate.com/arxiv/2608.26269)

*Ady Stern, Felix von Oppen*

**TL;DR** A point particle carrying a *classical* magnetic moment that precesses in a momentum-dependent field **B**(**p**), with no kinetic energy term, reproduces almost the entire quantum-geometry phenomenology within Hamiltonian classical mechanics: the moment's longitudinal component ℓ∥ generates the anomalous velocity (Berry curvature), while its precessing transverse component ℓ⊥ generates the quantum metric, a position spread, an orbital moment, and — the striking result — an emergent inertial mass and Drude weight in a nominally dispersionless system, provided the applied force is position-dependent. Only equilibrium magnetization (Bohr–van Leeuwen), condensation/phase rigidity, and Brillouin-zone topology remain irreducibly quantum.

**The big picture** Quantum geometry has become a standard organizing concept for band phenomena, from anomalous Hall transport to the superfluid stiffness of flat bands, and is usually presented as an intrinsically quantum property of wavefunctions. This paper asks which of the associated observables genuinely need quantum mechanics, and answers by constructing a fully classical toy system — a spinning top whose precession axis depends on the particle's momentum — that reproduces almost all of them. The lesson is that most "quantum geometric" effects are really the generic consequence of fast degrees of freedom slaved to slow ones, so experimental signatures attributed to wavefunction geometry do not by themselves demonstrate quantumness; the genuinely quantum ingredients are condensation, thermodynamic magnetization, and the periodicity of momentum space that makes topology possible.

**Key contributions**
- Classical anomalous velocity ṙᵢ = ℓ∥ **b̂**·(∂ᵢ**b̂**×∂ⱼ**b̂**)Fⱼ, recovering the standard result at ℓ∥ = ħ/2, with ℓ∥ continuous rather than quantized.
- A classical geometric tensor χᵢⱼ = ℓ⊥²(∂ᵢ**b̂**·∂ⱼ**b̂** − i **b̂**·∂ᵢ**b̂**×∂ⱼ**b̂**) obeying det g = Ω²/4 and tr g ≥ |Ω|.
- Position spread ⟨δrᵢδrⱼ⟩ = (ℓ⊥²/2)∂ᵢ**b̂**·∂ⱼ**b̂** (classical origin of the metric bound on Wannier spread) and orbital moment m_z = eBℓ⊥²Ω_xy.
- Mass generation: a spring force k**r** rectifies the fast precession-induced oscillation, giving H_kin = (kℓ⊥²/4) tr g and m* ∝ (kℓ⊥²)⁻¹.
- Two-particle version: mutual interaction endows a pair of individually infinitely massive particles with a joint mass; for arbitrary V, H_kin = ⟨V(x₁−x₂)⟩ averaged over the fast orbits, i.e. V_q dressed by Bessel form factors J₀(qξ₁)J₀(qξ₂), with ξ_a = ℓ⊥|∂**b̂**/∂p_a|.

**How it works** Poisson brackets {ℓᵢ,ℓⱼ}=ε_{ijk}ℓ_k, {rᵢ,pⱼ}=δᵢⱼ, H = −**ℓ**·**B**(**p**)+V(**r**), with |**B**| = B fixed and large. Adiabatic elimination in a parallel-transported frame gives **ℓ** ≈ ℓ∥(**b̂** + **b̂**×**ḃ̂**/B) plus the precessing part; the O(1/B) tilt feeds ṙᵢ = −**ℓ**·∂**B**/∂pᵢ to give an O(B⁰) transverse velocity. The transverse component produces O(B) velocity oscillations of O(B⁰) amplitude ξ; a uniform force cannot rectify them, but a position-dependent force modulates ∂**b̂**/∂p at the precession frequency, and the two B factors cancel, leaving a B-independent drift expressible as a momentum gradient of an emergent dispersion.

**Why it matters** It sharpens claims about "quantum geometric" transport: anomalous Hall velocity, metric-bounded localization, orbital moments, and even the inverse-mass part of the flat-band superfluid weight have classical semiclassical analogues; only condensation supplies the quantum part. Relevant to flat-band superconductivity, nonlinear Hall, and semiclassical wavepacket theory.

**Caveats** Restricted to fixed |**B**| (a two-level/flat-band analogue) and the adiabatic B→∞ limit; momentum space is non-compact, so no topology. The emergent mass is not a true kinetic energy — it depends on interparticle distance and vanishes beyond the interaction range plus ξ₁+ξ₂. The two-particle result requires the two precessions to dephase (unequal B or ℓ⊥) so that averages factorize; correlated oscillations would kill the effect. ℓ⊥ is a free classical parameter with no fixed quantum counterpart (precession phase is undefined quantum mechanically). No disorder, scattering, or many-body treatment.

## 4. Least Variable Quantum Counting Processes

[arXiv:2608.26240](https://arxiv.org/abs/2608.26240) · [SciRate](https://scirate.com/arxiv/2608.26240)

*Bita Olamaei, Florian Meier, Costantino Budroni, Pharnam Bakhshinezhad, Giuseppe Vitagliano*

**TL;DR** The authors prove the long-conjectured tight variance bound for classical finite-memory counting processes — any *d*-state discrete-time automaton with mean first-tick time μ obeys *d*σ² ≥ μ(μ−*d*), saturated by a discrete Erlang ladder — and then numerically construct *d*-dimensional quantum counting processes that violate it. The optimal quantum processes have a pure initial state, a single-Kraus (coherent, non-Hermitian) no-tick evolution and a rank-one tick effect; in the large-mean/continuous-time limit their relative precision scales empirically as *d*^(7/3), faster than the quadratic scaling of known clock families.

**The big picture** How precisely can a device with limited internal memory time an event — say, emit a tick after a prescribed average delay with as little jitter as possible? For classical machines there is now a rigorous, tight trade-off: memory, average waiting time and jitter are locked together, and the best possible design is a simple staircase of states advanced by biased coin flips. Quantum machines with the same amount of memory can do strictly better, by keeping the system almost invisible to the detector for a long stretch and then coherently steering it into the detectable direction just when the tick is due. This sharpens the notion of a genuinely quantum temporal correlation and connects discrete counting automata to autonomous quantum clocks.

**Key contributions**
- Proof of the classical finite-memory variance bound for arbitrary *d* (previously proven only for *d*=2, conjectured otherwise), with the discrete Erlang/negative-binomial ladder as the saturating process.
- A discrete-time cost function CF_d = *d*σ² − μ(μ−*d*) whose negativity certifies non-classicality at fixed memory size.
- A general hazard-based lower bound CF_d ≥ 2*d*μ/h_max − (*d*+1)μ², a discrete-time analogue of precision–resolution trade-offs.
- Numerical optima violating the classical bound in every dimension examined, plus a closed-form qubit analysis giving CF₂/μ² → −0.5982 asymptotically within the single-Kraus family.
- Continuous-time optimization showing effective precision scaling ~*d*^(7/3).

**How it works** The classical proof Poissonizes the discrete chain: replacing each step by an exponential waiting time of rate λ produces a continuous-time absorbing Markov chain with generator λ(T₀−1) and the same number of transient states, whose absorption-time variance equals (σ²+μ)/λ²; applying the Aldous–Shepp optimality of the Erlang process there and mapping back yields the shifted bound σ²+μ ≥ μ²/*d*. For the quantum side, the no-tick map is taken as a single Kraus operator K₀ = U₀√M₀ with M₁ = (1−q)|Ψ⟩⟨Ψ|; moments are computed exactly via resolvent (discrete) or Lyapunov (continuous) equations, and CF_d is minimized over 4(*d*−1)+1 real parameters at fixed μ. Optimal solutions show a suppressed hazard followed by a sharp rise, and detector strength scaling 1−q ∝ 1/μ, so the discrete process converges to a rank-one quantum-jump Lindblad unraveling with H_eff = H − (iΓ/2)|Φ⟩⟨Φ|.

**Why it matters** It supplies a sharp, dimension-resolved classical benchmark for temporal correlations — useful for memory-cost/macrorealism-style certifications — and identifies the structural ingredients (coherent dark evolution plus weak rank-one detection) of maximally precise finite-memory quantum clocks. Relevant to quantum thermodynamics of timekeeping, quantum-jump/waiting-time statistics, and matrix-exponential distributions in applied probability.

**Caveats** The quantum results are numerical: the single-Kraus, rank-one ansatz is not proven globally optimal (verified only by unrestricted search in small *d*), and the qubit asymptotic statement holds only within that family. The *d*^(7/3) exponent is an effective finite-size fit that cannot persist, since Yang–Renner's asymptotic bound is quadratic; the crossover is unresolved. Everything assumes cyclic reset (renewal statistics) and time-homogeneous dynamics.

## 5. The Find Rows and Columns and Decode algorithm for quantum expander codes

[arXiv:2608.27211](https://arxiv.org/abs/2608.27211) · [SciRate](https://scirate.com/arxiv/2608.27211)

*Dimiter Ostrev*

**TL;DR** The paper gives a new linear-time decoder ("Find Rows and Columns and Decode") for hypergraph-product quantum expander codes that adapts Viderman's classical Find-Erasures-and-Decode without ever enumerating subsets of stabilizer generators. It works under weaker lossless expansion (δ < 1/3 versus 1/6, 1/8 for Small Set Flip variants and 1/10 for Small Set Find), and in the paper's benchmark example corrects ~0.944·s adversarial errors versus 0.062·s and 0.058·s for prior decoders — more than an order of magnitude — while running in time linear in blocklength and parallelizing to logarithmic depth.

**The big picture** Quantum error-correcting codes built from expander graphs come with decoders that provably fix any sufficiently small error, but the known ones are slow, demand very strong (hence very high-degree) expanders, and correct only a tiny fraction of the errors the expansion should allow. This work transplants a classical two-stage strategy — first localize a small region guaranteed to contain the error, then solve exactly inside it — into the quantum setting, exploiting the grid structure of the product code so that the localization runs independently on rows and columns. The result is faster, tolerates weaker expansion, and pushes the guaranteed correction radius up by more than a factor of fifteen in a representative case, answering open questions posed in two recent papers.

**Key contributions**
- A decoder whose two localization runs are driven only by the row and column supports of the syndrome, avoiding the Ω(2^d) cost of examining subsets of stabilizer generators.
- Expansion requirement relaxed to δ < 1/3, with the parameter β free in (δ, 1−2δ]; decoding radius (β−δ)/β · (min(γ_A|E|/d_A, γ_B|E|/d_B) − 1 + min(1/d_A, 1/d_B)).
- Replaces the O(n^{3/2}) erasure-decoding stage of Small Set Find and the O(n²) ReShape reduction by an O(n)-time linear-algebra step.
- Analysis stated for irregular graphs, using edge-count-based expansion rather than vertex counts.

**How it works** The "β-neighborhood" A^β(T) collects vertices sending more than a β fraction of their edges into T; iterating this gives increasing subgraph sequences 𝒢_ℓ(rs(W)) and 𝒢_ℓ(cs(W)). Containment lemmas (via auxiliary upper-bound sequences seeded by a set C, D of size at most the error weight) keep the whole execution inside the expansion regime; lossless expansion implies 2δ unique-neighbor expansion, giving geometric shrinkage of the uncovered error support and hence ℓ ≈ log|E| / log((1−β)/2δ). Correctness uses stabilizer-equivalence moves that peel off rows of X_A supported on unique neighbors. The final decode uses a *peeling* — an ordered matching making the relevant submatrix of H triangular and invertible — so the inverse can be applied in linear time or log depth, first correcting X_A, then X_B from the residual syndrome.

**Why it matters** Relevant to anyone building qLDPC decoders: it removes the exponential-in-degree constant that has made small-set decoders impractical, and lowers the degree floor since δ < 1/3 expanders need degree only ~3.

**Caveats** Limited to hypergraph products (distance ~√n), not the asymptotically good lifted-product/Tanner families. Adversarial-error worst case only — no random-error threshold, no noisy-syndrome or single-shot analysis. At β = 1−2δ, ℓ can be Θ(√n), so log depth requires β strictly smaller and a slightly reduced radius; an explicit example suggests this is not merely a proof artifact. Gate count carries an extra log|E|/log(1/2δ) factor, and the headline improvement is illustrated on one parameter choice.
