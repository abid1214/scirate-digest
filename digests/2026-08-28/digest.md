# SciRate Daily Digest — 2026-08-28

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Fault-tolerant quantum computation cannot be achieved with constant spacetime overhead

[arXiv:2608.26272](https://arxiv.org/abs/2608.26272) · [SciRate](https://scirate.com/arxiv/2608.26272)

*Kishor Bharti, Tobias Haug, Andrew Tanggara*

**TL;DR** For the simplest fault-tolerant task — storing $K$ logical qubits for $S$ steps at target diamond-norm error $\varepsilon$ under i.i.d. located-erasure noise — the minimum worst-case number of physical storage locations is shown to be $\Theta\!\left(S(K+\log(S/\varepsilon))\right)$, with a matching positive-rate CSS (Gilbert–Varshamov) construction. The relative spacetime overhead is therefore $\Theta(1+\log(S/\varepsilon)/K)$: constant only once $K=\Omega(\log(S/\varepsilon))$, and logarithmically growing for narrow, long-lived registers.

**The big picture** Error correction lets noisy hardware run reliable computations, but at the price of extra qubits and extra time. Much recent work has driven the qubit-count price down to a constant factor; this paper asks whether the *total* price — qubits multiplied by how long they are held — can also be a constant factor, and answers no in general. The unavoidable extra cost is a reliability tax that grows with how long information must survive, but it can be shared across many logical qubits at once, so wide algorithms can still amortize it away while protocols that nurse a small register for a very long time cannot.

**Key contributions**
- A tight (up to constants) characterization of cumulative memory cost under located erasure, valid for fully adaptive protocols whose physical width may depend on the measurement record.
- An adaptive lower bound: the survival probability of avoiding a "whole live register erased" event obeys $P_{\rm surv}\le\exp(-Sp^{C/S})$, via a dynamic-programming reduction to deterministic width allocation plus Jensen; combined with a Schmidt-number argument giving $C\ge KS$.
- A matching upper bound: CSS-GV codes of block length $N=O(K+\log(S/\varepsilon))$ with linear relative distance $>p$, Chernoff tail on erasure weight, telescoping over $S$ steps.
- A *conditional* circuit-level theorem: given a code/gadget family with rate $R_{\rm gad}$, $O(N)$ qubits and $O(1)$ depth per logical layer, and per-layer error $Ae^{-\beta N}$, one gets $C_{\rm FT}\le c\,T(K+1+\log(AT/\varepsilon))$.
- Singleton-type bounds for subsystem spacetime codes: $N_{\rm st}\ge k+r+2(d_{\rm st}-1)$, plus a pairing argument giving $P_L\ge\rho^{d_{\rm st}}/(1+\rho^{d_{\rm st}})$ for full-support product Pauli noise, hence a distance floor $d_\varepsilon^\star=\log((1-\varepsilon)/\varepsilon)/\log(q_{\max}/q_{\min})$.

**How it works** The memory model counts only *storage* locations (one qubit for one time step), which lower-bounds any gate-level location count. The lower bound is driven by a single catastrophic event — every live qubit erased in one step — which leaves the reference separable and caps Bell fidelity at $1/2$; requiring this to be $\lesssim\varepsilon$ over $S$ steps forces width $\gtrsim\log_{1/p}(S/\varepsilon)$. The $KS$ term follows from Schmidt-number/singlet-fraction monotonicity.

**Why it matters** It sharpens the "constant-overhead fault tolerance" narrative: constant *space* overhead is not the same as constant *spacetime* overhead, and the crossover $K\sim\log(S/\varepsilon)$ cleanly separates wide algorithms (Shor) from narrow long-lived ones (iterative phase estimation, quantum memory, networking, long-time simulation). Useful for architecture-level resource estimation.

**Caveats** The tight result assumes located erasure with *ideal, free, nonlocal* recovery — precisely where practical overhead lives; the CSS construction is nonconstructive and requires $p<\delta_{\rm GV}\approx0.11$. The lower-bound mechanism (total erasure of the live register) is coarse and may be far from tight for realistic Pauli noise. The circuit theorem is conditional on gadget assumptions not established here; the spacetime-code bound needs an unproven $N_{\rm st}\le c_{\rm loc}C_{\rm map}$ locality assumption. The title overstates: constant relative overhead *is* attainable for sufficiently wide computations. The authors disclose generative-AI assistance in ideation and drafting.

## 2. Optimal cloning of mixed states

[arXiv:2608.27298](https://arxiv.org/abs/2608.27298) · [SciRate](https://scirate.com/arxiv/2608.27298)

*Marco Fanizza, Dmitry Grinko, Thilo Scharnhorst, Jack Spilecki*

**TL;DR** The sample complexity of approximate mixed-state cloning is settled at $n=\Theta(krd/\varepsilon)$: the naive "purify–clone–trace" (PCT) channel — randomly purify the $n$ copies, run Werner's optimal pure-state cloner in the $rd$-dimensional space, trace out the ancillas — is optimal up to constants for rank-$r$ states in dimension $d$. The matching lower bound is proved on the restricted family of maximally mixed projector states $P/r$, and the same $\Theta(krd/\varepsilon)$ rate is shown for approximate transposition ($\rho^{\otimes n}\to(\rho^T)^{\otimes k}$).

**The big picture** No-cloning forbids exact copying, but says nothing about how well one can copy approximately, and the mixed-state version of this question had been open for decades — described in the literature as "a completely open domain". This work shows that the obvious strategy — pretend your mixed state is really a pure state on a bigger space, use the known optimal pure-state cloner there, then discard the extra registers — cannot be improved. Notably, the hardest instances are states whose eigenvalue distribution is already fully known; all the difficulty lies in identifying the support. This also breaks a folklore analogy with tomography, where the cost of learning a state does not scale the same way with the number of copies produced.

**Key contributions**
- Tight analysis of the PCT cloner: fidelity $\ge 1-krd/n$, via concavity of root-fidelity plus data processing over the random purification ensemble.
- Matching $\Omega(krd/\varepsilon)$ lower bound, holding already for rank-$r$ projector states, for $d\ge2$, $r\le d/2$, $\varepsilon\le1/16$ (explicitly $n\ge krd/(8\varepsilon)$).
- A new operator inequality: the Haar average $\int q_\lambda(P)^T\otimes q_\mu(P)\,dP \preceq \frac{s_{\lambda\cup\mu}(1^r)}{s_{\lambda\cup\mu}(1^d)} I\otimes I$, proved by showing the untransposed gap $\Delta_{\lambda\mu}$ is *separable*, not merely PSD.
- Tight $\Theta(krd/\varepsilon)$ bounds for approximate transposition.

**How it works** Fidelity to $\rho^{\otimes m}$ is upper bounded by the linear overlap $\mathrm{tr}(\mathcal{C}(\rho^{\otimes n})P^{\otimes m})$; the optimal channel may be taken permutation-invariant, so its Choi state is block-diagonal in the Schur basis with identity on multiplicity registers. Worst case is bounded by the Haar average over projectors, reducing everything to the partially-transposed integral above. Separability of $\Delta_{\lambda\mu}$ is established by induction on $r$ using "lift" maps that embed $\mathcal{Q}^{d-1}_{\lambda'}$ into $\mathcal{Q}^d_\lambda$, plus a hook-content Schur identity. The optimal output shape is $\mu=\lambda+k e_1$, yielding a bound $\mathbb{E}_\lambda\prod_{j}\frac{r+\lambda_1+j-1}{d+\lambda_1+j-1}$; plugging in $\mathbb{E}[\lambda_1]\le n/r+2\sqrt n$ (O'Donnell–Wright) closes the argument.

**Why it matters** Resolves a long-standing open problem, validates random purification as a generically sample-optimal reduction technique, and reinforces projector states as canonical hard instances. Relevant to quantum cryptography bounds, shadow/state-processing pipelines, and representation-theoretic optimization of covariant channels.

**Caveats** Constants in the lower bound are unoptimized and require $r\le d/2$, $\varepsilon\le1/16$; the bound uses worst-case-over-$\rho$ fidelity (global, not marginal, fidelity), so per-copy or average-case notions could behave differently. No claim about circuit efficiency of PCT, and the authors disclose that AI tools generated the recursion underlying the separability proof.

## 3. Strong Converse Exponent of Quantum State Merging

[arXiv:2608.27202](https://arxiv.org/abs/2608.27202) · [SciRate](https://scirate.com/arxiv/2608.27202)

*Mario Berta, Hao-Chung Cheng, Roberto Rubboli, Marco Tomamichel*

**TL;DR** The paper pins down the exact exponential decay rate of the optimal fidelity of one-way quantum state merging when the net entanglement cost per copy is below the conditional entropy (strong converse regime). The answer is a max over α∈[1,2] of (2(α−1)/α)[H↑_{α,α/2}(A|B)_ψ − r], i.e. the *optimized α-z* conditional Rényi entropy along the previously uninterpreted path z=α/2 — not the sandwiched (z=α) family that governs most strong converse exponents. Equivalently, by duality, the exponent is a club-sandwiched conditional entropy on the reference side, which also turns out to be the strong converse exponent of the *partially* smoothed conditional min-entropy in purified distance.

**The big picture** Merging one party's share of a shared quantum state into the other party's lab costs (or produces) entanglement at a rate set by the conditional entropy. If you try to do it with less entanglement than that, the protocol fails, and the interesting question is how fast the success probability collapses as the number of copies grows. This work computes that collapse rate exactly, and finds that it is governed by a family of entropic quantities that had until now no operational meaning in information theory — a genuinely different mathematical structure from the one that appears in essentially all comparable strong converse results. The finding also reveals that fixing a marginal during smoothing (as merging effectively requires) changes the answer relative to unconstrained smoothing, even though the two agree in the opposite, error-exponent regime.

**Key contributions**
- Exact strong converse exponent for state merging entanglement cost; positive iff r < H(A|B), with matching finite-block converse bound.
- First operational interpretation of α-z Rényi divergences with z=α/2, α>1, in a standard information-processing task.
- Exact strong converse exponent for the partially smoothed conditional min-entropy in purified distance (club-sandwiched form), contrasted with the sandwiched arrow-down form for global smoothing; consolidated in a comparison table with known error exponents.

**How it works**
*Converse:* Anshu–Berta–Jain–Tomamichel's one-shot reduction bounds cost by the partially smoothed conditional min-entropy; a noncommutative Hölder factorization of the fidelity into a 2α-norm term (yielding the club-sandwiched trace) and a 2α/(2α−1)-norm term controlled via Araki–Lieb–Thirring plus the two constraints τ_R ≤ ρ_R and τ_AR ≤ 2^{−q}I⊗ρ_R; additivity of the club entropy on the DPI boundary λ=(1−2α)/(1−α) plus club duality gives the α-z form.
*Achievability:* relative-entropy decoupling (Berta–Cheng–Yao) applied to an auxiliary state τ, with a Log-Euclidean change of measure and Sion minimax to produce the variational form min_τ {D(τ_AR‖ρ_AR)+D(τ_R‖ρ_R)+[q−H(A|R)_τ]_+}; the decoupling instrument (one Kraus operator per outcome) is converted to a merging protocol by an outcome-controlled Uhlmann recovery with a Cauchy–Schwarz branch argument; finally a *double* pinching (universal permutation-invariant state and ρ_R^{⊗m}) makes ρ_AR, ρ_R and the auxiliary state commute simultaneously while preserving the marginal, converting Log-Euclidean into club-sandwiched at O(log m/m) cost, followed by blocking m,k→∞.

**Why it matters** Fills the last open piece in the exponent landscape of a canonical quantum Shannon primitive, and shows the sandwiched-Rényi orthodoxy for strong converses is not universal: metric choice (purified distance) and marginal constraints select different Rényi paths. Relevant to anyone working on decoupling, one-shot/second-order quantum information, randomness extraction, and the theory of α-z divergences.

**Caveats** Finite dimensions; one-way LOCC with unlimited free classical communication and only the *net* entanglement difference constrained. The matching direct-regime error exponent is known tight only in the low-cost regime. The α range is capped at 2 (z=1, Petz endpoint), so for very small r the exponent is attained at the boundary. Club-sandwiched additivity/DPI is used only on the boundary λ=(1−2α)/(1−α); singular-optimizer cases are handled by regularization pointers to prior work rather than in full.

## 4. On supporting affine functionals for Entanglement of Formation

[arXiv:2608.27363](https://arxiv.org/abs/2608.27363) · [SciRate](https://scirate.com/arxiv/2608.27363)

*A. S. Holevo, M. E. Shirokov*

**TL;DR** The authors disprove a folklore assumption used in several papers: that the convex-roof structure of the entanglement of formation guarantees a global supporting affine functional (a subgradient) at every state of a finite-dimensional bipartite system. Using an equivalence between the existence of such a functional and Lipschitz lower semicontinuity, plus Wootters' concurrence formula, they exhibit an explicit rank-2 two-qubit state where the EoF drops like the square root of the perturbation parameter, hence no supporting functional exists; they also give positive results (local/global existence criteria and explicit Lipschitz bounds) for finite-rank states.

**The big picture** Entanglement of formation is a convex function on quantum states, and many arguments implicitly assume one can always touch it from below with a flat plane at any state — a subgradient — which is what convex duality gives you at interior points. At the boundary of the state space, where states are rank-deficient, this can fail, exactly as a semicircle-shaped convex curve has no finite tangent at its endpoints. The authors show that this failure genuinely occurs for entanglement of formation, already for the simplest two-qubit case, and therefore that any proof relying on the existence of such a plane at degenerate states is unsound. They also identify precisely when the plane does exist, and turn that into quantitative one-sided continuity estimates.

**Key contributions**
- Theorem 1: for a state ρ and any subspace ℋ₀ ⊇ supp ρ, the bound E_F(ρ) − E_F(σ) ≤ C‖ρ−σ‖₁ on 𝔖(ℋ₀) is equivalent to attainment of the Fenchel-dual supremum by some Λ_ρ with spectral diameter D(Λ_ρ) ≤ 2C; valid in infinite dimensions (EoF defined via continuous ensembles).
- Explicit counterexample: ρ = ½|Φ⁺⟩⟨Φ⁺| + ½|01⟩⟨01| on two qubits. Along ρ_t = (1−t)ρ + t|10⟩⟨10|, exactly C(ρ_t) = (1−t)/2 − √(2t(1−t)) for t ≤ 1/3, so E_F(ρ) − E_F(ρ_t) ≈ κ√2·√t with κ = ln(2+√3)/√3 ≈ 0.760 — infinite one-sided slope, hence no supporting functional. Extends to all bipartite systems by restriction (Corollary).
- Consequence: local supporting functionals (on supp ρ, which always exist in finite dimensions) need not extend globally.
- Positive results: for finite-rank ρ, support-restricted bounds with constant (log d − E_F(ρ))/λ_min or S(ρ_A)/λ²_min − E_F(ρ)/λ_min; these become unrestricted when supp ρ = supp ρ_A ⊗ supp ρ_B, via the extension Λ→P_ρΛP_ρ.

**How it works** The dual variational formula E_F(ρ) = sup{TrΛρ : ⟨ψ|Λ|ψ⟩ ≤ S(ψ_A)} follows from Fenchel–Moreau given lower semicontinuity. Attainment is proved by a minimax argument (Sion/Simons) on the σ-weakly compact ball 𝔅(C) together with a barycentric decomposition of measures over pure states, and shifting Λ by multiples of the identity to convert a norm constraint into a spectral-diameter constraint. Compactness of the constraint set in Lemma 3 gives attainment for finite-rank states with bounded pure-state marginal entropy on supp ρ. The counterexample computation (block-diagonal spin-flip spectrum) was, per the authors, found with LLM assistance.

**Why it matters** Anyone using subgradient/supporting-hyperplane arguments for EoF — in entanglement-measure continuity bounds, Gaussian/infinite-dimensional extensions, or channel capacity duality — must now check nondegeneracy or use the explicit constants given here.

**Caveats** The obstruction is at degenerate states only; nondegenerate states are fine. The Lipschitz constants scale as 1/λ_min (or 1/λ²_min) and thus blow up near the boundary, and the unrestricted bound requires the fairly special product-support condition supp ρ = supp ρ_A ⊗ supp ρ_B. Whether the discrete-ensemble definition (1) is lower semicontinuous in infinite dimensions remains open.

## 5. Quantum Chaos and Quantum Optimal Transport

[arXiv:2608.27350](https://arxiv.org/abs/2608.27350) · [SciRate](https://scirate.com/arxiv/2608.27350)

*Jordan Cotler, Felipe Hernández*

**TL;DR** The authors define a quantum Lyapunov exponent as the exponential growth rate of a quantum optimal-transport (Wasserstein-type) distance between pairs of states, and prove that for any transport distance satisfying four natural axioms it equals the *global classical expansion coefficient* in the semiclassical limit — which coincides with the usual maximal Lyapunov exponent in typical settings — while the OTOC exponent is bounded above by the same rate and saturates it only when maximally-expanding trajectories carry non-exponentially-small weight. A key technical move is restricting to state pairs whose initial separation is parametrically larger than the coherent-state scale, which cures a genuine divergence of the naive infinitesimal definition.

**The big picture** Classical chaos is defined by how fast nearby trajectories separate, but quantum states are smeared-out objects in a phase space where position and momentum cannot be simultaneously sharp, so there is no obvious notion of "distance between two nearby states." Optimal transport — the mathematics of the cheapest way to move one pile of earth into another — supplies exactly the missing ruler, and a recently developed noncommutative version of it works for quantum states. Using this ruler, the authors show that a faithfully defined quantum sensitivity-to-initial-conditions rate reproduces the classical chaos rate in the appropriate limit, and clarifies precisely when the widely used operator-scrambling diagnostic captures the same physics and when it undercounts it.

**Key contributions**
- An axiomatic notion of "admissible" quantum transport distance: translation invariance, exact translation distance, double convexity under classical mixing, and a Husimi data-processing lower bound.
- Theorem: any admissible distance sandwiches the classical Wasserstein distance between Husimi functions, with an additive error of order ħ^{1/2}; the upper bound follows from the first three axioms.
- Identification of a pathology: naive infinitesimal quantum Lyapunov exponents diverge (e.g. ε√log(1/ε) behavior near rank-deficient states), unrelated to chaos; cured by requiring separations ω(ħ^{1/2}).
- Main theorem λ_q = λ_exp ≥ λ_OTOC, with saturation criterion.
- Extension of the Carlen–Maas 1- and 2-Wasserstein distances from finite dimensions to L²(ℝ^D), proof of admissibility, and a symplectic distortion bound by ‖S‖; exact result λ_q = 1 with sharp e^t growth for the inverted oscillator.

**How it works** The lower bound λ_q ≥ λ_exp uses coherent states at near-maximally expanding points plus the translation axiom. The upper bound uses a companion "Wasserstein–Egorov" estimate showing the Heisenberg-evolved Weyl translation W = e^{iHt}τ_δe^{-iHt} is approximately e^{Ct}ħ^{1/2}-local in phase space, yielding d_p(ρ(T),σ(T)) ≤ J(T)d_p(ρ,σ) + O(e^{CT}ħ^{1/2}), where J(T) is the Lipschitz constant of the classical flow. The OTOC bound uses Bouzouina–Robert Egorov to reduce the commutator matrix to a classical tangent-map second moment.

**Why it matters** It gives quantum chaos a metric-geometric foundation that is state-level rather than operator-level, and shows OTOCs are a state-weighted lower bound on a more primitive quantity. Relevant to semiclassical analysis, quantum information geometry, and anyone using OTOCs as chaos diagnostics.

**Caveats** Everything is semiclassical: ħ→0 is taken before T→∞, so Ehrenfest-time and genuinely quantum (post-scrambling) effects are invisible, and λ_q is ultimately a classical quantity. Hamiltonians must lie in S₂(1) (bounded Hessian), excluding Coulomb, many-body spin systems, and QFT — precisely the hardest cases. λ_exp differs from λ_cl in general. The OTOC comparison uses only linear phase-space observables. Full proofs are in appendices and a companion paper; LLM assistance is disclosed for functional-analytic aspects.
