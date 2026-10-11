# SciRate Daily Digest — 2026-10-11

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Scaling Quantum Optimization to the Thousand-Qubit Scale with Distributed Quantum Sampling

[arXiv:2610.10772](https://arxiv.org/abs/2610.10772) · [SciRate](https://scirate.com/arxiv/2610.10772)

*Amana Liaqat, Ahmed Darwish, Stephen DiAdamo, Dan Holme, Kieran McDowall, Emre Sahin, Naeimeh Mohseni, Giorgio Cortiana et al.*

**TL;DR** The authors build an end-to-end pipeline that uses depth-1 QAOA as a *candidate sampler* inside a classical Extended Fully-Corrective Frank–Wolfe solver for Minimum Birkhoff Decomposition, and run it on a 1,354-bus / 1,710-edge European transmission benchmark by spectrally partitioning the edge-encoded problem into 41 subgraphs of ≤50 qubits each. On IBM Heron hardware, repaired QAOA samples reach residual error 1.11×10⁻⁶, beating simulated annealing (which plateaus at round 18 with 15 matchings) and repaired uniform random sampling (>2×10⁻⁶), while spatially packing four circuits onto 144 of 156 qubits cuts wall-clock execution ~3×.

**The big picture** Many scheduling and energy-trading problems reduce to expressing a pattern of demands as a small number of conflict-free connection rounds, which is computationally hard to do sparsely. Quantum processors are far too small to encode an entire national grid at once, so the authors cut the network into pieces that fit on a chip, sample candidate solutions for each piece quantumly, glue them back together, and fix the inevitable conflicts at the seams with a cheap classical cleanup step. The result is a working recipe for applying today's noisy devices to a constrained optimization problem an order of magnitude larger than a single processor, and a useful diagnostic for how small the pieces can get before the quantum part stops contributing anything.

**Key contributions**
- Scaling quantum-assisted *constrained* (matching-feasible) decomposition past single-chip width, as opposed to prior divide-and-conquer work on unconstrained QUBOs.
- Spectral multi-way partitioning with an edge-count bound plus batched Cartesian stitching and O(|Ẽ| log |Ẽ|) greedy repair that only prunes — never adds — edges, isolating the sampler's contribution.
- Spatial circuit packing across disjoint Heron regions (two 38-qubit + two 34-qubit circuits), reducing dispatch rounds up to 4× and runtime ~3× at a cost of 4.7×10⁻⁷ in final error.
- A partition-size/bond-dimension study: p_s=20 stalls early; mirror fidelity and final cost both degrade with MPS truncation, arguing that nontrivial entanglement must remain inside each partition.
- Evidence that transpiled 2Q depth tracks line-graph interaction density, not qubit count (80 qubits → depth 67, but 52 qubits → depth 169).

**How it works** Each edge is a qubit; the QUBO rewards residual weight and penalizes adjacent-edge conflicts with a soft λ=0.2. Angles are calibrated offline on ≤16-qubit prototypes (PEGASE uses γ≈2.49, β≈0.16 from a χ=128 MPS scan of a 49-qubit partition) and frozen — no online variational loop. Top-5 distinct repaired candidates plus the exact global max-weight matching feed a cardinality-constrained QP over the active set; the residual graph is repartitioned each round, so cut edges can resurface later.

**Why it matters** This is a credible template for "utility-scale-shaped" quantum workloads: the quantum device supplies diversity to a classical solver that owns feasibility and convergence. The orchestration ideas (packing, repartitioning, repair) are reusable across constrained combinatorial problems, and the density-vs-depth analysis is a concrete design lesson for partitioning heuristics.

**Caveats** No quantum advantage is claimed or shown; the authors are explicit that budgets are not compute-matched (1.5×10⁶ SA sweeps vs 25,000 shots) and that MPS truncation sensitivity does not imply classical hardness. Baselines are weak — strong classical MBD solvers and full runtime accounting are deferred; the 4,096-variable QOBLIB results are preliminary. The "1,710 qubits" framing is nominal: actual circuits are ≤50 qubits. Greedy repair, applied identically to all samplers, does considerable work, and error mitigation reportedly hurt. Figures are absent from the provided source, so convergence curves could not be inspected.

## 2. Parameter-Dependent Noise Resilience in the Quantum Approximate Optimization Algorithm

[arXiv:2610.11710](https://arxiv.org/abs/2610.11710) · [SciRate](https://scirate.com/arxiv/2610.11710)

*Jorja Kirk, Ashley Montanaro*

**TL;DR** The authors prove that the total variation distance between noisy and noiseless QAOA output distributions is upper-bounded by a sum over the variational angles themselves — mixer angles *after* a Z error, cost angles (weighted by node degree) *before* an X error — so that small, smooth, adiabatic-looking schedules are intrinsically more noise-resilient. Simulations confirm the bound's qualitative ranking of parameter-generation strategies, and show that beyond Pauli error rate ≈0.01 unoptimized precomputed parameters match or beat noiselessly-optimized ones. Extending to the continuous limit, they show the adiabatic algorithm has an irreducible resilience floor scaling as system size times runtime squared, which a two-schedule generalization cannot beat once adiabaticity is enforced.

**The big picture** Variational quantum optimization is usually analyzed as if the circuit's tunable angles only affect solution quality, with noise treated as a separate, parameter-independent degradation. This work shows the two are coupled: because a single Pauli fault can be commuted to the circuit boundary where it becomes harmless, its only lasting effect is to flip the signs of a subset of the angles it passed through — so the damage is governed by how large those angles are and where in the circuit the fault occurred. The practical consequences are that gentle, slowly-varying schedules are self-protecting, that different error types should be prioritized for mitigation at different circuit depths and on differently-connected qubits, and that classical pre-optimization that ignores noise can be worse than useless. Pushing the same reasoning into the continuous-time adiabatic limit reveals a hard floor on how noise-resilient annealing schedules can be.

**Key contributions**
- Exact error-propagation picture: a single X/Z/Y fault in QAOA ≡ running the noiseless circuit with a subset of parameter signs flipped, plus a residual Pauli absorbed by the |+⟩ initial state or computational-basis measurement.
- Theorem bounding TVD by 2[χ_{K,X}Σ_{i>s}|sin β_i| + χ_{K,Z} max_ω Σ_{i≤s}|sin(ωγ_i)|] ≤ 2[Σ|β_i| + d_j Σ|γ_i|]; averaging over a Pauli channel gives a closed-form resilience metric E(γ,β) with layer-index weights i and (p−i+1).
- Structural predictions: Z errors most harmful early, X errors late, Y errors everywhere (numerically, D_Y ≈ D_X + D_Z); high-degree qubits are fragile only to X/Y.
- Two mitigation heuristics: an E-penalized objective and truncation of the search box to γ∈[0,π/2], β∈[−π/2,0] (halving the period for unweighted Max-Cut).
- Adiabatic analysis: single-schedule floor nT²·ε_xy ε_zy d_avg/(ε_zy+ε_xy d_avg); for two independent schedules with crossing value δ, Grover-like search gives T_cross ≳ √N/(2ηδ) hence E = Ω(nN(ε_zy+ε_xy d_avg)/(η²δ)) — shrinking δ *worsens* resilience.

**How it works** Errors are commuted through alternating cost/mixer exponentials; anticommutation flips the corresponding angle's sign, and TVD between the original and sign-flipped circuits is bounded by accumulating the per-layer unitary differences. Numerics use Max-Cut on 6–10-node line, 3-regular and Erdős–Rényi graphs, p up to 15, with Paulis injected per layer, LBFGS (exact) and SPSA (noisy) optimizers, and predicted parameters from prior work.

**Why it matters** It gives a cheap, closed-form, classically evaluable proxy for noise robustness that can be folded into parameter selection or compilation, plus actionable error-mitigation triage by error type, depth and qubit degree. The argument only needs an alternating pair of anticommuting generators, so it should port to other hardware-efficient ansätze.

**Caveats** The bound is loose (quantitatively; only qualitatively tracks the measured TVD), assumes Pauli-twirled noise and the standard X-mixer/|+⟩ ansatz, and says nothing about solution quality — small angles trivially minimize it. The two proposed resilience-engineering methods are explicitly "inconclusive," tested on only five 6-node graphs at one noise rate. Scaling behaviour, weighted/other Ising problems, and realistic hardware noise are untested. The adiabatic section relies on the first-order (non-rigorous) Roland–Cerf adiabatic condition, and the two-schedule negative result is derived only for unstructured search.

## 3. Geometry-optimized hyperbolic codes for modular fault-tolerant quantum architectures

[arXiv:2610.10948](https://arxiv.org/abs/2610.10948) · [SciRate](https://scirate.com/arxiv/2610.10948)

*Ahmed Adel Mahmoud, Steven Rayan*

**TL;DR** The authors exhaustively enumerate closed self-dual {p,p} hyperbolic surface codes with PSL(2,q) quotient groups (p ∈ {5,6,7,8}, prime q < 60), finding a [[51330, 17112, 10]] weight-6 code with efficiency kd²/n ≈ 33.3 — ~33× the toric code and ~6.6× the best hyperbolic Floquet benchmark — and show that merely changing which periodic identifications are used can double the distance (e.g. {7,7} at q=41 gives d = 4, 6, or 8) at identical n, k, and check weight. They add a topology-aware compiler that carves these codes into ≤80-qubit connected planar disk modules, and circuit-level Stim/PyMatching simulations showing the finite-size threshold drops only from ~0.22% to ~0.17–0.18% when long-range gate error is tripled.

**The big picture** Surface codes laid flat on a chip waste qubits: protecting more logical information forces the encoding rate down. Codes built on negatively curved surfaces escape this trade-off and can in principle keep getting more efficient as they grow, but they demand connections between distant qubits and have never been given a concrete hardware layout. This work searches systematically for the best such codes at small check weights, shows that the choice of how the curved surface is glued up — a purely combinatorial decision costing nothing in hardware — can quadruple the code's efficiency, and then supplies an algorithm that splits the resulting code into chip-sized flat tiles with controlled inter-chip communication, backed by noise simulations.

**Key contributions**
- Exhaustive enumeration within a well-defined algebraic class: 136 tiling–field cases → 38 inequivalent centralizer classes, with exact distances computed.
- Demonstration that periodic identifications (not the tiling) control distance: up to 2× distance, 4× efficiency, free.
- Finite-size sequences whose efficiency fits η ≈ 0.33(ln k)² (R² ≈ 0.996–0.998), consistent with saturating Delfosse's (log k)² ceiling.
- Topology-aware modular compiler enforcing capacity bounds plus a strict topological-disk condition per module; beats recursive spectral bisection on all five communication metrics where RSB is even feasible, and unlike Mt-KaHyPar (lower R but higher fragmentation K) satisfies all geometric constraints.
- Circuit-level thresholds for modular vs. monolithic layouts under an α-scaled remote-gate error model.

**How it works** Tilings come from the triangle group Δ_p = ⟨x,y | xᵖ=yᵖ=(xy)²=1⟩ quotiented by PSL(2,q); self-duality is imposed via y = JxJ⁻¹ for an involution J ∈ PGL(2,q), so n = |Q|/2 and k/n = (p−4)/p + 2/n. Distance is the shorter of primal/dual systoles. The compiler grows face regions on the dual graph under disk/size constraints, then reassigns data and vertex-ancilla qubits by greedy descent on a fragmentation-plus-load-penalty cost. Memory experiments run d rounds under an SI1000-like model with remote CNOTs at error αp, α ∈ {1,2,3}.

**Why it matters** It converts "hyperbolic codes are asymptotically good value" into specific codes, specific layouts, and specific threshold numbers — relevant to anyone designing modular superconducting qLDPC architectures.

**Caveats** Optimality is only within the self-dual prime-field PSL(2,q) family. Distances are small in absolute terms (8–12), and Stim's graphlike circuit-fault distances are strictly lower than homological ones (4,5,7,8 vs 6,8,10,12), so the quoted η overstates circuit-level protection. ~⅓ of all CNOTs are remote; the α model ignores latency, bus contention, and entanglement-generation overhead. Thresholds are finite-size estimates from four sizes with MWPM; no logical gates or lattice-surgery costing is given.

## 4. Improved Local Leakage Resilience of Shamir Secret Sharing and Worst-Case Optimal Polynomial Intersection

[arXiv:2610.12357](https://arxiv.org/abs/2610.12357) · [SciRate](https://scirate.com/arxiv/2610.12357)

*Yihang Sun, Mary Wootters*

**TL;DR** — The paper gives a single Fourier-analytic framework that reduces both local leakage resilience (LLR) of Shamir secret sharing and worst-case Optimal Polynomial Intersection (OPI) to list-decoding/list-recovery of the dual Reed–Solomon code, then plugs in the recent RS list-recovery-to-capacity breakthroughs. This yields the first LLR result below rate 1/2 (one-bit, worst-case leakage, improving on 0.668), and a polynomial-time quantum algorithm for worst-case OPI achieving satisfaction ratio SCL_ρ(R) − ε (the "double semicircle law"), beating all prior algorithmic *and* existential bounds.

**The big picture** — Shamir secret sharing is the canonical way to split a secret among many parties; a long line of work has asked how much redundancy is needed so that a single leaked bit from every share still reveals essentially nothing. Independently, a polynomial-constraint-satisfaction problem has become one of the leading candidates for demonstrating quantum advantage on a structured optimization task. This work shows the two questions are governed by the same underlying object — how many low-degree polynomials can simultaneously hit prescribed small sets of values — and imports recent dramatic progress in coding theory to improve the state of the art on both, including crossing a threshold that had been identified as a natural barrier for the leakage problem.

**Key contributions**
- First breaking of the "1/2 barrier": one-bit LLR for Shamir at rate 1/2 − δ for an absolute constant δ > 0; also b-bit LLR for any fixed b at any R > 1/2.
- A formal reduction showing OPI discrepancy is at least as hard as LLR (with a separation example showing the converse fails by up to an exponential factor).
- Quantum poly(n, log p) algorithm attaining SCL_ρ(R) − ε in expectation for worst-case lists, and exact perfect solutions when R + ρ > 1.
- Near-optimal OPI discrepancy (hence perfect solutions exist) for R > 1/2, for R > 1/2 − δ with ρ ≥ 1/2 − δ, and for R + ρ > 1.
- Existential bound V_ρ(R) = 1 − (1−2ρ)(1−2R) > SCL_ρ(R) for ρ < R ≤ 1/2.
- Unfolded, balanced-list OPI ensemble with unconditional quantum/classical separation relative to a membership oracle (quantum: perfect; classical poly-query: ≤ 1/2 + Ω(1/log log n)).

**How it works** — Both quantities of interest (OPI discrepancy, TV distance between leakage transcripts) are expanded as sums over the dual code of products of Fourier coefficients ĝᵢ of centered indicator functions. The central technical tool is a "weighted Fourier thresholding" lemma: thresholding each weight wᵢ at θ, list-recovery of the dual GRS code bounds the number of dual codewords lying in the heavy sets, while the rest are penalized by θ per coordinate — giving e^{o(n)}γ^k for dual weight t with 2k − t = Ω(n). This caps out at R = 1/2 (needs t = n). To go below, phases must be retained: the authors split at weight m = ⌊(2−δ)k⌋, handle light dual codewords with the lemma, and use a generalized von Neumann inequality plus U³ Gowers-norm bounds on the gᵢ to exploit cancellation among heavy ones. Algorithmically they use the DQI state |φ_ℓ⟩, with Jo's state-preparation via dual list-decoding (now to radius ≈ R, not the Johnson bound) and the thresholding lemma to control error from dual weights above k. The R + ρ > 1 case uses truncation of a degree-expansion H to j ≤ ℓ so only shells up to 2ℓ+1 matter.

**Why it matters** — Relevant to secret-sharing/leakage cryptography, coding theory, and the quantum-advantage debate: OPI is DQI's flagship application, and pushing worst-case guarantees from SCL_ρ(R/2) to SCL_ρ(R) markedly enlarges the regime where quantum beats the best known classical ratio ρ + R(1−ρ). The reduction also means any future list-recovery improvement automatically improves Shamir LLR.

**Caveats** — δ is an unspecified absolute constant, so "below 1/2" is quantitatively tiny; the LLR result still leaves R* ≫ 0 open. The existential improvement V_ρ(R) is explicitly non-algorithmic, and the SCL_ρ(R) algorithm gives an expectation/with-high-probability guarantee needing coherent membership oracles when p is superpolynomial. The classical-hardness separation requires quasipolynomial field size and rate 1/polylog(n), and bounds classical success only above 1/2 + Ω(1/log log n) — not a separation in the constant-rate regime where the algorithmic results live. Results assume prime fields with p ≥ n.

## 5. Quantum Magic and the Strong Coupling Constant

[arXiv:2610.11121](https://arxiv.org/abs/2610.11121) · [SciRate](https://scirate.com/arxiv/2610.11121)

*Qiaofeng Liu, Ian Low, Zhewei Yin*

**TL;DR** The authors compute the stabilizer Rényi entropy (second-order "magic") produced in tree-level, flavor-diagonal, color-singlet $q\bar q\to q\bar q$ scattering, averaged over the 60 two-qubit stabilizer input states and over solid angle, and scan the strong coupling while holding all other RG-running SM inputs fixed. In the $t\bar t$ singlet the magic has a finite-$\alpha_s$ minimum that tracks the $\overline{\rm MS}$ running $\alpha_s$ to within ~5% (typically a few %) from 1 TeV up to $10^8$–$10^9$ GeV, and this agreement collapses (excess grows from <3% to 26–48%) if physical Higgs exchange is removed. All six diagonal singlets sit near their magic minima and prefer $\alpha_s\gg\alpha$.

**The big picture** The strengths of the fundamental forces are inputs to the Standard Model, measured but not explained. This group previously found that the weak mixing angle sits very close to the value that minimizes a quantum-computational resource — the "non-classicality" beyond what a classical computer can efficiently simulate — generated in lepton scattering. Here they extend the same criterion to quark scattering and find that the strong force strength, including its energy dependence over many orders of magnitude, is likewise near a minimum, with Higgs exchange from the heavy top quark playing a decisive role. They speculate that nature's coupling constants are selected by a principle of quantum computational economy, as if the universe were a resource-constrained quantum simulation.

**Key contributions**
- First magic-based analysis where the gluon coupling enters the normalized outgoing spin state (via the $\alpha_s/\alpha$ ratio in the $t$-channel; $s$-channel gluon vanishes in the singlet).
- A finite-$\alpha_s$ magic minimum in the $t\bar t$ singlet that reproduces running $\alpha_s$ within a few percent over 1 TeV–$10^8$ GeV (global minimum above ~1.3 TeV).
- Demonstration that physical Higgs exchange (large $y_t$, with $s$- and $t$-channel contributions of opposite sign) is essential; $m_h\to\infty$ pushes the minimum to $\alpha_s=0$.
- Survey of all 21 flavor pairs × color channels: diagonal singlets within ~1% of minima; nonsinglet/nondiagonal channels show excesses up to ~41%; the $t\bar b$ singlet's 29–38% excess traced to charged-current, not Higgs, exchange.
- Explicit "quantum computational efficiency" conjecture plus a research program of falsifiable questions.

**How it works** Amplitudes are RG-improved tree-level: one-loop SM gauge and three-generation Yukawa running at $\mu=\sqrt s$, running masses defined via $m_f=y_f v/\sqrt2$ with fixed $v=246.9$ GeV to preserve tree-level mass–coupling relations for longitudinal $W/Z$ and Yukawa exchange; $m_h$ fixed at 125.2 GeV in propagators; zero widths. Spins are encoded as two qubits in the Lab basis ($\hat z$ along the incoming quark). Each of the 60 stabilizer states is acted on by the color-singlet-projected amplitude, renormalized, and its $M_2$ computed; averaging over states and solid angle gives $\bar M_2(\alpha_s/\alpha;\sqrt s)$, minimized over $\alpha_s\ge0$ including the pure-QCD limit $\alpha_s\to\infty$ (where the overall factor cancels).

**Why it matters** Relevant to the growing quantum-information-in-QFT community and to anyone interested in whether SM parameters have an information-theoretic origin. Even read conservatively, it establishes a nontrivial correlation between measured couplings and a Clifford-hierarchy resource measure across many decades of energy.

**Caveats** The result is a correlation without derivation; the magic measure, spin basis (Lab vs. helicity are not Clifford-related), uniform-solid-angle weighting, choice of stabilizer-state ensemble, and one-parameter-at-a-time scan are all conventions that affect the answer. Only $\alpha_s$ is varied, with $y_t$, CKM, and masses fixed, so the "determination" is not a global fit. Below 1 TeV the $t\bar t$ structure disappears entirely; several minima lie in regions where $\alpha_s>0.25$ and loop corrections are uncontrolled. Nondiagonal/nonsinglet channels, and $u\bar c$/$ud$ in particular, prefer couplings away from the SM, undermining universality; the link from perturbative quark singlets to physical hadronic states is unaddressed.
