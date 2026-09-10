# SciRate Daily Digest — 2026-09-10

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Loss-correcting fault-tolerant quantum computing architecture for neutral atoms

[arXiv:2609.10079](https://arxiv.org/abs/2609.10079) · [SciRate](https://scirate.com/arxiv/2609.10079)

*Sanaa Sharma, Yutaka Hirano, Akihisa Goban, Hayata Yamasaki, Shinichi Sunami, Prakash Murali*

**TL;DR** The authors build the first end-to-end framework that treats atom loss as a program-wide budget in neutral-atom fault-tolerant computing, coupling a zone-free "compute-zone" layout and loss-aware compiler (AOD-configuration-aware routing, transfer-deferred scheduling) to SWAP-based syndrome extraction with a delayed-erasure decoder. Against a zoned baseline (ZAC), they cut accumulated loss per syndrome-extraction round by 1.25× on average (2.15× max), CX routing time by 2.9× on average (8.4× on 32-qubit Ising), and logical error rates by up to 212× on 100-qubit lattice circuits. They also give the first evaluation of fold-transversal surface-code magic-state cultivation under realistic loss, finding erasure-aware decoding recovers nearly loss-free overhead (total ~1.53 attempts for a 10⁻⁷ magic state).

**The big picture** Neutral-atom quantum computers lose atoms outright — during gates, imaging, and especially when atoms are handed between static and moving traps or shuttled long distances. Standard error-correction analyses assume random bit- and phase-flips and simply cannot handle a qubit that vanishes, so published resource estimates for this platform may be optimistic, and compilers that only optimize gate fidelity can inadvertently make loss worse. This work makes loss a first-class design target across layout, compilation, and decoding simultaneously, showing that keeping atoms in the mobile traps and doing all entangling operations locally, rather than ferrying them to a dedicated interaction region, substantially improves achievable logical error rates and lowers the code size needed. It also converts the analysis into concrete hardware requirements, notably that atom-refill throughput must improve by orders of magnitude.

**Key contributions**
- Loss-aware layout using spatially selective (focused-beam) Rydberg gates: no separate storage/entangling zones, no repeated SLM–AOD handoffs (~4 pickups per transversal gate → ≤2).
- Transfer-deferred compilation: Hungarian-algorithm AOD-to-operation assignment that keeps atoms resident in AOD traps across consecutive layers; only inactive qubits are dropped to SLM.
- AOD routing under real hardware limits: per-axis RF tone budget (B≈60 MHz, Δf≈0.6 MHz → ≲100 tones/axis), rigid common-displacement constraint; simulated annealing over L/Z-shaped candidate paths plus deterministic column-grouped and Hungarian min-cost-matching fallbacks.
- Physical loss model tied to compiled schedules: pickup 0.2%, 2Q gate 0.1%, imaging 0.1%, transport loss from motional heating Δn ∝ ℓ²/(ω³t_f⁴) with trap-depth-averaged survival.
- Delayed-erasure decoder built as concatenated DEMs (Pauli DEM plus per-measurement loss-conditioned DEMs with depolarizing surrogates) fed to PyMatching; loss-aware cultivation including the escape stage.

**How it works** Compiled schedules yield a per-round loss p_rnd(d); Stim simulations of SWAP-SE memory experiments (d = 3–9, up to 10⁷ shots) are fit to P_L = A(p/p₀)^{αd} + Bγ^{(d+1)/2}, giving a tolerable per-round loss p_dec(d). The minimum feasible distance is the smallest d with p_rnd(d) ≤ p_dec(d); since transport length grows with d, shorter routes buy smaller codes. Sweeps show conventional SE fails to suppress loss while SWAP-SE grows LER only linearly in rounds, an interior space-time-volume optimum at Δn ≈ 5, and that more AODs compress schedules but concentrate loss (3 AODs fit d=11, 4 force d=13).

**Why it matters** Architecture and compiler work for neutral atoms has largely assumed a fixed, circuit-independent loss rate; this shows loss is a compilation-dependent quantity that determines code distance, and questions the scalability of zoned layouts for deep logical circuits. Useful to compiler designers, QEC decoder developers, and hardware architects setting reloading, AOD, and shuttling specs.

**Caveats** LERs are extrapolated from memory experiments, not full logical circuits; the ZAC comparison rescales a physical-atom rearrangement compiler into a logical-patch "token" model and only CX layers are compared. Cultivation uses |Y⟩ as a proxy for |T⟩ and simulates cultivation and escape stages separately, combined conservatively. Loss is modeled as inserted depolarizing noise with a leading-order additive accumulation; single-qubit gate errors and reloading dynamics/latency are neglected, and the layout presumes focused Rydberg addressing with ~10 µm interaction range.

## 2. Minimax games for quantum channel discrimination

[arXiv:2609.09839](https://arxiv.org/abs/2609.09839) · [SciRate](https://scirate.com/arxiv/2609.09839)

*Kun Fang, Michael X. Cao, Hao-Chung Cheng, Li Gao, Masahito Hayashi*

**TL;DR** This paper sets up a two-player (tester vs. jammer) minimax formulation of quantum channel discrimination in which both parties feed separate inputs into the channel under test, generating twelve game models from three input structures (entangled/IID for each player) crossed with four information patterns (public/secret jammer × hypothesis-aware/unaware). All twelve are exactly characterized at finite blocklength by nine hypothesis-testing channel divergences and asymptotically collapse to five Umegaki relative-entropy rates; a general "achievability implies strong converse" principle is developed that also settles an open strong-converse question of Berta–Brandão–Hirche and upgrades several of Lami's recent Stein lemmas.

**The big picture** Discriminating two quantum processes is usually studied either optimistically, where the experimenter fully controls what goes into the device, or pessimistically, where an adversary or uncontrolled environment does. Reality often sits in between: part of the input is trusted and part is noise, interference, or malicious injection. This work builds a game-theoretic bridge between the two extremes, classifies all the natural variants by who moves first and who knows the true hypothesis, and shows that in the long-run limit many of these seemingly different situations become operationally identical — provided the adversary is allowed correlated inputs. It also delivers a general technique that turns a lower bound on achievable performance into a proof that no strategy can do better even at large error tolerance.

**Key contributions**
- A minimax channel-discrimination framework with split input control, recovering tester-input and jammer-input settings as degenerate cases.
- Exact finite-blocklength operational correspondence: twelve games ↔ nine minimax/maximin hypothesis-testing divergences (secret games collapse hypothesis-awareness; secret IID jammers require convexification of the tensor-power set).
- "Operational collapse": with an entangled jammer, all four information patterns share one asymptotic Stein exponent (both for entangled and IID testers); with IID jammers the pattern still matters, though the two secret variants coincide.
- Replacer alternative channels: all twelve exponents equal one additive, single-letter quantity.
- A generic achievability→strong-converse upgrade for sequences of states *and* sets of states, yielding strong converses for several games, resolving Berta et al.'s Remark 2.2, and strengthening Lami's arXiv:2510.06340 results.

**How it works** Finite-blocklength values are matched to divergences via the hypothesis-testing relative entropy plus a composite-testing minimax identity (affinity of both error probabilities in the jammer state permits replacing the IID jammer set by its convex hull). Asymptotics use: (i) a minimax swap that erases the public/secret distinction for convex (entangled) jammer sets; (ii) a mixing construction replacing hypothesis-dependent jammer states by a common state at vanishing rate cost; (iii) for IID testers, where nonconvexity blocks minimax, an explicit jammer strategy that blends per-tester-tailored inputs into one input uniformly effective over all IID tester choices. Standard tools (sandwiched/measured Rényi bounds, permutation-invariance spectrum polynomial bounds) supply the one-shot estimates.

**Why it matters** It provides the right asymptotic figures of merit for verification, benchmarking, and sensing under partially adversarial or noisy input control, and connects to arbitrarily varying channel communication. The achievability-to-strong-converse principle is of independent interest for composite quantum hypothesis testing.

**Caveats** Several exponents remain regularized (non-single-letter) except for replacer alternatives; strong converses are established only for a subset of models (IID tester vs. secret entangled jammer, trivial tester vs. secret IID jammer), while the entangled-tester case — and the classic tester-input strong converse — remain open. Only parallel (non-adaptive) strategies and finite dimensions are treated, and the jammer is assumed at least as powerful as the tester.

## 3. Non-Multiplicativity of the Holevo Barycenter of Quantum Channels

[arXiv:2609.09373](https://arxiv.org/abs/2609.09373) · [SciRate](https://scirate.com/arxiv/2609.09373)

*Sayantan Chakraborty, Stefano Mancini, Leonardo Rossetti, Andreas Winter*

**TL;DR** The authors settle a residual open question left by Shor–Hastings: the Holevo barycenter (the unique average output state of any capacity-achieving ensemble) is *not* multiplicative under tensor products. Using direct sums of channels, where block weights are set by Holevo capacities, they mix a non-additive Hastings-type pair with an entanglement-breaking (or depolarizing) channel so that the block weights of the barycenter of the tensor square and of the tensor square of the barycenter provably disagree. They also show the entropy — indeed the majorization order — of the barycenter is neither universally sub- nor superadditive.

**The big picture** A quantum channel's optimal input ensemble for classical communication is generally non-unique, but the averaged output it produces is unique, and this average state is a natural geometric fingerprint of the channel. It has long been known that classical capacity fails to add up when channels are used in parallel, but the standard counterexamples were built with so much symmetry that this fingerprint still behaved perfectly multiplicatively, leaving open whether it always does. Here the authors show it does not: by gluing together a well-behaved channel and a badly-behaved one into a single channel that chooses between branches, the fingerprint of the parallel use is genuinely different from the product of the individual fingerprints, and the mismatch can go either way when measured by entropy. This means the geometric structure of optimal signal ensembles is intrinsically unstable under parallel composition, and no simple single-shot rule can predict it.

**Key contributions**
- A proof that the Holevo barycenter is non-multiplicative (Theorem 1), strengthening non-additivity of Holevo capacity.
- Explicit identification of why Shor's reduction hides the phenomenon: twirling by a perfectly randomizing unitary set forces maximally mixed barycenters both for the enlarged channels and their product, so they trivially tensorize.
- A construction showing no universal entropic ordering and, more strongly, no universal majorization ordering between the two states.

**How it works** For a direct-sum channel, Fukuda–Wolf give χ(⊕Nᵢ)=log Σ2^{χ(Nᵢ)} and a block-diagonal optimal ensemble with weights λᵢ ∝ 2^{χ(Nᵢ)}; hence the barycenter is block diagonal with those weights. Since N⊗N = ⊕_{i,j} Nᵢ⊗N_j, the barycenter of the square has weights ∝ 2^{χ(Nᵢ⊗N_j)} while the product of barycenters has weights ∝ 2^{χ(Nᵢ)+χ(N_j)}. Taking N = N₀ ⊕ N₁ ⊕ N₂ with N₁,N₂ strictly superadditive by δ>0 (Hastings + Shor) and N₀ entanglement-breaking (additive with everything, by Shor), the ratio a₁₂/a₀₁ = 2^δ · b₁₂/b₀₁, so the weight families cannot match. For the entropy result, N = N₀ ⊕ N₁ with N₀ depolarizing (King additivity) makes all blocks maximally mixed on dimension d², reducing the comparison to Shannon entropies of λ vs μ. Choosing χ(N₀)=χ(N₁) gives λ uniform and μ ∝ (1,1,1,2^δ), so H(μ)<H(λ); choosing χ(N₀)=χ(N₁)+δ (feasible since χ(N₁)+δ ≤ log d via data processing plus King) reverses the majorization.

**Why it matters** It cleanly separates two properties that were only known to be logically ordered (additivity ⇒ multiplicativity), completing the picture Shirokov initiated, and shows barycentric/geometric quantities are "relational" rather than absolute — relevant for anyone building resource measures or classification schemes from optimal output ensembles, and possibly for hunting a tractable additivity counterexample.

**Caveats** The result is purely existential: it inherits Hastings' non-constructive, high-dimensional random-unitary channels, so no explicit small example or quantitative bound on δ is provided, and the deviation is at most a factor 2^δ in block weights. Direct sums are arguably a somewhat artificial mechanism — the non-multiplicativity lives entirely in classical branch weights, not in the block states themselves. Whether irreducible (non-direct-sum) channels exhibit the phenomenon, and the infinite-dimensional/continuous-variable case, remain open.

## 4. Information Causality Characterizes the Set of Quantum Correlations in the Simplest Bell Scenario

[arXiv:2609.10508](https://arxiv.org/abs/2609.10508) · [SciRate](https://scirate.com/arxiv/2609.10508)

*Mariami Gachechiladze, Nikolai Miklin*

**TL;DR** Using the correlated-input generalization of information causality (IC) together with a new protocol — Alice feeds her *entire* record $(x_0,x_1,a)$ into a marginal-dependent noisy channel, and Bob's information is scored on the raw transcript $(m',b)$ rather than a guess — the authors derive the full Tsirelson–Landau–Masanes (TLM) criterion in the vanishing-capacity limit, thereby recovering the exact quantum boundary of the four correlators in the 2-input/2-output Bell scenario. They further exhibit an explicit non-signaling box that saturates TLM (so is macroscopically local) yet violates IC at unit capacity (LHS $=\tfrac14\log 5+\tfrac3{10}\log 3\approx1.056>1$), proving IC is strictly stronger than macroscopic locality (ML) already in the simplest scenario.

**The big picture** A long-standing programme in quantum foundations asks which simple, operationally meaningful physical principles pick out exactly the correlations quantum theory allows, without assuming Hilbert spaces. Information causality — the demand that a receiver cannot learn more about a sender's data than the number of bits transmitted, even with shared nonlocal resources — had only ever reproduced weaker bounds, and was widely suspected to be too blunt. This work shows that with a smarter communication protocol the same principle reproduces the exact known boundary for the simplest experiment, and in fact rules out some correlations that the competing macroscopic-locality principle permits. That reverses the prevailing hierarchy between these two principles and gives a systematic recipe for pushing the approach to larger settings.

**Key contributions**
- Derivation of the complete TLM criterion (including nonzero marginals, via the renormalized correlators $D_{x,y}$) directly from IC.
- A refined IC statement: transcript-based mutual information $I(x_0;m',b|y{=}0)+I(x_1;m',b|y{=}1,x_0)\le I(m;m')$, justified by data processing.
- Proof that generalized IC $\Rightarrow$ ML in this scenario, plus an explicit ML box violating IC, establishing strict inclusion.

**How it works** Alice measures $x=x_0\oplus x_1$; her inputs are correlated with parity bias $\varepsilon$. The channel is parametrized as $\Pr(m'|m)=\tfrac12+\tfrac{(-1)^{m'}e_c}{2}f_m$ with $f_{x_0,x_1,a}=(-1)^{a\oplus x_0}\kappa_{x_0\oplus x_1}/\sqrt{1-\langle a_{x}\rangle^2}$, which injects Alice's marginal normalization; keeping $b$ in the transcript weights terms by $1/\Pr(b|y)$, supplying Bob's normalization. Expanding as $e_c\to0$ (L'Hôpital twice) gives a quadratic form in $(\kappa_0,\kappa_1)$; positive semidefiniteness of the associated $2\times2$ matrix, optimized over $\varepsilon$ with $\frac{1+\varepsilon}{1-\varepsilon}=\sqrt{\frac{(1-D_{0,1}^2)(1-D_{1,0}^2)}{(1-D_{0,0}^2)(1-D_{1,1}^2)}}$, yields Landau's form of TLM. The separation from ML instead uses finite capacity: the van Dam protocol with a perfect bit channel on a hand-crafted box.

**Why it matters** Restores IC as a leading candidate device-independent principle; combined with the authors' earlier IC $\Rightarrow$ NTCC result, IC now dominates both main rival principles in this scenario. The marginal-dependent-channel + transcript trick is a reusable tool for deriving tight quantum Bell inequalities in richer scenarios.

**Caveats** The "characterization" is of the projection onto the four correlators, where quantum = ML = almost-quantum; the full probability-space quantum set is strictly smaller (their own ML counterexample has nonzero marginals and sits on TLM's boundary). Whether almost-quantum correlations satisfy generalized IC is explicitly left open, as is extension beyond binary inputs/outputs. Only a proof sketch plus appendix computation is given; the finite-capacity violation is a single hand-picked example rather than a general characterization.

## 5. Constant-depth global shadow estimation

[arXiv:2609.10408](https://arxiv.org/abs/2609.10408) · [SciRate](https://scirate.com/arxiv/2609.10408)

*Qingyue Zhang, Zhou You, Dayue Qin, Xiaopeng Li, Jens Eisert, You Zhou*

**TL;DR** The authors show that global classical-shadow estimation of stabilizer-state fidelities can be done with a *sparse Clifford-IQP* ensemble ($S$–$CZ$–$H$ circuits with each $CZ$ included at probability $p=\gamma\ln n/n$), even though this ensemble provably fails to be a relative-error state 2-design (it stays $\geq 1/8-o(1)$ away). The trick is a "second-look" principle: measure two tracks, $\rho$ and $H^{\otimes n}\rho H^{\otimes n}$, and pick which one to use per observable in post-processing, yielding bias $\le (4n^2+2n)n^{-0.4\gamma}+\mathrm{negl}(n)$ for $\gamma>3$. Because the diagonal layer commutes, the circuits run in $O(1)$ depth on all-to-all hardware with $O(n\log(n/\epsilon))$ ancillas (or $O(\log(n/\epsilon))$ depth ancilla-free), beating the $\Omega(\log\log n)$ depth barrier for approximate designs.

**The big picture** Reading out useful information from a large quantum processor via randomized measurements normally requires measurement circuits that are themselves "generically random", and generating that randomness costs circuit depth that grows with system size. This work shows that if you only care about a structured but practically central family of quantities — overlaps with stabilizer states, the workhorse states of error correction and measurement-based computing — then far less randomness suffices, and the readout circuits can be made constant depth. Crucially, the protocol still lets you decide which quantity to estimate after the data are collected, so the defining flexibility of classical shadows is preserved. The conceptual message is that scalable readout should be tailored to the class of questions being asked rather than mimicking full random unitary behaviour.

**Key contributions**
- Exact closed forms for the second (and third) moment operators of the sparse Clifford-IQP ensemble, with a clean trinomial decomposition into $\Delta_2$, $\mathbb{I}_4-\Delta_2$, $\mathbb{S}_2-\Delta_2$ blocks, and a Pauli-diagonal channel coefficient $\sigma_P$ depending only on $(n_1,n_2,n_3)$.
- Proof that the ensemble is *not* an $\epsilon$-relative-error state 2-design for $\epsilon<1/8-o(1)$, plus an explicit worst-case bias $\ge\frac12(1-2\gamma\ln n/n)$ for $|{+}\rangle^{\otimes2}|0\rangle^{\otimes n-2}$.
- The second-look principle: bias is governed by $\mathrm{rank}(C)$ vs $\mathrm{rank}(D)$ of the observable's stabilizer tableau; choosing the better track gives a uniform vanishing-bias guarantee over all stabilizer observables.
- Constant-depth synthesis via GHZ "rail" fan-out/fan-in with mid-circuit measurement and feedforward; resource bounds $3\gamma n\ln n$ ancillas at $O(1)$ depth, or depth $2\gamma\ln n$ ancilla-free.
- An exactly unbiased variant inverting the Pauli-diagonal channel by $\sigma_P^{-1}$, efficiently computable from tableaus, and compatible with Pauli-noise mitigation.

**How it works** The bias bound partitions stabilizer Paulis by $X$-weight $n_3$: small $n_3$ gives large $|\sigma_P-1|$ but few contributing Paulis, large $n_3$ gives many Paulis but exponentially suppressed deviations; the Hadamard-conjugated track guarantees a favourable $X$-weight distribution so both bad regimes never co-occur. Implementation-wise, each qubit is expanded into a rail of length equal to its $CZ$-degree in the sampled Erdős–Rényi interaction graph, so all $CZ$s fire in one layer.

**Why it matters** This is a concrete, hardware-adapted route to global (not just local/shallow-MPO) shadow estimation on neutral-atom and trapped-ion machines with native $CZ$ and long-range connectivity. Numerically, $\gamma=2$ already yields bias $\approx0.05$ at $n=50$ ($\approx182$ two-qubit gates at $n=48$), several-fold fewer entangling gates than gluing or 1D brickwork shadows at matched bias, with continuously tunable cost rather than discrete patch sizes.

**Caveats** Guarantees cover stabilizer-state fidelities only (motivated partly by classical post-processing tractability); extension to magic-carrying observables is left open. The lightweight estimator is biased, and the unbiased variant costs extra classical work (only empirically polynomial; MPO acceleration is speculative). Variance is proven merely sub-exponential, with small values only observed numerically; the theorem needs $\gamma>3$ while numerics work at $\gamma\approx2$. Constant depth assumes all-to-all connectivity, reliable mid-circuit measurement and feedforward, and $O(n\log n)$ ancillas whose rearrangement/shuttling cost is not modelled. Noise robustness is discussed only qualitatively.
