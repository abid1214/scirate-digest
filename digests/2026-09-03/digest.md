# SciRate Daily Digest — 2026-09-03

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. A quantum oracle separation between QMA(2) and QMA

[arXiv:2609.02865](https://arxiv.org/abs/2609.02865) · [SciRate](https://scirate.com/arxiv/2609.02865)

*John Bostanci, Sabee Grewal, Jonas Haferkamp, Andrew Huang, Yeongwoo Hwang, Anand Natarajan, Chinmay Nirkhe*

**TL;DR** The authors exhibit a unitary (quantum) oracle relative to which QMA(2) ≠ QMA, resolving a ~20-year-old question in quantum query complexity. The key is a highly structured family of instances of She–Yuen's Entangled Subspace problem built from symmetric/antisymmetric subspace projectors, for which every local-unitary-invariant polynomial collapses to a *single* univariate polynomial in the dimension — with the symmetric (YES) case appearing at *negative* dimension — reducing the QMA lower bound to the approximate degree of OR. A corollary settles Watrous's no-disentanglers conjecture: for any ε+δ<1, an (ε,δ)-disentangler needs exponentially many input qubits.

**The big picture** A central open question is whether promising a verifier that its two quantum proofs are unentangled actually buys computational power. This work shows that, in a black-box setting where both verifiers get identical access to an unknown quantum operation, the unentanglement promise provably helps: there is a problem an unentangled-proof verifier solves with one query and a short proof, while any single-proof verifier needs either exponentially many queries or an exponentially long proof. As a consequence, no efficient "disentangling" device can exist that converts a short arbitrary quantum input into essentially any separable state, ruling out the most natural route to collapsing the two proof models. It also implies that any in-place amplification procedure for two-proof systems, if one exists, must use non-black-box techniques.

**Key contributions**
- First unitary-oracle separation QMA^O ≠ QMA(2)^O.
- A concrete hard family: YES = rank-one product projectors; NO = the 4-copy antisymmetric projector Π_anti^{d,4} bipartitioned as (12|34), shown to have product value ≤ 1/3 for all d ≥ 4.
- The "negative dimension" identity: one degree-≤4t polynomial q(x) satisfies q(d) = J(Π_d^−) and q(−d) = J(Π_d^+) for every local-unitary invariant J.
- QMA lower bound q²(m+1) = Ω(√D); QMA(2) upper bound of 1 query, completeness 1, soundness 1/3.
- Disentangler lower bound m ≥ Ω(√D) in the full regime ε+δ<1, matching the recent Jeronimo–Wu–Xu upper bound up to a log factor.

**How it works** Amplify-and-guess (equivalently, the trace-power/guessing lemma: tr(M_P^ℓ) is degree 2qℓ and sandwiched between λ^ℓ and 2^m λ^ℓ) removes the witness, turning QMA into a multiplicative-gap query problem. Haar-twirling over local unitaries makes the acceptance polynomial local-unitary invariant, hence a combination of traces tr[(R_σ⊗R_τ)P^{⊗t}]. Expanding these gives sums of d^{cyc(ξ)}; because registers are grouped into blocks of four, the induced permutation is always even, and sgn(ρ) = (−1)^{cyc(ρ)}, so negating d exactly interchanges symmetric and antisymmetric projectors. Setting d = 5j−1 places the YES instance at the formal point j=0 and Θ(√D) antisymmetric NO instances at j=1,…,N, giving precisely the OR approximate-degree shape (0 at the origin, within 2^{−(m+1)} of 1 on a long runway), hence degree Ω(√(Nm)).

**Why it matters** This isolates unentanglement as a genuine black-box resource and closes the natural relativizing avenue for proving QMA(2)=QMA; anyone working on separability testing, product-state optimization, or QMA(2) amplification should note that new techniques are now required.

**Caveats** The separation uses a *quantum* (unitary) oracle; a classical oracle separation remains open, and unitary-oracle separations are weaker evidence about the unrelativized world. The hard instances are extremely structured (rank-one YES subspaces), and the lower bound is q²(m+1)=Ω(√D) rather than the stronger Ω(D) one might hope for. The disentangler bound in the regime ε+δ > c−s is quantitatively weaker (the extension is only sketched in the visible source).

## 2. Optimal Fusion Strategies for Quantum Computation

[arXiv:2609.02559](https://arxiv.org/abs/2609.02559) · [SciRate](https://scirate.com/arxiv/2609.02559)

*Kenneth Goodenough, Andrew Landahl, Joon Lee, Antonio Russo, Kevin Thompson*

**TL;DR** For stabilizer codes encoding one logical qubit, the authors give an exact characterization of the best non-adaptive photonic fusion strategy: the maximum number of tolerable physical fusion failures equals the weight of the largest *minimal* logical operator, and a "perfect" strategy (only one fusion needs to succeed) exists iff the code has a full-weight nontrivial logical operator containing no stabilizer as a substring. Recast graph-theoretically, this quantity is the maximum degree of the encoding vertex over the local-complementation orbit of the progenitor graph, and random graph codes admit perfect strategies with probability $1-O(2^{-\delta n})$.

**The big picture** In photonic quantum computing, the entangling measurements that stitch resource states together succeed only about half the time, and when they fail they collapse the fused qubits in a single-qubit basis chosen in advance. Encoding logical qubits in an error-correcting code lets a logical fusion still succeed despite many physical failures, but until now there was no simple test telling you which codes and which choices of failure bases achieve the best possible tolerance. This work supplies exactly such a test for single-qubit codes, translates it into a clean graph-theoretic quantity, resolves an open question about parity-check codes, and shows that near-optimal behavior is the generic case rather than a lucky exception.

**Key contributions**
- Failure criterion via code deformation: failures on subset $W$ cause logical failure iff the substring-closure $\hat{Q}[W]$ contains a nontrivial logical operator.
- Theorem: for $[[n,1,d]]$ codes the fusion distance equals the largest minimal logical operator weight; perfect-strategy corollary.
- Identification of fusion distance with the new graph invariant $\Delta_{LC}^{(e)}(G')$ — the first operational meaning for *maximum* LC degree (contrast: minimum LC degree relates to state-preparation cost/distance).
- Explicit perfect strategies for all quantum parity-check codes $QPC(n,m)$ (alternating $X\cdots XY$ per row), answering an open question of Schmidt et al.
- Genericity: uniformly random progenitor graphs admit perfect strategies with probability $1-O(2^{-\delta n})$.
- Smallest connected-progenitor counterexample (5 qubits) that has no perfect non-adaptive but does have a perfect adaptive strategy, refuting a natural connectivity conjecture.

**How it works** Two lemmas drive the characterization: a symplectic dimension count showing $\dim(\hat Q\cap\mathcal S^\perp)-\dim(\hat Q\cap\mathcal S)=k$ for full-weight $Q$, and a Bouchet-style extension lemma letting any Pauli string be completed to full weight without gaining stabilizer substrings. A local-complementation argument shows every minimal stabilizer supported on a vertex can be rotated into that vertex's canonical generator, giving the graph statement. For the randomness result, the substring condition for the all-generators product $\Gamma_S$ is shown equivalent to a $\bmod 2$ cut condition, i.e. to $\mathrm{rank}(L_S)=|S|-1$ for the binary Laplacian of the induced subgraph. Since the full Laplacian has maximal rank only with probability $q_\infty\approx0.42$ (via Silverman's result on random symmetric $\mathbb F_2$ matrices), the proof instead searches over induced subgraphs, using a Schur-complement bound on the full-rank probability of partially fixed random symmetric matrices.

**Why it matters** Gives resource-state and FBQC architects a cheap, checkable criterion for evaluating logical fusions, plus a constraint ("perfectness") to impose while optimizing against loss and noise. It also opens a fresh graph-theory question with concrete physical stakes.

**Caveats** Restricted to $k=1$, non-adaptive strategies, failure bases limited to $X/Y/Z$, and a strictly noiseless/lossless model — no loss or Pauli error analysis. The random-code result is for the uniform graph-code (progenitor-graph) distribution, which induces a different distribution on LC classes than uniform stabilizer codes, so the analogous statement for random stabilizer codes is not implied. The $k>1$ case, and the computational complexity of finding optimal strategies / maximum LC degree, remain open.

## 3. Purification of photonic graph states

[arXiv:2609.01710](https://arxiv.org/abs/2609.01710) · [SciRate](https://scirate.com/arxiv/2609.01710)

*Matthias C. Löbl, Aliki A. Capatos, Ming Lai Chan, Peter Lodahl, Anders Søndberg Sørensen, Stefano Paesani*

**TL;DR** The authors show that multipartite entanglement purification of photonic graph states can be done with linear optics alone — replacing deterministic CNOTs with transversal type-I fusions (PBS + photon-number-resolving detectors) — because a successful type-I fusion implements exactly a CNOT followed by a computational-basis measurement of the target, up to a heralded Pauli correction. They give protocols for GHZ/CSS states, a DEJMPS generalization for self-dual-code CSS states, and a scheme covering all graph (hence all stabilizer) states via two-colorable ancilla subgraphs, with success probabilities up to 1/2 per round; numerically, a depolarized 3-qubit GHZ at F≈0.86 reaches F=0.988 in two cascaded rounds at overall probability 1/8 (4-qubit: 0.81 → 0.981 at 1/16).

**The big picture** Photonic quantum computing needs large entangled resource states, and quantum dots or similar emitters can produce them deterministically but with fidelities limited by intrinsic noise that no amount of better hardware easily removes. Entanglement purification — trading several noisy copies for one cleaner copy — has long been known for multi-party states, but existing recipes assume deterministic two-qubit gates, which photons do not have. This work rebuilds those recipes entirely out of beam splitters and detectors, showing that the standard probabilistic photonic "fusion" operation is exactly the missing ingredient, and works out which sequences of purification rounds are optimal for realistic emitter noise.

**Key contributions**
- Identification of successful type-I fusion with CNOT + destructive Z-measurement (plus heralded Z correction), enabling transversal purification circuits without entangling gates.
- Bit-flip and phase-flip purification for arbitrary CSS states, with exact success probabilities σ_b/2^{n_x} and σ_p/2^{n_z} derived from stabilizer-tableau bookkeeping (fusions are deterministic exactly when ±Z_AZ_B is stabilized, else p=1/2).
- A DEJMPS generalization using transversal exp(iπX/4) for CSS states with H_x = H_z, i.e. self-dual binary codes (e.g. the [8,4,4] extended Hamming code ↔ 8-qubit cube graph state used in FBQC), which is Y-insensitive rather than Z- or X-insensitive.
- Extension to non-two-colorable graph states via ancillary two-colorable subgraph states on an independent set A and its neighborhood Ā, with p_s = σ/2^{|Ā|}.
- Numerical optimization of cascaded round orderings under Pauli/depolarizing noise and under physical time-bin emitter noise, plus multiplexing overhead analysis.

**How it works** States are tracked in the symplectic stabilizer representation; transversal CNOTs map (a_x,a_z)⊗(b_x,b_z) → (a_x⊕b_x, a_z)⊗(b_x, b_z⊕a_z), so measuring one copy heralds either bit- or phase-flip syndromes. Phase-flip rounds are obtained by transversal Hadamards before fusion. Bit-flip rounds square the error amplitudes but amplify phase errors (term 2Fα_{0,−}), hence the need to alternate rounds; the optimal order depends on the noise model.

**Why it matters** It supplies a concrete, gate-free route to push emitter-generated resource states below fusion-based-QC error thresholds, implementable in the same switch-network-plus-delay-line architecture already envisioned for photonic sources.

**Caveats** Density matrices are assumed diagonal in the graph/Bell basis (otherwise twirling is needed, and the quoted fidelities are lower bounds); analysis assumes lossless photons and ideal PNR detection; success probability falls as 1/2^{n_x} per round, so multiplexing overhead grows with state size; ancilla graph states in the general scheme must themselves be purified; the DEJMPS variant applies only to the restricted self-dual class.

## 4. Transversal Gates and Magic State Distillation in an Optimally Synthesized Spin-Qubit Shuttling Bus

[arXiv:2609.02641](https://arxiv.org/abs/2609.02641) · [SciRate](https://scirate.com/arxiv/2609.02641)

*Pau Escofet, Andrii Semenov, Niall Murphy, Elena Blokhina, Carmen G. Almudéver, Sergi Abadal, Eduard Alarcón*

**TL;DR** This work extends the "Quantum Reverse Mapping" co-design methodology — which synthesizes a 1D spin-shuttling bus layout directly from a surface code's syndrome-extraction schedule — from a single logical qubit to a full multi-logical-qubit processor supporting transversal CNOTs with all-to-all logical connectivity. Under a realistic spin-qubit noise model it finds a shuttling-velocity threshold of ~9–9.5 m/s, shows that a "symmetric" shuttling policy (swapping logical qubit positions after a gate) cuts transversal-CNOT logical error by up to 60% at d=13, and demonstrates ancilla sharing and a 2D junction grid as levers for long-range gate fidelity, culminating in an optimized 15-to-1 magic state distillation layout.

**The big picture** Most error-correction hardware co-design work optimizes the layout for keeping one logical qubit alive, leaving the question of how error-corrected qubits actually talk to each other for later. Here the authors take a semiconductor spin-qubit platform in which electrons are physically conveyed along a shared track between storage sites and gate sites, and show that this mobility buys something superconducting chips cannot easily get: direct, pairwise logical gates between any two logical qubits without the space-and-time overhead of stitching code patches together. They then quantify the tradeoffs — moving qubits costs coherence, so packing logical qubits more densely helps distant gates but hurts routine error correction — and apply the resulting design to the resource-hungry subroutine that supplies the non-Clifford resource states needed for universal computation.

**Key contributions**
- Multi-element bus: concatenated logical elements, each with d² storage zones and d² operation zones (one more than the d²−1 needed for syndrome extraction), giving all-to-all logical connectivity.
- Symmetric vs. asymmetric shuttling policies for transversal CNOT; symmetric wins by 45/50/60% at d=9/11/13.
- Ancilla sharing: m logical qubits per ancilla set, element length growing only as ~(m+1)/2 (1.45× for m=2, 2.35× for m=4); m=2 beats m=1 for tCNOTs beyond 14 logical hops at T_φ^Store=400 µs.
- 2D grid via single-dot junctions (50 ns turn penalty), reducing inter-element distance.
- Quantum Reverse Mapping applied at the *logical* level to place the 15-to-1 distillation circuit.

**How it works** Noise model separates gate depolarization, readout X-error, idling T₁/T_φ with distinct storage (100–800 µs) vs. operation-zone (10–30 µs) dephasing, and distance-dependent shuttling dephasing T_φ^Sh = T_φ^Bus·√((d_Sh+l_c)/l_c) with l_c=13 nm. Per-round LER extracted by fitting P_L = ℰ₀(1−ℰ_d)ⁿ + 1/2; per-gate tCNOT error via logical randomized benchmarking with the two-qubit analog. Sweeps cover d=3–13 and velocities 1–320 m/s.

**Why it matters** Operation-zone dephasing (micromagnet-induced) emerges as the dominant limiter, while bus dephasing is nearly irrelevant — a concrete, actionable message for spin-qubit fabrication. The logical-hop scaling and code-distance crossovers give architects a quantitative handle on when larger codes stop paying off for long-range gates.

**Caveats** Results are simulation-only, surface-code-specific, and reported in the worst-case X basis given the strongly Z-biased noise; decoder details and classical latency are not discussed. Round-Robin ancilla-sharing numbers are conservative and no realistic prioritization compiler is given. The junction turn penalty is admittedly an arbitrary placeholder, and leakage, crosstalk, valley physics, and charge-noise correlations are absent from the model. Global-bus control constraints (all qubits on a segment move together) at large scale remain to be compiled for.

## 5. Circuit-Level Loss Performance of FFCC and RHG Codes in a Compound Photon-Atom Quantum Architecture

[arXiv:2609.02428](https://arxiv.org/abs/2609.02428) · [SciRate](https://scirate.com/arxiv/2609.02428)

*Dana Ben Porath, Juval Bechar, Daniel Azses, Yaron Jarach*

**TL;DR** Under an architecture-aware circuit-level photon-loss model for a photon–atom (atom–cavity + flying photon) MBQC platform with near-deterministic photon–atom CZ gates, the standard RHG (foliated toric) cluster state beats both the Foliated Floquet Color Code and its reduced variant: thresholds of 2.75% vs. 1.45% and 1.85% per lossy operation, despite RHG's higher graph degree. The ordering only flips in favor of reduced FFCC when intermodule links carry roughly ≥3× extra loss, or in narrow low-loss windows at matched atom budgets.

**The big picture** Low-degree "Floquet-like" codes are often claimed to be better suited to photonic fault tolerance because each qubit participates in fewer entangling operations, and each operation is a chance to lose a photon. This paper tests that intuition on hardware where the entangling gate is a near-deterministic light–matter interaction rather than a probabilistic fusion, and finds the intuition fails: the older, higher-degree surface-code foliation wins on both threshold and logical error rate across most realistic operating points. The lesson is that code rankings are not intrinsic — they depend on the native entangling primitive, on how loss propagates through the generation schedule, and on where in a modular system the lossy links sit.

**Key contributions**
- Explicit hardware-compatible generation schedules for all three codes in two families: a *bipartite* scheme (one graph partition photonic, one atomic) and a *STAP* scheme (atom-to-photon state transfer mid-circuit).
- Circuit-level loss thresholds under a common model: RHG 2.75% (scheme-independent), FFCC 1.45%/1.25%, reduced FFCC 1.85%/1.50% (bipartite/STAP), versus IID benchmarks of 25%/8.5%/13.5%.
- A modular-loss study showing threshold-ordering reversal between excess intermodule loss q=2p and q=3p.
- Resource-matched comparisons using per-layer qubit counts (3d², 3d², 2d²) and peak simultaneously-active atoms (5d² for RHG vs 3d² for rFFCC).

**How it works** Every lossy primitive (photon generation, photon participation in a CZ, STAP, photon detection) gets probability p; atomic readout gets 2p. Loss is heralded only at detection, so each photon cycle is split into intervals between its CZs; conditioned on non-detection, the loss time is sampled with the correct conditional probabilities, implemented in Stim via CORRELATED_ERROR/ELSE_CORRELATED_ERROR chains. Missing downstream bonds are represented as a single correlated dephasing channel on the remaining neighbor set (not independent depolarization, as in prior erasure-qubit models), then decomposed into graphlike mechanisms and decoded with MWPM. Distances are estimated with `shortest_graphlike_error()` and cross-checked via fitted LER exponents β slightly above 1.

**Why it matters** It gives a concrete, primitive-specific counterexample to the "lower degree wins" heuristic that has driven honeycomb/Floquet code adoption in fusion-based photonics, and supplies a reusable recipe for conditional, delayed-heralding loss modeling in Stim. Relevant to anyone designing hybrid light–matter fault-tolerance stacks.

**Caveats** Photon loss is the *only* channel: no Pauli noise, atomic dephasing, or distinguishability. All boundaries are periodic (memory only, logical-X observable, no logical operations or boundary effects). MWPM discards the correlated structure it decomposes away, likely underestimating achievable thresholds. Graphlike distance is an upper bound on true fault distance. The large-scale comparison extrapolates a two-parameter LER ansatz with β fixed to 1, and the intramodule/intermodule split (first two CZs local) is an assumed, not derived, partition.
