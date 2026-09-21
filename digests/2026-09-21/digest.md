# SciRate Daily Digest — 2026-09-21

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Denser Planar Color Codes

[arXiv:2609.21376](https://arxiv.org/abs/2609.21376) · [SciRate](https://scirate.com/arxiv/2609.21376)

*Noah Shutty*

**TL;DR** The 4.8.8 (square–octagon) color code is re-embedded in a "brickwork" layout on a plain square lattice with alternating data/ancilla rails, and a periodic 12-layer superdense syndrome-extraction circuit is constructed that extracts all X and Z checks per reset/measure cycle while preserving full circuit distance at every size tested (planar d = 3, 7, 11, 15; torus d = 4, 8). Counting ancillas, the planar family needs q = (2d²+5d−5)/2 physical qubits per logical qubit — asymptotically q/(kd²) → 1 versus 3/2 for triangular 6.6.6 and 2 for the rotated surface code — and circuit-level SI1000 simulations at p = 10⁻³ and 5×10⁻⁴ show favorable logical-error scaling per physical qubit.

**The big picture** Error-corrected qubits are expensive, and most of the cost is the number of physical qubits needed per protected logical qubit at a given level of protection. Color codes are known to need fewer data qubits than surface codes for the same protection, but that advantage can evaporate once the helper qubits and the noise of the measurement circuits are included. This work shows that, with a carefully chosen layout on ordinary square-grid hardware and a measurement schedule that shares helper qubits between small and large checks while provably not degrading protection, the theoretical density advantage survives realistic circuit noise — roughly halving the qubit count relative to the surface code at matched protection, at plausible superconducting error rates.

**Key contributions**
- Brickwork embedding of 4.8.8 color codes on the square lattice with nearest-neighbor connectivity; ancilla pairs shared between weight-4 and weight-8 faces (rather than one pair per face as in 6.6.6 superdense extraction).
- A 12-CNOT-layer periodic superdense circuit; planar version uses forward/reverse alternating cycles to kill hook-induced distance loss, specified by a local rule with 90 ancilla-environment classes (covers boundaries and small sizes) valid for all d = 4m−1.
- Explicit binary-linear-algebra formalism for superdense Pauli-frame and syndrome bookkeeping (F^X, F^Z, Λ^P, record constraints C), derived via a "reference qubit" Bell-state trick, plus native-CZ transpilation (24 SI1000 moments/cycle, 60m²−20m−5 entangling gates).
- Resource table and a crossover proposition: under ℓ = A(cp)^{d/2}, the family with smaller footprint coefficient Ω always wins for small enough p and small enough target ε, regardless of prefactor or decay constant.
- A negative result: an 8-layer edge-coloring repacking of the 10-layer 6.6.6 torus schedule preserves ideal syndrome extraction but drops d_circ to ≤3 at d = 4.

**How it works** Torus codes come from enumerating finite-index subgroups of admissible translations (admissible parallelograms); planar patches from triangular cuts with one face color omitted per boundary. Circuits are verified by matched upper/lower bounds on d_circ over d rounds in both bases and both starting phases, then simulated in Stim with Tesseract decoding (beam 20, 21 detector orders) under SI1000 noise.

**Why it matters** Directly relevant to superconducting-processor roadmaps: a factor-2 qubit saving versus rotated surface code memories on identical square-lattice connectivity, with color codes' transversal Cliffords and cultivation-friendly structure retained.

**Caveats** Distance preservation is empirical ("appear to preserve"), checked only up to d = 15 planar / d = 8 torus; only d = 4m−1 distances are covered. The 24-moment cycle is 2.4× the surface code's, so the subthreshold decay constant is worse and the advantage rests on extrapolation from the two largest points; no threshold is quoted. Tesseract is near-optimal but slow — no fast/real-time decoder is demonstrated. Only memory is studied; logical gates, lattice surgery, and multi-logical-qubit layouts are left open. Confidence intervals are described as nominal, with some sampling incomplete.

## 2. The Pinnacle Architecture with fixed connectivity of degree eight

[arXiv:2609.21249](https://arxiv.org/abs/2609.21249) · [SciRate](https://scirate.com/arxiv/2609.21249)

*Paul Webster, Tom Peham, Lawrence Z. Cohen*

**TL;DR** The Pinnacle qLDPC architecture is re-engineered so that every qubit's coupler set is fixed at fabrication with maximum degree eight, as required for superconducting hardware, rather than relying on reconfigurable gadget placement. Circuit-level simulations plus sub-threshold extrapolation for a [[510,16,24]] generalised bicycle code give ~1.4×10⁻¹⁸ logical error per logical qubit per logical cycle at p=10⁻³, and the resource estimate yields RSA-2048 factoring in one month with 120,820 physical qubits (vs ~100,000 for the hardware-agnostic baseline).

**The big picture** Low-density parity-check quantum codes promise far fewer physical qubits than surface codes, but the most efficient proposals assume that which qubits talk to which can be changed during the computation — natural for atoms or ions, impossible for superconducting chips where wiring is frozen at fabrication. This work shows that the flexibility can be replaced by two fixed tricks: permanently wiring in one measurement helper per logical generator and toggling only whether each helper is switched on, and rotating the code block's data among its own qubits using couplers that already exist. The upshot is that the architecture's headline advantage — measuring any logical Pauli product in a single logical cycle, avoiding heavy compilation overhead — survives the fixed-wiring constraint with only about a twenty percent qubit penalty and no large slowdown. That makes the case that cryptographically relevant factoring near a hundred thousand superconducting qubits is not an artefact of idealised hardware assumptions.

**Key contributions**
- "Frozen Pinnacle": processing blocks with k/2 fixed-position Z-gadgets (a generating set) plus one X-gadget for the seed operator; arbitrary logical Pauli measurement via one code-block cyclic-shift automorphism (≤4 primitive shifts, costing 4 extra code cycles, d_t: 26→30) plus gadget activation.
- Memory via a single "port block" plus inter-block cyclic shifts (degree 7/8), with an alternative all-port variant at +30% qubits but degree 7 and only 130 added connections per block; plus reuse of the second logical sector of processing blocks as memory sectors (dual basis, fan-out by ZZ measurements).
- A degree-eight magic engine: 8T-to-CCZ distillation on a GB block with 4 Z- and 3 X-gadgets over a 5-cycle period, output infidelity ≈28p_in²=2×10⁻¹⁰, 1% reject rate, fed by twelve d=15 cultivation patches (7855 qubits total).
- Simulations at d=4,6,10 of shift-automorphism and bridged-measurement circuits, fitted to A(10⁻³/B)^{d/2} and extrapolated.

**Why it matters** It directly contests the view that fixed connectivity forces the large time overhead of restricted-instruction-set qLDPC architectures (e.g. the degree-7 bicycle/extractor architecture), and gives a concrete superconducting-relevant target for cryptanalytic resource estimates.

**Caveats** The error rate is extrapolated from d≤10 to d=24 (an order of magnitude in distance and ~16 in exponent; CI spans an order of magnitude), and shift and bridged-measurement contributions are simulated separately then summed rather than as an integrated architecture-level circuit including memory access and magic engine. Degree eight bounds coupler count but not coupler length or layout crossings, which is the real superconducting fabrication bottleneck; the inter-block memory shift construction adds 1020 connections per block. Decoder latency for the assumed 10 µs reaction time and throughput for large qLDPC blocks are not analysed, and cultivation packing/latency is handled by a conservative but coarse argument.

## 3. Weighted Quantum Signal Processing: Low-Depth Polynomial Approximation with Applications to Kolmogorov-Arnold Networks

[arXiv:2609.21567](https://arxiv.org/abs/2609.21567) · [SciRate](https://scirate.com/arxiv/2609.21567)

*Rohit Sarma Sarkar, Rupayan Bhattacharjee, Elias F. Combarro, Michele Grossi, Lirandë Pira, Carmen G. Almudéver, Sergi Abadal, Eduard Alarcon*

**TL;DR** The paper generalizes Quantum Signal Processing by raising the signal operator to integer (or real) powers, $U(x)^{w_j}$, between the $R_z$ phase rotations. The resulting "Weighted QSP" produces a Chebyshev expansion supported exactly on the *reach* of the weight vector — the set of absolute values of all signed sums $|\sum_j \pm w_j|$ — with coefficients given in closed form as $\mathbf{c} = B\,N_k\exp(iM_k\boldsymbol{\Phi})$, where $N_k$ is a permuted Hadamard matrix. Since $k$ weights can sum to degree $d$ while covering up to $2^{k-1}$ distinct Chebyshev orders, sparse-in-Chebyshev polynomials can be realized with exponentially fewer phase parameters than standard QSP's $d+1$.

**The big picture** Quantum signal processing is the workhorse primitive behind Hamiltonian simulation, matrix inversion, and singular value transformation, but realizing a polynomial of a given degree normally costs a number of tunable rotation angles that grows linearly with that degree, and finding those angles is numerically delicate. This work shows that the standard construction is carrying substantial redundancy: by letting each layer apply a repeated rather than single rotation, and by treating the repetition counts as a design choice, one can hit the same target functions with far fewer angles and a cleaner algebraic structure. Because the coefficient map becomes an explicit Hadamard-like linear system, angle recovery turns into solving a linear system rather than a bespoke nonlinear factorization. The authors then use these compact circuits as the learnable univariate edge functions in Kolmogorov–Arnold networks, giving a parameter-efficient hybrid architecture that avoids the block-encoding overhead of prior quantum KAN proposals.

**Key contributions**
- Exact characterization of the function class generated by weighted QSP: $P=\sum_{r\in\mathcal{R}_\mathbf{w}} c_r T_r$, $Q=i\sqrt{1-x^2}\sum d_r S_{r-1}$, with $\mathcal{R}_\mathbf{w}$ the reach and coefficients given by $B_{M_k\mathbf{w}}N_k\exp_{(iM_k\boldsymbol{\Phi})}$ (Thm. 3.4); standard QSP is the $\mathbf{w}=\mathbf{1}$ corollary, where $M_k\mathbf{1}$ has heavy multiplicity — the concrete source of redundancy.
- Explicit combinatorics for the aggregation matrix $B$ (full row rank, singular values equal to class sizes, min singular value 1) and the permutation $\tilde P$ relating $N_k$ to $H^{\otimes k-1}$.
- Observation that $\phi_0$ is always redundant for $d>0$, reducing QSP itself to $d$ parameters.
- A phase-fitting algorithm: choose a partition $\mathbf{w}$ of $d$ whose reach covers the nonzero Chebyshev support, then solve a linear system in $\exp(i\phi_j)$; plus a variational/learning formulation for continuous functions and error bounds for generic (non-integer) weights.
- WQSP-KAN: WQSP polynomials as learnable edge activations for multivariate approximation.

**Why it matters** Anyone implementing QSP/QSVT angle synthesis, or building variational models with provable polynomial expressivity, gets a structurally transparent parameterization and a principled knob trading classical weight design against circuit parameters. The $R_x/R_z$ gate set is also more hardware-native than GQSP's general $\mathrm{SU}(2)$ rotations.

**Caveats** The framework as stated lives in the classical-input regime: $U(x)^{w}$ collapses to a single $R_x(w\theta)$ only because $x$ is a classical scalar, so *query* depth to a block-encoded oracle is not reduced, and the extension to weighted oracle access inside QSVT is explicitly left open. Parity constraints remain (two circuits for general functions). Savings are contingent on the target being sparse in the Chebyshev basis with support matching an achievable reach; when no exact partition exists one falls back to a superset and an approximation error. With $k$ phases but up to $2^{k-1}$ coefficients, the realizable coefficient vectors form a low-dimensional manifold — "preserving expressive power" holds for favorable targets, not universally. The truncated source prevents assessment of the numerical KAN benchmarks.

## 4. Nonlocal Magic Spreading in Many-body Quantum Dynamics: From Chaotic Evolution to Quasi-particle Picture in Integrable Models

[arXiv:2609.20951](https://arxiv.org/abs/2609.20951) · [SciRate](https://scirate.com/arxiv/2609.20951)

*Sreemayee Aditya, Piotr Sierant, Xhek Turkeshi*

**TL;DR** The authors show that nonlocal magic — the magic that cannot be removed by local basis changes, quantified by the recently-solved stabilizer-fidelity measure $D_{\rm NL}$ — is controlled almost entirely by the capacity of entanglement $C$ (the variance of the entanglement Hamiltonian), with $D_{\rm NL}\simeq\frac12\log_2(\pi\ln^2\!2\,C/8)$ for broad spectra and $D_{\rm NL}\simeq(\ln 2/4)C$ for near-flat ones. This reduces a hard optimization over the full Schmidt spectrum to two cumulants, yielding a quasiparticle theory for integrable quenches and the result that chaotic dynamics produces nonlocal magic only transiently while free-fermion dynamics retains $D_{\rm NL}(\infty)\propto\log_2 L_A$.

**The big picture** Two resources make quantum many-body states hard to simulate classically: entanglement and non-stabilizerness. Their irreducible overlap — the non-stabilizerness that no local change of basis can erase — is the part that really certifies quantum complexity across a cut, but it has been almost impossible to compute or predict in dynamical settings. Here it is tied to a simple, tractable quantity measuring how much the entanglement spectrum fluctuates, which makes its spreading after a quench analytically predictable. The surprising payoff is operational: the most strongly scrambling dynamics destroys this resource at late times by flattening the entanglement spectrum, while free-fermion evolution — classically simulable — sustains it, and with it the ability to act as a universal catalyst for entanglement.

**Key contributions**
- A "peak-height law" $D_{\rm NL}\simeq-\log_2(4P_{\max}/\ln 2)$ for spectra smooth on the scale of one bit, plus Gaussian closure $D_G(S,C)$ interpolating the two asymptotic branches; error $O(1/C)$, with the $5/(2\ln^3\!2\,C)$ correction computed.
- Rigorous two-sided concentration bounds $a/8\le\max_k F_{2^k}\le 8a$, giving $D_{\rm NL}\le\frac12\log_2(1+C)+5.74$ unconditionally, and for fermionic Gaussian states $\frac12\log_2(1+M_F)-\alpha_0\le D_{\rm NL}\le M_F$ via Kolmogorov–Rogozin.
- Quasiparticle formula: $S_{\rm QP},C_{\rm QP}$ from $w_k(t)=\min(L_A,2|v_k|t)$, giving $D_{\rm NL}(\infty)=\frac12\log_2 L_A+\frac12\log_2(\pi\ln^2\!2\,\bar c/8)$.
- TBA extension to interacting integrables: $\bar c$ as a dressed charge susceptibility with weight $\vartheta_n(1-\vartheta_n)[w_n^{\rm dr}]^2$.
- Link to embezzlement: strong scramblers embezzle only transiently.

**How it works** Exact statevector evolution ($L=20$, $\ge2000$ realizations) for Haar brickwall circuits, kicked Ising and MFIM; covariance-matrix methods for XX/TFI dimer quenches ($L=4096$, $L_A\le512$) and random matchgate circuits ($L=256$). Chaotic: $C\propto t^{0.63}$ (circuit) or $t^{1.01}$ (MFIM), peak at $\tau_M\propto L_A$, then exponential (circuit) or algebraic $t^{-0.42}$ (MFIM, energy conservation) relaxation to $D_0\simeq0.244$ at the balanced cut; ETH gives $D_{\rm NL}(\infty)\simeq\beta^2V_A/(4\ln 2)$ for small blocks. Matchgates saturate diffusively at $\tau_M\propto L_A^2$ with Page curve peak $\frac12\log_2 L$.

**Why it matters** Provides the first predictive, analytically controlled theory of nonlocal-magic dynamics, connects it to a quantity already measurable in experiment and computable in tensor networks/TBA, and decouples catalytic (embezzling) power from scrambling strength.

**Caveats** The MFIM peak height grows faster than $\log_2 L_A$ over accessible sizes and $D_G$ there is only an upper envelope with no systematic convergence — attributed to preasymptotics but unverified. The TBA prediction is untested numerically. The Gaussian closure fails at hard-edged spectra (balanced-cut Haar: $0.195$ vs exact $0.244$). Large capacity does not imply large $D_{\rm NL}$ in general (spike-plus-tail counterexample), and a prime-occupation construction shows $D_{\rm NL}=M_F/4+O(1)$, so the logarithmic law is not universal. Chaotic results rest on $L\le20$.

## 5. Ensemble Dependence of the Critical Exponent at a Quantum Error Correction Threshold

[arXiv:2609.21886](https://arxiv.org/abs/2609.21886) · [SciRate](https://scirate.com/arxiv/2609.21886)

*Idan Dror, Moshe Goldstein*

**TL;DR** In a solvable toy model of quantum error correction (Haar-random encoding, single-site error channel, inverse decoding), the finite-size scaling exponent of the fidelity and of the stabilizer Rényi entropy at the error-correction threshold depends on how the random errors are drawn: ν=1 when the number of each error type is fixed ("canonical"), ν=2 when each site independently samples an error ("grand-canonical") with a quenched average. Both values exactly saturate information-theoretic lower bounds, which the authors extend from the grand-canonical to the canonical case and to a one-parameter family of interpolating ensembles; for some channel decompositions the transition disappears altogether.

**The big picture** Physicists routinely assume that how you bookkeep randomness — fixing a quantity versus letting it fluctuate — cannot change universal properties of a phase transition once the system is large. This work exhibits a clean, analytically tractable counterexample at the error-correction threshold of a random-encoding quantum code: the rate at which the transition sharpens with system size, and even whether a transition exists at all, hinges on the statistical ensemble used to model errors and on whether one averages the success probability itself or averages the underlying process first. Because the same physical noise process can be decomposed into classical randomness in many inequivalent ways, this is a practical warning for anyone extracting thresholds and scaling collapses from simulated or experimental noisy circuits.

**Key contributions**
- Closed-form annealed fidelity for an arbitrary global channel: F̃ = (D−1)(DR+1)/[DR(D−K)+KD−1], controlled by a single channel invariant R = D⁻²Σ⟨i|ℰ(|i⟩⟨j|)|j⟩, which is basis/Kraus independent, bounded in [0,1], linear in convex mixtures, and multiplicative under tensor products.
- Natural error strength E = −log_D R with threshold at the redundancy rate E_c = 1−r (a Singleton-bound analogue); scaling form F ≈ [1+d^{N^{1/ν}(Ē−E_c)}]⁻¹.
- Demonstration that error-annealed averages (F₁, F̃₁) are exactly equivalent to a single deterministic mixture channel with parameter Ẽ = E(Σp_αℰ_α) ≠ Ē, giving ν=1 but a *different* critical point; error-quenched grand-canonical averaging gives an erf scaling function with ν=2 via CLT/saddle-point over multinomial error counts.
- Extension of the Feldman et al. information bound: ν≥2 (grand-canonical, essentially 1D Harris), ν≥1 (canonical), and ν ≥ 2/(2−min(a,1)) for ensembles sampling without replacement from a reservoir with N_hidden ~ N^a. All bounds are saturated here.
- Same exponent switch for magic (stabilizer Rényi entropy), since M̃_q ∝ −log₂F̃.
- Explicit example: decomposing the depolarizing channel into unitary trajectories e^{±iφσ_i/2}; φ=π gives Ē=∞, pushing λ_c to zero and destroying the transition, despite identical mixture channel.

**How it works** Second-moment (replica-2) Haar averaging reduces the circuit to Weingarten sums over S₂, collapsing everything onto R. Permutation symmetry of Haar encoding makes the fidelity a function only of error *counts*, so canonical randomness is inert; grand-canonical count fluctuations of order √N smear the step function over δ ~ N^{−1/2}. Numerics use brick-wall 2N-layer random two-qubit encodings, z-only depolarizing noise, r=1/2, φ=π/2, N up to 20, confirming self-averaging over U and the predicted collapses.

**Why it matters** Relevant to measurement/error-induced transition studies, magic transitions, and threshold estimation: reported exponents may encode modeling choices about noise randomness rather than intrinsic universality. The R-invariant formalism is also a compact, reusable tool.

**Caveats** The model is single-shot with no actual recovery operation; fidelity post-selected on the zero-syndrome sector is only a proxy for decoding success. Analytics are for the encoding-annealed average (quenched agreement argued and checked numerically only at N ≤ 20; canonical data show strong discreteness "staircase"). The ν≥1 bound rests on a heuristic integer-resolution argument (δ ~ M⁻¹), and conditions for bound saturation are left open. One could argue the "ensembles" here are genuinely different quenched noise models rather than thermodynamically equivalent ones — the critical point itself also shifts between averaging schemes.
