# SciRate Daily Digest — 2026-09-07

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Optimal inequalities for completely bounded polynomials and the limitations of quantum query algorithms

[arXiv:2609.05201](https://arxiv.org/abs/2609.05201) · [SciRate](https://scirate.com/arxiv/2609.05201)

*Francisco Escudero Gutiérrez, Miquel Saucedo, Carlos Palazuelos*

**TL;DR** The paper sharpens the completely bounded (cb) polynomial method into several *optimal* functional inequalities: a root-influence bound for block-multilinear polynomials with the best possible constant (1/t rather than 1/t²), and an essentially tight bound on the top-level Fourier growth of t-query quantum algorithms, √C(n−1,2t−1) ≈ (en/(2t−1))^{t−1/2}, matching 2t-fold forrelation up to an exponential-in-t factor. These yield a new junta-based simulation argument giving O(t²/(ε²δ)) *non-adaptive* classical queries for block-query quantum algorithms, versus O(t³/(ε⁴δ³)) adaptive queries before.

**The big picture** A long-standing question is whether quantum algorithms that make few queries to an unstructured input can always be mimicked classically with few queries, which would explain why huge quantum speedups seem to require promise structure. Prior work showed that quantum query algorithms are not merely bounded low-degree polynomials but obey a stronger matrix-valued boundedness condition, and this extra structure has been mined for progress on the Aaronson–Ambainis conjecture and on Fourier-growth bounds. Here the relevant inequalities are pushed to their exact optimal constants, and a new simulation strategy — inspired by the classical theorem that low-influence functions are close to juntas — converts them into faster classical simulations that need no adaptivity at all. The result is both a quantitative improvement and a conceptual one: the classical simulator can decide all its queries in advance.

**Key contributions**
- Optimal root-influence inequality ‖p‖_cb ≥ Σ_{s,i}√Inf_{x_s(i)}[p] / t for block-multilinear p of degree t; tight via x₁(1)···x_t(1).
- A cb-Bohnenblust–Hille inequality with constant exactly 1 for block-multilinear polynomials (previously √(t+1)), with a consequent PAC-learning improvement.
- A new simulation theorem: any p is ε-approximated on a (1−δ)-fraction by a junta on (Σ_i√Inf_i[p])²/(ε²δ) variables ⇒ non-adaptive deterministic simulation. Also gives exp(O(t)) *non-adaptive* queries for general bounded degree-t polynomials (previously adaptive).
- Tight top-level Fourier growth for t-query algorithms, plus level 2t−1, plus a bounded-adaptivity bound (2en/(2t−t_max))^{t−t_max/2} beating Girish–Sinha–Tal–Wu and quantifying how parallelism weakens algorithms.
- Amplitudes of fully non-adaptive t-query algorithms satisfy ‖â‖_{ℓ₁} ≤ 1 (vs. O_t(n^{(t−1)/2}) from the plain polynomial method), giving O(tr²ε⁻²log(1/δ)) non-adaptive randomized simulation for algorithms accepting on r outcomes.

**How it works** The root-influence bound comes from an explicit construction of contractive matrices X_s(i) and a unit vector such that products X_R(**i**_R)e form an orthonormal set, so the cb-norm supremum reproduces Σ_i‖v_i‖₂ = Σ_i√Inf. Fourier growth is proved by exhibiting matrices and vectors whose matrix elements equal sign(p̂(S))/√C(n−1,2t−1) exactly on the top-degree multi-indices and vanish elsewhere, turning the cb-norm ≤ 1 constraint directly into an ℓ₁ bound. The non-adaptive ℓ₁ bound uses the observation that such amplitudes are restrictions of *degree-1* forms, where cb-norm equals sup-norm.

**Why it matters** Relevant to anyone working on the Aaronson–Ambainis/simulation conjecture, Fourier growth separations (Raz–Tal-style oracle separations, bounded-adaptivity models), and to the operator-space community: the constants are now exactly right, so future progress must come from new inequalities, not better constants.

**Caveats** The Fourier-growth technique only reaches the top two levels (the construction provably fails at 2t−s, s≥2), leaving Girish's question open in general; the top-level bound is tight only up to roughly e^t. The √-influence route cannot resolve the simulation conjecture for all bounded polynomials, since the degree-t address function has Σ√Inf ≥ 2^{t−2}. The strongest simulation applies to block-query algorithms' amplitudes, not arbitrary t-query acceptance probabilities, and concurrent work handles constant-round adaptivity, which this paper's simulation does not.

## 2. Compiling the 2D Fermi-Hubbard ground-state energy estimation algorithm for active volume quantum architectures

[arXiv:2609.05316](https://arxiv.org/abs/2609.05316) · [SciRate](https://scirate.com/arxiv/2609.05316)

*Harriet Apel, Athena Caesura, Carys Harvey, Sam Heavey, Angus Kan, Jessica Lemieux, Ryan Levy, Sam Pallister et al.*

**TL;DR** The authors recompile the 2D Fermi–Hubbard ground-state energy estimation algorithm (QPE + second-order Trotter) with *active volume* — a spacetime cost metric for fault-tolerant architectures with limited non-local connectivity — as the optimization target, obtaining up to a 3.9× active-volume reduction over the T-count-optimized state of the art for lattices up to 20×20. As a byproduct they set the lowest reported Toffoli counts for this benchmark (1.96× below Kan et al., 3.37× below Campbell at L=20), and, combined with a block scheduler, a 73× runtime improvement at L=8 under matched logical-qubit budgets.

**The big picture** Most fault-tolerant algorithm design minimizes the count of expensive non-Clifford gates, treating everything else as free. But on architectures that allow some long-range logical connectivity — photonic, neutral-atom, or superconducting with long couplers — idle qubits and routing are cheap while Clifford operations are not negligible, so that proxy misleads. This work is the first to compile a lattice-model simulation algorithm directly against the architecture-relevant spacetime cost, showing that the compilation choices change and that costs drop substantially even in the conventional metric. It argues concretely that early fault-tolerant resource estimates should be architecture-aware rather than gate-count-driven.

**Key contributions**
- First active-volume compilation and resource estimate of a lattice-Hamiltonian FTQC algorithm; quantifies that conventional circuit volume overestimates cost by 12.1× at L=20 before any compilation change.
- Swap from adaptive "entanglement-free" iterative QPE to sine-windowed QPE with directional control: ~3× fewer queries at comparable precision (32 vs 96 at phase error 0.05).
- New Trotter term ordering ("PIG": pink-plaquette / interaction / gold-plaquette) chosen by query-merging economics rather than commutator convenience, letting the most expensive gold-plaquette evolution occupy the least-queried slot.
- Explicit, cheap controlled and *directionally* controlled Hamming-weight-phasing circuits (including phase fix-ups and catalyst reuse, 2⌊log₂L²⌋+3 catalyst rotations), plus ZX-diagram-optimized gate-level primitives and a cheaper fermionic SWAP network.
- Full accounting of the QPE control structure (usually omitted), re-optimized error budget, and runtime/space-time scans using an active-volume scheduler.

**How it works** Total active volume is summed from per-operation logical-block counts (Toffoli 47, CNOT 4). Optimizations are attributed by subroutine: the fSWAP network dominated the baseline and yields the largest gain; the optimized circuit is much more balanced, with Clifford and non-Clifford volume approaching 1:1 at L=20 and total volume roughly flat at ~4×10⁷ blocks across L=4–20 (recovering the size-independence Campbell predicted, which the baseline lost to Clifford overhead). Batching HWP into four batches cuts logical qubits ~25% at only ~3% volume cost; a workspace scan at L=20 trades an order of magnitude in qubits for an order of magnitude in runtime until the reaction limit.

**Why it matters** Useful both as a concrete resource-estimate improvement for a canonical materials-science benchmark and as a methodological argument for co-design; the appendix worked example is pitched as a tutorial for active-volume estimation.

**Caveats** Initial-state preparation, window-state prep, and the inverse QFT are excluded — state preparation at L=20 is an open and potentially dominant cost. Query counts are restricted to 2^{k-1}, which the authors note is conservative. Runtimes assume an illustrative photonic hardware model, so only trends are meaningful. Conclusions can invert on locality-dominated architectures (e.g. HWP versus direct rotation synthesis).

## 3. The marginal is pretty good

[arXiv:2609.05225](https://arxiv.org/abs/2609.05225) · [SciRate](https://scirate.com/arxiv/2609.05225)

*Lukas Schmitt, Joseph M. Renes*

**TL;DR** For Petz–Rényi divergences of order α ∈ [1/2,1), replacing the optimal second-argument state σ_B in min_σ D_α(ρ_AB‖τ_A⊗σ_B) by the canonical marginal ρ_B costs at most a multiplicative factor 1/α (≤ 2), independent of dimension and vanishing as α→1. An analogous statement is proved for fidelity (F(ρ_AB,τ_A⊗ρ_B) ≥ max_σ F(ρ_AB,τ_A⊗σ_B)²) and for the sandwiched divergence restricted to α=1/2, pure states, and quantum–classical states; the general sandwiched case is conjectured, with a weaker 1/α² bound proved.

**The big picture** Many one-shot and Rényi-type conditional entropies are defined through an optimization over an auxiliary state, and the optimizer typically depends on the input in an opaque, nonlinear way, which complicates both computation and proofs. This note shows that one can simply plug in the obvious, explicit choice — the reduced state of the system in question — and lose only a small, dimension-independent multiplicative factor that shrinks to nothing as the order approaches one. That turns an awkward variational quantity into a closed-form one at negligible cost, which is useful whenever such measures appear inside larger arguments, e.g. in cryptography or channel-coding bounds.

**Key contributions**
- Main theorem: for α ∈ [1/2,1) and any bipartite ρ_AB, τ_A, the marginal is within factor 1/α of the optimum for the Petz–Rényi divergence; extended to non-full-rank τ_A by continuity.
- A tightness example: a classical distribution family (a point mass p at (0,0) plus a uniform background on n²−1 cells) for which the gap between the two sides vanishes as n→∞, showing the 1/α factor cannot be improved.
- Fidelity result: a "square" bound obtained via an operator Cauchy–Schwarz lemma, equivalent to the α=1/2 sandwiched statement for arbitrary states.
- Sandwiched-divergence bound for pure and QC states; a corollary 1/α² bound in general via Araki–Lieb–Thirring, plus an explicit conjecture.

**How it works** Two ingredients. (i) A Hölder-type variational identity: max_σ tr[W_B σ_B^{1−α}] = (tr W_B^{1/α})^α with optimizer σ* ∝ W_B^{1/α}, where W_α = tr_A[(τ_A^{(1−α)/2}⊗I)ρ_AB^α(τ_A^{(1−α)/2}⊗I)]. (ii) An operator inequality W_α ≤ ρ_B^α, derived by testing the data-processing inequality for the Petz divergence under partial trace against all full-rank ω_B. Since (1−α)/α ∈ [0,1] exactly when α ≥ 1/2, x ↦ x^{(1−α)/α} is operator monotone, giving W_α^{1/α} ≤ W_α ρ_B^{1−α} in trace, which is precisely the claimed factor-1/α statement after taking logs. The fidelity proof uses X_U = tr_A[(√τ_A⊗I)√ρ_AB U], shows X_U X_U* ≤ ρ_B via an operator Cauchy–Schwarz bound, and sandwiches max_σ F² ≤ max_U ‖X_U‖₂² ≤ F(ρ_AB,τ_A⊗ρ_B) using a polar-decomposition choice of unitary.

**Why it matters** Useful as a plug-in simplification for Rényi conditional entropies, one-shot decoupling/randomness-extraction bounds, and any argument where explicit optimizers are unavailable; the multiplicative rather than additive nature of the loss keeps it harmless in the α→1 regime typically used for asymptotic equipartition arguments.

**Caveats** Restricted to α ≥ 1/2 (operator monotonicity is essential); the loss is multiplicative in the divergence, so it can be large in absolute terms when the divergence itself is large, and it does not shrink with dimension. The sandwiched case remains open for general states, with only the 1/α² bound available. Finite dimensions throughout; the "small factor" is up to 2 at α=1/2.

## 4. Learning unknown stabilizer codes using product measurements

[arXiv:2609.04997](https://arxiv.org/abs/2609.04997) · [SciRate](https://scirate.com/arxiv/2609.04997)

*Heather Leitch, Sowmya Tirukkovalluri, Yingkai Ouyang*

**TL;DR** The paper gives a simple randomized protocol that learns the stabilizer generators of an *unknown* stabilizer code from copies of codeword states, using only single-qubit X/Y/Z measurements: sample random product bases, then declare any low-weight subset whose outcome parity is strongly biased (|p[0]−p[1]| > r/4) to be a stabilizer element. Chernoff-bound analysis gives accept/reject guarantees under depolarizing noise, and for weight-w qLDPC codes r = Θ(w log n) repetitions per pattern suffice for failure probability ≤ n^(−2w), with an explicit noise tolerance (p < 0.045 for weight-6 bivariate-bicycle codes).

**The big picture** Existing verification protocols for error-correcting codes assume you already know which code the device is supposed to implement, and check closeness to that target. Here the converse problem is addressed: given only states drawn from an unknown protected subspace, reconstruct the checks that define it, using nothing more than independent single-qubit measurements — the easiest operations available on hardware. Because practical low-density codes have sparse, bounded-weight checks, the search can be restricted to small qubit clusters, making the task tractable. This is a plausible route to certifying that a fabricated device really implements the code its designers intended.

**Key contributions**
- A two-stage product-measurement algorithm (random basis patterns → subset-parity hypothesis testing) that outputs stabilizer generators with no prior knowledge of code structure.
- A copy-count bound N ≥ 2A ln g, with A = Σ_{k≤w} C(n,k)3^k the number of Paulis of weight ≤ w, for success probability 1 − 1/g.
- Noise analysis: parity-error probability q = (1−(1−2p)^w)/2 for weight-w products; explicit Chernoff bounds Pr(accept|Q∈G) ≥ 1−2c_q^{5r/8} and Pr(reject|Q∉G) ≥ 1−2(64/27e)^{r/8}; the false-accept term dominates only once q < 0.217.
- Overall failure bound Pr(fail) ≤ 4A²ln(n)(64/27e)^{r/8}, giving r ≥ 76(2w ln(3n²) + ln(4w²) + ln ln n).
- Explicit positioning against known-target verification protocols (Dangniam et al., Takeuchi–Morimae, SVAFE).

**How it works** Each of m random n-trit strings fixes a product basis; r copies are measured per pattern. For every support s of size ≤ w, the induced Pauli ⊗_{i∈s}B_i has expectation ±1 if it lies in the state's stabilizer group and 0 otherwise, so the empirical parity imbalance separates the two cases; the r/4 threshold is analyzed via a multiplicative Chernoff bound. Enumeration costs O(n^w), constant-exponent for qLDPC, with O(n) memory.

**Why it matters** Relevant to anyone benchmarking qLDPC/BB-code hardware: it shows subspace-level certification is possible with product measurements and logarithmically many repetitions, without joint or Bell measurements or a known target.

**Caveats** The stated bound N ≥ 2A ln g is polynomial (≈n^w log n), not polylogarithmic as the abstract claims; the polylog statement appears to conflate N with r, and the "probability 1/A per query" step looks overly pessimistic (matching a fixed weight-w Pauli on its support has probability 3^{−w}, independent of n). Theorem 1's success probability is written as "at least 1/g" where the derivation gives failure ≤ 1/g. The union bound is written as an equality and treats generator-discovery events as independent. The number of patterns m is never bounded, and N is used ambiguously for both distinct codewords and copies of a single state. Crucially, measurements on one codeword reveal that state's full n-generator stabilizer group, including logical-dependent elements (as the [[4,2,2]] example notes, 16 candidates); no procedure or sample bound is given for intersecting across codewords to isolate the g code checks. The weight bound w must be known in advance, noise is idealized as pre-measurement depolarizing only, and there are no numerical simulations.

## 5. Fundamental Limits of Quantum Metrology Beyond Fixed Causal Order

[arXiv:2609.05355](https://arxiv.org/abs/2609.05355) · [SciRate](https://scirate.com/arxiv/2609.05355)

*Wenjie Wei, Yutong Li, Shengshi Pang*

**TL;DR** The authors prove that general indefinite-causal-order (ICO) process matrices give no asymptotic metrological advantage over simple parallel strategies for estimating a single parameter in $N$ uses of a finite-dimensional channel. They derive three nested QFI upper bounds — a universal Heisenberg envelope $4N^2\min_{\{K_i\}}\|\alpha\|$, a structurally refined bound that keeps SQL-limited channels at SQL, and an asymptotically tight bound $4\min_{\{K_i\}}[N\|\beta\|+\sqrt{N\|\alpha-\beta\beta^\dagger\|}]^2$ — the last of which pins the leading QFI coefficient to exactly the optimal parallel value in both SQL and Heisenberg regimes.

**The big picture** Quantum sensing precision usually improves faster than classical statistics allows when probes are entangled, but noise often destroys that speedup. A tantalizing hope has been that processes without a definite temporal order of operations — where a control system puts the sequence of channel uses into superposition — could restore or even exceed the best known scaling. This work closes that hope at the level of leading-order asymptotics: the most general causally indefinite protocols are exactly as good as the simplest parallel entangled-probe protocols in the many-query limit, so any genuine benefit from indefinite causality in this setting must live at small query numbers or in subleading corrections.

**Key contributions**
- Extension of "no ICO advantage for unitary channels" from the causal-superposition and QC-QC subclasses to the full process-matrix class, with two independent proofs (iterative Cauchy–Schwarz; KKT with an explicit recursive dual construction).
- Proof that Theorem 1 and the unitary corollary are logically equivalent via Stinespring dilation (with an explicit construction of a dilation whose generator satisfies $\|H_g\|^2=\|\alpha\|$).
- Structurally refined bound showing the $O(N^2)$ sector always carries a factor $\|\beta\|$, hence the Hamiltonian-in-Kraus-span condition forces $\lim F^{\mathsf{Gen}}_N/N = 4\min_{\beta=0}\|\alpha\|$.
- The asymptotically tight bound fixing $\lim F^{\mathsf{Gen}}_N/N^2 = 4\min\|\beta\|^2 = \lim F^{\mathsf{Para}}_N/N^2$.
- A QC-QC finite-query iterative bound matching the CS one; plus a side result that $\mathrm{im}\,\mathcal{Q}_{\mathsf{Gen}}$ has dimension $(d^4-d^2+1)^N-1$ out of $d^{4N}$, with a Sierpiński self-similar structure — i.e. almost all operator components are ICO-allowed for large $N$, opposite to quantum combs.

**How it works** The $N$-channel performance operator is decomposed under a non-optimal but admissible gauge $h^{(N)}=h^{(N-1)}\otimes\mathbb{I}+\mathbb{I}\otimes h^{(1)}$ into accumulation, local, and interference pieces; the interference piece is bounded by an operator Cauchy–Schwarz inequality, yielding $\sqrt{F_N}\le\sqrt{F_{N-1}}+\sqrt{F_1}$. The sharper bounds exploit a structural fact: any operator with vanishing partial trace on the channel output space has zero overlap, in tensor pairs, with any valid two-party process matrix. Writing $\dot V = V\beta^\dagger + R$ with $R^\dagger V=0$ isolates the coherently accumulating part ($N\|\beta\|$) from an incoherent residual ($\sqrt{N\|\alpha-\beta\beta^\dagger\|}$).

**Why it matters** This settles a much-debated question for local frequentist single-parameter channel estimation and redirects the search for ICO advantages toward finite-$N$, Bayesian, multiparameter, or non-Markovian settings. Relevant to anyone working on higher-order quantum maps, metrology bounds, or ICO resource theory.

**Caveats** Restricted to single-parameter, local-frequentist, finite-dimensional, i.i.d. channel uses — notably excluding the continuous-variable super-Heisenberg switch result. Attainability comes from prior parallel-strategy results, so "tightness" is asymptotic only; finite-$N$ ICO advantages are explicitly not excluded (numerics show general ICO exceeding the CS/QC-QC bound at $N=3,4$). The KKT optimality argument assumes a non-degenerate generator, and subleading-order behavior remains open.
