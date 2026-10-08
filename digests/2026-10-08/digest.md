# SciRate Daily Digest — 2026-10-08

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Building codes with transversal CCZ using projective geometry and SAT solvers

[arXiv:2610.09341](https://arxiv.org/abs/2610.09341) · [SciRate](https://scirate.com/arxiv/2610.09341)

*Bohan Lu, Kenneth R. Brown*

**TL;DR** The authors give a systematic recipe for CSS codes on three logical qubits whose logical CCZ is implemented by bare physical T/T† gates: the X-stabilizer support is forced (by Reed–Muller duality) to come from a low-degree Boolean polynomial, which simultaneously gives 8-divisibility and guarantees d_Z ≥ 3, after which a SAT solver or a small F₂ linear system picks the three X-logical operators. They produce 13 codes with n = 48 … 496 (d_Z = 3 or 4), exhibit a [[48,3,3]] example, and prove no such code (even allowing a diagonal Clifford correction) exists below n = 39, leaving n ∈ [39,46] open against the known n = 47 construction.

**The big picture** Fault-tolerant quantum computing needs a non-Clifford gate, and the cheapest way to get one is a code in which simply applying the same single-qubit rotation to every physical qubit enacts a useful logical operation. Finding such codes has largely been a matter of clever one-off constructions; here the search space is cut down by showing that the admissible stabilizer supports are exactly the point sets carved out by low-degree polynomials in a finite geometry, turning a brute-force hunt into a small, structured search that a satisfiability solver can finish. The same structure theory lets the authors prove a lower bound on how few physical qubits such a code can possibly use, narrowing the remaining gap to eight block lengths.

**Key contributions**
- A clean "nine conditions" criterion (overlap parities of logical/stabilizer rows) that is necessary and sufficient for quasi-transversal CCZ, derived by multilinear expansion of the T-gate phase mod 8 and a budget argument showing the diagonal Clifford can only shift degree-1 coefficients by multiples of 2 and degree-2 by 4.
- A block-length spectrum theorem: the stabilizer column indicator must lie in RM(s−4,s) ∪ (δ₀ + RM(s−4,s)), so admissible n equals |c| or |c|−1 for a degree-≤(s−4) polynomial c.
- A two-stage search: SAT over support plus label bits, or, for a fixed support, enumerate pairs (κ₁,κ₂) in V_P = ev_P(RM(2,s))^⊥ and solve a 2+2s+1 equation linear system for κ₃ by Gaussian elimination; then solve a mod-16 condition for the T/T† sign pattern.
- Thirteen explicit codes (n = 48 to 496), with the [[48,3,3]] code verified by hand via block-weight counting (three 16-column blocks, |γ| = 22).
- Lower bound n ≥ 39, via reduction to projective supports, affine-equivalence classification, an exclusion of affine-flat supports (labels lie in RM(m−3,m), so deg κ₁κ₂κ₃ ≤ m−1 and K3 fails), rank-reduction lemmas, and exhaustion of all 49,741,825 label pairs at s = 5.

**Why it matters** Transversal CCZ codes are a direct substitute for magic-state distillation; a geometric classification plus optimality bounds moves this from folklore constructions to a design methodology, and the length lower bound tells architects how little overhead is achievable.

**Caveats** Only d_Z is controlled (d_X and the full code distance get little attention); rate is fixed at k = 3 and the large-n codes have no better distance than the small ones. The SAT search is existential, not exhaustive, above s = 5, so these codes need not be optimal. No decoder, fault-tolerance, or overhead comparison against distillation is given, and the n = 39–46 window remains unresolved.

## 2. Efficient Estimation of Logical Sensitivities Through Fault-Counting

[arXiv:2610.10531](https://arxiv.org/abs/2610.10531) · [SciRate](https://scirate.com/arxiv/2610.10531)

*Winston Fu, J. Wilson Staples, Jeff D. Thompson*

**TL;DR** The authors apply the score-function (likelihood-ratio / REINFORCE) estimator to the fault-sampling distribution of stabilizer QEC simulations, yielding all partial derivatives of the logical error rate with respect to every physical noise parameter from a single Monte Carlo run at one noise point. In circuit-level surface code simulations the estimator matches central finite differences but reduces the shots needed for equal variance by 1–2 orders of magnitude, with a derived variance ratio ≈ s/(a²·E[M_i²|L]). They then use the gradients inside Newton root-finding to trace multi-dimensional finite-distance threshold contours.

**The big picture** When evaluating a quantum error-correcting code, one wants an error budget: how much each physical noise source (two-qubit gates, idling, measurement, individual qubits) contributes to logical failure. The standard way is brute force — nudge one noise rate, rerun the whole simulation and decoder, repeat for every noise source — which is expensive and forces you to decide in advance how to group errors. Here the authors notice that simulators already know exactly which faults occurred in each shot, information normally thrown away, and that this bookkeeping is enough to read off all the sensitivities at once from one simulation. The payoff is cheap, fine-grained error budgets down to individual qubits and time steps, plus a much faster way to map out where a code stops helping.

**Key contributions**
- Score-function estimator for ∂p_L/∂p_i evaluated on the physical fault distribution (not, as in prior QEC RL work, on a policy over candidate parameters), giving the full gradient from one dataset.
- Analytic variance-ratio prediction R_i ≈ s/(a²E[M_i²|L]), validated numerically; notes R_i grows ~quadratically with the number of parameters s (s = 268/1526/4544 for d = 3/5/7 at per-fault resolution).
- Post-hoc arbitrary regrouping of per-fault sensitivities: error-type budgets, spatial heatmaps (bulk qubits matter more than boundary), per-round breakdowns, and components of ∂Λ_d⁻¹/∂p_i.
- A local "effective distance" diagnostic d̂ = 2(ν p/p_L) − 1 from the summed gradient along the uniform-noise ray, recovering d at low p and → −1 as p_L → 1/2.
- Model-agnostic threshold-contour tracing: Newton steps on Δ = log p_L(d₂) − log p_L(d₁) with the gradient from the same shots, plus tangent-direction continuation, reducing sampling from O(K^s) to O(K^{s−1}).

**How it works** Faults are independent Bernoulli mechanisms with probabilities W_e(p) (an "inclusive" depolarizing parameterization, Appendix A). Writing p_L = E[L(E)] and differentiating the log-likelihood gives ν_i = E[L(E)(Σ_{e∈E} ∂W_e/W_e − Σ_{e∉E} ∂W_e/(1−W_e))]. Since L is zero for most shots, only failing configurations contribute: the estimator essentially measures how over-represented channel-i faults are in logical failures. At small p the score behaves as M_i/p_i, giving the variance scaling. Validation: unrotated surface code in Stim, d = 3,5,7, 10⁻³ ≤ p ≤ 10⁻², up to 2×10⁹ shots, bootstrapped; FD bias becomes visible at step fraction a ≳ 0.2. Contours traced with PyMatching, correlated PyMatching, and Tesseract for (3,5) and (5,7) pairs, converged to |Δ| ≤ 2σ_Δ.

**Why it matters** Error budgeting is now routine in experimental QEC papers; this turns a per-parameter simulation campaign into free post-processing of existing runs, and makes per-qubit/per-location sensitivity maps practical for heterogeneous hardware and resource-allocation decisions. It applies to any independently sampled stochastic mechanism — erasure, leakage, correlated faults — not just Pauli noise.

**Caveats** Requires independent fault sampling and simulator access to fault configurations, so it is a simulation tool, not an experimental one; the decoder is held fixed (decoder priors are not re-differentiated, so these are sensitivities at fixed decoder). Score-function variance generically grows with the number of fault locations per shot, and only first-order derivatives are demonstrated — threshold-contour curvature and second-order terms are left to future work. Threshold contours are finite-distance crossings, not asymptotic thresholds. Concurrent independent work (Ref. on optimizing QEC) is noted.

## 3. Witnessing Quantum Bayesian Inference beyond Classical Learning

[arXiv:2610.09293](https://arxiv.org/abs/2610.09293) · [SciRate](https://scirate.com/arxiv/2610.09293)

*Francesco Buscemi*

**TL;DR** A two-draw "forecast table" produced by quantum Bayesian retrodiction (Petz-style update $\gamma_x \propto \sqrt{\gamma}P_x\sqrt{\gamma}$, then re-predicting the same POVM) is exactly a *completely positive semidefinite* matrix, whereas any classical "learn the unknown urn, then forecast" model produces a *completely positive* matrix. Since doubly nonnegative matrices of order ≤4 are always CP (Maxfield–Minc), no separation exists up to four outcomes in any Hilbert-space dimension; at five outcomes a single qubit with a pentagon-arranged POVM and the maximally mixed prior violates an explicit classical bound, achieving $(3+\sqrt5)/10 \approx 0.5236 > 1/2$.

**The big picture** Suppose you can only see an agent's predictions: its initial forecast and its revised forecast after one observation. Can you tell whether the agent is reasoning with ordinary probability — learning about a fixed but unknown source from repeated draws — or with quantum theory? This paper shows the answer is yes, but only once the measurement has at least five possible outcomes; below that threshold, every quantum forecast pattern, even from genuinely incompatible measurements, can be mimicked by some classical urn-learning story. The separation is certified by a single inequality involving only the observed forecasts, with no need to know the agent's internal model, its prior, or how many hidden hypotheses it entertains.

**Key contributions**
- Identifies classical conditionally-i.i.d. Bayesian forecasting with the cone of completely positive matrices, and quantum retrodictive forecasting with the completely positive semidefinite cone (including the real/complex reduction via realification).
- Proves a sharp outcome-number threshold: all quantum retrodictive tables with $n\le 4$ admit a classical realization with at most $n$ urns, in any finite dimension.
- Gives an explicit classical urn realization of the tetrahedral (informationally complete) qubit POVM table — showing noncommutativity alone is not witnessable.
- Derives a classical witness $\mathcal B_5(T)=2\sum_j T_{j,j+1}\le 1/2$ from the five-cycle Motzkin–Straus bound, with an elementary proof and tightness example.
- Exhibits a minimal qubit counterexample (five coplanar Bloch vectors at $2\pi j/5$, $\gamma=I/2$) violating it.

**How it works** Classical realizability means $T=BB^{\mathsf T}$ with $B\ge0$ entrywise, which converts directly into a prior $r(z)=s_z^2$ and compositions $u(x|z)=B_{xz}/s_z$. Quantum tables factor as $T_{xy}=\mathrm{Tr}(Q_xQ_y)$ with $Q_x=\gamma^{1/4}P_x\gamma^{1/4}\succeq0$; conversely any such Gram matrix is realized by $\gamma=S^2$, $P_x=S^{-1/2}Q_xS^{-1/2}$. Both classes are symmetric, entrywise nonnegative and PSD; the gap between CP and doubly nonnegative opens only at $n\ge5$, and the pentagon/Horn-matrix inequality separates them.

**Why it matters** It turns the CP-vs-CPSD gap — previously studied for psd-rank and correlation cones — into an operational statement about agents' forecasts, connecting quantum retrodiction to the econometric question (Fudenberg–Lanzani) of when forecasts are Bayesian-explainable. Relevant to quantum foundations, quantum Bayesianism, and anyone interested in behavioral tests of quantum reasoning.

**Caveats** The "classical" benchmark is narrow: a fixed sampling law, conditionally i.i.d. draws, same law for both draws — latent dynamics or non-i.i.d. learning are not excluded. The quantum side assumes one specific retrodiction rule and that the agent re-measures the same POVM. The $5\times5$ matrix and its separating inequality already appear in the psd-rank literature; the novelty is the retrodictive interpretation and threshold statement. Noise robustness, the maximal quantum value of $\mathcal B_5$, dimension dependence, and any device-independent version remain open.

## 4. Efficiently computable bounds on the energy-constrained quantum reading capacity

[arXiv:2610.08945](https://arxiv.org/abs/2610.08945) · [SciRate](https://scirate.com/arxiv/2610.08945)

*Vishal Singh, Zixin Huang, Mark M. Wilde*

**TL;DR** The paper gives the first uniformly computable (semidefinite-programming-representable) converse bound on the energy-constrained quantum reading capacity of an arbitrary finite family of finite-dimensional channels, valid against fully adaptive protocols. The bound follows from an input-dependent chain rule for the Belavkin–Staszewski (BS) relative entropy, expressed via Choi operators and the operator relative entropy, with the average-energy constraint dualized into a Lagrangian operator inequality; a complementary bilinear-SDP relaxation of the standard non-adaptive Holevo rate supplies achievable rates via see-saw optimization. For jointly classical–quantum channel families, an Umegaki-based converse matches the non-adaptive rate in the unconstrained case, re-deriving the recent result that adaptivity does not help there.

**The big picture** Quantum reading asks how much classical information can be retrieved from a memory whose cells are physical processes, by sending in quantum probes and measuring what comes out — a model relevant to optical disc readout and more generally to channel discrimination with coding. Previous capacity bounds were either information-theoretic expressions involving unbounded reference systems, or tailored to channels admitting special simulations, so they could not be evaluated numerically for a general family, especially under a realistic constraint on probe energy. This work converts both the upper and lower bounds into finite-dimensional convex (or bilinear) optimizations whose size depends only on the channel dimensions, so capacity can actually be bracketed numerically. It also confirms, by an independent route, that for an important class of memories the simplest, non-adaptive readout strategy is already optimal.

**Key contributions**
- Converse on the energy-constrained reading capacity against arbitrary adaptive protocols: an infimum over a "reference" channel Choi operator plus Lagrange multipliers, with constraints of the form (partial trace of operator relative entropy of Choi operators) transposed ≤ λI + μH; objective λ + μE.
- Reduction, at zero energy constraint, to the BS channel information radius inf_S max_x D̂(N^x‖S).
- Observation that the Fawzi–Saunderson semidefinite approximations of operator relative entropy make the bound evaluable in poly(d); explicit SDP given in an appendix.
- A bilinear-SDP lower bound, built from Jenčová's integral representation of Umegaki relative entropy and its discretized SDP hierarchies, such that *any feasible point* yields a certified achievable rate (probe state + prior, evaluated via Holevo information); alternating minimization gives SDP blocks.
- For jointly classical–quantum families, a tighter Umegaki converse using the cq chain rule of Wang et al., matching the non-adaptive rate without energy constraint — an independent proof of the Pascual Abraldes–Winter result.

**How it works** The converse proceeds by converting a reading code into a hypothesis test distinguishing the true memory-encoded channel sequence from a fixed "useless" channel S, bounding log|M| by the hypothesis-testing relative entropy, relaxing to Umegaki, then to BS (D̂ ≥ D) so the input-dependent chain rule applies. Iterating the chain rule telescopes the accumulated information into a sum of terms linear in the average probe marginal, so the average-energy constraint enters as a linear constraint on that marginal; SDP duality over that marginal produces λ + μE.

**Why it matters** It supplies a practical numerical toolkit — two-sided, certifiable bounds — for a capacity that had only abstract characterizations, and the dualization of average-energy constraints via chain rules should transfer to other energy-constrained adaptive capacities (discrimination, estimation, channel coding).

**Caveats** Only finite-dimensional channels and finite alphabets are treated, so the original photonic/CV reading setting is not covered directly. The BS relaxation is lossy in general, so the gap to the achievable rate need not close except for jointly cq channels (and there only without an energy constraint). The lower bound's bilinear program is non-convex; see-saw gives no global-optimality guarantee, and the achievability restricts to non-adaptive, i.i.d. pure probes with |R| = |A|. Efficiency is "poly(d)" up to the accuracy of the operator-relative-entropy approximation hierarchy.

## 5. Gaussian Scrooge Ensemble from Deep Thermalization in Free-Fermions

[arXiv:2610.10279](https://arxiv.org/abs/2610.10279) · [SciRate](https://scirate.com/arxiv/2610.10279)

*Angelo Russotto, Katja Klobas, Pasquale Calabrese, Bruno Bertini*

**TL;DR** — In an XX free-fermion chain measured in the bath with Gaussianity-preserving, particle-number-breaking Majorana-bilinear measurements, the late-time projected ensemble converges to a *fermionic Gaussian Scrooge ensemble*: the Haar measure on the manifold of pure Gaussian states distorted so that its first moment is the subsystem's reduced GGE. The key physical claim is that although individual outcomes do carry information about local conserved charges at finite size, this information washes out as O(L_A²/L_B), making a partially revealing basis *effectively* non-revealing in the thermodynamic limit.

**The big picture** — When you measure the environment of a quantum system and record the outcomes, the system collapses into a random pure state; the statistics of that random state is a much finer probe of equilibration than the usual local averages. In chaotic systems with conserved quantities, this distribution is expected to be a tilted version of the uniform distribution over states. Here the authors show that the same picture survives in an integrable, non-interacting chain with infinitely many conservation laws — provided one restricts to the smaller manifold of Gaussian states — and, importantly, that the answer can be written purely in terms of the subsystem's own equilibrium state, with no reference to the global wavefunction. This clarifies when environment measurements genuinely leak conserved-charge information and when that leakage is irrelevant, which matters for using many-body dynamics as a source of structured randomness.

**Key contributions**
- Explicit subsystem-level construction of a fermionic Gaussian Scrooge ensemble, including the induced nonlinear map on covariance matrices Γ′ = Γ_GGE + SΓ(1−Γ_GGE Γ)⁻¹S with S = √(1+Γ_GGE²), and the Haar reweighting 2^(−L_A)√det(1−Γ_GGE Γ).
- Argument for "effective non-revelation": conditional bath-charge variances are extensive (e.g. Var_z(N_B) = b_z ≈ L_B/4; Var_z(J_B) = L_B/4 − 1/2 exactly), so conditional subsystem states collapse to the unconditioned one up to O(L_A²/L_B).
- Proof that no conserved charge can be *perfectly* revealed by this protocol (requires [X,E_α]=0 ∀α ⇒ X=0), while fermion parity is always exactly revealed, since M₁M₂ = −P for the whole SO(4) family of protocols.
- Symmetry classification of trajectory-preserved (anti)unitaries, yielding exactly two candidate infinite-temperature ensembles: the Gaussian Haar ensemble on O(2L_A)/U(L_A), or a constrained ensemble (Γ off-diagonal with R ∈ O(L_A)) when the initial state is invariant under an antiunitary T.

**How it works** — Each bath two-site cell is measured in the Bell-like basis of two commuting Majorana bilinears (Y X and −X Y in spin language), a rank-1, Gaussianity-preserving, U(1)-breaking projection. Covariance-matrix methods give the projected states in polynomial time. Convergence is tested via Frobenius distances Δ^(k) of correlation-matrix moments up to k=4 (~10⁴ samples per time), and via the projected-ensemble-averaged, space-averaged von Neumann entropy, which depends on all moments. Néel initial states (T-invariant) flow to the constrained ensemble; the critical staggered-SSH ground state (T-breaking, n(k)=1/2) to the unconstrained one; dimer states with α=0.5 and α=e^{2i/(1+√5)}/2 flow to the finite-temperature Gaussian Scrooge ensemble, indistinguishable from the earlier global "deep-GGE" construction.

**Why it matters** — It replaces a global representative-state recipe with a local, closed-form universal ensemble fixed solely by the reduced GGE, and sharpens the charge-revelation taxonomy by showing that finite-size partial revelation need not spoil Scrooge universality. Relevant to deep-thermalization theory, monitored free fermions, and randomness benchmarking.

**Caveats** — Numerics are limited to L_A = 2–4 and moments k ≤ 4; since the parity-resolved and full Gaussian Haar ensembles only differ at k ≥ L_A, the distinction is barely probed. The finite-temperature non-revelation argument is heuristic (extensive variance of Born-typical charges) — the clean generator-ensemble derivation exists only at infinite temperature, and the charges do not commute, so only linear combinations' marginals are controlled. Convergence Δ^(k)→0 is power-law and numerical, not proven; the ordering L_B→∞ then t→∞ is assumed throughout, and the extension to interacting integrable models is left open.
