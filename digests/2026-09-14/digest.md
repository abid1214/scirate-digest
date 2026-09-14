# SciRate Daily Digest — 2026-09-14

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. 2609.13032

[arXiv:2609.13032](https://arxiv.org/abs/2609.13032) · [SciRate](https://scirate.com/arxiv/2609.13032)



**TL;DR** The paper proves QMA = QMA₁: every QMA proof system can be made perfectly complete, and moreover with a fixed finite gate set {X, CNOT, Toffoli, H⊗H} with rational entries. The trick is to have Merlin certify not the (algebraically intractable) top eigenvalue of the acceptance operator, but a single diagonal entry Γ_z = ⟨z|(2E)^ℓ|z⟩ of a poly-power of it, which is an exactly describable dyadic rational, and to use it to close a finite non-unitary "history" into an exact cycle. Immediate corollaries: quantum 3-SAT, XZ-quantum 6-SAT, and gapped clique homology are QMA-complete, and QMA₁ ≠ QCMA relative to known classical oracles.

**The big picture** A twenty-year-old open question asks whether quantum verifiers who check quantum proofs can always be redesigned so that honest proofs are accepted with certainty, rather than merely with high probability. Known black-box obstructions show any solution must exploit the internal arithmetic of the verifier, and this work does exactly that: after recompiling into a gate set whose matrix entries are fractions with powers of two, the prover can hand over an exactly representable number that lets the verifier close a consistency check with no slack. Beyond settling the question, this collapses a whole family of hardness results that had been stated only for the perfectly complete class into hardness for the standard class, and it establishes for the first time that the perfectly complete class even has a universal gate set.

**Key contributions**
- QMA = QMA₁^{G₂}, hence QMA₁ (over any gate set exactly implementing G₂, including Clifford+T and Hadamard/Toffoli/X) equals QMA; G₂ is universal for QMA₁.
- Quantum 3-SAT, XZ-quantum 6-SAT, and weighted/unweighted gapped clique homology are QMA-complete.
- The construction relativizes to classical (XOR and in-place permutation) oracles, so recent classical oracle separations of QMA from QCMA now separate QMA₁ from QCMA.

**How it works** Aharonov's real simulation compiles any verifier into G₂ with completeness/soundness unchanged (eigenvalues just double in multiplicity), making 2^{2g}E an integer matrix. Set A = 2E: YES gives λ_max ≥ 4/3, NO gives ‖A‖ ≤ 2/3. With ℓ ≈ 4(m+1), Tr(A^ℓ) ≥ (4/3)^ℓ forces some z with Γ_z = ⟨z|A^ℓ|z⟩ > 2, and Γ_z is rational with O(hℓ) bits. Since Γ_z^{-1}|z⟩⟨z|A^ℓ|z⟩ = |z⟩, the history Σ_t |t⟩A^t|z⟩ is an exact fixed point of the cyclic operator C_{z,Γ} = shift⊗A plus the closing rank-one term. In NO cases C factors as unitary × block-diagonal, so ‖C‖ = max{‖A‖, 1/Γ} ≤ 2/3 for any claimed Γ ≥ 2, giving ‖(I−C)|ψ⟩‖ ≥ 1/3 unconditionally. An LCU block encoding over a 2^k-index register — a branches of I, 2a of −T, b of −R_z, with Γ = a/b — realizes (a/M)(I−C) exactly using only G₂ gates plus reversible arithmetic; rejection is the all-zeros ancilla outcome, giving rejection probability 0 in YES and ≥ 1/576 in NO.

**Why it matters** It removes perfect completeness as a distinguishing property of QMA, cleanly upgrading a decade of QMA₁-hardness results (Bravyi, Gosset–Nagaj, Crichigno–Kohler, King–Kohler, Rudolph) to QMA-completeness, and it circumvents the Aaronson and Aaronson–Harris–Witteveen black-box barriers by using arithmetic structure rather than amplification.

**Caveats** Raw soundness is only 1 − 1/576 (amplifiable by parallel repetition, which preserves completeness 1). Necessarily fails for quantum oracles. The prover must send a classical certificate of poly length in addition to a highly nonuniform history state. Analogues for BQP₁ and QMA₁(2) remain open, and the argument visibly breaks there (no prover; no operator-norm bound on product states). The proof is short and self-contained but new enough that independent verification is still pending.

## 2. 2609.12146

[arXiv:2609.12146](https://arxiv.org/abs/2609.12146) · [SciRate](https://scirate.com/arxiv/2609.12146)



**TL;DR** QUOPS is a cross-platform, application-agnostic benchmark that reports the largest random rotation+CNOT circuit (in a "size within the cone w²≤s≤w³" sense) a machine can execute with mean process polarization ≥1/√e, together with an error-mitigation-adjusted throughput ("QUOPS rate"). Measured directly on physical qubits, Quantinuum Helios reaches 1504 QUOPS at 303 QUOPS/s, H2-1 1320, Google Willow 216 (at 2×10⁷ QUOPS/s), IBM Boston 204; an 8-logical-qubit Steane-code processor on Helios reaches 40 QUOPS at 4.9 QUOPS/s. Mapping RSA-2048 and FeMoco resource estimates into the same units gives targets of ~2.5–3.4×10⁸ QUOPS — five orders of magnitude away.

**The big picture** Different quantum computers use incompatible qubit technologies, connectivities, and error-correction schemes, so claims about who is ahead, and how far anyone is from useful computation, are hard to adjudicate. This work defines a single measurement — how big a generic, algorithmically representative random computation a machine can run correctly, and how fast — that can be run identically on superconducting chips, trapped ions, and error-corrected logical qubits, and that can be compared against published resource requirements for landmark problems like breaking RSA encryption or simulating a nitrogenase cofactor. Running it on four leading machines shows current hardware falls short of useful computation by about five orders of magnitude in capability, though not in speed, and that raw qubit-level improvement alone will never close the gap.

**Key contributions**
- A benchmark family whose circuit width and size are independently varied, yielding a two-dimensional "capability region" rather than a single square-circuit number as in quantum volume; verification is classically efficient via mirror-circuit fidelity estimation, unlike quantum volume.
- A defensible single-number score: largest passing size inside the cone w²≤s≤w³, excluding classically easy shallow/narrow shapes and bracketing plausible first-utility circuit shapes.
- A throughput metric Ω = 2s·γ̂²/τ_wall·√(κ_total κ_kept) that charges for error-mitigation sampling overhead (~1/α²) and postselection discards, unlike CLOPS.
- First head-to-head measurement of physical- and logical-qubit architectures on identical footing, including a distance-3 fault-tolerant Steane-code processor.
- A non-Clifford resource-matching translation converting Toffoli-count resource estimates into QUOPS targets (Toffoli→~4 T; error-per-T matched to synthesis precision).

**How it works** QUOPS circuits alternate random all-to-all CNOT pairings with random single-qubit R_P(θ) rotations; size counts single-qubit gates plus 2× CNOTs. Architecture-specific compilation (routing, synthesis, serialization) is allowed, with compilation barriers preventing cheating. Success at shape (w,s) requires the lower end of a one-sided 95% confidence interval on mean polarization to exceed α; capability regions use Hochberg multiple-testing control at 90% confidence and monotonicity in w,s. Error-mitigated regions with α<1/√e are partly extrapolated via ML fits to γ̄ = exp(−r_w s). Projections use FLASQ surface-code modeling and a [[20,2,6]] concatenated symplectic double code.

**Why it matters** Gives funders, roadmap-writers, and skeptics a hardware-agnostic yardstick anchored to utility targets. Historical extrapolation from quantum volume data gives doubling times of 1.4 yr (Quantinuum) / 2.1 yr (IBM), reaching utility only in 2050–2070 — a 4× acceleration is needed for early-2030s roadmap claims. It also operationalizes Gottesman's fault-tolerance criterion: the first logical architecture to beat every physical-qubit score (plausibly ~10⁴ QUOPS, projected achievable with 20–30 logical qubits on 1000–5000 physical).

**Caveats** The challenge-problem translation is approximate: it ignores Clifford errors, assumes Clifford+T compilation, and R_P(θ)-heavy circuits are only an indirect proxy for Toffoli-dominated algorithms. All-to-all CNOT layers likely overstate routing cost relative to real algorithms. Error-mitigated scores rely on exponential extrapolation beyond executed circuit sizes and may not be operationally achievable; the 1/α² overhead is a heuristic. The Steane-code demo (distance 3, chosen for simplicity) is far from saturating Helios's fault-tolerant capability and is beaten by bare physical qubits.

## 3. 2609.12219

[arXiv:2609.12219](https://arxiv.org/abs/2609.12219) · [SciRate](https://scirate.com/arxiv/2609.12219)



**TL;DR** The paper gives the first tomography algorithm whose complexity scales with the *support size* of a quantum state rather than the Hilbert space dimension: an $n$-qubit $k$-sparse pure state can be learned to infidelity $\eps$ using $\tilde O(k/\eps)$ single-copy measurements and $\tilde O(kn/\eps)$ gate time, both optimal up to polylogs. Via the random-purification-channel trick this yields $\tilde O(kr/\eps)$ samples for $k$-sparse rank-$r$ mixed states, matching a simple $\Omega(kr/\eps)$ lower bound, though the running time there is only polynomial.

**The big picture** In classical statistics, learning a distribution gets easier in proportion to how few outcomes it actually puts weight on. Quantum tomography had no analogous guarantee: existing algorithms pay for the full exponential dimension even when the unknown state lives on only a handful of basis vectors. This work shows the classical intuition does carry over — both in number of copies consumed and in classical/quantum running time — and as a byproduct gives polynomial-time learning for any state that is sparse in a basis you know how to rotate into, including several families studied in quantum chemistry, many-body physics with conserved particle number, and pseudorandom-state cryptography.

**Key contributions**
- $\tilde O(k/\eps)$ copies and $\tilde O(kn/\eps)$ time for $k$-sparse pure-state tomography; single-copy measurements, circuits of size $O(n\log k)$ and depth $O(\log n)$ (CNOTs + Pauli measurement).
- A new near-time-optimal route to general pure-state tomography ($k=2^n$), independent of the recent Frobenius-distance-based approach.
- $\tilde O(kr/\eps)$ samples for $k$-sparse rank-$r$ mixed states, plus an $\Omega(kr/\eps)$ sample / $\Omega(knr/\eps)$ time lower bound.
- Corollaries: improved time for Pauli-sparse unitary channel tomography; near-tightness in $k$ of subset-phase-state pseudorandomness; resolution of an open question on learning sparse phase states.

**How it works** Learn the support by coupon collecting in the computational basis. Then apply an XOR oracle for a random $\mathbb{F}_2$-linear map $f_i(x)=A_ix$ into $\lceil\log 2k\rceil$ bits and measure the hash register; outcomes with exactly two preimages collapse the state to a two-basis-state superposition whose *relative* phase survives. CNOT-ing the differing coordinates onto one qubit reduces relative-phase estimation to single-qubit $X,Y$ expectation values. Each hash induces a random partial matching on the support with edge probability $>1/8k$; a Paley–Zygmund/Chernoff argument (Lemma 4.3) shows $O(\log(k/\delta))$ such matchings give diameter $O(\log k)$, so BFS from a reference vertex reconstructs all phases with only $O(\log k)$ error accumulation. For non-uniform amplitudes, classical bucketing splits the distribution into $L=O(\log(k/\eps))$ near-uniform levels (each a "phase state"), each with its own graph sharing the global reference $r$, and per-level phase accuracy $\xi_j\approx\sqrt{\eps/(L\hat\mu_jD_j^2)}$ weighted by level mass. Mixed states: the purification channel maps $k$-sparse rank-$r$ states to $kr$-sparse pure states.

**Why it matters** It establishes sparsity as the right structural parameter for tomography, alongside rank, and delivers rare *time*-optimal guarantees. Relevant to anyone doing state certification for GHZ/W/Dicke states, sparse state preparation, or PRS security analysis.

**Caveats** The sparse basis must be known and efficiently implementable. Mixed-state time complexity is bottlenecked by the Schur-transform-based purification channel and is likely far from optimal. The algorithm uses two-qubit gates, so whether $\tilde O(kn/\eps)$ is achievable with Pauli-only measurements is open, as is removing the several stacked log factors.

## 4. 2609.12262

[arXiv:2609.12262](https://arxiv.org/abs/2609.12262) · [SciRate](https://scirate.com/arxiv/2609.12262)



**TL;DR** The authors build a hierarchically parallelized version of sparse blossom (the MWPM/embedded-matching decoder behind PyMatching) and prove it returns *exactly* the same correction as the serial algorithm. Under circuit-level local stochastic noise below a finite threshold, the average parallel runtime for an O(d)-round rotated-surface-code window is exp[O(log log d · log log log d)] — quasi-polylogarithmic — implying o(1) decoding time per syndrome round (total latency o(d)), using O(pd³) processors on average.

**The big picture** Matching decoders give the strongest rigorous error-suppression guarantees and are needed for things like post-selection gap metrics in magic-state cultivation, but their runtime grows with code size, threatening both throughput and the feed-forward latency of adaptive logical operations. Because physical errors are sparse and spatially clustered, most of the decoder's work is local and could in principle be done simultaneously — but the matching algorithm's dynamics, with growing, freezing and shrinking regions, blossoms and alternating trees, make it hard to know when distant parts of the problem are truly independent. This work supplies a provable decomposition of the matching computation into a hierarchy of independent local subproblems inferred only from observed detection events, with a guarantee that the parallel answer is identical to the serial one and that the time grows almost not at all with code distance. It suggests classical decoding need not be the scaling bottleneck of fault tolerance.

**Key contributions**
- A parallel sparse-blossom algorithm with a proof of output equivalence to global sparse blossom (hence to MWPM decoding).
- A weighted-graph extension of the Gács-style hierarchical error-clustering framework (previously used for union-find threshold proofs) to blossom dynamics, via "extended SB clusters."
- A *stopping theorem*: every level-k extended SB cluster becomes stable before it can collide with any cluster of equal or higher level.
- A decomposition lemma letting the decoder build the hierarchy from visible detection events only, with edge-based → vertex-based parameter conversion.
- Quasi-polylogarithmic average-runtime bound; numerics showing per-round parallel event counts *decreasing* with d at p = 10⁻⁵.

**How it works** Errors (faulty edges) are recursively grouped into level-k clusters of diameter ≤ d_k^E separated by error-free buffers ≥ b_k^E, with d_k^E, b_k^E = exp[Θ(k log k)]. Cluster-level probability decays doubly exponentially, p_k = O((p/p_th)^{2^{k-1}}), so only k = O(log log d) matters; level-k processing time exp[O(k log k)] gives the stated bound. The decoder instead grows exploring regions of radius b_k^V/2 around residual detection events, accepts components meeting diameter and parity conditions as level-k processing clusters, runs sparse blossom concurrently on them, and inherits stopped matching configurations upward, resuming dynamics only when a higher-level execution "touches" them.

**Why it matters** It closes the gap left by Fowler's informal O(1)-parallel-time claim, providing a correctness-guaranteed algorithmic and complexity foundation for real-time matching decoders in sliding-window and latency-critical (gate-teleportation) settings.

**Caveats** Runtime is measured in an idealized circuit-depth model with no geometric locality, communication, synchronization, memory-access, or scheduling costs, and unbounded (polynomial) processors; numerics report parallel *event counts* as a proxy, not wall-clock time, over only 256 shots per point, d ≤ 49. The asymptotically valid parameter schedule is too conservative to show finite-size benefit, so numerics use a different heuristic schedule. Threshold p_th is not numerically quantified; favorable regime depends strongly on the noise model (advantage clear only at p ≈ 10⁻⁵); results are proven for the rotated surface code only.

## 5. 2609.13087

[arXiv:2609.13087](https://arxiv.org/abs/2609.13087) · [SciRate](https://scirate.com/arxiv/2609.13087)



**TL;DR** This paper builds a compositional theory of detector error models (DEMs) for fault-tolerant circuits: each logical gadget is assigned an "extended DEM" (EDEM), a linear map over $\mathbb{F}_2$ whose extra input/output ports carry *virtual syndrome flips* and *boundary Pauli errors* across code-block boundaries. The central result is that the EDEM of a composite gadget is exactly the contraction of the diagram obtained by wiring per-gadget EDEMs along code blocks, so DEMs for large circuits can be assembled — even symbolically, as polynomials in the component blocks — rather than re-simulated globally.

**The big picture** Decoding a fault-tolerant quantum computation requires a noise model expressed in terms of the parity checks the decoder actually sees, and today this is normally produced by simulating the entire circuit at once, which is expensive and does not reuse work across the repeated logical building blocks that make up a computation. This work gives each logical operation a self-contained, verifiable noise-model "contract" that includes not just its own checks but also how errors and inferred stabilizer signs cross its boundaries, together with a proof that connecting these contracts along the wires of a logical circuit yields exactly the noise model of the whole. Because the pieces compose by simple algebra, one can build noise models for arbitrarily long computations, derive closed-form models for parameterized families by induction, and feed the results directly into windowed decoders.

**Key contributions**
- Channel-level formulation of stabilizer flows as *boundary constraints* on stabilizer channels with declared classical ports, with serial composition rules.
- A "detector cutting" construction that splits detectors spanning several operations into per-gadget virtual detectors, fixing a limitation of the earlier per-operation virtual-syndrome scheme (which requires exactly one output-virtual-syndrome bit per detector, and so misses detectors like $b_j+c_j+d_j$ in the transversal-CNOT example).
- *Raw fault-effect maps*: propagation of faults **and** incoming boundary Pauli errors to outcome flips and outgoing boundary errors, composing by diagram contraction.
- *Code presentations* (possibly overcomplete generators plus syndrome/logical-effect coordinates) and their sections, used to compress boundary-error ports; *gadget detector contracts* generalize the detector basis, with correctness checkable by Clifford simulation plus a rank condition.
- EDEM composition theorem, with structural zero blocks: observable flips and outgoing boundary coordinates never depend on incoming virtual-syndrome flips.
- Symbolic evaluation of contractions (block matrices as polynomials, with zero blocks where no path connects ports) and an application to sliding-window decoding.

**How it works** Faults are pulled back to control ports so the noisy circuit is a single stabilizer channel; Pauli covariance then makes every fault act on the boundary as a Pauli plus outcome bit flips. Virtual unencoder/encoder pairs inserted at gadget boundaries yield circuit-equivalent representations whose syndromes become the composition interface. Per-gadget EDEM blocks ($D,O,V,B$ acting on $f,b_{\rm in},\Delta v_{\rm in}$) are then contracted along code wires.

**Why it matters** Relevant to anyone building decoders or verifying logical gadget libraries: it turns DEM construction into modular, reusable, auditable algebra, supporting per-gadget verification and windowed decoding at scale.

**Caveats** Restricted to stabilizer circuits with stochastic Pauli faults (no leakage/coherent noise); gadgets compose only when code *presentations*, not just codes, match; contracts must be verified by Clifford simulation; fault-effect maps are unique only up to output representative, so only deterministic detector/observable rows are intrinsic; merging mechanisms assumes independence. Quantitative performance data lie in the truncated implementation section.
