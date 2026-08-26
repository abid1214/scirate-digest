# SciRate Daily Digest — 2026-08-26

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Optimal Lower Bound for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24493](https://arxiv.org/abs/2608.24493) · [SciRate](https://scirate.com/arxiv/2608.24493)

*Rolando D. Somma, Ronald de Wolf*

**TL;DR** The paper proves an Ω(log(1/ε)/(γδ)) query lower bound for guided ground-state energy estimation, matching the very recent transducer-based upper bound of Jeffery–Witteveen and settling the joint dependence on all three parameters (precision δ, guiding-state overlap γ, failure probability ε), which was open. The bound holds both for degenerate ground spaces (dimension ≳ log(1/ε)/γ²) and for the more physically relevant unique-ground-state, spectrally gapped case (dimension ≳ log(1/ε)²/γ²), and carries over to block-encodings, continuous-time/fractional simulation, ground-*state* preparation, and sum-of-squares spectral amplification (where it gives Ω(log(1/ε)/(γ√δ))).

**The big picture** Estimating the lowest energy of a quantum system is the workhorse subroutine of quantum chemistry algorithms, and the dominant cost is how many times one must run the time evolution. Algorithms exploit a cheaply preparable trial state that has some guaranteed overlap with the true ground state, and their cost scales with the desired accuracy, that overlap, and the tolerated failure probability. Prior lower bounds only pinned down the cost when one of these three knobs was held fixed; this work shows the known algorithm is simultaneously optimal in all three, meaning no further speedup is possible in this access model — including no cheap trick for driving the failure probability down, in contrast to Grover search where error reduction is nearly free.

**Key contributions**
- Joint lower bound Ω(log(1/ε)/(γδ)), tight in ε, closing the open question of [Mande–de Wolf 2026].
- A second hard family with a *unique* ground state and spectral gap 3δ achieving the same bound (at the cost of a log(1/ε) factor in dimension).
- A polynomial-method lemma for *fractional* phase queries: T queries at fraction φ yield a degree-O(Tφ + log(1/ε)) approximating polynomial — a generic recipe for lifting phase-query lower bounds by a 1/δ factor.
- Corollaries: block-encoding access, ground-state preparation in trace distance, and near-optimality of SOSSA.

**How it works** Hard family 1: H = diag(0, {3δ·xⱼ}), so U = e^{iH} is a (3δ/π)-fractional phase oracle for x; distinguishing x = 0ⁿ from |x| ≥ γ²N is OR. Expanding U^{±φ} = c₊I + c₋O_x and truncating terms with more than K = O(Tφ + log(1/ε)) oracle factors gives an operator-norm error ≤ ε/3, hence a degree-2K polynomial ε-approximating the acceptance probability. Symmetrization plus Coppersmith–Rivlin (integer-grid → interval) plus Chebyshev extremality yields error ≥ 2^{−O(D²/N + Dγ)}; setting N = log(1/ε)/γ² forces T = Ω(log(1/ε)/(γδ)). Family 2 replaces the oracle by U = I + (e^{iθ}−1)|ψ⟩⟨ψ| with |ψ⟩ = √a|0⟩ + ω√(1−a)|j⟩, decomposed via the reflection R_ψ; averaging over the sign ω kills odd powers of √(a(1−a)), giving a univariate polynomial in a. A case split on p(0,3δ) yields either the Ω(√N/δ) search bound or the Chebyshev bound; N = log(1/ε)²/γ² balances them.

**Why it matters** Ends the search for better guided ground-state energy algorithms in the U/block-encoding model, and validates SOSSA's quadratic gain as essentially optimal for black-box G. Relevant to anyone costing out chemistry pipelines or using GSEE as an inner subroutine.

**Caveats** Bounds require Hilbert-space dimension polynomial in 1/γ and log(1/ε); they do not apply to the *sparse-access* model (the hard Hamiltonians are 1- or 2-sparse but the reduction fails), an explicit open problem. Only queries to U are counted; A is free. Tellingly, both hard families use guiding states carrying no information about the ground state beyond raw overlap, which the authors argue means the overlap-based problem formulation may itself be the wrong abstraction. Note also the disclosed heavy use of ChatGPT 5.6 Pro in constructing the hard families and initial (20+ page) proofs, subsequently simplified by the authors.

## 2. Optimal Quantum Algorithm for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24494](https://arxiv.org/abs/2608.24494) · [SciRate](https://scirate.com/arxiv/2608.24494)

*Stacey Jeffery, Freek Witteveen*

**TL;DR** The authors give a quantum algorithm for guided max-eigenphase (equivalently guided ground-state energy) estimation that uses $O(1/(\gamma\delta))$ controlled calls to the evolution/walk unitary $U$ and $O(\tfrac{1}{\gamma}\log\tfrac1\delta\log\log\tfrac1\delta)$ calls to the state-preparation unitary $A$, shaving the $\log(1/\gamma)$ factor that all previous QPE- and QSVT-based approaches incurred. This matches the $\Omega(1/(\gamma\delta))$ lower bound of Mande–de Wolf, settling their open question; the key tool is Belovs' transducer framework.

**The big picture** Estimating the lowest energy of a quantum system, given a trial state with some guaranteed overlap with the true ground state, is the canonical fault-tolerant quantum chemistry primitive, and its cost is dominated by how long one must simulate the system's dynamics. Every prior method paid a small but real penalty because the underlying subroutines — phase estimation or polynomial filtering — must suppress their own error below the level of the overlap signal before they can be amplified. This work removes that penalty entirely by building the algorithm out of "transducers," a recently developed way of composing quantum subroutines that behave exactly rather than approximately, so no error-suppression overhead accumulates. The resulting query cost is now provably optimal, closing a long-standing gap between the best algorithm and the best lower bound.

**Key contributions**
- Optimal query complexity for guided max-eigenphase estimation; combined with the concurrent lower bound of Somma et al., the answer is $\Theta(\tfrac{1}{\gamma\delta}\log\tfrac1\varepsilon)$ for large enough dimension.
- An explicit, gate-model-friendly transducer for *decision amplitude amplification* (a quantum walk on a star graph with a tunable boundary weight $w=\gamma$).
- An explicit infinite-dimensional transducer for *decision phase estimation* — a weighted walk on parallel half-lines with edge ratios $\gamma_k=\tan(\theta_k/2)$, reflections implementable with $O(1)$ controlled calls to $U,U^\dagger$.
- A general lemma (exact $(D,m)$-truncation) showing the infinite counter register can be truncated to $O(\log D)$ qubits with *zero* error, generalizing an argument of Belovs' purifier paper.

**How it works** The threshold problem — distinguish $\|\Pi_{>s}\ket\psi\|\ge\gamma$ from $\|\Pi_{>s-\delta}\ket\psi\|=0$ — is solved by a single canonical transducer $S=S^\circ O$ whose transduction action is $\ket{\bar1,0}\mapsto\pm\ket{\bar1,0}$, the sign encoding the answer, read out by single-bit phase estimation. Its transduction complexity is $W=O(1/(\gamma\delta))$ (controlling calls to $S^\circ$, hence to $U$), while its Las Vegas query complexity with respect to the oracle $O_\gamma(A)=I-2\ket{\varphi_\gamma}\bra{\varphi_\gamma}$ is only $L\le 1+1/\gamma$, so $A$ is queried a factor $\delta$ less often. Binary search over $s$ yields the estimate.

**Why it matters** Phase estimation is the workhorse of fault-tolerant algorithms; the authors argue the construction is simple with modest constants, so it plausibly beats state-of-the-art QSVT resource estimates, and suggest transducers can strip similar logarithmic factors elsewhere.

**Caveats** Requires a "window promise" (all eigenphases in $[0,\pi/2]$), easy to arrange but assumed throughout. Space overhead is $O(\log\tfrac{1}{\gamma\delta})$ ancillas versus $O(\log\tfrac1\delta)$ for the standard approach — the authors ask whether this can be reduced. The $A$-query count is optimal only up to $\log\tfrac1\delta\log\log\tfrac1\delta$. Constants are unoptimized and no numerical resource estimate is given. Full coherence (avoiding the classical binary-search outer loop) is left open. The authors disclose LLM assistance in some proofs and computations.

## 3. Improved Quantum Codes with Transversal T Gates

[arXiv:2608.24000](https://arxiv.org/abs/2608.24000) · [SciRate](https://scirate.com/arxiv/2608.24000)

*Adam Wills*

**TL;DR** — This work gives the first improvement since 2017–2018 in the asymptotic parameters of quantum CSS codes admitting a strictly transversal $T$ gate (physical $T^{\otimes n}$ ⇒ logical $\bar T^{\otimes k}$, no Clifford correction). Using 8-divisible *decreasing monomial* codes punctured at a *downward-closed* set of hypercube points, the author obtains a closed-form distance formula for such punctures and constructs, for the first time, constant-rate families ($R<1/3$, $d=\Omega(2^{(c_R+o(1))\sqrt{\log_2 n}})$, $c_R=-\Phi^{-1}(2R/(1+R))$), yielding magic-state-distillation overhead exponent $\gamma\to 0$ with a transversal $T$ gate — beating Hastings–Haah's $\gamma\approx0.678$.

**The big picture** — Fault-tolerant quantum computers need a non-Clifford gate, and the cheapest way to get one is a code where applying the same simple gate to every physical qubit directly performs that gate on every logical qubit. Codes with this property for the standard single-qubit non-Clifford gate have stubbornly poor parameters, forcing large overheads in magic state distillation. This paper substantially widens the achievable rate–distance trade-off and, for the first time, gets a constant fraction of the qubits to be logical while the distance still grows, meaning the distillation overhead exponent can be driven to zero.

**Key contributions**
- A closed-form distance for a decreasing monomial code punctured at a downset: $d=\min_{A\in\Delta}|\{V\subseteq \bar A: V\notin\Gamma\}|$, valid under a "non-annihilation" condition; of independent interest for polar/evaluation codes.
- Explicit families beating prior polynomial-rate/distance frontiers (Thm. 1.4: $\beta_{\text{explicit}}(\alpha)=(1-2q^*(\alpha))/3$ above $\alpha=H_2(1/6)$).
- First constant-rate, growing-distance transversal-$T$ codes; first $\gamma\to0$ for transversal $T$ (even allowing Clifford corrections / triorthogonality).
- A randomized "protected-point" variant improving the non-explicit frontier ($\beta_{\text{exist}}$, e.g. $1-2H_2^{-1}(\alpha)$ for $\alpha\ge H_2(1/3)$).

**How it works** — In the standard $X$-generator-matrix formalism, transversal $T$ follows from an 8-divisible classical code $C$ plus a puncture set $\Gamma$ carving out logical qubits; the quantum distance equals $d(\mathrm{punc}_\Gamma(C^\perp))$. Instead of Reed–Muller, the author uses weighted Reed–Muller downsets with weights $(1,\dots,1,h)$, which remain 8-divisible while achieving much larger (even constant) rate; taking $h>1$ helps in the high-rate regime. Choosing $\Gamma$ itself to be a downset (low-Hamming-weight points in the first $m-1$ variables) makes the punctured distance exactly computable and $\Gamma\subseteq\Delta$ guarantees non-annihilation. The randomized version protects points containing any hyperedge of a random $t$-uniform hypergraph that covers all $y$-sets, sacrificing few logical qubits to save distance.

**Why it matters** — Relevant to magic state distillation (fast $T$-to-$T$ protocols, no Clifford correction needed), concatenated/hierarchical architectures where LDPC-ness isn't required, and as a technical input to the ongoing search for qLDPC codes with transversal non-Clifford gates; the punctured-evaluation-code distance lemma may help reduce field sizes in product-expansion constructions.

**Caveats** — Codes are non-LDPC and must be run at the logical level of another code. Constant-rate distance grows only as $2^{\Theta(\sqrt{\log n})}$ (sub-polynomial), and rate is capped below $1/3$; at low rates the new constructions do not beat Hastings–Haah/Haah. The randomized construction is non-explicit and gives no gain at constant rate. Restricted to stabiliser (CSS) codes; the author suspects non-stabiliser codes could do better. Distillation error-suppression constants and finite-size performance are not analyzed.

## 4. Nearly Optimal Amplitude Estimation at any Depth

[arXiv:2608.24434](https://arxiv.org/abs/2608.24434) · [SciRate](https://scirate.com/arxiv/2608.24434)

*Jona Erle, Bálint Koczor*

**TL;DR** The paper introduces Windowed Least Squares Amplitude Estimation (WLSAE): sample Grover-circuit depths from a probability distribution ("window") over $\{-M,\dots,M\}$, then fit the angle by minimizing a one-dimensional squared loss over a grid. For any window in an explicitly characterized "admissible" class, the estimator provably achieves $M^2N \in \tilde{O}(\epsilon^{-2})$ error in the Grover angle *uniformly* over $\lambda\in[0,\pi/2]$ — including the boundaries $\lambda\to 0,\pi/2$ where all prior depth-tunable schemes lose the speedup — with no ancillas and no controlled Grover operators.

**The big picture** Amplitude estimation is the workhorse subroutine behind quadratic speedups for Monte Carlo, finance, chemistry and optimization, but the textbook version needs deep coherent circuits, ancilla registers and a Fourier transform that early fault-tolerant hardware cannot supply. A line of recent work trades circuit depth for repetitions, but the guarantees quietly break down when the amplitude being estimated is very close to zero or one — exactly the regime relevant to overlap certification and trial-state verification — where the methods silently degrade to classical sampling. This work shows that a simple randomized-depth-plus-least-squares recipe retains the full depth-versus-repetition optimality across the entire range of amplitudes, and that the previously proposed special-case patch at the boundary is unnecessary and in fact wasteful.

**Key contributions**
- A window-class abstraction: admissibility requires only a symmetrized mass lower bound $p(m)+p(-m)\ge b/T$ for $1\le m\le T$ plus moment bounds $\mathbb{E}[m^{2k}]\le C T^{2k}$ (the latter is automatic).
- A uniform-in-$\lambda$ proof that any admissible window attains $M^2N\in O(\epsilon^{-2}\log(\epsilon^{-1}\delta^{-1}))$, matching Zalka–Burchard up to logs, continuously interpolating $M=1$ to $M=\Theta(\epsilon^{-1})$ (with $M=\epsilon^{-1+\beta}$ giving $MN = \tilde O(\epsilon^{-1-\beta})$ queries).
- Shows GLSAE's Gaussian window is one member; its boundary fallback is provably superfluous.
- Numerics over five windows (Gaussian, Kaiser, uniform, linear, cubic) at $Q=10^6$: the plain uniform window beats the Gaussian, approaching the Cramér–Rao bound.

**How it works** Population loss $\mathcal{E}^{(\lambda)}(\theta)=\mathbb{E}_m[(\cos 2m\lambda-\cos 2m\theta)^2]$ is sandwiched, $C_2\Psi^2\le\mathcal{E}\le C_1\Psi^2$, with envelope $\Psi(\Delta)=\min(1,T\Delta,T^2\Delta\max(\bar\lambda,\Delta))$ — near the boundary the loss becomes quartic rather than quadratic in $\Delta$, which alone would kill the rate. The fix: a Bernstein bound whose variance profile $\Omega$ inherits the factor $\sin^2(2m\lambda)$, so the shot noise vanishes at the same rate the curvature flattens. A localization lemma then guarantees the grid minimizer lies within $A\kappa$ of $\lambda$ once $T/\sqrt{r}\ge C_9/\kappa$, with $r=\log(2K/\delta)/N$ and $K=\lceil A\pi/2\epsilon\rceil$.

**Why it matters** Directly relevant to early-fault-tolerant algorithm designers: the circuits are powers of $G$ plus one reflection, measured via a shifted Loschmidt echo, with tunable depth set by hardware coherence. Small-amplitude overlap certification now keeps its quadratic advantage.

**Caveats** The proven constants are astronomical ($A>3\times10^6$, so $K$ and the grid search are enormous); the practical claims rest entirely on numerics at a single $\lambda=0.5$ and fixed budget, not at the boundary the theory is about. Query cost is bounded by $MN$ rather than the (smaller) $N\mathbb{E}|m|$; analysis assumes noiseless circuits and exact i.i.d. sampling; classical grid minimization scales as $O(\epsilon^{-1})$.

## 5. Essentially optimal gate teleportation

[arXiv:2608.24345](https://arxiv.org/abs/2608.24345) · [SciRate](https://scirate.com/arxiv/2608.24345)

*Lukas Schmitt, David Sutter*

**TL;DR** The authors give an explicit deterministic LOCC protocol implementing the two-qubit controlled-phase gate $U_\phi=\mathrm{diag}(1,1,1,e^{i\phi})$ using a Schmidt-rank-3 resource state costing $h(q)+1-q$ ebits with $q=1/(1+\sin(\phi/2))$, plus a majorization converse of $h(q)$. This is the first protocol to break the one-ebit barrier for non-Clifford gate teleportation, with cost vanishing as $\phi\to0$; as an application, a distributed $2n$-qubit QFT needs only $\approx 12.19$ ebits total instead of $n^2$.

**The big picture** Two distant parties can apply a joint quantum gate without ever interacting directly, by consuming pre-shared entanglement and exchanging classical messages. Until now, every known exact, deterministic protocol burned at least one full unit of entanglement, even for gates that barely entangle anything — which is wasteful and clearly not fundamental. This work exhibits a protocol whose entanglement cost shrinks continuously to zero as the gate's rotation angle shrinks, and proves a nearly matching lower bound, so weak interactions between distant registers can be simulated with correspondingly weak entanglement. This changes the resource accounting for distributed and modular quantum computing, where circuits like the Fourier transform are dominated by many tiny-angle nonlocal rotations.

**Key contributions**
- Explicit 4-round protocol (4 bits of classical communication, qutrit-level resource) achieving $h(q)+1-q$ ebits, so $T_C(U_\phi)\le\min\{1,\,h(q)+1-q\}$.
- Converse $T_C(U_\phi)\ge h\!\left(1/(1+\sin(\phi/2))\right)$ from Nielsen majorization; the two bounds coincide asymptotically as $\phi\to0$ (both $\sim s\log(1/s)$).
- A strictly tighter converse for resource states of fixed Schmidt rank $D$, showing every finite $D$ forces one full ebit for some angles.
- Application: distributed bit-reversed QFT on $2n$ qubits at $O(1)$ (≈12.1869) ebits, versus $n^2$ with the prior one-ebit-per-gate construction.
- Extensions to arbitrary controlled two-qubit gates and, via KAK, to arbitrary two-qubit unitaries (three separate teleportations).

**How it works** Alice entangles her input qubit with the rank-3 resource via a controlled unitary and measures an ancilla, collapsing $A'$ to a 2D support; the outcome is unbiased so no input information leaks. Bob permutes, applies a diagonal phase $D_x$ encoding the nonlocal phase, then a qutrit Fourier transform (to avoid learning Alice's branch) and measures. Alice's corrective unitary $T_{x,y}=R^{-1}L$ must be unitary, which forces a circle-intersection condition on the phases $d_{i_x},d_{j_x}$; feasibility reduces to $\sin^2(\phi/2)(1-2p_1)(1-2p_2)\le 4p_1p_2$. Optimizing entropy over feasible spectra shows the symmetric choice $p_1=p_2=(1-q)/2$ is the minimizer. The refined converse uses SEP product-Kraus operators, Binet–Cauchy determinant expansion, and Cauchy–Schwarz tail bounds on the spectrum.

**Why it matters** Directly relevant to circuit knitting, distributed/modular architectures, and entanglement-cost accounting for nonlocal gates; the QFT result turns a quadratic entanglement cost into a constant one.

**Caveats** A gap remains between achievability and converse at moderate/large angles (at $\phi=\pi$ the protocol costs 1.5 ebits, so one falls back to the one-ebit protocol); $T_C(U_\phi)$ is still unknown exactly. Costs for general two-qubit unitaries are likely loose since the three KAK factors are teleported independently. Only exact, deterministic, single-shot implementations are treated — approximate or amortized/asymptotic costs could be lower. The authors credit an LLM with assistance in developing the protocol and the tighter converse.
