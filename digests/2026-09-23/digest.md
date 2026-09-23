# SciRate Daily Digest — 2026-09-23

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. When are bosonic Gaussian states classical to learn?

[arXiv:2609.26705](https://arxiv.org/abs/2609.26705) · [SciRate](https://scirate.com/arxiv/2609.26705)

*Senrui Chen, Antonio Anna Mele, Francesco Anna Mele, John Preskill*

**TL;DR** The sample complexity of tomography for $n$-mode bosonic Gaussian states under non-entangled (single-copy) measurements is pinned down as $\Theta\!\left(n^2\varepsilon^{-2}\min\{n,1+\nu^{-1}\}\right)$, where $\nu$ lower-bounds the thermal photon occupation per eigenmode ($\Sigma\ge(\tfrac12+\nu)\I$). Cold states ($\nu\lesssim 1/n$) require $\Omega(n^3/\varepsilon^2)$ copies — strictly worse than the $\Theta(n^2/\varepsilon^2)$ cost of learning a classical $2n$-variate Gaussian, and the hardness survives $k$-copy entangled measurements up to a $\min\{\sqrt k,n\}$ factor. Warm states ($\nu=\Omega(1)$) are learnable with $\Theta(n^2/\varepsilon^2)$ copies by plain non-adaptive heterodyne detection.

**The big picture** Light can look either like a classical fluctuating field or like discrete photons, and it has long been understood that thermal noise washes out quantum features. This paper makes that intuition quantitative in a new currency: how many experimental repetitions, and how sophisticated a measurement apparatus, are needed to reconstruct the state. It shows that states with at least about one thermal photon per mode are exactly as cheap to characterize as an ordinary classical multivariate Gaussian distribution using the simplest optical readout, whereas near-vacuum states are provably harder, requiring a factor of the mode number more data unless one can jointly measure many copies at once inside a quantum computer. The crossover is sharp and located, and the authors argue real dark-matter search experiments sit on both sides of it.

**Key contributions**
- Tight single-copy sample complexity across the whole temperature range, including the previously unknown lower bounds and the improved upper bound for $\nu=\omega(1/n)$.
- $\Omega(n^3/\varepsilon^2)$ single-copy lower bound holding for *passive, cold* states with $O(1)$ total photons; for non-adaptive schemes it holds even with the spectrum of $\Sigma$ known.
- $k$-copy lower bound $\Omega(n^3/(\varepsilon^2\min\{\sqrt k,n\}))$: constant-$k$ entanglement doesn't help.
- A black-box reduction embedding $n$-dimensional mixed-state tomography into cold passive Gaussian tomography via the fugacity-matrix representation.
- A new one-sided trace-distance bound for Gaussian states with prefactor depending only on distance from the pure-state boundary, not on $n$ or energy.

**How it works** The reduction sets fugacity ${\sf R}=\sigma/4$, so the one-photon block of the resulting passive Gaussian state is $\sigma$; a rejection-sampling simulator produces one Gaussian copy from $\mathbb{E}T\le 4/9$ copies of $\sigma$, letting finite-dimensional $k$-copy no-go theorems transfer. The temperature-dependent lower bound instead uses Bayesian posterior anti-concentration over a GUE-based prior ${\sf R}_X=r(\I+\xi X)$, with a multiplicative local reparametrization to handle the nonlinearity of $\rho$ in $X$, and Schur-polynomial/log-Sobolev estimates for symmetric-power Haar moments; each copy contributes only $O(\varepsilon^2/n)$ posterior tilt against an $n^2$-dimensional prior volume. The upper bound *inflates* the empirical heterodyne covariance by $1/(1-\zeta)$ so $\widehat\Sigma\succeq\Sigma$ automatically (hence physical), then applies the new one-sided bound via resolvent/Pinsker arguments.

**Why it matters** It cleanly separates entangling from non-entangling measurements for Gaussian tomography (complementing the earlier Gaussian/non-Gaussian separation): $n^2$ needs *both* resources, while warm states need neither. Practically, it certifies heterodyne readout as optimal in the warm regime relevant to e.g. ADMX-like haloscopes, and quantifies the penalty for quantum-limited Gaussian readout in cold regimes where photon counting is preferred. It also offers a learning-theoretic notion of classicality strictly finer than $P$-function positivity.

**Caveats** Results concern full tomography of unstructured Gaussian families; practical sensing targets low-dimensional submanifolds, and the authors note heterodyne may be far from optimal there. No matching $k$-copy upper bound. Squeezed states ($\nu\le 0$) are outside the tight characterization, retaining $\widetilde\Theta(n^3)$ with energy-dependent logs. The experimental mode-count/occupation estimates in Table 1 are heuristic.

## 2. A quantum lower bound for path finding in welded trees

[arXiv:2609.26712](https://arxiv.org/abs/2609.26712) · [SciRate](https://scirate.com/arxiv/2609.26712)

*Joseph Carolan, Andrew M. Childs, Matthew Coudron, Amin Shiraz Gilani*

**TL;DR** The authors prove that any quantum query algorithm needs $\Omega(2^{n/12})$ queries to output an explicit entrance-to-exit path in a height-$n$ welded tree graph whose weld is formed by three independent random color-matchings between the leaves — even though a quantum walk finds the exit in $\mathrm{poly}(n)$ time. The proof builds a compressed-permutation-oracle simulation of the welded-tree oracle and shows that the oracle's coherent database provably stays inside a "path-free" subspace of color-word states, with the database's informative *core* growing by only $O(n)$ per query.

**The big picture** A quantum walk can cross a maze built from two binary trees glued at their leaves exponentially faster than any classical search, but only by exploring exponentially many routes at once; writing down the route destroys the interference that gives the speedup. Whether some cleverer quantum algorithm could actually output a route has been a well-known open problem for two decades. This work shows no algorithm can: detecting and traversing the maze is easy quantumly, while producing any concrete route is provably exponentially hard. It is thus a clean, unconditional example separating "solving by superposition" from "exhibiting a witness."

**Key contributions**
- First unconditional exponential quantum lower bound for welded-tree path finding, removing the "rooted and genuine" algorithm restrictions of prior work (CCG22); arbitrary quantum algorithms are allowed, including ones that forget the paths to vertices they hold.
- Extension of the compressed permutation oracle formalism to *expanding injections*: inverse label queries can be replaced by database lookup with error $O(\sqrt{N/M})$, plus a "sanitized" (subnormalized) oracle with $O(q^2/\sqrt{M})$ hybrid error.
- A compressed welded-tree oracle assembled from a label injection and three weld permutations, with an explicit faithful-simulation lemma.
- The invariant subspace machinery: color words, block decomposition, database *cores*, random core placements, and the *clipping lemma* controlling superpositions.

**How it works** Randomness is split into a uniform injection $P:V\hookrightarrow\{0,1\}^{2n}$ and three independent weld bijections $W_r,W_b,W_g$ on the non-$c$-colored leaves; a graph query is compiled into two inverse label lookups, at most two weld queries, and one forward label query, each replaced by compressed versions. Reachable database states are shown to lie near the span of *color-word states*: superpositions of minimal databases realizing nonbacktracking color-labeled walks from the left and right roots that never meet. Each tree is partitioned into $\sqrt N$ blocks of $\sqrt N$ leaves; the relevant bad events are *block collisions* (a fresh weld arrival landing in an occupied block) and *block overflow* (exiting a block upward after arriving via the weld), both exponentially unlikely. The clipping lemma shows removing violating extensions barely changes the state — proved by decomposing anchored random-core-placement states orthogonally, which is what makes the bound hold for arbitrary superpositions. Iterating gives core size $O(nq)$, and the compressed-oracle fundamental lemma converts path-freeness of the database into the query bound.

**Why it matters** It resolves (for this weld distribution) a problem on Aaronson's list of open quantum query questions, and gives a rigorous "double-slit" separation between search and witness-finding, relevant to verifiable quantum advantage, adiabatic optimization, and quantum learning constructions that use welded trees as a gadget. It also demonstrates compressed permutation oracles as a general tool for non-cryptographic graph lower bounds.

**Caveats** The result is proved for the independent-matchings weld rather than the original single-random-cycle weld; adapting the argument is claimed straightforward but deferred. The exponent $n/12$ is presumably far from tight. Concurrent independent work (MP26) reportedly obtains a similar result. Much of the technical burden — the clipping lemma and non-orthogonality of left- vs. right-rooted color words (re-rooting degeneracy) — sits in appendices truncated here, so the error bookkeeping cannot be fully checked from this excerpt.

## 3. $\mathsf{BQP} \subseteq \mathsf{IP}$ Does Not Relativize

[arXiv:2609.25680](https://arxiv.org/abs/2609.25680) · [SciRate](https://scirate.com/arxiv/2609.25680)

*Adam Bouland, Andrew Huang, Anand Natarajan, Itay Shalit, Avishay Tal*

**TL;DR** The authors exhibit a classical oracle relative to which BQP ⊄ IP, using Aaronson–Ambainis's Forrelation distribution unchanged. The technical core is a structural result: the optimal acceptance probability of an oracle IP verifier, represented as an average/max tree, can be replaced by a *convex* smooth surrogate with ℓ₁-gradient ≤ L and ℓ₁-Hessian ≤ 2λdL², and Gaussian-sign distributions with off-diagonal covariances ≤ β = N^{-1/2} fool such functions to within 2^{-Ω(n)}.

**The big picture** Interactive proofs are the classic way a weak verifier delegates hard computation to an untrusted prover, and a long-standing goal is to let a purely classical verifier check quantum computations with unconditional soundness and an efficient prover. This work shows that no such protocol can exist by "black-box" reasoning alone: there is a world with an oracle where quantum polynomial time escapes everything single-prover interactive proofs can verify, even with polynomially many rounds and polynomial communication. Combined with a recent relativizing multi-prover protocol for quantum computation, it also gives the first oracle separating single-prover from multi-prover interactive proofs, a question open since Fortnow's thesis. This partly explains why decades of effort toward doubly-efficient classical verification of quantum computation have stalled, and pinpoints exactly which structural feature — joint maximization over full prover strategies — multi-prover systems exploit to escape the barrier.

**Key contributions**
- Oracle with BQP ⊄ IP; first oracle separation IP vs MIP (with Aaronson et al.'s relativizing MIP protocol).
- Softmax smoothing lemma for AVG/MAX circuits preserving convexity, with additive error dLln2/λ and simultaneous first/second derivative bounds — and a remark showing that without convexity such bounds are vacuous (every Boolean function admits a smooth extension with gradient ≤ 2, Hessian ≤ O(log m)).
- A rounding lemma using convexity to compare E[F(sgn(a+G))] and E[F(h_δ(G))] with only √log m dimension dependence (18Lδ(‖a‖_∞+√ln 2m)).
- A PRG fooling poly-size Avg-Max circuits: signs of ⟨v_i, g⟩ for Ta-Shma-code unit vectors, seed length poly(log m, 1/β) Gaussians.

**How it works** Goldwasser–Sipser (relativizing) puts the verifier in public-coin form with queries at the end; adaptive query trees become affine leaves of ℓ₁-norm ≤ L, giving a convex (d,L)-AM extension C. Softmax gates yield convex smooth F. Convexity gives F(sgn) − F(h_δ) ≤ ⟨∇F(sgn), sgn − h_δ⟩; conditioning on the sign vector and on D leaves each coordinate an independent truncated Gaussian, whose conditional density near zero is bounded by 1/σ + |μ|/σ², yielding per-coordinate error O(δ(1+|a_i|+|D_i|)) and hence an ℓ₁·ℓ_∞ bound. Gaussian interpolation (smart path) then costs βK/(4δ²). A hybrid over T = O(log N) noise-halving steps, with arbitrary shifts a handled by freezing coordinates with |a_i| > 10√ln m, reaches D itself; δ = N^{-1/8}, λ = 1/δ gives 2^{-Ω(n)}, then diagonalization.

**Why it matters** It is a formal barrier: any prover-efficient classical IP for BQP must be non-relativizing. The bound tolerates up to exp(n/10) rounds, strictly strengthening Raz–Tal's o(n/log n)-alternation PH lower bound. The convex-smoothing technique may be reusable wherever max-gates obstruct Fourier-analytic arguments.

**Caveats** This is an oracle result; non-relativizing techniques (e.g., arithmetization, cryptographic assumptions) remain unaffected, and existing LWE-based verification protocols are untouched. The separation says nothing about unrelativized BQP ⊆ IP, which is open only in the prover-efficient regime. The MIP separation is contingent on the cited relativizing MIP protocol.

## 4. Good Quantum Locally Testable Codes from Product Expansion

[arXiv:2609.26735](https://arxiv.org/abs/2609.26735) · [SciRate](https://scirate.com/arxiv/2609.26735)

*Mitali Bafna, Anqi Li, Quynh T. Nguyen*

**TL;DR** Assuming a modified product-expansion conjecture for Reed–Solomon codes evaluated on multiplicative subgroups of order 2^m+1, this paper constructs an explicit family of binary quantum CSS codes that are simultaneously good (constant rate and distance) and good locally testable codes (constant soundness and locality). The construction plugs projective Reed–Solomon local codes into the Dinur–Lin–Vidick 4-dimensional framework, but instantiated on the *non-Abelian* cubical complexes of Rungtanapirom–Stix–Vdovina, removing the polylogarithmic losses inherent to Abelian Cayley complexes.

**The big picture** Quantum error-correcting codes that are both efficient and locally checkable are the quantum analogue of the classical locally testable codes that underpin probabilistically checkable proofs, and they are the key missing ingredient in several approaches to the quantum PCP conjecture and to low-overhead fault tolerance. Until now the best quantum locally testable codes were only "almost good": their distance and soundness decayed logarithmically, a bottleneck traceable to the fact that commutative symmetry groups need many generators to expand well. This work shows that switching to a non-commutative algebraic complex built from products of trees, and equipping it with algebraically structured local codes whose symmetries match the complex's own symmetries, removes that bottleneck entirely — conditional on a conjecture about the robustness of tensor products of Reed–Solomon codes evaluated on carefully chosen structured point sets.

**Key contributions**
- Conditional construction of good qLTCs: constant rate, distance, soundness, locality over a binary alphabet.
- A concrete recipe for making projective Reed–Solomon local codes compatible with the non-Abelian complex's edge-label permutations, executing an approach floated but abandoned in earlier work.
- A binary-field variant of the Bafna–Vyas product-expansion conjecture: subgroups of coprime orders of the form 2^m+1 in F_{2^r}*, motivated by ruling out low-degree-curve obstructions that kill the naive generalization.
- Characteristic-two spectral expansion for the RSV complexes (λ_i ≤ 2√s_i/(s_i+1)) via Morgenstern's tree-quotient bounds, plus explicit "frame matrix" structure (Lemma 4.1(4)) extracted from Bruhat–Tits lattice bases.

**How it works** Vertices are (PGL₂(F_{2^r})/PGL₂(F₂)) × {0,1}⁴; direction-i edges are labeled by P¹(F_{s_i}), s_i = 2^{m_i} with 8 | m_i. Edge-opposite labels across an edge are related by an SL₂(F_{s_j}) Möbius matrix, under which projective RS codewords are only *scaled* permutations of codewords. The fix: lift squares to the product of trees, extract comparison matrices F_i(v,Q) ∈ SL₂ from adapted lattice bases, define per-(vertex,square) weights ν_v(Q) as products of powers of the scaling scalars, and compose with an h-fold Frobenius permutation, imposing s_i − 1 | (2^h+1)d_i so the weights reconcile at both endpoints. Each edge then carries a rescaled/permuted PRS code; since product expansion depends only on Hamming supports, rescaling is harmless, and every vertex local view becomes a genuine tensor PRS codeword. DLV's local-to-global machinery then applies.

**Why it matters** If the conjecture holds, this closes the qLTC parameter question and immediately improves downstream applications: NLTS, quantum IOPs, gap amplification for quantum CSPs, and fault-tolerance overhead. The frame-matrix structure of algebraic HDXs may be reusable elsewhere.

**Caveats** Everything is conditional on an unproven and newly modified conjecture (the authors note the original prime-field version fails over extension fields). Constants — rate, distance, soundness — are not quantified; locality is constant but presumably large, since local code rates must be near 1 and near 0 in paired directions. The RSV complex requires large-degree reduction polynomials and injectivity radius ≥ 8 arguments; the Reed–Solomon-to-subgroup reduction and the full 4-dimensional bookkeeping are only sketched in the available source.

## 5. Hamiltonian Learning and Certification via Eigenphase Engineering

[arXiv:2609.26596](https://arxiv.org/abs/2609.26596) · [SciRate](https://scirate.com/arxiv/2609.26596)

*Myeongjin Shin, Yu Tong*

**TL;DR** The paper introduces "eigenphase engineering," a primitive that reads Hamiltonian energy-expectation differences off the perturbative response of isolated eigenphases of an actually-implemented controlled evolution, rather than off a simulated effective Hamiltonian. This yields the first Heisenberg-limited learner for $s$-sparse $k$-local Hamiltonians, total evolution time $\widetilde O(s/\varepsilon)$, that works on a fixed time grid of near-maximal spacing $\tau=\widetilde\Theta(1/\Lambda)$; a companion lower bound $\Omega_k(s^{1-1/(2k)}/\varepsilon)$ improves the previous $\Omega(\sqrt s/\varepsilon)$.

**The big picture** Learning an unknown many-body Hamiltonian from its own dynamics at the best possible precision scaling normally requires interleaving control pulses ever more frequently as you demand more accuracy — an unrealistic demand given finite pulse durations. This work shows that optimal precision scaling is compatible with pulses spaced as far apart as information theory allows, essentially the inverse of the energy scale, with no shrinking as accuracy improves. It also gives a version using only single-qubit preparations, pulses and measurements with no ancillas, at modest extra cost, plus certification and single-coefficient protocols. This makes near-optimal Hamiltonian characterization substantially closer to what analog simulators and processor-calibration setups can actually execute.

**Key contributions**
- Energy-gap primitive: $\langle x|H|x\rangle-\langle y|H|y\rangle$ to error $\varepsilon$ with $T=\widetilde O(1/\varepsilon)$ on a grid $\tau=\widetilde\Theta(1/\Lambda)$, forward evolution only, no controlled-$U$ or inverse.
- $\ell_2$ learning in $\widetilde O(s/\varepsilon)$ at $\tau=\widetilde\Theta(1/\Lambda)$ (removes the $1/s$ in Bakshi et al.'s step size and the $\varepsilon$-dependence in Ma et al.'s).
- Single-qubit-only variant: $\ell_\infty$ at $\widetilde O(s/\varepsilon)$, $\ell_2$ at $\widetilde O(s\sqrt n/\varepsilon)$, same step size.
- Improved evolution-time lower bound $\Omega_k(s^{1-1/(2k)}/\varepsilon)$, valid for adaptive, ancilla-assisted, unrestricted-time protocols.
- Tolerant certification in $\widetilde O(1/\varepsilon)$ ($\widetilde O(n^{3/2}/\varepsilon)$ single-qubit), and estimation of one Pauli coefficient in $\widetilde O(1/\varepsilon)$ with no locality/sparsity assumption.

**How it works** A known control $V$ gives $|e_0\rangle,|e_1\rangle$ eigenvalues $1,-i$ and $-1$ on the complement, a constant spectral gap $\sqrt2$. The circuits $F_\pm(t)=V^{\pm1}W^\dagger e^{-itH}W$ have analytic eigenphases whose $t$-derivatives at $0$ are the two energy expectations; symmetrizing over $\pm$ leaves an even series $\delta_a(t)=\langle e_a|K|e_a\rangle+\sum_j b_{a,j}t^{2j}$. Repeating $F_\pm^m$ amplifies the phase coherently while eigenvector error stays $m$-independent; robust phase estimation extracts $\delta_a$ at $t=q\tau$, $q\le p$, and Lagrange extrapolation in $t^2$ (weights $c_q$, $\sum|c_q|=O(\sqrt p)$) with $p=O(\log)$ kills the bias without shrinking $\tau$. Random Pauli product states make these gaps a bounded orthonormal system, so basis-pursuit denoising recovers the unknown support with $\widetilde O(s)$ measurements. The single-qubit case lacks a global gap (subset-sum argument gives only $O(1/n)$); Diophantine rotation angles plus the fact that order-$r$ Dyson terms flip $\le kr$ bits restore separation inside a Hamming ball, analyzed via an auxiliary unitary with defect only at order $L+1$. The lower bound packs an exponentially large well-separated Hamiltonian family (matrix Khintchine controls operator norms) against a truncated-Dyson dimension bound in the adaptive tree model.

**Why it matters** It cleanly decouples two resources previously entangled — precision and control frequency — and supplies a single primitive serving learning, certification and targeted coefficient estimation. Relevant to anyone benchmarking analog simulators or calibrating processors, and to the theory community tracking the $s$-dependence gap.

**Caveats** Noiseless model: no SPAM or pulse-error analysis, so robustness of the high-order extrapolation to realistic imperfections is untested. Constants degrade as $k$ grows ($k=O(1)$ throughout); certification tolerance is $\varepsilon/12^k$ versus $\varepsilon$, not a constant-factor gap. An $\widetilde O(s^{1/(2k)})$ gap to the new lower bound remains, and the single-qubit $\ell_2$ result carries a $\sqrt n$ penalty. Protocols require interleaved control, unlike control-free baselines.
