# SciRate Daily Digest — 2026-08-31

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Quantum Fourier transform toolbox

[arXiv:2608.28573](https://arxiv.org/abs/2608.28573) · [SciRate](https://scirate.com/arxiv/2608.28573)

*Carli Bruinsma, Pietro M. Posta, Joppe Stokvis, Dmitry Grinko, Maris Ozols*

**TL;DR** The authors give two new general recipes for building quantum Fourier transform circuits over non-abelian finite groups: one based on Mackey theory (Fourier transform of a group from that of a subgroup, organized by double cosets), one on Clifford theory. Applying the first, they obtain an explicit QFT circuit for $\mathrm{GL}_2(\F_q)$ of size $\mathrm{poly}(\log q,\log 1/\varepsilon)$ — an exponential improvement over $\mathrm{poly}(q)$ — and applying the second, QFT circuits for wreath products $F\wr S_n$ whose cost is inherited from a QFT for $F$, lifting the earlier requirement that $F$ be of size polynomial in $n$.

**The big picture** Fourier transforms over non-abelian groups are the engine behind hidden-subgroup style quantum algorithms, but efficient circuits are known only for a handful of group families; generic constructions typically cost time polynomial in the group order rather than in its logarithm. This work supplies two systematic construction techniques drawn from classical representation theory, and uses them to produce genuinely efficient circuits for the group of invertible two-by-two matrices over a finite field and for wreath products with the symmetric group. The matrix-group result is notable because the group order grows polynomially in the field size, so previous approaches were exponentially slower, and the wreath-product result decouples the cost from the size of the base group.

**Key contributions**
- A Mackey-theoretic "induced transform" generalizing Beals-style subgroup-adapted (Gelfand–Tsetlin) QFT constructions: the transform factorizes into a subgroup QFT, a double-coset-indexed untwisting unitary, and a block-diagonal $A$-matrix of multiplicity-space isometries.
- Complete, explicit representation-theoretic data for $\{\I\}\subset T\subset B\subset \mathrm{GL}_2(\F_q)$: multiplicity-free restrictions, GT bases for principal series, Steinberg/determinant, and cuspidal irreps, and all transversal matrix coefficients (Gauss sums, and $\F_{q^2}$ Gauss sums for cuspidals).
- A $\mathrm{poly}(\log q)$ circuit for the only $q$-dimensional block $A_{\rho_\gamma,\rho_\gamma}$.
- A Clifford-theoretic construction for $F\wr S_n$.

**How it works** The Borel QFT is assembled from additive/multiplicative $\F_q$ Fourier transforms plus reversible exponentiation and a coherent discrete logarithm (reversible, amplified Shor), with a "regime flag" tagging additive vs. multiplicative encodings and protecting the zero element. Bruhat decomposition gives exactly two double cosets ($e$, $w$) with $H_w=T$, so untwisting is just a controlled swap of character labels. The hard block is diagonalized structurally: a diagonal Gauss-sum phase, an inverse multiplicative Fourier transform, then a *quadratic branching gate* that routes $t$ according to whether $X^2-X+t$ splits over $\F_q$ — split values feed the split torus and principal series, irreducible ones feed the nonsplit torus and cuspidals — followed by Fourier transforms on each torus, folding of Weyl/Frobenius orbit pairs onto single irrep labels, and a two-dimensional reflection handling the exceptional $\delta^2=\gamma$ (Steinberg/determinant) cases. A coherent Gauss-phase gate $\Gamma_q$ (phase kickback on character phases, adapted from van Dam–Seroussi) supplies the required unit-modulus factors.

**Why it matters** These are new efficient QFTs for structurally rich non-abelian families, of direct interest to anyone hunting hidden-subgroup or non-abelian phase-estimation applications; the Mackey and Clifford frameworks are reusable templates rather than one-off constructions.

**Caveats** Results are approximate (operator-norm $\varepsilon$) and depend on quantum discrete logarithm, so the circuits are not elementary; the Fourier basis depends on a non-canonical choice of field generator. Only rank two is treated — extension to $\mathrm{GL}_n(\F_q)$ or general reductive groups is open, and the construction leans heavily on multiplicity-freeness of the chain and on the two-cell Bruhat structure. No end-to-end gate counts or algorithmic application is given.

## 2. Quantum Fourier transform for the symmetric group

[arXiv:2608.28569](https://arxiv.org/abs/2608.28569) · [SciRate](https://scirate.com/arxiv/2608.28569)

*Carli Bruinsma, Dmitry Grinko, Maris Ozols*

**TL;DR** The authors give a careful, gate-level reanalysis of the two known constructions of the quantum Fourier transform over the symmetric group. They show that the Kawano–Sekigawa circuit actually costs $\widetilde{\mathcal{O}}(n^{3.5})$ one- and two-qubit gates (not the claimed $\widetilde{\mathcal{O}}(n^3)$) with $\widetilde{\mathcal{O}}(n^3)$ depth, and that the older Beals construction — with a better choice of coset representatives — achieves $\widetilde{\mathcal{O}}(n^3)$ gates and depth on $\widetilde{\mathcal{O}}(n^{1.5})$ qubits, the best known asymptotics.

**The big picture** The Fourier transform over the group of permutations is the workhorse behind quantum algorithms for estimating representation-theoretic multiplicities (Kostka, Littlewood–Richardson, Kronecker, plethysm coefficients) and behind the currently best Schur transform when the local dimension is large; in both settings it is the dominant cost, so its exact polynomial exponent determines whether a quantum speedup survives. Previous complexity claims rested on subroutines that were never compiled down to elementary gates, and a key multi-qubit operation turns out not to admit the assumed linear-size decomposition. Here both constructions are worked out explicitly to the level of one- and two-qubit gates plus coherent arithmetic, correcting the record and, somewhat unexpectedly, showing that the older and conceptually simpler of the two constructions is the faster one. This makes the transform concretely implementable and pins down the polynomial gaps in the downstream algorithms.

**Key contributions**
- Corrected complexity for the Kawano–Sekigawa algorithm: $\widetilde{\mathcal{O}}(n^{7/2})$ gates, $\widetilde{\mathcal{O}}(n^3)$ depth, $\widetilde{\mathcal{O}}(n^{3/2})$ qubits; the embedding gate $\mathrm{A}_n$ costs $\mathcal{O}(n^{3/2})$ gates (only its *depth* is $\mathcal{O}(n)$).
- Simplification of that algorithm: deriving the second induction relation from Mackey theory yields the transversal $\mathcal{T}_n=\{(i,\dots,n)\}$, eliminating the gate $\mathrm{K}_n$; correctly identifying the post-recursion basis (including previously overlooked "detour" paths through $\tilde\lambda\neq\lambda$) eliminates the relabeling gate $\mathrm{P}_n$.
- Improved Beals/Moore–Rockmore–Russell-style circuit: choosing $\mathcal{T}_n=\{(1,\dots,n)^i\}$ makes consecutive irrep gates telescope into products of adjacent transpositions, cutting the count from $\widetilde{\mathcal{O}}(n^4)$ to $\widetilde{\mathcal{O}}(n^3)$.
- Encoding analysis: Yamanouchi-word (relative path) encoding is space-optimal at $\Theta(n\log n)$ bits, while absolute path encoding never is.

**How it works** The QFT is built from the multiplicity-free chain $S_1\subset\cdots\subset S_n$, applying induction maps $\mathrm{U}^{\mathrm{ind}}_m$ layer by layer in the Young–Yamanouchi (Gelfand–Tsetlin) basis. Beals' induction map loops over the $n$ transversal elements using three gates: $\mathrm{U}_\uparrow$ (spreading a path over successors with amplitudes $\sqrt{d_\mu/(nd_\lambda)}$, computed via a content-product identity), $\mathrm{V}_k$ (a controlled $X$ on the transversal/$\star$ subspace), and $\mathrm{R}(t_k)$ (Young's orthogonal form). With the chosen transversal, $\mathrm{R}^\dagger(t_k)\mathrm{R}(t_{k-1})$ collapses to $\mathrm{R}(\sigma_{n-1})\cdots\mathrm{R}(\sigma_1)$, each $\widetilde{\mathcal{O}}(1)$ gates, giving $\widetilde{\mathcal{O}}(n^2)$ per layer. The Mackey route instead uses the two $S_{n-1}$-double cosets of $S_n$ ($\Omega=\{e,\sigma_{n-1}\}$, with $H_e=S_{n-1}$, $H_{\sigma_{n-1}}=S_{n-2}$) to recurse $\mathrm{U}^{\mathrm{ind}}_{n-1}$ inside $\mathrm{U}^{\mathrm{ind}}_n$. Errors are measured in diamond norm with $\mathrm{polylog}(1/\epsilon)$ scaling.

**Why it matters** Anyone building Schur transforms, multiplicity-estimation algorithms, or non-abelian Fourier sampling subroutines now has a concrete, cheaper circuit and a trustworthy exponent; the $n^{3.5}\to n^3$ correction directly shifts the quantum-vs-classical crossover estimates for plethysm and Kronecker coefficients.

**Caveats** Complexities are asymptotic and $\widetilde{\mathcal{O}}$ hides polylog factors; coherent arithmetic is treated as polylog-cost, so constants and real resource counts remain unquantified. Optimality is not established — no lower bound is given, and the $\widetilde{\mathcal{O}}(n^{1.5})$ qubit count exceeds the $\Theta(n\log n)$ information-theoretic minimum. The truncated source leaves several low-level appendix constructions (e.g. $\mathrm{A}_n$, shape registers) unverified in this reading.

## 3. Exact quantification of nonlocal magic

[arXiv:2608.28563](https://arxiv.org/abs/2608.28563) · [SciRate](https://scirate.com/arxiv/2608.28563)

*Piotr Sierant*

**TL;DR** The nonlocal magic of a bipartite pure state — magic minimized over all local unitaries — is solved exactly for the stabilizer-fidelity (min-relative-entropy) measure: it equals the minimum Rényi-1/2 divergence between the entanglement spectrum and the flat spectra of *k* Bell pairs, i.e. a maximum over only ν+1 partial sums of ordered Schmidt coefficients. The same quantity is shown to be equivalent (up to a sharp additive constant of log₂(3+2√2)) to the largest Schmidt weight in any factor-of-two rank window, which is the known necessary-and-sufficient criterion for universal LOCC embezzlement — so a family embezzles universally exactly when its nonlocal magic diverges.

**The big picture** Magic quantifies how far a state lies beyond classically simulable Clifford circuits, but it depends on the choice of local axes, so for a shared state one wants the part of magic stored in the correlations rather than in either party's basis. Isolating that part requires minimizing over all local basis changes, an optimization that had resisted exact solution beyond tiny systems. This work solves it in closed form for one standard magic measure and shows the answer is a simple, experimentally accessible property of the entanglement spectrum — how evenly the spectrum's weight is spread across logarithmic scales of rank — which simultaneously decides whether the state can act as a universal catalyst from which entanglement can be borrowed. It also shows this diagnostic separates states that entanglement entropy alone cannot distinguish.

**Key contributions**
- Exact closed form for nonlocal stabilizer fidelity, any pure multiqubit state, any (unbalanced) cut; the sorted computational-basis representative is proved globally optimal and simultaneously optimal in every Bell-pair sector.
- Universal bound 0 ≤ D ≤ log₂(ν+1) and entropy ceiling D ≤ log₂(2S₁+3): nonlocal magic is at most logarithmic in entanglement entropy, hence O(1) for area law, O(log log ν) at criticality.
- Two-sided equivalence with the octave-weight embezzlement parameter, giving an "if and only if" between divergent nonlocal magic and universal LOCC embezzlement; constant shown asymptotically sharp.
- Nonlocal SRE bracketed by NMRE ((1/5)D ≤ M ≤ 4D on balanced cuts); nonlocal extent and generalized robustness lower-bounded.
- Four spectral classes: Haar-random (D₀ < 1/4, exponentially smaller for imbalance Δ, closed form via Marchenko–Pastur), CFT chains (½log₂ln L_eff + ½log₂(πc/24)), random singlets (exactly 0), van Dam–Hayden (log₂ln d − 2); tensor powers give ½log₂m + O(1) for any non-flat spectrum.

**How it works** Stabilizer entanglement is quantized: across any cut a stabilizer state is local-Clifford-equivalent to exactly *k* Bell pairs plus product spectators, so its spectrum is flat with 2^k equal entries. Von Neumann's trace inequality then makes the maximal overlap with any rank-2^k stabilizer state equal to 2^{-k}(Σ_{x<2^k} μ_x)², and interchanging the maxima over stabilizer states and local unitaries yields the envelope over k. Dyadic-shell decompositions and AM–GM give the bounds and the octave equivalence; a saddle-point evaluation on the smoothed Calabrese–Lefevre spectrum gives the CFT law.

**Why it matters** Nonlocal magic becomes free in any MPS/DMRG simulation (bond spectra already stored) and measurable by entanglement spectroscopy, with an explicit 2√ε robustness bound in ℓ₁ error — replacing an exponentially hard on-device optimization previously feasible only for two qubits. It also links a computational resource to catalytic entanglement power.

**Caveats** Exactness holds only for the stabilizer fidelity; optimizers for nonlocal SRE, extent, robustness and mana remain open (the balanced-cut SRE linear bound leans on an unpublished companion result). NMRE is not an entanglement monotone, not additive, and has zero regularized rate. The critical-chain law is derived for a smoothed CFT spectrum, not verified in finite chains. Mixed-state generalization is unresolved, and sample-efficient estimators for ordered-Schmidt partial sums are not provided.

## 4. Learning to Decode Concatenated Quantum Codes with Hierarchical Message Passing

[arXiv:2608.28571](https://arxiv.org/abs/2608.28571) · [SciRate](https://scirate.com/arxiv/2608.28571)

*Jiahui Wu, Chao Zhang, Zipeng Wu, Shilin Huang*

**TL;DR** The authors build a hierarchical decoding graph for arbitrary concatenated stabilizer codes — one variable node per Pauli type (X, Y, Z) at every address and every concatenation level, tied together by stabilizer checks, "parent = parity of children" hierarchy constraints, and X+Y+Z=0 compatibility constraints — and run a learned, differentiable message-passing decoder on it. On the concatenated [[15,7,3]] Hamming code the depolarizing pseudo-threshold rises from 6.5% to 12.3% (bit-flip: 4.4% → 6.8%), with L=3 block failure rates 2–4 orders of magnitude below the state-of-the-art bidirectional hard-decision decoder; fine-tuned on circuit-level Knill teleportation data, it beats the dedicated many-hypercube decoder by 17× at level 4 and p=0.005.

**The big picture** Concatenated codes are attractive for low-overhead fault tolerance because they pack many logical qubits into few physical ones, but every new code family has historically required a hand-crafted decoder, and those decoders typically process each level and each error type separately, discarding correlations and truncating their search to stay fast. This work replaces that bespoke engineering with a single generic architecture: soft confidence values flow up and down the concatenation hierarchy and across error types, with tiny neural networks learning only how to combine incoming evidence. The same architecture works for non-CSS codes and can be adapted to realistic circuit noise by learning position-dependent error biases, turning decoder design into a training problem and freeing researchers to explore the code design space.

**Key contributions**
- A unified hierarchical factor graph covering non-CSS component codes, with redundant stabilizer generators and *auxiliary* stabilizer-dressed logical-observable triples added as extra nodes/constraints (e.g. 45 stabilizer nodes and 42 triples per [[15,7,3]] block).
- Differentiable parity messages via the periodic map φ(x)=sin²(πx/2) on continuous r=8-dimensional beliefs, with four aggregation channels (upward, downward, stabilizer, cross-Pauli).
- Learned gated updates (update MLP hidden 80, gate MLP hidden 8 reading squared belief–message discrepancies), recurrent weight sharing (train R=5, infer R=22, up to 90 iterations) with syndrome-consistency early stopping.
- Substantial threshold and logical-error-rate gains over specialized decoders, plus a full circuit-level fine-tuning pipeline with learnable per-node initial embeddings and careful Pauli-frame canonicalization of training labels.

**How it works** Training uses online-sampled depolarizing errors with p drawn uniformly from [0, p_max], BCE loss on both physical and top-level logical bits, supervision at the last three recurrent outputs, and Muon (matrices) + AdamW (rest). Circuit-level data are harvested from the 10-round protected transversal-CNOT benchmark (22 samples per trajectory), with exact tracked errors as labels; only 20 fine-tuning epochs at 10× lower learning rate.

**Why it matters** Decoder availability, not code existence, is often the bottleneck for concatenated schemes; a generic learned decoder makes non-CSS and multi-logical-qubit concatenations practically testable, and the fixed-iteration inference avoids the combinatorial searches of minimum-distance decoders.

**Caveats** Pseudo-thresholds are level-crossing artifacts at L≤4, not asymptotic thresholds. Circuit noise omits single-qubit-gate and idling errors; the level-4 preparation is not distance-preserving, so a weight-6 error creates an error floor that limits the gain at low p (3.6× at p=0.002). Their EDT acceptance rule (C3′) is strictly stricter than the reference's (C3), complicating the comparison. Label canonicalization is only done exactly at levels 1–2. Runtime/latency and scaling to higher levels, plus per-code retraining cost, are not addressed in the visible text.

## 5. Spectral Theory of Semisimple Bivariate Bicycle Codes

[arXiv:2608.27565](https://arxiv.org/abs/2608.27565) · [SciRate](https://scirate.com/arxiv/2608.27565)

*Eric Sabo, Mahir Bilen Can, David Marquis*

**TL;DR** This paper recasts bivariate bicycle (BB) CSS codes inside the classical theory of two-dimensional cyclic codes, working in the semisimple regime gcd(q, ℓm)=1 where R = F_q[x,y]/(x^ℓ−1, y^m−1) splits by CRT/Wedderburn into finite fields indexed by q-Frobenius orbits of Z_ℓ × Z_m. The logical dimension is shown to equal twice the size of the *common-zero region* of the two defining polynomials, orbits where only one polynomial vanishes are homologically trivial, and a new colon-ideal lower bound on distance captures mixed-block logical operators missed by prior per-block bounds. A "spectral slope" invariant then characterizes coordinate-permutation automorphisms, yielding unconditional existence of the signed block-swap ZX-duality needed for fold-transversal logic.

**The big picture** Good bivariate bicycle codes — currently among the most practical low-density parity-check quantum codes — have been found almost entirely by brute-force computer searches over pairs of defining polynomials, so we know good codes exist at given sizes but cannot design them deliberately. This work supplies the missing algebraic dictionary: by decomposing the underlying ring into independent "frequency" components, the number of encoded qubits, bounds on the code distance, the code's symmetries, and how parameters behave under lifting to covering graphs can all be read off from which components the two defining polynomials annihilate. That converts code discovery from a numerical sweep into a finite, structured enumeration, and it makes explicit the tension between dimension and distance: the same shared roots that create logical qubits also weaken distance.

**Key contributions**
- Orbit-idempotent dimension formula: k is determined solely by the common-zero region; single-polynomial-zero orbits contribute nothing. Exact X/Z logical duality via the coordinate involution ι.
- Colon-ideal distance bound d ≥ min{E_a, E_b, N_{a,b}} using annihilator ideals ann⟨a⟩, ann⟨b⟩ and colon ideals ⟨b:a⟩, ⟨a:b⟩, plus an "alternating stabilizer exclusion" refinement (N*).
- Spectral slope λ_O on the coupled active-support region; a slope-matching criterion for block-monomial permutation automorphisms over F_p, existence proof of ZX-duality, CZ-type phase gates, and metachecks for redundant stabilizers.
- Independent algebraic (quotient-ring surjection) treatment of lifts/projections giving an exact dimension formula over any F_q from strictly new common roots of the cover, not just covering degrees dividing p.
- Appendix: BCH-based product construction Prod(C_x, C_y) with a designed-distance lower bound.

**How it works** Multiplication operators M_a, M_b give H_X = [A B], H_Z = [M_{ι(b)} −M_{ι(a)}]; R is a symmetric Frobenius algebra with M_c^T = M_{ι(c)} and ann(ann(I)) = I. Orbits are partitioned into regions where both, one, or neither polynomial vanishes, with a Fourier duality swapping support-regions and zero-regions. Logical spaces reduce to classical 2D cyclic codes C(S) whose minimum weights supply the bounds; the worked examples verify k against literature codes ([[90,8]], [[162,24]], [[434,10]]) without writing down stabilizers.

**Why it matters** Anyone building or searching QLDPC code families gains a first-principles design language, symmetry classification (needed for fold-transversal gates and metachecks), and a route to structured enumeration rather than random search. The framework extends to abelian two-block group-algebra codes and multivariate generalizations.

**Caveats** Restricted to the semisimple case (non-semisimple/repeated-root case is flagged as open and requires Gröbner machinery). Automorphism analysis specializes to prime fields because stabilizer codes are only F_p-linear. Crucially, the new distance bound is loose in the three examples shown (4 vs ≤10, 4 vs ≤6, and only 2 vs ≤26), with the mixed-block term N_{a,b} dominating; the [[434,10]] case needs an ad hoc argument to reach d ≥ 3. No control over stabilizer weight — the authors concede example weights are likely infeasible for most near-term hardware. No new code tables; a systematic search is deferred.
