# SciRate Daily Digest — 2026-08-31

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Quantum Fourier transform toolbox

[arXiv:2608.28573](https://arxiv.org/abs/2608.28573) · [SciRate](https://scirate.com/arxiv/2608.28573)

*Carli Bruinsma, Pietro M. Posta, Joppe Stokvis, Dmitry Grinko, Maris Ozols*

**TL;DR** The paper gives two general recipes for building quantum Fourier transform circuits over finite groups — one based on Mackey theory (induction along a subgroup chain with double-coset/twisting bookkeeping) and one on Clifford theory (for normal subgroups) — and uses them for two concrete exponential speedups: a QFT for the group of invertible 2×2 matrices over a finite field with $q$ elements in $\mathrm{poly}(\log q,\log 1/\varepsilon)$ gates instead of $\mathrm{poly}(q)$, and QFTs for wreath products $F\wr S_n$ whose cost is inherited from a QFT for $F$, lifting the previous $|F|=\mathrm{poly}(n)$ restriction.

**The big picture** Quantum Fourier transforms over commutative groups are the workhorse of Shor-type algorithms, but for non-commutative groups efficient circuits are known only for a handful of families, which is one reason the hidden subgroup problem beyond abelian groups remains algorithmically stuck. This work supplies two systematic construction toolkits built from classical representation-theoretic machinery — decomposing an induced transform over double cosets, and exploiting normal subgroups — and demonstrates them on two families where the resulting circuits are exponentially smaller than what previous generic methods gave. The matrix-group case is notable because the group is a natural nonabelian family of exponentially large order whose transform now costs only polynomially in the number of bits describing a group element.

**Key contributions**
- A Mackey-theoretic "induced transform" primitive generalizing Beals' subgroup-chain algorithm, with explicit twisting/untwisting and $A$-matrix operators for double cosets where restriction is not simply multiplicity-free.
- An explicit, fully worked $\mathrm{poly}(\log q)$ QFT for $\mathrm{GL}_2(\mathbb F_q)$ along the chain $\{I\}\subset T\subset B\subset \mathrm{GL}_2$, including Gelfand–Tsetlin bases and all transversal matrix coefficients (Gauss-sum expressions) for principal series, Steinberg, determinant and cuspidal irreps.
- A coherent "Gauss phase" gate $\ket\alpha\mapsto (g_q(\alpha)/\sqrt q)\ket\alpha$ built from phase kickback plus additive/multiplicative Fourier transforms.
- A Clifford-theoretic construction for wreath products with cost depending on the QFT for $F$ and on representation-register size.

**How it works** For $\mathrm{GL}_2$, restriction along $T\subset B\subset G$ is shown multiplicity-free, and the Bruhat decomposition yields only two double cosets ($H_e=B$, $H_w=T$), so untwisting reduces to swapping character labels. The only block whose size grows with $q$ is the $q\times q$ block $A_{\rho_\gamma,\rho_\gamma}$ mixing the identity cell with the Weyl cell; it is implemented by a diagonal Gauss-sum phase, an inverse multiplicative Fourier transform over $\mathbb F_q^*$, a "quadratic branching" gate that routes a field element $t$ according to whether $X^2-X+t$ splits (split torus → principal series; irreducible → cuspidal, indexed via $\ker\mathrm{No}\subset\mathbb F_{q^2}^*$), branch Fourier transforms, then folding of Weyl/Frobenius orbit labels and small exceptional rotations. Interconversion between additive and multiplicative field encodings uses reversible exponentiation and an amplified reversible Shor discrete-logarithm routine.

**Why it matters** This substantially widens the catalogue of nonabelian groups with efficient QFTs and provides reusable machinery (double-coset induction, Clifford-theoretic normal-subgroup induction) that others can apply to further families — of interest to anyone working on nonabelian HSP, Schur-like transforms, or representation-theoretic quantum subroutines.

**Caveats** Efficient QFT does not by itself yield HSP algorithms. The circuits are approximate and rely on coherent discrete logarithm as a subroutine, so gate counts hide Shor-sized overheads and the basis choice depends non-canonically on a generator of $\mathbb F_q^*$. The result is specific to rank one/2×2; extension to $\mathrm{GL}_n(\mathbb F_q)$ is left open. Wreath-product cost still scales with representation-register size, and constants/explicit gate counts are not optimized.

## 2. Quantum Fourier transform for the symmetric group

[arXiv:2608.28569](https://arxiv.org/abs/2608.28569) · [SciRate](https://scirate.com/arxiv/2608.28569)

*Carli Bruinsma, Dmitry Grinko, Maris Ozols*

**TL;DR**
The authors re-derive, at the level of one- and two-qubit gates, the two known circuit families for the quantum Fourier transform over the symmetric group. They show that Kawano–Sekigawa's claimed Õ(n³) gate count is an artifact of a nonstandard gate model (and of an under-specified multi-qubit "embedding" gate), correcting it to Õ(n^3.5) gates / Õ(n³) depth, and show that Beals' older construction, with a better choice of coset transversals and Yamanouchi-word path encoding, actually achieves Õ(n³) gates, Õ(n³) depth and Õ(n^1.5) qubits — the best known.

**The big picture**
The Fourier transform over the group of permutations is the workhorse behind quantum algorithms for representation-theoretic quantities such as Kronecker, Kostka, Littlewood–Richardson and plethysm coefficients, and it is currently the asymptotic bottleneck in the fastest known Schur transform. Since no superpolynomial speedups are expected for these tasks, the size of the polynomial gap — and hence the practical value of the algorithms — hinges entirely on how efficiently this transform can actually be compiled. The paper does the compilation carefully, finds that the fastest published construction was over-optimistically costed, and shows that a simpler, older recursive construction wins once the encoding of group elements is chosen well.

**Key contributions**
- Corrected complexity of the Kawano–Sekigawa algorithm in the standard one-/two-qubit model: Õ(n^3.5) gates, Õ(n³) depth, Õ(n^1.5) qubits; the embedding gate costs O(n^{3/2}) gates (O(n) depth), not O(n) gates.
- Simplification of that algorithm: a Mackey-theoretic derivation of its second induction relation, a transversal choice that eliminates the gate K_n entirely, and correct identification of the post-recursion basis (including previously omitted "detour" paths) which eliminates the relabeling gate P_n.
- Detailed circuit for the Beals/Moore–Rockmore–Russell approach with transversal T_n = {(1,…,n)^i}, whose gate cancellations drop the count from Õ(n⁴) to Õ(n³) — currently the best asymptotics.
- Space-complexity analysis of path encodings: Yamanouchi words use Θ(n log n) bits (optimal); absolute path encoding is never asymptotically optimal.

**How it works**
Both algorithms are recursive along the multiplicity-free chain S₁ ⊂ … ⊂ Sₙ, so the QFT is a product of induction maps U_ind^(m) acting on a Gelfand–Tsetlin (Young–Yamanouchi) path register, controlled by the endpoint of the conjugate path. For Beals, U_ind = ∏ₖ R(tₖ) U↑ Vₖ U↑† R†(tₖ), where U↑ extends a path to a superposition over addable cells with amplitudes √(d_μ/(n d_λ)) (computed via the content/hook-ratio identity), Vₖ swaps a transversal label with a marker state |⋆⟩, and R(tₖ) applies Young's orthogonal form. Choosing cyclic transversals makes consecutive R†(tₖ)R(tₖ₋₁) collapse to a product of adjacent-transposition irreps, each costing Õ(1) gates; U↑ costs Õ(n) gates in Õ(√n) depth, giving Õ(n²) per level. The Mackey route instead uses the two S_{n−1}-double cosets of Sₙ, {e, σ_{n−1}}, with H_e = S_{n−1}, H_{σ} = S_{n−2}, yielding transversals {(i,…,n)} and a recursion of U_ind on itself.

**Why it matters**
Anyone quantifying quantum-vs-classical gaps for plethysm/Kronecker coefficients, or costing Krovi's Schur transform, should use the corrected numbers; the explicit low-level circuits also make the transform implementable rather than merely asymptotically bounded.

**Caveats**
Coherent arithmetic subroutines are assumed to be polylog-cost, absorbing nontrivial constants into the Õ. Space is Õ(n^1.5) qubits, well above the Θ(n log n) information-theoretic optimum. Errors are stated as polylog(1/ε) in diamond norm with no explicit constants or resource estimates, and no lower bound or optimality claim is established for Õ(n³).

## 3. Exact quantification of nonlocal magic

[arXiv:2608.28563](https://arxiv.org/abs/2608.28563) · [SciRate](https://scirate.com/arxiv/2608.28563)

*Piotr Sierant*

**TL;DR** The local-unitary minimization defining nonlocal magic is solved exactly for the stabilizer fidelity: for any pure multiqubit state and any bipartition, the nonlocal min-relative entropy of nonstabilizerness equals the minimum Rényi-1/2 divergence between the entanglement spectrum and the flat spectra of dyadic rank $2^k$ ("Bell-pair sectors"), i.e. the largest of only $\nu+1$ partial sums of ordered Schmidt coefficients. The same quantity is shown to be equivalent, up to a sharp additive constant $\log_2(3+2\sqrt2)$, to the maximal Schmidt weight in any octave of rank, so a family universally embezzles entanglement under LOCC precisely when its nonlocal magic diverges.

**The big picture** Magic — the resource beyond stabilizer circuits — depends on the choice of local measurement axes, so for a state shared by two parties one wants the part of magic locked into the correlations rather than into local bases. Extracting it requires optimizing over all local basis changes, which had resisted solution beyond two qubits. Here that optimization collapses to reading off the entanglement spectrum, making nonlocal magic as cheap to obtain as entanglement itself in tensor-network simulations or entanglement spectroscopy, and revealing that it coincides with a state's power to lend out entanglement catalytically.

**Key contributions**
- Exact closed form for nonlocal stabilizer fidelity at arbitrary, possibly unbalanced, cuts; the sorted computational-basis representative is proven globally optimal, and simultaneously optimal in every rank sector.
- Bounds: $0\le D^{\rm NL}_{\min}\le\log_2(\nu+1)$ and $D^{\rm NL}_{\min}\le\log_2(2S_1+3)$ — nonlocal magic is at most logarithmic in entanglement entropy, so its regularized rate vanishes.
- Two-sided equivalence with the embezzlement octave weight $\eta_{\rm emb}$; divergent nonlocal magic ⟺ universal LOCC embezzler.
- Class analysis: Haar states $O(1)$ ($D_0<1/4$; exponentially small $\sim 2^{-\Delta}/(4\ln 2)$ for imbalanced cuts); CFT/Calabrese–Lefevre spectra $\tfrac12\log_2\ln L_{\rm eff}+\tfrac12\log_2(\pi c/24)$; van Dam–Hayden catalysts $\log_2\ln d-2$; random singlets exactly zero. Tensor powers: $\tfrac12\log_2 m+O(1)$ unless the spectrum is flat.
- Nonlocal SRE bracketed by NMRE ($\tfrac15 D\le \mathcal M\le 4D$ on balanced cuts), plus lower bounds on nonlocal extent and robustness.

**How it works** Any pure stabilizer state is, up to party-local Cliffords, $k$ Bell pairs plus product spectators, so its entanglement spectrum is flat with $2^k$ entries. Maximizing overlap over local unitaries at fixed rank is then von Neumann's trace inequality (Schmidt-vector overlap lemma), giving $F_k=2^{-k}(\sum_{x<2^k}\mu_x)^2$; the answer is the upper envelope of these $\nu+1$ branches. The entropy bound follows from a greedy allocation over dyadic shells; the embezzlement bounds from an AM–GM argument inserting an octave into the nearest dyadic sector.

**Why it matters** Nonlocal magic becomes a free by-product of DMRG/MPS bond spectra (with an explicit $2\sqrt{\varepsilon}$ stability bound under truncation or measurement error) and of randomized-measurement/entanglement-Hamiltonian tomography, versus exact fixed-basis stabilizer fidelity capped at ~9 qubits. It also gives a computational-resource reading of catalytic entanglement and separates states that entanglement entropy cannot distinguish (critical chains vs. random singlets).

**Caveats** Exact solution is specific to stabilizer fidelity; nonlocal SRE, extent, robustness and mana optimizers remain open (the balanced-cut SRE bound relies on a companion result). NMRE is neither an entanglement monotone nor additive, and has zero regularized rate, complicating a resource-theoretic reading. The CFT scaling assumes the smoothed Calabrese–Lefevre spectrum and is untested in finite chains. Mixed states are unaddressed, and sample-efficient estimators for partial sums of ordered Schmidt coefficients are still needed.

## 4. Learning to Decode Concatenated Quantum Codes with Hierarchical Message Passing

[arXiv:2608.28571](https://arxiv.org/abs/2608.28571) · [SciRate](https://scirate.com/arxiv/2608.28571)

*Jiahui Wu, Chao Zhang, Zipeng Wu, Shilin Huang*

**TL;DR** The authors build a differentiable, hierarchical message-passing decoder for concatenated stabilizer codes in which soft beliefs about X/Y/Z error bits propagate up and down the concatenation tree, and tiny MLPs learn only the aggregation rule. On the concatenated [[15,7,3]] Hamming code it roughly doubles the depolarizing pseudo-threshold (6.5% → 12.3%) versus the state-of-the-art bidirectional hard-decision decoder, and after fine-tuning on circuit-level Knill teleportation data it beats Goto's dedicated minimum-distance decoder for many-hypercube codes by up to 17× in logical-CNOT failure rate at p = 0.005.

**The big picture** Concatenated codes are attractive for low-overhead fault tolerance, but each new construction has historically needed its own hand-crafted decoder, and the best available ones either ignore correlations between bit-flip and phase-flip errors or truncate their search to stay fast. This work replaces the hand-crafted logic with a generic, learnable belief-propagation scheme that runs directly on the code's concatenation hierarchy, so the same architecture applies to any concatenated stabilizer code, including non-self-dual and non-CSS ones. It shows that learned soft decoding, rather than level-by-level hard decisions, buys large threshold and failure-rate improvements, and that the decoder can be adapted to realistic noise from actual fault-tolerant gadget circuits.

**Key contributions**
- A hierarchical decoding graph whose variable nodes are X, Y, Z observables at every concatenation level, with three constraint types: Pauli compatibility (b_X+b_Y+b_Z=0), stabilizer checks including deliberately redundant generator products (e.g. 45 per [[15,7,3]] block), and parent–child parity constraints linking levels.
- Four aggregated message channels (cross-Pauli, up, down, stabilizer) built from a smooth parity kernel φ(x)=sin²(πx/2), keeping mod-2 semantics differentiable; learning is confined to lightweight update and gate MLPs (state dim r=8, hidden 80/8), level-specific and shared across recurrent blocks.
- Use of auxiliary, stabilizer-dressed logical-observable triples (e.g. weight-3 Steiner-triple representatives in [[15,7,3]]) to enrich the inter-level graph.
- Circuit-level fine-tuning with learnable per-node initial embeddings that absorb position- and level-dependent error biases; 20 epochs on data harvested from the ECT benchmark itself.
- Demonstration on a non-CSS [[8,3,3]] concatenation, where hand-designed decoders are impractical.

**How it works** Beliefs are updated by gated residual mixing of candidate features against the previous state, with the gate reading per-channel squared discrepancies. Training supervises both physical- and logical-level bits with BCE at the last three recurrent outputs (R=5, T=22), sampling p uniformly from [0,p_max] online; inference unrolls R=22 (T≤90) with early stopping when inferred physical errors reproduce the syndrome and agree with the logical prediction. Circuit-level targets are the exact tracked logical coset L(E), with Pauli-frame "label pollution" from postselected |0_L⟩ preparation reduced to minimum-weight representatives.

**Why it matters** It gives a single, retrainable decoding tool for exploring concatenated-code design space (including non-CSS codes) where bespoke decoders don't exist, and shows soft/correlation-aware decoding is worth a factor-of-two in threshold. Relevant to anyone weighing concatenated architectures against surface/qLDPC codes.

**Caveats** Pseudo-thresholds come from crossings at L=2,3 only and are explicitly flagged as finite-size, not asymptotic. The circuit-level comparison uses a *stricter* EDT postselection rule (C2′/C3′) than the reference scheme, so acceptance rates and overhead differ; the reported floor stems from a non-fault-tolerant level-4 preparation admitting weight-6 logical failures. Idling and single-qubit gates are noiseless; failure rates are per block, not per logical qubit. Up to 90 message-passing iterations with per-level networks implies nontrivial latency, and no decoding-time or hardware analysis is given; each code (and level) requires separate training.

## 5. Spectral Theory of Semisimple Bivariate Bicycle Codes

[arXiv:2608.27565](https://arxiv.org/abs/2608.27565) · [SciRate](https://scirate.com/arxiv/2608.27565)

*Eric Sabo, Mahir Bilen Can, David Marquis*

**TL;DR** The paper embeds bivariate bicycle (BB) CSS codes into the classical theory of two-dimensional cyclic codes in the semisimple regime, where the defining ring splits by CRT/Wedderburn into finite fields indexed by Frobenius orbits of the root grid. This yields a root-counting dimension formula (logical dimension = size of the orbit region where *both* check polynomials vanish), a new "colon-ideal" lower bound on distance that captures mixed-block logicals, an orbit-slope criterion for permutation automorphisms and ZX-dualities, and an exact dimension formula for covers/lifts over any finite field.

**The big picture** Bivariate bicycle codes are currently one of the most attractive low-overhead quantum LDPC families for near-term hardware, but essentially every good instance in the literature was found by brute-force numerical search over pairs of defining polynomials, leaving the reasons for their parameters opaque. This work replaces the search with classical harmonic analysis over finite fields: the code is decomposed into independent frequency components, and the number of logical qubits, bounds on distance, symmetries, and behavior under covering constructions can all be read off directly from which frequencies the two defining polynomials kill. That turns code discovery from a lottery into a design problem, and simultaneously makes precise the tension between having many logical qubits and having large distance — the same roots control both.

**Key contributions**
- Self-contained idempotent/Wedderburn theory of semisimple 2D cyclic codes, with orbit idempotents indexed by Frobenius orbits of the grid, and a region partition (both / one / neither polynomial vanishing).
- Dimension formula: only the common-zero region contributes; single-vanishing orbits are proved homologically trivial. Exact X/Z logical duality via the coordinate involution.
- A colon-ideal distance lower bound accounting for logicals supported across both blocks, refined by an "alternating stabilizer exclusion," giving computable bounds from classical 2D cyclic minimum distances.
- Automorphism theory over the prime field: a "spectral slope" per orbit (ratio of the two check components) must match across orbits; unconditional existence of the signed block-swapping ZX-duality needed for fold-transversal logic; characterization of CZ-type gates; metachecks.
- Algebraic (quotient-surjection) treatment of lifts/projections giving an exact cover dimension formula from strictly new common roots, valid over any finite field rather than only characteristic-dividing degrees.
- Appendix: BCH-based product constructions with distance guarantees.

**Why it matters** Anyone designing BB or abelian two-block group-algebra codes gets a way to enumerate and certify all codes on a given grid without writing down stabilizers, plus a principled route to fold-transversal gate structure. The framework also transfers to multivariate and (claimed) twisted-torus and non-abelian generalizations.

**Caveats** The three worked examples show the colon-ideal bound is often far from tight: it certifies 4 for a distance-10 code, 4 for distance 6, and only 2 for a distance-26 code (where the block ideals coincide). The theory is restricted to the semisimple case (gcd(q, ℓm)=1); the non-semisimple/repeated-root extension is left open and expected to require Gröbner methods. Automorphism results specialize to the prime field, since stabilizer codes are only F_p-linear. No new code tables are given (deferred to follow-up), and stabilizer weight is explicitly not controlled — the authors concede the example codes' check weights are likely out of reach for most near-term platforms.
