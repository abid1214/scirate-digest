# SciRate Daily Digest — 2026-09-12

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Walking Floquet code circuits for zero-overhead leakage reduction

[arXiv:2609.10666](https://arxiv.org/abs/2609.10666) · [SciRate](https://scirate.com/arxiv/2609.10666)

*Hanna Westerheim, Kaavya Sahay, Shruti Puri*

**TL;DR** The authors construct two "walking" circuit implementations of the P6 honeycomb Floquet code — *swirling* (for reconfigurable/neutral-atom hardware) and *sliding* (for fixed square-lattice connectivity) — that reset every physical qubit periodically using SWAP-based leakage reduction units folded into the syndrome-extraction circuit at zero cost in qubits, gates, or depth, while provably preserving the code's Pauli distance. Qubit lifetimes drop from 8 entangling gates (walking surface code) to 4 on average, and numerics under four leakage models show regimes — driven by entropic "waterfall" behavior rather than asymptotic distance — where the Floquet code beats the same-distance surface code.

**The big picture** Qubits sometimes escape the computational states entirely, and error-correcting codes cannot see this happen, so the damage spreads silently and correlates errors across space and time. The standard fix is to periodically shuffle roles so that every qubit gets freshly reset, which has been worked out for the surface code. This work does the same for honeycomb Floquet codes, where the checks touch only two qubits at a time, so leakage has less chance to spread before being flushed out — and it does so without adding any operations to the circuit. The comparison also reveals that at realistic hardware error rates, the counting of many moderately bad failure patterns matters more than the single worst-case one, which can reverse which code looks better.

**Key contributions**
- First hFC leakage-reducing circuits that are simultaneously zero-overhead *and* distance-preserving (prior dynamic hFC circuits sacrificed distance).
- Combining early-SWAP and late-SWAP LRU gadgets in a single schedule; the sliding variant embeds the honeycomb on square nearest-neighbor connectivity with one plaquette per site, using only 3d² total qubits (vs 5d² for swirling).
- Fault-tolerance proofs for standard/early-/late-SWAP SECs via ZX fault-equivalence rewrites.
- Upper bounds on minimum malignant leakage fault weight: hFC ⌈d/2⌉ vs SC ⌈d/4⌉ under *tailored* leakage; equal (⌈d/4⌉, ⌈d/2⌉) under depolarizing and skip-gate.
- Numerical evidence that observed scaling exponents exceed these bounds and grow with distance, i.e. entropy-dominated waterfall behavior.

**How it works** Late-SWAP inserts a SWAP before measurement, compiled away via CX-decomposition plus measurement-absorption into a classical Pauli-frame update (folded into the decoder); early-SWAP inserts it after the first CX, where it becomes trivial. Swirling applies late-SWAPs on a bipartite-alternating half of the data qubits each subround, with atom rearrangement restoring geometry; sliding chooses early vs late per edge according to available connectivity, translating the lattice diagonally each pair of subrounds. Detectors are rebuilt to absorb the randomized frame updates — still 12 edge outcomes over five timesteps, but with modified spacetime support. Simulations at d=6,12 under uniform per-location leakage with depolarizing, tailored, skip-gate, and 10%-transport models.

**Why it matters** Leakage is a growing fraction of the error budget in transmon and neutral-atom devices; this gives a free-of-charge LRU schedule for a code family with weight-2 checks and shows the surface code is not automatically the right choice under leakage.

**Caveats** Toric geometry only (planar boundaries untested); minimum-weight values are adversarial *upper bounds*, not exhaustive searches; crossovers are extrapolated below simulated p; hFC uses 1.5–2.5× the qubits of the SC per code distance (encoding two logicals, one reported); leakage-detection/erasure-conversion information is not exploited; the sliding variant's non-uniform, longer maximum lifetimes make its advantage less pronounced, and the explanation is hypothesized rather than established.

## 2. Tight Time-Space Lower Bounds for Collision Finding and Element Distinctness under Label Symmetry

[arXiv:2609.10808](https://arxiv.org/abs/2609.10808) · [SciRate](https://scirate.com/arxiv/2609.10808)

*Frédéric Magniez, Sebastian Zur*

**TL;DR** — For quantum algorithms whose behaviour is invariant under relabelling the range of the hash function ("label-symmetric"), this work proves a tight query–space tradeoff for finding a *single* collision in a uniformly random $f:[M]\to[N]$: $T=\Omega(N^{1/3})$ and $T^2S=\Omega(N\log N)$, matched by a space-efficient BHT implementation, with the corollary $T=\Omega(n^{2/3})$, $T^2S=\Omega(n^2\log n)$ for search Element Distinctness on $f:[n]\to[n^2]$, matching Ambainis's walk. The engine is a space-sensitive compressed-oracle argument: representation theory of $\mathfrak S_N$ shows an $S$-qubit label-symmetric algorithm can effectively hold only $O(S/\log N)$ collision-free database entries.

**The big picture** — Quantum algorithms can find hash collisions faster than classical ones, but only if they have a large, quantumly addressable memory; how the speedup degrades as memory shrinks has been a long-standing open question, highlighted by Aaronson. This paper settles the question for the natural class of algorithms that treat the hash function's output values as anonymous tokens — a class that includes the two canonical algorithms for these problems. The answer says those two algorithms are exactly optimal across the whole memory range, which is directly relevant to choosing post-quantum security parameters for hash functions.

**Key contributions**
- First quantum time–space lower bound for finding a *single* collision in a random function (previous work handled only $K$ collisions), under label symmetry.
- Proof that BHT, Ambainis's quantum walk, and any algorithm using only pairwise equality queries are label-symmetric.
- A space-sensitive version of the compressed-oracle technique: an "orbit bound" $\dim\mathrm{span}\{\sigma\ket\beta\}\le 2^S$ from the rank of the reduced input state.
- Sharpened spectral analysis of arrangement graphs $A_{N,s}$ (injective $s$-tuples, adjacency = differ in one coordinate) for all $N\ge 2s$: least eigenvalue $-s$, exact gap $N-2s+2$ above it.

**How it works** — Progress is tracked by $\Delta_t=\|\Pi_{\ge1}\ket{\tilde\psi_t}\|$; one query increases it by at most $\frac{4}{\sqrt N}(\sum_s s\|\Pi_{=0}\Lambda_s\ket{\tilde\psi_t}\|^2)^{1/2}$. The crux is bounding that sum by $\min\{t,2S/\log_2 N\}$ rather than $t$. Databases with $s$ occupied cells that are both collision-free and valid compressed states live in $C_s^\perp\cap W^{\otimes s}$, identified via a coordinate-deletion map $D$ with $D^\dagger D=A_{N,s}+s\,\mathrm{id}$, i.e. the $(-s)$-eigenspace of the arrangement graph. All its irreducible constituents have dimension $\ge\binom Ns-\binom N{s-1}>2^S$ once $s>2S/\log_2N$, so the orbit bound forces zero overlap there. Since the collision-free and Fourier-support projections don't commute, a gap-derived bound $\|\Pi_{C_s^\perp}\Pi_{W^{\otimes s}}-\Pi_{C_s^\perp\cap W^{\otimes s}}\|^2\le (2s-2)/N$ converts "no overlap" into a $(2s-2)/N$ damping factor.

**Why it matters** — It converts a folklore intuition (BHT's memory is necessary) into a theorem for essentially all known algorithms, and supplies a reusable template — symmetry plus representation theory on top of compressed oracles — for other short-output time–space problems.

**Caveats** — Label symmetry is the whole crutch: the authors note that generic symmetrisation stores a random permutation costing $\Theta(N\log N)$ extra space, so removing the assumption is genuinely open. Bounds assume $t\le\sqrt N$, $S\ge\log_2 N$, $N\ge 2s$; tightness of the collision bound is claimed for $M=N$. Space is dimension of the algorithm's Hilbert space, so the distinction between QRAM and quantum-accessible classical memory is abstracted away.

## 3. The generalised semi-Clifford conjecture is false

[arXiv:2609.11903](https://arxiv.org/abs/2609.11903) · [SciRate](https://scirate.com/arxiv/2609.11903)

*Nadish de Silva, Oscar Lautsch*

**TL;DR** The authors exhibit an explicit five-qubit gate — a two-control multiplexed-Clifford gate built from a controlled-Clifford $\ctrl_{\mathtt c}(B)$ and a controlled-commutator $\ctrl_{\mathtt d}(A)$ with $A=JBJ^\dagger B^\dagger$ for a Pauli $\pi/2$-rotation $J$ — that lies in $\mathcal C_5\setminus\mathcal C_4$ but admits no decomposition $C_1\Pi D C_2$, refuting the 2007 Zeng–Chen–Chuang generalised semi-Clifford (GSC) conjecture. The same gate's inverse lies in no level of the hierarchy, showing the Clifford hierarchy is not closed under inverses. The paper is written as a derivation: each section narrows the search space until explicit equations are solved.

**The big picture** Fault-tolerant quantum computing relies on a nested family of gate sets that can be implemented by teleportation with magic states, and for over fifteen years the leading structural guess was that every such gate is a Clifford gate, followed by a permutation of basis states, a phase-only operation, and another Clifford. That guess was proven at the third level and widely believed in general. Here it is shown to fail at the fifth level on five qubits, by systematically deducing — rather than guessing — what a counterexample must look like. Consequently no simple normal form classifies these gates, and the natural intuition that the gate set behaves like a group is also wrong, since the constructed gate's inverse escapes the hierarchy entirely.

**Key contributions**
- Criteria for multiplexed-Clifford gates: hierarchy membership reduces to Pauli commutators; GSC holds iff the normalised target symplectic matrices share a common invariant Lagrangian (proved via a "compression" lemma showing a maximal commuting Pauli algebra compresses to a control-independent target algebra).
- Positive results: every singly-controlled-Clifford gate in the hierarchy is GSC; and the $m=1$ (level-4) case of their two-control criterion always yields GSC gates. These force any counterexample of this type to level ≥5 with ≥2 controls.
- A sufficient two-control hierarchy criterion: second-control independence of comparison matrices plus $(\mathsf R_{\vx}-\mathbb I)^{2^m-1}=0$ implies $W\in\mathcal C_{m+3}$.
- The explicit counterexample, plus non-membership of its inverse in any $\mathcal C_k$.

**How it works** Normalising $C_{\bm 0}=\mathbb I$, the independence equations force $C_{\vz}=B^{z_{\mathtt c}}A^{z_{\mathtt d}}$ with $\mathsf A^2=\mathbb I$. Choosing $A$ as a group commutator with a Pauli rotation $J_P$ (a symplectic transvection) makes two of the three nilpotency conditions collapse, leaving $\mathsf N^6=0$ for $\mathsf N=\mathsf B-\mathbb I$. Requiring $\vp=[P]$ to be a *cyclic* vector for $\mathsf N$ pins the target register to $n=3$ qubits, gives $\ker\mathsf N$ one-dimensional, and hence forces its generator into every $\mathsf B$-invariant subspace — which $\mathsf A$ then moves, killing any common invariant Lagrangian. Reality of $B$ and $J$ is essential: it reduces phase ambiguities in the symplectic kernel to $\pm1$, so controlled corrections stay Pauli.

**Why it matters** GSC structure underpinned intuitions about hierarchy gates, magic-state distillation and gate synthesis; its failure means classification must proceed by other invariants (e.g. the symplectic/commutator machinery developed here). The inverse-closure failure also constrains how hierarchy levels can be used as a resource-theoretic bookkeeping device.

**Caveats** The construction is sufficient, not exhaustive: it is not shown that 5 qubits or level 5 are minimal, nor whether level-4 counterexamples exist at all (only that this family's $m=1$ case is GSC). Everything is qubit-specific and leans on reality of the Cliffords; qudit and continuous-variable analogues are untouched. The final verification that $U\notin\mathcal C_4$, and the inverse argument, rest on sections beyond the portion of the derivation examined here.

## 4. The cost of simulating classically tractable quantum circuits and dynamics

[arXiv:2609.11847](https://arxiv.org/abs/2609.11847) · [SciRate](https://scirate.com/arxiv/2609.11847)

*Su Yeon Chang, Supanut Thanasilp, Zoë Holmes, M. Cerezo*

**TL;DR** The authors put "classically simulable" circuit families and direct quantum execution on the same resource footing, tracking three separate costs — quantum samples (shots), quantum time (circuit depth), and classical operations — for Clifford, shallow HEA, matchgate, $S_n$- and $U(1)$-equivariant, QCNN, and restricted ADAPT-VQE evolutions. The decisive structural difference is not polynomial vs. exponential scaling but *one-time vs. per-instance* costs: classical surrogates typically need an expensive one-off quantum characterization of an unknown input state, after which each of the $T$ circuit instances is cheap, whereas quantum simulation pays shots for every instance. Translated into hardware wall-clock times and cloud per-shot prices, this yields crossovers where quantum execution is preferable despite a provably polynomial classical algorithm.

**The big picture** A proof that some quantum process can be simulated efficiently on a classical computer is an asymptotic statement about scaling, not a verdict about what you should actually run. This paper asks the practical question: given a family of circuits that provably admits a polynomial-time classical simulation, is it cheaper in wall-clock time or in dollars to run the classical surrogate or to just execute the circuit on hardware? The answer depends heavily on whether the input state is already known classically — if it is not, the surrogate must first be fed experimental measurement data, and that characterization step can dwarf everything else — and on how many different circuits you need to evaluate. The upshot is that classical simulability, wall-clock advantage, and cost advantage are three distinct notions that frequently disagree.

**Key contributions**
- A unified three-metric accounting framework (quantum sample, quantum time, classical time) applied uniformly to QS and to architecture-specific classical simulators.
- Per-family complexity theorems, e.g. Clifford surrogates still require the *same* $O(T\|\vec c\|_1^2\epsilon^{-2}\log(T/\delta))$ shots as QS but only $O(1)$ depth; shallow HEA needs $O(16^k n^4 \epsilon^{-2}\|\vec c\|_1^2 \log(MT/\delta))$ shots *once*; matchgates $O(n^{\kappa/2}\cdots)$; $U(1)$-equivariant $O(n^{3h}\cdots)$; QCNN $\exp(O(\tau))$; ADAPT-VQE with a Hartree–Fock input needs zero quantum resources.
- Explicit separation of one-time preprocessing (e.g. $O(Kd_\lambda^3)$ for $\mathfrak{g}$-sim) from per-instance evaluation ($O(TLd_\lambda^2)$).
- Conversion into representative hardware wall-clock and cloud pricing estimates, identifying $T$-dependent crossover regimes.

**How it works** Expectation-value estimation $\mathrm{Tr}[U\rho U^\dagger O]$ to additive $\epsilon$ is the common task. QS is analyzed with a weighted shot-allocation strategy ($N_\alpha \propto |c_\alpha|$) under a worst-case ungrouped-measurement model. Each classical surrogate is chosen to match the structure: symplectic $\mathbb{F}_2$ matrices for Clifford, light-cone-reduced unitaries for shallow circuits, $\mathfrak{g}$-sim on invariant Majorana/irrep submodules for matchgates and $S_n$-equivariance, Givens-rotation blocks for fixed-Hamming-weight sectors, and truncated Pauli/Majorana propagation for QCNNs and ADAPT-VQE.

**Why it matters** It reframes "dequantization" claims: proving polynomial simulability does not settle which route to take, especially for high-degree polynomials with large prefactors or when input-state tomography is needed. Relevant to anyone benchmarking variational algorithms, claiming quantum advantage, or using surrogates as hardware-development tools.

**Caveats** Single-copy access only — no quantum memory or multi-copy shadow protocols, which could substantially reduce the data-acquisition bottleneck. Noise and error correction are outside the model. Measurement grouping is relegated to an appendix, so QS sample counts are pessimistic. Truncation-based results (QCNN, ADAPT-VQE) inherit assumptions about random initialization or persistence of low-weight structure during training. Conclusions about monetary cost hinge on current cloud pricing, which is volatile.

## 5. Hierarchy of Rényi Coherent Information in Stabilizer Codes

[arXiv:2609.11930](https://arxiv.org/abs/2609.11930) · [SciRate](https://scirate.com/arxiv/2609.11930)

*Akash Vijay, Luis Colmenarez, Jong Yeon Lee*

**TL;DR** For any finite qubit stabilizer code under Pauli noise built from *independent Bernoulli fault events*, the Rényi-$n$ coherent information is proven nondecreasing in integer $n$, settling a widely observed but unproven numerical ordering of Rényi error thresholds. Separately, for arbitrary stochastic Pauli noise the Rényi-$n$ coherent information is given operational teeth: it governs recovery after postselecting on matching syndromes across one data block and $n-1$ maximally mixed ancilla blocks, with saturation equivalent to asymptotically perfect decoding under the power-reweighted syndrome distribution $p_s^n$.

**The big picture** Studies of decoherence-induced phase transitions in noisy quantum memories almost always compute replica-style entropies instead of the true von Neumann coherent information, because only the former map onto tractable statistical-mechanics models. It has long been observed numerically that the apparent error threshold drifts upward as one increases the replica index, but this ordering had no proof and the replica quantities carried no operational guarantee about error correction. This work proves the ordering for a broad and physically standard class of noise, identifies explicitly where it breaks, and shows exactly what error-correction statement the replica quantity does make — namely a statement about decoding a postselected ensemble in which more likely syndromes are over-weighted.

**Key contributions**
- A general binary-linear theorem: for independent Bernoulli bits mapped linearly to nested labels (fine $T$, coarse $C$), $\Delta_n = H_n(T)-H_n(C)$ is nonincreasing in integer $n$. Covers classical linear codes and circuit-level detector error models, and allows multi-qubit correlated events.
- Corollary: $I_c^{(1)}\le I_c^{(2)}\le\cdots\le I_c^{(\infty)}$ for all stabilizer codes (no CSS structure, no locality, any $k$), hence ordered threshold crossings $p_c^{(n)}$.
- Explicit counterexamples with *product* (but non-independent-event) Pauli noise: a $[[2,1,1]]$ channel violating $\Delta_1\ge\Delta_2$ and a distance-2 $[[4,1,2]]$ channel violating $\Delta_2\ge\Delta_3$; plus a single-qubit Fourier criterion $\hat\nu(X)\hat\nu(Y)\hat\nu(Z)\ge0$ characterizing the independent-event class (depolarizing noise qualifies up to $p=3/4$).
- Matched-syndrome gadget: $n$-balance (input-independent acceptance) is shown necessary *and* sufficient for the normalized postselected map to be a channel; it holds automatically for stochastic Pauli noise. Bounds $F_n^n\le e^{-(n-1)\Delta_n}\le F_n$, and for general noise $F_n\ge B_n^2$ with a $d_L$-dependent converse.

**How it works** Step I ($\Delta_1\ge\Delta_2$) compares a binary symmetric channel to an erasure channel with $\theta_a=4p_a(1-p_a)$ via strong data processing, giving $\Delta_1\ge(\log 2)\,\mathbb{E}_\mu\kappa(\Gamma)$ with $\kappa=\mathrm{rank}\,T_\Gamma-\mathrm{rank}\,C_\Gamma$; the collision entropy is bounded from the other side by Harris's inequality plus Jensen. Step II writes the $(m{+}1)$st coset moment as a replica ferromagnetic Ising partition function with couplings $J_a=\frac12\log\frac{1-p_a}{p_a}\ge0$, expresses $\Delta_{m+1}$ as a pinning free-energy integral over $\langle\zeta_{1,j}\rangle$, and uses GKS correlation inequalities while interpolating in the coupling $\eta$ of an added replica.

**Why it matters** It legitimizes the standard practice of reading thresholds off replica calculations: the $n=2$ (statistical-mechanics-mapped) threshold is a rigorous *upper* bound relative to $n=1$ only in the stated direction, so replica thresholds systematically overestimate the true one. Relevant to mixed-state phase classification, decoder benchmarking, and randomized-measurement estimation of code performance.

**Caveats** Monotonicity is proven only for integer $n$ and binary (qubit) systems — the $\pm1$-character/Ising argument does not extend to qudits. The independent-event condition is sufficient, not necessary; whether *homogeneous* product noise $\nu^{\otimes N}$ can violate the hierarchy is open. The matched-syndrome channel costs acceptance probability $Z_n=e^{-(n-1)H_n(S)}$, exponentially small for extensive $H_n(S)$. Positive $I_c^{(n)}$ does not imply positive matched coherent information, and the general-noise converse degrades as $d_L^{n-1}$.
