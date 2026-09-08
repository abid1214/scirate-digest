# SciRate Daily Digest — 2026-09-08

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Fanout Complexity of Symmetric Boolean Functions in $\mathsf{QAC}^0$

[arXiv:2609.05153](https://arxiv.org/abs/2609.05153) · [SciRate](https://scirate.com/arxiv/2609.05153)

*Boyan Xu, Lvzhou Li*

**TL;DR** For every symmetric Boolean function, the exact amount of fanout needed to compute it in constant-depth quantum circuits is pinned down by a single combinatorial parameter: the *transition radius* ρ(f), the distance from the innermost sign change of f (as a function of Hamming weight) to the nearer end of the weight interval. Computing f in QAC⁰ and implementing FANOUT_{ρ(f)} in QAC⁰ are equivalent under QAC⁰ reductions, so any symmetric f with ρ(f) ≥ n^δ is QAC⁰_f-complete even when computed with worst-case success probability only 1/2 + 1/polylog(n).

**The big picture** In quantum circuits, copying a bit to many places is not free the way it is classically, and whether shallow quantum circuits can do it remains a nearly thirty-year-old open problem, equivalent to whether they can compute parity. Recent work showed that preparing certain symmetric quantum states requires exactly a specific amount of copying. This paper shows that the same tight correspondence holds for *all* functions whose value depends only on how many input bits are one: a simple structural feature — how deeply inside the range of possible input weights the function's innermost value change sits — determines precisely how much copying power is necessary and sufficient. This unifies a scattered collection of hardness results for majority, thresholds, exact-weight, and modular counting functions under one criterion, and shows that if parity is genuinely hard for shallow quantum circuits, then any shallow-computable function with high approximate degree must be asymmetric.

**Key contributions**
- Exact characterization: f ∈ QAC⁰ ⇔ FANOUT_{ρ(f)} ∈ QAC⁰ for symmetric f.
- A single criterion (ρ(f) ≥ n^δ) implying QAC⁰_f-completeness, recovering PARITY/MAJORITY and *strengthening* prior THRESHOLD_k, EXACT_{n/2}, MOD_q results from exact/1-poly-approximate computation to worst-case success 1/2 + 1/polylog(n).
- Via Paturi's deg̃(f) = Θ(√(n·ρ(f))): if PARITY ∉ QAC⁰, every QAC⁰ function of approximate degree n^{1/2+Ω(1)} is nonsymmetric.

**How it works** *Fanout → f*: with k = ρ(f), all transitions lie in the outermost k weight layers, so f (up to output negation) is an OR of ≤2k EXACT_j predicates with j < k or j > n−k; each is computable using FANOUT_k (Grier–Morris–Wu, reproved in an appendix via a modular-hashing threshold construction), evaluated in parallel after two FANOUT_k layers.
*f → fanout*: restrict to m = 2k−1 inputs (zeroing the rest) so the chosen transition sits at the center. For g = Pr[C=0] − Pr[C=1], the worst-case guarantee forces |g(x)−g(y)| ≥ 4ε on all Θ(2^m√k) adjacent weight-(k−1)/k pairs, giving total influence I[g] ≥ γ²√(m/2) with γ = 2ε. Since ‖g‖ ≤ 1, Parseval plus the influence-level identity yields W^{≥ℓ}[g] ≥ γ²/√(8m) at level ℓ ≈ ε²√(2m) ≥ m^{1/3}. Feeding this into the Gretta–Gupta–Joshi Fourier-tail-to-fanout reduction produces FANOUT_ℓ; a three-level fanout tree then gives FANOUT_k.

**Why it matters** It converts "is this specific symmetric function hard?" into a purely combinatorial computation, and cleanly delineates the frontier: symmetric functions can no longer be a route to exhibiting high-approximate-degree functions in QAC⁰ unless parity is easy.

**Caveats** The equivalence is asymmetric (exact computation from fanout; fanout from bounded-error computation), and the 1/2 + 1/polylog threshold is required by the ℓ ≥ m^{1/3} condition of the Fourier-tail reduction — average-case correlation results for PARITY and MAJORITY are not subsumed. Sub-polylog transition radius is trivially handled by known polylog fanout, so the content lies in ρ(f) ≥ polylog. Nothing here resolves the fanout question itself, and ancilla overhead is polynomial but not optimized.

## 2. Efficient Quantum Error Correction from Three Dimensional Qubit Control

[arXiv:2609.04459](https://arxiv.org/abs/2609.04459) · [SciRate](https://scirate.com/arxiv/2609.04459)

*Kevin Yipu Wu, Ohik Kwon, Maxwell F. Parsons*

**TL;DR** — The authors take the fixed [[144,12,12]] bivariate-bicycle (gross) code and compare a planar four-register neutral-atom embedding against a four-plane, triangular-lattice 3D embedding, holding code, syndrome-extraction circuit, and noise model constant. The 3D layout cuts the transverse footprint from 4608 µm² to 1237 µm² (~4× areal logical-qubit density, ~42× vs. twelve distance-11 surface codes) and halves the syndrome-extraction round (1605 µs vs. 3002 µs planar, 2469 µs for a systolic baseline), with 17 vs. 25 moves and 404 µm vs. 1512 µm total transport, at essentially unchanged simulated logical error rates.

**The big picture** — High-rate quantum LDPC codes promise large savings in physical qubits, but their parity checks connect qubits that are far apart, so on real hardware most of the cost is shuttling atoms around rather than performing gates. Neutral-atom tweezer arrays could in principle be stacked into multiple layers, and this work asks whether that extra spatial dimension buys anything beyond raw qubit count. It does: packing the code's four registers into stacked planes shortens the travel needed to realize the same connectivity, halving the error-correction cycle and quadrupling how many logical qubits fit inside a microscope's limited field of view.

**Key contributions**
- First 3D (four-plane) embedding and transport schedule for the gross code on neutral atoms, with data registers static and both check registers rigidly translated by a single shared waveform.
- A blockade-overlap "interaction region" construction: feasible displacements for each rigid check–data group are intersected so multiple groups execute at one stop; a precedence-constrained DP over witness points finds a 16-stop tour (vs. exact Held–Karp 24-stop planar tour).
- Areal vs. volumetric logical-qubit-density metrics, arguing field of view, not volume, is the binding optical constraint.
- A time-vs-extended-distance Pareto analysis over 36 interaction orderings, separating hook-error propagation (circuit property) from routing cost (layout property).

**How it works** — Registers L, Z, X, R occupy 4 µm-spaced planes of a common 4 µm-pitch triangular lattice; register-to-height assignment was chosen by enumeration under the routing objective. Schedules are compiled to Stim with a one-parameter circuit-noise model (depolarizing gates/measurements at p, Pauli-twirled T1/T2 only during idle and transport, transfer faults 0.16p), decoded by BP-OSD (order 10) versus PyMatching for surface codes, 12-round memory experiments to 400 logical failures per point.

**Why it matters** — It gives a quantitative, schedule-level argument that hardware dimensionality is a codesign knob for qLDPC overhead, relevant to anyone building 3D tweezer control or estimating fault-tolerant footprints.

**Caveats** — The 3D device is an extrapolation; single-shot multi-plane readout has no demonstration. Volumetric density shows no gain (6.1 vs 6.5 ×10⁻⁴ µm⁻³) — the win is purely transverse, and planar layouts are assigned an arbitrary 4 µm effective thickness. Logical error curves converge to the surface-code baseline; the 3D advantage is speed/space, not protection. No leakage, atom loss, crosstalk, or correlated noise; decoder latency excluded despite ms-scale cycles. The appendix stop counts (16 visits, s₁…s₁₈, 19-stop claim) are internally inconsistent. The n^{1/12} asymptotic scaling argument is heuristic and untested.

## 3. Lindblad Multiproduct Formulas

[arXiv:2609.05024](https://arxiv.org/abs/2609.05024) · [SciRate](https://scirate.com/arxiv/2609.05024)

*Niall F. Robertson, Andrea D'Urbano, Anton Dekusar, Max Rossmannek, Eric D. Switzer, James R. Garrison, Nicolas Lorente, Igor Pasichnyk et al.*

**TL;DR** The authors propose Lindblad Multiproduct Formulas (L-MPF), an error-mitigation scheme in which the *coefficients* of a linear combination of differently-noisy hardware expectation values are obtained by minimizing a Lindblad-superoperator projection cost function evaluated with 2D tensor networks contracted via loop-corrected belief propagation. Because tensor-network error enters the final estimate only multiplied by residual hardware error (second order), low-bond-dimension classical simulations that badly mispredict the observable itself can still mitigate it accurately; demonstrated on 65 qubits of a heavy-hex IBM device for a 2D discrete time crystal, with a 3–5.6× GPU speedup for the classical stage.

**The big picture** Error mitigation on noisy quantum processors and classical tensor-network simulation are usually framed as competitors. This work argues they are complementary: even when a classical simulator cannot get the answer right, it can compute the much easier auxiliary quantities needed to tell a quantum computer how to combine several noisy runs into a better estimate. The result is a hybrid workflow that beats both the raw hardware and the classical simulator used alone, and that comes with an error bar — something the widely used "rescale against an exactly solvable point" heuristic lacks.

**Key contributions**
- L-MPF: a multiproduct formula over *noise levels* rather than Trotter step sizes, with coefficients from minimizing ‖⟨O|Λ_{λ₀} − Σcᵢ⟨O|Λ_{λᵢ}‖² subject to Σcᵢ = d, where d comes from Clifford rescaling.
- An error-propagation analysis: the residual error is ε_proj + (1/d)Σσ_{cᵢ}ε^O_{λᵢ}; ill-conditioning of the Gram matrix Fᵢⱼ amplifies coefficient errors only along directions where Σεᵢ|O_{λᵢ}⟩ ≈ 0; uniform errors on Fᵢⱼ cancel identically under the sum constraint.
- *Ergodic amplification*: amplify the XY coupling ε (γ = 1, 1.4, 1.8) instead of noise rates, giving PEA-like damping at zero sampling overhead, since L-MPF needs no assumed functional form for extrapolation.
- First use of loop-corrected BP on 2D tensor networks inside a mitigation workflow, with no bespoke contraction path (avoiding the quadratic bond-dimension cost of MPO/TNO middle-out contraction), plus a GPU port.

**How it works** Pauli–Lindblad noise is learned on device; the vectorized observable is evolved in the Heisenberg picture as a heavy-hex tensor-network state under Λ_{λᵢ}; overlaps Fᵢⱼ are contracted with BP plus loop corrections, coefficients are optimized at several truncation thresholds, and the resulting Σcᵢ⟨O⟩_{λᵢ} is extrapolated to zero truncation error and compared against a purely classical bond-dimension extrapolation.

**Why it matters** It reframes classical simulators as *mitigation oracles* rather than rivals, and makes the workflow modular — future BP/loop-correction advances plug in directly. Relevant to anyone doing utility-scale hardware experiments where ZNE bias and PEC sampling cost are the bottleneck.

**Caveats** The reference "truth" is itself a high-bond-dimension BP simulation (ε_χ = 10⁻⁸), not exact. Only a single-site Z on one qubit over 10 Floquet cycles is shown. Ergodic amplification is explicitly a problem-specific heuristic that can produce impractically large error bars if the perturbed circuits stray too far; the PEA variant already shows overlapping error bands at γ = 2, 3. Convergence in ε_χ is non-monotonic, and the first two extrapolation points are discarded by hand. Error bars are heuristic, and the uniform-Fᵢⱼ-error cancellation is an assumption, not a demonstrated property.

## 4. Exact quantum spin liquids with topological order on maple-leaf and trellis lattices

[arXiv:2609.04319](https://arxiv.org/abs/2609.04319) · [SciRate](https://scirate.com/arxiv/2609.04319)

*Li Ern Chern, Roderich Moessner, Claudio Castelnovo*

**TL;DR** The authors build Γ-matrix ("generalized Kitaev") models on the two penta-coordinated Archimedean lattices not yet treated this way — maple-leaf and trellis — obtaining exactly solvable $\mathbb{Z}_2$ spin liquids. Quantum Monte Carlo fixes the ground-state flux sector (0 on hexagons, $\pi$ on squares, uniform $\pm\pi/2$ on triangles, i.e. spontaneous time-reversal breaking), and the resulting band structures host Chern numbers 0 (toric code) and $-1$ (Ising/non-Abelian), with a closed-form mass term giving the phase boundary. Crucially, the maple-leaf model realizes the first time-reversal-breaking case where the $e/m$ anyon labeling changes without any fermion gap closing in the vortex-free sector — the change is instead flagged by gap closings in two-vortex sectors.

**The big picture** Frustrated lattices built from triangles are prime hunting grounds for quantum spin liquids, but realistic isotropic models there are not solvable and numerical methods disagree. Here, by choosing bond-dependent anisotropic couplings tailored to lattices where each site has five neighbours, the authors obtain models solvable exactly, with fractionalized excitations and emergent gauge fields, and read off which kind of topological order arises in each region of coupling space. Beyond expanding the catalogue of exactly solvable spin liquids, the work shows that the identity of the fractionalized particles can change across a phase without any visible signature in the ground state — a subtlety detectable only by looking at excited sectors.

**Key contributions**
- Unique (up to colour permutation) five-colour bond assignments on both lattices; point-group symmetry reduces the couplings to a two-dimensional triangular parameter space.
- Replica-exchange QMC (sign-problem free, accelerated by a Green's-function kernel polynomial method, $M=256$–512, up to $L>5$) at 28 parameter points establishes the ground-state flux sector, supporting the extended flux-phase conjecture $W_p=-(\pm i)^{|\partial p|}$ on non-bipartite lattices.
- Analytic mass terms: maple-leaf $\mathsf{m}/\sqrt2=[\sum(\Delta J)^2]^{1/2}-\sqrt6 J_{zx}$ (gap closes at $\Gamma$); trellis $\mathsf{m}=-4J_{zx}+2J_{zz}$ at M — exact $\nu=0/-1$ boundaries.
- Anyon assignment in dimer limits via fusion-rule/fermion-parity corollaries, bypassing the failure of degenerate perturbation theory for odd-length plaquettes.
- Numerical scan of all 45 two-vortex sectors on a $16\times12$ torus: gaps vanish along $J_{x0}=J_{y0}\ge(1+\sqrt3)J_{zx}$ whenever a hexagon hosts a vortex, splitting the $\nu=0$ region into two anyon-labelling domains.

**How it works** Five anticommuting $4\times4$ Γ matrices (two spin-1/2 per site) are represented as $\Gamma^\lambda_i=ib^\lambda_i c_i$, reducing the Hamiltonian to free Majoranas hopping in a static $\mathbb{Z}_2$ gauge field. Since Lieb's theorem fails (non-bipartite), fluxes are sampled thermally; heat-capacity data show fractionalization near $T\sim1$ plus a sharp flux-ordering/TRS-breaking peak (and, at anisotropic trellis couplings, separate square- and triangle-flux ordering scales). A translationally invariant gauge then permits momentum-space Chern-number and two-band effective-Hamiltonian analysis.

**Why it matters** Extends the exactly solvable Kitaev family to two much-discussed frustrated geometries, supplies clean benchmarks for the flux-phase conjecture, and gives a concrete, TRS-breaking illustration that anyon-species assignment is an excited-state-sensitive property.

**Caveats** Flux sectors verified only at 28 discrete points and modest sizes; domain-wall effects relegated to supplement. The Γ-matrix interactions require quadrupolar/spin-orbital mechanisms with no known material realization; anyon identification relies on corollaries of a companion preprint; two-vortex gaps are "nearly (if not exactly)" degenerate within groups.

## 5. SIC dimension towers via cyclotomic polynomials

[arXiv:2609.04431](https://arxiv.org/abs/2609.04431) · [SciRate](https://scirate.com/arxiv/2609.04431)

*Gary McConnell*

**TL;DR** The paper shows that the SIC dimension tower attached to a real quadratic field — dimensions built from traces of powers of the fundamental totally positive unit — is just one row (level 3) of a two-dimensional cyclotomic array indexed by the minimal polynomials of 2cos(2π/m), with the two auxiliary SIC factors appearing as the ramified levels 1 and 2 of the quotient of the multiplicative group by inversion. The technical engine is a single closed composite norm relation for the family 1 − ζ_m ε^k across the cyclotomic tower, from which exact ranks of apparition, p-adic valuations, and a link to Wall–Sun–Sun/Leopoldt-mod-p follow uniformly at every level.

**The big picture** The known number-theoretic reformulation of Zauner's conjecture on symmetric informationally complete quantum measurements attaches to each candidate dimension a real quadratic field, generating an infinite ladder of dimensions from powers of a fundamental unit. This work shows that ladder is not special: it is one horizontal slice of a much larger arithmetic array, with the two auxiliary factors that appear in the SIC formulation being exactly the two branch points of a natural two-to-one map. Placing the threefold symmetry central to Zauner's conjecture in this wider setting connects it cleanly to the notoriously hard question of exceptional prime divisibility of unit groups — the analogue of Wieferich/Wall–Sun–Sun primes for real quadratic fields — and to p-adic L-values via the p-adic class number formula.

**Key contributions**
- A closed composite norm formula (Thm 1) for the two-parameter family over K(μ_{mn})/K(μ_m), with a Möbius-twisted product of Galois-conjugated terms, proved by peeling primes one at a time.
- Identification of the SIC tower as level m=3 (since Ψ₃(t)=t+1), with d−3 and d+1 as the ramified levels m=1,2 arising from the different of G_m → A¹ generated by z − z⁻¹.
- Theorem A: bijectivity of (D,k) ↦ t_k onto integers ≥3; density-zero images at all levels except m ∈ {3,4,6}; exact support ρ_m(p) = o(p)/m when m | o(p); exact valuation v_p(Ψ_m(t_k)) = a_p + v_p(k), doubled at branch levels.
- A "leading edge" Möbius inversion isolating first occurrences, plus existence of primes with o(p)=n for all n>12 via the Lehmer-sequence primitive divisor theorem.
- A local false Tate (Kummer–cyclotomic) reformulation where the Chebyshev shift k↦pk becomes two equal partial norms on a divided grid; a_p−1 is the local Kummer depth of ε^{o(p)}.
- Exhaustive Wall–Sun–Sun tables for 1<D<50 up to p ≈ 1.74×10^13 (all found have a_p=2, except two with a_p=3).

**Why it matters** It gives a clean, level-uniform structural account of the SIC dimension arithmetic, replacing ad hoc SIC-specific arguments (cf. earlier m=3 results) with a general cyclotomic distribution framework, and makes explicit the equivalence a_p ≥ 2 ⟺ v_p(L_p(1)) ≥ 1 when p ∤ h_K. Relevant to SIC-POVM/Stark-unit researchers and to number theorists working on p-rationality.

**Caveats** The framework detects and quantifies a_p ≥ 2 but does not predict when it occurs; the authors' own extensive statistical tests (regulator, splitting type, unit heights, biquadratic quotients, dilogarithm functionals) found no reproducible predictor, consistent with a 1/p heuristic. No new SIC existence results follow. Many ingredients (cyclotomic norm identities, lifting-the-exponent, Chebyshev/Lucas factorizations) are classical; the novelty is the assembly and the geometric identification of branch levels. Statements assume p ∤ 2mD and generically K ∩ Q(μ_{mn}) = Q; the false Tate material is heuristic/programmatic, with field-norm interpretation valid only at non-collapsed squares.
