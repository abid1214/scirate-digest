# SciRate Daily Digest — 2026-08-26

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Optimal Lower Bound for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24493](https://arxiv.org/abs/2608.24493) · [SciRate](https://scirate.com/arxiv/2608.24493)

*Rolando D. Somma, Ronald de Wolf*

**TL;DR** The authors prove a query lower bound of Ω(log(1/ε)/(γδ)) on uses of U = e^{iH} (or a block-encoding of H) for estimating a ground-state energy to precision δ given a guiding state of overlap ≥ γ and failure probability ε — tight in all three parameters simultaneously, matching the concurrent Jeffery–Witteveen upper bound. The bound survives in the well-conditioned regime (unique ground state with spectral gap), extends to ground-state *preparation*, and yields Ω(log(1/ε)/(γ√δ)) for sum-of-squares spectral amplification, showing SOSSA is near-optimal as a black-box use of the square-root operator.

**The big picture** Estimating the lowest energy of a quantum system, starting from a cheap trial state that has some nonzero overlap with the true ground state, is the workhorse subroutine of quantum chemistry algorithms, and the dominant cost is the number of time-evolution steps. Prior lower bounds only pinned down the cost when one of the three knobs — precision, overlap, or allowed failure probability — was held fixed; in particular it was unclear whether the failure probability could be suppressed cheaply, as it can for quantum search. This work shows it cannot: the naive strategy of repeating and taking a median is already optimal, and the resulting bound exactly matches the best known algorithm, closing the problem. A side observation is philosophically interesting: the hardest instances have trial states that carry essentially no information about the ground state, suggesting that "overlap" alone may be the wrong way to formalize what a good guiding state is.

**Key contributions**
- Joint lower bound Ω(log(1/ε)/(γδ)) (dimension ≥ log(1/ε)/γ²), resolving the open problem of Mande–de Wolf.
- Same bound for the restricted, more physically relevant case of a *unique* ground state with a 3δ gap, at the cost of dimension log²(1/ε)/γ².
- Reduction giving the same bound for ground-state preparation to trace distance ε with gap δ; extensions to block-encoding access and continuous-time/fractional queries.
- Ω(log(1/ε)/(γ√δ)) for the SOSSA setting H = G†G with black-box G.

**How it works** The first hard family is H = diag(0, {θx_j}) with θ = 3δ, so U is a (3δ/π)-fractional phase query to x; distinguishing x = 0 from |x| ≥ γ²N is exactly OR. A truncation argument writes the fractional query as a convex-like combination of I and the ordinary phase oracle, discards terms with more than K = O(Tδ + log(1/ε)) oracle factors (operator-norm error ≤ ε/3), and yields a degree-O(Tδ + log(1/ε)) approximating polynomial — i.e. converts a T-query δ-precision algorithm into an O(Tδ)-degree object. Coppersmith–Rivlin plus Chebyshev extremality then force the approximation error to be ≥ 2^{-O(D²/N + Dγ)}; setting N = log(1/ε)/γ² gives the bound. The unique-ground-state version uses U = I + (e^{iθ}−1)|ψ⟩⟨ψ| with |ψ⟩ = √a|0⟩ + ω√(1−a)|j⟩; averaging over the sign ω kills odd powers of √(a(1−a)), producing a univariate polynomial in a, and a case split (small vs. large acceptance at a = 0) balances a √N/δ search bound against the Chebyshev bound at N = log²(1/ε)/γ².

**Why it matters** Fixes the exact cost of the central quantum-chemistry primitive, including the ε-dependence that matters when it is used as a subroutine inside larger algorithms (where transducer tricks fail for multi-output subroutines). Confirms SOSSA's quadratic δ-improvement is essentially the end of the line for black-box G.

**Caveats** The bounds require dimension growing as log(1/ε)/γ² (or log²(1/ε)/γ²); no bound is claimed for small Hilbert spaces. Sparse-access Hamiltonians (with the sparsity-d overhead) remain open despite the hard instances being 1- or 2-sparse. The hard guiding states are input-independent, so the bounds arguably indict the problem formulation rather than the algorithms. Notably, the authors credit ChatGPT 5.6 Pro with generating both hard families and long initial proofs, later simplified by hand.

## 2. Optimal Quantum Algorithm for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24494](https://arxiv.org/abs/2608.24494) · [SciRate](https://scirate.com/arxiv/2608.24494)

*Stacey Jeffery, Freek Witteveen*

**TL;DR** The authors give a quantum algorithm for guided ground-state energy / maximum-eigenphase estimation that uses $O(1/(\gamma\delta))$ controlled calls to the evolution/walk unitary $U$ and $O(\frac{1}{\gamma}\log\frac1\delta\log\log\frac1\delta)$ calls to the state-preparation unitary $A$, shaving the $\log(1/\gamma)$ factor that both QPE-based and QSVT-based approaches incur. This matches the $\Omega(1/(\gamma\delta))$ lower bound of Mande–de Wolf, settling their open question; the tool is Belovs-style *transducers*, which compose without error-reduction overhead.

**The big picture** Estimating the lowest energy of a quantum system, given a trial state with some guaranteed overlap with the true ground state, is the canonical fault-tolerant quantum chemistry primitive, and its cost is dominated by how long one must simulate the system. Every previous method paid a logarithmic penalty in the inverse overlap, because a subroutine's error had to be pushed below the (small) signal from the ground state — either by lengthening phase estimation or by raising the degree of an approximating polynomial. Here the penalty is removed by replacing bounded-error subroutines with a composable, error-free algorithmic object whose "cost" is a catalyst state rather than a failure probability, yielding the first provably query-optimal algorithm for this task.

**Key contributions**
- Query-optimal algorithm for the guided max-eigenphase / ground-state energy problem; combined with a simultaneous companion lower bound, the complexity is $\Theta(\frac{1}{\gamma\delta}\log\frac1\epsilon)$.
- An exact transducer for *decision amplitude amplification* (decide whether $\Pi_M|\psi\rangle=0$), with $W\le \max(w/\epsilon,1/w)$, balanced at $w=\gamma$.
- An exact transducer for *decision phase estimation* (is $x\gtrless s$?) via a quantum walk on weighted infinite lines.
- A general lemma (Def. of exact $(D,m)$-truncation + Lemma 3) showing the infinite counter register can be truncated at $D=O(K)$ with *zero* error.

**How it works** A transducer $S$ on $\mathcal H\oplus\mathcal L$ implements a target unitary $U_S$ exactly, at the cost of a catalyst $|v\rangle$; $W=\||v\rangle\|^2$ controls the number of applications of $S$, and the Las Vegas query complexity $L=\|\Pi_{\mathcal L^\bullet}|v\rangle\|^2$ separately controls oracle calls — allowing fewer than one query per iteration. The composed transducer (Thm. 4) acts as $|\bar1,0\rangle\rightsquigarrow \pm|\bar1,0\rangle$, the sign deciding the threshold problem, read out by single-bit phase estimation. It uses the oracle $O_\gamma(A)$ = reflection about $\sqrt{\gamma/(1+\gamma)}|0,0\rangle+\frac{1}{\sqrt{1+\gamma}}|1\rangle A|0\rangle$ (one call each to $A,A^\dagger$), with $W=O(1/(\gamma\delta))$, $L\le 1+1/\gamma$. In the phase-estimation piece, the catalyst is a geometric sequence along a line with ratio $\gamma_k=\tan(\theta_k/2)$, $\theta_k=x_k+\pi/2-s$: it is normalizable exactly when $x_k<s$, and its norm blows up as $1/\delta$ near threshold. Reflections use $R(U)=|-\rangle\langle+|\otimes e^{i\sigma}U+\text{h.c.}$, i.e. $O(1)$ calls to $U$ per step. Binary search over $s$ gives the estimate.

**Why it matters** Phase estimation is ubiquitous; the authors argue the same transducer trick should remove logarithmic overheads elsewhere. The construction is simple enough (two reflections, a counter register) that constant factors may be competitive with QSVT-based resource estimates.

**Caveats** Requires a window promise (all eigenphases in $[0,\pi/2]$); costs $O(\log\frac{1}{\gamma\delta})$ ancillas versus $O(\log\frac1\delta)$ for standard approaches, an explicit open question. The $A$-count is optimal only up to $\log\frac1\delta\log\log\frac1\delta$. Constants are unoptimized and no numerical/resource-estimate comparison is given; whether the algorithm can be made fully coherent is left open. LLMs were used for some computations and proofs (authors state they verified all details).

## 3. Improved Quantum Codes with Transversal T Gates

[arXiv:2608.24000](https://arxiv.org/abs/2608.24000) · [SciRate](https://scirate.com/arxiv/2608.24000)

*Adam Wills*

**TL;DR** — This paper gives the first parameter improvements since 2017–18 for asymptotic families of CSS codes admitting a *strict* transversal T gate (physical T on every qubit → logical T on every logical qubit, no Clifford correction). The key tool is a closed-form distance formula for decreasing monomial codes punctured at a downward-closed set, instantiated with weighted Reed–Muller codes; it yields constant-rate codes with growing distance for the first time, hence the first transversal-T codes with magic-state-distillation exponent γ → 0 (previous best ≈ 0.678).

**The big picture** — Fault-tolerant quantum computers need a non-Clifford gate, and the cheapest way to get one is a code where applying the same simple gate to every physical qubit directly enacts that gate on every logical qubit. Codes with this property for the standard non-Clifford single-qubit gate have been stuck at essentially the same trade-off between how many logical qubits they store and how much error they tolerate for nearly a decade. This work broadens that trade-off substantially and, for the first time, produces families that store a constant fraction of their qubits as logical qubits while still improving error protection as they grow — which drives the asymptotic overhead of magic state distillation toward zero.

**Key contributions**
- Closed-form distance of a decreasing monomial code punctured at a *downset*: d = min over sets in the defining downset of the number of subsets of the complement not lying in the puncture set (valid under a stated non-annihilation condition). Likely of independent interest for polar/monomial codes.
- Explicit families with parameters [[n, Ω(n^{α+o(1)}), Ω(n^{β(α)+o(1)})]] with a new boundary β_explicit(α) strictly improving on Hastings–Haah for α > H₂(1/6).
- First constant-rate transversal-T codes: for any R ∈ (0,1/3), explicit [[n, (R+o(1))n, Ω(2^{(c_R+o(1))√log₂ n})]] with c_R = −Φ⁻¹(2R/(1+R)); hence γ = log(n/k)/log d → 0.
- A randomized "protected points" variant improving the non-explicit polynomial-regime frontier: β_exist = 1/2 for α ≤ 1/2, then linear down to 1−2H₂⁻¹(α).

**How it works** — Standard X-generator-matrix formalism: an 8-divisible binary code C, punctured at k coordinates Γ, gives a CSS code with k logicals and transversal T via the Ward identities; quantum distance equals the distance of punc_Γ(C^⊥). Instead of Reed–Muller, the author uses weighted Reed–Muller codes with weight vector (1,…,1,h), which retain 8-divisibility at much higher rate (up to the extreme Δ = 2^{[m−3]}, rate 1/8 in dimension). Choosing Γ itself to be a downset (low-Hamming-weight points in the first m−1 coordinates) makes the punctured distance computable exactly. The randomized variant excludes from Γ all points containing a hyperedge of a random t-uniform hypergraph that "covers" all y-sets, protecting distance while sacrificing few logical qubits.

**Why it matters** — Relevant to magic state distillation (T-to-T, no Clifford correction, so fast), and to concatenated/hierarchical architectures where non-LDPC outer codes are acceptable. Transversal T also immediately gives transversal *addressability* of lower Clifford-hierarchy gates, unlike CCZ-based constructions. The punctured-monomial machinery may feed into ongoing efforts to lower field sizes in product-expansion-based LDPC constructions.

**Caveats** — Codes are not LDPC. In the constant-rate regime the distance is only sub-polynomial (2^{Θ(√log n)}), so γ→0 without γ=0, and rate is capped below 1/3. The randomized construction gives no gain at constant rate. Results are confined to stabilizer/CSS codes; the author speculates non-stabilizer codes could do better. Explicitness of the hypergraph-protected family is not established.

## 4. Nearly Optimal Amplitude Estimation at any Depth

[arXiv:2608.24434](https://arxiv.org/abs/2608.24434) · [SciRate](https://scirate.com/arxiv/2608.24434)

*Jona Erle, Bálint Koczor*

**TL;DR** The paper introduces Windowed Least-Squares Amplitude Estimation (WLSAE): sample Grover-circuit depths from any "admissible" window distribution, then fit the Grover angle by minimizing a one-dimensional least-squares loss on a grid. For any tunable maximum depth, it provably attains the Zalka–Burchard-optimal tradeoff up to logs, *uniformly* over the whole angle range including the endpoints where previous depth-tunable methods either degrade to classical sampling or require amplitude-dependent depths.

**The big picture** Amplitude estimation is the workhorse behind quadratic speedups in Monte Carlo, finance, and chemistry, but the textbook version needs ancillas, controlled reflections, and deep coherent circuits that early fault-tolerant hardware cannot supply. A recent line of work trades depth for repetitions, but the guarantees quietly break down when the quantity being estimated is very close to zero or one — precisely the regime relevant to overlap certification and trial-state verification. This work shows that the breakdown is an artifact of the analysis, not of the algorithms: with a mild condition on how circuit depths are randomized, the quantum advantage survives all the way to the boundary, and the method needs no ancillas and no controlled operations.

**Key contributions**
- A general class of *admissible* windows on depths, defined by only two conditions: a lower bound on symmetrized mass at scale T = max(1, M/σ), and moment bounds up to eighth order (automatically satisfied by any window on the support).
- Theorem: any admissible window achieves |θ̂ − λ| ≤ ε with probability 1 − δ when M²N ≥ O(ε⁻² log(ε⁻¹δ⁻¹)), uniformly for λ ∈ [0, π/2], including λ → 0, π/2.
- Corollary: setting M = ⌊ε^{−1+β}⌋ gives O(ε^{−1−β} log) queries at depth ε^{−1+β}, continuously interpolating from classical sampling (β = 1) to Heisenberg scaling (β → 0).
- Shows the Gaussian window of GLSAE is a special case and that its "boundary patch" (which forfeits the speedup) is unnecessary; numerics show a plain uniform window outperforms the Gaussian.

**How it works** The estimator minimizes L(θ) = N⁻¹ Σ (Z_i − cos(2m_i θ))², where E[Z_m] = cos(2mλ) and Var[Z_m] = sin²(2mλ). The analysis proves matching upper/lower envelopes on the population loss, C₂Ψ² ≤ E ≤ C₁Ψ² with Ψ(Δ) = min(1, TΔ, T²Δ·max(λ̄, Δ)), λ̄ = min(λ, π/2 − λ). Near the boundary the curvature degenerates (quartic rather than quadratic), but the crucial observation is that the measurement variance degenerates in step: Bernstein concentration gives fluctuations bounded by a *smaller* envelope Ω containing the factor min(1, T²λ̄²). Signal-to-noise is therefore preserved, and a localization lemma plus a union bound over K ≈ A/ε grid points yields the uniform guarantee. Lower bounds on the loss for far-away θ use Dirichlet-kernel estimates.

**Why it matters** Provides a drop-in, ancilla-free, control-free amplitude estimation primitive with a rigorous, uniform, depth-tunable guarantee — directly relevant for early fault-tolerant Monte Carlo, overlap/fidelity certification, and verifying near-orthogonal trial states, where λ is small by construction.

**Caveats** The proof constants are enormous (A = 3C₈/8C₂ > 3×10⁶, and C₉ ≥ 8/3 amplifies further), so the stated sample complexities are not practically meaningful; the numerics (Q = 10⁶, λ = 0.5, 10⁴ runs) are the actual evidence for low overhead, and are shown only at a single interior λ in the excerpt available. Grid minimization costs O(NK) classically. No noise model or gate-error analysis is included.

## 5. Essentially optimal gate teleportation

[arXiv:2608.24345](https://arxiv.org/abs/2608.24345) · [SciRate](https://scirate.com/arxiv/2608.24345)

*Lukas Schmitt, David Sutter*

**TL;DR** The authors give the first explicit deterministic LOCC protocol that implements a two-qubit controlled-phase gate using strictly *less* than one ebit, with entanglement consumption h(q)+1−q for q=1/(1+sin(φ/2)), matched by a converse of h(q). The resource is a Schmidt-rank-3 state, the protocol uses four rounds and 4 bits of classical communication, and as an application a distributed 2n-qubit QFT can be done with a constant ~12.19 ebits instead of n² ebits.

**The big picture** Implementing a joint gate on two distant quantum computers normally costs at least one full unit of pre-shared entanglement, no matter how weakly entangling the gate is — a longstanding mismatch, since a nearly trivial rotation ought to cost nearly nothing. This work closes that gap for the controlled-phase family by exhibiting an explicit protocol whose entanglement cost shrinks continuously to zero as the rotation angle shrinks, together with a lower bound showing the protocol is close to optimal at every angle. Because such phase gates dominate the nonlocal cost of things like the quantum Fourier transform, this turns a cost that grew quadratically with system size into a constant, which matters directly for distributed and modular quantum architectures.

**Key contributions**
- Explicit deterministic sub-ebit gate teleportation protocol for U_φ=diag(1,1,1,e^{iφ}), resolving an open question raised by Eisert et al. and supported numerically by Stahlke–Griffiths.
- Achievability H = h(1/(1+s)) + s/(1+s), s=sin(φ/2), with a rank-3 resource state proved optimal *within* the protocol family (feasibility region sin²(φ/2)(1−2p₁)(1−2p₂) ≤ 4p₁p₂; entropy concavity argument puts the minimizer at a boundary).
- A simple converse H ≥ h(1/(1+s)) via Nielsen majorization applied to a cleverly chosen entangled input state that U_φ maps to a maximally entangled state.
- A substantially tighter converse for fixed Schmidt rank D, via SEP product-Kraus operators and a Binet–Cauchy determinant identity, implying every finite-rank resource requires a full ebit for some angles.
- Distributed QFT: constant 12.1869 ebits for all n vs. n²; plus extensions to arbitrary controlled two-qubit gates and (suboptimally) to arbitrary two-qubit unitaries via KAK.

**How it works** Alice entangles input, ancilla and her qutrit with a controlled unitary and measures one bit; conditioned on x (which occurs with probability 1/2 regardless of input, hence leaks nothing), Bob's register collapses to a two-dimensional subspace. Bob permutes, applies phases d_i, d_j solving a circle-intersection equation e^{iφ}(½−p_i+p_i d_i)=½−p_j+p_j d_j (the unitarity condition for Alice's later correction), Fourier-transforms and measures a trit. Alice then applies a determined unitary T=R⁻¹L, measures, and Bob applies a single diagonal phase fix; the amplitude-magnitude condition |c_z|=|k_z| makes the outcome exactly U_φ|Λ⟩ for all outcomes.

**Why it matters** Relevant to distributed quantum computing, entanglement-resource accounting, and circuit knitting: entanglement cost of nonlocal gates can now be tied to entangling power rather than to a coarse one-ebit quantum.

**Caveats** The achievability–converse gap of s/(1+s) remains open (tight only at φ→0 and φ=π); the rank-D converse shows rank-3 is genuinely suboptimal at larger angles. General two-qubit unitaries are handled by decomposing into three separate Pauli rotations, admittedly suboptimal. Costs are exact single-shot entropies; converting ebits into these non-maximally-entangled states is only asymptotically free, and noise robustness of the finely tuned resource state is not addressed.
