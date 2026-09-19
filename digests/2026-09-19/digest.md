# SciRate Daily Digest — 2026-09-19

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Hardness of Pathfinding in a Welded Tree

[arXiv:2609.20651](https://arxiv.org/abs/2609.20651) · [SciRate](https://scirate.com/arxiv/2609.20651)

*David Miloschewsky, Supartha Podder*

**TL;DR** The paper proves that no quantum query algorithm can output an entrance-to-exit path in a welded tree of height $n$ using fewer than $\Omega(2^{n/24})$ queries — success probability is $O(q^6/N^{1/4})$ for $q \le \sqrt N/100$, $N=2^n$. This resolves the open question of Aaronson and of Childs–Coudron–Gilani for *general* quantum algorithms, removing their "genuine and rooted" restrictions, and it does so by building a compressed (recording) oracle for welded trees out of compressed permutation oracles.

**The big picture** The welded trees problem is the canonical example of an exponential quantum speedup from a quantum walk: a quantum computer can find the far exit of a maze-like graph exponentially faster than any classical one, yet it seemingly cannot say how it got there. Classically, finding a vertex and finding a route to it are the same task, because a walker can just log its steps; quantumly, logging the route destroys the interference the walk depends on. This work shows that this is not a failure of imagination but a theorem: any quantum algorithm needs exponentially many queries to write down an entrance-to-exit route, even though it can name the exit in polynomial time. That makes the speedup fundamentally "non-constructive" and is directly relevant to cryptographic proposals and path-finding problems that rest on this hardness.

**Key contributions**
- First unconditional exponential quantum query lower bound for welded-tree pathfinding, with no structural restrictions on the algorithm.
- A compressed/recording oracle for welded trees, assembled from two compressed permutation oracles: a label permutation $L$ and a column-and-color-preserving edge permutation $C$ over the middle columns $[n/2,3n/2]$; proofs of soundness, bounded growth ($O(q)$ records), and a "fundamental lemma" in this setting.
- A generalized intertwiner lemma extending Carolan's compressed permutation oracle from domains of size a power of 4 to arbitrary finite domains (error $K(q+1)^2/|S|^{1/4}$).
- A "fresh oracle" variant in which newly inserted edges never close cycles or merge recorded components, shown to be exponentially close to the real oracle since each middle color class contains $\ge \sqrt N/4$ edges.
- A compressed-oracle analysis showing the standard quantum walk keeps only its current label in the database (up to exponentially small error), formalizing why "forgetting" enables interference.

**How it works** Under the fresh oracle the recorded subgraph is always a forest, so any recorded entrance-exit path must, via a Feynman-history argument on the last insertion of a weld edge, grow monotonically outward from that weld. A union bound over paths ($O(q^2)$ overhead) reduces to bounding the probability that a component rooted at a fixed weld "escapes" to column $n/2$ or $3n/2$ while the weld record persists. That is bounded by grouping databases into an "inside" description (color sequences only, vertices hidden) and an "outside" part, and showing the oracle approximately preserves a superposition whose amplitudes are square roots of random-walk probabilities — quantizing the classical fact that escaping requires $n/2$ consecutive upward steps, each occurring with probability $\approx 1/2$.

**Why it matters** It cleanly separates search from path-finding quantumly, validates the hardness assumption behind welded-tree-based cryptographic and pathfinding constructions, and demonstrates that compressed permutation oracles are a workable tool for graph-structured lower bounds.

**Caveats** The oracle is label-plus-color rather than returning all neighbors, and the weld distribution is sampled compatibly with a fixed coloring (single-cycle equivalence recovered by a hybrid argument). The exponent $1/24$ is surely not tight; the bound is query, not time, complexity, and applies to exactly this graph family — related modified welded trees are known to admit quantum path-finding speedups.

## 2. Emergent classicality and wavefunction branching in an isolated quantum many-body system

[arXiv:2609.19254](https://arxiv.org/abs/2609.19254) · [SciRate](https://scirate.com/arxiv/2609.19254)

*Saúl Pilatowsky-Cameo, Jordan Cotler, Daniel Ranard, C. Jess Riedel*

**TL;DR** The authors construct an explicitly isolated, unitarily evolving system of *N* qubits — a chaotic kicked top with weak, SU(2)-preserving 3-local disorder — in which the collective-spin sector decoheres against the permutation (multiplicity) sector that Schur–Weyl duality supplies as an *internal* bath. They derive and numerically verify an effective Lindblad equation with rate γ = (ε/S)·J\*(εS) ≈ ε/N (up to logs), prove that the resulting spin dynamics converge to a positive classical Fokker–Planck flow on the sphere, and show numerically that the induced coherent-state histories are consistent because distinct trajectories imprint nearly orthogonal microscopic records.

**The big picture** Standard accounts of why the macroscopic world looks classical invoke an external environment that carries away phase information — which leaves out systems that have no outside, including the universe itself and modern cold-atom experiments. This work exhibits a concrete many-body model where the coarse-grained collective variable is decohered by the system's own microscopic degrees of freedom, which are invisible to any collective measurement, and shows that the macroscopic variable then follows classical chaotic equations of motion long past the time when quantum-classical correspondence normally fails. Crucially, because the full dynamics are closed and simulable, the authors can verify rather than assume the open-system description, and can directly inspect the microscopic "records" that keep alternative histories from interfering.

**Key contributions**
- An emergent, non-spatial system/bath split: collective spin ⊗ permutation multiplicity space, with d_P ~ N^{k/2} ≫ d_S ~ N, arising from symmetry rather than from a tensor-factor partition of sites.
- Heuristic microscopic derivation plus numerical confirmation of an isotropic dephasing Lindblad equation; fitted rates collapse onto γS² = εS·J\*(εS), with trace-distance error scaling as 1/√N for ε ≳ 1/√N.
- Theorem: for γ ≥ |κ|/(2S+1) the Glauber–Sudarshan P-function stays positive, and the exact evolution equals the classical Fokker–Planck equation up to O(1/S) and O(γ\*/γ). An improved "not-too-squeezed" version lowers the threshold to γ ≫ S^(−4/3), implying classicality for ε ≥ N^(−1/3+δ).
- Explicit branch/record construction: record overlaps decay as exp(−Γ D⁽²⁾) with Γ = γS²Δt/(1+γS Δt), D⁽²⁾ the cumulative squared history separation — verified numerically at N = 100, M = 5 branchings.

**How it works** The disorder ε(K̂_x Ŝ_x + K̂_y Ŝ_y + K̂_z Ŝ_z), with K̂_μ random all-to-all Heisenberg (SU(2)-invariant) couplings, is 3-local in qubits yet acts purely within one total-spin sector, factorizing as bath ⊗ system. This lets simulation run in H_S = S ⊗ P (Trotterized, δt ≤ 0.005) rather than 2^N, reaching N = 200 with k = 4 singlets seeding the multiplicity space. Histories are built by inserting spin-coherent projectors at unit time intervals; each branch factorizes into a coherent state times a record in P, and off-diagonal collective matrix elements are suppressed by the record overlap.

**Why it matters** It supplies an existence proof, with controllable numerics, for the Everettian/consistent-histories picture of intrinsic decoherence, bridging Lindblad-derivation, quantum-classical-correspondence, and branching literatures. Relevant to foundations, quantum chaos, and anyone asking what "branch" should mean operationally.

**Caveats** Interactions are all-to-all, not geometrically local; the disorder is engineered to commute with total spin, so dynamics never leave a single sector (the generic case would require a direct-sum subalgebra structure); the emergent classical variable is read off almost directly from the Hamiltonian since H and [H, Ŝ] are low-order polynomials in Ŝ. The Lindblad rate derivation is heuristic, not rigorous, and the bath correlator carries an unexplained log^α divergence specific to 2-local Heisenberg couplings. Consistency and quasiclassical Markovianity of histories are verified numerically at modest N and M = 5, not proven.

## 3. FT-Weave: Real-Time Compilation Framework for Reconfigurable Fault-Tolerant Quantum Architectures

[arXiv:2609.20573](https://arxiv.org/abs/2609.20573) · [SciRate](https://scirate.com/arxiv/2609.20573)

*Wan-Hsuan Lin, Milan Kornjača, Chen Zhao, Sheng-Tao Wang, Jason Cong*

**TL;DR** FT-Weave is a runtime (rather than ahead-of-time) compilation framework for early fault-tolerant neutral-atom architectures that jointly decides which resource states to prepare, which factory serves which logical qubit, how atoms are batched into AOD moves, and how repeat-until-success corrections are handled — all in reaction to stochastic preparation/teleportation outcomes. On 2D TFIM Trotter circuits it reports up to 3× end-to-end speedup over an offline baseline at surface-code distance 9, and shows that fully asynchronous, event-driven scheduling can be *slower* than synchronous round-based scheduling because smaller optimization windows and AOD contention outweigh the extra concurrency.

**The big picture** Fault-tolerant machines spend most of their time manufacturing and shipping the special resource states that non-Clifford gates consume, and that manufacturing succeeds only probabilistically. Compilers that assume a fixed, nominal factory output therefore bake in stalls: the schedule cannot react when a batch of states fails or arrives early. This work builds an orchestration layer that makes those decisions live, treating preparation, routing, and logical execution as overlapping pipeline stages on reconfigurable atom-shuttling hardware, and uses it to compare two representative early fault-tolerant architectures under a common model. The surprising takeaway is that exposing more parallelism is not the same as going faster — coordination quality dominates.

**Key contributions**
- A stage-aware real-time controller unifying angle collection, factory assignment, teleportation routing, and correction handling for two architectures: transversal STAR (native arbitrary-angle rotation states via TMR) and distance-5 magic-state cultivation.
- Speculative "angle collection": allocates the idle-factory budget across active rotations and *future* RUS correction levels using demand estimate 2^(−ℓ)/p_succ(θ⁽ℓ⁾), with lookahead L=3 and coarse level L′=1, via largest-remainder rounding.
- Routing-aware assignment as a rectangular min-cost max-cardinality matching (Jonker–Volgenant), with preparation edge weight d(f,q)/(ℓ+1) so speculative demands tolerate longer moves.
- AOD-compatible move batching reduced to minimum chain decomposition of a source/destination order (Dilworth → bipartite matching), plus return-path destination reassignment, cross-partition rebatching, and relay decomposition of the critical long move.
- "Rematerialization": deferring a teleportation batch when its amortized cost 2τ(B)/|B| + t_CNOT exceeds one preparation round and a closer idle factory exists (gated to ≤10% of logical qubits).
- A controlled synchronous-vs-asynchronous policy comparison on identical compilation primitives.

**How it works** Both policies maintain identical runtime state (idle/successful/returning factories, free AODs, enabled rotation requests). Synchronous execution dispatches a global preparation round, waits for all outcomes, then jointly matches and batches teleportations; asynchronous execution is event-driven and non-blocking, letting a failed factory retry while others teleport. Timing is in QEC cycles (TMR attempt = 6; cultivation check = 12.5 with p=0.25, escape = 0.5–6 with p=0.90; patch move = 0.5 per row/column). Fidelity is estimated with an independent-gadget model using logical error rates extrapolated from d=7 data.

**Why it matters** Relevant to anyone designing FTQC control stacks, neutral-atom architects, and resource-estimation efforts: it quantifies how much of the "magic-state bottleneck" is actually a scheduling and routing problem, and gives an open-source testbed (github.com/UCLA-VAST/FT-Weave) for comparing resource protocols on equal footing. The fidelity study also finds STAR better at matched distance, but cultivation at d=13 lowest overall.

**Caveats** Everything is simulation under a specific latency/error model; success probabilities are empirical fits (STAR d=9 uses an analytic k=⌊d/2⌋ form flagged as model-specific, and STAR d=13 was omitted as impractical). Classical decoding and control-loop latency are acknowledged as overhead but appear coarsely modeled. Several heuristics carry hardcoded constants (the 10% rematerialization gate, horizontal-then-vertical routing, Manhattan distance costs), and the 3× figure is against one baseline flow on one workload family.

## 4. Scalable logical qubits

[arXiv:2609.20549](https://arxiv.org/abs/2609.20549) · [SciRate](https://scirate.com/arxiv/2609.20549)

*Matthias Troyer, Chetan Nayak, John Martinis*

**TL;DR** — A position paper from Microsoft's quantum leadership proposing a formal definition of a "scalable logical qubit": an error-corrected qubit that is (i) maintained through many rounds of repeated syndrome extraction, (ii) supports a universal fault-tolerant gate set with real-time, low-latency decoding and classical feedback, and (iii) can be replicated to the hundreds or thousands demanded by real applications. The authors organize the requirements into four coupled axes — reliability, scale, capability, performance — and discuss the trade-offs among them.

**The big picture** — The field is awash in demonstrations that claim "logical qubits," but these range from a handful of post-selected states held for a few cycles to genuinely repeated, actively corrected memory. Without a shared definition, progress is hard to compare across hardware platforms and easy to overstate. This paper tries to fix the vocabulary by specifying what a logical qubit must actually do to be useful in a long algorithm — not just exist momentarily, but survive arbitrarily long computations, be acted on with a universal set of operations, be decoded fast enough to keep up in real time, and be manufacturable in large numbers.

**Key contributions**
- A concrete, application-grounded definition of a *scalable* logical qubit, intended as a community benchmark rather than a hardware-specific figure of merit.
- Decomposition of the requirement into four dimensions — reliability (logical error rate per operation and its suppression with code distance), scale (number of logical qubits), capability (universal fault-tolerant operations, including non-Clifford gates), and performance (logical clock speed, including the real-time decoding/feedback loop).
- Explicit emphasis on real-time decoding and feedback latency as a first-class requirement, which many memory-only demonstrations sidestep.
- Discussion of the trade-offs: improving one axis (e.g., lower logical error via larger distance) generally costs another (physical qubit count, logical cycle time).

**How it works** — The framing is definitional and analytic rather than experimental. The argument runs from the top down: utility-scale algorithms require end-to-end error budgets orders of magnitude below what physical qubits deliver, which dictates target logical error rates, logical qubit counts, and total logical operation counts; these in turn imply minimum code distances, decoder throughput, and feedback latencies. Demonstrations that omit repetition, universality, or real-time decoding are argued to be non-scalable in a specific, checkable sense.

**Why it matters** — Useful for anyone evaluating logical-qubit claims: experimentalists designing next milestones, algorithm and resource-estimation researchers, funders, and reviewers. A shared rubric makes roadmaps comparable across superconducting, trapped-ion, neutral-atom, and topological platforms.

**Caveats** — The LaTeX source was unavailable, so this assessment rests on the abstract; specific thresholds, numerical targets, and any comparative assessment of existing experiments could not be verified. The work appears to be a perspective/standards proposal rather than new theory or data, and definitional papers from a vendor-affiliated group inevitably encode architectural assumptions — readers should check whether the chosen axes and thresholds privilege particular hardware roadmaps.

## 5. Quantum Simulation of Dissipative Non-Markovian Coupled Classical Oscillators

[arXiv:2609.20721](https://arxiv.org/abs/2609.20721) · [SciRate](https://scirate.com/arxiv/2609.20721)

*Malte Schade, Sophia Simon, Nathan Wiebe, Scott Keating, Cyrill Bösch, Andreas Fichtner*

**TL;DR** The authors extend the Babbush et al. coupled-oscillator quantum speedup to *dissipative, history-dependent* classical systems (viscoacoustic/viscoelastic media) by approximating memory kernels with a Prony series, embedding the resulting non-Markovian dynamics into a Markovian non-Hermitian generator $\mathbf{C}=i\mathbf{H}+\mathbf{L}$ with $\mathbf{L}\succeq 0$, and simulating it with optimal LCHS at cost $\widetilde{\mathcal{O}}((\alpha_\mathbf{H}+\alpha_\mathbf{L})t/\epsilon)$ for subsystem-energy estimation. They prove the task remains BQP-complete even with strong localized damping, but also prove a Lieb–Robinson-type bound for *inhomogeneous* (source-driven) differential equations that rules out exponential advantage on local lattices, leaving a quartic speedup in 3D.

**The big picture** Real materials do not just store and exchange energy; they lose it, and the loss depends on the entire deformation history. Prior quantum algorithms for networks of springs and masses assumed no damping at all, which excludes essentially every realistic wave-propagation problem in seismology, acoustics, or structural engineering. This work shows how to fold arbitrary linear memory-dependent damping into the quantum framework, and — just as importantly — pins down honestly how much advantage remains: for locally connected systems the exponential speedup evaporates, but a substantial polynomial speedup survives in three dimensions.

**Key contributions**
- Graph-theoretic formulation with generalized Maxwell connectors (dashpot in parallel with $C$ Maxwell bodies) covering Kelvin–Voigt, standard linear solid/fluid; state $\boldsymbol\phi=[\mathbf v;\mathbf f_1;\dots;\mathbf f_C]$ of dimension $N=M+C(N_e+N_g)$, with energy-metric similarity transform making $E=\tfrac12\|\boldsymbol\psi\|^2$.
- Explicit block encodings: $\alpha_\mathbf{H}=(\sqrt{d_{\rm in}}+\sqrt{d_{\rm out}})\sqrt{Ck_{\max}/m_{\min}}$ — up to $\sqrt2$ tighter than prior work, and effectively $\propto\sqrt{K_{\rm total}}$ independent of $C$ (only $\mathcal{O}(\log C)$ gate overhead) — and $\alpha_\mathbf{L}=\max((\sqrt{d_{\rm in}}+\sqrt{d_{\rm out}})^2\|\boldsymbol\eta_0\|_{\max}/m_{\min},\|\boldsymbol\Lambda\|_\infty)$.
- BQP-completeness of subspace energy estimation *with* strong dissipation, via a dissipation-based clock construction (strengthening Krovi's result).
- A Lieb–Robinson-like locality bound for source-driven ODEs with non-positive log-norm, plus a matching classical light-cone truncation algorithm costing $\widetilde{\mathcal O}(s\Delta^D(\alpha+\omega_\chi)t(\alpha t+\log(\cdot/\epsilon))^D\log^3(\cdot))$.
- Treatment of time-varying material properties, shown to appear as effective damping or gain in the energy representation, with corresponding encodings.

**How it works** The hereditary integral $f(t)=\int G(t-\tau)v(\tau)d\tau$ is split into an instantaneous $\eta_0\delta(t)$ part and $\sum_c k_c e^{-\lambda_c t}$; each exponential becomes an auxiliary force variable obeying a first-order ODE, converting memory into extra degrees of freedom. Sparse-access oracles over head/tail/ground selector matrices build $\mathbf{H}$ and $\mathbf{L}$; LCHS then block-encodes $e^{-\mathbf{C}T}$ with $\mathcal{O}(1)$ normalization, and amplitude-estimation-style measurement yields subspace energies to error $\epsilon$ with $\mathcal{O}(\log(1/\delta)/\epsilon)$ repetitions.

**Why it matters** It gives the first unified quantum treatment of realistically damped classical wave media, and simultaneously delivers a sobering, general no-go: spatial locality plus bounded log-norm forces polynomial-only advantage even with persistent sources, a claim previously conjectured to enable exponential gains. Relevant to quantum-algorithms researchers working on linear ODEs/PDEs and to computational seismology/acoustics.

**Caveats** Speedups are query-model results assuming efficient index, phase, and (controlled) state-preparation oracles — nontrivial for heterogeneous media. The $Q_\psi$ prefactor $(\|\boldsymbol\psi(0)\|+\|\boldsymbol\chi\|_{L^1})/\|\boldsymbol\psi(T)\|$ can blow up precisely when dissipation is strong. Output is restricted to subspace energies, not full fields. The authors themselves note (Sec. on kernel approximation) that the apparent $C$-independence likely does not translate into advantage, since classical methods handle Prony expansions cheaply. The quartic 3D speedup is relative to their own new classical algorithm, is asymptotic, and ignores constant factors and error-correction overhead.
