# SciRate Daily Digest — 2026-09-18

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Achieving the limits of automorphism gates

[arXiv:2609.19250](https://arxiv.org/abs/2609.19250) · [SciRate](https://scirate.com/arxiv/2609.19250)

*Jin Ming Koh, Shayan Majidy, Aranya Chakraborty, Anqi Gong, Shi Jie Samuel Tan, Norman Y. Yao*

**TL;DR** For stabilizer codes with k ≥ 3 logical qubits, the largest logical group implementable by automorphism gates (physical single-qubit Cliffords + qubit permutations) is exactly the Siegel parabolic P(2k,𝔽₂) = ⟨all addressable S and CX⟩, and this is attained by explicit codes — but doing so costs n = Θ(2ᵏ) physical qubits (tight at n = 2ᵏ−1). By contrast, all addressable *diagonal* Clifford gates ⟨S, CZ⟩ need only n = Θ(k²) via transversal single-qubit Cliffords, and all addressable diagonal gates at level t of the Clifford hierarchy need only Θ(kᵗ) — so the sharp qubit-cost divide is diagonal vs. CX-type, not Clifford vs. non-Clifford.

**The big picture** Fault-tolerant architectures mix expensive universal operations with cheap ones that use only single-qubit rotations and qubit relabelling, and their efficiency hinges on how much work can be pushed onto the cheap ones. This paper settles, for all stabilizer codes, exactly which sets of logical operations those cheap operations can ever produce and how many physical qubits are needed. The surprise is that the cost of a gate set is governed by whether it merely adds phases or actually shuffles logical information between qubits, rather than by the usual easy-versus-hard distinction that dominates fault-tolerance thinking. This tells code designers which native gate sets are fundamentally impossible, which are merely expensive, and where to stop chasing maximal power.

**Key contributions**
- Tight classification of the maximal logical group for every combination of {permutations, transversal single-qubit Cliffords, both} × {stabilizer, CSS, permutationally self-dual, strictly self-dual}, with matching constructions (Table I). Exceptional maxima: 6 elements at k=1, 72 (≅ O⁺(4,𝔽₂)) at k=2.
- Tight qubit-cost bounds: n ≥ 2ᵏ−1 for all addressable CX via automorphisms (or permutations alone); n ≥ k(k+1)/2 for ⟨S, CZ⟩ transversally; n ≥ Σ_{s≤t} C(k,s) for level-t addressable diagonal gates, all attained at Z-distance one and liftable by concatenation.
- New no-gos: no addressable H/HS/SH from automorphisms on indecomposable CSS codes; no PSD code is a "phantom" code for k ≥ 3 (resolving an open question); full Sp(k,𝔽₂)/O(k,𝔽₂) unattainable for k ≥ 8/9; high-rate n = Θ(k) codes fall short of transversal maxima by ~2^{k²/2}.

**How it works** In the binary symplectic picture, single-qubit Cliffords split into preserving- and exchange-type. An "all-or-nothing" lemma shows that on indecomposable CSS codes exchange-type Cliffords must appear on all or no qubits, forcing every automorphism to factor into separately valid transversal and permutation logical gates — giving Aut = Trans ⋊ Perm, i.e. the Levi decomposition U(2k,𝔽₂) ⋊ GL(k,𝔽₂) = P(2k,𝔽₂). Self-duality adds an invariant overlap form, cutting Perm to symplectic/orthogonal (or "flagged isometry") isometries and Trans to S₃. For general stabilizer codes the factorization fails, so the authors induct on k, combine a preserved-Lagrangian argument with the Yin–Lan–Liu–Chen refinement of Aschbacher's classification of *large* maximal symplectic subgroups, and kill the remaining candidates O^±(2k,𝔽₂) and G₂(2) via a prime-order (p ≥ 5) argument reducing cyclic logical actions to pure permutations.

**Why it matters** Architecture designers now know the exact ceiling: maximizing automorphism power forces the rate k/n to zero exponentially, so high-rate codes should target narrowly chosen, workload-relevant gates instead. Adding one suitable non-Clifford gate to the parabolic already gives universality, and diagonal magic gates (T, CS, CCZ) at full addressability cost only Θ(k³) qubits — cheaper than all addressable CX.

**Caveats** Optimal-size constructions have Z-distance one (distance requires concatenation, with unquantified overhead here); tightness of the self-dual permutation bounds is open for 6 ≤ k ≤ 8; several classifications assume indecomposable codes and CSS logical bases; and the results bound group *size/structure*, not the circuit-level fault tolerance or decoding cost of the resulting codes.

## 2. Efficiently estimating failure rates of fault-tolerant logical non-Clifford blocks

[arXiv:2609.19485](https://arxiv.org/abs/2609.19485) · [SciRate](https://scirate.com/arxiv/2609.19485)

*Julio C. Magdalena de la Fuente, Thomas R. Scruby*

**TL;DR** The authors give an algebraic (homological) framework that makes the *decoding problem* of fault-tolerant blocks built from CSS operations plus diagonal third-level Clifford-hierarchy gates ($T$, $CS$, $CCZ$) efficiently samplable. The key structural insight is that fault tolerance forces the non-Clifford gates to be a *cohomology invariant* of the circuit's spacetime fault complex; given that, the $Z$-detector structure conditioned on an $X$-error/measurement pattern $b$ is computed from an explicitly constructible matrix $M^b$, whose kernel is the surviving ("twisted") detector space and whose image supplies extra random "twisted errors". The resulting failure-rate estimate is a provable overestimate, with non-Clifford overhead independent of the number of logical qubits.

**The big picture** Simulating how well an error-corrected quantum computer performs is easy for the Clifford part of an algorithm but generically intractable for the non-Clifford operations that make computation universal — exactly the pieces (magic-state preparation, code switching, transversal non-Clifford gates) whose noise performance we most need to benchmark at scale. This work shows that for a broad and practically important family of such blocks one does not need to track the quantum state at all: because these protocols are fault tolerant, the statistics of the measurement record are almost independent of the encoded information, and the deviations can be computed from a compact algebraic object attached to the circuit's geometry. The payoff is a decoder-level simulator whose cost does not grow with the number of logical qubits being acted on, enabling large-scale threshold and failure-rate studies of magic-state and code-switching gadgets.

**Key contributions**
- Tensor-network/path-integral ("spacetime phase polynomial") representation of third-order circuits; errors and outcomes become chains on a 4-term fault complex $D_X\to T_Z\to T_X\to D_Z$.
- Identification of fault-tolerant non-Clifford gate placement with *local cohomology invariance* of the phase polynomial on the fault complex.
- "Condition C" (contractibility/isolation of the residual $X$-error region), under which the twisted $Z$-detector structure is computable.
- Main theorem: $D_X^b=\ker M^b$, $\partial_0^b=K^b d_0^T$, twisted errors $=\operatorname{im}\widetilde M^b$, affine shift $\kappa_b$ from second derivative of $S$; plus a lemma proving the conditional outcome distribution is *flat* on the allowed subspace.
- A concrete simulator pipeline and an interface to Pauli-frame Clifford simulators for embedding blocks in larger circuits.

**How it works** Since $Z$ operators commute through diagonal gates, the $X$-error decoding problem is unchanged from the underlying CSS circuit. The residual combined $X$-pattern $b=e_x+m_z+b_c$ then "twists" the $X$-symmetries: only those $t$ with $S[A+t]-S[A]$ depending solely on $b$ survive as detectors. Discrete derivatives of $S$ on coboundaries give $M^b$ (symmetric, independent of the chosen filling $A$), so twisted detectors, the syndrome offset $\kappa_b$, and the extra effective errors follow by linear algebra. Success is judged by canonically mapping corrections back to the untwisted ($b=0$) decoding graph where logical classes are defined.

**Why it matters** This closes a real gap between Clifford-simulable benchmarking and the non-Clifford gadgets dominating fault-tolerant resource budgets; it applies to code switching, gauging of diagonal symmetries, transversal non-Clifford gates, and non-Abelian code deformations, and scales to many parallel logical qubits.

**Caveats** Exactly verifying condition C is exponentially hard in circuit volume; practical use requires approximate checks or topological structure (as in the earlier just-in-time work), so estimates are upper bounds — how loose is not quantified here. Failures of condition C are *declared* decoding failures. No numerics appear in the visible source (deferred to a companion paper). The method only simulates the decoding problem, not the logical state, so low-distance post-selection-heavy protocols (cultivation) are better served by the concurrent tableau approach of Takada et al. The circuit class is restricted to CSS operations plus diagonal third-level gates.

## 3. Coherent error threshold for quantum LDPC codes

[arXiv:2609.20537](https://arxiv.org/abs/2609.20537) · [SciRate](https://scirate.com/arxiv/2609.20537)

*Zhengyi Han, Yuanchen Zhao, Yijia Xu, Yixu Wang, Zi-Wen Liu*

**TL;DR** The authors prove that any family of qLDPC codes with distance $d=\Omega(\log n)$ has a nonzero code-capacity threshold against arbitrary local *coherent* (and more generally local CPTP) noise: below a constant rotation strength, the logical error in diamond distance is bounded by $C\sqrt{n}\,e^{-cd}$ under optimal recovery and $C n\,e^{-cd}$ under minimum-weight decoding. The enabling technique, "cluster resummation," exactly resums all error configurations disconnected from an isolated large cluster *before* taking operator norms, avoiding the factor exponential in circuit size that naive term-by-term bounding produces.

**The big picture** Threshold theorems for quantum error correction are almost always proved for random Pauli errors, where one can reason about probabilities of independent error patterns. Real hardware, however, produces coherent control errors — small unitary over- or under-rotations whose amplitudes can add constructively even after a syndrome is measured — and existing rigorous guarantees covered only special codes or special noise. This work shows that sparsity of the checks plus a distance growing merely logarithmically with code size already guarantees exponential suppression of worst-case logical error under arbitrary bounded-support coherent noise, covering surface/color codes, hypergraph-product, bivariate-bicycle, expander, good qLDPC and locally testable codes alike.

**Key contributions**
- A general coherent-noise code-capacity threshold for qLDPC families requiring only $d=\Omega(\log n)$, versus prior work needing constant rate *and* linear distance.
- Polynomial-in-$n$ prefactors with exponential-in-$d$ suppression, improving on earlier bounds with prefactors exponential in $n$.
- The same threshold for a concrete, noise-agnostic decoder (minimum weight), with strictly worse constants ($c_{\rm MW}<c$, $\eta_{\rm th}^{\rm MW}<\eta_{\rm th}$).
- Cluster resummation, a substitute for the union bound that works for interfering amplitudes; extends to local CPTP noise.
- A proposition showing noisy constant-depth logical circuits reduce to this noise model (depth $\le Dr^{2D-1}$, support $\le r^D$).

**How it works** Noise is a depth-$D$ circuit of gates $e^{-i\eta h}$, $\|h\|\le1$, support $\le r$, supports arbitrary (bounded weight, not geometrically local). After perfect syndrome measurement, recoverability is bounded via the complementary channel — here just the syndrome distribution — using the information–disturbance tradeoff: $\epsilon^\star\le\sqrt{\|\mathcal{Q}_U\circ(\mathrm{id}-\mathcal{D}_A)\|_\diamond}$. Expanding $\mathrm{Ad}_U=\sum_B F_B$ with $F_\alpha=\mathrm{Ad}_{u_\alpha}-\mathrm{id}$ ($\|F_\alpha\|_\diamond\le 2\sin|\eta|$), configurations whose interaction-graph components all have $<m=\lceil d/r\rceil$ locations act as $X\mapsto \mathrm{Tr}(X)\sigma$, carrying no logical dependence. The rest is controlled by interpolating $\mathcal{T}_W(t)=\sum_B t^{\nu_m(B)}F_B$; differentiating marks one large cluster and exactly resums the remainder into another $\mathcal{T}$, giving $\|\mathrm{Ad}_U-\mathcal{T}_{\rm small}\|_\diamond\le \Xi/(1-\Xi)$ with $\Xi=\sum_{\text{connected }|C|\ge m}a^{|C|}\le Dnq^m/[\chi(1-q)]$, $q=\chi a$.

**Why it matters** It closes a long-standing gap: the codes actually used in near-term FTQC proposals now have provable robustness to worst-case coherent miscalibration, measured in diamond distance (the right metric, since coherent errors scale as the square root of infidelity).

**Caveats** Code capacity only — syndrome extraction is perfect and noiseless; circuit-level and non-Markovian noise remain open. Thresholds are constants depending on $w,\ell,D,r$ through $\chi$ and are not numerically evaluated; they are likely far below true thresholds. Minimum-weight decoding is not efficiently implementable in general, so no efficient coherent-noise decoder with guarantees is provided. The threshold also depends on the constant $c_d$ in $d\ge c_d\log n$.

## 4. Asymptotically Good Quantum Locally Testable Codes

[arXiv:2609.20780](https://arxiv.org/abs/2609.20780) · [SciRate](https://scirate.com/arxiv/2609.20780)

*William Gay, Fernando Granha Jeronimo*

**TL;DR** The authors claim explicit families of CSS qLDPC codes on qubits that simultaneously achieve constant rate, constant relative distance, and constant-weight local testers with constant soundness — i.e. asymptotically good quantum locally testable codes, the quantum analogue of c³-LTCs. The construction places equivariant Reed–Solomon-based local codes as a cosheaf on non-abelian cubical complexes (arithmetic quotients of products of Bruhat–Tits trees), and the technical engine is a new algebro-geometric proof that tuples of Reed–Solomon codes on norm-one grids are *product-expanding* uniformly in dimension, field extension, duals, and monomial changes.

**The big picture** Quantum error-correcting codes with the best possible rate and distance have been known for a few years, but it remained open whether such codes could also be checked locally: whether a few random measurements suffice to estimate how far a state is from the code space. This paper claims a positive answer, completing the quantum side of a story whose classical analogue was settled only recently. Local testability is the property underlying probabilistically checkable proofs, so a positive resolution is a natural stepping stone toward quantum hardness-of-approximation results, and it also supplies codes with strong self-correcting diagnostics.

**Key contributions**
- Claimed resolution of the asymptotically good quantum LTC conjecture with an explicit family.
- A uniform product-expansion theorem for tuples of (generalized/projective) Reed–Solomon codes of rate in [ε, 1−ε] on multiplicative grids μ_{q_i+1}, with q_i = 2^{m_i} distinct and ratio ≤ K; constant ρ(t,K,ε) fixed *before* choosing dimensions, fields, or duals.
- A regularity bound reg I_Y ≤ c_e(R+1), c_e = 1+4^e σ_e, for reduced coordinate-flat arrangements in (P¹)^e, plus anisotropic H¹-vanishing giving multi-degree interpolation.
- "Reciprocal" pairs of SL₂(F_q)-invariant projective RS codes whose Iwahori characters (χ_e, χ_{−e}) match across a tree edge, enabling equivariant cosheaves with rates → 1/(2^h+1).

**How it works** Product expansion is reduced to a dual statement: a low-weight word of the directional sum lies in its ℓ-locator closure T, whose maximal full flats are indexed by point strata. Line constraints force tensor-RS behaviour on each flat; gluing (via monomial-ideal intersection arguments) plus regularity/H¹-vanishing extends these to a single polynomial of individual degree < r_i, identifying the annihilator with the tensor dual and yielding a line decomposition of cost ≤ d|T| ≤ d(K/θ)^d|W|. Point interpolation on strata needs O(⌈aΛ⌉) to separate points whenever curve multiplicities obey μ_Z(C) ≤ Λ deg C, proved in char 2 via Frobenius-jet amplification and a trace argument; the incidence hypothesis comes from a separate Szemerédi–Trotter-type theorem. Equivariance transports these codes onto arithmetic towers of products of trees via induced representations Ind_I^{K}W.

**Why it matters** A genuine asymptotically good qLTC would close a central open problem in quantum coding and is a prerequisite for quantum PCP-style constructions; the product-expansion theorem for RS tuples is of independent interest for robust tensor codes.

**Caveats** The argument is long, spans thirteen sections plus appendices, and has not been independently verified; several steps invoke external algebraic-geometry results in modified form (e.g. a "proved simultaneous-jet implication" rather than the cited theorem's statement). Constants are explicit but astronomically bad (ρ ≈ (εθ/4c_tK)^t/2t with c_t ~ 4^t·2^{2t−1} and θ an incidence exponent), so locality, rate and soundness will be numerically tiny; the source here is truncated, so the distance, cosystolic-expansion and soundness arguments were not inspected.

## 5. Proof of a positive coherent-error threshold for topological quantum codes

[arXiv:2609.20708](https://arxiv.org/abs/2609.20708) · [SciRate](https://scirate.com/arxiv/2609.20708)

*Shiro Tamiya, Masato Koashi*

**TL;DR** The authors give the first rigorous proof that a *constant*, code-size-independent threshold exists for coherent single-qubit Z-rotation errors on CSS QLDPC codes with a bounded number of logical qubits — including the rotated surface, toric, and color codes — in the code-capacity setting with maximum-likelihood Pauli recovery. They show the entanglement infidelity obeys $1-F_e^{\mathrm{ML}}\le (2^{k_0}-1)^2\, n\, e^{-b d_Z}$ whenever $\max_j|\tan 2\theta_j|<\delta_{\rm th}=1/\big(e[(e+1)c(r-1)+1]\big)$, giving $\delta_{\rm th}\approx1.6\times10^{-2}$ (i.e. $|\theta|\lesssim 2.5\times10^{-3}\pi$) for the rotated surface code.

**The big picture** Standard threshold theorems assume errors are random coin flips, but real hardware suffers coherent, calibration-type over-rotations whose error amplitudes can interfere — adding and cancelling like waves rather than accumulating like probabilities. Numerics have long suggested that surface codes still have a threshold under such noise, but proofs either lost the interference (yielding vacuous bounds) or required the rotation angle to shrink as the code grows. This work supplies an honest proof at fixed rotation angle for an entire family of sparse topological codes, and in doing so recasts coherent error correction as a convergent cluster expansion of a statistical-mechanical polymer model.

**Key contributions**
- First proof of a positive, size-independent coherent-error threshold for topological/QLDPC codes with bounded logical-qubit count, with an explicit lower bound.
- Exact expression for the entanglement fidelity of the logical channel under any syndrome-dependent Pauli decision rule, $F_e(\Lambda^f)=\sum_{\mathbf s}Q_{\mathbf s,f(\mathbf s)}$, plus optimality of ML among such rules.
- An explicit demonstration (Eq. 39) that discarding interference via the triangle inequality gives a bound growing *exponentially* in $n$ — so retaining cancellation is not a technicality but essential.
- A Fourier/polymer dictionary for coherent-error QEC, importing tools from classical coding theory.

**How it works** The infidelity is bounded by pairwise overlaps $B_{\mathbf u,\mathbf v}=\sum_{\mathbf s}|A_{\mathbf s,\mathbf u}A_{\mathbf s,\mathbf v}|$ over distinct logical classes. Writing the diagonal phases $f_{\bm\alpha}(\mathbf y)$ of computational-basis states inside the codespace, the products $A_{\mathbf s,\mathbf u}A_{\mathbf s,\mathbf v}$ become Fourier coefficients of convolutions $g_{\bm\alpha,\bm\beta}=f_{\bm\alpha}*f_{\bm\beta}$ over $\mathbb F_2^{m_X}$; subtracting the $\bm\alpha$-average exploits $\mathbf u\neq\mathbf v$ without destroying phases, reducing everything to a Fourier 1-norm difference. That norm is a partition function of an abstract polymer model whose polymers are connected trivial-syndrome qubit sets with activities controlled by $\delta=\max|\tan 2\theta_j|$; Kotecký–Preiss-type cluster expansion converges for $\delta<\delta_{\rm th}$ with sparsity degree $\Delta_0=c(r-1)$. Comparing cluster sums for two codewords, only clusters carrying nontrivial logical action survive, and these contain at least $d_Z$ qubits — yielding $e^{-bd_Z}$ with $b=\tfrac12\log(\delta_{\rm th}/\delta_*)$ and an $O(n)$ prefactor.

**Why it matters** It closes a conceptual gap: coherent noise can be suppressed by syndrome extraction plus Pauli recovery alone, without twirling or teleportation-induced randomization. The gap to numerics is now quantitative, not qualitative. The polymer representation also hints at a statistical-mechanics classification of coherent-error phases.

**Caveats** Code capacity only: noiseless syndrome extraction, no X-type or measurement errors, and only pure single-qubit Z rotations. The proven threshold is one to two orders of magnitude below numerical estimates. Bounded $k$ is needed for a uniform prefactor (relaxable for asymptotically good codes via $bd_Z-\log n-2\log(2^k-1)\to\infty$). ML decoding is assumed and requires knowing the angles; MWPM-style decoders are not covered. Entanglement fidelity (maximally mixed input) is the figure of merit; the derived diamond-norm bound is weaker by $\sqrt{n}\,e^{-bd/2}$. Circuit-level coherent noise remains open.
