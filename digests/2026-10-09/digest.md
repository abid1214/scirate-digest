# SciRate Daily Digest — 2026-10-09

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Single-shot magic state factories for quantum LDPC codes

[arXiv:2610.10731](https://arxiv.org/abs/2610.10731) · [SciRate](https://scirate.com/arxiv/2610.10731)

*Varun Menon, Rohan Mehta, Andi Gu, Andrei C. Diaconu, Daniel Bochen Tan, Xiao Xiao, Michael J. Gullans, Qian Xu et al.*

**TL;DR** The authors build a magic-state factory that generates non-Clifford resource states transversally in 3D balanced-product "tricycle" codes and then teleports them, via a depth-1 homomorphic CNOT, into algebraically matched 4D "quadcycle" codes that have larger, balanced distances and are single-shot in both Pauli bases. At circuit-level depolarizing noise $p=10^{-3}$, the resulting CCZ states reach logical error rates of $1.2\times10^{-5}$ to $\sim10^{-8}$ at 10–40× lower expected space-time volume than surface- or color-code cultivation, and they arrive already encoded in a high-rate LDPC block.

**The big picture** Low-density parity-check codes promise far fewer physical qubits per logical qubit than the surface code, but nobody had a cheap, native way to produce the non-Clifford resource states that universal computation requires inside such codes. This work pairs two code families with shared algebraic structure: one is good at producing magic cheaply but cannot hold it, the other is good at holding and processing it but cannot produce it. A single layer of physical gates moves the magic from the first to the second, with postselection applied in the brief window where errors are detectable but the state is still cheap to throw away. The result is the lowest reported space-time cost for magic state production to date, delivered directly in the kind of high-rate block a downstream algorithm would use.

**Key contributions**
- Quadcycle codes: four-element abelian group-algebra (balanced/lifted product) CSS codes with $6n_G$ qubits, metachecks in *both* bases, an $X$–$Z$ duality forcing $d_X=d_Z$, and depth-1 translation automorphisms; concrete pairs from $[[54,6,6]]$ to $[[420,6,25]]$.
- The "escape": the quadcycle complex is the mapping cone of multiplication by $d$ on the tricycle complex, yielding a canonical embedding and a depth-1 transversal homomorphic CNOT covering all $k_{3\mathrm{D}}$ logicals ($k_{4\mathrm{D}}=2k_{3\mathrm{D}}$ saturated).
- A fan-out gadget (distance-2 repetition concatenation, reusing $Z$-ancilla qubits) that compresses the CCZ circuit from depth 2 to depth 1, preserving circuit distance; measured error exponents $3.11\pm0.04$ and $3.91\pm0.07$ confirm full-detection doubling of effective distance.
- Downstream gadgets: homomorphic measurement extracting two disjoint CCZ states from the nine-qubit $\det$ hypergraph state, plus teleported CZ fix-ups.
- Explicit neutral-atom compilation: monomials act as uniform AOD row/column translations; constant number of array traversals per operation.

**How it works** Three tricycle blocks in $|\bar+\rangle$ receive a depth-1 transversal CCZ producing the $|\det_3\rangle$ hypergraph state; three quadcycle blocks are prepared single-shot in $|\bar0\rangle$; one transversal CNOT layer teleports the magic; transversal $X$ readout of the tricycle blocks supplies both Pauli-frame corrections and full detector-based postselection. Simulations are in Stim under SD6 with a three-qubit depolarizing CCZ channel ($p_{\mathrm{CCZ}}=p,2p$), decoded by most-likely-error; quadcycle memory uses sliding-window ($W=3,S=1$) single-shot decoding.

**Why it matters** This closes the main missing piece of qLDPC architectures — a native, high-throughput non-Clifford source that preserves the rate advantage — and should interest anyone doing fault-tolerant resource estimation or neutral-atom architecture design.

**Caveats** Only a single tricycle–quadcycle pair is simulated; cross-block CCZ correlations are traced out, and full-factory yield is the cube of the quoted per-block acceptance. Space-time accounting excludes the homomorphic logical measurements, CZ fix-ups, injection surgery, and decoder latency (also excluded for the baselines). Larger-code distances come from Stern's algorithm, and the $[[162,6,14]]$ point at $p=10^{-3}$ is extrapolated as $p^{d/2}$ with $d=12$. Soundness is established only for some codes, and MLE decoding is not real-time-practical.

## 2. Error-Corrected Memory and Logic on a Heavy-Hex Superconducting-Qubit Processor

[arXiv:2610.11658](https://arxiv.org/abs/2610.11658) · [SciRate](https://scirate.com/arxiv/2610.11658)

*Campbell K. McLauchlan, Georgia M. Nixon, Julien M. Drouet, Xanda C. Kolesnikow, Seok-Hyung Lee, James Raftery, Karthik Siva, Stephen D. Bartlett et al.*

**TL;DR** The authors run a distance-scaled dynamic compass (Floquet-like) code across all 156 qubits of an IBM Heron heavy-hex chip, combining ACES-derived circuit-level Pauli noise models, explicit exclusion of two bad qubits and their couplers, and IQ-based leakage post-selection to cut logical error per round by ~32–35% in memory (to 4.11% in Z, 2.56% in X) and failure probability by up to 56% in 30-round stability experiments. Lattice surgery between two small patches reaches Bell fidelity lower bounds of 77.3% with pre-selection alone and >97% with logical-gap post-selection at 27% relative yield.

**The big picture** Real superconducting chips are not uniform: a handful of qubits or couplers are often one to two orders of magnitude noisier than the median, and these outliers can dominate the error rate of any code large enough to cover them. This work shows that simply refusing to use the bad components — redesigning the sequence of parity checks so the code routes around them — plus feeding the decoder a carefully measured, device-specific noise model and discarding runs where atoms of the processor have leaked out of their computational states, recovers most of the lost performance across memory, logical measurement, and a two-patch merge-and-split logic operation. It is a practical demonstration that monolithic, imperfect processors can still be pushed toward the regime where bigger codes help rather than hurt.

**Key contributions**
- First defect-exclusion construction for the dynamic compass code on a heavy-hex array: gauge checks are deformed into superstabilizers avoiding dead qubits (weight-2/3 X checks, weight-1 Z checks; stabilizer weight grows from 8 to at most 10 near defects).
- Full-device 7×7 memory on 156 qubits, reaching parity with the *median* 5×5 patch in Z and beating the mean 5×5 patch in X once defects are excluded.
- Demonstration that defect exclusion yields a roughly constant ~27–28% gain even with an ACES-informed BeliefMatching decoder — decoders cannot absorb defects.
- Stability experiments with 16 checks/round showing continued error suppression out to 30 rounds only with defect exclusion (plateau at ~12 rounds otherwise), attributed to leakage, not Pauli noise.
- Leakage/code-space *pre*-selection for lattice surgery (abort before running), plus exclusive-decoder logical-gap and belief-propagation-convergence post-selection.

**How it works** ACES supplies layer-specific Pauli error rates as BeliefMatching priors; IQ readout data is fit to Gaussian mixtures over |0⟩,|1⟩,|2⟩ to give per-shot leakage probabilities (cut at 0.9 memory / 0.7 stability) and soft measurement-error priors. Bell fidelity is bounded from ⟨X̄X̄⟩ and ⟨Z̄Z̄⟩ since ⟨ȲȲ⟩ is inaccessible.

**Why it matters** Relevant to anyone building or decoding on monolithic superconducting hardware: it quantifies the relative payoff of better noise models versus hardware-aware code surgery, and shows leakage is the dominant ceiling on long logical operations.

**Caveats** Everything is above threshold — 3×3 patches still beat 7×7. Lattice surgery uses only d=3-scale patches and leans heavily on selection (total yield 4.55% for the best 3×3 result; pre-selection alone discards 86.7% of attempts). No mid-circuit reset halves timelike distance. Some ACES models came from different days or slightly different circuits. Only BeliefMatching was tested; stronger decoders might change the defect-exclusion conclusion. The soft-information/ACES redundancy is observed in stability only, with unclear generality.

## 3. On PPT entanglement distillation

[arXiv:2610.12454](https://arxiv.org/abs/2610.12454) · [SciRate](https://scirate.com/arxiv/2610.12454)

*Ludovico Lami*

**TL;DR** This paper gives an exact regularised formula for the PPT distillable entanglement as the limit of a measured-relative-entropy-like POVM functional, plus two new converse bounds built from operator quadratic forms and from Hirschman's sharpening of the Hadamard three-line theorem. Together these settle (negatively) the conjecture that PPT distillable entanglement equals the regularised Rains bound: for a qutrit Werner state with antisymmetric weight 25/26, a certified upper bound of 0.62107 ebits sits strictly below the Rains value ≈0.64766.

**The big picture** How much pure entanglement can be extracted from many copies of a noisy quantum state is one of the central unsolved questions of quantum information theory. To make progress, people relax the physically motivated class of local operations and classical communication to a larger, mathematically tractable class defined by a positivity condition under partial transposition, and the best known upper bound in that relaxed setting has long been conjectured to be exactly tight. This work shows the conjecture is false, exhibiting a concrete, certified gap for one of the simplest symmetric two-qutrit families, while also supplying an exact (though regularised) characterisation of the achievable rate and a new quantitative guarantee that any state with negative partial transpose yields a strictly positive distillation rate.

**Key contributions**
- Exact identity E_d,PPT(ρ) = L^∞(ρ) = sup_n L(ρ^⊗n)/n, where L is a POVM optimisation of Σ_j p_j log(p_j/‖E_j^Γ‖_∞) — Rains's projective bound with projections replaced by general POVMs, then regularised. An auxiliary variant L̃ (keeping |E_j^Γ| before norming) has the same regularisation.
- A faithful negativity lower bound: E_d,PPT(ρ) ≥ 1 − h₂(1/2 + N(ρ)/(d+1)), making the Eggeling–Vollbrecht–Werner–Wolf qualitative NPT-distillability theorem quantitative.
- Two new converses E_Q and E_A, both yielding exponential strong converses, and hence new computable upper bounds on LOCC distillable entanglement alongside R^∞ and squashed entanglement.
- Refutation of the Regula et al. conjecture E_d,PPT = R^∞, with 0.5836 ≤ E_d,PPT(ρ_{25/26}) ≤ 0.6211 < 0.6477.

**How it works** Achievability: apply a fixed block POVM i.i.d., accept weight-typical words, and bound ‖Q^Γ‖_∞ via a wordwise spectral sandwich, so the rate equals the weighted objective; the converse pulls back the Bell test as a two-outcome POVM. E_Q uses left-multiplication superoperators and weighted geometric means on Hilbert–Schmidt space, with the transformer inequality giving data processing for a quadratic functional V_α; an all-copies quadratic domination condition ties ⟨Q⊗X, 𝒦[Q⊗X]⟩ to ‖Q^Γ‖_∞^α, and conditioning on an ancilla subtracts its contribution. E_A embeds ρ's reference state in an operator-valued analytic family on an annulus, bounds min{log‖Z‖₁, log‖Z^Γ‖₁ − R} on both boundary circles, averages with Hirschman's explicit positive density, then transfers to ρ via sandwiched Rényi hypothesis testing. Werner numerics use twirling to reduce to a linear program (a 48-copy POVM certifies the lower bound) and directed rounding for the upper bound.

**Why it matters** This removes the main candidate closed form for PPT distillation, redirects effort toward genuinely new converse technology, and supplies the first quantitative negativity-based distillation rate. The analytic-family and quadratic-form techniques look reusable well beyond entanglement theory.

**Caveats** The formula is regularised with no convergence-rate guarantee; E_d,PPT is shown only lower semicomputable, and its Turing computability is now open since the R^∞ algorithms no longer apply. E_Q's hypothesis is an all-copies constraint, not its one-copy version. The gap is numerically modest (~4%) and rests on certified but finite-certificate computations, and nothing is concluded about LOCC distillability or NPT bound entanglement.

## 4. 2 Fast 2 Surgery: Fast surgery on QLDPC codes with $\tilde{O}(n(k + d))$ space overhead

[arXiv:2610.11079](https://arxiv.org/abs/2610.11079) · [SciRate](https://scirate.com/arxiv/2610.11079)

*Nouédyn Baspin*

**TL;DR** This paper shows that the Baspin–Berent–Cohen fast (constant-time) surgery scheme for QLDPC codes can be run with only $\tilde{O}(n(k-\kappa+d))$ ancilla qubits when measuring a $\kappa$-dimensional subspace of logicals, improving the previous $\tilde{O}(nkd)$ and matching the $\tilde{O}(nk)$ cost of ordinary (slow) surgery up to the additive $nd$ term. The construction inverts the usual design logic: build a *dense* ancilla that manifestly expands, then sparsify it with gadgets proven to preserve expansion.

**The big picture** Logical operations on quantum error-correcting codes normally stall for a number of rounds proportional to the code distance; recent "fast surgery" schemes remove that delay but pay for it with a large block of helper qubits. The question is how cheaply such a helper system can be built. Here the author shows it can be built roughly as cheaply as for ordinary slow surgery, by starting from a helper system that has the needed robustness property but overly heavy parity checks, and then thinning those checks with transformations that provably do not destroy the robustness. This brings constant-time logical measurement into a space budget comparable to standard surgery, which matters for architectures where logical cycle time, not qubit count, is the bottleneck.

**Key contributions**
- Main theorem: a surgery ancilla complex that is 1-expanding relative to the projection onto the code, has the right homology image, preserves the cosystole, has $O(1)$-sparse $\partial_1$ and chain map, and has $\dim D_0 \le \tilde{O}(n(k-\kappa+d))$.
- A "dense expanding map" $\sigma = [\sigma_{\text{cocycles}};\sigma_{\text{boost}}]$ with only $O(k-\kappa + d\log n)$ rows, where $\sigma_{\text{cocycles}}$ kills unwanted logicals and $\sigma_{\text{boost}}$ is a random compression $R[H_{\text{logical}};\partial_1]$.
- A random-coding lemma: $t=O(d\log(em/d))$ random rows suffice to inflate all nonzero syndromes of weight $<d$ up to weight $\ge d$.
- The $d$-threshold property (stronger than relative systolic expansion) and proofs that Williamson's non-decongested gauging gadgets preserve it.
- A new *dual*-gauging (degree-reducing) gadget: replacing each high-degree qubit by an expander-graph vertex cluster (a generalized layer code), with explicit path-based correction map $\phi$ ensuring chain-map commutation.
- A slick cosystole-preservation argument: $\sigma\partial_2=0$ forces $(\ker\sigma)^\perp\subset Z^1(C)$, so added redundancies cannot shrink $\syst^1$.

**How it works** The ancilla is $\fib(\sigma)$ over a copy of the code itself (crucially $D_2=C_2$, which is what makes cosystole preservation work). Expansion is obtained by brute force: syndrome weights are boosted above $d$ by random coding. Then two sparsification passes — gauging (weight reduction via expander graphs attached to each row of $\sigma$) and dual gauging (degree reduction via expander data layers of size $\omega_\dagger+1$) — are composed into $\gamma^{\text{sparse}} = \gamma\circ\pi\circ\rho$, each step shown to preserve the threshold/expansion property, the homology isomorphism, and the cosystole.

**Why it matters** Relevant to anyone designing QLDPC architectures with low logical latency: it removes a factor of $d$ from the dominant space cost of the most general fast-surgery construction, and for constant-rate codes the result is optimal up to polylogs.

**Caveats** $\partial_2^{D^{\text{sparse}}}$ (the metachecks) is not sparse — the dual-gauging data layers force $\tilde\partial_2^A$ to act densely — so single-shot structure is lost; the author flags this as the main practical limitation and the key open problem. $\sigma_{\text{boost}}$ is existential (random matrix, no derandomization). Hidden constants from expander degrees and path choices are not tracked, and there are no numerics or threshold simulations. The near-optimality discussion leans on an $\Omega(k^2)$ lower bound whose citation is missing in the source.

## 5. A lower bound on the overhead of surgery on sparse stabiliser codes

[arXiv:2610.11097](https://arxiv.org/abs/2610.11097) · [SciRate](https://scirate.com/arxiv/2610.11097)

*Nouédyn Baspin*

**TL;DR** A simple but sharp counting argument shows that any lattice-surgery scheme on a sparse stabiliser code, using sparse ancilla systems, must use at least Ω̃(k²/ω log n) ancilla qubits to be able to measure an arbitrary logical subspace. This nearly matches the Õ(tn) upper bound of recent parallel-surgery constructions, making it essentially tight (Ω̃(n²) vs Õ(n²)) for constant-rate codes.

**The big picture** Reading out logical information from a quantum error-correcting code is usually done by attaching an ancillary patch of qubits that fuses with the code — lattice surgery. Recent work has generalised this to arbitrary low-density-parity-check codes and to measuring many logical operators at once, raising hopes that readout could be made cheap even for high-rate codes. This paper shows a fundamental obstruction: if you demand the freedom to measure *any* chosen collection of logical degrees of freedom, the ancilla must grow roughly as the square of the number of encoded qubits, because there are simply far more possible measurement requests than there are sparse ancilla gadgets of a given size. The consequence is a space–time trade-off: cheap ancillas can only serve a tiny fraction of the possible measurements, so generic readout must be broken into many sequential rounds.

**Key contributions**
- A no-go theorem: for the set 𝓕 of subspaces a surgery scheme can measure, the ancilla size obeys N⋆ ≥ Ω(log|𝓕| / (ω log n)) — an "addressability vs. overhead" bound.
- Specialisation to all k/2-dimensional subspaces of the X-logical space gives N⋆ ≥ Ω(k²/(ω log n)).
- Demonstrates near-tightness of the Õ(tn) parallel-surgery construction of Cowtan et al. for constant-rate codes.
- Observes that near-linear-overhead surgery via "suitable subcodes" cannot be generically addressable when k ≫ √n, since such subcodes must be rare.

**How it works** Surgery is formalised as a symplectic embedding of an ancilla CSS chain complex D into the code's symplectic complex C, with a chain map g and defect map p; the measured subspace is [g](H₁(D)). Fixing ω-sparsity of ∂₁^D and g, the number of ω-sparse binary matrices of size s×t is at most (1+s)^{ωt} (binomial sum bound). Counting pairs (∂₁^D, g) over all dimension splittings d₀+d₁ ≤ N⋆ yields |𝓕| ≤ (1+N⋆)²((1+N⋆)(1+2n))^{ωN⋆}; combined with the Gaussian-binomial lower bound 2^{r(l−r)} = 2^{k²/4} on the number of k/2-dimensional subspaces, the result follows after eliminating the log N⋆ term.

**Why it matters** It sets a hard architectural limit for anyone designing logical readout for high-rate qLDPC codes: full addressability is not achievable at constant or linear ancilla overhead, and compilers must trade ancilla area against rounds of surgery.

**Caveats** The bound is worst-case over measurement sets, not a lower bound for any particular measurement; a scheme that only ever measures a restricted, structured family (small |𝓕|) escapes it entirely. It becomes vacuous for k ≲ √n. It constrains static ancilla gadgets per measurement; adaptive, reconfigurable, or multi-round protocols are not directly covered, and no matching lower bound on time is proved. Sparsity of both ∂₁^D and g is essential, and the bound degrades linearly in the weight ω and loses a log n factor relative to the known upper bound.
