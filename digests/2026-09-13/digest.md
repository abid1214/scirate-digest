# SciRate Daily Digest — 2026-09-13

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. 2609.11830

[arXiv:2609.11830](https://arxiv.org/abs/2609.11830) · [SciRate](https://scirate.com/arxiv/2609.11830)



**TL;DR** For every constant $k\ge 2$ there is an oracle relative to which $\FH_k \subsetneq \FH_{k+1}$ in Shi's Fourier hierarchy, in both the phase-oracle and standard-oracle models — the first oracle separations between consecutive levels above the base case. The separating problem is an OR of $(2k-1)$-fold Forrelation instances: level $k{+}1$ solves it with $O_k(1)$ queries, while level $k$ fails even with $N^{c_k}$ queries ($c_k = \tfrac{1}{4(2k-1)(2k-2)}$, $N=2^n$).

**The big picture** Quantum circuits can be graded by how many rounds of "creating superposition" they use, with everything in between restricted to permutations and phases; one round gives classical randomized power, two already suffice for Simon's problem and factoring. Whether each extra round genuinely buys more power has been open for two decades. This work shows that, at least in a black-box world, the answer is yes at every level, by identifying the right structural principle: the number of interference rounds caps how adaptively a circuit can interrogate its oracle, converting a circuit-depth question into a well-studied query-complexity question about bounded-adaptivity algorithms.

**Key contributions**
- Exact simulation: any $\FH_k$ circuit with $q$ phase queries is reproduced *exactly* (same acceptance probability on every oracle) by a quantum algorithm with $k-1$ rounds of $\le q$ parallel queries.
- Consequent Fourier-growth bound for $\FH_k$ acceptance probabilities, stable under restrictions: $L_{1,\ell}\le (2^{2k-2}-1)^{2\ell}q^{\ell}M^{\frac{\ell}{2}(1-\frac{1}{2k-2})}$.
- Odd-order Forrelation splits into two depth-$k$ halves plus one basis-preserving middle query, yielding a depth-$(k+1)$ interference test using only $k$ queries (and a SWAP-test variant estimating $\mathsf{forr}^2$).
- Worst-case promise problem via OR of $m=2^{5K}$ i.i.d. Bansal–Sinha instances, plus diagonalization; a single oracle strict at all levels; extension to growing depth $k\le cn^{1/3}$ (uniform for $k\le c\log n$).
- A separate decision-tree argument for standard oracles, plus a separation showing standard queries are strictly stronger than phase queries at equal depth.

**How it works** Step 1 observes that in a phase-oracle $\FH_k$ circuit, queries in the first and last basis-preserving blocks contribute only a global phase or a relabeling, and inside each interior block the query *addresses* are oracle-independent — so each block collapses to one parallel batch, giving $k-1$ rounds. Feeding this into the Girish–Sinha–Tal–Wu growth theorem for $r$-round algorithms, then the Bansal–Sinha biased-measure transfer and distinguishing criterion, the advantage sums to $C_k\sum_\ell q^\ell N^{-\ell/(2(2k-1)(2k-2))}$. The choice $K=2k-1$ makes the exponent gap $2(k-1)<K$ strict; a hybrid argument over the $m$ copies reduces worst-case correctness to single-instance distinguishing. At $k=2$ the simulation is non-adaptive, sharpening $c_2$ to $1/6$.

**Why it matters** Resolves Shi's first-step question at every level, and gives a clean dictionary between Hadamard-layer depth and query adaptivity that should be reusable for other depth-limited quantum classes.

**Caveats** Relativized only; the unrelativized conjecture is untouched. The simulation is one-way, so $\FH_k$ is not *characterized* by $(k-1)$-round algorithms, and the optimal query exponent is unknown (limited by the Fourier-weight route, not the construction). Results are for constant $k$, or $k=O(\log n)$ in the uniform variant. The standard-oracle lower bound and the $\bigcup_k\FH_k$ vs $\BQP$ separation fall outside the visible source.

## 2. 2609.11849

[arXiv:2609.11849](https://arxiv.org/abs/2609.11849) · [SciRate](https://scirate.com/arxiv/2609.11849)



**TL;DR** The authors construct explicit PPT (positive-partial-transpose) states on ℂ^m ⊗ ℂ^n whose Schmidt number is at least ⌈(m+n−√((m−n)²+4(m+n−1)))/2⌉, i.e. n − O(√n) for m = n — dramatically beating the previous best lower bounds of roughly n/2. Consequently max-Schmidt-number-of-PPT-states / n → 1, and there exist k-positive indecomposable maps on n×n matrices with k = n − O(√n).

**The big picture** Bound entanglement — entanglement that survives the partial-transpose test yet cannot be distilled into pure entanglement — has long been suspected to be "weak," and one natural quantitative form of that suspicion is that such states should have low entanglement dimensionality. A famous small case (two qutrits) confirmed this, and every construction to date topped out at about half the local dimension. This work shows the intuition is wrong in the asymptotic regime: undistillable states can carry almost the maximum possible entanglement dimensionality, up to a square-root correction. Via the standard duality with positive maps, this also yields indecomposable maps that are positive on nearly all low-rank inputs.

**Key contributions**
- Lower bound n − ⌊√(2n−1)⌋ for equal dimensions (previous: n/2 + O(1)); and Schmidt number ≥ n−1 on ℂ^n ⊗ ℂ^{3n−4}.
- A fully explicit, short (≈4-page) construction and proof.
- Identification of the exact obstruction to pushing further: any state with positive-*definite* partial transpose has rank ≥ m+n−1.

**How it works** Two ingredients. (1) A low-rank state whose partial transpose is strictly positive: take the spin-coupling embedding Sym^{m+n−2}(ℂ²) ⊆ Sym^{m−1}(ℂ²) ⊗ Sym^{n−1}(ℂ²), i.e. the normalized projector onto the top-spin sector, of rank exactly m+n−1, with λ_min of the partial transpose equal to C = 1/((m+n−1)·C(m+n−2, m−1)) > 0. (2) A rank-one perturbation ρ = (σ + 2C|g⟩⟨g|)/(1+2C). PPT-ness follows since λ_min of any pure state's partial transpose is ≥ −1/2. For the Schmidt number, a dimension count: vectors of Schmidt rank ≤ r form a determinantal variety of dimension r(m+n−r), so when (m−r)(n−r) > m+n−1, the Zariski closure of im(σ) + D_r is a proper algebraic subset cut out by polynomials over the algebraic numbers. Choosing |g⟩ with entries exp(2^{(in+j)/mn}), algebraically independent over the algebraics by Eisenstein plus Lindemann–Weierstrass, guarantees |g⟩ avoids that set; hence no Schmidt-rank-≤r decomposition of ρ exists. Solving the quadratic in r gives the stated bound.

**Why it matters** Settles the asymptotic behavior of the maximum Schmidt number of PPT states (ratio → 1), reshaping the qualitative picture of bound entanglement, and supplies a large new family of highly k-positive indecomposable maps — of direct interest to entanglement theory, positive-map/matrix-analysis, and entanglement-dimension witnessing.

**Caveats** The mixing weight 2C/(2C+1) is exponentially small (the binomial coefficient grows like 4^n), so the high-Schmidt-number component is a vanishingly small, presumably extremely fragile perturbation; robustness to noise is not addressed. The bound is only a lower bound and gives nothing new in small dimensions (no improvement on the 4×5, 7×7, 9×9 records). The gap of order √n remains, and the authors note the m+n−1 rank barrier means their strategy cannot be pushed further without new ideas. Whether the true maximum is n−1 or smaller is open.

## 3. 2609.11926

[arXiv:2609.11926](https://arxiv.org/abs/2609.11926) · [SciRate](https://scirate.com/arxiv/2609.11926)



**TL;DR** The paper gives a single-letter formula for the optimal i.i.d. asymptotic conversion rate between *arbitrary* (mixed) states in the resource theory of asymmetry for any compact Lie group: the rate is the largest $r$ such that $\mathcal F_\rho^{f_q}\ge r\,\mathcal F_{\rho'}^{f_q}$ for *every* $q\in[1/2,1)$, i.e. for the whole one-parameter family of quantum Fisher information matrices interpolating SLD and RLD. Crucially, no state-independent finite subset of this family suffices — even for $U(1)$ — which is a qualitative break from all known pure-state laws and leads to a new "asymmetry activation" effect.

**The big picture** How much symmetry breaking does a quantum state contain, and how much of it survives when you convert many copies of one state into copies of another using only symmetry-respecting operations? For pure states this was recently settled by a single geometric quantity, but realistic states are noisy and mixed, and until now only bounds and no-go results existed. This work closes the problem: the answer is governed not by one number or matrix but by an entire continuous family of information measures, all of which must be simultaneously satisfied. That continuum is not a technical artifact — it creates genuine irreversibility, and it lets two states help each other when processed together in a way no single measure could explain.

**Key contributions**
- Complete conversion-rate theorem (the interpolating QFI family is a complete set of asymmetry measures), with constructive protocols achieving error $O(n^{-1/2+\kappa})$.
- Proof that no fixed finite grid of $q$ values works universally; nonetheless the rate is computable by a finite SDP.
- Distillation to pure targets collapses to a single measure: $R(\rho\to\phi)=\sup\{r:\mathcal Q_\rho\ge r\mathcal Q_\phi\}$ with the generalized QGT $(\mathcal Q_\rho)_{ij}=\mathrm{Tr}(\rho X_i(I-\Pi_\rho)X_j)$; converse of Marvian's bound-asymmetry result: $D_\phi(\rho)=0\iff[\Pi_\rho,H]=0$.
- Necessary and sufficient condition for asymptotic reversibility (equal symmetry subgroups plus a *common* proportionality factor across all $q$); round-trip efficiency $1-\tilde{\mathcal F}^{f_{1/2}}_\rho/\mathcal F^{f_{1/2}}_\rho$.
- Asymmetry activation: explicit qubit example with $R(\rho_1\to\sigma)=1/4$, $R(\rho_2\to\sigma)=0$, yet $R(\rho_1\otimes\rho_2\to\sigma)=1/2$.
- Technical: QLAN extended to finite-dimensional unitary models of arbitrary rank and spectral degeneracy; exact characterization of Gaussian-shift-model convertibility by the same QFI family.

**How it works** Covariant-channel convertibility is recast as convertibility of the statistical model $\{\mathcal U_g(\rho)\}$. An estimate-and-localize step (sublinear copies, exponentially small failure) narrows $g$ to $O(n^{-1/2})$, after which the generalized QLAN maps i.i.d. models reversibly onto Gaussian shift models preserving all $f_q$-QFIs; convertibility between Gaussian shifts at rate $r$ is shown equivalent to the full family of QFI inequalities. The converse needs a continuity bound $\frac{1}{m_n}\mathcal F^{f_q}_{\chi_n}\ge\mathcal F^{f_q}_{\rho'}-h_q(\epsilon_n)\mathcal X$ to defeat the $O(\epsilon_n n^2)$ discontinuity of QFI.

**Why it matters** Symmetry breaking now joins entanglement and athermality as an operationally, single-letter-quantified resource — with no regularization or ensemble optimization — and QFIs are measurable via linear response. Directly relevant to quantum clocks/reference frames, covariant error correction, and thermodynamics of coherence.

**Caveats** Finite dimensions, compact Lie groups, exact i.i.d. inputs and vanishing-error (no second-order or finite-$n$ rates, no error exponents); differentiable representations assumed (extension claimed in SM). Activation and the finite-grid no-go are demonstrated on $U(1)$ examples; how common activation is, and its physical exploitability, is open. Reversibility's "unique $r$" clause implicitly excludes degenerate zero-QFI cases.

## 4. 2609.10965

[arXiv:2609.10965](https://arxiv.org/abs/2609.10965) · [SciRate](https://scirate.com/arxiv/2609.10965)



**TL;DR** The paper proposes an end-to-end compilation/resource-estimation pipeline for surface-code FTQC built around an "executable workload" intermediate representation that retains three scheduling-relevant descriptors (weighted logical interaction graph, per-layer operation parallelism, per-layer non-Clifford demand) instead of collapsing a circuit to aggregate gate counts. Using these descriptors to co-select patch layout, non-Clifford supply strategy, and code distance, the authors show on 20 benchmarks that physical cost varies by ~10⁴–10⁵× even though logical widths span only 8–16 qubits, with hybrid rotation handling giving a median 23.8× and maximum 241.5× space–time reduction over all-synthesis.

**The big picture** Estimates of what a quantum algorithm will cost on an error-corrected machine are usually made by counting logical qubits and gates and then assuming a generic hardware substrate. This work argues that the substrate should instead be derived from the algorithm: how the logical qubits talk to each other, how much work runs in parallel at each step, and when in time the expensive non-Clifford operations are needed. Carrying that information forward changes the answer enormously — circuits of nominally identical size can differ by orders of magnitude in real hardware footprint and runtime. The practical payoff is better decisions about layout, magic-state supply, and error-correction strength for near-term fault-tolerant machines.

**Key contributions**
- The executable-workload abstraction and a hierarchical, dependency-preserving scheduler that preserves measurements, resets, classical feed-forward, and rotation angles.
- Workload-conditioned, circuit-specific surface-code layout synthesis (multi-start genetic search over patch placement/orientation, validated by replaying the schedule with explicit routing-cell conflicts) benchmarked against a matched Litinski fast block.
- *Pre-patch parallel cultivation* (PPC): seeding many cultivation candidates before the logical patch boundary is fixed, so grow-and-graft direction is chosen after postselection outcomes are known.
- A full 20-circuit / 7-family benchmark plus a hierarchically composed secp256k1 ECDLP estimate: d=35, 24 factories, 4,014,344 physical qubits, 14.94 days.

**How it works** Algorithms are decomposed recursively into modules with invocation multiplicities (N_g(v) = intrinsic + Σ m_e N_g(child)), compiled to Clifford+R_z, and scheduled under disjoint-support plus precedence constraints. Layout is chosen by minimizing an interaction-weighted communication/resource-access cost; then non-Clifford strategy and code distance are chosen to minimize space–time volume — a *sequential*, not joint, optimization. PPC latency is modeled as T_eff/T_attempt = 1/(1−q^{N_S}) with seeding density N_S = αN_Q; catalogue inputs q = 0.535 (Folded-H f=3) to 0.990 (Gidney f=5), the latter needing ~230–688 seeds for 90–99.9% batch survival.

**Why it matters** Relevant to anyone doing FT resource estimation, magic-state architecture, or lattice-surgery compilation: it gives a traceable path from algorithm to concrete footprint/runtime and quantifies when circuit-specific layouts pay for their extra area (13/20 circuits, 0.07–25.8% volume savings; the other 7 sit 0.20–3.05% above break-even).

**Caveats** Layout uses a static cost proxy, not a time-dependent lattice-surgery schedule; factories are counted but not embedded in a closed 2D floorplan. The 241.5× figure is model-based and hinges on the chosen direct-rotation calibration. PPC assumes independent candidates and ignores correlated failures, boundary effects, grafting contention, storage, and queueing. The ECDLP number is a hierarchical count-consistent proxy with serialized cross-module scheduling, not an expanded schedule. Benchmarks are small (8–16 logical qubits), so layout conclusions may not extrapolate; decoding is folded into an effective stabilizer-round time.

## 5. 2609.11854

[arXiv:2609.11854](https://arxiv.org/abs/2609.11854) · [SciRate](https://scirate.com/arxiv/2609.11854)



**TL;DR** The paper proves $\mathsf{QMA} = \mathsf{PureSuperQMA} = \mathsf{PureSuperQMA}(\exp) = \mathsf{BellPureSymQMA}(\poly)$, refuting Kamminga–Rudolph's conjecture (ITCS'26) that the purity-promise classes sit strictly between $\mathsf{QMA}$ and $\mathsf{QMA}(2)$. The engine is a new dimension-free stability estimate for symmetric tensors: an extremal symmetric eigenvector's test value is within $O(t^2/N)$ (resp. $O(m^2R/N)$) of that of a tensor power, with no dependence on $\dim\mathcal H$. A corollary: exact $k$-local pure-state consistency, and exact bosonic/fermionic pure $N$-representability, are $\mathsf{QMA}$-complete for every fixed $k\ge 2$.

**The big picture** A recurring question in quantum complexity is whether promising a verifier that its proof is a pure state, or that several proof registers hold identical copies of one state, buys any extra verification power. Such promises look powerful because natural physics problems — deciding whether prescribed local marginals of a molecule or many-body system come from a single pure global wavefunction — sit naturally in these models but were not known to sit in the standard quantum analogue of NP. This work shows the promise is worthless: any verifier relying on it can be simulated by an ordinary single-proof quantum verifier, so those physics problems are exactly as hard as the standard local Hamiltonian problem, no harder. The technique sidesteps finite de Finetti theorems, whose error grows with Hilbert-space dimension, by comparing optimal values directly rather than approximating states.

**Key contributions**
- Collapse theorem, including the succinct variant with $2^{\poly(n)}$ uniformly indexed checks (at inverse-poly margin *and* inverse-poly violated fraction), and the Bell model with poly-many local measurements of $O(\log n)$ output length.
- A "bosonic argmax" lemma: for $|\Psi^*\rangle$ symmetric and $|u\rangle$ maximizing $\alpha=|\langle\Psi^*|u^{\otimes N}\rangle|$, all one-transverse-direction overlaps vanish, and $k$-transverse overlaps are $\le \alpha e^{O(k)}(k/N)^{k/2}\prod\|v_j\|$, independent of dimension.
- Explicit uniform compilers with witness $N=O(\delta^{-1}\epsilon^{-4}\log^2(2/\delta))$ blocks (pure-super) and $N=\Theta(m^2R)$ (Bell), raw gap $\Omega(1/N)$.
- Resulting $\mathsf{QMA}$-completeness of exact pure CLDM / pure $N$-representability.

**How it works** Merlin sends $N$ registers; Arthur runs a random-pair SWAP test with probability $1-\vartheta$ and a permutation-invariant lift of the original test otherwise. Both effects commute with $\Pi_{\mathrm{sym}}$, so the rejection operator is block diagonal; on the non-symmetric block the Jucys–Murphy content computation gives $\mathrm H_{\mathrm{asym}}\succeq (I-\Pi_{\mathrm{sym}})/(N-1)$. On the symmetric block one contracts the extremal eigenvector equation against $u^{\otimes N}$: the zeroth-order term is $\alpha\times$(tensor-power value), the first-order term vanishes by optimality, and the argmax bound (via a generating-function/Fourier extraction plus torus polarization) controls the rest — crucially all terms carry the same factor $\alpha$, which may be exponentially small but cancels. For the count test, Bernstein-polynomial derivative bounds $|Q^{(j)}|\le 2^{j-1}(t)_j$ supply the transverse expansion; for Bell, POVM normalization gives $\sum_a\|u_{j,a}^\perp\|\le\sqrt R$.

**Why it matters** It removes a plausible candidate route to separating $\mathsf{QMA}(2)$ from $\mathsf{QMA}$, isolating *non-identical, jointly measured* witnesses as the only remaining source of $\mathsf{QMA}(2)$'s conjectured extra power. For quantum chemistry/complexity, pure and mixed marginal problems — with very different feasible-set geometry — are now known to be equivalent in complexity.

**Caveats** The collapse does not touch $\mathsf{QMA}$ vs $\mathsf{QMA}(2)$. The exponential-check result excludes exponentially small margins or violated-check densities. The Bell result needs $R=2^{\ell_{\mathrm{out}}}$ polynomial; superlogarithmic output length would break $N=\Theta(m^2R)$. Witness blowup is polynomial but concrete constants (e.g. $N=256t^2/\delta$) are large.
