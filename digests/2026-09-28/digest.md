# SciRate Daily Digest — 2026-09-28

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Oracle Distillation

[arXiv:2609.31596](https://arxiv.org/abs/2609.31596) · [SciRate](https://scirate.com/arxiv/2609.31596)

*Ruohan Shen, Soonwon Choi*

**TL;DR** The authors define *oracle distillation*: converting many uses of a noisy unknown oracle into one near-perfect oracle, without ever learning which oracle it is. For Boolean (phase) oracles they give an explicit protocol costing $T_{\rm OD}=O(N^{H(\alpha)+2\alpha}\ln(1/\epsilon))$ queries under adversarial weight-$\alpha n/2$ index noise, prove a matching $\tilde\Omega(N^{H(\alpha)})$ lower bound, and derive a threshold theorem: any Boolean oracle problem with polynomial advantage budget (Grover, $k$-forrelation, Simon) keeps a quantum advantage below a constant per-qubit depolarizing rate (e.g. $p^*=5.1\times10^{-4}$ for Grover).

**The big picture** Fault tolerance protects operations you know in advance, but in learning and sensing the crucial interaction is with an unknown system — precisely the thing you cannot compile into an error-corrected circuit. This work shows that if the unknown interaction belongs to a structured family, you can still purify it: query it many times in a deliberately weakened, noise-symmetric way, aggregate the faint responses, and undo the interaction so that residual errors become correctable without ever identifying the system. The consequence is a threshold theorem for query-based quantum speedups, most notably that Grover-type advantages — long thought fragile under noisy oracles — survive independent per-qubit noise below a constant rate, even though almost every individual query is faulty.

**Key contributions**
- Formal definition of oracle distillation and the three-way tension (label-agnosticism vs. error correction vs. functionality) that distinguishes it from FTQC, magic-state distillation, entanglement distillation, and QSP.
- The *weak query* primitive plus a two-stage protocol (repetition-code gadget converting adversarial noise to phase noise; then encode → weak query → aggregate → uncompute → recover).
- Near-optimality: a Knill–Laflamme-based lower bound $\tilde\Omega(N^{H(\alpha)})$ for distilling Grover oracles while keeping errors correctable; the upper bound exceeds it only by $N^{2\alpha}$.
- Threshold theorem under i.i.d. depolarizing noise, with explicit thresholds mapped in the (query-exponent, budget-exponent) plane.
- Extension to fractional and continuous-time oracles with two-sided/Lindbladian noise, total evolution time $\theta T_{\rm OD}=O(N^\gamma\ln(m/\epsilon))$.

**How it works** Inputs $|x\rangle$ are replaced by query states $|\Theta(x)\rangle=X^x|\Theta_s\rangle$ whose amplitude distribution is $2r$-wise independent, so weight-$\le r$ $Z$ errors act orthogonally (Knill–Laflamme) while retaining matched overlap $\eta=p(0^n)$. Permutation symmetry reduces seed-state design to Krawtchouk moment conditions on a Dicke-state weight distribution, with the bound $\eta\le 1/\sum_{j\le r}\binom{n}{j}$. $L$ query blocks are queried weakly; a threshold-on-response-count unitary writes $Z^{f(x)}$ onto a clean data block with error $e^{-\Theta(\eta L)}$; a second query uncomputes (using $O_f^2=I$), and since phase noise commutes with both $O_f$ and the diagonal aggregator, all noise piles up as a weight-$2w_P$ channel corrected by a label-independent recovery. Hence $T_{\rm OD}=2L\sim\eta^{-1}\ln(1/\epsilon)$.

**Why it matters** It is the first genuine fault-tolerance analogue for *unknown* dynamics, decoupling algorithm design from error correction in the query model, and it reconciles with prior Grover no-go results by pinpointing correlated-versus-local noise as the decisive distinction. Relevant to quantum algorithms theory, error correction, and computational sensing, where oracles synthesized from sensing dynamics need only be distillable, not perfect.

**Caveats** Gates, memory, and encoding are assumed noiseless; noise is restricted to the index register (response-register $Z$ noise makes distillation information-theoretically impossible) or i.i.d. depolarizing. The thresholds are protocol-specific and very small ($\sim5\times10^{-4}$ for Grover), the overhead is polynomial in $N$ (so advantage requires a large classical/quantum gap), and the results cover Boolean oracles only — general unitary families remain open.

## 2. Sipser-Spielman meets Dijkgraaf-Witten: non-Abelian qLDPC codes via twisted sheaf gauge theory and almost-constant-overhead magic state fountain

[arXiv:2609.31541](https://arxiv.org/abs/2609.31541) · [SciRate](https://scirate.com/arxiv/2609.31541)

*Guanyu Zhu, Shi Jie Samuel Tan, Ryohei Kobayashi, Po-Shen Hsin*

**TL;DR**
The paper shows that a Tanner/Sipser–Spielman code is literally the first homology of a sheaf on a graph, and that any classical code can be *subdivided* into such a sheaf code on an honest simplicial graph — which restores cup/cap products at the cochain level and lets one write down a type-III Dijkgraaf–Witten twist intrinsically on a qLDPC chain complex. The resulting twisted $\mathbb{Z}_2^3$ "sheaf gauge theory" gives Clifford-stabilizer qLDPC codes with non-Abelian $D_4$ order in 2D, and a gauging-measurement protocol on them prepares $\Theta(n^{1-\epsilon})$ CZ-type magic states in parallel — an almost-constant magic rate.

**The big picture**
Getting a universal set of fault-tolerant logic out of high-rate quantum codes has, until now, seemed to require adding a third dimension to the code's product structure, which costs connectivity. This work instead borrows the other classic route to universality — non-Abelian topological order — and shows it can be imported into expander-based codes without ever leaving the code's own combinatorial structure, by reinterpreting sparse-graph codes as sheaves. The payoff is a protocol that harvests a number of magic states nearly proportional to the number of physical qubits in a single shot, rather than distilling them one at a time.

**Key contributions**
- Subdivision theorem: any parity-check matrix with no zero rows/columns becomes a sheaf code on a graph (repetition codes at bit vertices, SPC at check vertices), preserving dimension exactly and with distance $w_c^{\min}d \le d_1(\mathcal F) \le w_c^{\max}d$; the dual code is the dual sheaf on the *same* graph.
- A twisted $\mathbb{Z}_2^3$ sheaf gauge theory: three BF terms plus $\pi\int_{\tilde\eta_3} a\cup b\cup c$, proven to be a cohomology invariant; gauging the resulting sheaf SPT (or the untwisted code's CZ symmetry) yields a Clifford stabilizer code with CZ-dressed $X$ checks, commuting on the zero-flux subspace.
- "0-form subcomplex symmetry": because a 2D chain complex has many top cycles, transversal CZ supported on $\eta_2\frown\rho^0$ gives $\dim H^0(\mathcal L,\mathcal F)$ *independently addressable* logical CZs — refuting the folklore that addressable CZ needs a 3D product code with transversal CCZ.
- Reduction of nontriviality of the twist to a local Schur-product condition $\mathcal C_v^{\mathrm r,\perp}*\mathcal C_v^{\mathrm b,\perp}\subseteq\mathcal C_v^{\mathrm g}$; full $\mathbb F_q$ generalization where the gauge group is $(\mathbb Z_p)^u$ and the field enters only via $T_{ijk}=\mathrm{Tr}(\theta_i\theta_j\theta_k)$.
- Magic fountain: $O(d)$ rounds of weight-$O(1)$ commuting dressed-$X$ measurements then ungauging; $\Theta(\sqrt n)$ states from good LDPC inputs, and $\ge n^{1-\epsilon}$ from Golowich–Tamo–Zhu multiplication-property codes, with disjointness guaranteed by a perfect-matching lemma.

**Why it matters**
It removes the third dimension from native non-Clifford resource generation on qLDPC codes and, unlike the predecessor code-to-manifold approach, keeps everything on the code's own complex so parameters scale like the underlying Abelian code. Relevant to anyone working on qLDPC logic, topological order in expander codes, or NLTS/NLTM-type complexity questions.

**Caveats**
Distance is a subsystem-code distance; the non-Abelian code is Clifford-stabilizer, so decoding and syndrome extraction are harder than Pauli-stabilizer analogues and no threshold or decoder analysis appears in the visible source. The almost-constant rate needs $q=p^{O_\epsilon(1)}$, so constants blow up as $\epsilon\to0$, and the constant-rate instantiation is stuck at $\varrho=\Theta(n^{-1/2})$ because one sheaf factor is constant. The "CZ magic states" are eigenstates of a non-Pauli Clifford; their downstream cost for universal computation is not quantified here.

## 3. Non-Abelian qLDPC: TQFT Formalism, Addressable Gauging Measurement and Application to Magic State Fountain on 2D Product Codes

[arXiv:2601.06736](https://arxiv.org/abs/2601.06736) · [SciRate](https://scirate.com/arxiv/2601.06736)

*Guanyu Zhu, Ryohei Kobayashi, Po-Shen Hsin*

**TL;DR** The authors generalize Kitaev-style non-Abelian topological codes and their combinatorial TQFTs from manifold triangulations to Poincaré CW complexes and certain general chain complexes, yielding the first non-Abelian qLDPC codes (as Clifford-stabilizer "twisted" hypergraph-product codes) with constant rate and $\Omega(\sqrt n)$ subsystem distance. Using a spacetime path integral of a higher-form Dijkgraaf–Witten-type twisted $\mathbb{Z}_2^3$ gauge theory, they construct an *addressable* gauging measurement of newly identified 0-form *subcomplex* symmetries, which are equivalent to addressable transversal CZ gates on ordinary 2D HGP codes. This yields a magic-state fountain producing $\Theta(\sqrt n)$ disjoint CZ magic states in parallel in $O(d)$ rounds — showing 3D product codes are *not* necessary for native non-Clifford logic.

**The big picture** A central tension in fault-tolerant quantum computing is that codes with the best storage efficiency tend to lack native universal logic, and the standard belief is that non-Clifford operations require higher-dimensional code constructions with even more demanding qubit connectivity. This work imports the machinery of topological field theory — path integrals, gauge symmetry, gauging of higher-form symmetries — into the setting of general expander-based codes, where there is no underlying geometric space to speak of. The payoff is a demonstration that two-dimensional product codes already contain enough hidden topological structure to host individually addressable non-Clifford resources, breaking a widely assumed connectivity-versus-universality tradeoff. It also opens a route to studying non-Abelian topological order in systems that are not lattices at all.

**Key contributions**
- Path integral of a twisted higher-form $\mathbb{Z}_2^3$ theory defined via cup product on a Poincaré CW complex, proven invariant under coboundary shifts (gauge invariance) and under subdivision (the analogue of retriangulation invariance).
- Non-Abelian qLDPC codes as Clifford-stabilizer codes ($X$-stabilizers dressed by CZ), with commutation relations, logical operators, and derivation by gauging a higher-form SPT.
- "Thickened" twisted/untwisted 2D HGP codes on a 16D Poincaré CW complex (tensor product of two 8D complexes from Freedman–Hastings-style code-to-manifold maps), with $k=\Theta(n)$, $d=\Omega(\sqrt n)$; plus a *pullback* to the bare skeleton 2D chain complex, drastically reducing constant overhead.
- Identification of **0-form subcomplex symmetries**: because a general 2D chain complex has many top-dimensional 2-cycles ("book pages" sharing a hinge), unlike a 2-manifold, one gets $O(1)$-addressable transversal CZ — an explicit counterexample to the folklore that addressable $C^{n-1}Z$ requires a global $C^nZ$.
- Addressable, ancilla-free gauging-measurement protocol and magic state fountain, with logical action derived from first principles via the spacetime path integral; non-Abelian order confirmed via fusion rules and Borromean-ring braiding tied to triple intersections of magnetic worldsheets.

**How it works** Gauging factorizes a global transversal Clifford symmetry into weight-$O(1)$ Gauss-law operators (CZ-dressed $X$ stabilizers) that can be measured fault-tolerantly. Products of measurement outcomes over a chosen homology class reconstruct the eigenvalue of the subcomplex symmetry supported on that class, giving independent projective measurements of many disjoint transversal CZs simultaneously. One starts in logical $|+\rangle/|0\rangle$ on an untwisted HGP code, gauges (flowing to the twisted Clifford-stabilizer code), then ungauges; the net effect is projection onto hypergraph magic states, converted to non-Clifford gates by teleportation. The spacetime picture is a defect-decorated imaginary-time path integral with spacetime domain walls rather than anyon braiding.

**Why it matters** Relevant to anyone designing qLDPC architectures: it suggests non-Clifford logic and parallel magic-state preparation may be achievable on the 2D product codes already targeted for near-term hardware, and it supplies a general symmetry-based criterion (subcomplex symmetries) for addressability. Conceptually, it extends TQFT invariants beyond manifolds.

**Caveats** The distance bound for the twisted codes assumes an unproven TQFT statement about condensation descendants. Distances are *subsystem* distances, with spurious short (co)cycles absorbed into gauge qubits. Magic yield is $\Theta(\sqrt n)$ per $n$ qubits, not constant-rate. Constant factors from the thickening/CW construction are large (mitigated, not eliminated, by the skeleton pullback), and no circuit-level noise simulations, decoders, or thresholds are presented; connectivity demands of HGP codes remain.

## 4. Optimal noisy sequential multiparameter quantum sensing

[arXiv:2609.30398](https://arxiv.org/abs/2609.30398) · [SciRate](https://scirate.com/arxiv/2609.30398)

*Andrew Tanggara, Lorcán O Conlon, Alexey V. Gorshkov, Kishor Bharti*

**TL;DR** The authors lift the Nagaoka–Hayashi Cramér–Rao bound to the sequential (adaptive) setting using the quantum comb/tester formalism, yielding a single semidefinite program whose value lower-bounds the MSE of *any* physically realizable strategy — jointly over probe state, intermediate controls, final POVM, and estimator — for arbitrary multi-time, temporally correlated parameterized processes. For regular finite-dimensional single-parameter problems admitting an optimal tester, the SDP is provably tight (its value equals the reciprocal of the comb/sequential QFI), and an explicit locally optimal protocol can be reconstructed from the optimizer.

**The big picture** Finding the best possible quantum sensing protocol requires simultaneously optimizing what state you send in, how you steer the system between interactions with the thing you are measuring, how you measure at the end, and how you convert data into estimates — a notoriously intractable joint optimization, especially when noise is correlated in time and several parameters are estimated at once. This work recasts the whole adaptive protocol as a single mathematical object and turns the search for the ultimate precision limit into a convex optimization problem that standard solvers can handle, with the optimizer itself yielding a concrete recipe for the protocol in the single-parameter case. That matters because it gives both benchmarks that no experiment can beat and, when the bound is achievable, ready-made designs for noise-resilient sensors.

**Key contributions**
- A sequential Nagaoka–Hayashi lower bound: an SDP over a block matrix whose top-left block is a valid quantum tester, with local-unbiasedness enforced as linear trace constraints; applies to correlated-noise channels and general multi-time processes with an inaccessible environment.
- Runtime polynomial in probe dimension and number of parameters, but exponential in the number of steps (tester matrices of size D^{2T}).
- Tightness proof for single-parameter regular problems, with identification SDP value = 1/J_seq, J_seq = max over testers of the output-state SLD QFI of ρ_θ^M = M^{1/2}Λ_θ^⊤M^{1/2}.
- A constructive extraction procedure: SLD spectral projectors give tester outcome operators and rescaled eigenvalues give the estimator; the tester is decomposed into a pure input state, intermediate isometries, and a final POVM.
- Identification of the obstruction in the multiparameter case: saturation requires commuting effective estimator observables Y_i = √(M⁺)X_i√(M⁺) on supp(M).
- Review/adaptation of the Hamiltonian-not-in-Kraus-span condition, plus a sufficient criterion (Prop. on finite latent noise labels) for lifting Heisenberg-limited known-noise strategies to correlated processes with an unknown discrete noise label, via calibration.
- Numerics: error-corrected sensing under unknown correlated noise, qudit estimation, and comparison of one- vs two-copy-per-step control in noisy multiparameter sensing.

**Why it matters** It unifies the three traditionally separate optimization stages (state, control, measurement) into one convex program, subsumes prior fixed-state results and Hayashi–Ouyang's state+measurement optimization, and gives computable ultimate limits in exactly the regime — correlated, non-Markovian noise with multiple parameters — where QFI-based tools are weakest and probe/measurement incompatibility bites.

**Caveats** The exponential-in-T cost restricts numerics to few time steps, so asymptotic Heisenberg-scaling claims rest on separate analytic arguments rather than the SDP. The bound is only guaranteed tight for single parameters (and requires regularity plus existence of an optimal tester); for multiparameter problems it may be strictly loose and the optimizer blocks need not correspond to a physical strategy. Everything is local unbiasedness at a known θ₀, i.e., local rather than global estimation, and the HNKS-to-HNLS correspondence is only a leading-order limiting statement, not valid for fixed finite dt or arbitrary correlated processes.

## 5. Nonstabilizerness of quantum tensor network states is intractable in two dimensions

[arXiv:2609.31459](https://arxiv.org/abs/2609.31459) · [SciRate](https://scirate.com/arxiv/2609.31459)

*Gianluca Esposito, Georgios Styliaris*

**TL;DR** — For two-dimensional PEPS given by their local tensors, computing the stabilizer α-Rényi entropy is #P-hard already at bond dimension 4 (and is #P-complete under weakly parsimonious reductions), while merely deciding whether the encoded state is a stabilizer state is C₌P-complete at bond dimension 33. Both hardness results survive constant additive slack: approximate stabilizer membership with any constant promise gap below 1/5 stays C₌P-hard, and estimating M₂ to additive error 1/100 is C₌P-hard. This sharply separates 2D from 1D, where stabilizer entropies of MPS are computable in polynomial time.

**The big picture** — Magic, or nonstabilizerness, has become a standard many-body diagnostic alongside entanglement, and in one dimension it can be extracted efficiently from the compressed tensor description of a state. The natural hope was that the same would hold for two-dimensional tensor networks, which are the workhorse ansatz for area-law states and topological phases. This work shows that hope is unfounded in the worst case: even for tiny, fixed bond dimension and even with generous error tolerance, extracting the magic — or just certifying that a state has none — is as hard as exact counting problems that neither classical nor quantum computers are believed to solve efficiently. Any practical algorithm must therefore exploit additional physical structure rather than the tensor-network form alone.

**Key contributions**
- #P-hardness of exact/high-precision stabilizer entropy evaluation for square-lattice qubit PEPS at D = 4, for every integer α ≥ 2, plus matching upper bound (one #P oracle call + poly post-processing).
- C₌P-completeness of exact stabilizer membership for PEPS at D = 33 — a class not commonly invoked in quantum information, with the collapse consequences worked out (C₌P ⊆ P ⇒ P = NP = PH = PP; C₌P ⊆ BQP ⇒ NP ⊆ BQP).
- Robustness: C₌P-hardness of the promise problem for all 0 ≤ a < b ≤ 1/5 in Euclidean distance to STAB, with ApproxSTABPEPS₀,₁/₁₆ complete; hence constant-accuracy SE estimation is hard.

**How it works** — Counting satisfying assignments of a Boolean circuit is written as a scalar tensor-network contraction (delta tensors for wires, truth-table tensors for gates). The contraction value t is then embedded, via direct sums of the original tensors, into a single "marked" qubit of a bond-dimension-4 PEPS whose state is (t|0⟩+|1⟩)/√(1+t²) ⊗ |0…0⟩. The stabilizer purity of such a state is an injective function of t, so binary search recovers the count in polynomial time. For membership, the direct-sum trick C[A_{f₁} ⊕ (−A_{f₂})] = C(A_{f₁}) − C(A_{f₂}) encodes a GapP difference; the state is a stabilizer iff the two #P counts cancel exactly — precisely a C₌P zero test. The containment direction uses the replica identity SP₂ = 2^N Tr[Q_N ψ^{⊗4}] with Q_N = Q₁^{⊗N}, which is itself a PEPS contraction of polynomially larger bond dimension.

**Why it matters** — This delimits what magic-estimation algorithms for 2D tensor networks can promise, and it says the obstruction is not precision but structure: bounded physical and bond dimension alone buy nothing. Relevant to anyone developing magic diagnostics for topological order, PEPS numerics, or classical-simulability criteria.

**Caveats** — Worst-case only; average-case and physically motivated subclasses (injective PEPS, translation invariance, uniformly gapped parent Hamiltonians, isometric TNs) are explicitly left open. Constant-accuracy hardness is only C₌P, not #P — whether the stronger hardness persists at fixed tolerance is unresolved. The membership construction uses D = 33, far above the D = 2 known for contraction hardness, and results cover integer α ≥ 2 with exact rational tensor inputs.
