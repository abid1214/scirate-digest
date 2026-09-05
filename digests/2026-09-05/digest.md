# SciRate Daily Digest — 2026-09-05

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Experimental validation of a compact fault-tolerant architecture for trapped ions

[arXiv:2609.03194](https://arxiv.org/abs/2609.03194) · [SciRate](https://scirate.com/arxiv/2609.03194)

*Noah Berthusen, Ali Lavasani, Asmae Benhemou, M. S. Allman, Joan Dreiling, Brian Estey, Cameron Foltz, Trent Jacobs et al.*

**TL;DR** The authors introduce the $[[20,2,6]]$ "$C_4$-Helix" code — a concatenated symplectic double code built from $[[5,1,3]]\!\to\![[10,2,3]]\!\to\!C_4$ — whose logical Clifford group on two logical qubits is generated almost entirely by qubit permutations/single-qubit gates plus one depth-4 fold-transversal $\overline{S}_0\overline{S}_1$. On Quantinuum's 98-qubit Helios they demonstrate repeated QEC at $4.6^{+6.2}_{-2.6}\times10^{-5}$ per logical qubit per cycle, two-qubit logical randomized benchmarking at $2.8^{+1.0}_{-1.6}\times10^{-4}$ per Clifford (vs. $1.2\times10^{-3}$ physical), and a chain-map CNOT to a $[[25,1,5]]$ surface code producing a heterogeneous 3-logical-qubit GHZ state with fidelity $\geq 99.925\%$ — all without postselection.

**The big picture** Most error-correction demonstrations so far have shown that encoded memory can beat raw hardware, but a useful machine also needs cheap logical gates and a way to import the non-Clifford resources that make computation universal. This work packages all three ingredients into one compact code family designed for trapped-ion machines with all-to-all connectivity, and shows each ingredient beating its unencoded counterpart on real hardware. The point is a shift in design philosophy: build codes around the requirements of computation from the start, rather than optimizing memory and bolting operations on afterwards.

**Key contributions**
- A concrete architecture around a rate-1/10, distance-6 code with ~3.5× less space overhead than a comparable rotated surface code, yet with near-free Clifford logic.
- Replacing the previously proposed (prohibitive) gate-injection route to $\overline{S}_0\overline{S}_1$ with an optimization-found circuit made fault-tolerant (circuit distance 6, verified in Stim) via flag gadgets on the intra-block CZs.
- A lookup-table compiler: Dijkstra on the Cayley graph of $\mathrm{Sp}_4(\mathbb{F}_2)$ (720 elements) with zero-cost automorphism edges; every two-qubit Clifford needs ≤3 phase gates (distribution 36/324/324/36).
- First logical RB of the *complete* two-qubit Clifford group inside a single $k=2$ codeblock, with runtime Guppy sequence generation and per-sequence detector/sign tracking.
- Experimental validation of a chain-map CNOT between distinct CSS code families (depth 2, distance 6), the proposed magic-state injection interface.
- Extensions: $[[60,2,12]]$ Carbon-Helix, $[[100,2,18]]$ Double-Helix; and a $\ket{CZ}\to\ket{\mathrm{TOF}}$ zero-level distillation route native to $C_4$-Helix.

**How it works** Syndrome extraction is layered: flagged two-ancilla circuits measure the weight-4 $C_4$ checks while also swapping out data qubits (all four rotate out every two rounds, mitigating leakage alongside hardware repump and LRUs); Shor-style flagged circuits handle the ten weight-8 checks, total depth 10 with 32 ancillas. Adaptive syndrome extraction skips upper-level checks when $C_4$ flags are silent — with an extra rule to catch $XX\!\to\!ZZ$ errors that the phase gate propagates undetectably — cutting two-qubit gates 33% and wall-clock 23%. Decoding is offline over the full circuit volume with the Frontier decoder, whose inter-class confidence gap enables forced-gap postselection (0.4% discard → $9.3\times10^{-6}$).

**Why it matters** This is among the first demonstrations that a high-rate, $k>1$ code can support full Clifford control at error rates below hardware baselines without postselection, and that logical qubits in structurally different codes can be entangled fault-tolerantly. Relevant to anyone planning early-FT architectures or magic-state factories.

**Caveats** Memory was sampled only in the $X$ basis, so the logical Pauli channel is not characterized (argued conservative given dephasing dominance). Statistics are thin: the distance-6 memory and 4,000-shot GHZ results have very wide asymmetric intervals (the $\varepsilon_6$ upper edge overlaps $\varepsilon_3$'s lower edge; postselected value spans an order of magnitude). No non-Clifford gate or $T$-state injection was actually run; the GHZ bound covers the whole sequence, not the chain map alone. Decoding was offline, not real-time. The $10^{-6}$–$10^{-8}$ claim is simulation-based extrapolation to $\sim10^{-4}$ physical infidelity, and the spacetime-volume comparison against surface/color codes excludes syndrome-extraction overhead.

## 2. Non-local Magic: closed-form solution and equivalence with magic of purification

[arXiv:2609.04119](https://arxiv.org/abs/2609.04119) · [SciRate](https://scirate.com/arxiv/2609.04119)

*Michele Viscardi, Lorenzo Leone, Alioscia Hamma*

**TL;DR** For the log-stabilizer fidelity, the notoriously hard double optimization over local unitaries defining non-local magic collapses to a one-line formula depending only on the Schmidt spectrum: $D^{\rm NL}_{\rm stab}=-\log\max_k 2^{-k}(\sum_{i\le 2^k}\theta^\downarrow_i)^2$. The authors then define the *magic of purification* (minimum pure-state magic over all purifications), show it induces a resource theory whose free states are exactly normalized stabilizer-code projectors (STAB0), and prove that non-local magic of a bipartite pure state equals the minimum purification magic over the unitary orbit of its reduced state.

**The big picture** Magic, the resource beyond stabilizer operations needed for universal quantum computation, is basis-dependent: a product state can carry lots of it while sharing no correlations. Stripping away what local basis changes can remove leaves "non-local magic," a natural but seemingly intractable quantity requiring optimization over two exponentially large unitary groups. This work shows that for one standard magic measure the optimization has an exact closed-form answer determined solely by the entanglement spectrum, and reinterprets non-local magic as a genuine mixed-state magic measure of the reduced density operator. That links three previously separate viewpoints — entanglement spectra, mixed-state resource theories, and the sharpness of quantum filters.

**Key contributions**
- Exact analytic solution for non-local log-stabilizer fidelity; evaluation costs $O(2^n)$ given the Schmidt spectrum, far cheaper than the stabilizer fidelity itself, and is experimentally accessible via entanglement-spectrum tomography.
- Definition of the magic of purification and proof it is faithful on and monotone under free operations preserving STAB0 (the states with vanishing stabilizer Rényi entropy).
- $\mathcal{M}_f \le \mathcal{M}_p$: the convex-roof "magic of formation" lower-bounds the purification magic whenever the pure-state monotone is strongly monotonic.
- Uhlmann-theorem reduction: $D^{\rm pur}_{\rm stab}(\rho)=-\log\max_{\sigma\in\mathrm{STAB0}}F(\rho,\sigma)$, a standard distance-to-free-set form, with $|E|=n$ ancillas sufficient and $D^{\rm pur}_{\rm stab}\le n$.
- $D^{\rm NL}_{\rm stab}(|\rho\rangle_{AB})=\min_{U_A}D^{\rm pur}_{\rm stab}(U_A\rho_AU_A^\dagger)$, plus a characterization of minimizers (top-$2^k$ eigenspace must be a stabilizer code).
- Choi–Jamiołkowski application: stabilizer Choi states correspond to Cliffords or sharp stabilizer projections; any *unsharp* (graded) filter necessarily costs non-local magic.

**How it works** The lower bound uses Bell-pair-plus-$|0\rangle$ stabilizer ansätze in the Schmidt basis; the upper bound combines a von-Neumann-trace-type overlap inequality ($|\langle\psi|\phi\rangle|\le\sum_i\lambda_i^\downarrow\theta_i^\downarrow$, proved via doubly-substochastic majorization) with the quantized fact that stabilizer states have flat Schmidt spectra of dyadic rank. The orbit theorem absorbs the Clifford in $\sigma=C(\Pi_0^k/2^k)C^\dagger$ into $U_A$ and applies a Cauchy-interlacing/Ky-Fan compression bound $\|A\Pi\|_1\le\sum_{i\le s}\lambda_i^\downarrow$.

**Why it matters** Provides a computable, spectrum-only proxy for irreducible non-stabilizerness usable in many-body, holographic, and experimental settings, and clarifies which mixed-state extension of magic (purification vs. convex roof) is the right dual to non-local magic.

**Caveats** Everything closed-form is specific to the stabilizer fidelity; extension to stabilizer Rényi entropies is left open. $O(2^n)$ still presupposes the full Schmidt spectrum. STAB0-based free operations are not closed under classically conditioned operations, and SRE itself fails partial-trace monotonicity. The equality condition stated in Lemma 1 (identical ordered Schmidt bases) appears to ignore spectral degeneracies. A concurrent independent work reportedly obtains the same closed form.

## 3. Parameterised graph theory for tensor networks: entanglement rerouting, structural simplification, and agnostic tomography

[arXiv:2609.04165](https://arxiv.org/abs/2609.04165) · [SciRate](https://scirate.com/arxiv/2609.04165)

*Matthias C. Caro, Natalie McHugh, Sergii Strelchuk*

**TL;DR** The paper imports parameterised graph theory into tensor-network *representation* and *tomography*: a simple local "entanglement rerouting" move lets any tensor-network state on a known graph be rewritten as an MPS with bond dimension χ^cw(G), or as a TTN on grouped sites with local dimension d^{2tcw(G)} and bond dimension χ^{2tcw(G)}. Combining this with an extension of the Cramer et al. disentangling learner to trees and to arbitrary known graphs yields tomography with sample complexity O(n³/ε⁴ · (d^{lc} + log(n/δ))), where the exponent is a new parameter (learning complexity) bounded via degree, treewidth, and Markov–Shi contraction complexity; an agnostic version achieves fidelity within ε of the best state in the class.

**The big picture** Tensor networks compress quantum states by wiring small tensors along a graph, and it has long been known that the graph's structure controls how hard the network is to contract classically. Much less was known about which structural features control whether such a state can be rewritten in one of the few forms we know how to handle, and how many copies of the state are needed to reconstruct it experimentally. This work identifies specific, computable structural widths that govern both rewriting cost and learning cost, extends the standard chain-based tomography algorithm to trees and then to arbitrary known network topologies, and handles the realistic case where the true state only approximately fits the assumed structure. It also gives a rigorous justification for heuristics already used to choose orderings in numerical simulations of molecules.

**Key contributions**
- **Entanglement rerouting**: deleting an edge {x,y} and multiplying the weights of {x,z},{y,z} by w(e), with a Kronecker-delta-padded tensor at z, preserves the state exactly.
- Representation theorems: TNS → MPS with bond dim χ^{cw(G)}; TNS → TTN with grouped physical dim d^{2tcw(G)}, bond dim χ^{2tcw(G)} (first use of tree-cutwidth here).
- First efficient TTN tomography with explicit guarantees: O(n³/ε⁴((dχ)^{max{2,Δ}} + log(n/δ))) copies; efficient for tree degree O(log n).
- New parameter **learning complexity** lc_{d,χ}(G), with lc ≤ min{n, 3⌈CC(G)log_d χ⌉} = O(Δ·tw·log_d χ), and a proven separation lc(K_n)=n vs CC(K_n)=Θ(n²).
- Agnostic TNS tomography on general graphs, given a fidelity floor θ, with cost polynomial in 1/θ, 1/min{ε,θ} and exponential only in the largest active register.

**How it works** The MPS construction fixes a vertex ordering and routes every long-range edge through the intervening path, so each path bond accumulates the product of weights crossing that prefix cut — hence cutwidth in the exponent; the TTN version routes along the decomposition tree, with adhesions bounding bonds and torso sizes bounding grouped local dimensions. Optimal orderings/decompositions come from FPT algorithms (2^{O(cw²)}n; 2^{O(tcw²log tcw)}n²). The learner generalises iterative disentangling: instead of one qudit at a time along a path, it follows a "learning sequence" (rooted schedule assembling V), acting on fresh vertices plus children's residual registers, using only the rank-≤χ^{|cut(S_i)|} bound across the cut, then compressing to ≈|cut(S_i)|log_d χ qudits. Agnostic guarantees use a sharpened subspace-error-propagation lemma.

**Why it matters** It reframes "which states are learnable/compressible" as a question about graph widths rather than ad hoc topologies, connects the learning exponent to the same contraction complexity that governs classical simulability (bearing on the learnability-vs-simulability question), and explains DMRG orbital-ordering heuristics as approximate cutwidth minimisation. Relevant to quantum learning theorists and TN numerics practitioners.

**Caveats** All results are upper bounds; no lower bounds on copy complexity, and the exponents (χ^{cw}, d^{lc}) are only efficient for graphs of constant/logarithmic width — grids, cliques, and stars are excluded. The graph must be known (no structure learning), representations are exact with no truncation, the agnostic learner needs a known fidelity floor θ and outputs an improper (circuit-represented) state, and the contraction-complexity bound on lc is provably loose for cliques. Tightness of that bound and extension to property testing remain open.

## 4. Quantum Hamiltonian Evolution for Coherent Quantum Learning

[arXiv:2609.03640](https://arxiv.org/abs/2609.03640) · [SciRate](https://scirate.com/arxiv/2609.03640)

*Ignacio B. Acedo, Javier Gonzalez-Conde, Pablo Rodriguez-Grasa, Barry C. Sanders, Lirandë Pira*

**TL;DR** The paper proposes Coherent Quantum Learning (CQL): instead of a classical outer optimizer, the trainable parameters of a variational quantum model are placed in a quantum register in superposition and evolved under a Quantum-Hamiltonian-Descent-style Hamiltonian whose potential is the data-dependent loss, so amplitude concentrates on low-loss parameter values through interference. The main technical content is an explicit block-encoding recipe for the loss Hamiltonian from a coherent model-evaluation unitary — a $(1, m+5, 0)$ block encoding with $\mathcal{O}(m)$ depth and $\mathcal{O}(1)$ controlled queries — plus small numerical demonstrations (a 2-parameter data-reuploading classifier and Mach–Zehnder phase estimation, 5 qubits per parameter).

**The big picture** Almost all quantum machine learning today trains quantum models with an entirely classical optimization loop: try one parameter setting, measure, estimate a gradient, update. That means the distinctive quantum features — superposition and interference — play no role in learning itself, only in evaluating the model. This work reformulates training as a physical process: all candidate parameter settings are explored simultaneously as a wave in parameter space, and the dynamics push probability toward the settings that fit the data best, with no gradients and no classical feedback. The same machinery also handles physical inference tasks such as estimating an unknown phase, suggesting learning from data and learning physical parameters are the same kind of process.

**Key contributions**
- A learning-specific (data-dependent, batched) instantiation of quantum Hamiltonian descent, where the potential is generated by evaluating a parameterized circuit on data.
- A coherent model-evaluation unitary that entangles model output amplitudes with all discretized parameter values at once.
- Explicit conversion of that unitary into a block encoding of the diagonal loss Hamiltonian, via amplitude-to-diagonal conversion for $\sqrt{H}$ and $\sqrt{H}^\dagger$ followed by block-encoding multiplication; extensions to multi-sample batches (product-type loss) and to general smooth losses via QSVT on the probability operator.
- Batched training as sequential Hamiltonian evolutions, with the evolution time and damping schedules playing the role of a learning rate; notably, the usual QHD asymptotic concentration condition must be relaxed to avoid overwriting earlier batches.
- Time-dependence removed by a Page-style clock register, giving a time-independent Hamiltonian simulable by qubitization.

**How it works** Parameters are discretized onto $2^m$ grid points; the state evolves under kinetic plus loss terms with exponential damping schedules, promoted to a clock-register position operator. Numerically, after one epoch of 100 size-1 batches the parameter distribution anti-correlates with the full-dataset loss landscape (bimodal at the two minima); the interferometer example localizes on the true phase.

**Why it matters** It offers a concrete fault-tolerant-era alternative to hybrid variational training, potentially sidestepping measurement-noise-driven gradient estimation and backpropagation obstructions, and connects QML to the growing quantum-optimization-as-dynamics literature.

**Caveats** No complexity analysis and no claimed advantage over hybrid optimization — explicitly left open. The momentum-operator block encoding has normalization scaling as $\mathcal{O}(N)=\mathcal{O}(2^n)$, i.e. exponential simulation cost unless one restricts to a low-bandwidth subspace; the authors flag optimal discretization as out of scope. Batched losses are products of per-sample success probabilities, not the empirical mean. Numerics are classically simulated toy problems (2 parameters, 5 qubits each); the "matching gradient-based performance" claim is not quantified. Barren plateaus are motivation but not shown to be avoided, and readout of the final distribution still requires sampling.

## 5. Quantum communication and Bell nonlocality require infinite classical communication to simulate

[arXiv:2609.04182](https://arxiv.org/abs/2609.04182) · [SciRate](https://scirate.com/arxiv/2609.04182)

*Carlos de Gois, Thyago S. R. Santos, Carlos Vieira*

**TL;DR**
The authors settle the long-standing question of how much one-way classical communication (plus unlimited shared randomness) is needed to exactly reproduce the statistics of prepare-and-measure quantum communication and of bipartite quantum correlations, for every dimension. For dimension ≥ 4 no finite alphabet suffices — even for pure states and binary rank-one projective measurements, and even for binary measurements on the maximally entangled ququart — while qutrit communication (and hence Bell correlations with a qutrit on one side) is exactly simulable with fewer than 2^357 messages (9328 messages for binary projective measurements).

**The big picture**
A quantum system of fixed size can be prepared in a continuum of states but can carry only a bounded amount of readable classical information, which has long suggested that everything one can observe from preparing and measuring such a system could be faked by sending a bounded classical message plus shared randomness. This was known only for the smallest quantum systems, where two classical bits suffice. The paper shows that this classical-simulation picture breaks down abruptly once systems reach four dimensions: no finite classical message, however large, reproduces all the observable statistics, whereas three-dimensional systems remain finitely simulable. So at the level of observed statistics, small quantum systems are just efficient classical ones, but slightly larger ones are qualitatively different — and this holds already for the correlations of two entangled particles under simple two-outcome measurements.

**Key contributions**
- Impossibility of exact finite classical simulation of d-dimensional quantum communication for all d ≥ 4 (previously only exponential lower bounds were known).
- First finite upper bound beyond qubits: an explicit qutrit protocol for arbitrary POVMs and mixed states with d_C < 2^357 (9328 for binary projective measurements).
- Transfer to Bell nonlocality: 357 bits suffice when one side is a qutrit; the maximally entangled ququart's *full* binary-measurement statistics need infinite communication — a sharp separation from Regev–Toner's two-bit simulation of binary *correlators*.
- A harmonic-analysis "zero-slope" technique on complex projective space, with an explanation of why the threshold lands exactly at d = 4.

**How it works**
Impossibility: restrict to rays x, y ∈ CP³ with fidelity f = |⟨x|y⟩|², and average the outcome probability over the unitary-orbit of fixed-fidelity pairs. Quantum gives a_Q(t) = t, slope 1 at t = 0. Each (λ, c) branch factorizes as ⟨A_{λ,c} | R_t B_{λ,c}⟩ where R_t averages the decoder over the fidelity-t ring. By symmetry R_t is diagonal in the Laplace–Beltrami eigenspaces of CP³ with multipliers φ_ℓ(0) = 2(−1)^ℓ/((ℓ+1)(ℓ+2)) and φ′_ℓ(0) = −ℓ(ℓ+3)φ_ℓ(0). The ℓ^(−2) decay exactly cancels the Laplacian's ℓ² growth, giving (R_t − R_0)/t → (¼)Δ R_0 in L². Perfect exclusion at t = 0 forces A_{λ,c}·R_0B_{λ,c} = 0 a.e., and enough regularity that ΔR_0B also vanishes there, so every branch has zero slope; summing over finitely many c contradicts slope 1. Below d = 4 the decay is too slow for this regularity — hence the exact threshold.

Qutrit protocol: rejection sampling on shared (h, α, β) with α ≥ β, α + β ≥ 1, tuned so that joint acceptance is |⟨x|y⟩|²/18 and Alice's acceptance is 1/18; Alice sends the index of her first accepted sample (finite a.s., ~18 bits average). Finiteness is obtained by truncating at N = 112 samples and adding a fallback branch indexed by a covering of CP² by 9216 balls of radius 1/√24 (overlap > 5/6), with reserved randomness slices and a correction variable Γ to keep the branch weights exact; POVMs/mixed states follow by binarization and 26 combined copies.

**Why it matters**
This closes the qubit-only gap left since Toner–Bacon, gives the first qualitative dimension-dependent separation in classical simulation cost, and suggests unbounded classical cost at *fixed* small quantum dimension — relevant to unconditional "quantum information supremacy" constructions, which currently need growing quantum systems.

**Caveats**
Everything is about *exact* simulation over a continuum of inputs; approximate simulation, finite measurement sets, or noise robustness are untouched, and no explicit task with growing quantifiable separation is yet given. The qutrit bound is wildly unoptimized (lower bound is 5 vs. 9328/2^357). The model is one-way, single-round.
