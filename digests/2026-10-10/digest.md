# SciRate Daily Digest — 2026-10-10

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Entanglement entropy and magic of ZX-diagrams

[arXiv:2610.12447](https://arxiv.org/abs/2610.12447) · [SciRate](https://scirate.com/arxiv/2610.12447)

*Marcin Szyniszewski, Razin A. Shaikh, Aleks Kissinger*

**TL;DR** — Using flow conditions, any state-preparation ZX-diagram can be put in polynomial time into a normal form consisting of a graph state dressed by Pauli exponentials, and from this structure one reads off two-sided additive bounds on bipartite entanglement entropy (graph-state cut rank ± sum of binary entropies of the gadget angles) and an additive upper bound on logarithmic stabilizer extent. Both bounds are computed without ever contracting the diagram, are exact in the Clifford limit, and scale as angle-squared-times-log for small rotations, far tighter than generic entangling-capacity bounds. Numerics on 20–26 qubit random, monitored, and Trotterized circuits show the entanglement bounds track exact entropy long after generic bounds saturate the trivial interval.

**The big picture** — Two distinct resources make quantum states hard to simulate: how entangled they are, and how far they are from the easy-to-simulate stabilizer family. Both are normally expensive to compute, requiring something like full contraction of the state. This work shows that for circuits written in the ZX graphical calculus, a structural rewriting step cleanly separates the "free" stabilizer backbone — whose entanglement is a purely graph-theoretic quantity — from a list of non-stabilizer rotations, each of which can contribute only a bounded, angle-dependent amount to either resource. The result is a cheap, purely diagrammatic thermometer for entanglement and magic that stays informative even for volume-law states, where tensor-network methods become hopeless.

**Key contributions**
- Flow-based polynomial extraction of a graph-state-plus-Pauli-gadget normal form as a resource-estimation primitive.
- Two-sided additive entanglement bounds: upper via dephasing into branch sectors plus mixture-entropy inequality; lower via a Maassen–Uffink uncertainty relation exploiting the flat Schmidt spectrum of graph states (every stabilizer-orbit state has product overlap at most 2^(−S₀/2)).
- Rényi generalization with conjugate indices (asymmetric bounds, symmetric only at von Neumann).
- Identification of the exact failure condition — "coherent branch interference," when a product of gadget Paulis equals a stabilizer of the backbone up to phase — plus a four-step preprocessing (commuting-region fusion, stabilizer-equivalent fusion, Clifford-residue unfusing, one-sided gadget removal).
- Additive upper bound on log stabilizer extent via per-gadget decomposition into two stabilizer branches with cost factor max + (√2−1)min.

**How it works** — Each gadget splits into sine/cosine branches; since Paulis preserve the flat graph-state spectrum, the entropy is controlled by the Shannon entropy of the branch weights, giving the binary-entropy terms, summed only over gadgets crossing the cut. Implementation uses PyZX plus PauliOpt; exact magic benchmarks come from existing stabilizer-extent solvers at L=8.

**Why it matters** — Gives resource-aware cost functions for ZX-based compilation, and a scalable probe for measurement-induced entanglement/magic transitions where volume-law states block tensor networks.

**Caveats** — Entanglement bounds are not certified: preprocessing only removes pairwise/low-weight interference, so sufficiently deep structured circuits violate them (first violation at step 64 in the Trotter circuit, matching the Clifford periodicity). Magic benchmarks are only L=8 and the bound nearly saturates there partly because circuits are random; the generic single-gadget bound's ancilla-independence at finite angle rests on numerical evidence. Restricted to pure states and diagrams possessing flow.

## 2. Measure Now, Mitigate Later: Virtual Error Cancellation for Logical Quantum Circuits

[arXiv:2610.12400](https://arxiv.org/abs/2610.12400) · [SciRate](https://scirate.com/arxiv/2610.12400)

*Oles Shtanko, Saswata Roy, Shashwat Kumar, Zlatko Minev*

**TL;DR** The paper shows that the syndrome record already measured during a fault-tolerant run is sufficient to cancel residual logical error *in classical post-processing*, with no noise learning, no modified circuits, and no extra executions. Shots are partitioned into syndrome sectors (most practically: sectors where a fast real-time decoder and a slow, more accurate offline decoder agree or disagree in which logical Pauli they apply), and each sector is given a quasi-probability weight — positive and >1 on the consensus sector, negative on contested sectors — yielding an unbiased estimator with sampling overhead 1 + O(p_L), versus postselection's residual bias floor and exponential rejection. A d=7 rotated surface code simulation shows >3 orders of magnitude error suppression relative to the decoded logical error rate.

**The big picture** Even below threshold, error-corrected quantum computers leave a small residual bias in expectation values, and the usual fixes — learning the noise, running modified circuits, or throwing away suspicious shots — are expensive or incomplete. This work points out that the error-correction syndrome data that is already recorded for free carries enough information to tell which shots were likely corrupted and in which logical direction, so the bias can be removed afterwards in software by reweighting shots, including with negative weights. Because the heralding can be sharpened simply by re-decoding the same data offline with a better, slower decoder, the scheme costs essentially nothing beyond classical compute and a modest increase in shot count. This makes residual-error removal a post-hoc data-analysis step rather than an experimental protocol.

**Key contributions**
- Virtual error cancellation: quasi-probability mitigation implemented purely on syndrome-conditioned classical weights, applicable to universal (not Clifford-restricted) logical circuits.
- A variational theory (matrix Cauchy–Schwarz / KKT with Schur complements) giving optimal weights and the minimum sampling overhead C_S* = Σπ_k w_k², with closed forms w_0 = (1+1ᵀV⁻¹p_0)/π_0, w_k = −(V⁻¹p_0)_k/π_k for the minimal K = M+1 sector partition.
- Proof that the sector-centroid displacement matrix V is strictly diagonally dominant (Lévy–Desplanques margin ≥ p_{c,X}p_{c,Z}, ≥ 1/4 at the MWPM tie-break baseline), hence invertible with κ(V) = O(1) for all classifier confidences and cross-basis correlations ρ.
- Universal overhead law C_S* = 1 + (V⁻¹p̄_L)ᵀdiag(π)⁻¹(V⁻¹p̄_L) + O(p_L²) = 1 + O(p_L), with dual-decoder slope η^dd = (1+r)/(1−α) ∈ [1,2] set by the decoder error-asymmetry ratio r = (p′_L−p_I)/(p_L−p_I).
- Calibration robustness: residual bias ‖p_res‖ = O(α ε_max ‖p̄‖), i.e., suppressed by the consensus factor α relative to physical PEC, plus exact invariance under uniform/common-mode miscalibration.

**How it works** Decoder disagreement up to logical Pauli Q partitions syndrome space into 4ⁿ sectors; the consensus sector carries weight 1−O(p_L) and suppressed error αp̄, while contested sectors have O(1) conditional failure probability. Solving the trace-preservation and channel-nulling constraints gives a signed filter w(s) applied shot-by-shot to measurement outcomes. Sector probabilities can be taken directly from empirical frequencies of the evaluation stream, making the estimator exactly trace-preserving.

**Why it matters** It reframes syndrome data as a mitigation resource, offering near-unit overhead where postselection pays exponential rejection and still leaves bias — directly relevant to early fault-tolerant demonstrations where a d≈7 memory has nonzero logical error.

**Caveats** The minimal partition needs 4ⁿ sectors for n logical qubits, so direct multi-qubit resolution scales badly; results rest on hypotheses H1–H3 (conditioning of V, per-channel sampling adequacy, dominant consensus sector) and on Pauli logical noise; the leading-order V model assumes a specific CSS/correlation parameterization; and conditional centroids p_k must still be estimated, with error entering as ε_max.

## 3. Energy-constrained two-way capacities of the pure-loss channel

[arXiv:2610.12365](https://arxiv.org/abs/2610.12365) · [SciRate](https://scirate.com/arxiv/2610.12365)

*Alessandro Falco, Francesco Anna Mele, Ludovico Lami, Vittorio Giovannetti*

**TL;DR** The paper proves that for the single-mode pure-loss channel with transmissivity η and an average input photon budget N, the two-way-assisted quantum capacity and secret-key capacity both equal exactly g(N) − g((1−η)N), the reverse coherent information of a two-mode squeezed vacuum. The converse comes from an amortized bound on the *regularized* relative entropy of entanglement, whose sub-linear correction terms vanish under regularization, closing the last open capacity formula for pure loss.

**The big picture** For an optical fibre that simply loses photons, we have long known how many classical bits it can carry, how much quantum information it can carry without feedback, and — when the sender may use arbitrarily bright light — how many entangled bits or secret key bits per use two cooperating parties can generate with unlimited classical back-and-forth. What was missing was the last of these when the transmitter's average optical power is capped, which is the physically realistic case; only an achievable rate and looser upper bounds were known. This work shows the simple known protocol (squeezed light plus reverse reconciliation) is exactly optimal among all adaptive strategies obeying the power budget, so no cleverer scheme can do better. That settles the ultimate repeaterless rate-versus-power tradeoff for lossy optical links.

**Key contributions**
- Exact formula Q₂ = K = g(N) − g((1−η)N) under an average photon-number constraint, with a finite-blocklength weak converse (1−ε)log d ≤ n f_η(N) + h₂(ε).
- An amortized, energy-dependent bound on the regularized relative entropy of entanglement for the loss channel: E_R^∞ increases by at most f_η(ν) per use, regardless of memories.
- A privacy-test argument that survives regularization, lower-bounding E_R^∞ (not just E_R) by the approximate key length, uniformly in shield dimension.
- An explicit separable comparison state for the Choi state of loss restricted to a fixed-total-photon-number sector.

**How it works** Loss restricted to the m-mode k-photon sector Sym^k(C^m) is covariant under U(m) with an irreducible input action, so it is LOCC-simulable by its Choi state. Using the condensate states |u;k⟩ — which split cleanly across the beamsplitter — the authors build a separable state σ_{k,j} satisfying σ P = P/d_k on the flat Choi support, yielding E_R(Ω_{m,k}) ≤ log d_k − E_J[log d_J]. Phase covariance lets one dephase total photon number at cost H(K) (non-lockability lemma), and rewriting the resulting bound via auxiliary thermal-like states ζ, ζ′ plus data processing under thinning (L_q(τ_x)=τ_{qx}) gives an increase ≤ m f_η(ν) + g(q m ν). Grouping r i.i.d. copies and regularizing kills the logarithmic g term, giving the tight per-use constant; telescoping over adaptive rounds plus concavity/monotonicity of f_η and Jensen imposes the budget. The key-to-entanglement step uses Uhlmann on diagonal key blocks, and a multi-copy privacy test bounded via a moment-generating-function/variational inequality.

**Why it matters** This completes the pure-loss capacity picture alongside C, C_E, Q, P, and gives the benchmark that any repeater or finite-energy QKD scheme must beat; at η = 1/2, N = 1 the rate is ≈0.6226, positive where unassisted Q and P vanish. The sector-simulation plus regularized-privacy-test toolkit should transfer to other phase-covariant bosonic channels.

**Caveats** Pure loss only — thermal noise is not covered. The constraint is on unconditional per-use mean photon number averaged over the block; it is a weak converse (ε→0), not strong. Concurrent independent work reports the same result.

## 4. High-Rate Concatenated Quantum Error-Correcting Codes for Qudits

[arXiv:2610.11225](https://arxiv.org/abs/2610.11225) · [SciRate](https://scirate.com/arxiv/2610.11225)

*Takanori Nishi, Hayato Goto*

**TL;DR** The many-hypercube (MHC) concatenated code family is generalized from qubits to prime-dimension qudits, yielding [[6^L, 4^L, 2^L]]_q codes with explicit stabilizers, encoders, transversal SUM, and a (non-transversal but local) logical Fourier gate. Under code-capacity X-noise with a qudit level-by-level minimum-distance (LLMD) decoder, the threshold rises monotonically from 5.1% at q=2 to 10.0% at q=13, and a "waterfall" regime appears for q≥5 with fitted error exponents exceeding the distance bound (up to 5.73 vs. the expected 4).

**The big picture** Error-correcting codes for quantum computers are usually designed for two-level systems, but many hardware platforms can natively control systems with many more levels, and recent trapped-ion experiments have demonstrated coherent control of thirteen-level and even twenty-five-level units. This work takes a family of codes known for packing an unusually large amount of logical information into few physical carriers and rebuilds it for these higher-dimensional systems. The result is that noise tolerance roughly doubles as the number of levels grows, because each syndrome measurement reveals far more about which error occurred. This suggests that pairing high-rate code architectures with richer hardware could meaningfully cut the overhead of fault-tolerant quantum computing.

**Key contributions**
- Qudit [[6,4,2]]_q base code with explicit stabilizers (Z^⊗6 and alternating X/X†), logical Paulis, zero-state and arbitrary-state encoders, and error-correcting teleportation circuits.
- Transversal logical SUM gate; logical Fourier implemented as physical F^{(−1)^i} plus a fixed SWAP pattern, generalized recursively to level L.
- Qudit generalizations of both the hard-decision (Knill-style) and LLMD decoders, including candidate-pruning heuristics (caps of 10^5 level-2 combinations, M≤6 level-1 candidates) to keep cost tractable.
- Numerics up to q=13 using the Sdim qudit stabilizer tableau simulator, with up to 1.5×10^9 shots.
- Entropy-based explanation of the q-advantage and of the opposite q-ordering in waterfall vs. error-floor regimes.

**How it works** Concatenating the [[6,4,2]]_q error-detecting code gives rate (2/3)^L with distance 2^L. LLMD decoding keeps, at each level, all codewords at minimum Hamming distance from the measured string; a level-1 block with nonzero syndrome s yields six distance-1 candidates x − s·e_i. Candidates propagate upward with the sixth block fixed by the stabilizer sum constraint, its distance re-evaluated against the q computational-basis strings in its logical class. Noise is the symmetric q-ary X channel. Plotting logical error vs. q-ary entropy H_q collapses level-2 curves onto one line; the residual level-3 spread is attributed to the ratio of typical error weight nε to d/2, which grows with q at fixed H_q — penalizing large q in the waterfall regime while the richer syndrome alphabet helps in the error floor.

**Why it matters** It shows the qudit threshold enhancement previously seen in topological codes carries over to a structurally very different high-rate concatenated family, and gives a concrete architecture for qudit FTQC with 2/3-per-level encoding rate. The waterfall observation, previously tied to neural decoders on qLDPC codes, appears here with a simple recursive decoder.

**Caveats** Code capacity only — no circuit-level or measurement noise, and the X-only channel is symmetric, so Hamming distance is optimal by construction; realistic amplitude damping would require different metrics. Restricted to prime q (not Galois q=p^r). Thresholds are read off level-2/level-3 crossings with only two levels available, so finite-size effects are untested. The HD decoder shows essentially no q-dependence (threshold ~1.1–1.4%), so the advantage is decoder-specific. Candidate pruning makes LLMD suboptimal in a way that may itself be q-dependent, and level-3 error-floor exponents have not converged for q≥5.

## 5. Markov length can diverge in systems whose universal physics is spatially Markovian

[arXiv:2610.11235](https://arxiv.org/abs/2610.11235) · [SciRate](https://scirate.com/arxiv/2610.11235)

*Yu-Hsueh Chen, Tarun Grover*

**TL;DR** The authors show that conditional mutual information (CMI) is not an RG-universal quantity: an *irrelevant*, detailed-balance-breaking perturbation of a critical classical Gibbs state — which has strictly zero CMI beyond its interaction range — generically generates algebraically decaying CMI and hence an infinite Markov length, even though the perturbation does not change the fixed point. These power-law tails are "cutoff-suppressed": their amplitude scales as a positive power of the lattice spacing and vanishes in the continuum limit, distinguishing them from genuine, continuum-surviving power-law CMI (e.g. at the long-range Ising critical point).

**The big picture** Recent proposals define phases of mixed states by whether two states can be connected by short, locally reversible noisy evolutions, and the key diagnostic is whether conditional correlations across a buffer region decay exponentially or as a power law. This paper shows that this diagnostic is more fragile than the usual notion of universality: two systems that flow to the same long-distance fixed point, and therefore share all ordinary critical exponents, can nonetheless differ qualitatively in their conditional correlations, with one of them acquiring an infinite "Markov length" from a perturbation that is irrelevant in the usual sense. The resulting tails are an artifact of the microscopic cutoff in the sense that they vanish when the lattice is taken to zero — yet at any fixed lattice they still obstruct local reversibility. This exposes a real tension between renormalization-group universality and channel-based definitions of mixed-state phases, and suggests the latter may need to admit channels with weak, cutoff-suppressed algebraic tails or sublinear range.

**Key contributions**
- A 1D theorem: for translation-invariant states, CMI ≈ (l/l_B)² g(l_B/a); CMI decays faster than l_B⁻² iff CMI vanishes as a→0 (Markovian long-distance physics). Exponent η<2 implies UV-divergent CMI (illustrated by the colored Motzkin chain, η=3/2).
- A closed second-order formula for CMI of perturbed Langevin steady states: I = (ε²/2)∫dt dt′ ⟨(e^{tL⁰}Σ)_×(e^{t′L⁰}Σ)_×⟩₀, combining the quadratic expansion around a Markov distribution with the McLennan–Zubarev steady state.
- Scaling form CMI ~ (ξ_cross/l_B)^{2|ω|}(l/l_B)^{d+h_loc}, with two other regimes governed by the nonlocal kernel dimension h_nloc, derived from a Gaussian trace-log CMI.
- A sufficient condition for exponential CMI: rapid mixing plus locality give I ≲ ε²e^{−2κl_B}, κ=μγ/(v+γ); conserved (diffusive) dynamics violate it.
- A solvable two-component anisotropic Toom-like model with exact steady-state kernel, numerically confirming CMI ~ ε²l_B⁻⁶ on 128×128.
- Prediction: Toom's cellular automaton at its Ising-symmetric critical point has cutoff-suppressed power-law CMI with universal exponent set by ω ≈ −1.3 ± 0.2.
- Long-range Ising: high-T phase gives η = 2(1+σ) (cutoff-suppressed); the 1D Gaussian critical point gives CMI = σ²(l/l_B)²/8 (genuine).

**Why it matters** Anyone building a classification of mixed-state/nonequilibrium phases via Markov length, or interpreting CMI numerics in decohered/driven systems, needs this distinction; it reframes the cutoff as a "dangerously irrelevant" parameter for conditional correlations.

**Caveats** The main perturbative result is O(ε²) (though the argument is claimed to persist at higher order); UV-finiteness of CMI is assumed throughout; the Toom prediction rests on a mapping to Model A plus literature estimates of ω and is untested numerically; the explicit nonperturbative verification is Gaussian and classical, with the single-site region A (l=1) on a finite torus requiring an infinitesimal-mass regularization.
