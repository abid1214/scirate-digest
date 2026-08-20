# SciRate Daily Digest — 2026-08-20

The top 10 papers on [SciRate](https://scirate.com/) today.

## 1. Quantum Speedups Require Structure or Depth

[arXiv:2608.19158](https://arxiv.org/abs/2608.19158) · [SciRate](https://scirate.com/arxiv/2608.19158)

*Guy Blanc, Jordan Docter, Carmen Strassle, Li-Yang Tan*

**TL;DR** The authors resolve the folklore "simulation conjecture" (every $t$-query quantum algorithm is approximable on most inputs by a $\mathrm{poly}(t)$-query classical algorithm) for *parallel* quantum algorithms: any $t$-query, $d$-round algorithm can be simulated on all but a $\delta$-fraction of inputs using $t^{O(d^2)}\log(1/\delta)^{O(1)}$ classical queries (improved to $t^{O(d)}$ in a follow-up note). The route bypasses the Aaronson–Ambainis polynomial conjecture entirely, instead reasoning directly about BBBV *query weights* plus Talagrand's convex-distance inequality.

**Key contributions**
- A new "quantum-native" conjecture replacing influences with query weights: every $t$-query algorithm has a variable with $\E_\bx[W_i(\bx)] \ge \mathrm{poly}(\mathrm{Var}/t)$. Since query weights upper-bound influences, this is formally weaker-looking yet still implies the simulation conjecture.
- A regularity lemma: greedily querying variables of weight $>\eta$ yields a classical decision tree of depth $\mathrm{poly}(t,1/\eta,\log 1/\delta)$ after which the residual algorithm is $\eta$-regular w.h.p.
- Proof of the conjecture for $t$-parallel $d$-round algorithms: $\max_i \E[W_i] \ge 2^{-\Omega(d^2)}(t\log(1/\delta))^{-\Omega(d)}$; a one-page proof for $d=1$ (nonadaptive) via McDiarmid.
- An *algorithmic* regularity lemma showing the classical approximator is time-efficient assuming only $\mathsf{PromiseBPP}=\mathsf{PromiseBQP}$ (vs. AA's $\mathsf{P}=\mathsf{P}^{\#\mathsf{P}}$), yielding equivalences for $\mathsf{BPP}$ vs. $\mathsf{BQP}$/$\mathsf{QNC}$ relative to a random oracle.

**How it works** BBBV's hybrid method gives $\sum_r \dist_{\mathcal D_x^{(r)}}(x,y)=\Omega(1/d)$ for $x\in\mathrm{Acc}$, $y\in\mathrm{Rej}$, where $\mathcal D_x^{(r)}$ is the round-$r$ distribution over query sets. Because the metric depends on $x$, McDiarmid fails; Talagrand's convex-distance inequality supplies the needed concentration provided $\|W(x)\|_\infty$ is small for most $x$. That is established inductively: each round-$r$ weight $w_i^{(r)}(x)$ is itself the acceptance probability of an $(r-1)$-round algorithm, so Talagrand converts exponential tail bounds at rounds $<r$ into one at round $r$. Naively this forces thresholds $\gamma_{r-1}\ll\gamma_r^2$ (hence $2^{-2^d}$). Replacing "no heavy coordinate" by "$(m,\gamma)$-spread" ($\Pr_{\bS}[\bS\cap T\ne\emptyset]\le\gamma$ for all $|T|=m$), plus a stronger set-level hybrid bound and a greedy-hitting-set argument, improves the recurrence to $\gamma_{r-1}\le c\gamma_r$, giving $2^{-O(d^2)}$. Dependence on $N$ is removed by setting $N=\mathrm{poly}(2^{td},1/\delta)$.

**Why it matters** This is the first unconditional progress past the $\exp(t)$ hypercontractivity barrier that has stood since DFKO'07, for a natural and broad class (all of $\mathsf{QNC}^0$-like constant-depth query algorithms). It sharpens "quantum speedups need structure" into "structure or depth": superpolynomial unstructured speedups need superconstant depth, exponential ones polynomial depth — notable since many known speedups are low-depth. The query-weight/Talagrand toolkit is a plausible route to the full conjecture.

**Caveats** Only parallel/bounded-round algorithms; the bound is vacuous once $d\gtrsim \log t$, so genuinely adaptive $t$-query algorithms remain open. The random-oracle results are conditional equivalences, not separations. The $N$-removal step and the $(m_r,\gamma_r)$ parameter setting are somewhat lossy. Quantitative improvements ($t^{O(d)}$, round-preserving) are deferred to a companion note.

## 2. Integer Linear Programming Decoder for Abelian and Non-Abelian Topological Codes

[arXiv:2608.18512](https://arxiv.org/abs/2608.18512) · [SciRate](https://scirate.com/arxiv/2608.18512)

*Dian Jing, Aubrey Zhang, Liang Jiang, Ruben Verresen*

**TL;DR** The authors recast minimum-weight decoding of arbitrary topological orders as an integer (in fact binary) linear program, encoding anyon fusion rules and noise correlations as linear constraints via auxiliary fusion-channel indicator variables. This yields near-optimal thresholds for ℤ₂ depolarizing noise (18.039(7)% vs. optimal 18.9(3)%) and the ℤ₃ TO (15.346(5)% vs. optimal 15.8(2)%, beating RG decoders' <13%), and beats two-step MWPM for the non-Abelian D₄ TO.

**Key contributions**
- A general ILP/BLP formulation for decoding any anyon model: binary error variables ε_i for local incoherent anyon-creation events, plus binary fusion variables g_{f→a,s} selecting which fusion channel produces the measured syndrome a at site s.
- Constraints Σ_{f∈F_a} g_{f→a,s} = 1 and Σ_{ε_i↦b at s} ε_i = Σ_f N_{f,b} g_{f→a,s} (per species b, per site) enforce fusion consistency; objective w·x = ln[P(σ|E)P(E)] makes the LP optimum the MAP error configuration, so the decoder is a direct non-Abelian analog of MWPM.
- Worked instances: ℤ₂ under correlated (Y-error) depolarizing noise using mod-2 slack variables n_s∈{0,1,2}; ℤ₃ with the tri-fusion rule e×e×e=1 (no pairwise matching exists) using mod-3 slacks; D₄ (≅ℤ₄⋊ℤ₂) on the three-colorable kagome lattice.
- Spacetime extension for noisy syndromes: 3D lattice with defects Δ *and* raw syndromes **a** as input (needed because e.g. a×b=a lets an error go undetected), with incoming/outgoing temporal-string multiplicities N^in, N^out; a just-in-time variant for continuous correction.
- Physics result: the D₄ error-correction phase diagram has only one classical-memory phase (protecting Ẑ_L), unlike ℤ₂³, since m-anyon proliferation drags e-anyons along — decoder-independent across all variants tested.

**How it works** For D₄ three weight choices are compared: (i) maximize P(E) only (w_{f→a,s}=0), which over-trusts intrinsic heralding of m-strings by e-anyons and degrades badly at large p_z; (ii) full P(σ|E)P(E), which adds an entropic penalty per fusion event along m-strings and matches MWPM at large p_z; (iii) a single tunable effective ratio r_eff = w_m/w_e, optimized per noise point, which dominates all others across the phase diagram. Solved with Gurobi; D₄ simulation uses generalized stabilizer-tableau updates.

**Why it matters** Provides the first non-clustering, fusion-aware, general-purpose decoder for non-Abelian codes, closing much of the historic gap between clustering thresholds and matching/optimal thresholds — relevant for D₄-based non-Clifford gates already realized on trapped-ion hardware.

**Caveats** ILP is NP-hard; only empirical evidence of polynomial mean/median runtime subthreshold, with sharp slowdown at threshold. P(σ|E) is approximated by a product of local fusion probabilities, discarding global "isolated cluster fuses to vacuum" conditions. Best D₄ performance requires heuristically tuned r_eff, not a first-principles weight. Restricted to incoherent anyon noise with definite species labels; D₄ is acyclic and self-conjugate, so cyclic models (e.g. Fibonacci) remain untested. Measurement-error and JIT sections are truncated here, so those thresholds are unverified.

## 3. (Almost) quadruply optimal unitary designs in 1D

[arXiv:2608.18650](https://arxiv.org/abs/2608.18650) · [SciRate](https://scirate.com/arxiv/2608.18650)

*Guoding Liu, Jonas Helsen*

**TL;DR** The paper constructs explicit 1D-local, ancilla-free $\varepsilon$-relative-error unitary $k$-designs at depth $O(\log(n/\varepsilon)+k\log k)$ using $O(nk\log k)$ $T$ gates, valid for $k=O(n)$ — matching the $\Omega(\log(n/\varepsilon)+k)$ depth and $\widetilde\Omega(nk)$ magic lower bounds up to a single $\log k$. The two technical engines are a reduction of the magic-block locality in magic-augmented Clifford circuits from $O(k\log k)$ to $O(\log k)$, and a constant-size, constant-depth, 1D-local generating set with $\Omega(1)$ Kazhdan constant for the Clifford group.

**Key contributions**
- Main theorem: 1D design with depth $O(\log(n/\varepsilon)+k\log k)$, no ancillas, relative error, $k=O(n)$ (previously $k=o(\sqrt n)$ with $2^{O(k\log k)}$ depth in Zhang et al.); $T$-count $O(nk\log k)$, independent of $\varepsilon$, improving on $O(\log^2 k(nk+\log(1/\varepsilon)))$ for $t$-doped Clifford circuits.
- Locality reduction: $\ell\ge 8\log k$ (i.e. $2^\ell\ge k^8$) suffices for tensor-product $\ell$-local random unitaries to kill all non-permutation Clifford commutant elements, versus $\ell=O(k\log k)$ before.
- Theorem: an explicit symmetric generating set $S_{\mathrm{Cl},\ell}$ of the full Clifford group with $|S|\le 451$, each element of $O(1)$ 1D nearest-neighbor depth, and Kazhdan constant $\Omega(1)$ — of independent interest for randomized benchmarking/verification.
- 1D constant-depth realization of Kassabov's permutation-group generators via a "folded-qubit" layout (previously only all-to-all or periodic-boundary 1D), giving a fully 1D-local constant-gap CPZPC generating set: $\ell$-qubit design in depth $O(\ell k+\log(1/\varepsilon''))$ for $k\le c\,2^{\ell/6.1}$.
- Remark: combining prior results yields all-to-all designs at depth $O(\log\log(n/\varepsilon)+\log^2 k)$ (with $nk\widetilde O(\log k)$ ancillas) or $O(\log\log(n/\varepsilon)+k\log k)$.

**How it works** Block-brickwork of two overlapping layers of $2\xi$-qubit blocks with $\xi=\Theta(\log(n/\varepsilon)+k)$; the gluing lemma (Schuster et al.) lifts $(\varepsilon/n)$-designs on blocks to an $n$-qubit $\varepsilon$-design. Each block is a random Clifford sandwiched by tensor products of $\ell=O(\log k)$-qubit designs with error $\varepsilon''=2^{-2\ell k}$. The analysis expands the Clifford twirl in the stochastic-Lagrangian-subspace basis $\Sigma_{k,k}$, splitting into (i) the permutation block, where the Clifford–Haar Weingarten discrepancy is bounded by $k!2^{k-2\xi+3}$; (ii)/(iii) non-permutation terms, controlled by $\eta=\|(2^{\xi k}\mathrm{Wg}_C)^{-1}-\mathbb{1}\|_{\infty\to\infty}\le 2^{k-\xi}$ (via Gaussian-binomial counting) times $f(T)^{2\xi/\ell}$, where $f(T)=\|\Phi_H^{(k)}(T)\|_\infty$ on $\ell$ qubits; the new lemma gives $\sum_{T\notin S_k} f(T)^{2\xi/\ell}\le k!2^k(k^4/2^\ell)^{2\xi/\ell}$ by exploiting permutation invariance and focusing on commutant elements nearest identity. The Clifford expander is built from a 1D-local $\mathrm{SL}(\mathbb{F}_2)$ generating set (Kassabov/Nikolov), extended to the symplectic group by bounded products of automorphic images, then to the projective Clifford group via Pauli extension and to the full group by an abelian phase extension, using Hadad's extension bound and bounded-product Kazhdan comparison.

**Why it matters** It essentially settles the 1D depth question for unitary designs, decoupling $n$ and $k$ while simultaneously near-optimizing depth, error, ancilla count (zero), and magic — the last being the fault-tolerantly expensive resource. The 1D constant-depth Clifford expander is a reusable primitive.

**Caveats** A $\log k$ gap remains in depth and $\log^2 k\log n$-type gaps in magic; removing the former requires Weingarten analysis in the singular $2^\ell<k$ regime. Restricted to $k=O(n)$ (Clifford Weingarten singular for $k\ge n$). Constants are large (451 generators, $\ell\ge 8\log k$, $k\le c2^{\ell/6.1}$ with small $c$), so practicality at modest $n,k$ is unclear. Concurrent/overlapping work (Bär et al.; Anshu et al.) provides alternative routes to some ingredients. Source is truncated, so several key lemma proofs were not verifiable here; the authors also disclose LLM assistance in deriving initial estimates for two lemmas.

## 4. Quantum Mixedness Testing with Pauli Measurements

[arXiv:2608.18839](https://arxiv.org/abs/2608.18839) · [SciRate](https://scirate.com/arxiv/2608.18839)

*Jayadev Acharya, Abhilash Dharmavarapu, Yuhan Liu, Nengkun Yu*

**TL;DR** The paper pins down the copy complexity of testing whether an $N$-qubit state is maximally mixed using only single-qubit (Pauli-basis) measurements: $\widetilde\Theta(\sqrt{10}^{\,N}/\varepsilon^2)$, i.e. $\approx d^{1.66}/\varepsilon^2$ — strictly between the $d^{1.5}$ achievable with arbitrary single-copy POVMs and the $d^2$ needed with two-outcome Pauli observables. The upper bound comes from a randomized Pauli-basis protocol built on a new Krawtchouk-polynomial uniformity tester; the lower bound from a measurement-dependent Le Cam/mutual-information framework.

**Key contributions**
- Matching (up to $\mathrm{poly}(N)$, here $N^5$) upper and lower bounds of $\sqrt{10}^{\,N}/\varepsilon^2$ for single-qubit mixedness testing, separating Pauli *basis* measurements from both general single-copy measurements and single Pauli *observables*.
- "Pauli influence" $L_P=\sum_{Q\triangleleft P}3^{w(Q)}\alpha_Q^2$, with a work-investment lemma: for uniform $P$, some $i$ satisfies $\Pr[L_P\ge 3^{i-2}L]\ge 3^{-i}/N$.
- A new primitive: uniformity testing of *$(\Delta,k,\beta)$-correlation-concentrated* distributions on $\{\pm1\}^N$ with $O(\sqrt{\binom{N}{k}}\log(1/\delta)/(\beta\Delta))$ samples and $O(n^2kN\log N)$ time — an exponential runtime improvement over parity-enumeration estimators (which need $\Omega(\binom{N}{k})$ evaluations).
- A measurement-dependent adaptive lower-bound framework: $\chi^2$/KL bounds controlled by $\sup_{\mathcal M}\sum_m\langle\Lambda_{\mathcal M}(V_m),V_m\rangle$ over a basis chosen adversarially against the allowed POVM set (recovers $\Omega(\sqrt8^{\,N}/\varepsilon^2)$ for a complete basis).

**How it works** Measuring in Pauli basis $P$ yields a hypercube distribution whose Fourier coefficients are exactly the Pauli coefficients $\alpha_P(S)$, $Q\triangleleft P$. Rather than a collision estimator (which sees all $2^N$ coefficients and costs $\sqrt d$), they replace the indicator $d\mathbb 1[x=y]=\sum_k K_k^{(N)}(d_H(x,y))$ by the single degree-$k$ Krawtchouk term, giving an unbiased estimator of $\|\alpha^{=k}\|_2^2$ with standard deviation scaling as $\sqrt{\binom Nk}$, evaluable via a three-term recurrence. Levin work investment over $3^i$ random bases plus a weight-$w$ sweep yields total cost $\max_w 3^w\sqrt{\binom Nw}=\sqrt{9^w\binom Nw}\le\sqrt{10}^{\,N}$, tight at $w=9N/10$ — precisely the weight range used in the lower-bound hard ensemble (random $\pm$ perturbations of $\rho_{\rm mm}$ along Pauli directions).

**Why it matters** Establishes a sharp, experimentally relevant complexity landscape for the most implementable measurement class, quantifying exactly how much randomized Pauli-basis readout buys over fixed Pauli observables. The Krawtchouk estimator should be reusable for $k$-wise uniformity testing and shadow-style Fourier estimation.

**Caveats** $\mathrm{poly}(N)$ slack ($N^5$ in the tester); the algorithm is non-adaptive while the lower bound covers adaptive single-copy schemes (so adaptivity provably doesn't help here, but constants/log factors remain open). The full Pauli-specific lower-bound instantiation is in a truncated section and not verifiable here; the hard construction needs $d^{3/2}\le\ell\le d^2-1$ and small constant $c\le1/200$, and the $\varepsilon$ regime dependence isn't spelled out. Extensions beyond mixedness (general state certification, adaptive bases) are left open.

## 5. Subsystem Symmetries and Fracton Models in Quantum Error Correction

[arXiv:2608.18961](https://arxiv.org/abs/2608.18961) · [SciRate](https://scirate.com/arxiv/2608.18961)

*Giovanni Canossa*

**TL;DR** — A thesis-length study connecting classical 3D Ising models with subsystem symmetries to fracton codes, whose centerpiece is a statistical-mechanics-mapping determination of the optimal code-capacity threshold of the checkerboard code, $p_c = 0.107(3)$. This value saturates the entropic upper bound for zero-rate CSS codes ($H(p)=1/2 \Rightarrow p\approx0.110$), making it the highest known optimal threshold for a 3D code, and the saturation is attributed to Kramers–Wannier self-duality of the associated spin models.

**Key contributions**
- Detailed characterization of two 3D self-dual subsystem-symmetric Ising models: the Tetrahedral Ising model (TIM, four-spin tetrahedral terms on the FCC lattice) and the Fractal Ising model (FIM, two four-body terms on the cubic lattice), including their symmetry generators, constraints, and sub-dimensional order parameters.
- Explicit counting of planar $\mathbb{Z}_2$ subsystem symmetries in the TIM: $3L$ plane-flip generators minus 3 relations, giving $\log_2 \mathrm{GSD}=3L-3$; fractal symmetries of the FIM derived via Haah's polynomial-ring formalism (kernel of the excitation map $\varphi(f)=(\bar\varepsilon_1 f,\bar\varepsilon_2 f)$ with $\bar\varepsilon_1=1+\bar x+\bar y+\bar z$, $\bar\varepsilon_2=1+\bar x\bar y+\bar y\bar z+\bar z\bar x$).
- Prediction and numerical confirmation of *non-standard* first-order finite-size scaling: with subextensive degeneracy $2^{3L^{D-d}}$, $\beta_c(L)=\beta^\infty - 3\ln 2/(L^{d}\Delta\hat e)$, i.e. $L^{-2}$ rather than the usual $L^{-D}$ volume law.
- Threshold $0.107(3)$ for the checkerboard code and a general argument that any zero-rate CSS code whose $X$- and $Z$-noise stat-mech models are Kramers–Wannier duals of each other saturates the CSS capacity bound.

**How it works** — Gauging the subsystem symmetries of the TIM/FIM produces fracton stabilizer models (checkerboard-type and fractal codes). The optimal decoder threshold is then obtained by the standard random-bond mapping: quenched disorder along the Nishimori line, with the multicritical point locating $p_c$. Because the underlying classical model is self-dual, the Nishimori point coincides with the self-dual point, and a generalized entropy relation between the dual models forces the entropy of the disordered spin model to equal exactly the value that saturates the CSS bound. Monte Carlo work uses parallel tempering plus dedicated strategies for the hysteresis/metastability endemic to strong first-order transitions.

**Why it matters** — Fracton codes are usually discussed for their (partial) self-correction and constrained excitation mobility; the demonstration that the checkerboard code's code-capacity threshold saturates the CSS bound gives a concrete design principle — self-duality of the mapped spin models — for constructing maximally noise-resilient CSS codes. Relevant to QEC theory, stat-mech-mapping practitioners, and the fracton/subsystem-symmetry community.

**Caveats** — 0.107(3) sits ~1σ below the 0.110 bound; it is an *optimal* (ideal-decoder, code-capacity) threshold, not an achievable circuit-level or phenomenological one. The duality argument is presented as an argument, not a theorem, and assumes zero encoding rate and dual $X$/$Z$ noise models. First-order transitions with no scale invariance complicate the finite-size extrapolation, and the claim that all subsystem-symmetric 3D Ising models transition discontinuously remains empirical. Source here is truncated (Chapter 1), so the numerical details of the threshold estimate could not be verified.

## 6. Real Classical Shadows with Noise

[arXiv:2608.18935](https://arxiv.org/abs/2608.18935) · [SciRate](https://scirate.com/arxiv/2608.18935)

*Atharva Hingane, Dax Enshan Koh*

**TL;DR** This paper extends Koh–Grewal's noisy-classical-shadows analysis from the unitary (Clifford) ensemble to West et al.'s orthogonal (real Clifford) ensemble, computing the noisy shadow channels exactly via orthogonal Weingarten/Brauer-algebra calculus. The main message is that the real protocol's variance advantages — a factor approaching 2 globally and $(3/2)^k$ for $k$-local real Pauli strings — survive intact under an arbitrary known CPTP channel acting after the evolution, with the noise entering only through a single scalar $\beta=\mathrm{tr}[\Lambda\circ\mathrm{diag}]$.

**Key contributions**
- Exact noisy global orthogonal shadow channel: $\mathcal M_{\mathbb O,\Lambda}=\mathcal D_{n,f}\circ(\cdot)_{\rm sym}$ with $f(\Lambda)=2(\beta-1)/[(d-1)(d+2)]$ (general non-TP form uses $\alpha=\mathrm{tr}\Lambda(\mathbb 1)$); invertible on the symmetric subspace iff $d\beta\neq\alpha$.
- Exact (not merely bounded) single-shot variance and shadow seminorm, two-sided bounds, and $N_{\rm tot}\le 170(d-1)^2(\beta-1)^{-2}\varepsilon^{-2}\log(2M/\delta)\max_i\mathrm{tr}(O_i^2)$.
- Because variances are exact, the orthogonal/unitary ratio is a function of one dimensionless parameter $\kappa$; the noise-dependent factor $\varrho_L$ satisfies $\sup_{1<\beta\le d}|\varrho_L-2|=2/(d+2)$, so the advantage is uniform in the noise. Rank-one targets provably saturate strictly below 2; extensive Hamiltonians approach 2 exponentially in $n$.
- Local/product case: seminorm for a Pauli string equals $(2f_1^2)^{-\mathrm{wt}(P)}$ with $f_1=\tfrac12(\mathrm{tr}[\Lambda_1\circ\mathrm{diag}]-1)$, preserving the $(3/2)^k$ gain.
- Complex measurement bases handled via reality fraction $\varsigma=\alpha_{\rm r}/d$ and a transposed-noise scalar $\tilde\beta$; the visible space becomes all of $\mathcal L(\mathbb C^d)$, recovering unitary shadows as $\varsigma\to0$, $d\to\infty$.
- Design-independence of all results across orthogonal 3-designs; a self-contained Brauer/Weingarten appendix including a representation-theoretic account of the order-3 Gram matrix rank drop $15\to10$ at $d=2$ (the case Parts II/IV rest on).
- Corrects West et al.'s identification of the global visible space with $\mathbb C\mathfrak o(d)$: the symmetric subspace has dimension $d(d+1)/2$, not $d(d-1)/2$.

**How it works** Averages of $\mathbb E_U\sum_b\langle b|\Lambda(U\rho U^\intercal)|b\rangle\, U^\intercal\Pi_b U$ over $\mathbb O(d)$ require second and third moments, whose commutant is the Brauer algebra; the Weingarten pseudoinverse of the Gram matrix yields closed forms. A structural lemma factors all four shadow channels as $\mathcal D_{n,f}\circ\Psi_q$ with $\Psi_q(A)=qA+(1-q)A^\intercal$, giving unit-trace shadows, reduction to $O_0$, and visibility $\mathcal V=\mathrm{im}\,\mathcal M^\dagger$ in one stroke. Noise-blind post-processing is shown to incur an exact multiplicative bias $(\beta-1)/(d-1)$ (equal to $p$ for depolarizing).

**Why it matters** It makes the real-shadows advantage a calibratable, hardware-relevant statement: one noise calibration ($\beta$) serves both ensembles, since $f/f_{\mathbb U}=2(d+1)/(d+2)$ is noise-independent. Useful to anyone estimating real-valued (time-reversal-even) observables — GHZ fidelity, TFIM energies — with randomized measurements.

**Caveats** Gate-independent, time-stationary, Markovian noise acting once between evolution and measurement, and assumed *known*; in-circuit or gate-dependent noise (Yu et al., Brieger et al.) is not covered. Requires $\beta>1$; sample complexity blows up as $(\beta-1)^{-2}$. Antisymmetric observables (e.g. scalar spin chirality) are invisible to the real protocol. The stated seminorm bounds are loose by a factor 5 from $\|O_0^2\|_{\rm sp}\le\mathrm{tr}(O_0^2)$, so the "factor 2" claim rests on the exact variances, not the bounds; the weaker bound comparison gives only 1.2. Source is truncated before the case studies and numerics.

## 7. Realizing Logical Diagonal Gates via Transversal Physical $Z$-Rotations in CSS Codes

[arXiv:2608.19094](https://arxiv.org/abs/2608.19094) · [SciRate](https://scirate.com/arxiv/2608.19094)

*K. Sai Mineesh Reddy, Navin Kashyap*

**TL;DR** The authors give an explicit "target-driven" characterization of when a transversal dyadic $Z$-rotation $U(p,w)$ on a CSS code $(C_1,C_2)$ implements a *specified* logical diagonal gate, reducing the question to three modular conditions on $w\cdot x$, $w\cdot y_a$, and $w\cdot(x\ast y_a)$. They then turn this into a constructive "appending" framework that bolts extra physical qubits onto any CSS code to make it support a chosen list of addressable logical $Z$-rotations (single-qubit and multi-controlled), preserving $k$ and controlling distance loss.

**Key contributions**
- **Theorem (characterization):** $U(p,w)$ realizes $\overline{U}_L=\mathrm{diag}(e^{\iota\pi f(a)/2^\ell})$ iff $p\ge\ell$ and, for all $x\in C_2$, $a\in\mathbb F_2^k$: $w\cdot x\equiv 0\ (2^{p+1})$, $w\cdot y_a\equiv 2^{p-\ell}f(a)\ (2^{p+1})$, $w\cdot(x\ast y_a)\equiv 0\ (2^{p})$. The first and third conditions alone give code-space preservation; only the second fixes *which* logical gate. Recovers Camps-Moreno et al.'s result that only single-qubit and multi-controlled $Z$-rotations are reachable (via the inclusion–exclusion expansion of $w\cdot y_a$ over Schur products of the coset basis).
- **Sharpened level bound:** for an addressable $(m-1)$-controlled $R_Z(\pi/2^\ell)$, necessarily $p\ge \ell+m-1$ (e.g. $\mathrm{CCZ}$ needs $p\ge2$), strengthening the naive $p\ge\ell$.
- **Appending construction:** given an $[[n',k',d']]$ code, append block-diagonal auxiliary matrices $G_1^{(i)}$ (to the logical-$X$ generator) and $G_2^{(i)}$ (to the $X$-stabilizer generator), one block per target gate. Resulting code is $[[n'+\sum n_i,\ k',\ \min\{d_X,d_Z\}]]$ with $d_X\ge d'$ and $d_Z\ge\min\{d_{\min}((C_2')^\perp),d_{\min}((C_2^{(i)})^\perp)\}$.
- **Explicit appending matrices** for addressable single-qubit rotations (base case) and, recursively, for $m$-controlled rotations built from lower-order ones.
- **Code families:** for $\ell=1$ (logical $S$ on a fixed address set), asymptotically good $[[n,\Theta(n),\Omega(n)]]$; for $\ell>1$, $[[n,\Theta(n),\Omega(n^\eta)]]$ with $\eta=\min\{(1-\epsilon)/\ell,1/(\ell+1)\}$ on $\le n^\epsilon$ addressed qubits. For *any* address configuration: $[[n,\Omega(\sqrt n),\Omega(\sqrt n)]]$ for $\ell=1$, and $[[n,\Omega(n^{1/(1+\epsilon)}),\Omega(n^{\epsilon/((\ell+1)(1+\epsilon))})]]$ for $\ell>1$.

**How it works** The key technical reduction (Lemma on Schur products of basis vectors) converts the condition $w\cdot x_a\equiv w_H(a\ast A)\ (2^{\ell+1})$ over all $2^k$ cosets into $O(k^{\ell+1})$ conditions on basis vectors: $w\cdot x_i\equiv A(i)\ (2^{\ell+1})$ and $w\cdot(x_{i_1}\ast\cdots\ast x_{i_j})\equiv0\ (2^{\ell-j+2})$ for $2\le j\le \ell+1$. Because the constraints only involve $\mathrm{supp}(w)$, one can localize the rotation to a dedicated block of appended qubits per target gate — this modularity is what makes multiple gates (e.g. $T$ and $\mathrm{CS}$) coexist in one code. Divisibility of the appended codes supplies the higher-order Schur-product vanishing.

**Why it matters** It gives a recipe, rather than a search, for endowing an *arbitrary* good CSS code with a chosen addressable diagonal logical gate set, with quantifiable distance and qubit-count trade-offs — relevant to anyone designing codes where only logical $H$ is left to code switching.

**Caveats** Overhead grows with the number of target gates (no rate guarantee once $\numtargates$ is large); the good $[[n,\Theta(n),\Omega(n)]]$ family is only for $\ell=1$ (Clifford $S$), and non-Clifford families lose distance polynomially. Distance bounds are lower bounds, not exact. Addressability for arbitrary configurations costs a factor in $k$. "Transversal" here means strictly single-qubit tensor products; no numerical/logical-error-rate simulations are reported, and the characterization overlaps with concurrent work.

## 8. RushHour: A Dynamically Reconfigurable Lattice-Surgery Architecture

[arXiv:2608.18985](https://arxiv.org/abs/2608.18985) · [SciRate](https://scirate.com/arxiv/2608.18985)

*Nathaniel Tornow, Aleksandra Świerkowska, Peter Wegmann, Pramod Bhatotia*

**TL;DR** RushHour makes the surface-code lattice a *mutable machine state*: free ancilla space is organized as a single "staircase corridor" whose position can be moved anywhere in one logical round via parallel walking-qubit slides, with magic/|Y⟩/Bell states allocated just-in-time on any free tile and patch orientation tracked lazily as metadata. Across 35 Clifford+T benchmarks it fits on chips 1.2–3.5× smaller than six state-of-the-art LS compilers, runs a median 2.0–7.2× faster in the space-constrained regime, and lands 4.8× (geomean) from the idealized FLASQ resource bound.

**Key contributions**
- A dynamic LS execution model with a *local, checkable* validity invariant: corridor arrays (α, β) that are "jointly monotone." Lemma: any two valid configurations are one parallel single-tile slide apart, regardless of how far the corridor moves — so reconfiguration is O(1) rounds by construction.
- The RushHour ISA: gates and lattice transitions priced in logical rounds; Hadamard lowers to a zero-cost edit of the orientation field, with a physical 3-round `rotate` emitted lazily only when a later gate demands a specific boundary.
- The Lattice Management Unit: translation table + BFS access engine (returns realizations avoiding already-claimed tiles) + a corridor solver that completes a set of "pinned" boundary demands to a full valid corridor in O(n+m) via interval propagation, greedily batching multiple blocked gates per reshape.
- A compiler that schedules by criticality, pipelines cultivation/Bell prep beneath running gates, and sweeps region shapes × 3 placement strategies × feasible code distances to emit a per-circuit Pareto frontier (median 22 non-dominated points vs. 2–6 for static designs).

**How it works** Data patches occupy an n×m slot grid embedded in an (n+1)×(m+1) tile grid; the n+m+1 leftover tiles interlock into one connected corridor, displacing each patch by at most one tile from its home slot. Scheduling alternates: serve every ready gate the standing configuration admits, otherwise call `reshape`. ~9,300 lines of Rust; costed under FLASQ's model (p_phys=10⁻³, t_r=10 µs, cultivated T at v_cult(d)≈2–3 blocks, p_mag=9.7×10⁻⁷), reporting T_succ = W/e^{−ε}.

**Why it matters** Early FTQC chips will be qubit-starved; this is the first LS architecture that both fits the tightest chips (30/35 benchmarks run on no baseline at its minimum chip) and stays within ~1.2× of the best design at every larger budget, replacing per-workload floor-plan selection with one architecture. Overheads are small: reshapes ~1 per 140 ancilla-served gates, physical rotations 1 per ~1,035 Hadamards, patch motion 0.14% of space-time (all zero above 5 tiles/qubit).

**Caveats** The headline assumes one-round walking, a rate *conjectured* but not proven fault-tolerant (2-round arm shifts results ≤10%); walking is priced at the resting error rate. Comparison is circuit-model: PBC-based compilers with Clifford absorption (PureMagic, O3LS, Litinski) still win up to ~2× on some circuits. Cultivation is handled as expected occupancy classes, not stochastic retry; benchmarks cap at 100 logical qubits; first-order ε<1 feasibility cutoff.

## 9. Good Stabilizer Codes from Shallow Clifford Circuits with Random Matchings

[arXiv:2608.18536](https://arxiv.org/abs/2608.18536) · [SciRate](https://scirate.com/arxiv/2608.18536)

*Emile Anand, Elia Gorokhovsky, Jennifer Hritz, Jingtong Sun*

**TL;DR** The paper shows that depth-$O(\log n)$ random Clifford circuits built from independent uniformly random perfect matchings — with only CNOT as the entangling gate, sandwiched by single-qubit Clifford twirls that can be drawn from the 3-element set $\{I, HS, (HS)^2\}$ — produce $[n,k]$ stabilizer codes achieving the quantum Gilbert–Varshamov tradeoff $k/n < 1 - H(d/n) - (d/n)\log_2 3 - \delta$ with probability $\ge 1 - n^{-m} - 2^{k-n(1-H(d/n)-(d/n)\log_23-\delta)}$. This improves Brown–Fawzi's $O(\log^3 n)$ depth to the light-cone-optimal $O(\log n)$ while shrinking the gate set, answering two of their open questions.

**Key contributions**
- Optimal $O(\log n)$-depth, $O(n\log n)$-gate, ancilla-free encoder attaining quantum GV, using $n/2$ CNOTs per layer on a random matching plus local twirls.
- A general universality theorem: any two-qubit Clifford distribution $p_2$ satisfying (i) bi-invariance under $\mathcal H\otimes\mathcal H$ for a subgroup $\mathcal H\subseteq\mathcal C_1$ acting transitively on $\{X,Y,Z\}$ up to sign, (ii) positive probability on some entangling gate, (iii) closure under inversion, works. CNOT (or any fixed entangling gate mixed with its inverse) qualifies.
- A matching-model lower bound: any ensemble of independent random matching layers with $N$ total two-qubit gates achieving distance $d+1$ with probability $\ge p$ needs $N \ge \frac{n-1}{2}\ln(p(d+1))$, so $N=\Omega(n\log n)$ for linear distance — their gate count is optimal within the model.

**How it works** The distance criterion (Brown–Fawzi) requires that no nontrivial input Pauli be mapped to a weight-$\le d$ Pauli. Bi-invariance forces the second-moment operator, restricted to $\sigma_\nu\otimes\sigma_\nu$, to depend only on the binary support $b(\nu)$: local twirls project onto the basis $E_x = 3^{-w(x)}\sum_{b(\upsilon)=x}\sigma_\upsilon^{\otimes2}$. This yields a Markov chain $Q_0$ on $\{0,1\}^n\setminus 0^n$ whose per-pair kernel $K'_{p_2}$ is shown (via reversibility of $p_2$ and Skolem–Noether to rule out non-entangling gates) to be reversible with stationary distribution $\propto 3^{w}$, with $1/3\le p_{11\to11}<1$. The induced weight chain has $\pi(w)=3^w\binom{n}{w}/(4^n-1)$. The authors prove $O(\log n)$ hitting times from low weight to linear weight and then to a neighborhood of $3n/4$, and use reversibility to compare return-to-low-weight probabilities against stationary tails, giving the uniform bounds needed for the union bound.

**Why it matters** It shows Haar/2-design-level coding performance is achievable without design convergence, from an ensemble close to what trapped-ion hardware already runs (e.g., Quantinuum's 98-qubit random Clifford layers with random pairings and a fixed $R_{ZZ}(\pi/2)$).

**Caveats** Non-explicit (existence only; derandomization open); no efficient decoder; all-to-all connectivity assumed, ignoring routing/noise; bi-invariance is technical and excludes natural sets like $\{I,H,S\}$; the $O(n\log n)$ gate count still exceeds the naive $\Omega(n)$ bound, and the depth constant $c(\delta,m,p_2)$ is unquantified.

## 10. Entanglement battery and entanglement catalyst in local state discrimination problems

[arXiv:2608.19139](https://arxiv.org/abs/2608.19139) · [SciRate](https://scirate.com/arxiv/2608.19139)

*Saronath Halder, Aby Philip, Alexander Streltsov*

**TL;DR** The paper imports the "entanglement battery"/catalyst framework into LOCC state-discrimination problems, proving a no-go theorem: no exact battery or catalyst can enable perfect LOCC discrimination of an orthonormal basis consisting entirely of entangled states (hence any assisted-distinguishable set must have cardinality < dim H). It then gives explicit constructions where exact and approximate batteries/catalysts do help — most strikingly a 2⊗2 Bell state that, after discriminating a 2n-qubit set, is returned as an n-qubit GHZ state.

**Key contributions**
- No-go theorem (Thm 1) + corollaries: entangled orthonormal bases remain locally indistinguishable even with an exact battery/catalyst; a bipartite battery can never be "recharged" into genuine multipartite entanglement when discriminating a genuinely-entangled multipartite basis.
- Construction (Prop 2) of a 4-element, 2n-qubit set distinguishable with one ebit, returning an n-qubit GHZ state deterministically — an exact battery with unbounded "gain" (Remark 1).
- Exact catalyst example (Prop 3): an n-qubit GHZ state catalyzes discrimination of a 2ⁿ-element set built from the GHZ basis.
- A state-merging argument showing that catalyst-assisted discrimination via merging requires every state in the set to be entangled (S(A|B)_ψ < 0).
- Approximate catalyst from d+1 maximally entangled states in d⊗d (d = d′²), recovered with probability 1 − 2/(d+1) → 1.
- General result (Prop 5) turning many-copy-indistinguishable ensembles {ρ₁,ρ₂} into approximate batteries, with qudit, n-qubit GHZ, and three-qubit UPB examples; a Nielsen-condition bound α₀ ≤ (1/d)^{1/m} for non-maximally-entangled cases.

**How it works** The no-go proof adapts the Horodecki-type "entanglement-generation" argument: take the maximally entangled Φ_{AC}⊗Φ_{BD}, which is a product state across AC:BD; using U⊗U* invariance rewrite it as Σ|ψ_k⟩_{AB}|ψ_k*⟩_{CD}. Perfect LOCC discrimination of {|ψ_k⟩_{AB}} would leave an entangled state on CD, i.e., create AC:BD entanglement from nothing. Adding a battery τ→τ′ with an additive, LOCC-monotone measure (squashed entanglement) and E(τ′) ≥ E(τ) leaves the contradiction intact. The positive constructions rely on tensor-product structures |ψ_i⟩⊗|ψ′_j⟩ where a small resource state (teleport one qubit across a bipartition, then apply an orthogonality-preserving projective measurement P₁=|00⟩⟨00|+|11⟩⟨11|, P₂=|01⟩⟨01|+|10⟩⟨10|) resolves the first factor while leaving the second factor — the "recharged" battery — untouched. Approximate cases exploit asymmetric branch probabilities (2/(d+1) failure) or the 1/2 chance of being left with m−1 copies of an entangled ρ₁, whose additive entanglement averages to at least E(|ξ⟩).

**Why it matters** Connects two active lines — catalytic/battery resource theory and LOCC discrimination — giving both a hard structural constraint and constructive protocols where the entanglement "cost" of discrimination is fully (or more than fully) recovered. Of interest to entanglement-theory and distributed-measurement researchers, and to anyone budgeting entanglement in networked measurement protocols.

**Caveats** The no-go relies on additivity of the chosen measure (squashed entanglement) and on the battery being uncorrelated with the system; the fairly informal proof of Corollary 2 assumes a bipartite battery. In the "approximate" cases the resource is recovered only on average or with probability →1, and one branch aborts the discrimination task, so the operational status of these as genuine catalysts is arguably weaker than in embezzlement-style results (the authors flag this distinction). The multipartite GHZ example needs an additive multipartite measure imported from elsewhere. No optimality/converse bounds on the battery gain are given.
