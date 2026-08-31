# SciRate Daily Digest — 2026-08-31

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Quantum Fourier transform toolbox

[arXiv:2608.28573](https://arxiv.org/abs/2608.28573) · [SciRate](https://scirate.com/arxiv/2608.28573)

*Carli Bruinsma, Pietro M. Posta, Joppe Stokvis, Dmitry Grinko, Maris Ozols*

**TL;DR** Two new general recipes for building quantum Fourier transform circuits over finite groups are developed — one from Mackey theory (double-coset/Bruhat induction) and one from Clifford theory — and applied to get a QFT for the group of invertible 2×2 matrices over a finite field with gate count polynomial in log *q* (previously poly(*q*)), plus QFTs for wreath products *F* ≀ *S*ₙ whose cost no longer requires |*F*| = poly(*n*).

**The big picture** Quantum Fourier transforms over abelian groups are the workhorse behind period finding and factoring, but for non-abelian groups efficient circuits are known only for a handful of families, which is one reason the non-abelian hidden subgroup problem remains largely out of reach. This work supplies two systematic construction techniques drawn from classical representation theory — one exploiting how representations of a subgroup recombine when induced up along double cosets, the other exploiting how representations of a normal subgroup extend to the whole group. Applied to matrix groups over finite fields and to symmetry groups built by permuting copies of a smaller group, they turn circuits whose size scaled with the group's size into circuits scaling with its logarithm.

**Key contributions**
- A Mackey-theoretic "induced transform" primitive: given a QFT for a subgroup *H* ⊂ *G*, build the QFT for *G* from double-coset representatives, an untwisting unitary, and a block-diagonal *A*-matrix of Clebsch–Gordan-type coefficients.
- An explicit poly(log *q*, log 1/ε) QFT circuit for GL₂(𝔽_q) via the chain {1} ⊂ *T* ⊂ *B* ⊂ GL₂(𝔽_q), including full Gelfand–Tsetlin bases and transversal matrix coefficients for principal, Steinberg, determinant, and cuspidal irreps.
- A coherent "Gauss phase" gate Γ_q implementing g_q(α)/√q as a phase in poly(log q) gates.
- A Clifford-theoretic construction for *F* ≀ *S*ₙ removing the |*F*| = poly(*n*) restriction of prior generic methods.

**How it works** For GL₂, restriction along *T* ⊂ *B* ⊂ *G* is shown multiplicity-free, so GT bases exist; these turn out to be additive/multiplicative Fourier bases of 𝔽_q, and all transversal matrix coefficients become Gauss sums. The Borel QFT is then three abelian QFTs plus reversible field arithmetic, using Shor's discrete log to convert between additive and multiplicative encodings. Bruhat gives only two double cosets (e, w), with *H_w* = *T* normalized by *w*, so untwisting is a controlled swap of character labels. The only *A*-block growing with *q* is the *q*×*q* block *A*_{ρ_γ,ρ_γ} (naively O(q² polylog) by Givens rotations); it is factored as a Gauss-phase diagonal, an inverse multiplicative QFT, a "quadratic branching" gate that routes *t* by whether *X*²−*X*+*t* splits over 𝔽_q (split torus → principal series; non-split → cuspidal), branch-wise Fourier transforms over 𝔽_q^* and ker(Norm), and label-folding plus exceptional-case rotations.

**Why it matters** These are new, reusable structural tools rather than one-off circuits, and GL₂(𝔽_q) is the first non-abelian family of this type (finite groups of Lie type) with a genuinely polylogarithmic QFT — relevant for anyone probing non-abelian HSP, Schur-type transforms, or representation-theoretic quantum algorithms.

**Caveats** Efficiency is inherited from Shor's discrete-logarithm routine and is basis-dependent: the circuits implement the QFT only in the specific GT bases fixed here (some choices, e.g. 𝔽_q^* ≅ its character group, are non-canonical). Results are ε-approximate in operator norm. The GL₂ case is genuinely intricate and does not obviously generalize to GL_n or larger rank; the wreath-product bound remains conditional on an efficient QFT and small representation registers for *F*. No end-to-end algorithmic application is demonstrated.

## 2. Quantum Fourier transform for the symmetric group

[arXiv:2608.28569](https://arxiv.org/abs/2608.28569) · [SciRate](https://scirate.com/arxiv/2608.28569)

*Carli Bruinsma, Dmitry Grinko, Maris Ozols*

**TL;DR** The authors re-derive, correct, and optimize the two known explicit circuit constructions for the quantum Fourier transform over the symmetric group. A careful low-level analysis shows that Kawano–Sekigawa's claimed Õ(n³) gate count is actually Õ(n^3.5) in the standard one- and two-qubit gate model (their multi-qubit "embedding" gate costs Õ(n^{3/2}) gates, not Õ(n)), while a judicious choice of coset transversals in the older Beals/Moore–Rockmore–Russell construction yields gate cancellations that bring its cost down from Õ(n⁴) to Õ(n³) gates and Õ(n³) depth with Õ(n^{1.5}) qubits — the best known asymptotics.

**The big picture** The Fourier transform over the group of permutations is a workhorse subroutine: it sits inside quantum algorithms for representation-theoretic multiplicities such as Kronecker and plethysm coefficients, and it is currently the bottleneck in the fastest known Schur transform for large local dimension. Because all the claimed speedups in those applications are polynomial rather than exponential, the exact exponent of the Fourier subroutine actually determines whether a quantum advantage survives. This work pins down that exponent honestly, at the level of explicit one- and two-qubit gates, and finds that the older and conceptually simpler construction — once the right choice of coset representatives is made — beats the more recent, allegedly faster one.

**Key contributions**
- Revised complexity for the Kawano–Sekigawa algorithm: Õ(n^{7/2}) gates, Õ(n³) depth, Õ(n^{3/2}) qubits; the discrepancy with the published Õ(n³) is traced to the gate-count model and to the embedding operation's true Õ(n^{3/2}) size (Õ(n) is only its depth).
- Full circuit-level working-out of the Beals construction with transversal 𝒯ₙ = {(1,…,n)^i}, so that consecutive irrep-multiplication gates contract into products of adjacent-transposition gates; result: Õ(n³) gates and depth, Õ(n^{1.5}) qubits.
- A Mackey-theoretic derivation of Kawano–Sekigawa's "second induction," which explains it structurally and identifies the natural transversal 𝒯ₙ = {(i,…,n)}, eliminating two of their four gates (the left-regular-representation gate Kₙ and the relabeling gate Pₙ).
- Identification of a gap in the KS basis: paths through non-λ intermediate nodes ("detours") were omitted from the codomain after recursion.
- Encoding analysis: Yamanouchi words achieve the information-theoretic optimum Θ(n log n) bits for Bratteli-diagram paths, whereas absolute node-by-node path encoding never does.

**How it works** Both algorithms implement the QFT as a sequence of induction maps along the multiplicity-free chain S₁ ⊂ ⋯ ⊂ Sₙ, with irrep labels controlled by the endpoint of the conjugate path register. The induction map is realized either by looping over transversal elements with an "add-a-box" isometry U↑ (amplitudes √(d_μ/(n d_λ)) obtained from the content-ratio identity), a flag-swap gate V_k, and irrep-of-transversal gates R(t_k); or recursively, via the Mackey decomposition of Res Ind V_λ using the two S_{n−1}-double cosets of Sₙ with associated subgroups S_{n−1} and S_{n−2}. Young's orthogonal form plus coherent arithmetic on Yamanouchi words and cell contents supplies the low-level gates.

**Why it matters** Anyone quantifying polynomial quantum advantage for Kronecker/plethysm coefficient estimation, or implementing Krovi-style Schur transforms, should update their exponent bookkeeping; the paper also supplies circuits concrete enough to compile.

**Caveats** Complexities are Õ with polylog(1/ε) error dependence and treat coherent arithmetic as polylog-cost; no lower bounds are given, so Õ(n³) may not be optimal. Constant factors and qubit counts (Õ(n^{1.5}) — superlinear in the Θ(n log n) information-theoretic minimum) are not optimized, and no numerical or hardware validation is reported.

## 3. Exact quantification of nonlocal magic

[arXiv:2608.28563](https://arxiv.org/abs/2608.28563) · [SciRate](https://scirate.com/arxiv/2608.28563)

*Piotr Sierant*

**TL;DR** The minimization of magic over all local unitaries — the "nonlocal magic" of a bipartite pure state — is solved exactly for the stabilizer fidelity: it equals the Rényi-1/2 distance of the entanglement spectrum to the nearest flat spectrum of dyadic rank, i.e. the closest configuration of Bell pairs, and the optimum is attained by the sorted computational-basis representative. The same spectral quantity (largest Schmidt weight in any factor-of-two window of rank) controls universal LOCC entanglement embezzlement, so a family embezzles universally iff its nonlocal magic diverges.

**The big picture** Magic — the resource beyond Clifford circuits — depends on the choice of local axes, so for a state shared by two parties one wants to strip away the magic that either party could rotate away and keep only what lives in the correlations. Doing that requires an optimization over two exponentially large groups of local basis changes, which had resisted solution. Here the optimization collapses completely: the answer depends only on the entanglement spectrum, and specifically on how the spectrum's weight is spread across logarithmic scales of Schmidt rank. This makes the quantity readable off any tensor-network simulation or entanglement-spectroscopy experiment, and it unexpectedly coincides with a state's power to lend out entanglement catalytically.

**Key contributions**
- Exact closed form: the nonlocal min-relative entropy of nonstabilizerness is $-\log_2 \max_{k\le\nu} 2^{-k}(\sum_{x<2^k}\mu_x)^2$, valid for any bipartition, replacing two exponential optimizations by a choice among $\nu+1$ integers; the sorted computational-basis state is globally optimal and simultaneously optimal in every Bell-pair sector.
- Bounds: universal ceiling $\log_2(\nu+1)$; entropy ceiling $\log_2(2S_1+3)$ — nonlocal magic is at most logarithmic in entanglement entropy, hence $O(1)$ for area law, $O(\log\log)$ at criticality, and with zero regularized rate.
- Two-sided equivalence with the embezzlement parameter $\eta_{\rm emb}$ within the sharp constant $3+2\sqrt2$, giving an iff criterion for universal LOCC embezzlement.
- Explicit values for four classes: Haar-random states converge to a closed-form $O(1)$ limit ($<1/4$ at balanced cuts, $\sim 2^{-\Delta}/(4\ln 2)$ for imbalance $\Delta$); CFT (smoothed Calabrese–Lefevre) spectra give $\tfrac12\log_2 S_1 + \tfrac12\log_2(\pi\ln2/8)$; random singlets give exactly zero; van Dam–Hayden catalysts give $\log_2\ln d - 2$. Tensor powers of any nonflat spectrum grow as $\tfrac12\log_2 m$.
- Nonlocal SRE bracketed by NMRE: within factor 4 in general, and $\tfrac15 D \le \mathcal M^{\rm SRE}_{\rm NL}\le 4D$ on balanced cuts; extent and robustness bounded below.

**How it works** Quantization of stabilizer entanglement: across a cut, any stabilizer state is local-Clifford-equivalent to $k$ Bell pairs plus spectators, so its Schmidt vector is flat with $2^k$ entries. Maxima over stabilizer states and over local unitaries commute, and von Neumann's trace inequality gives the best overlap with a fixed-rank flat spectrum as an ordered partial sum. A dyadic-shell decomposition plus Cauchy–Schwarz/AM–GM yields the entropy bound and the octave equivalence; Marchenko–Pastur asymptotics and a saddle-point evaluation give the random and critical cases.

**Why it matters** Nonlocal magic becomes as cheap as reading MPS bond spectra (with an $\ell_1$-error robustness $2\sqrt{\varepsilon}$), versus fixed-basis stabilizer fidelity capped near nine qubits, and becomes measurable via entanglement-Hamiltonian tomography or randomized measurements. It also gives a physically motivated diagnostic that separates states with identical entanglement scaling, and a bridge between magic resource theory and catalysis.

**Caveats** NMRE is neither an entanglement monotone nor additive; its zero set includes arbitrarily entangled flat-dyadic states. Exactness is specific to stabilizer fidelity — nonlocal SRE, extent, robustness and mana optimizers remain unknown (SRE only bracketed, with the balanced-cut lower bound resting on a companion result). The CFT scaling assumes the smoothed Calabrese–Lefevre spectrum and is untested in finite chains. Mixed states are open, and sample-efficient estimators for ordered partial sums are not provided.

## 4. Learning to Decode Concatenated Quantum Codes with Hierarchical Message Passing

[arXiv:2608.28571](https://arxiv.org/abs/2608.28571) · [SciRate](https://scirate.com/arxiv/2608.28571)

*Jiahui Wu, Chao Zhang, Zipeng Wu, Shilin Huang*

**TL;DR** The authors build a differentiable, hierarchical message-passing decoder for arbitrary concatenated stabilizer codes: soft belief vectors live on X/Y/Z variable nodes at every concatenation level and are updated by small level-specific MLPs that aggregate four message channels (Pauli-compatibility, stabilizer, upward, downward). On the concatenated [[15,7,3]] Hamming code it raises the depolarizing pseudo-threshold from 6.5% to 12.3% (bit-flip: 4.4% → 6.8%), and after fine-tuning on circuit-level data it beats the dedicated level-by-level minimum-distance decoder for many-hypercube codes by 17× in logical-CNOT failure rate at p=0.005, L=4.

**The big picture** Concatenated codes are attractive for low-overhead fault tolerance, but each code family has so far needed its own hand-crafted decoder, and those decoders typically throw away information by treating bit-flip and phase-flip errors independently or by truncating a combinatorial search. Here a single learned decoding architecture is defined on the natural tree structure of concatenation, so beliefs flow both up and down the hierarchy while the neural networks only learn how to combine incoming evidence. It works out of the box for non-CSS component codes and for realistic circuit noise, turning decoder design for concatenated codes from a bespoke engineering task into a training run.

**Key contributions**
- A generic hierarchical decoding graph: variable nodes for all three Pauli sectors at every level, plus *auxiliary* logical-observable triples (stabilizer-dressed to minimum weight) and *redundant* stabilizer constraints (all products of generators of acceptable weight) to enrich the graph.
- Message rules that are smooth surrogates for mod-2 parity via φ(x)=sin²(πx/2), giving fully differentiable "soft syndrome" constraints instead of standard BP log-likelihood updates.
- A gated recurrent update (2 warm-up + 4 shared recurrent blocks, repeated R=22 at inference, T ≤ 90, with early stopping on syndrome consistency), r=8 belief dimension, trained with BCE on both physical and top-level logical bits, Muon+AdamW.
- Circuit-level fine-tuning inside Knill teleportation-based EC, using learnable per-node initial embeddings to absorb position- and level-dependent error bias; training labels harvested from the exact tracked Pauli frame, with a canonicalization step that removes spurious logical-Z dressing from prepared |0_L⟩ blocks (otherwise it pollutes P(L|σ)).
- Demonstration on a non-CSS concatenated [[8,3,3]] code, where no specialized decoder exists.

**Why it matters** Concatenated codes with transversal gates and high rate (many-hypercube, [[15,7,3]]) are live candidates for early fault tolerance; decoding quality directly sets their break-even noise budget. Nearly doubling the depolarizing pseudo-threshold, and doing so with a fixed iteration count rather than combinatorial search, is relevant both to code designers exploring the concatenation design space and to anyone building real-time decoders.

**Caveats** The crossing points are finite-level pseudo-thresholds, not asymptotic thresholds. No latency, throughput, or parameter-count/hardware analysis is given despite T up to 90 iterations. Circuit-level comparison uses a *stricter* postselection rule (C3′) than the reference work's (C3) and a fast level-2 lookup, plus noiseless single-qubit gates and idling; acceptance/postselection overhead is not reported. Improvements shrink at low p (3.6× at p=0.002) because both decoders hit a floor set by the non-fault-tolerant level-4 preparation, where weight-6 errors are accepted. Each code and level requires separate training.

## 5. Spectral Theory of Semisimple Bivariate Bicycle Codes

[arXiv:2608.27565](https://arxiv.org/abs/2608.27565) · [SciRate](https://scirate.com/arxiv/2608.27565)

*Eric Sabo, Mahir Bilen Can, David Marquis*

**TL;DR** The paper recasts bivariate bicycle (BB) codes as two-block objects over the semisimple ring $R=\mathbb{F}_q[x,y]/\langle x^\ell-1,y^m-1\rangle$ and pushes them through the Wedderburn/CRT decomposition into finite-field components indexed by $q$-Frobenius orbits of $\mathbb{Z}_\ell\times\mathbb{Z}_m$. This yields a closed-form logical dimension (governed entirely by the orbits where *both* check polynomials vanish), a new "colon-ideal" distance lower bound that captures logicals spread across both blocks, and an orbit-level theory of permutation automorphisms, $ZX$-dualities and metachecks — all computable without ever writing down a stabilizer matrix.

**The big picture** Bivariate bicycle codes are among the most promising low-overhead quantum LDPC codes for near-term hardware, but essentially all good instances were found by brute-force search over pairs of defining polynomials, leaving no explanation of *why* a given code has its dimension and distance. This work embeds the family into the classical theory of two-dimensional cyclic codes, so that the code parameters, symmetries and covering-code behaviour can be read off from where the two defining polynomials vanish on a grid of roots of unity. The payoff is a design principle rather than a lottery ticket: one can see which roots buy dimension, which buy distance, and hence the intrinsic tension between the two.

**Key contributions**
- Dimension formula: $k$ is fixed by the common-zero region; orbits where only one of $a,b$ vanishes are proved homologically trivial. Exact duality between $X$- and $Z$-logical spaces via the coordinate involution $\iota$.
- A colon-ideal lower bound $N_{a,b}=d_R(\langle b{:}a\rangle)+d_R(\langle a{:}b\rangle)$ on mixed-block logicals, refined by "alternating stabilizer exclusion", combined with single-block annihilator terms $E_a,E_b$ into $d\ge\min\{E_a,E_b,N_{a,b}\}$.
- Automorphism theory over $\mathbb{F}_p$: introduction of a *spectral slope* $\lambda_O$ (ratio of the two check components on an orbit), with slope-matching as a necessary condition; unconditional existence of the signed block-swapping $ZX$-duality needed for fold-transversal gates; characterization of $CZ$-type phase gates; metachecks for redundant stabilizers.
- Algebraic (quotient-surjection) treatment of lifts/projections giving an exact cover dimension formula over any $\mathbb{F}_q$, not just when the covering degree divides $p$.
- Appendix: BCH-based product construction $\mathsf{Prod}(C_x,C_y)$ with a designed-distance bound.

**How it works** Semisimplicity ($\gcd(q,\ell m)=1$) splits $R$ into fields, one per Frobenius orbit; orbit idempotents $e_O$ act as spectral projectors. Partitioning orbits into regions where both, one, or neither of $a,b$ vanish (with a Fourier duality swapping support-regions and zero-regions) reduces homology to bookkeeping on regions, and reduces distance questions to minimum weights of classical 2D cyclic codes $\mathcal{C}(S)$. Worked examples re-derive $k$ for known codes ($[[90,8]]$, $[[162,24]]$, $[[434,10]]$) purely from zero orbits.

**Why it matters** Anyone designing BB/two-block group-algebra codes gets a deterministic construction and certification route, plus algebraic criteria for the symmetries that enable fold-transversal logic. The framework is stated to extend to abelian (and plausibly non-abelian) group-algebra and multivariate generalizations.

**Caveats** The distance bounds are demonstrably loose: the three examples give lower bounds 4, 4 and 2 against true/upper distances 10, 6 and 26 — the mixed-block term dominates and can collapse (empty zero set ⇒ weight-1 colon-ideal elements). Semisimplicity is essential; the repeated-root case needs Gröbner-style tools the theory was built to avoid. Automorphism results are restricted to prime fields, untwisted tori, and a *subgroup* (block-monomial) of the automorphism group. No control over stabilizer weight — the authors concede the example codes' check weights are likely impractical — and no new code tables; a systematic search is deferred.
