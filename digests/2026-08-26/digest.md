# SciRate Daily Digest — 2026-08-26

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Optimal Lower Bound for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24493](https://arxiv.org/abs/2608.24493) · [SciRate](https://scirate.com/arxiv/2608.24493)

*Rolando D. Somma, Ronald de Wolf*

**TL;DR** The paper proves an $\Omega(\log(1/\varepsilon)/\gamma\delta)$ query lower bound for guided ground-state energy estimation, jointly tight in all three parameters (precision $\delta$, guiding-state overlap $\gamma$, failure probability $\varepsilon$), matching the concurrent upper bound of Jeffery–Witteveen. The bound holds both for degenerate ground spaces (dimension $\log(1/\varepsilon)/\gamma^2$) and for the harder, more physical case of a unique ground state with spectral gap $3\delta$ (dimension $\log(1/\varepsilon)^2/\gamma^2$), and extends to block-encodings, fractional/continuous-time queries, ground-state *preparation*, and sum-of-squares spectral amplification (where it gives $\Omega(\log(1/\varepsilon)/\gamma\sqrt{\delta})$).

**The big picture** Estimating the lowest energy of a quantum system is the workhorse subroutine of quantum chemistry algorithms, and in practice one starts from a cheap trial state that is only guaranteed to have some modest overlap with the true ground state. Until now it was unclear how the cost scales when precision, overlap quality, and the demanded reliability of the answer all get simultaneously demanding — in particular whether failure probability could be suppressed cheaply, as it can be for quantum search. This work shows that no such cheap suppression exists: the known algorithm is optimal in every parameter at once, closing the gap between best algorithm and best lower bound. A side observation is philosophically interesting: the hardest instances have trial states that carry essentially no information about the ground state beyond the bare overlap guarantee, suggesting the standard overlap-based formulation of the problem may be the wrong abstraction.

**Key contributions**
- First lower bound tight in $\delta$, $\gamma$, and $\varepsilon$ *simultaneously*; previously only bounds with one parameter held constant were known.
- A version for unique ground states with a genuine $3\delta$ spectral gap (not just a degenerate ground space with diffuse overlap).
- Extension to ground-state preparation in trace distance, to block-encoding access, and to fractional-time Hamiltonian simulation.
- $\Omega(\log(1/\varepsilon)/\gamma\sqrt{\delta})$ lower bound for the SOSSA setting, showing that sum-of-squares spectral amplification is near-optimal as a black-box use of $G$ with $H=G^\dagger G$.

**How it works** A fractional-query polynomial method: writing $e^{i\theta x_j}$ queries as $\frac{1+e^{i\theta}}{2}I+\frac{1-e^{i\theta}}{2}O_x$ and truncating the resulting $2^T$-term expansion at $K=O(T\theta+\log(1/\varepsilon))$ standard queries yields, with operator-norm error $\le\varepsilon/3$, an approximating polynomial of degree $O(T\delta+\log(1/\varepsilon))$ — effectively converting a $\delta$-precision, $T$-query algorithm into a constant-precision, $T\delta$-query one. Degree is then lower bounded by combining Coppersmith–Rivlin (integer-grid to real-interval) with the Chebyshev extremal bound $T_D(1+\mu)\le e^{2D\sqrt{2\mu+\mu^2}}$, giving error $\ge 2^{-O(D^2/N+D\gamma)}$ à la Buhrman–Cleve–de Wolf–Zalka. For the unique-ground-state family, $U=I+(e^{i\theta}-1)|\psi_{a\omega j}\rangle\langle\psi_{a\omega j}|$ with $|\psi\rangle=\sqrt a|0\rangle+\omega\sqrt{1-a}|j\rangle$; averaging over the sign $\omega$ kills odd powers of $\sqrt{a(1-a)}$, leaving a univariate polynomial in $a$, and a case split on $p(0,3\delta)$ trades a $\Omega(\sqrt N/\delta)$ search bound against the Chebyshev bound, balanced at $N=\log(1/\varepsilon)^2/\gamma^2$.

**Why it matters** It settles an open problem from Mande–de Wolf and certifies optimality of the transducer-based algorithm, so no further asymptotic improvement in $U$-queries is possible under overlap-only guarantees. Relevant to anyone building phase-estimation subroutines inside larger algorithms, where subconstant error probability is required and, unlike single-output subroutines, no cheap error-reduction technique is known.

**Caveats** The lower bounds need dimension at least $\log(1/\varepsilon)/\gamma^2$ (or its square), so they say nothing about small systems; they count only $U$/$U^{-1}$ (unlimited $A$ uses, gates, ancillas — which strengthens the bound but leaves other cost models open); the sparse-access model, including $d$-dependence, remains open despite the hard Hamiltonians being 1- or 2-sparse; and the hard instances are arguably degenerate as physics, with uninformative guiding states, which the authors themselves flag as evidence that the overlap promise is a weak problem formulation. Proofs were substantially AI-assisted (disclosed), then simplified by the authors.

## 2. Improved Quantum Codes with Transversal T Gates

[arXiv:2608.24000](https://arxiv.org/abs/2608.24000) · [SciRate](https://scirate.com/arxiv/2608.24000)

*Adam Wills*

**TL;DR** This work builds quantum CSS codes on which physical $T$ on every qubit implements logical $T$ on every logical qubit with *no* Clifford correction, using 8-divisible *decreasing monomial* codes punctured at a downward-closed subset of the Boolean hypercube. The central technical tool is a closed-form minimum distance for such punctured codes, which yields the first constant-rate families with growing distance (hence the first magic-state-distillation exponent $\gamma\to 0$ for a transversal-$T$ code) and strictly enlarges the achievable $(\text{rate},\text{distance})$ exponent region — the first improvement since Hastings–Haah (2017) and Haah (2018).

**The big picture** Fault-tolerant quantum computers need a non-Clifford gate, and the cheapest and most useful candidate is the single-qubit T gate; codes on which applying it bitwise cleanly enacts it on all logical qubits are rare and have resisted improvement for nearly a decade. The author replaces the Reed–Muller codes at the heart of prior constructions with a much richer family of monomial evaluation codes, and shows that if the set of coordinates removed to create logical qubits is chosen to have the same nested combinatorial structure as the code itself, the resulting distance can be computed exactly. This unlocks families whose number of logical qubits scales with the block size while the distance still grows, which translates into asymptotically vanishing overhead for distilling magic states — a regime previously reachable only with multi-qubit non-Clifford gates.

**Key contributions**
- Closed-form distance for a binary decreasing monomial code $C(\Delta)$ punctured at a *downset* $\Gamma$: $d=\min_{A\in\Delta}|\{V\subseteq \bar A: V\notin\Gamma\}|$, valid under an explicit non-annihilation condition (puncturing injective). Of independent interest for polar/monomial codes and for randomly punctured evaluation codes over small fields.
- Explicit construction: 8-divisible *weighted* Reed–Muller codes with weights $(1,\dots,1,h)$, punctured at low-Hamming-weight points of $[m-1]$, giving $\beta_{\rm explicit}(\alpha)$ with $q^*(\alpha)$ defined implicitly; improves prior explicit frontier for $\alpha>H_2(1/6)$.
- Constant-rate regime: for any $R\in(0,1/3)$, explicit $[[n,(R+o(1))n,\Omega(2^{(c_R+o(1))\sqrt{\log_2 n}})]]$ with $c_R=-\Phi^{-1}(2R/(1+R))$; hence $\gamma=\log(n/k)/\log d\to 0$, versus $\gamma\approx0.678$ before.
- Randomised construction: "protecting" points from the puncture using a random $t$-uniform hypergraph that covers all $y$-sets, giving $\beta_{\rm exist}(\alpha)=1/2$ up to $\alpha=1/2$, then linear, then $1-2H_2^{-1}(\alpha)$.
- Extends to $R_\ell=\mathrm{diag}(1,e^{2\pi i/2^\ell})$, which (being single-qubit) immediately implies transversal *addressability* of $R_{\ell-1}$.

**How it works** In the standard $X$-generator formalism, $G$'s logical rows must have weight $\equiv 7 \bmod 8$, pairwise overlaps $\equiv 0 \bmod 4$, triple overlaps even — automatically satisfied (via Ward's identities) if the parent classical code is 8-divisible. Quantum distance equals $d(\mathrm{punc}_\Gamma(C^\perp))$, and monomial-code duality ($C(\Delta)^\perp=C(\Delta^\perp)$, $\Delta^\perp=\{A:\bar A\notin\Delta\}$) turns this into $\min_{A\notin\Delta}|2^A\setminus\Gamma|$. Maximising dimension pushes toward $\Delta=2^{[m-3]}$ (constant rate, but distance 2); weighted Reed–Muller codes interpolate. The lower bound $d\ge d(\mathcal G_0^\perp)$ is shown tight throughout.

**Why it matters** Relevant to magic-state distillation (fast $T$-to-$T$ protocols, no Clifford correction), to concatenated/hierarchical architectures where non-LDPC inner codes are acceptable, and as guidance for the active effort to find LDPC codes with transversal non-Clifford logic.

**Caveats** Constant-rate distance grows only as $2^{\Theta(\sqrt{\log n})}$ — sub-polynomial, so finite-size benefits are unclear. Codes are non-LDPC. Restricted to stabiliser/CSS codes; the author suspects non-stabiliser codes could do better. The randomised construction gives no gain at constant rate, and asymptotically good transversal-$T$ (even triorthogonal) qubit codes remain open. Low-rate regimes ($\alpha$ small) do not improve on prior work.

## 3. Optimal Quantum Algorithm for Ground-State Energy Estimation with a Guiding State

[arXiv:2608.24494](https://arxiv.org/abs/2608.24494) · [SciRate](https://scirate.com/arxiv/2608.24494)

*Stacey Jeffery, Freek Witteveen*

**TL;DR** The authors give a quantum algorithm for guided max-eigenphase (equivalently guided ground-state energy) estimation using $O(1/(\gamma\delta))$ controlled queries to the evolution/walk unitary $U$ and $O(\frac{1}{\gamma}\log\frac1\delta\log\log\frac1\delta)$ queries to the state-preparation unitary $A$, removing the $\log\frac1\gamma$ factor present in all prior QPE- and QSVT-based approaches. This matches the $\Omega(1/(\gamma\delta))$ lower bound of Mande–de Wolf, settling their open question; the tool is Belovs–Jeffery *transducers*, which compose subroutines without error-reduction overhead.

**The big picture** Estimating the lowest energy of a quantum system, given a trial state with some guaranteed overlap with the true ground state, is the flagship fault-tolerant quantum application in chemistry and materials science. Every known method paid a logarithmic penalty in the inverse overlap, because the "noise floor" of phase estimation (or the ripple size of a polynomial filter) had to be pushed below the overlap-sized signal. This work shows that penalty is entirely avoidable, by building the whole subroutine inside a compositional framework where bounded-error primitives are replaced by exactly-composable objects, and only converted into a circuit at the very end. The resulting query cost is provably optimal, so the asymptotic complexity of this central task is now closed.

**Key contributions**
- Optimal query complexity: $\Theta(1/(\gamma\delta))$ calls to $U$ (with the concurrent lower bound of Somma et al., $\Theta(\frac{1}{\gamma\delta}\log\frac1\epsilon)$ in the $\epsilon$-error setting).
- A standalone transducer for *decision* amplitude amplification (a quantum walk on a star graph with a tunable boundary weight $w$; transduction complexity $w/\epsilon$ vs. $1/w$, balanced at $w=\gamma$).
- A standalone transducer for *decision* phase estimation: a walk on infinite weighted lines with per-eigenspace geometric ratios $\gamma_k=\tan(\theta_k/2)$, whose reflections are implementable with $O(1)$ controlled calls to $U,U^\dagger$.
- A composed canonical transducer for the threshold problem with $W=O(1/(\gamma\delta))$ and Las Vegas query complexity $L\le 1+1/\gamma$ w.r.t. the reflection oracle $O_\gamma(A)$ — hence the asymmetric $A$-vs-$U$ costs.
- A general "exact $(D,m)$-truncation" lemma showing infinite counters can be replaced by mod-$D$ increments with *zero* added error when the algorithm makes fewer than $D/m$ transducer calls.

**How it works** The threshold decision problem (is $\|\Pi_{>s}\ket\psi\|\ge\gamma$, or $\Pi_{>s-\delta'}\ket\psi=0$?) is encoded as a transducer whose transduction action is $\ket{\bar1,0}\mapsto\pm\ket{\bar1,0}$; single-bit phase estimation reads out the sign. Converting via the transducer-implementation theorem costs $O(W)$ work-unitary calls and $O(L)$ oracle calls. Binary search over the threshold yields the estimation result, with $O(\log\frac1\delta\log\log\frac1\delta)$ overhead only on $A$.

**Why it matters** Phase estimation is ubiquitous; the authors argue the same transducer trick should strip log factors elsewhere. Constants are unoptimized but the construction is simple (two reflections, one infinite counter), so it may be competitive in resource estimates.

**Caveats** Requires the window promise (all eigenphases in $[0,\pi/2]$), harmless for Hamiltonians with a known norm bound $\lambda$ — note evolution time scales as $\lambda/(\gamma\delta)$. Space overhead grows to $O(\log\frac{1}{\gamma\delta})$ ancillas versus $O(\log\frac1\delta)$ classically; reducing this is open. Gate count includes an additive $\frac{1}{\gamma\delta}\log\frac{1}{\gamma\delta}$ term. Full coherence (using the routine inside a larger superposition) is not addressed. Source is truncated before the composed construction and binary-search analysis; the authors also disclose LLM assistance in proofs and computations.

## 4. Nearly Optimal Amplitude Estimation at any Depth

[arXiv:2608.24434](https://arxiv.org/abs/2608.24434) · [SciRate](https://scirate.com/arxiv/2608.24434)

*Jona Erle, Bálint Koczor*

**TL;DR** The paper introduces Windowed Least Squares Amplitude Estimation (WLSAE): sample Grover-circuit depths $m$ from a "window" distribution on $\{-M,\dots,M\}$, collect $\pm1$ outcomes with $\mathbb{E}[Z_m]=\cos(2m\lambda)$, and estimate the Grover angle by minimizing a one-dimensional least-squares loss on a uniform grid. For any *admissible* window it proves $M^2N\in\tilde{\mathcal{O}}(\epsilon^{-2})$ additive-angle accuracy **uniformly** over $\lambda\in[0,\pi/2]$, including the boundaries $\lambda\to0,\pi/2$ where prior depth-tunable schemes degrade to classical sampling — with no ancillas and no controlled Grover operators.

**The big picture** Amplitude estimation is the workhorse behind quadratic speedups in Monte Carlo, finance, and chemistry applications, but the textbook version needs deep coherent circuits, ancilla registers, and controlled reflections that early fault-tolerant hardware cannot support. A line of recent work replaces coherence with repetition and classical inference, letting you dial circuit depth against shot count, but the accuracy guarantees quietly break down when the amplitude is very close to zero or one — exactly the regime relevant to overlap certification and trial-state verification. This work shows that a broad, explicitly characterized family of depth-sampling distributions plus a plain least-squares fit achieves the theoretically optimal depth–repetition tradeoff everywhere, boundaries included, so the quantum advantage never silently disappears.

**Key contributions**
- A general admissibility criterion for depth windows: enough probability mass ($\geq b/T$) on small depths plus moment bounds $\mathbb{E}[m^{2k}]\lesssim T^{2k}$; Gaussian, Kaiser, uniform, linear, cubic windows all qualify.
- Uniform-in-$\lambda$ guarantee $M^2N\in\mathcal{O}(\epsilon^{-2}\log(\epsilon^{-1}\delta^{-1}))$, matching Zalka–Burchard up to logs, spanning $M=1$ (classical sampling) to $M=\Theta(\epsilon^{-1})$ (Heisenberg), i.e. $MN\in\mathcal{O}(\epsilon^{-1-\beta})$ at depth $\epsilon^{-1+\beta}$.
- Shows the "boundary patch" of GLSAE (Huang–Koczor) is unnecessary and actually forfeits the speedup where invoked.
- Numerics: at fixed budget $Q=10^6$, a *uniform* window beats the Gaussian one and tracks the Cramér–Rao bound closely.

**How it works** The analysis is an M-estimation argument. The population loss $\mathcal{E}^{(\lambda)}(\theta)=\mathbb{E}_m[(\cos2m\lambda-\cos2m\theta)^2]$ is sandwiched between constants times an envelope $\Psi(\Delta)^2$ with $\Psi=\min(1,T\Delta,T^2\Delta\max(\bar\lambda,\Delta))$, where $\bar\lambda=\min(\lambda,\pi/2-\lambda)$ — the cubic factor near the boundary is precisely what earlier Bernstein–von Mises-style arguments miss. The empirical fluctuation is controlled by Bernstein's inequality with matched variance/range proxies (using $\mathrm{Var}[Z_m]=\sin^2(2m\lambda)$, which itself vanishes at the boundary) plus a union bound over the $K=\Theta(1/\epsilon)$ grid points; a localization lemma then converts "loss near $\lambda$ beats loss far away" into $|\hat\theta-\lambda|\leq\epsilon$. Dirichlet-kernel estimates supply the far-field lower bound $\mathcal{E}\geq\tfrac{4b}{243}$.

**Why it matters** This closes the boundary gap in low-depth amplitude estimation and gives implementers a design space of windows rather than one prescription — directly relevant to early fault-tolerant Monte Carlo, overlap/fidelity certification, and trial-state verification.

**Caveats** The explicit constants are astronomical ($A=3C_8/8C_2>3\times10^6$, hence $N$ prefactors $\sim A^2C_9^2$ and grids of size $\sim A/\epsilon$); the guarantee is asymptotically tight but the stated finite-sample bound is far from practical, and the numerics (single $\lambda=0.5$, heuristic grid $K\propto\sqrt{\mathbb{E}[m^2]N}$) do not test the boundary regime the theory is about. No hardware noise or gate-error model is included, and the total query count still degrades as $\epsilon^{-1-\beta}$ at reduced depth, as the lower bound demands.

## 5. Essentially optimal gate teleportation

[arXiv:2608.24345](https://arxiv.org/abs/2608.24345) · [SciRate](https://scirate.com/arxiv/2608.24345)

*Lukas Schmitt, David Sutter*

**TL;DR** The authors give the first deterministic LOCC protocol that implements a two-qubit controlled-phase gate $U_\phi=\mathrm{diag}(1,1,1,e^{i\phi})$ using strictly less than one ebit, with a Schmidt-rank-3 resource state costing $h(q)+1-q$ ebits where $q=1/(1+\sin(\phi/2))$, matched by a converse of $h(q)$. As $\phi\to 0$ the cost vanishes, resolving a long-standing question of whether sub-ebit gate teleportation is possible, and yielding a distributed QFT on $2n$ qubits with a constant $\approx 12.19$ ebits instead of $n^2$.

**The big picture** Implementing a joint operation on two distant quantum systems without letting them interact requires pre-shared entanglement plus classical messages. Until now, every known exact, always-succeeding scheme burned at least one full unit of entanglement, even for gates that are nearly trivial and barely entangle anything. This work shows that the entanglement price can be made to scale smoothly with how nonlocal the gate actually is, and proves a nearly matching lower bound — with an immediate payoff for distributed algorithms built from many weak two-qubit rotations, such as the Fourier transform, where the total entanglement budget drops from growing quadratically with system size to a fixed constant.

**Key contributions**
- Explicit four-round, two-way LOCC protocol (4 classical bits) using a rank-3 resource state, with full correctness proof for all measurement branches.
- Proof that the stated rank-3 state is entropy-optimal *within* the protocol family (via a feasibility condition and concavity argument in the parametrized equality manifold).
- A simple converse via Nielsen majorization giving $H\ge h(q)$, plus a substantially stronger Schmidt-rank-$D$-restricted converse based on a SEP/Cauchy–Binet determinant argument, showing any finite-rank resource needs a full ebit for some angles.
- Extensions to arbitrary controlled two-qubit unitaries and, via KAK, to general two-qubit gates (as three separate teleportations); distributed QFT application.

**How it works** Alice's first unitary plus ancilla measurement splits the rank-3 state into two rank-2 branches with outcome probability exactly $1/2$, leaking nothing about her input. Bob applies a controlled diagonal phase $D_x$ followed by a qutrit Fourier transform and measures, so no which-branch information leaks; the phases $d_{i_x},d_{j_x}$ are chosen as intersection points of two circles in the complex plane, a condition that is exactly the unitarity requirement for Alice's round-3 correction $T_{x,y}=R^{-1}L$. That feasibility reduces to $\sin^2(\phi/2)(1-2p_1)(1-2p_2)\le 4p_1p_2$. Alice's computational-basis measurement equalizes amplitude magnitudes; Bob then applies a diagonal phase fix.

**Why it matters** Relevant to distributed/modular quantum computing, entanglement-cost accounting for nonlocal gates, and the theory of LOCC implementation of unitaries. The QFT example shows constant-overhead distributed implementations are possible for circuits dominated by small-angle controlled phases.

**Caveats** There remains a gap of up to $\frac{\sin(\phi/2)}{1+\sin(\phi/2)}$ ebits between achievability and the general converse; $T_C(U_\phi)$ is not determined exactly. The general two-qubit extension is explicitly suboptimal (subadditivity over three KAK factors). Protocol optimality is proven only within rank-3 states of the given form; higher-rank resources are unexplored on the achievability side. The construction was developed with LLM assistance (disclosed), so independent verification of the algebra is warranted.
