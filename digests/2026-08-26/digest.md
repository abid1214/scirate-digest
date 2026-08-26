# SciRate Daily Digest — 2026-08-26

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Optimal Lower Bound for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24493](https://arxiv.org/abs/2608.24493) · [SciRate](https://scirate.com/arxiv/2608.24493)

*Rolando D. Somma, Ronald de Wolf*

**TL;DR** The authors prove a joint lower bound of Ω(log(1/ε)/(γδ)) on the number of applications of the time-evolution unitary needed for guided ground-state energy estimation, closing the last open case (all three parameters simultaneously subconstant) and exactly matching the concurrent upper bound of Jeffery–Witteveen. The bound holds for a family with degenerate ground space in dimension log(1/ε)/γ², and — with an extra log(1/ε) factor in dimension — also for instances with a *unique*, δ-gapped ground state, plus it transfers to block-encoding access, fractional/continuous-time queries, ground-state *preparation*, and sum-of-squares spectral amplification (giving Ω(log(1/ε)/(γ√δ)) there).

**The big picture** Estimating the lowest energy of a quantum system is a flagship application of quantum computers, and the standard recipe assumes you can cheaply prepare a trial state that has some non-negligible overlap with the true ground state. The cost of such algorithms scales with three things: how accurate the answer must be, how good the trial state is, and how confident you want to be in the answer. Until now it was only known that the best-known algorithm is optimal when one of these three is held fixed; this paper shows it is optimal in all three at once, so no further improvement in the black-box setting is possible. A side observation is arguably more interesting: the hardest instances have trial states that carry no useful information about the ground state at all, suggesting the overlap condition is the wrong way to formalize "a helpful guess."

**Key contributions**
- Tight joint lower bound Ω(log(1/ε)/(γδ)); previously only single-parameter-tight bounds were known.
- A fractional-query polynomial method lemma: T queries to e^{iπφx} yield a degree-O(Tφ + log(1/ε)) polynomial ε-approximating the acceptance probability. The *additive* log(1/ε) term is what buys the tight error dependence, and it generalizes any polynomial lower bound for phase queries to fractional queries.
- A second hard family with unique ground state and spectral gap 3δ, based on rank-one phase rotations about √a|0⟩ + ω√(1−a)|j⟩.
- Corollaries: block-encoding model, ground-state preparation to trace distance ε, and near-optimality of SOSSA when the square-root operator is treated as a black box.

**How it works** For the first family, H = diag(0, {3δ·x_j}), so U is a (3δ/π)-fractional phase query to x; distinguishing x=0 from |x| ≥ γ²N is OR. Expanding U into I and the ordinary phase oracle and truncating past K = O(Tδ + log(1/ε)) oracle terms costs only ε in operator norm. Symmetrizing, Coppersmith–Rivlin lifts the bound from integer points to the real interval, and Chebyshev extremality gives error ≥ 2^{−O(D²/N + Dγ)}; setting N = log(1/ε)/γ² yields the bound. The unique-ground-state family splits into two cases (a search-style Ω(√N/δ) bound versus a Chebyshev argument in the amplitude a), balanced at N = log(1/ε)²/γ².

**Why it matters** Ground-state energy estimation is the dominant cost driver in quantum chemistry pipelines, and subroutine error reduction (where subconstant ε is unavoidable) has no general cheap transducer-style fix for multi-output subroutines. This settles the query complexity and certifies SOSSA's quadratic-in-δ speedup as near-optimal.

**Caveats** The bounds require dimension growing as log(1/ε)/γ² (or its square), so they say nothing about low-dimensional instances. The sparse-access model — arguably the most physically relevant — remains open, and the hard Hamiltonians are 1- or 2-sparse, so no d-dependence is captured. Only U-queries are counted; A is free. Notably, the authors credit ChatGPT 5.6 Pro with generating both hard families and initial (long, largely correct) proofs, later simplified by hand.

## 2. Optimal Quantum Algorithm for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24494](https://arxiv.org/abs/2608.24494) · [SciRate](https://scirate.com/arxiv/2608.24494)

*Stacey Jeffery, Freek Witteveen*

**TL;DR** — The authors give a quantum algorithm for guided ground-state energy / maximum-eigenphase estimation that uses $O(1/(\gamma\delta))$ (controlled) calls to the evolution/walk unitary $U$ and only $O(\tfrac1\gamma\log\tfrac1\delta\log\log\tfrac1\delta)$ calls to the guiding-state preparation $A$, removing the long-standing $\log\frac1\gamma$ overhead of QPE- and QSVT-based approaches. This matches the $\Omega(1/(\gamma\delta))$ lower bound of Mande–de Wolf, settling their open question; combined with a concurrent lower bound of Somma et al., the query complexity is $\Theta(\tfrac{1}{\gamma\delta}\log\tfrac1\epsilon)$.

**The big picture** — Estimating the lowest energy of a quantum system, given a trial state with some guaranteed overlap with the true ground state, is the workhorse subroutine for fault-tolerant quantum chemistry and materials simulation. Every known method paid a logarithmic penalty in the inverse overlap, because both phase estimation and polynomial-filter methods must suppress spurious signal below the overlap level before amplitude amplification can be applied. This work shows that penalty is avoidable entirely, by building the algorithm in the "transducer" framework, where bounded-error subroutines are replaced by exactly-composable objects so no error-reduction repetitions are needed. The result closes the gap to the known lower bound and could shave a real constant-to-logarithmic factor off resource estimates for practical simulation.

**Key contributions**
- Query-optimal algorithm for the guided max-eigenphase / ground-state-energy problem; time-evolution time $O(\lambda/(\gamma\delta))$.
- An *exact* transducer for decision amplitude amplification (a two-reflection walk on a weighted star, with $W\le w/\epsilon$ or $1/w$; $w=\gamma$ balances both).
- An exact transducer for *decision* phase estimation (deciding $x \gtrless \tilde s$ for an eigenstate), as a walk on infinite geometrically-weighted lines with ratio $\gamma_k=\tan(\theta_k/2)$, $\theta_k = x_k+\pi/2-\tilde s$; convergence of the catalyst series encodes the answer.
- A general "exact truncation" lemma showing the infinite counter register can be cut at level $D$ without any error if the transducer raises the level by at most $m$ per application and $Km<D$.
- Avoids quantum random-access gates, which the generic algorithm-to-transducer conversion would require.

**How it works** — The composed canonical transducer $S(O)=S^\circ O$ acts as $\ket{\bar1,0}\rightsquigarrow \pm\ket{\bar1,0}$, with the sign deciding the threshold problem; single-bit phase estimation reads it out. Its transduction complexity is $W=O(1/(\gamma\delta))$ while its Las Vegas query complexity with respect to the oracle $O_\gamma(A)=I-2\ket{\varphi_\gamma}\bra{\varphi_\gamma}$ is only $L\le 1+1/\gamma$ — the oracle acts on only a small part of the catalyst, so it is invoked once per $W/L$ steps. Reflections are implemented via $R(U)=\ket-\bra+\otimes e^{i\sigma}U + \ket+\bra-\otimes e^{-i\sigma}U^\dagger$, i.e. $O(1)$ calls to $U,U^\dagger$ per iteration. Binary search over thresholds yields the estimation result.

**Why it matters** — Phase estimation is ubiquitous; the authors argue similar transducer-based log-factor removals should apply elsewhere. The construction is simple enough that constants are plausibly competitive with state-of-the-art resource estimates.

**Caveats** — Requires the window promise (all eigenphases in $[0,\pi/2]$), easy to arrange but assumed. Space overhead is $O(\log\frac{1}{\gamma\delta})$ ancillas versus $O(\log\frac1\delta)$ for standard approaches. Constants are unoptimized and no numerical resource estimate is given. Calls to $A$ are optimal only up to $\log\frac1\delta\log\log\frac1\delta$. Full coherence of the subroutine (relevant for use inside larger algorithms) is left open. The authors disclose LLM use for some proofs and computations.

## 3. Improved Quantum Codes with Transversal T Gates

[arXiv:2608.24000](https://arxiv.org/abs/2608.24000) · [SciRate](https://scirate.com/arxiv/2608.24000)

*Adam Wills*

**TL;DR** — This paper builds new families of CSS codes on which physical $T^{\otimes n}$ implements logical $\bar T^{\otimes k}$ exactly (no Clifford correction), improving on Hastings–Haah (2017) and Haah (2018) for the first time in eight years. The key tool is a closed-form distance formula for decreasing monomial codes punctured at a *downward-closed* set of hypercube points; instantiating it with weighted Reed–Muller codes gives constant-rate families with growing distance $d=\Omega(2^{(c_R+o(1))\sqrt{\log_2 n}})$, $c_R=-\Phi^{-1}(2R/(1+R))$ for any rate $R<1/3$ — the first transversal-$T$ codes with magic-state-distillation exponent $\gamma\to 0$.

**The big picture** — Fault-tolerant quantum computers need a non-Clifford gate, and the cheapest way to get one is a code where applying the same simple gate to every physical qubit directly enacts that gate on every logical qubit. Such codes are hard to build, and the best known families had been stuck for years, forcing magic state distillation to pay a large qubit overhead per distilled resource. This work substantially enlarges the space of achievable rate–distance trade-offs and, for the first time, produces families whose relative overhead per output vanishes asymptotically, by recognising that puncturing algebraic evaluation codes at a specially structured set of points keeps the distance under tight control.

**Key contributions**
- Closed form: for downsets $\Delta,\Gamma$, $d(\mathrm{punc}_\Gamma(C(\Delta)))=\min_{A\in\Delta}|\{V\subseteq\bar A: V\notin\Gamma\}|$, valid under a "non-annihilation" condition — new even classically (polar-code relevance).
- Explicit polynomial-regime frontier $\beta_{\rm explicit}(\alpha)$ (Thm 1), strictly beating the previous explicit boundary for $\alpha>H_2(1/6)$.
- Explicit constant-rate, growing-distance transversal-$T$ codes (Thm 2) — previously unknown even allowing Clifford corrections; yields $\gamma=\log(n/k)/\log d\to0$, versus $\gamma\approx0.678$ before.
- Randomised construction improving the non-explicit frontier $\beta_{\rm exist}(\alpha)$ (Thm 3), e.g. $\beta=1-2H_2^{-1}(\alpha)$ for $\alpha\ge H_2(1/3)$.

**How it works** — Strict transversal $T$ follows (via Ward's identities) from an 8-divisible binary code $C$ whose generator matrix is put in semi-systematic form on a puncture set $\Gamma$; $k=|\Gamma|$, and $d=d(\mathrm{punc}_\Gamma(C^\perp))$. Reed–Muller codes with $3r<m$ are 8-divisible but low rate; the author instead uses weighted Reed–Muller downsets with weight vector $(1,\dots,1,h)$, which raise the classical rate while retaining 8-divisibility, and punctures at the downset $\Gamma=\{A\subseteq[m-1]:|A|\le w\}$. Duality of downsets ($\Delta^\perp=\{A:\bar A\notin\Delta\}$) turns the quantum distance into $\min_{A\notin\Delta}|2^A\setminus\Gamma|$. The randomised variant "protects" points from puncturing using a random $t$-uniform hypergraph covering all $y$-sets, sacrificing few logical qubits for a distance boost.

**Why it matters** — Directly improves distillation-to-$T$ protocols (no Clifford correction means fast, clean $T\to T$ routines), and supplies target parameters/structural lessons for the active push toward LDPC codes with transversal non-Clifford gates. Also gives transversal $R_\ell$ gates, hence transversally *addressable* lower-hierarchy gates.

**Caveats** — Codes are not LDPC; they are meant for concatenated/logical-level use. Constant-rate distance is only $2^{\Theta(\sqrt{\log n})}$ — sub-polynomial — and confined to $R<1/3$; $\gamma\to0$ but never $0$ (asymptotically good transversal-$T$ codes remain open). The randomised construction gives nothing in the constant-rate regime. Analysis is asymptotic; no finite-length or fault-tolerance-threshold numbers. Restricted to stabiliser/CSS codes, which the author suspects is itself suboptimal.

## 4. Nearly Optimal Amplitude Estimation at any Depth

[arXiv:2608.24434](https://arxiv.org/abs/2608.24434) · [SciRate](https://scirate.com/arxiv/2608.24434)

*Jona Erle, Bálint Koczor*

**TL;DR** This paper introduces Windowed Least Squares Amplitude Estimation (WLSAE): sample Grover-circuit depths from a probability distribution ("window") over a symmetric index set, collect ±1 outcomes whose conditional mean is cos(2mλ), and estimate the Grover angle by minimizing a one-dimensional least-squares loss over a uniform grid. For any window in an explicitly characterized "admissible" class, they prove the near-optimal depth–query tradeoff M²N ∈ Õ(ε⁻²) for additive error ε *in the angle λ*, uniformly over all λ ∈ [0, π/2] — including the boundaries λ→0, π/2 where prior depth-tunable schemes degrade to classical sampling.

**The big picture** Amplitude estimation is the workhorse behind quadratic quantum speedups for Monte Carlo, finance, and chemistry, but the textbook version needs coherent control, ancillas, and a Fourier transform that early fault-tolerant machines cannot afford. A line of recent "low-depth" variants trades circuit depth for repetitions, but their optimality guarantees quietly break down when the amplitude being estimated is very close to zero or one — exactly the regime relevant to overlap certification and trial-state verification. This work shows that a simple recipe — randomize the circuit depth according to a well-chosen distribution and fit the resulting outcomes by least squares — recovers the optimal tradeoff everywhere, with no ancillas and no controlled Grover operations, and it identifies a whole family of usable depth distributions rather than a single one.

**Key contributions**
- A window-admissibility criterion: a mass condition p(m)+p(−m) ≥ b/T for 1 ≤ m ≤ T (with T = max(1, M/σ)) plus moment bounds up to 8th order, which are automatically satisfied by any window on the support.
- Theorem: every admissible window achieves |θ̂ − λ| ≤ ε with probability 1−δ using M²N ∈ O(ε⁻² log(ε⁻¹δ⁻¹)), matching the Zalka–Burchard lower bound up to logs, *uniformly in λ* — a strictly stronger guarantee than uniform additive accuracy in the amplitude a.
- Corollary: setting M = ⌊ε^(−1+β)⌋ interpolates continuously across β ∈ [0,1] from classical sampling to the Heisenberg limit, with MN ∈ Õ(ε^(−1−β)) queries.
- Shows the boundary "fallback to classical sampling" patch in GLSAE (the Gaussian member of this family) is unnecessary and in fact discards the speedup where it is invoked.
- Numerics: at fixed budget Q = 10⁶, a plain uniform window beats the Gaussian window and tracks the Cramér–Rao bound.

**How it works** The population loss ℰ^(λ)(θ) is sandwiched between constant multiples of an envelope Ψ(Δ)² = min(1, TΔ, T²Δ·max(λ̄, Δ))², where λ̄ = min(λ, π/2−λ) captures boundary proximity — this is what makes the analysis uniform. Lower bounds near λ use the sin²(x) ≥ 4x²/π² inequality and partial sums of m⁴; the "far" regime uses Dirichlet-kernel bounds to show ℰ ≥ 4b/243. Bernstein's inequality with variance V and range B both scaled by the same envelope, plus a union bound over K = ⌈Aπ/2ε⌉ grid points, controls the empirical fluctuation, and a localization lemma converts this into |θ̂ − λ| ≤ ε.

**Why it matters** For early fault-tolerant hardware, depth is the binding constraint; this gives a provably optimal, ancilla-free, control-free knob to spend whatever depth is available, with guarantees that survive at extreme amplitudes — precisely the regime for certifying that a prepared state has small overlap with a target.

**Caveats** The proven constants are enormous: A = 3C₈/(8C₂) > 3×10⁶, forcing a grid of ~10⁶/ε points in the worst-case bound, so the theorem is asymptotic in spirit and the practical claim rests on numerics (single λ = 0.5, one budget shown in the excerpt). The guarantee is for a grid minimizer, not a continuous optimizer, and assumes an exact noiseless Loschmidt-echo/reflection measurement model; the polylog gap to the Zalka–Burchard bound remains.

## 5. Essentially optimal gate teleportation

[arXiv:2608.24345](https://arxiv.org/abs/2608.24345) · [SciRate](https://scirate.com/arxiv/2608.24345)

*Lukas Schmitt, David Sutter*

**TL;DR** For the two-qubit controlled-phase gate $U_\phi=\mathrm{diag}(1,1,1,e^{i\phi})$, the authors give an explicit deterministic LOCC protocol using a Schmidt-rank-3 resource state costing $h(q)+1-q$ ebits with $q=1/(1+\sin(\phi/2))$, plus a majorization converse of $h(q)$ ebits. This is the first deterministic gate teleportation consuming strictly less than one ebit, with cost vanishing as $\phi\to0$ and matching the converse to leading order at small angles.

**The big picture** Implementing a joint operation on two distant quantum systems normally consumes at least one unit of shared entanglement, even when the operation itself is barely entangling — a mismatch that is wasteful for distributed quantum computing, circuit cutting, and modular architectures. This work closes that gap for the most common family of two-qubit gates: the entanglement consumed now scales down smoothly with how weakly entangling the gate is, and comes within a small factor of an information-theoretic lower bound at every angle. As a headline consequence, a distributed quantum Fourier transform split across two parties can be done exactly with a constant amount of entanglement, independent of the number of qubits, rather than an amount growing quadratically.

**Key contributions**
- An explicit four-round LOCC protocol (4 bits of classical communication: 1+2+1) implementing $U_\phi$ exactly and deterministically with a rank-3 resource state $\sqrt{q}\ket{00}+\sqrt{(1-q)/2}(\ket{11}+\ket{22})$.
- Proof that this is the optimal rank-3 state for the protocol: the feasibility region is characterized by $\sin^2(\phi/2)(1-2p_1)(1-2p_2)\le 4p_1p_2$, and entropy is concave along the equality curve, so the optimum sits at a boundary point.
- A converse $H\ge h(q)$ via Nielsen majorization, using the witness input $\tfrac12(\ket{00}+\ket{01}-e^{i\phi}\ket{10}+\ket{11})$ (Schmidt spectrum $\tfrac{1\pm\sin(\phi/2)}{2}$), which the gate maps to a maximally entangled state — forcing $p_0\le q$.
- A strictly tighter converse for fixed Schmidt rank $D$, derived from SEP product-Kraus determinant identities (Binet–Cauchy plus an adjugate derivative trick), yielding $\sin(\phi/2)(2p_0-1)\le 2\sum_{1\le i<j}\sqrt{p_ip_j}$; it shows every finite-rank resource needs a full ebit for some angles.
- Extensions: any controlled two-qubit unitary reduces to some $U_\phi$; general two-qubit unitaries via KAK cost at most the sum over the three Pauli-rotation angles.
- Application: exact bit-reversed QFT on $2n$ qubits split $n{:}n$ costs $\le 12.1869$ ebits for all $n$, versus $n^2$ with the standard one-ebit-per-gate construction.

**How it works** Alice's first unitary, controlled on her input qubit, coherently collapses the qutrit resource onto a two-dimensional subspace with an unbiased outcome (probability $1/2$ regardless of input), leaking nothing. Bob applies a permutation, a diagonal phase $\mathrm{diag}(1,d_{i_x},d_{j_x})$ that injects the nonlocal phase, and a qutrit Fourier transform before measuring — the Fourier basis prevents him learning Alice's branch. Alice's third-round unitary is fixed by requiring that the map $T_{x,y}=R^{-1}L$ relating the two branches be unitary; that condition is exactly the intersection of two circles in the complex plane, which is solvable precisely under the feasibility inequality. Bob's final diagonal correction fixes residual phases, using $|c_z|=|k_z|$.

**Why it matters** It settles a question open since Eisert et al. (2000), turns entanglement cost into a continuous function of gate strength, and gives a directly implementable recipe (rank-3 state, 4 classical bits) relevant to distributed/modular quantum computing and to entanglement-assisted circuit knitting.

**Caveats** A gap remains between $h(q)+1-q$ and $h(q)$; only small $\phi$ is near-tight, and above the crossover one reverts to the one-ebit protocol. The multi-qubit/general-unitary extension is admittedly suboptimal since it teleports the three KAK rotations separately. No noise or approximate-implementation analysis. The authors acknowledge an LLM ("GPT 5.6 Sol") in developing both the protocol and the tighter converse — the correctness proofs are self-contained, but readers may want to verify independently.
