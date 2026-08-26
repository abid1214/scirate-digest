# SciRate Daily Digest — 2026-08-26

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Dynamical Consequences of Nontrivial Topology of Molecular Conical Intersections

[arXiv:2608.24864](https://arxiv.org/abs/2608.24864) · [SciRate](https://scirate.com/arxiv/2608.24864)

*Indranil Ghosh, Kush Banker, Gregory S. Engel*

**TL;DR** — Starting from the linear $E\otimes\epsilon$ Jahn–Teller conical intersection, the authors construct two gapped two-level Hamiltonians with *identical* adiabatic potential energy surfaces but different electronic-eigenvector topology: one obtained by adding a $\lambda\sigma_y$ (imaginary/spin–orbit-like) term, which retains a smeared Berry-curvature distribution and a half-integer invariant $\mathcal{C}=\tfrac12\,\mathrm{sgn}(\lambda)$, and one engineered with $d_y\equiv 0$, which has zero Berry curvature everywhere. Fewest-switches surface hopping (1000 trajectories, $M=2000$ a.u., $F=1.8$, $\lambda=0.1$) gives relaxation rates that agree along one approach direction but differ by ~6× (diagonal) and ~30× (along $\hat Q_y$: $6.0\times10^{-3}$ vs $1.9\times10^{-4}$ a.u.$^{-1}$), traced to a symmetry-enforced vanishing of the nonadiabatic coupling component in the trivial case.

**The big picture** — Where two electronic states of a molecule meet, the electronic wavefunction acquires a sign change on encircling the meeting point, a hallmark of nontrivial topology that is known to shape photochemical outcomes. This work shows that even when the degeneracy is lifted and the surfaces are pushed apart, the topological character can either survive or be destroyed depending on the nature of the coupling that opens the gap — and that two systems with literally the same energy landscape can relax at rates differing by more than an order of magnitude. Since the couplings that preserve topology are exactly those that appear physically as spin–orbit, derivative, and chiral interactions, this suggests a genuinely topological handle on nonradiative relaxation rates.

**Key contributions**
- Explicit pair of gapped Hamiltonians with identical spectra ($\varepsilon_\pm=\pm\sqrt{F^2\rho^2+\lambda^2}$) but Berry phases $\pi(1-\lambda/\sqrt{F^2\rho^2+\lambda^2})$ versus 0 — demonstrating that PES do not determine geometric phase.
- Promotion of the known $h/2$ result of Requist–Gross into a labeling invariant $\mathcal{C}=\frac{1}{2\pi}\iint_{\mathbb{R}^2}\Omega_-$ over the noncompact branching space, half-integer by analogy with the parity anomaly / single Haldane Dirac point.
- FSSH demonstration that topology, not energetics, controls direction-dependent hopping kinetics, with a Hellmann–Feynman analysis showing $f_{-+}^{(Q_y)}=0$ identically for the trivial model along $\hat Q_y$.

**How it works** — Two-band $d$-vector formalism: $\mathbf{d}_{top}=(FQ_y,\lambda,FQ_x)$ covers one hemisphere of the Bloch sphere, yielding a Lorentzian Berry curvature of half-width $|\lambda|/F$ (the smeared monopole $\pi\delta^{(2)}$ of the bare CI); $\mathbf{d}_{triv}=(\sqrt{F^2Q_y^2+\lambda^2},0,FQ_x)$ stays on a great circle, giving $\Omega\equiv0$. Dynamics use Jain–Sindhu FSSH with a Cayley electronic propagator ($\Delta t_q=0.05$ a.u.), velocity Verlet nuclei in an added rotationally invariant harmonic trap, Wigner-sampled initial conditions with $P_0=10$ a.u., and trajectory-level bootstrap (500 resamples) for rate errors.

**Why it matters** — Provides a clean, controlled counterexample to the intuition that adiabatic surfaces determine nonadiabatic dynamics, and connects molecular photophysics to Chern-number language. Relevant to anyone modeling spin–orbit-mediated intersystem crossing, CISS-adjacent chiral photochemistry, or benchmarking surface hopping.

**Caveats** — The logic "$\mathcal{C}=0\Rightarrow\Omega=0$ pointwise" holds only within this engineered two-parameter family; generically a vanishing integral does not force vanishing curvature, so the observed effect is arguably a *local* NAC-symmetry consequence of $d_y\equiv0$ rather than of the global invariant. $\mathcal{C}$ is half-integer only for the exactly linear model — it is not quantized for generic $\mathbf{d}(\mathbf{Q})$. $H_{triv}$ is constructed by hand and not obviously realizable. Standard FSSH contains no Berry force, so only $\mathcal{O}(\hbar)$ effects are captured (the authors acknowledge this); interference/tunneling in the low-momentum regime is untested. Figures are absent from the provided source.

## 2. Certified Randomness without Structure Against Shallow-Query Adversaries

[arXiv:2608.24832](https://arxiv.org/abs/2608.24832) · [SciRate](https://scirate.com/arxiv/2608.24832)

*Dakshita Khurana, Bhaskar Roberts, Avishay Tal*

**TL;DR** The Yamakawa–Zhandry (YZ) proof of quantumness is turned into a *provably* certified-randomness protocol against quantum adversaries limited to $o(\log\lambda)$ layers of adaptive (arbitrarily wide, polynomial) oracle queries — no Aaronson–Ambainis conjecture needed. Such adversaries cannot output a valid codeword with min-entropy below $o(\lambda^{c/2})$, where $c$ is the list-recoverability parameter of the underlying code.

**The big picture** Certified randomness lets a classical client verify that a remote quantum device's outputs were genuinely unpredictable, and the leading random-oracle-based candidate protocol has resisted proof for years: its security rested on a broad unproven conjecture about how much quantum algorithms can be influenced by a few input bits. This work removes that dependence for adversaries that interact with the hash function in only a few adaptive rounds — precisely the regime the honest protocol itself lives in, since the honest algorithm needs just one round of parallel queries. The argument replaces the conjectural route with a hands-on combinatorial one: a cheater must "check" its intended answer by concentrating query effort on it, and with few adaptive rounds it must place those bets before it knows anything useful. This is the first unconditional evidence for the conjecture at the heart of the protocol.

**Key contributions**
- Unconditional $(D,k)$-certifiable min-entropy for the YZ protocol for any depth $D=o(\log\lambda)$ and $k=o(\lambda^{c/2})$, replacing the AA-conjecture-based proof.
- A "heavy query lemma": any adversary outputting a correct codeword $\mathbf{x}$ with conditional probability $\ge p$ must put cumulative query weight $\ge p^2/16Qn$ on all but $s$ symbols of $\mathbf{x}$, except with probability $2^{-(s-1)}$.
- A threshold-bootstrapping technique that extends the (easy) single-parallel-query argument to constant/slowly-growing depth, handling oracle-dependent query weights.

**How it works** Both lemmas are reprogram-and-count arguments. Given a good pair (oracle $h$, answer $\mathbf{x}$), flip $h$ from 0 to 1 on nonempty subsets of $s+1$ low-weight symbols of $\mathbf{x}$, producing $\ge 2^s$ "bad" oracles where $\mathbf{x}$ is wrong; the swapping lemma bounds the state perturbation by $2\sqrt{D\sum w}$, so the adversary still outputs (or still heavily queries) $\mathbf{x}$. Disjointness/pigeonholing of the bad sets then bounds the good-set measure. For depth $>1$ one picks the *critical layer* $q^\*$ — the first at which $(1-\zeta)n$ symbols cross threshold $t_q=(2Qn/\ell)^{4^{-q}}$ — and reprograms the $\zeta n$ still-light positions; the recurrence $t_q\ge Q/\ell+2Q\sqrt{Dn\,t_{q-1}}$ ensures heavy symbols retain weight $\ge Q/\ell$. List recoverability caps at $L=2^{\tilde O(\lambda^{c'})}$ the codewords any oracle can heavily query, versus $2^{\Omega(\lambda)}$ bad oracles per good one.

**Why it matters** Relevant to anyone building or analyzing QROM-based proofs of quantumness and randomness expansion; it also gives the first non-trivial unconditional progress on the YZ entropy conjecture.

**Caveats** The doubly-exponential threshold sequence is exactly what caps depth at $o(\log\lambda)$; even $\Theta(\log\lambda)$ is out of reach. Certified entropy $o(\lambda^{c/2})$ is far below the honest algorithm's $\Theta(\lambda)$-ish entropy, and $c<c'<1$ is code-dependent. Security is in the QROM with a monolithic random oracle (no instantiation), min-entropy is measured conditioned on acceptance for a single run, and no accounting of seed randomness / multi-round expansion is given.

## 3. Masked Differential-linear Distinguishers and Quantum Approaches

[arXiv:2608.24799](https://arxiv.org/abs/2608.24799) · [SciRate](https://scirate.com/arxiv/2608.24799)

*Shobhit Pandey, Sarbani Sen, Debajyoti Bera, Ravi Anand*

**TL;DR** The paper defines *masked auto-correlation* (MAC) — the correlation between two differently masked outputs of a permutation evaluated at inputs separated by a fixed difference — which subsumes linear, differential-linear, and DLCT cryptanalysis as special cases. It then shows that the task of *finding* mask pairs with large MAC ("MAC Fishing") admits a constant-query quantum sampler drawing pairs proportional to squared correlation, while any classical randomized algorithm needs Ω(N/log N) queries (N = 2ⁿ), via an adaptation of Aaronson–Chen's Fourier Fishing hardness. Capacity-based distinguishers and last-round key recovery are built on top, with amplitude-estimation giving a quadratic speedup in the verification step, validated on 16-bit mini-AES and a toy Simon.

**The big picture** Classical block-cipher cryptanalysis has always separated two tasks: verifying that a given statistical approximation is good, and searching the astronomically large space of possible approximations to find good ones in the first place. This work formalizes a general family of approximations that unifies several known attack styles, and then proves that the *search* step is where quantum computers help most: a quantum algorithm samples good approximations essentially for free, while any classical method must effectively read almost the entire cipher. That makes the search step, rather than the usual data-collection step, the natural target for quantum cryptanalysis.

**Key contributions**
- The MAC primitive and associated masked differential-linear (MDL) approximations; ordinary linear cryptanalysis, DL cryptanalysis, and the DLCT recovered as special cases.
- A constant-quantum-query sampler (MACSample) returning (α,β) with probability ∝ cor², paired with a classical Ω(N/log N) lower bound — claimed as the first upper/lower bound pairing for the approximation-*finding* task.
- Distributional analysis for random permutations: the normalized Walsh statistic is N(0,1) for α≠β and N(0,2) for α=β; expected fishing advantage = Succ_Q(τ) + Δ(τ)/N with Chebyshev concentration (failure ≤ 48.5n²/N).
- Capacity-based distinguisher plus a two-stage key recovery: an unsigned energy filter followed by signed cosine-similarity template matching to break the sign-degenerate equivalence class.

**How it works** The lower bound splits the correlation into seen/unseen query contributions; with t = o(N/log N) queries the seen part contributes only o(1) after the √(t/N) scaling, so the algorithm cannot beat the random-guess success rate Succ_R. Attacks: QuantumVerify phase-encodes α·B(x)⊕β·B(x⊕w) so the overlap with |+ⁿ⟩ equals the correlation exactly, read off by a Hadamard test with amplitude estimation at O(1/√τ) vs O(1/τ) classically. Key recovery costs O((2^κ + 1/adv)·m/√τ) quantum queries; the distinguisher needs Ω(√(2^t)/Cap) pairs and O(2^t) memory. On mini-AES with a 16-dimensional approximation and w=0x0003, capacity ≈ 1.7 vs ≈ 1 for a random 16-bit permutation.

**Why it matters** It reframes quantum symmetric cryptanalysis away from Grover/Simon-style speedups toward provable query separations for approximation discovery, and gives a single algebraic object covering several attack families. Relevant to symmetric-key cryptanalysts and quantum query-complexity researchers.

**Caveats** Everything quantum requires the strong Q2 (superposition oracle) model. The Ω(N/log N) bound is only ~N queries — classical FFT-based linear cryptanalysis already costs about that — and is proved in the dense regime Nτ=Θ(1), whereas the distinguishers run at τ=ω(log N/N); the authors explicitly flag this gap. The signed reference template v\* is obtained from the reduced-round cipher, i.e. a known-key setting; fully online sign recovery is left open. The random-permutation capacity baseline is a conjecture; complexity bounds are expected costs with no variance/false-positive analysis; the Grover-accelerated key search needs coherent nested amplitude estimation, deferred to future work. Experiments are toy-scale (16-bit).

## 4. Graphix: A software framework for Measurement-Based Quantum Computation

[arXiv:2608.24781](https://arxiv.org/abs/2608.24781) · [SciRate](https://scirate.com/arxiv/2608.24781)

*Mateo Uldemolins, Pranav Nair, Emlyn Graham, Shinichi Sunami, Thierry Martinez, Maxime Garnier*

**TL;DR** Graphix is a Python framework that treats measurement-based quantum computation as a first-class object rather than emulating it in the circuit model: labelled open graphs, xz-correction strategies, measurement-calculus patterns, and the full flow hierarchy (causal, generalised, Pauli) are all native types with mutual conversions. It bundles state-of-the-art flow-finding, pattern-optimisation and simulation machinery (statevector, density-matrix, Stim, Qiskit/Perceval plugins) behind a modular backend/branch-selector/noise-model architecture, plus a proof of max-space optimality for causal-flow patterns.

**The big picture** Measurement-based quantum computing replaces gates with a large entangled resource state that is consumed by adaptive single-qubit measurements, and it is the natural language for photonic hardware, fusion-based error correction, and blind delegated computation. Until now researchers have mostly re-implemented its abstractions from scratch or bolted them onto circuit toolkits, which makes results hard to reproduce, compare, or compose. This work presents a maintained, extensible software foundation whose data structures mirror the theory one-to-one, so that new compilation, determinism-analysis, or simulation techniques can be added and benchmarked in a shared representation. The payoff is the same one circuit-model software delivered a decade ago: cumulative, reusable infrastructure rather than isolated prototypes.

**Key contributions**
- Unified type hierarchy — `OpenGraph`, `XZCorrections`, `Pattern`, `StandardizedPattern`, and `CausalFlow`/`GFlow`/`PauliFlow` — with automatic conversions in both directions (flow → corrections → pattern; pattern → open graph).
- Implementation of the best-known flow-finding complexities: O(|V|²) causal, O(|V|³) algebraic gflow and Pauli flow; flows carry a `check_well_formed` method that reports which defining proposition is violated (pedagogy and debugging).
- Extraction of a flow from an arbitrary runnable xz-correction strategy (appendix), and a proof that a specific command ordering is max-space optimal for causal-flow patterns.
- Formalised and implemented "Pauli pushing" (moving all Pauli measurements before planar ones, tracking outcome flips through σ(λ, D_X, D_Z) with symmetric differences), Pauli-measurement removal via graph complementation, and space-minimising command reordering.
- MBQC+LC extension: unconditional single-qubit Clifford commands (24 elements, stored as H/S/Z products) with commutation rules and `output_cliffords` on open graphs, chosen so flow analysis is unaffected.
- Noise as a pattern-to-pattern transduction via a signal-conditioned CPTP command, making noise models backend-agnostic (including Stim for Pauli-only patterns).
- Circuit interoperability: transpiler, QASM 3.0 export with classical feed-forward, and Simmons-style ancilla-free unitary extraction.

**How it works** The simulator is two-tier: a top layer walks the command list, computes outcome probabilities and handles feed-forward; a backend layer applies the semantics to a state representation with a *dynamically sized* register (grows on N, shrinks on destructive M) — the key structural difference from circuit simulators. Branch selectors are orthogonal: `Random`, `Fixed`, `Const`; for strongly deterministic patterns all branches are equiprobable up to phase, so uniform sampling skips the expensive expectation-value computation.

**Why it matters** Relevant to anyone doing MBQC compilation, blind/verified delegated computation (Veriphix builds on the custom preparation/measurement hooks), photonic and fusion-based architectures, and ZX-calculus-based circuit optimisation, where open graphs and flow are the interchange format.

**Caveats** Shadow Pauli flow — the complete characterisation of robust determinism at the pattern level — is not implemented. The tensor-network backend has "limited functionality." Qudit and continuous-variable measurement-based models are discussed in the introduction but not supported. Claims of reproducing and extending prior results appear in a section not fully present in the supplied source, so I could not verify their scale or runtime benchmarks.

## 5. Geometry-controlled correlated electric-field noise in enclosed ion traps from billiard return spectra

[arXiv:2608.24770](https://arxiv.org/abs/2608.24770) · [SciRate](https://scirate.com/arxiv/2608.24770)

*Ayush Nadiger*

**TL;DR** This paper recasts surface-induced electric-field noise in ion traps as a billiard "return-depth" problem: for a grounded cover above a noisy plane, the image series is exactly the unfolding of a parallel-wall billiard, and the noise spectrum becomes a pair-sum over unfolded depths. This yields exact enclosure gain factors (ζ(3) for normal fields, η(3) for tangential at cover height twice the ion height), an operator-level theorem that a passive cover raises the *entire* normal-field covariance matrix and lowers the entire tangential one in Loewner order, and — beyond flat walls — a numerically validated claim that specular ray saddles of a screened boundary operator control the electrostatic response of curved covers (correlation 0.9991 across 16 shapes).

**The big picture** Anomalous heating of trapped ions from nearby surfaces is usually reported as a single number per ion, but what actually limits multi-ion gates is the full spatial pattern of correlated field noise across the whole chain. This work holds the microscopic surface physics fixed and asks what purely passive metal geometry does to that pattern, showing that geometry acts as a mode-selective filter with a clean ray-optics interpretation: reflected paths reinforce noise along one field direction and cancel it along the other. The payoff is that enclosure shape becomes both a diagnostic knob for identifying the noise source and a design knob for reshaping the collective bosonic environment seen by an ion register.

**Key contributions**
- Exact return-pair functional: noise = sum over pairs of unfolded normal depths of a Laplace-type transform of the arbitrary stationary surface spectrum; separates source physics from geometry.
- Exact special-function enclosure ratios at h=2d (ζ(D+1) normal, η(D+1) tangential; normal/tangential anisotropy 8/3 vs. open-space 2).
- Loewner-ordering theorem for the N-ion cross-spectral matrix, holding for any unchanged nonnegative source spectrum and separately for the signed-frequency (up/down) quantum rate blocks.
- Collective noise eigenchannels + participation rank; ten-ion example: rank 5.61→5.11, leading channel 23.7%→28.6% at h=2d (3.48→3.03 with correlation length ξ=d).
- Sharp asymptotics: transfer ratio = 1 + c(h/d)(qd)^{-5/2}, with c(2)=9.335 and c ~ ε^{-5/2} as h→d.
- Screened-BEM tests: exponent tracks Euclidean specular excess length (2.5658 measured vs. 2.5184 predicted, vs. 1.7115 for a vertical-depth surrogate); shape derivative matches −2q_z to 1.5%; focusing prefactor correlation 0.9997; two-saddle interference 0.987.

**How it works** Boundary-potential covariance plus the Dirichlet Green function gives an N-ion field cross-spectral matrix; its diagonal is the usual heating rate, its projections give mode heating, and within a degenerate secular block its diagonalization gives Lindblad jump operators. In the slab, the momentum-space kernel k cosh[(h−d)k]/sinh(hk) is a geometric series over depths |d−2nh|; tangential fields carry alternating sign, which is exactly why the two orderings are opposite. Curved covers are handled by Fourier transforming an invariant direction into a modified-Helmholtz problem solved by constant-panel BEM, where Laplace's method on the first-reflection integral picks out specular points.

**Why it matters** Trap designers get quantitative, convention-independent predictions (normal heating +20.2%, tangential −9.85% at h=2d) that are directly testable with a cover-in/cover-out interleaved experiment, plus a bridge from the covariance to gate infidelity (Δ(1−F) = 0.400 ṅ t_g for a primitive MS gate; bus-exposure ratios 1.237/1.044 normal, 0.878/0.967 tangential).

**Caveats** No experimental data. The ordering theorem assumes an infinite slab and, critically, that the cover does not perturb adsorbate/patch statistics — and the cover must be quiet (χ < 0.109 for tangential suppression to survive). Curved-cover results are 2D cross-sectional Fourier slices, not full trap simulations. The MS coefficient and the ten-ion mechanical model are illustrative; the ray-reconstruction appendix is explicitly not independent validation. Statistical estimate: ~19 repeats per geometry for 3σ on the tangential effect, likely systematics-limited.
