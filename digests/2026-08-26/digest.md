# SciRate Daily Digest — 2026-08-26

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Optimal Lower Bound for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24493](https://arxiv.org/abs/2608.24493) · [SciRate](https://scirate.com/arxiv/2608.24493)

*Rolando D. Somma, Ronald de Wolf*

**TL;DR** The paper proves the first lower bound Ω(log(1/ε)/γδ) on the number of Hamiltonian-simulation calls needed for guided ground-state energy estimation that is simultaneously tight in the precision, overlap, and failure-probability parameters, matching the concurrent Jeffery–Witteveen upper bound. The bound is established via the polynomial method with fractional phase queries, and extends to unique-ground-state instances with a spectral gap, to ground-state *preparation*, to block-encoding access, and (with a quadratically weaker precision dependence) to the sum-of-squares spectral amplification setting.

**The big picture** Estimating the lowest energy of a quantum system is the flagship application of quantum computers in chemistry, and the standard formulation assumes you can cheaply prepare a trial state with some guaranteed overlap with the true ground state. The cost of such algorithms is governed by three quantities: how precisely you want the energy, how good your trial state is, and how confident you want to be in the answer. Until now, matching lower bounds were known only when one of these three was held fixed; this work closes the gap and shows the recently discovered algorithm is optimal in all three at once. It also shows the same hardness applies when you actually want the ground state itself rather than just its energy.

**Key contributions**
- Joint lower bound Ω(log(1/ε)/γδ) for degenerate instances of dimension ≈ log(1/ε)/γ².
- Same bound for the physically natural case of a *unique* ground state with spectral gap 3δ, at the price of dimension log(1/ε)²/γ².
- Transfer of the bound to block-encoding access (via H = −i(U−U⁻¹)/2), to fractional/continuous-time simulation, and to ε-accurate ground-state preparation.
- Ω(log(1/ε)/γ√δ) for the SOSSA model with black-box access to G where H = G†G, showing SOSSA's quadratic speedup is near-optimal.

**How it works** The hard family is H = diag(0, {3δ·xⱼ}), so U = e^{iH} is a (3δ/π)-fractional phase query to x; distinguishing x = 0ⁿ from |x| ≥ γ²N is OR. Writing the fractional query as a convex-like combination of I and the ±1 phase oracle and truncating the 2^T-term expansion at K = O(Tδ + log(1/ε)) oracle factors gives an ε-close low-degree approximating polynomial (norm error ≤ 2^{−K}). Symmetrization plus Coppersmith–Rivlin (integer-to-real interval bound, cost 2^{O(D²/N)}) and Chebyshev extremality (growth 2^{O(Dγ)}) force log(1/ε) ≲ D²/N + Dγ, hence T = Ω(log(1/ε)/γδ). The unique-ground-state version uses U = I + (e^{iθ}−1)|ψ⟩⟨ψ| with |ψ⟩ = √a|0⟩ + ω√(1−a)|j⟩; averaging over the sign ω kills odd cross terms, yielding a univariate polynomial in a, and a two-case split (small vs. large acceptance at a = 0) balances a √N/δ search bound against the Chebyshev bound.

**Why it matters** Subconstant-ε dependence matters when energy estimation is a subroutine inside a larger algorithm, where median-amplification overheads compound; this settles that no cleverer error reduction (à la the √log(1/ε) trick for Grover) exists here. The AI-assistance statement is also notable: ChatGPT produced the hard families and a 20+ page proof, later simplified by the authors.

**Caveats** The bounds require dimension growing with log(1/ε)/γ² (or its square), so they say nothing about small fixed-dimension instances. They do not apply to sparse-matrix access and capture no sparsity overhead — left open. Most conceptually, the guiding states in both hard families are *uninformative*: they are fixed states independent of H that merely satisfy the overlap promise, suggesting the standard overlap-only formulation of the guided Hamiltonian problem may be the wrong abstraction. Gate complexity and calls to A are not counted (which only strengthens the lower bounds).

## 2. Optimal Quantum Algorithm for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24494](https://arxiv.org/abs/2608.24494) · [SciRate](https://scirate.com/arxiv/2608.24494)

*Stacey Jeffery, Freek Witteveen*

**TL;DR** This paper closes the long-standing logarithmic gap in guided ground-state energy estimation: it gives an algorithm that estimates the largest eigenphase of a unitary $U$ to precision $\delta$, given a guiding state with ground-space overlap $\ge\gamma$, using $O(1/(\gamma\delta))$ controlled queries to $U$ and $O(\tfrac1\gamma\log\tfrac1\delta\log\log\tfrac1\delta)$ queries to the state-preparation unitary $A$. This removes the $\log(1/\gamma)$ factor inherent to both QPE-based and QSVT-based approaches and matches the Mande–de Wolf lower bound, answering their open question.

**The big picture** Estimating the lowest energy of a quantum system, given a decent trial state, is one of the flagship applications of fault-tolerant quantum computers, and essentially all known methods pay a small but real overhead in running time that grows as the trial state gets worse. That overhead comes from having to suppress errors in phase estimation, or ripples in polynomial approximations, below the level of the trial state's overlap. Here the authors show the overhead is entirely avoidable by rebuilding the algorithm in the "transducer" framework, which composes bounded-error subroutines without paying for error reduction. The resulting query cost is provably optimal, and since simulation time dominates real resource estimates, the improvement is of practical, not just asymptotic, interest.

**Key contributions**
- Optimal query complexity $\Theta(1/(\gamma\delta))$ for max eigenphase estimation / guided ground-state energy; combined with concurrent work (Somma et al.), $\Theta(\tfrac{1}{\gamma\delta}\log\tfrac1\epsilon)$ including error dependence.
- A standalone exact transducer for *decision amplitude amplification* ($\Pi_M|\psi\rangle=0$ vs. not), with $W\le 1/\gamma$ when $w=\gamma$.
- A standalone exact transducer for *decision phase estimation* (is $x>\tilde s$?), a quantum walk on infinite weighted lines with weights $\gamma_k=\tan(\theta_k/2)$.
- A general lemma (exact $(D,m)$-truncation) letting one replace an infinite counter register by a $O(\log D)$-qubit one with *zero* error, useful beyond this paper.

**How it works** The threshold problem — distinguish $\|\Pi_{>s}|\psi\rangle\|\ge\gamma$ from $\Pi_{>s-\delta'}|\psi\rangle=0$ — is solved by a single canonical transducer $S=S^\circ O$ where $O=O_\gamma(A)$ is a reflection about $\sqrt{\gamma/(1+\gamma)}|00\rangle+\frac{1}{\sqrt{1+\gamma}}|1\rangle A|0\rangle$ (one call each to $A,A^\dagger$), and $S^\circ$ uses $O(1)$ controlled calls to $U,U^\dagger$ via $R(U)=|-\rangle\langle+|\otimes e^{i\sigma}U+\mathrm{h.c.}$. The transduction action is $|\bar1,0\rangle\rightsquigarrow\pm|\bar1,0\rangle$, read out by single-bit phase estimation. Crucially the transduction complexity $W=O(1/(\gamma\delta))$ while the Las Vegas query complexity to the $A$-oracle is $L\le 1+1/\gamma$, so the conversion theorem of Belovs yields separate, optimal counts for $U$ and $A$. Binary search over $s$ gives the estimation result.

**Why it matters** Phase estimation is a universal subroutine; the authors argue similar transducer surgery should strip log factors elsewhere. For chemistry/materials resource estimates, evolution time scales as $O(\lambda/(\gamma\delta))$, and constants are claimed modest.

**Caveats** Requires the window promise (all eigenphases in $[0,\pi/2]$). Space overhead is $O(\log\frac{1}{\gamma\delta})$ qubits versus $O(\log\frac1\delta)$ for standard QPE. The $A$-query count retains $\log\frac1\delta\log\log\frac1\delta$ factors of unknown optimality. Constants are not optimized and no numerics are given; full coherence of the routine is left open. LLMs were used for some proofs/computations (authors state all were verified and rewritten).

## 3. Improved Quantum Codes with Transversal T Gates

[arXiv:2608.24000](https://arxiv.org/abs/2608.24000) · [SciRate](https://scirate.com/arxiv/2608.24000)

*Adam Wills*

**TL;DR** — This paper gives the first improvement since 2017–18 (Hastings–Haah, Haah) on asymptotic parameters of quantum CSS codes admitting a *strict* transversal T gate (physical T on every qubit ⇒ logical T on every logical qubit, no Clifford correction). The key technical tool is a closed-form distance formula for decreasing monomial codes punctured at a downward-closed set of hypercube points, instantiated with weighted Reed–Muller codes. It yields the first constant-rate, growing-distance codes with transversal T, hence the first magic-state-distillation overhead exponent γ → 0 for a code with a transversal T gate (previously γ ≈ 0.678).

**The big picture** — Fault-tolerant quantum computers need at least one gate outside the "easy" Clifford set, and the cheapest way to get one is a code where applying the same simple physical gate to every qubit directly enacts that gate on every encoded qubit. Codes with this property for the standard non-Clifford single-qubit gate have been stuck at the same parameter frontier for nearly a decade, while recent breakthroughs only handled bulkier multi-qubit gates. This work broadens the achievable trade-off between how many qubits a code encodes and how well it protects them, and for the first time achieves a constant encoding rate with distance that still grows — implying magic state distillation whose overhead cost exponent vanishes asymptotically.

**Key contributions**
- Closed-form distance of a decreasing monomial code punctured at a downset Γ: d = min_{A∈Δ} |{V ⊆ Ā : V ∉ Γ}|, valid under a "non-annihilation" condition (of independent interest for polar-code / punctured-evaluation-code literature).
- Explicit families with [[n, Ω(n^{α+o(1)}), Ω(n^{β_explicit(α)+o(1)})]], β_explicit(α) = (1−2q*(α))/3 for α > H₂(1/6), strictly beating the previous explicit frontier.
- Explicit constant-rate families: for any R ∈ (0,1/3), [[n, (R+o(1))n, Ω(2^{(c_R+o(1))√log₂ n})]] with c_R = −Φ⁻¹(2R/(1+R)); first γ = log(n/k)/log d → 0 with transversal T (even allowing Clifford corrections).
- Randomised construction improving the polynomial-rate frontier further: β_exist(α) = 1−2H₂⁻¹(α) for α ≥ H₂(1/3), etc.

**How it works** — Standard X-generator-matrix formalism: an 8-divisible classical binary code C, punctured at k coordinates Γ, gives a CSS code with transversal T via Ward identities; distance equals d(punc_Γ(C^⊥)). Rather than Reed–Muller with 3r < m (low dimension), the author uses weighted Reed–Muller downsets with weight vector (1,…,1,h), which keeps 8-divisibility while raising dimension, and punctures at Γ = {A ⊆ [m−1] : |A| ≤ w}. Because both Δ and Γ are downsets, the distance formula applies and the naive "distance drops by ≤ k" bound is beaten. The randomised variant "protects" points from puncturing using a random t-uniform hypergraph on [m−1] covering all y-subsets, so any large A ∉ Δ retains ≥ 2^{|A|−t} unpunctured subsets, trading a small loss in k for a distance gain.

**Why it matters** — Relevant to magic state distillation (T-to-T, no Clifford correction ⇒ fast protocols), to concatenated/hierarchical architectures where non-LDPC inner codes are acceptable, and as theory input for the active line on LDPC codes with transversal non-Clifford gates. Transversal T also immediately gives transversally addressable lower-hierarchy gates, unlike CCZ constructions.

**Caveats** — Codes are non-LDPC, so they must be run at a logical level of some other code. The constant-rate distance is only sub-polynomial (2^{Θ(√log n)}), and R is capped below 1/3. The randomised construction gives no improvement in the constant-rate regime and is non-explicit. Restriction to stabiliser/CSS codes; the author suspects non-stabiliser codes could do better.

## 4. Nearly Optimal Amplitude Estimation at any Depth

[arXiv:2608.24434](https://arxiv.org/abs/2608.24434) · [SciRate](https://scirate.com/arxiv/2608.24434)

*Jona Erle, Bálint Koczor*

**TL;DR** The paper introduces Windowed Least Squares Amplitude Estimation (WLSAE): sample Grover depths from a "window" distribution, collect ±1 outcomes, and fit the Grover angle by minimizing a one-dimensional least-squares loss on a grid. For any window in an explicitly characterized *admissible* class, the estimator achieves additive error ε in the angle with M²N ∈ Õ(ε⁻²) — matching the Zalka–Burchard lower bound up to logs — *uniformly* over λ ∈ [0, π/2], including the boundaries where prior depth-tunable methods degrade to classical sampling.

**The big picture** Amplitude estimation is the workhorse behind quadratic speedups in quantum Monte Carlo, finance, and chemistry, but the textbook version needs long coherent circuits, ancillas, and phase estimation — all unaffordable on early fault-tolerant hardware. A line of recent work trades circuit depth for repetitions, but existing accuracy guarantees quietly break down when the amplitude is very close to zero or one, exactly the regime relevant to overlap certification and trial-state verification. This work shows that a simple randomized-depth, ancilla-free, control-free sampling scheme with a least-squares fit is optimal (up to logarithmic factors) at every depth *and* every amplitude, so the speedup never collapses at the extremes.

**Key contributions**
- A general admissibility criterion for depth distributions: (W1) each symmetric depth pair carries mass ≳ b/T up to the effective width T = max(1, M/σ); (W2) moment bounds E[m^{2k}] ≤ O(T^{2k}) for k ≤ 4. Every window on W_M satisfies (W2) with σ^{2k}, so (W1) is the real condition.
- Uniform-in-λ guarantee: |θ̂ − λ| ≤ ε w.p. 1 − δ once M²N ≥ O(σ²A²C₉² ε⁻² log(1/εδ)), giving the full interpolation M = ⌊ε^{−1+β}⌋, N = Õ(ε^{−2β}), queries Õ(ε^{−1−β}) for β ∈ [0,1].
- Shows the "boundary patch" of Gaussian LSAE (Huang–Koczor) is unnecessary and actually forfeits the speedup where invoked; Gaussian windows are just one member of the class.
- Numerics: at fixed Q = 10⁶ over 10⁴ runs, a plain uniform window beats the Gaussian one, tracking the Cramér–Rao bound.

**How it works** The population loss ℰ^{(λ)}(θ) = E_m[(cos 2mλ − cos 2mθ)²] is sandwiched between C₂Ψ² and C₁Ψ², with envelope Ψ(Δ) = min(1, TΔ, T²Δ·max(λ̄, Δ)), λ̄ = min(λ, π/2 − λ). Near the boundary the loss flattens from quadratic to quartic in Δ — but Bernstein concentration of the empirical fluctuation, using Var[Z_m] = sin²(2mλ), gives a matching envelope Ω that shrinks in the same way. The signal-to-noise ratio is therefore preserved, and a localization lemma (grid minimizer lies within Aκ of λ whenever the loss gap beats the fluctuation) closes the argument.

**Why it matters** A practically implementable, ancilla-free AE primitive with a provable, amplitude-independent depth–repetition tradeoff is directly useful for EFT resource estimates, and the admissible-window framework decouples the proof from any specific distribution, allowing empirical window optimization.

**Caveats** The proven constants are astronomical: A = 3C₈/(8C₂) > 3×10⁶ forces a grid of K ≈ Aπ/(2ε) points, whereas the experiments use K = ⌈100√(E[m²]N)⌉ — so the theory is asymptotic and the practical claim rests on numerics. The guarantee is on the Grover angle (translating to |â − a| ≤ 2√(a(1−a))ε + ε²); analysis assumes exact, noiseless Grover iterates; and no adaptive/sequential variant or noise-robustness analysis is given.

## 5. Essentially optimal gate teleportation

[arXiv:2608.24345](https://arxiv.org/abs/2608.24345) · [SciRate](https://scirate.com/arxiv/2608.24345)

*Lukas Schmitt, David Sutter*

**TL;DR** The authors give the first explicit deterministic LOCC protocol that implements a two-qubit controlled-phase gate $U_\phi=\mathrm{diag}(1,1,1,e^{i\phi})$ using strictly less than one ebit, with a Schmidt-rank-3 resource state costing $h(q)+1-q$ ebits where $q=1/(1+\sin(\phi/2))$, together with a matching-in-form converse of $h(q)$. Small rotation angles therefore need only vanishing entanglement, which lets a distributed $2n$-qubit QFT be teleported with a *constant* $\approx 12.19$ ebits instead of $n^2$.

**The big picture** A quantum gate acting on two distant parties can be implemented without any direct interaction, by consuming pre-shared entanglement plus classical messages. Until now every known deterministic protocol burned at least one full unit of entanglement, even for a gate that barely entangles at all — an obvious mismatch, since a nearly trivial gate ought to be nearly free. This work closes that gap for the controlled-phase family: the entanglement consumed now shrinks continuously to zero as the gate approaches the identity, and both a concrete protocol and a near-matching impossibility bound are provided. The immediate payoff is for distributed and modular quantum computing, where the entanglement budget across chip or node boundaries is the dominant cost.

**Key contributions**
- An explicit four-round deterministic LOCC protocol (4 bits of classical communication) using a rank-3, non-maximally-entangled resource state, resolving the open question of sub-ebit gate teleportation posed by Eisert et al. and numerically hinted at by Stahlke–Griffiths.
- A general converse $H(A')_\psi \ge h(1/(1+\sin(\phi/2)))$ from Nielsen majorization, plus a strictly tighter converse for resource states of fixed Schmidt rank $D$, showing that for any finite $D$ some angles still require a full ebit.
- Proof that the chosen resource state is the entropy-optimal one within the protocol's feasible family, and extension via KAK to arbitrary controlled and general two-qubit unitaries.
- Application: distributed (bit-reversed) QFT on $2n$ qubits at $\le 12.1869$ ebits for all $n$, versus $n^2$ with the one-ebit-per-gate construction.

**How it works** Alice's first unitary plus an ancilla measurement collapses the qutrit resource into a two-dimensional, input-independent branch (outcome probability exactly 1/2, so no information leaks). Bob applies a controlled diagonal phase $D_x$ followed by a qutrit Fourier transform, treating all three Schmidt coordinates symmetrically so his measurement neither learns Alice's bit nor destroys coherence. The nonlocal phase $e^{i\phi}$ is absorbed by choosing $d_{i_x},d_{j_x}$ as intersection points of two circles in the complex plane; the intersection condition is exactly the feasibility constraint $\sin^2(\phi/2)(1-2p_1)(1-2p_2)\le 4p_1p_2$. Unitarity of Alice's final correction is then automatic, and Bob's last step is a diagonal phase fix. The rank-restricted converse uses Binet–Cauchy determinant identities on separable-channel product Kraus operators, plus Cauchy–Schwarz tail bounds on the Schmidt spectrum.

**Why it matters** Entanglement distribution is the bottleneck in modular/distributed architectures and in circuit-knitting-style cut simulations; this shows the cost should scale with a gate's entangling power, not be quantized to ebits. The constant-cost distributed QFT is a striking concrete consequence.

**Caveats** A gap remains between $h(q)+1-q$ and $h(q)$; the protocol beats one ebit only for roughly $\phi \lesssim 0.6$ rad, and reverts to the known one-ebit scheme beyond that. The exact teleportation cost $T_C(U_\phi)$ is still unknown, and the finite-rank converse suggests unbounded Schmidt rank may be needed for optimality. General two-qubit unitaries are handled suboptimally by teleporting the three KAK components separately. The authors credit an LLM with assisting in developing the protocol and the tighter converse.
