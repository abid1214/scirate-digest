# SciRate Daily Digest — 2026-10-01

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. All Unitaries Have Constant Depth Quantum Circuits

[arXiv:2609.40351](https://arxiv.org/abs/2609.40351) · [SciRate](https://scirate.com/arxiv/2609.40351)

*Barak Nehoran, Henry Yuen*

**TL;DR** Every unitary on n qubits can be approximated in operator norm to error ε by a circuit of one- and two-qubit gates of depth poly(n, log 1/ε) using 2^{O(n)} ancillas — and constant depth if unbounded fan-out is allowed. The construction reduces arbitrary unitary synthesis to *three* queries to a diagonal quadratic-phase oracle interleaved with two Fourier transforms, and that quadratic phase is a sum of two-register-local terms, hence massively parallelizable.

**The big picture** It has long been known that an arbitrary unitary on many qubits can be built from elementary gates, but only with an exponentially long sequence of them, and it was open whether exponential *time* (as opposed to exponential *hardware*) was unavoidable even with unlimited scratch space. This paper shows it is not: with exponentially many ancilla qubits, any unitary can be performed in polynomial, and with a powerful copying primitive even constant, parallel time. The construction routes through an unexpected connection to local decoding and private information retrieval, where a small constant number of queries into a large encoded object suffices to recover what you want. This reframes the hardness of general quantum operations as a question of total resources rather than circuit depth.

**Key contributions**
- Depth poly(n, log 1/ε) circuits with 2^{O(n)} ancillas for arbitrary n-qubit unitaries; constant depth with unbounded fan-out.
- A "three-chirp" unitary synthesis identity: for traceless real symmetric unitaries (WLOG by an equivalence lemma), the target is realized exactly in the continuum, and to error ε after discretization, by Q–F–Q–F–Q sandwiched between an encoding isometry and its adjoint.
- A rigorous discretization analysis bounding both aliasing and Gaussian-tail truncation simultaneously via Poisson summation; error O(N^{3/2}K^{3/4}e^{−πK/8}) with grid size K = Θ(log(N/ε)) per register.
- An explicit link between Aaronson–Kuperberg unitary synthesis and 3-query LDC/PIR-style structure.

**How it works** The input index x ∈ [N], N = 2^n, is encoded into N bosonic-like registers as a single "excitation": discretized harmonic-oscillator ground states everywhere except a first-excited state in register x. Each register holds K grid points (K = Θ(log(N/ε)), a power of two), so 2^{O(n)} ancilla qubits total. The algorithm applies a diagonal quadratic phase exp(i αᵀSα/2), a Fourier transform, and repeats — the metaplectic "chirp–Fourier–chirp" factorization of a symplectic map. Correctness is proven by comparing the half-algorithm isometry to an *ideal* isometry that applies a square root of −iS directly, using a wrapped sampling map that exactly intertwines continuous and discrete Fourier transforms. Parallelism comes from two facts: the grid Fourier transform factorizes into per-register QFTs on K points conjugated by diagonal phases, and the quadratic phase decomposes into N² two-register terms that commute and can be applied simultaneously on fan-out copies.

**Why it matters** Circuit depth and circuit size are now provably decoupled for general unitaries; depth lower bounds must assume bounded ancillas. Relevant to anyone studying unitary synthesis, parallel quantum complexity (QNC⁰ with fan-out), and oracle-based complexity separations.

**Caveats** Size remains exponential — at least 2^{O(n)} gates and ancillas; only depth improves. Gates carry arbitrary real angles derived from the target matrix, so the construction is non-uniform and assumes exact-angle two-qubit gates. Constant depth requires unbounded fan-out, a strong nonlocal primitive. Ancilla "leakage" (imperfect reset) is bounded only to the stated ε-type accuracy. The LDC/PIR connection is structural; quantitative consequences in either direction are not developed in the excerpt shown.

## 2. Quantum circuit compilation with constant overhead

[arXiv:2609.39092](https://arxiv.org/abs/2609.39092) · [SciRate](https://scirate.com/arxiv/2609.39092)

*Chenyi Zhang, Xinyu Tan, Robin Kothari, David Gosset, Craig Gidney*

**TL;DR** The usual logarithmic overhead of compiling arbitrary one- and two-qubit gates into {H, T, CNOT} can be removed entirely: any circuit with G arbitrary gates can be implemented to inverse-polynomial diamond-norm error by an adaptive circuit with only O(G) elementary gates, which a counting argument shows is optimal. For the "dyadic" gate set (Clifford+T plus all π/2^j Z-rotations), the cost is O(G + log(1/ε)), enabled by a new O(n)-gate, 2^{-n}-accurate *unitary* preparation of the n-qubit phase gradient state (improving Jones's O(n log n) expected-cost adaptive construction).

**The big picture** Quantum algorithms are usually written using continuous rotations, but real fault-tolerant hardware offers only a finite instruction set, so every rotation must be approximated — costing a logarithmic factor per gate that everyone has learned to live with. This work shows that factor is not actually necessary: by letting the compiled circuit use mid-circuit measurements and classical feedback, and by recycling a small shared pool of specially prepared auxiliary qubits, the total instruction count becomes proportional to the original gate count, with accuracy good enough for essentially any practical application. A matching impossibility argument shows this is the best achievable for arbitrary input gates. The result also sharpens a widely used subroutine for preparing a standard resource state used in arithmetic and Fourier-transform circuits.

**Key contributions**
- Constant-overhead compilation: O(G) gates over {H,T,CNOT} for 1/poly(G) error, plus a counting lower bound showing superpolynomially small error forces superlinear gate count even for depth-1 product-state preparation.
- O(G + log(1/ε)) compilation for the dyadic gate set, matching the Ω(log(1/ε)) lower bound (shown to apply to dyadic gates); ancilla cost reducible to O(log(G/ε)).
- Optimal phase gradient state preparation: unitary, worst-case O(n) gates, error 2^{-n}.
- Concrete T-count: ≤ 8G + o(G) T gates for G Z-rotations at error 1/√G (≈8 T per rotation).

**How it works** Two gadgets drive the compilation. State injection consumes a resource state R(θ)|+⟩ to apply R(θ), failing w.p. 1/2 with correction R(2θ); the phase-halving gadget (Gidney–Fowler) runs this in reverse, consuming R(2θ) and a catalyst to produce two R(θ) applications. Keeping one "catalyst" and one "bank" copy per angle, a recursive algorithm alternates withdrawals and deposits so the bank never depletes; Hoeffding gives worst-case cutoff t_max = O(G + log(1/ε)). For arbitrary gates, randomized compilation (Campbell/Hastings mixing lemma) rounds angles to a grid of spacing 2π/D at error O(1/D²) per gate; for general inverse-polynomial ε, grid points are written in base B = O(√G) so each rotation is r = O(1) digits, shrinking the resource state to O(rB) qubits prepared by Ross–Selinger at o(G) cost. The phase gradient theorem expands e^{-iH} as an LCU with 1-norm ≤ e^π, implements SELECT in O(n) via a tree encoding plus Holmgren–Rothblum multiselection circuits, and applies 100 rounds of exact amplitude amplification.

**Why it matters** Removes a log factor that quietly multiplies the cost of every resource estimate for fault-tolerant algorithms, and the core protocol (gadgets plus a resource-state bank) is implementable. Relevant to compiler designers, resource estimators, and anyone budgeting T-counts.

**Caveats** Adaptivity is essential; whether randomized-unitary compilation suffices is open. The O(G) constant grows with the polynomial degree of the target error, and exponentially small error is provably out of reach. The optimal phase-gradient construction needs elaborate coherent reversible circuits and 100 amplification rounds — impractical near-term; substituting Jones's method gives a more practical O(G + log(1/ε)log log(1/ε)) expected-cost variant.

## 3. Testing quantum Gaussianity with constant sample complexity

[arXiv:2609.40270](https://arxiv.org/abs/2609.40270) · [SciRate](https://scirate.com/arxiv/2609.40270)

*Mahtab Yaghubi Rad, Ricard Puig, Saksham Hassanandani, Luke Coffman, Jens Eisert, Carlos Bravo-Prieto, Antonio Anna Mele*

**TL;DR** The paper proves that the known exact few-copy symmetry tests for Gaussianity — the two-copy Majorana/matchgate identity for fermions and passive copy-mixing interferometry for bosons — are globally *robust*: any pure state at trace distance ≥ ε from the pure Gaussian family is rejected per round with probability Ω(ε²), with constants independent of the number of modes and, for bosons, of energy. This gives Θ(ε⁻²log(1/δ)) sample complexity (matching lower bounds even for arbitrary collective measurements), improving the previous O(nε⁻²log(1/δ)) fermionic bound and removing bosonic energy assumptions.

**The big picture** Gaussian states are the canonical "easy" states of fermionic many-body physics and quantum optics, and certifying that a lab-prepared state really is Gaussian is a basic experimental task. Simple interference tests that accept Gaussian states perfectly have long been known, but nobody could rule out that non-Gaussian states a fixed distance away might sneak through with vanishing detection probability as the system grows. This work shows the detection probability is bounded below by a constant depending only on the distance, so a fixed number of experimental repetitions suffices no matter how large the system or how energetic the state — and the required measurements are ones already demonstrated on hardware.

**Key contributions**
- Mode-independent, energy-independent robustness for pure fermionic Gaussian states, Slater determinants, general/centered bosonic Gaussian states, and coherent states; no parity promise needed for fermions.
- Matching lower bounds establishing optimality in both ε and δ.
- Tolerant testers distinguishing distance ≤ ε_A from ≥ ε_B using O((ε_B−ε_A)⁻²log(1/δ)) copies, with joint measurements on q = O(1/η) copies.
- The "gradient-flow method": a general recipe converting exact few-copy symmetry characterizations into quantitative testers.

**How it works** Membership in the (nonlinear) target family becomes membership of the tensor power in a fixed linear accepted subspace, so rejection is R(ψ)=‖Qψ^{⊗q}‖². The core trick: on three copies, average the two-copy acceptance projector over the three pairs, T=(P₁₂+P₁₃+P₂₃)/3. Representation theory (SO(3)/SU(3) copy-rotation representations, uniform over mode number and over fixed photon-number sectors) bounds T's spectrum away from the common accepted subspace, which — since overlapping pairs share a copy — translates into a gradient inequality ‖∇R₂‖₂² ≥ 16R₂(κ−R₂) with κ mode-independent. Following negative gradient flow on the one-copy unit sphere then converges to an exactly accepted state with total path length O(√R₂), so d(ψ) ≲ √R(ψ). A parallel "closest-target geometry" argument expands around the nearest target, using normal stationarity (deviation has no tangential component) plus a local sensitivity coefficient λ to get sharp near-family rejection, which drives the tolerant result. Displaced bosonic Gaussians require an extra step: a four-copy argument (difference port cancels the common displacement, reduced to the coherent-state bound) transferred to three copies.

**Why it matters** It closes the testing-vs-tomography gap (tomography needs Θ(n²/ε²)) and certifies that experimentally realized Bell sampling and tritter/photon-counting protocols are provably sound at constant cost. The gradient-flow machinery looks reusable for other symmetry-defined families (stabilizer states, product states).

**Caveats** Guarantees apply only to *pure* inputs — testing against mixed Gaussian families is known to be exponentially hard. Tolerant testing holds only in the small-threshold regime ε_A ≤ cη with unspecified universal c, and the block size blows up as 1/η. Constants κ, λ are not quantified in the summary text. Whether adaptive single-copy measurements suffice remains open. Concurrent independent work by Iyer et al. reports overlapping results.

## 4. Parallel algebraic surgery for qLDPC codes with constant shuttling depth

[arXiv:2609.39874](https://arxiv.org/abs/2609.39874) · [SciRate](https://scirate.com/arxiv/2609.39874)

*Tian-Gang Zhou, Boren Gu, Jens Eisert, Chen Zhao*

**TL;DR** The authors build code surgery for lifted-product (LP) qLDPC codes entirely at the group-algebra level: the auxiliary "tube" is itself an LP code, attached through a rank-one coordinate map, so the merged code inherits the cyclic (circulant) structure of the data code. This lets all the ancilla–data matchings in a syndrome round be realized as uniform cyclic shifts, giving constant AOD shuttling depth under stated layout assumptions; in a neutral-atom hardware model a merged code measuring 33 canonical logical operators in parallel runs at ~1.1–1.2× the memory cycle time versus ~1.8–3.3× for single-observable graph-based surgery, with ~41% fewer qubits.

**The big picture** High-rate quantum codes promise far fewer physical qubits per logical qubit, and reconfigurable atom arrays can supply the long-range connectivity they need by physically moving atoms. But most surgery schemes for logical measurements attach an unstructured auxiliary gadget, destroying the regular symmetry that made the code cheap to operate and forcing complicated, slow atom rearrangements. Here the logical measurement, the auxiliary code, and the atom-movement schedule are designed together so the regular symmetry survives, so each measurement round reduces to a fixed number of rigid collective shifts and many logical measurements can be done at once. The upshot is that the algebraic structure of high-rate codes buys not only space savings but also faster, simpler logic.

**Key contributions**
- Algebraic surgery: data code LP(A,B), auxiliary LP(A′,D) with ker D rank-one and a unit coordinate, attached via f₁ = (I⊗ε_jε_q^T, 0); the measured logical subspace is exactly [f₁ ker ∂₁] = ker A′ ⊗ ε_j.
- Shuttling-depth taxonomy: O(log n_a + log l) for general seeds, O(log n_a) with boundedly many distinct monomials, O(1) when nonzeros also lie on boundedly many diagonals; graph-based auxiliaries need O(log w).
- Addressability theory: canonical logical fibres (Künneth + systematic kernel/cokernel bases) and CRT packets; selector rows H_L^fib and g_S·ε_k^T carve out fibres or translation-invariant packets, with sparse g_S (e.g. 1+x^11 for l=33, d_S=11, weight 2) keeping routing cheap.
- Algebraic adapters giving l joint PPMs P_a Q_{a+s} between blocks with equal lifts, and gcd(l₁,l₂) PPMs for unequal lifts (e.g. 33 and 11).
- Amortization analysis: N_aux = N_shared + l·s_T·n_D, so per-PPM auxiliary cost falls as more packets are addressed.
- Explicit CRT atom layout (a ↦ (a mod 3, a mod 5) for l=15) realizing cyclic shifts as AOD row/column shuffles; full shuttling-time and circuit-level simulations.

**How it works** Everything is done over R_l = F₂[x]/(x^l+1) with odd l, so x^l+1 is square-free and CRT splits R_l into fields, removing torsion in the Künneth decomposition and making kernels computable component-wise. Appending selection rows to A restricts ker A′ to one normalized kernel generator (a fibre) or to idempotent-projected subspaces (packets); the tube factor D adds redundancy without changing the kernel. Monomial entries lift to circulant permutations = rigid shifts. Benchmarks use 12 μm spacing, a_max = 5500 m/s², 1 μs gates, rest-to-rest moves τ = 2√(L/a_max); LERs from 20-round Stim-style sampling decoded by Relay-BP with BP-LSD fallback.

**Why it matters** Resource estimates for high-rate architectures usually ignore shuttling; this work shows the two can be reconciled, and that parallel logical measurements on overlapping supports (useful for compiling lattice-model Clifford layers) are available almost for free. Relevant to anyone compiling fault tolerance on neutral atoms.

**Caveats** No distance lower bound is proven for merged codes — distances are checked case by case and the l=33 instance only has d ≤ 20. Addressability is constrained by cyclic symmetry, and residual kernel directions K_res must be separately removed or absorbed. Z-basis surgery LER is up to an order of magnitude worse than memory; idling errors are omitted, as are readout, reset, trap transfer, and intra-block collision avoidance in the timing model. The graph-based baselines are run as l replicated single-observable gadgets, and the competing parallel hypergraph-surgery construction is not benchmarked.

## 5. Fault Tolerant Quantum Phases of Matter

[arXiv:2609.39879](https://arxiv.org/abs/2609.39879) · [SciRate](https://scirate.com/arxiv/2609.39879)

*Colin V. Coane, Shouzhen Gu, Aleksander Kubica*

**TL;DR** The authors define a notion of mixed‑state phase equivalence in which two *convex sets* of states (e.g. code spaces) are equivalent if shallow quantum‑local circuits — local channels plus local measurements plus global classical feedforward — can transfer the encoded logical information back and forth *while every operation, including measurement, is noisy*. They show that having a nonzero recovery threshold ("stability") is a property of a whole phase, that finite‑depth locally reversible channel circuits between stable sets are automatically fault tolerant, and that 2D and 3D color codes are in the same fault‑tolerant phase despite being in different local‑channel phases. They also prove a no‑go: shallow measure‑and‑correct preparation circuits with point‑like syndromes are not fault tolerant.

**The big picture** Existing classifications of phases of matter ask whether two states can be converted into each other by shallow local operations, possibly with measurements and classical feedforward. But on real hardware every gate and every measurement outcome can be faulty, and a single flipped outcome can trigger a globally wrong correction. This work rebuilds the classification around the question that matters for quantum computing — can encoded information be moved reliably in both directions by noisy shallow circuits? — and finds that this yields a coarser, operationally meaningful notion of phase that naturally handles code switching and subsystem codes, while ruling out many popular measurement‑based state‑preparation recipes as genuinely robust.

**Key contributions**
- Phase equivalence defined between convex sets equipped with decoding maps, with fault tolerance as part of the definition (residual noise must stay in a controlled noise class with threshold, and be recoverable); shown to be a valid equivalence relation (composition lemma).
- Stability (nonzero local‑stochastic recovery threshold) is a phase invariant; proved for LDPC codes with polynomially scaling distance, and disproved for any encoding localized in a geometric region.
- Theorem: finite‑depth locally reversible LC circuits between stable sets are fault tolerant, so LC equivalence implies FTQL equivalence at finite depth — hence FTQL phases are strictly coarser (color‑code example).
- Gauge‑state‑agnostic classification of subsystem codes; 2D ↔ 3D color code equivalence via dimensional jumps in the 3D gauge color code.
- Single‑shot preparation/QEC for *qudit* stabilizer codes with extended (≥1D) syndromes, under general channel noise, extending Bombín's result beyond qubits and Pauli noise.
- No‑go for a broad class of shallow point‑like‑syndrome measure‑and‑feedback circuits (depth up to O(log log n)), covering published preparation schemes for 2D topological codes and non‑Abelian orders with solvable anyon theories.

**How it works** Circuits are built from layers of range‑r local channel gates (required to be *locally reversible*, following recent mixed‑state phase work) and deterministic measurement‑feedback blocks; shallow means range×depth = O(polylog n). Noise classes must contain local‑stochastic noise, be monotone in strength, and compose additively; measurement errors flip reported outcomes with a λ‑bounded distribution. Fault tolerance means the noisy circuit equals the ideal circuit followed by residual noise of strength η(τ,ζ) continuous and vanishing at zero, which is recoverable. A worked example — toric‑code preparation with measurement error rate p — shows the output is in a *different* LC phase for any p>0, motivating the whole framework.

**Why it matters** It bridges the condensed‑matter phase‑classification program and fault‑tolerance theory: "same phase" now means "same information, robustly interconvertible," which is exactly what code switching and logical gate design need. The no‑go result is a concrete warning for experiments preparing topological order by measurement and feedforward.

**Caveats** Noise is assumed uncorrelated in time; with temporal correlations transitivity of fault tolerance can fail. Recovery channels are assumed noiseless and unrestricted in complexity, so stability is information‑theoretic, not necessarily efficiently achievable. The LC⇒FTQL implication is proved only for finite‑depth, not polylog‑shallow, circuits. The no‑go constrains a specific circuit form (measure Hamiltonian terms, apply conditional unitaries) and does not exclude all shallow fault‑tolerant preparations.
