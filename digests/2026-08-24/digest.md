# SciRate Daily Digest — 2026-08-24

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. A Classification of Translation-Invariant Quantum Codes in Any Dimension

[arXiv:2608.20981](https://arxiv.org/abs/2608.20981) · [SciRate](https://scirate.com/arxiv/2608.20981)

*Andrew Li, Dominic J. Williamson*

**TL;DR** Any translation-invariant CSS code on a $D$-dimensional lattice that arises as a length-2 window of a length-$D$ free resolution over $\mathbb{F}_2[x_1^{\pm1},\dots,x_D^{\pm1}]$ — with the ZX-dual complex also exact — is Hamiltonian-equivalent to $k$ copies of the $(n,D-n)$ toric code, where $k=\dim_{\mathbb{F}_2}M$ is the dimension of the charge module. This covers all $D$-variate $D$-cycle codes (the natural multivariate-multicycle generalization of bivariate bicycle codes) and directly extends Haah's/Bombín's 2D classification to arbitrary dimension.

**The big picture** In two dimensions, every well-behaved translation-invariant topological stabilizer code is just stacked copies of the toric code, which is why the anyon-theoretic toolbox applies uniformly to such codes. In higher dimensions this fails in general, because of fracton phases whose excitations cannot move freely and because several inequivalent toric codes exist. The authors identify a clean structural condition — that the algebraic complex encoding the code's checks, metachecks and duals be as long as the number of translation directions — under which the higher-dimensional classification is just as simple. The upshot is that a large and practically interesting family of low-density parity-check codes with lattice symmetry, including the natural higher-dimensional relatives of the bivariate bicycle codes now popular in hardware proposals, are topological-phase-equivalent to stacks of toric codes, so their logical structure and possibly their decoders inherit toric-code technology.

**Key contributions**
- Proposition 1: if the length-$D$ complex's ZX-dual is exact below degree $D$, the resolved module $M$ has grade $\geq D$, hence codimension $D$, hence is zero-dimensional (charges are mobile, finitely many superselection sectors). Proof via the Rees identity $\mathrm{grade}(M)=\mathrm{grade}(\mathrm{ann}\,M)$ and $\mathrm{grade}\leq\mathrm{codim}$. This rules out fracton behavior *a priori* rather than by assumption.
- Lemma (coarse-graining): restricting scalars to $R'=\mathbb{F}_2[x_i^{\pm L}]$ (with $L$ from Haah's Lemma 7.3) turns $M$ into $(R'/\mathfrak{m})^{\oplus k}$, whose Koszul resolution *is* $k$ copies of the toric code complex.
- Lemma (stably-isomorphic resolutions): two bounded finite-rank free resolutions of the same module agree after adding contractible complexes; proved by placing bounded complexes of projectives in a Frobenius category whose stable category is the homotopy category, plus Quillen–Suslin-type freeness over Laurent rings. The contractible summands decompose into "disks" that are exactly product-state ancillas or stabilizer-module-invisible pieces.
- Main theorem assembling these into a symplectic isomorphism $f_n\oplus(f_n^{-1})^\dagger$ of stabilizer modules.

**How it works** The chain map between $F'_\bullet$ and the Koszul target $G'_\bullet$ is lifted to the doubled (CSS $\oplus$ ZX-dual) stabilizer complex, where the "inverse-dagger" pairing on the qubit degree is automatically symplectic; equivalence therefore holds in Haah's sense (coarse-graining + ancillas + local Clifford circuit).

**Why it matters** Provides a phase-classification anchor for higher-dimensional TI qLDPC codes, and tells designers that $D$-variate $D$-cycle codes cannot yield genuinely new phases — novelty must come from having fewer cycles than variables (fractons) or from breaking translation invariance/finite-size boundary effects.

**Caveats** Results are on the infinite lattice; finite-lattice statements require compactification and the coarse-graining factor $L$ is only guaranteed constant, not small, so practical overhead is unquantified. No distance/rate or decoder consequences are derived (explicitly left open). Exactness of both the complex and its ZX-dual is a strong hypothesis. Concurrent independent work (arXiv, Song et al.) overlaps and motivated Proposition 1.

## 2. Continuous-angle logical rotations in the Steane code

[arXiv:2608.20676](https://arxiv.org/abs/2608.20676) · [SciRate](https://scirate.com/arxiv/2608.20676)

*Eric Huang, Daiwei Zhu, Matteo Ippoliti, Christopher Monroe, Michael J. Gullans*

**TL;DR** — The authors run a transversal-rotation-plus-error-correction protocol on the [[7,1,3]] Steane code on IonQ Forte, showing that a transversal physical $R_Z(\theta)$ followed by Steane syndrome extraction yields a *syndrome-conditioned* coherent logical $Z$ rotation with continuously tunable angle. They derive closed-form expressions for the logical angle and logical dephasing under a physical dephasing model, verify them via logical Ramsey fringes and logical process tomography (best-fit $p\approx2.1$–$2.6\%$), and show that a two-round $+\theta,-\theta$ sequence cancels the logical angle with low dephasing on the trivial-trivial syndrome branch.

**The big picture** — Fault-tolerant quantum computers can only apply a limited set of "easy" logical operations directly; anything with an arbitrary rotation angle normally requires expensive distilled resource states and long gate sequences. A recently proposed alternative is to rotate every physical qubit by a small angle at once and then run ordinary error correction: the measured error syndrome tells you exactly which random-but-known logical rotation you got, and repeating with adaptively chosen angles steers you to the target. This work is the first hardware demonstration of that idea on a genuine error-correcting code, confirming that the resulting logical operations are coherent, predictable, and composable across rounds — a potentially much cheaper route to arbitrary-angle logical gates for quantum simulation.

**Key contributions**
- Exact analytic logical channel for the Steane code under transversal $R_Z(\theta)$ + i.i.d. dephasing: coherence factors $\eta_{\rm t},\eta_{\rm n}$, syndrome probabilities $p_{\rm t}=\tfrac18+\tfrac{7}{32}\lambda^4[3+\cos4\theta]$ ($\lambda=1-2p$), and derived $\phi_s,q_s$. Ideal limit: $\phi_{\rm n}=3\theta$ exactly for all nontrivial syndromes.
- First experimental realization: logical Ramsey interferometry resolving trivial vs. nontrivial syndrome branches, on 7 data + 16 ancilla qubits with flag-qubit-postselected $|\bar0\rangle$ preparation.
- Full syndrome-conditioned logical process tomography (4 input states × 3 bases), decomposing $\mathcal{E}_s=\mathcal{E}'_s\circ\mathcal{R}_Z(\phi_s)$ by Frobenius-minimizing the residual Bloch matrix.
- Two-round $\pm\theta$ composition experiment resolving four syndrome-pair classes, demonstrating angle cancellation and order-asymmetric noise accumulation.

**How it works** — Because the Steane code has weight-4 CSS generators, odd $d_X=d_Z=3$, and $Z$-rotations commute with the antiunitary $\mathcal{K}\prod_j(iY_j)$, each syndrome branch acts as a unitary logical rotation. Analytically, the diagonal action on $|x\rangle\langle y|$ picks up $\lambda^{|x\oplus y|}e^{i\theta(|x|-|y|)}(-1)^{z\cdot(x\oplus y)}$, so $\eta_s$ is a small polynomial in $\lambda$ and $e^{i\theta}$ computed from the Hamming codewords. Experimentally, Pauli corrections are commuted through and absorbed as classical bit-flips $\vec{\delta}=H_X\vec{z}$ in postprocessing, avoiding feedforward.

**Why it matters** — Validates the "rotate-and-correct" primitive that underlies proposals for magic-state-free small-angle logical rotations, and gives a concrete noise-model-vs-data benchmark for the next generation of adaptive, feedforward implementations on larger codes.

**Caveats** — Distance 3 means no genuine fault-tolerance claim; the exponential-in-$d$ suppression of $q_s/\phi_s$ is untestable here. Corrections are postprocessed, not fed forward, and state prep is postselected on the flag. Hardware's 36-qubit limit and lack of mid-circuit measurement forced the two-round experiment to use $X$-syndromes only and a single input state. The dephasing-only model fits syndrome probabilities well but fails to capture residual infidelity, especially in nontrivial branches; the observed trivial/nontrivial-order asymmetry is unexplained.

## 3. Tomographic Limits of the Petz Recovery Map

[arXiv:2608.21309](https://arxiv.org/abs/2608.21309) · [SciRate](https://scirate.com/arxiv/2608.21309)

*Peter Sidajaya, Clive Cenxin Aw, Mingxuan Liu, Valerio Scarani*

**TL;DR** Iterating the Petz recovery map on measurement data does not perform quantum state tomography: event-wise updates collapse to pure states (the only fixed points for IC-POVMs), and batch updates can stall on rank-deficient states even though the classical analogue provably converges to the MLE. Lifting the inference to a classical distribution over candidate quantum states — the "extended Petz" map with a candidate state ensemble — restores convergence and reproduces exactly standard Bayesian tomography (event-wise) plus a new batch variant. A "mirrored Petz" update, √R ρ √R, is also introduced and converges numerically wherever the ordinary Petz fails.

**The big picture** Retrodiction — inferring what went in from what came out — is the quantum version of Bayes' rule, and the Petz recovery map is the leading candidate for it. One would expect that repeatedly applying rational inference to accumulating measurement data should eventually pin down the unknown state, exactly as repeated Bayesian updating does classically. This paper shows that expectation fails for the standard quantum construction, and diagnoses why: the belief being updated is stored as a single quantum state rather than as a spread of confidence over possible states. Once the belief is stored the right way, quantum retrodiction and Bayesian tomography become the same thing.

**Key contributions**
- Systematic 2×2 classification (classical vs. Petz, event-wise vs. batch, unextended vs. extended) of when iterated retrodiction achieves tomography.
- Proof (Theorem 3) that classical batch Jeffrey conditionalization converges to the MLE, by identifying it as Csiszár–Tusnády alternating I-projection / EM between the two convex sets {E(y|x)p(x)} and {J(x,y): Σ_x J = q(y)}; this isolates the classical–quantum gap.
- Showing the event-wise extended Petz update reduces exactly to Schack–Brun–Caves Bayesian tomography, and the batch extended Petz reduces to classical Jeffrey updating on the parameter space (hence converges).
- The mirrored Petz map, obtained by reversing factor order, evocative of but distinct from the RρR MLE algorithm; empirically robust.
- Mechanistic explanation of Petz failure: in the ρ̂ eigenbasis the update scales off-diagonal entries by √(λ_j λ_k) ~ O(√ε), so near-rank-deficient estimators cannot rotate their eigenbasis and get locked, forcing λ_j → 0.

**How it works** The extended Petz map applies the Petz construction to Tr_B ∘ (E_A ⊗ I_B) with reference prior ∫dx p(x)|ψ_x⟩⟨ψ_x|_{AR} ⊗ |x⟩⟨x|_C, where ψ_x purifies candidate ρ_x. Tracing out RC yields p_{i+1}(x) = p_i(x)·Tr[M_k ρ_x]/Tr[M_k ρ̂_i], i.e. Bayes' rule on the candidate ensemble, with ρ̂ only the mean.

**Why it matters** It sharpens what "quantum Bayesianism via Petz" can and cannot do, and argues that a density operator alone is an inadequate carrier of belief about a quantum system — one needs a classical distribution over purified candidates. Relevant to quantum retrodiction, thermodynamics of inference, and tomography practitioners.

**Caveats** Convergence claims for the mirrored Petz are purely numerical (no theorem); failure diagnosis is a sketch. Batch analysis is asymptotic (q = E[ρ], no sampling noise). Failure flagging (trace distance > 0.01 after 5×10⁴ iterations) admits false positives/negatives. Extended methods require discretizing the candidate ensemble, whose cost in high dimension is not analyzed. The prior-to-estimator map is non-injective, so the underlying belief is not identified.

## 4. Random quantum circuits, chaos and quantum thermalization

[arXiv:2608.21303](https://arxiv.org/abs/2608.21303) · [SciRate](https://scirate.com/arxiv/2608.21303)

*J. T. Chalker*

**TL;DR** — Lecture notes from the June 2025 "Fundamental Problems in Statistical Physics XVI" school giving a compact, pedagogical derivation of the three canonical random-circuit results: biased-random-walk operator spreading (butterfly velocity v = (q²−1)/(q²+1), diffusive broadening D = 2q²/(q²+1)²), entanglement growth as a minimal-cut / entanglement-membrane domain wall with tension ln[(q²+1)/2q] per step, and the spectral form factor of spatially extended Floquet circuits, K(t) = t[1+(t−1)e^{−εt}]^{L−1} for the random phase model, giving a Thouless time scaling as ln L.

**The big picture** — Most of the tools of many-body quantum theory were built for special cases: integrable systems with extensively many conserved quantities, or low-temperature states with long-lived quasiparticles. Generic, strongly interacting, far-from-ground-state dynamics has neither, and the interesting information is not in any individual matrix element or energy level but in statistical regularities. Random quantum circuits transplant the old nuclear-physics idea of replacing a specific Hamiltonian with an ensemble directly to the time-evolution operator, while retaining spatial locality; averaging over the ensemble makes questions about information spreading, entanglement growth and level statistics analytically tractable. These notes walk through the minimal calculations that yield the universal answers, aimed at readers meeting the subject for the first time.

**Key contributions** — pedagogical, not new research:
- A unified narrative connecting Dyson's "renounce knowledge of the system" to circuit ensembles, motivating why one models the evolution operator rather than the Hamiltonian.
- A counting-argument shortcut for the operator-string hopping probability p = q²(q²−1)/(q⁴−1) = q²/(q²+1), avoiding the explicit Weingarten computation.
- A self-contained treatment of the second-order Haar average (Weingarten weights W(1)=(N²−1)⁻¹, W(σ)=−[N(N²−1)]⁻¹) in a pairing-vector |A⟩, |B⟩ formalism, showing M|A⟩=|A⟩, M|B⟩=|B⟩ and the domain-wall weight q/(q²+1).
- A Feynman-path-in-Fock-space account of the SFF ramp and its many-body modification by pairing domain walls with penalty e^{−εt}.
- A taxonomy of circuit variants: RUC vs. random Floquet circuits, U(1)-symmetric block gates on (↑,↓)⊗C^q, and the random phase model with tunable coupling ε.

**How it works** — Operators are treated as vectors under the Hilbert–Schmidt product; the right end of a Pauli-string distribution p_k(t) executes a biased random walk under Haar averaging, and the OTOC follows exactly as C(x,y;t)=Σ_{k<x} p_k(t). Purity is computed by contracting two forward and two backward copies of the circuit; each Haar gate projects onto the two-dimensional {|A⟩,|B⟩} pairing space, so [Tr ρ_A²]_av = (2q/(q²+1))^t at early times, a directed walk whose minimal-cut geometry reproduces linear-then-saturating entropy growth. The SFF is expanded diagrammatically with Gaussian W_{ab} of variance 1/N; the t time-translated path pairings give K(t)=t up to the Heisenberg time N, while in the extended system position-dependent pairings generate the L-dependent enhancement.

**Why it matters** — A clean, short entry point for students and for researchers in adjacent areas (quantum information, holography, cold atoms) who want the actual mechanics behind butterfly velocities, entanglement membranes and Thouless times rather than a review-length citation list.

**Caveats** — Strictly 1D brickwork, Haar gates, and mostly the large-q limit; averaged purity is computed rather than averaged entropy (replicas deferred); the SFF plateau beyond the Heisenberg time is inaccessible to the diagrammatics presented; figures are absent from the source, so the pictorial arguments require reconstruction; measurement-induced transitions and experimental platforms are explicitly out of scope.

## 5. Hypothesis testing between quantum ensembles

[arXiv:2608.21321](https://arxiv.org/abs/2608.21321) · [SciRate](https://scirate.com/arxiv/2608.21321)

*Jian Yao, Quntao Zhuang*

**TL;DR** The authors set up binary hypothesis testing between *finite quantum ensembles* — unordered collections of labeled states, where only the equality pattern of observed labels is meaningful — and show the sampled joint state decomposes, via Möbius inversion on the partition lattice, into power-weighted moment operators $\mathcal K^{(r)}=\sum_i p_i^r\rho_i^{\otimes r}$. This gives the exact Bayes-optimal measurement and error for $M$ samples, Chernoff-type exponent bounds (tight for uniform pure-state ensembles, where the exponent equals $-\log[1-W]$ for an optimal-transport distance), and a sharp $\Theta_d(t^{-2})$ scaling for the best achievable exponent between two $t$-designs.

**The big picture** Many objects in quantum information — random circuit ensembles, designs, measurement-induced ensembles, communication constellations — are collections of states with attached classical tags, and they carry more information than their average state but less than a fully labeled classical-quantum object, because relabeling the components leaves the ensemble unchanged. This work builds the discrimination theory for exactly that intermediate object: how many samples, and what measurement, are needed to tell two such collections apart. The answer is that distinguishability is controlled by the whole hierarchy of moments up to the sample number, not by any single moment, and that ensembles matching to high design order are exceptionally hard to separate.

**Key contributions**
- Formal label-invariant sampling model: observed data are a partition of sample positions, with branch state $\Omega_\Pi$ summing over compatible intrinsic label assignments.
- Möbius moment expansion $\Omega_\Pi=\sum_{R\succeq\Pi}\mu(\Pi,R)\bigotimes_D\mathcal K^{(|D|)}$, with $\mu=\prod_D(-1)^{m_D-1}(m_D-1)!$.
- Exact minimum Bayes error as a sum of trace norms of branchwise Helstrom operators; reduces to the classical formula when components are orthogonal.
- Exponent sandwich $\min\{\xi_{\rm in},\xi_{\rm acr}\}\le E\le\xi_{\rm acr}$ using permutation-indexed Chernoff quantities; equality for finite uniform pure ensembles (proved via a support-test POVM plus a compactness lemma bounding branch-frame singular values away from zero).
- Identification $E=-\log(1-W(\mathcal E_0,\mathcal E_1))$ with the fidelity-cost Wasserstein distance.
- $t$-design converse: $E\le-\log x_{\max}$, $x_{\max}$ the largest root in $(0,1)$ of a Jacobi polynomial $P^{(d-2,\beta_t)}_{\lceil t/2\rceil}$, giving $O_d(t^{-2})$ and sample complexity $\Omega_{d,\epsilon}(t^2)$; matching achievability gives $\Theta_d(t^{-2})$.

**How it works** The refined "labeled" problem is an i.i.d. test between direct-sum states $\widetilde\rho_{h,\alpha}$ over all relabelings; averaging over $S_N$ reproduces the label-invariant branch structure exactly, so the multiple-hypothesis quantum Chernoff theorem yields achievability and the refined test yields the converse. Worked examples: $\mathcal E_Z$ vs $\mathcal E_X$ ($P_e=1/2$ for $M=1$, $1/4$ at $M=2$, $\sim2^{-M-1}$); rotated BPSK constellations with $E=2|\alpha|^2$; and ensembles sharing components but with swapped weights, where the exponent transitions between classical ($\xi_B(p,1-p)$) and quantum ($-\log c$) control at $c_*=2\sqrt2/3$ for $p=1/3$.

**Why it matters** Provides operational, moment-based figures of merit for how well finite designs approximate each other or Haar, relevant to deep thermalization, generative quantum models, and constellation identification in optical communication.

**Caveats** Exponent tightness is proven only for finite *uniform pure-state* ensembles of equal cardinality; for mixed or nonuniform ensembles a gap between $\xi_{\rm in}$ and $\xi_{\rm acr}$ remains. Optimal measurements are collective across all $M$ registers and branch-dependent, hence impractical. Finite-$M$ formulas require summing over the partition lattice (Bell-number many terms). The $N^{1-1/k}$ sample-complexity claim is asserted, not proved here; the source is truncated before the design proofs. The authors note ChatGPT was used to assist the analyses.
