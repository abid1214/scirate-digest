# SciRate Daily Digest — 2026-09-26

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Design Principles for Ultra-High-Rate Quantum Codes

[arXiv:2609.30069](https://arxiv.org/abs/2609.30069) · [SciRate](https://scirate.com/arxiv/2609.30069)

*Jong Yeon Lee, Koki Okada, Nishad Maskara, Kenta Kasai, Hengyun Zhou*

**TL;DR** The authors give a systematic design methodology for ultra-high-rate quantum LDPC codes built from circulant-permutation "pair-partition" (CPM-PP) templates, plus a symplectic "halving" (fold) transformation that exactly halves blocklength while preserving rate at modest distance cost. Using ensemble density-evolution and weight-enumerator analysis they identify the column weight (qubit degree per Pauli type) as the key knob, and show that at 0.1% physical error the distance gain from heavier checks outweighs the decoding penalty — yielding compact non-CSS codes such as [[90,21,11]], [[140,31,15]], and [[200,43,20]] at check weight 10.

**The big picture** Fault-tolerant quantum computing is bottlenecked by the number of physical qubits needed per logical qubit, and a new generation of very high rate codes promises as few as two physical qubits per logical one. What has been missing is a principled way to navigate the tradeoffs among rate, protection level, how many qubits each parity check touches, and total block size — most known examples come from brute-force search. This work supplies templates, a symmetry-based blocklength-halving transformation, ensemble-level theory predicting where good codes live, rigorous tools for certifying protection levels, and recipes for choosing low-weight logical operator bases, turning an ad hoc search into a design flow.

**Key contributions**
- Pair-partition CPM code templates and a *halving* transformation that folds a CSS parent with a fixed-point-free ZX duality into a non-CSS code of half the blocklength and same rate.
- A twisting trick (multiplying the duality by a central, φ-fixed group element) that removes fixed points; a necessary condition that the lift group's center have even order — which, e.g., excludes the [[150,30,10]] code's group.
- Family-level distance upper bound d ≤ (J+1)! for fully-populated CPM families at column weight J (24 for J=3, 120 for J=4), via permanent vectors — showing distance cannot grow unboundedly with lift size at fixed degree.
- Symmetry-reduced branch-and-bound minimum-distance certification for CSS and general stabilizer codes, with cyclic-translation reduction (state count independent of lift size P) and parent-distance pruning for folded codes; yields exact certificates like [[92,25,8]].
- CRT/"packet" machinery for constructing canonically paired, low-weight logical bases, including repeated-root (even P) cases; e.g. [[184,50,10]] bases reduced from weights (46,54) to (10,12).

**How it works** Density evolution on joint-Pauli BP over depolarizing noise ranks degree distributions; finite-size checks show p₅₀ converging to p_DE (gap 2.2×10⁻⁴ at n=3684, widths scaling as n^{-1/2} with σ√n ≈ 0.25). Regular-ensemble weight enumerators give a growth-rate exponent whose first positive zero sets the achievable relative distance, motivating larger column weight for compact blocklengths. Logical bases are obtained by factoring the cyclic group algebra into packets, imposing field-valued duality in each reciprocal packet pair, then reducing weights by stabilizer-coset BP-OSD search.

**Why it matters** Relevant to anyone building qLDPC memories under qubit-count pressure — especially neutral-atom and other platforms tolerant of weight-10 checks. The halving construction and certified-distance toolkit are reusable beyond these families.

**Caveats** The first-moment ensemble argument only excludes low-weight codewords; it proves neither existence nor concentration, and applies to unconditioned classical kernels rather than CSS quotients. Several reported distances are upper bounds from explicit logicals, not certificates. Analysis is code-capacity, not circuit-level: heavier checks' syndrome-extraction cost and connectivity demands are not simulated, and the even-center condition is necessary but not sufficient.

## 2. Optimal spectrum estimation

[arXiv:2609.30171](https://arxiv.org/abs/2609.30171) · [SciRate](https://scirate.com/arxiv/2609.30171)

*Ainesh Bakshi, Apoorv Vikram Singh, Xinyu Tan*

**TL;DR** The authors pin down the copy complexity of quantum spectrum estimation with entangled measurements at $O(d^2\min\{(\varepsilon\log d)^{-4},(\varepsilon\log d)^{-2}\})$, matching Wang's recent lower bound exactly (up to constants) and refuting the previously conjectured $\Theta(d^2/(\varepsilon^2\log^2 d))$ rate. The engine is a Chebyshev moment-matching framework whose estimator variance is controlled via classical and quantum Efron–Stein (Hoeffding) decompositions, reducing matrix-derivative bounds to scalar derivatives of Chebyshev polynomials. A parallel result gives $O(d^3\min\{\cdot\})$ for unentangled measurements, conjectured optimal.

**The big picture** Learning the full description of an unknown quantum state is expensive, but often one only wants its list of eigenvalues, which determines purity, entropies, and entanglement measures. A natural question is how much of the cost of learning the eigenbasis can be avoided; recent work showed spectrum estimation is genuinely cheaper than full tomography, but the exact rate — and how it varies with the target accuracy — was open. This work settles the question for collective measurements by giving a matching algorithm, revealing two distinct accuracy regimes with different scaling, and shows that the coarse-accuracy regime is cheaper than experts had conjectured.

**Key contributions**
- Tight upper bound for entangled spectrum estimation, matching Wang's lower bound across all accuracy regimes; at constant accuracy $O(d^2/\log^4 d)$ copies.
- Unentangled-measurement algorithm with $O(d^3\min\{\cdot\})$ copies, removing a $(\log\log d)^4$ factor and improving $\varepsilon^{-6}\to\varepsilon^{-4}$ or $\varepsilon^{-2}$ over prior work.
- A general classical recovery framework: reconstruct a spectrum in $\mathcal{Z}_d$ by weighted least-squares matching of estimated Chebyshev moments, with error bounded by approximation error plus $L\sum_k \mathrm{Var}(\widehat F_{q_k})/k^2$.
- Variance bounds for polynomial moment estimators (uniform-POVM snapshots and weak Schur sampling) in terms of $\|p^{(r)}\|_\infty$, via a quantum Hoeffding decomposition.
- Rank-$r$ version via Lowe–Tan dimension reduction, also optimal.

**How it works** Stage one reuses known bucketing algorithms to learn eigenvalues above a threshold and project onto a small-bucket state $\sigma\preceq L I$. Stage two matches Chebyshev moments of $\sigma$. Wasserstein duality plus a Jackson approximation with damped Chebyshev coefficients gives a test function whose coefficient energy $\sum k^2 a_k^2 \le CL\,\mathrm{TV}$, converting moment error into TV error. Variance of $\widehat F_p$ decomposes over Efron–Stein levels $r$ with weights $c_r/\binom{n}{r}$ and $(\|p^{(r)}\|_\infty/r!)^2$. Two affine rescalings trade off: mapping $[0,L]\to[-1,1]$ gives approximation error $\sqrt{dL}/K$ but derivatives $2k^2/L$; mapping to $[-1/2,1/2]$ gives $dL/K$ but derivatives $\le 2k/L$, permitting higher degree $K$. These yield the $(\varepsilon\log d)^{-4}$ and $(\varepsilon\log d)^{-2}$ branches respectively.

**Why it matters** Closes a line of work started by Wright's 2016 conjecture, and supplies a reusable moment-matching + Efron–Stein toolkit likely applicable to other property-estimation problems (entropies, purity, spectral functions). Relevant to quantum learning theory, and to anyone budgeting copies for entanglement-spectrum measurements.

**Caveats** Optimality for unentangled (including adaptive) measurements remains conjectural. Guarantees are in expectation over TV with 0.99 success after the bucketing stage; recovery is a convex program over a grid costing $\mathrm{poly}(d,K,1/\eta)$ classical time, and the entangled scheme requires weak Schur sampling on all copies. Constants are unspecified universal constants, and the source shown is truncated before the final rate derivations.

## 3. Deep thermalization and Hilbert space ergodicity

[arXiv:2609.30248](https://arxiv.org/abs/2609.30248) · [SciRate](https://scirate.com/arxiv/2609.30248)

*Daniel K. Mark, Manuel Endres, Matteo Ippoliti, Wen Wei Ho, Soonwon Choi*

**TL;DR** A review of deep thermalization and Hilbert space ergodicity: the claim that quantum state *ensembles* — projected ensembles of conditional subsystem states given bath measurement outcomes, and temporal ensembles traced out by a state under unitary evolution — become maximally random subject to physical constraints, not just maximally mixed at the level of density matrices. The organizing principle is information-theoretic: unconstrained dynamics yields the Haar ensemble, while conserved quantities or informative measurement bases yield Scrooge and generalized Scrooge ensembles, which minimize accessible information (equivalently maximize an ensemble entropy) at fixed mean state.

**The big picture** Conventional quantum thermalization says that a small piece of a large isolated system looks thermal once you average over everything you cannot see. But today's quantum simulators can see much more: single-shot snapshots of every particle, subsystem tomography, and long time traces. Once that fine-grained information is available, the right object is no longer an averaged state but a whole probability distribution over pure states, and it turns out these distributions have their own universal, maximally random form dictated by which conservation laws and which measurements are in play. This upgrades statistical mechanics with a second, deeper layer of universality, and simultaneously turns ordinary chaotic dynamics into a source of usable randomness for benchmarking, tomography, and certification on hardware without gate-level control.

**Key contributions**
- Unified presentation of projected and temporal ensembles as two faces of one framework, with moment operators and trace distance between k-th moments as the diagnostic.
- A maximum-entropy/minimum-accessible-information organizing principle: Holevo bound above, subentropy below, Scrooge ensemble saturating the lower bound; generalized Scrooge ensembles when bath measurements leak charge or energy information (minimizing interaction information).
- Survey of exact/rigorous results: dual-unitary circuits, single-instance deep random circuits, aperiodically driven Hamiltonians, and time-independent Hamiltonians under k-th no-resonance conditions.
- Catalog of the emerging phase structure: "deep ergodicity breaking" transitions driven by coherence or non-stabilizerness thresholds; k-HSE vs complete HSE; Gaussian (bosonic/fermionic) Scrooge ensembles; noisy generalizations giving Erlang/hypoexponential/Wishart probability-of-probabilities.
- Experimental synthesis across Rydberg arrays, superconducting qubits, and NV centers, including direct measurement of higher moments.

**How it works** Ensembles are compared via k-copy moment operators; vanishing trace distance at order k means indistinguishability by any k-copy protocol, i.e. a state k-design. Scrooge sampling is Haar sampling deformed by the square root of the mean density matrix with an acceptance probability. Physically, infinite-temperature or unconstrained dynamics gives Haar; finite temperature or conservation laws deform the limit to Scrooge ensembles built on local Gibbs states (projected) or the diagonal ensemble (temporal).

**Why it matters** It supplies a principled taxonomy for what "maximally random" means under constraints, and makes intrinsic, deterministic chaos a substitute for externally injected randomness — relevant to analog simulator benchmarking, randomized measurement protocols, and possibly cryptography.

**Caveats** As a review, no new results. Key open issues flagged: the post-selection problem and exponential sample complexity of reconstructing either ensemble; unclear logical relations between deep thermalization, ETH refinements, and conventional thermalization; the complexity of specifying energy-conserving generalized Scrooge ensembles may be exponential; mixed-state, open-system, and channel-level generalizations remain immature; and whether Scrooge randomness enables applications Haar randomness cannot is unresolved.

## 4. Proper Agnostic Learning of Matrix Product States and Tree Tensor Networks

[arXiv:2609.30148](https://arxiv.org/abs/2609.30148) · [SciRate](https://scirate.com/arxiv/2609.30148)

*Constantin Cedillo Vayson de Pradenne, Jordan Cotler*

**TL;DR** The authors give the first *proper* agnostic tomography algorithms for matrix product states and bounded-degree tree tensor networks: from copies of an arbitrary $\rho$, they output an actual bond-$D$ MPS/TTN whose fidelity score is within $\varepsilon$ of the best achievable in the class, using $\mathrm{poly}(n,d,D,1/\varepsilon)$ copies and runtime polynomial in $n$ for fixed $d,D,\varepsilon$. The two new ingredients are a generic improper-to-proper reduction that compresses the *objective* (not the hypothesis) onto an $O(\varepsilon^{-2})$-dimensional subspace, and a "comparator-dual" singular-value-shrinkage compression whose error is independent of chain length.

**The big picture** Learning algorithms for many-body states either assume the unknown state really is a simple tensor network, or they return an answer that scores well but is itself complicated and therefore useless as a compact description. This work closes that gap: with no assumption at all on the unknown state, it returns a genuine low-complexity description whose quality is provably near the best any description of that complexity could achieve. Along the way it introduces a compression idea — approximate a state only as seen by a restricted family of test states — whose error does not grow with system size, which is of independent interest for classical tensor-network rounding.

**Key contributions**
- General reduction: repeated calls to an improper learner on postselected residuals build $m\le 2/\theta$ orthonormal directions such that projecting $\rho$ there perturbs every comparator's score by $\le 2\sqrt\theta$; spectral cutoff plus an $\varepsilon$-net then yields $(C/\varepsilon)^{O(1/\varepsilon)}$ explicit *pure* targets.
- Comparator-dual compression: for any $u$, a bond-$K$ MPS $\tilde u_K$ with $\sup_{\psi\in\mathrm{MPS}_D}|\langle\psi|u-\tilde u_K\rangle|\le\|u\|_2\sqrt{D/(K+1)}$ — no $n$-dependence. Same sweep gives Euclidean relative error $(K+1)/(K+1-D)$ vs. best bond-$D$ approximation.
- A dynamic program over discretized isometric tensors and "cross environments" that is proper by construction (no final truncation), runtime $n(Cn\sqrt D/\eta)^{O(KD+dD^2)}$.
- TTN version via heavy-child preorder ordering (every prefix cut crosses $\le\Delta_T(1+\lceil\log_2 n\rceil)$ edges, so $\mathrm{TTN}_{T,D}\subseteq\mathrm{MPS}_{D^{w_T}}$, polynomial in $n$), plus leaves-to-root compression.
- Extensions: MPOs by vectorization; reuse of the same quantum data across all $D\le D_{\max}$; learning coherent superpositions of $r$ MPS "branches" under a $k$-local non-interference budget.

**How it works** The shrinkage step is the crux: at each cut one discards the tail *and* subtracts $\Delta_i=\sigma_{K+1}^2$ from every retained squared singular value, yielding $T_i=C_i(T_{i+1}\oplus L_i)$ with $C_i$ contractive, $\|L_i\|_\infty\le\sqrt{\Delta_i}$, and $(K+1)\Delta_i\le\|T_i\|_2^2-\|T_{i+1}\|_2^2$. Since a bond-$D$ comparator has Schmidt rank $\le D$ per cut, von Neumann's trace inequality gives $\|L_i\|^2_{\mathrm{MPS}(D)}\le D\Delta_i$, and the energy drop telescopes to $\|u\|_2^2$.

**Why it matters** Proper learning is what one actually wants for compact classical descriptions and for benchmarking how well a variational class fits real data; the ability to sweep $D$ from a single measurement set turns this into a model-selection tool. Relevant to quantum learning theory, tomography experimentalists, and classical tensor-rounding practitioners.

**Caveats** Runtime exponent scales as $D^2/\varepsilon^2+dD^2$; some such blowup is necessary since even $D=1$ with poly $1/\varepsilon$ would give $\mathsf{NP}\subseteq\mathsf{BQP}$. TTN copy complexity inherits the ambient bond $D^{w_T}=n^{O(\Delta_T\log D)}$. The reduction uses adaptive subspace projections and postselection across copies rather than single-copy local measurements. Near-optimal score is not reconstruction, and the optimum itself may be small. Periodic-boundary MPS remains improper (bond $D^2$ output), and cyclic tensor networks are open; branch recovery needs an extra identifiability assumption.

## 5. Syndrome measurements enable deterministic fault-tolerant $T$ gates

[arXiv:2609.29890](https://arxiv.org/abs/2609.29890) · [SciRate](https://scirate.com/arxiv/2609.29890)

*Kishor Bharti, Tobias Haug, Andrew Tanggara*

**TL;DR** Any stabilizer code with distance ≥ 2 admits a deterministic logical *T* gate built from two overlapping anticommuting Pauli rotations, a syndrome measurement with only two possible outcomes, and Clifford feed-forward — no magic state, no code switching. The authors characterize exactly the "intermediate" code that protects the state mid-gate ($\delta=\min\{d,\mu(s),\nu(A)\}$), show that this alone does *not* give fault tolerance, and give two single-fault-tolerant circuits: a 22-qubit selectively concatenated code (33 qubits peak, 15 physical *T*s) and a Golay-code gate protected by a "transported" check (32 qubits, 22 *T*s per attempt).

**The big picture** Non-Clifford gates are the expensive bottleneck of fault-tolerant quantum computing, usually handled by preparing and distilling special resource states or by switching between codes. This work shows that the error-detection machinery itself — the act of temporarily dropping one check and then measuring the syndrome — can *be* the non-Clifford gate: releasing a check frees up an extra encoded qubit inside the same block of physical qubits, and two carefully chosen rotations plus a measurement steer the logical state deterministically. The authors then analyze exactly how much protection survives while the state is outside the code space, show that this protection is necessary but insufficient, and build explicit circuits that close the remaining gap.

**Key contributions**
- Exact identity: for $AB=iL$ (forced anticommuting, equal syndrome $s\neq0$), $R_A(\pi/2)R_B(\pi/4)$ followed by syndrome measurement yields outcomes $0$ or $s$ with probability 1/2 each, both correctable to $R_L(\pi/4)$; all corrections can be made Pauli via adaptive measurements of $G=iAh$, $M=AhL$, $h$.
- Weight theorem: $\mathrm{wt}(A)+\mathrm{wt}(B)\ge \mathrm{wt}(L)+1$, balanced split gives max rotation weight $\lceil(d+1)/2\rceil$; the maximally unbalanced limit reproduces the ideal channel of magic-state injection.
- Intermediate-code distance $\delta=\min\{d,\mu(s),\nu(A)\}$; pure codes give $\lfloor d/2\rfloor\le\delta\le\lfloor(d+1)/2\rfloor$, but weight-$w$ checks cap $\delta\le w$ — so *no* LDPC family gets unbounded intermediate protection this way.
- Explicit no-go: a $B$ fault between the rotations is syndrome-invisible and reverses the second rotation's angle, giving logical $L$ and $\Theta(p)$ infidelity regardless of $d$ or $\delta$.
- Two one-fault-tolerant constructions with resource counts; the 22-qubit one supports recursive concatenation ($22^\ell$ qubits, $\le15^\ell$ *T*s, distance $\ge3^\ell$, failure needs $\ge2^\ell$ faults).

**How it works** Rotations preserve $\mathcal C\oplus A\mathcal C$, a code whose stabilizer is the half of $\mathcal S$ commuting with $A$; the omitted check $h$ and $A$ act as $\bar Z_p,\bar X_p$ on the freed logical qubit. The 22-qubit gate picks a Clifford frame where $B'=Z_1$, encodes qubit 1 in $[[15,1,3]]$ (transversal $T^\dagger$) and qubit 2 in a 2-qubit repetition block, leaving five qubits bare. The Golay gate measures the Clifford observable $G_B=U_BhU_B^\dagger$ via two verified 4-qubit cat states (circuit-gauge flagging); a local-filter theorem shows $I$ and $B$ are the only Paulis on $\mathrm{supp}(B)$ commuting with retained checks, so every nonidentity fault there is caught, and rejection still permits recovery of the unknown input (Golay syndrome separates all 14,848 hypotheses) plus one retry.

**Why it matters** Offers a magic-state-free, code-agnostic route to *T* gates with concrete small-block circuits, and — arguably more importantly — a clean theory of what protects encoded data *during* a non-Clifford operation, relevant to pieceable fault tolerance, cultivation, and continuous-angle logical rotations.

**Caveats** No thresholds or logical-error numbers are computed; only single-fault guarantees plus an analytic $\binom{N_G}{2}p^2$ bound. The $\delta\le w$ bound makes the direct construction unattractive for LDPC codes. The Golay monitor is protected only for ideally encoded inputs, and correlated angle error shared between rotation and check circuit can be accepted. The 22-qubit gate still consumes 15 physical *T*s; connectivity is assumed flexible with reset and serial ancilla reuse.
