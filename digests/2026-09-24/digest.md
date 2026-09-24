# SciRate Daily Digest — 2026-09-24

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Emergent Prethermal Symmetries for Scalable Hamiltonian Learning

[arXiv:2609.27181](https://arxiv.org/abs/2609.27181) · [SciRate](https://scirate.com/arxiv/2609.27181)

*Myeongjin Shin, Junseo Lee, Iman Marvian, Yu Tong*

**TL;DR** The authors give a Hamiltonian-learning protocol for geometrically local qubit lattices that reaches the Heisenberg limit — total evolution time $\mathcal{O}(\log^d(1/\varepsilon)\log^2(n/\delta)/\varepsilon)$ for $\ell^\infty$ accuracy $\varepsilon$ — using only *static* single-qubit fields, product states, single-qubit measurements, and non-adaptive experiments. The required field strength is independent of system size and only polylogarithmic in $1/\varepsilon$, replacing the $\mathcal{O}(1/\sqrt{\varepsilon})$ pulse-rate requirement of Hamiltonian reshaping. The mechanism is an emergent prethermal symmetry (dressed charge of the applied field) that suppresses thermalization for the full $\mathcal{O}(1/\varepsilon)$ experiment.

**The big picture** Learning a many-body Hamiltonian at the best possible precision-per-unit-time requires stopping the system from scrambling the local information you are trying to read out, which usually means either trusted entangling operations or ever-faster control pulses — exactly the resources you lack when the machine is not yet calibrated. This work shows that simply switching on strong-but-modest static local fields is enough: the fields create approximate conservation laws that delay thermalization for exponentially long times while leaving informative coherent oscillations intact. The strength needed does not grow with the number of qubits, so the method scales to large lattices with only local state preparation and readout. This turns a demanding control problem into a collection of parallel, Ramsey-style local spectroscopy experiments.

**Key contributions**
- Heisenberg-limited learning with only static single-qubit control whose strength is $\tilde{O}(1)$ in $1/\varepsilon$ and $n$-independent; extends a prior fixed-size ($n=O(1)$) result to scalable many-body systems.
- A uniform analytic continuation of the Abanin–De Roeck–Ho–Huveneers (ADHH) prethermal recursion to *non-Hermitian* interactions, plus Cauchy estimates controlling Taylor truncations (locality, derivatives).
- A locality reduction: full-lattice transition energies agree with radius-$R$ patch predictions to $O(J2^{-K})$ when $R\ge(K+1)r_0$, via connected $p$-word expansions.
- A Walsh–Hadamard randomization argument showing the strong-field Jacobian Gram matrix concentrates to a diagonal $\mathrm{diag}(p_a 3^{-p_a})$, giving well-conditioned inversion with $m=\Theta(\log(n/\delta))$ patterns per site.
- Parallelization via lattice coloring with separation $\Theta(\log(1/\varepsilon))$, giving $O(\log^d(1/\varepsilon))$ batches and removing the linear-in-$n$ factor.

**How it works** A "defect" site gets half-strength field, its radius-$R$ ball full strength, zero outside. The charge $N=Q_k+2\sum_j Q_j$ becomes an approximately conserved dressed symmetry; $s\le n_*(\nu)=\Theta((\nu/J)/[1+\log(\nu/J)]^3)$ ADHH steps yield an effective Hamiltonian commuting with $N$ up to remainder $CJ|B|(2/3)^s$. The two product states differing by a defect flip are eigenstates, so a Ramsey signal oscillates at $\nu+2E_\rho^\Lambda$; robust phase estimation extracts $E_\rho^\Lambda$. Coefficients are recovered by least-squares against the patch forward map using a $\Gamma^{-1}$-preconditioned gradient iteration with contraction factor $1/3$ and Lipschitz stability. With multiple defects the charge-one sector is degenerate; separation $L\gtrsim 2R+(P+1)r_0$ ensures defect-coupling processes appear only at order $\ge L/r_0$, contributing $CJ2^{-P}$.

**Why it matters** It cleanly decouples Heisenberg scaling from trusted multi-qubit gates or vanishing pulse intervals — the regime relevant to calibrating trapped-ion, Rydberg, and superconducting platforms. It also establishes prethermalization as an explicit *resource* for quantum learning, with tools (analytic continuation of ADHH, cluster truncation) reusable for certification and constrained-dynamics problems.

**Caveats** Finite achievable field strength still imposes a precision floor (though exponentially milder). Constants and the ADHH machinery may be pessimistic in practice; no numerics are reported. Results assume $\|\lambda\|_\infty\le 1$, known Pauli term structure, constant $d,q,r_0$, and qubits with Pauli interactions; extensions to fermions/bosons/qudits remain open. SPAM robustness is only to a constant threshold, and the authors note they avoid relying on one ADHH theorem they could not verify.

## 2. Sharp pairwise reduction for quantum hypothesis testing

[arXiv:2609.28440](https://arxiv.org/abs/2609.28440) · [SciRate](https://scirate.com/arxiv/2609.28440)

*Kuan-Yi Lee, Ludovico Lami*

**TL;DR** For any finite ensemble of subnormalized states in any dimension, the pretty good measurement's average error is at most 4 times the sum of the optimal Holevo–Helstrom errors of all pairwise sub-problems, and the constant 4 cannot be improved (a regular-simplex ensemble forces ratio (1+√(1−2/N))² → 4 even for the globally optimal POVM). This halves the constant 8 of Cheng–Liu, confirms the Audenaert–Mosonyi numerical conjecture, and attaches the guarantee to an explicit, implementable measurement rather than a sequential-test construction.

**The big picture** Distinguishing one of many quantum states is a hard optimization with no closed form, whereas telling apart just two states has an exact, classic solution. The natural hope is that the difficulty of the full problem is controlled by the difficulties of all its two-state sub-problems, up to a universal constant that does not depend on the number of candidates or the size of the system. This work settles what that constant is, shows it is attained by the standard "pretty good" measurement that experimentalists can actually build, and proves it cannot be lowered. It also delivers usable finite-sample statements: how many copies of an unknown state suffice for a target error, computed purely from pairwise overlaps.

**Key contributions**
- Sharp pairwise reduction: Err^pg_N ≤ 4 Σ_{i<j} Err*_{ij}, valid for positive trace-class operators in finite or infinite dimension; constant 4 shown optimal.
- A constant-one inequality between squared quantum Hellinger distance and Bures χ² divergence, ‖X^{1/2}−Y^{1/2}‖₂² ≤ ⟨X−Y, Ω_Y^{−1}(X−Y)⟩, improving the previously available factor 2 (relevant independently for χ²-based tomography guarantees).
- A refined one-shot pairwise Chernoff bound with an extra factor α(s)=s^s(1−s)^{1−s} ∈ [0.5,1), shown optimal at the scalar level, applying to the PGM itself.
- Explicit copy count n ≥ ⌈(log(N−1) − log δ)/log(1/ε)⌉ with ε = max_{i<j} Tr√ρ_i√ρ_j, saving log2/log(1/ε) copies over prior work.
- Trace-class/continuity extension by finite-rank truncation, covering bosonic/Gaussian ensembles without photon-number cutoffs.

**How it works** Write T = (A_1^{1/2} … A_N^{1/2}); then S = TT†, G = T†T is the block Gram matrix, and polar decomposition gives T†S^{−1/2}T = G^{1/2}, so the PGM error equals Σ_{i≠j}‖(G^{1/2}−D^{1/2})_{ij}‖₂² ≤ ‖G^{1/2}−D^{1/2}‖₂² with D the block diagonal. The new Hellinger–χ² inequality (proved by reducing to the scalar bound (√x−√y)² ≤ (x−y)²/(x+y) in the joint left/right multiplication eigenbasis, plus positivity of Ω_Y^{−1} via a Sylvester integral) converts this into blockwise harmonic terms ⟨A_i^{1/2}A_j^{1/2}, (L_{A_i}+R_{A_j})^{−1}A_i^{1/2}A_j^{1/2}⟩. Each such term is bounded by Err*(A_i,A_j) using the Helstrom projector and the fact that T†(TT†)^{−1}T is a projector.

**Why it matters** It gives a computable, dimension-free certificate for multi-hypothesis discrimination in terms of exactly solvable binary problems, with the best possible universal constant, and applies to the PGM — the workhorse of decoding, shadow/classical-shadow-adjacent estimation, and optical discrimination experiments.

**Caveats** Sharpness is attained only asymptotically in N; the optimal constant at fixed N is left open, as is the conjectured monotone hierarchy C_{N,2} ≥ … ≥ C_{N,N}=1 for k-wise reductions. The appendix "PGM pairwise reduction" theorem is stated with an equality sign where an inequality is meant. The optimality claim for α(s) is established for the underlying scalar inequality, not demonstrably for the full N-hypothesis Chernoff bound. Extension to continuous/parametric ensembles remains open.

## 3. Efficient learning of Clifford disentanglers and typical $t$-doped unitaries with exponentially more $T$ gates

[arXiv:2609.27565](https://arxiv.org/abs/2609.27565) · [SciRate](https://scirate.com/arxiv/2609.27565)

*Gerard Aguilar, Sofiene Jerbi, Jens Eisert, Lennart Bittel*

**TL;DR** The authors show that states of the form (unknown Clifford) × (tensor product of arbitrary factors) leave a detectable fingerprint in their Bell-sampling distribution: a vector space of *quadratic* symmetries over F₂ whose elements are all simultaneously block-diagonalizable in the Clifford's symplectic frame. Lifting Bell outcomes to q⊗q linearizes these constraints, and a Wedderburn-type simultaneous block-diagonalization recovers both a disentangling Clifford and the hidden partition in poly(n) time with O(λ⁻²(n² + log 1/δ)) copies. Applied to Choi states, this gives *proper* learners for typical t-doped Clifford circuits up to t ≈ 2n — exponentially beyond the previous O(log n) barrier.

**The big picture** It has been folk wisdom that quantum states with lots of entanglement and lots of "magic" should be hard to learn, and that circuits doped with more than logarithmically many non-Clifford gates enter a chaotic, unlearnable regime. This work shows that a structural property — being a product state hidden behind an arbitrary Clifford scrambler — survives the scrambling as an algebraic invariant that two-copy measurements can extract efficiently. The consequence is that a fraction of near-chaotic doped Clifford circuits that shrinks only very slowly (and remains constant even at twice the qubit number in gate count) is in fact efficiently and properly learnable from state access alone. This reframes what counts as evidence of pseudorandomness: high entanglement and high magic are not enough.

**Key contributions**
- A general framework of *quadratic* Bell symmetries qᵀMq = c on supp(b_ρ), with an explicit dictionary mapping them to generalized purity constraints on the Pauli distribution; ordinary subsystem purity and stabilizers appear as special cases.
- Proof that Clifford action maps symmetries by congruence plus an affine shift, M ↦ C⁻ᵀ(M+λ_C)C⁻¹.
- Theorem: for stabilizer-free product states, *every* quadratic Bell symmetry is block-diagonal across the cut — so the whole kernel, not just the two purity forms, carries the partition.
- Polynomial-time simultaneous block-diagonalization via the commutant algebra 𝔢 of 𝔱 = span{Ω(Mᵢ+Mᵢᵀ)}, its semisimple/radical decomposition, and a subsequent correction to a symplectic change of basis.
- Efficient testing and learning theorems, plus full state tomography when factors have O(log) size, via Bakshi et al.
- Typical learnability of t-doped Cliffords: success probability ∏ᵢ₌₀^{k−1}(1 − (2ⁱ−1)/(4ⁿ−1)), giving 1 − O(2^{−cn}) at k ≤ 2n − cn and Θ(1) at k = 2n − O(1).

**How it works** Bell-sample the state; run stabilizer learning first to strip off stabilizer factors (needed for the block theorem); Gaussian-eliminate on lifted samples q⊗q to get a basis of the finite-sample quadratic kernel; block-diagonalize; then solve a small linear system over F₂ to identify which blocks correspond to genuinely pure factors. For unitaries, conjugating T gates through yields U_C ∏ e^{iπP_i/8}; algebraic independence of the resulting Paulis makes the Choi state fit the template, and single-factor tomography gives a proper circuit description with diamond-norm error accumulating only linearly in t.

**Why it matters** Relevant to quantum learning theory and pseudorandomness (an obstruction to "gluing" Cliffords onto pseudorandom product states), to benchmarking encoded logical product states code-agnostically, to Clifford-augmented MPS as a simulation ansatz, and to Hamiltonian compression using only forward-time evolution (no inverse access, unlike Grewal et al.).

**Caveats** Everything is exact: exact Cliffords, exact product structure. Perturbing either turns the constraints noisy and reduces recovery to an LPN-like problem — the authors conjecture this is genuinely hard. A stabilizer-gap promise η is required (spectral separation |⟨P⟩| = 1 or ≤ 1−η), and runtime/sample counts scale as 1/λ² with λ = min(η, ε/√n). Full-state learning needs small factors. The claim that all quadratic Bell constraints reduce to stabilizer and subsystem purities is left as a conjecture.

## 4. Improved Transversal Non-Clifford Gates from Cup Products

[arXiv:2609.27801](https://arxiv.org/abs/2609.27801) · [SciRate](https://scirate.com/arxiv/2609.27801)

*Louis Golowich, Itzhak Tamo, Guanyu Zhu*

**TL;DR** The authors give a general cup-product recipe turning classical Tanner codes with a component-wise *multiplication property* into quantum CSS codes with transversal $C^{r-1}Z$, and instantiate it with punctured tensor powers of algebraic-geometry codes. The result is the first *constant*-weight-stabilizer qLDPC family with $d\ge n^{(1-\epsilon)/r}$ and logical yield $s\ge n^{1-\epsilon}$, breaking the previous $ds\le O(n)$ barrier and giving magic-state overhead exponent $\gamma\to 0$ with LDPC checks; a variant achieves $s=\Omega(n)$, $d=\Omega(n^{1/r})$ at stabilizer weight/depth $n^\epsilon$. Both come with polynomial-time adversarial decoders and support addressable gates.

**The big picture** Fault-tolerant quantum computers need non-Clifford gates, and the cheapest known way to get them is a code on which the gate can be applied in a shallow physical circuit. Until now, every sparse-check code with such a shallow non-Clifford gate was stuck at a repetition-code-like tradeoff: either good error protection or many gates in parallel, never both. This work constructs sparse-check codes that beat that tradeoff, and in doing so gives the first sparse-check codes whose magic-state distillation overhead exponent can be pushed arbitrarily close to zero. It also supplies a modular recipe, so future classical code constructions can be plugged in directly.

**Key contributions**
- A clean classical-to-quantum theorem: given $r$ local-code systems on a graph obeying $\mathrm{im}\mathcal F^{(1)}*\cdots*\mathrm{im}\mathcal F^{(r-1)}\subseteq \mathrm{im}\mathcal F^{(r)}$ vertex-wise, plus a shared extendable set $M$, one gets quantum codes of length $\Theta(|V|^r)$, distance $\Omega(d)$, and logical yield $|M|^r$.
- First constant-weight-stabilizer codes with $ds\gg n$ and $\gamma$ arbitrarily small (prior work needed $\mathrm{polylog}$ or linear weight).
- A new family of constant-check-weight classical Tanner codes with the multiplication property, obtained by puncturing high tensor powers of AG codes — resolving the rate-$\le 1/2$ obstruction that blocks naive constraint-counting.
- Addressability of individual logical tuples, plus efficient decoders.

**How it works** Quantum codes are $r$-fold tensor products of the 1-dimensional cochain complexes of the Tanner codes (cyclically permuting which factor is the dual system $\mathcal F^{(r)\perp}$). A cup product is built at the 1-complex level from the multiplication property, then lifted to the tensor products via the Koszul-signed formula $(a\otimes b)\smile(a'\otimes b')=(-1)^{i_bi_{a'}}(a\smile a')\otimes(b\smile b')$; pairing against the all-ones cycle $z_*$ defines the multilinear form $f$, whose subrank on the chosen subsystem equals the logical yield and factorizes across tensor factors. Circuit depth is bounded by sparsity via a graph-coloring argument. Classically, $C^{\otimes t}$ is realized as a Tanner code on a $t$-partite graph of axis-parallel lines in $[2n]^t$, with edges at line intersections thinned so each point carries at most one edge; the punctured code decomposes into few unpunctured tensor codes, giving decoders via the generalized Quintavalle–Roffe–Browne product decoder.

**Why it matters** Relevant to anyone designing magic-state factories or qLDPC architectures: constant-weight checks plus near-linear yield is the regime where constant space-time overhead magic-state preparation becomes plausible (the paper identifies exactly what is missing: constant-rate, polynomial-distance classical LDPC codes with a multiplication property).

**Caveats** These are *subsystem* codes: distance holds only on a chosen subsystem, and all gauge qudits plus unused logicals must be gauge-fixed to $|0\rangle$ beforehand — no fault-tolerant gauge-fixing or Clifford protocol is given. Distance is only $\sim n^{1/r}$, far from linear (the suggested fix, balanced products, requires expansion proofs that do not yet apply). Yield stays sublinear in the LDPC regime; the $\Omega(n)$-yield variant sacrifices constant weight and depth. Decoding guarantees are adversarial, not stochastic, and constant-size-alphabet/depth-1 statements rely on prior reduction lemmas whose decoder preservation is only asserted.

## 5. Sustained growth of quantum circuit complexity in many-body Hamiltonian dynamics

[arXiv:2609.26885](https://arxiv.org/abs/2609.26885) · [SciRate](https://scirate.com/arxiv/2609.26885)

*Wonjun Lee, Saúl Pilatowsky-Cameo, Soonwon Choi*

**TL;DR** The authors prove, without complexity-theoretic or spectral assumptions, that for generic local extensive Hamiltonians and typical product states at high effective temperature, the ε-robust circuit complexity of the evolving state (and of any sufficiently large subsystem) is at least exp Ω(n) for all but a doubly-exponentially small fraction of times, with ε allowed exponentially close to 1. The two enabling structural results — that generic local Hamiltonians satisfy the k-th no-resonance condition for *every* k, and that typical finite-temperature product states have exponentially large inverse participation ratio in the energy basis — were previously assumed but unproven.

**The big picture** After a chaotic quantum system thermalizes, local observables and entanglement stop changing, yet the wavefunction keeps evolving; circuit complexity — how many elementary gates are needed to build the state — has been proposed as the quantity that keeps growing. Until now, rigorous results were confined to models that inject randomness in time and violate energy conservation, which is precisely the constraint that makes the holographic version of the conjecture interesting. This work delivers the first unconditional statement for ordinary, fixed, energy-conserving local Hamiltonians and ordinary product initial states, showing that complexity must climb to an enormous value and must therefore keep growing for an extraordinarily long stretch of time. It also explains why nobody sees this: any small enough region of the system remains easy to prepare.

**Key contributions**
- Proof that violations of the arbitrary-order no-resonance condition form a measure-zero set of local Pauli-coefficient space (generalizing the k=2 result of Huang et al.), via exhibiting one explicit 1D spectrally ergodic Hamiltonian and a polynomial-nonvanishing argument.
- Energy dispersion for the continuous microcanonical product-state ensemble E_{β,δ} at |β|<β_c, with explicit non-asymptotic constants (previous work covered only stabilizer product states).
- Theorem 2: exponential complexity from spectral ergodicity + energy dispersion alone — applies to nonlocal Hamiltonians and entangled initial states too.
- Corollaries: sustained growth over exponentially many ordered time points; volume-law entanglement irremovable by circuits of ≤ exp(O(n^{1-η/4})) gates; generic no-fast-forwarding (so all-commuting, 1D quadratic fermionic, number-conserving quadratic bosonic models are measure-zero); doubly-exponential average recurrence time.
- Complementary upper bound: regions that thermalize have complexity exp(polylog|A|), proven for |A| ≤ O(log n) in translation-invariant systems.

**How it works** A covering-net count gives ≲ G^{O(G)} states reachable by G two-qubit channels. Markov's inequality on the k-th temporal moment of ⟨ψ(t)|σ|ψ(t)⟩ bounds the time fraction spent ε-close to any fixed σ by M_k(1−ε)^{−2k}; spectral ergodicity kills all non-resonant off-diagonal terms giving M_k ≤ k!(max_μ p_μ)^k, and energy dispersion gives max_μ p_μ ≤ 2^{−γn/2}. Choosing k = e^{αn} with α < γ/4 makes this exp(−exp(αn)), surviving a union bound over the net for G = exp(α′n).

**Why it matters** It moves the Brown–Susskind program from random-circuit toy models to physical Hamiltonian dynamics, and supplies two long-assumed lemmas that many equilibration/deep-thermalization proofs rely on. Relevant to holography, quantum simulation lower bounds, and pseudorandomness.

**Caveats** Linearity of growth is not established — and cannot be, absent PSPACE ⊄ BQP. "Generic" is measure-theoretic: no explicit Hamiltonian is certified. The finite-time bound scales as exp(exp(O(n)))/Δ^{(k_c)}, and no rigorous lower bound on the k-th spectral gap exists even for k=1,2; the quoted t_typ ≲ exp(exp(Ω(n))) rests on a heuristic Δ^{(k)} ~ exp(−Θ(nk)). Subsystem results require |A| ≥ cn with c = 1−γ/8 near 1, leaving the half-system regime open. Restricted to qubits on hypercubic lattices, high temperature, no symmetries or fermions.
