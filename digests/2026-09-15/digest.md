# SciRate Daily Digest — 2026-09-15

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. 2609.15059

[arXiv:2609.15059](https://arxiv.org/abs/2609.15059) · [SciRate](https://scirate.com/arxiv/2609.15059)



**TL;DR** Any fermionic quantum error-correcting code with Majorana distance ≥ 3 contains *no* pure fermionic Gaussian state in its code space, so free-fermion (matchgate) resources alone can never implement nontrivial fermionic QEC. The authors further show that even distance-2 detection codes admit no Gaussian encoder or non-destructive syndrome measurement, and prove a lower bound of Ω(d_F + k) bounded-weight non-Gaussian gates for exact codeword preparation.

**The big picture** Fermionic hardware — Majorana qubits, cold-atom simulators — comes with a natural set of easy operations built from free, non-interacting particle dynamics, which are also efficiently simulable on a classical computer. For qubits, the analogous easy operations (stabilizer circuits) are exactly the ones used to build error-correcting codes, which is why large-scale qubit codes can be designed and benchmarked classically. This work shows that the fermionic analogy breaks completely: protecting logical information necessarily requires genuine many-body interactions beyond free dynamics, and the required amount grows with both the protection strength and the amount of information stored. That means fermionic platforms cannot inherit their simulability or their native topological gate set into the fault-tolerant regime without extra experimental machinery.

**Key contributions**
- No-go: code space with d_F ≥ 3 contains no pure Gaussian state (tight — a d_F = 2 code with an entirely Gaussian logical space is constructed).
- Stronger no-go at d_F ≥ 2: no exact universal Gaussian encoding channel and no exact Gaussian non-destructive code-projector measurement, even with classical randomness.
- Quantitative resource bound in the doped-Gaussian model: fidelity bound Eq. (12) and g ≥ ⌊(d_F−3)/(q−2)⌋ + ⌈k/q⌉.
- Approximate-QEC version: quantitative tradeoff between code-space Gaussian fidelity and correctability.
- Fermionic vs. bosonic distillation asymmetry: local Gaussian channels (plus shared randomness) cannot raise EPR fidelity of |ψ_θ⟩^⊗m, yet Gaussian *postselection* distills a perfect EPR pair with probability 2sin²θ.

**How it works** The core argument is two lines: a pure Gaussian state is uniquely fixed by its covariance matrix (weight-2 Majorana correlators), while Knill–Laflamme with d_F ≥ 3 forces all weight-<3 Majorana expectation values to be identical across the code space — so all codewords would collapse to the same state, contradicting rank > 1. The cost bound absorbs the ⌊(d_F−3)/(q−2)⌋ output-nearest non-Gaussian gates into the projector (retaining distance ≥ 3), then uses a compression trick to confine the remaining gates to ≤ qg modes; if that core is smaller than k, the Gaussian complement leaks overlap, and iterating gives the binary-entropy-based fidelity decay. Distillation results use the fermionic Choi/graded-tensor formalism and the Schur-complement covariance update, whose sign differs from the bosonic case — the source of the fermionic/bosonic divergence.

**Why it matters** This is a clean structural statement that non-Gaussianity is to fermionic QEC what magic is to stabilizer QEC, but *unavoidably so*: there is no "free" fermionic code layer. Relevant to Majorana-based architectures (braiding alone is insufficient at the code level), fermionic cold-atom computing, and resource-theory/complexity researchers — the authors flag links to NLTS/NLTM and to classification of interacting fermionic phases.

**Caveats** The no-go concerns *exact* structures (approximate versions are quantitative but the tradeoff constants aren't summarized in the excerpt); the gate-count bound is for exact codeword preparation by unitary doped circuits with bounded generator weight q, not for fault-tolerant protocols with measurement and feedforward, and the Ω(d_F + k) scaling is a lower bound with no matching construction shown. The distillation no-go is proven only for the specific one-parameter Gaussian pair family and product channels, not general LOCC-with-Gaussian-elements.

## 2. 2609.15926

[arXiv:2609.15926](https://arxiv.org/abs/2609.15926) · [SciRate](https://scirate.com/arxiv/2609.15926)



**TL;DR** — The paper resolves a cluster of long-standing open problems by showing that one- and two-message quantum proof systems can be made perfectly complete: $\QIP(2)=\QIP(2)_1$, ${\rm qq}\text{-}\QAM = {\rm qq}\text{-}\QAM_1$, and (over the fixed gateset $\{H,X,\mathrm{Toffoli},S\}$) $\QMA^\calG=\QMA^\calG_1$ and $\QAM^\calG=\QAM^\calG_1$. The two engines are a new "endpoint-inward" turn-halving transformation that folds four messages into two while preserving completeness, and an exactly constructible block-encoded matrix whose kernel certifies yes instances of a verification circuit.

**The big picture** — In a proof system, perfect completeness means an honest prover can convince the verifier with certainty rather than merely with high probability. Classically this is always achievable, and quantumly it was known for protocols with at least three rounds of communication, but the one-message (witness-only) and two-message cases had resisted attack for over two decades, with known black-box approaches provably ruled out. This work closes those cases, for plain quantum witnesses, for two-message interaction, and for the public-coin variants where the verifier's only message is random or consists of halves of entangled pairs. Beyond tidying up the zoo of quantum proof classes, it shows that acceptance-with-certainty is a structural feature of quantum verification rather than a round-number artifact.

**Key contributions**
- Endpoint-inward turn-halving: when both the initial *and terminal* states of a perfectly complete protocol are efficiently preparable, the verifier can run both halves of the interaction in coherent superposition (forward and backward) and accept iff the two branches meet, halving the message count. Soundness degrades as $g_{\rm inward}(s)=(1+\sqrt s)/2$.
- Combining single-qubit exact-half calibration and EPR-pair completion ($g_{\rm EPR}(s)=\tfrac12+\sqrt{s(1-s)}$) yields a 4-message perfectly complete protocol whose terminal state is *exactly* an EPR pair; folding gives $\QIP(2)_1$ with soundness $s_\star<0.993$, then amplified to $1/3$ by parallel repetition.
- For ${\rm qq}\text{-}\QAM$, where the two branches' maximally mixed messages have mismatched dimensions, the endpoint conditions are instead encoded as a fixed-target \textsc{Close Image} instance via a padding channel $\calN_{\rm qq}$ with target $I_\sfF/2\otimes I_\sfZ/2\otimes I_\sfW/\dim\sfW$.
- For $\QMA$: with $M$ the acceptance operator, $B=I-2L\otimes M$ ($L$ a nilpotent clock shift), the matrix $K=\alpha BB^\dagger-\beta|b_z\rangle\langle b_z|$ has nonempty kernel exactly when $\alpha/\beta=\vartheta_z=\sum_j\|(2M)^j|z\rangle\|^2$, which is dyadic with denominator $2^{2hT}$ and hence encodable in polynomial bits. The witness is $(z,m,|\varphi_z\rangle)$; the exact kernel test accepts with probability $1-\|K|\psi\rangle\|^2/16^2$, and $\sigma_{\min}(K)\ge 1/16$ on no instances gives soundness $1-2^{-16}$.

**How it works** — The $\QMA$ construction is a "finite matrix generating function": the forward history vector $\sum_j |j\rangle(2M)^j|z\rangle$ solves $B|\phi_z\rangle=|b_z\rangle$, and the adjoint system's solution lies in $\ker K$ once the prover supplies the (exactly dyadic) normalization $\vartheta_z$ as a classical label. Crucially the verifier never computes $\vartheta_z$ or solves either linear system — it only checks $m$'s range and applies an exact block encoding of $K/16$ built from $V_x,V_x^\dagger$ and reversible comparisons. This label-checking-plus-exact-arithmetic structure is what evades the relativizing obstructions of Aaronson and of Aharonov–Hayden–Wootters.

**Why it matters** — Perfect completeness is the natural normal form for proof systems and is often needed for hardness-of-approximation and completeness results (e.g., quantum $k$-SAT-style problems). The results complete the classification picture for constant-message public-coin quantum protocols, and the turn-halving lemma is a reusable tool: the authors note it also applies to space-bounded two-message systems such as $\QIP_L(2)$.

**Caveats** — The $\QMA$/$\QAM$ results are gateset-dependent ($\{H,X,\mathrm{Toffoli},S\}$, exact dyadic/Gaussian-integer entries), so they are statements about a fixed exact gate model, not gateset-independent. Raw soundness is extremely weak ($<0.993$, $1-2^{-16}$) and relies on existing parallel-repetition machinery for amplification. $\QMA(2)$ remains open — the generating-function argument bounds eigenvalues, not separable values — as does $\QMA_L$, since the precision parameter $d=2hT$ can be polynomial even for logspace verifiers. The turn-halving theorem requires the terminal state be efficiently preparable and the message count be a multiple of four. Concurrent independent work also establishes $\QMA=\QMA_1$ with a similar witness.

## 3. 2609.15842

[arXiv:2609.15842](https://arxiv.org/abs/2609.15842) · [SciRate](https://scirate.com/arxiv/2609.15842)



**TL;DR** The paper shows that the Hamiltonian phase state (HPS) assumptions of Bostanci et al. — recently proposed as a concrete, plausibly OWF-independent instantiation of one-way state generators and pseudorandom state generators — in fact imply the existence of quantum-secure one-way functions, so they cannot instantiate "genuine Microcrypt." The engine is a general framework that builds one-way puzzles from one-way state generators using *"measure first, ask later"* state certification protocols, where structural properties of the certification protocol (classical simulability, efficient post-processing) transfer to properties of the resulting puzzle.

**The big picture** A major hope in quantum cryptography is that secure protocols might exist even in a world where all classical one-way functions are broken. To realize that hope one needs concrete candidate hardness assumptions that plausibly do not secretly encode a classical one-way function; a recent proposal based on the hardness of learning states produced by shallow commuting quantum circuits was the leading candidate. This work shows the candidate fails: if that hardness assumption holds, classical one-way functions provably exist. The same technical machinery is constructive, though — it turns progress on quantum state certification into a recipe for building efficiently verifiable one-way puzzles, and it recasts the failed assumption as a new, inherently quantum foundation for *classical* cryptography.

**Key contributions**
- Definition of "measure first, ask later" state certification protocols with three graded properties: copy efficiency, computational efficiency (efficient classical post-processing), and η-simulability (classical PPT sampling of the measurement outcome distribution within TV distance η given the key).
- New primitives: certifiable / efficiently certifiable / simulable certifiable OWSGs (and PRSGs); log-output certifiable PRSGs imply certifiable OWSGs.
- Certifiable OWSG ⇒ one-way puzzle; efficiently certifiable OWSG ⇒ *efficiently verifiable* one-way puzzle (generalizing Khurana–Tomer's classical-shadow construction to arbitrary certification protocols).
- 1/3-simulable certifiable OWSG with classical KeyGen ⇒ quantum-secure OWF (via distributional OWF → weak OWF → OWF); with negligible η *and* efficient post-processing, a direct and simpler OWF construction bypassing distributional OWFs.
- Main theorem: the Search HPS assumption (weaker than Decision HPS) yields an explicit quantum-secure OWF, by showing the Huang–Preskill–Soleimanifar phase-state certification protocol is computationally efficient and η-simulable with negligible η for phase states.

**How it works** The OWP construction samples a key, prepares many copies of the OWSG output state, and runs the target-independent measurement; the measurement record is the puzzle and the key is the answer, with the certification predicate serving as the verification relation. Soundness of certification gives correctness; hardness follows from OWSG security. If the measurement record can be classically sampled from the key alone, the entire puzzle-sampling procedure becomes classical, which places the puzzle outside Microcrypt by construction.

**Why it matters** It closes off the most concrete proposed route to instantiating Countcrypt, sharpens what a viable candidate must look like (computationally efficient certification that is *not* simulable), and adds HPS to the small set of quantum learning assumptions (alongside learning stabilizers with noise) usable for classical cryptography.

**Caveats** No new evidence is given that any ensemble satisfies "efficient but non-simulable" certification, so the constructive half remains a toolbox without an instantiation. The OWF from HPS rests on an untested, unrelated-to-LWE assumption whose strength is unknown. Simulability thresholds (1/3 vs. negligible η) and the need for classical key generation are essential hypotheses; extensions to quantum post-processing verification are left open.

## 4. 2609.15063

[arXiv:2609.15063](https://arxiv.org/abs/2609.15063) · [SciRate](https://scirate.com/arxiv/2609.15063)



**TL;DR** The authors construct a total Boolean function on $N=\tilde O(n^3)$ bits with certificate complexity $\Omega(n^2)$ but bounded-error randomized query complexity $\tilde O(n)$ and quantum query complexity $\tilde O(\sqrt n)$. Since $\mathrm{C}(f)=O(\mathrm{R}(f)^2)$ and $\mathrm{C}(f)=O(\mathrm{Q}(f)^4)$ hold for all total functions, both separations are optimal up to logarithmic factors, resolving the long-standing question of whether randomized query complexity can be much smaller than certificate complexity.

**The big picture** For total Boolean functions, it has long been known that having short proofs for both answers does not obviously help a randomized algorithm, but nobody knew whether a function could exist whose answer is always cheaply certifiable yet which no fast randomized algorithm can evaluate — or, conversely, whether short certificates always imply fast randomized algorithms up to the known quadratic gap. This paper exhibits a function achieving the maximum possible gap: randomized algorithms can be quadratically faster than the shortest certificates, and quantum algorithms quartically faster. Conceptually, it is the query-complexity analogue of a problem that is easy for randomized computation yet hard to verify with short nondeterministic proofs, and it closes one of the last major open cells in the table of relations between query-complexity measures.

**Key contributions**
- A simple, explicit "tournament champion" function with $\mathrm{C}_0=\Omega(n^2)$, $\mathrm{R}=O(n\log n)$: a near-quadratic $\mathrm{R}$ vs $\mathrm{C}$ separation, matching the known upper bound.
- The same function gives $\mathrm{Q}=\tilde O(\sqrt n)$, a near-quartic $\mathrm{Q}$ vs $\mathrm{C}$ separation (concurrent with Ambainis–Iraids–Kokainis).
- As a byproduct, a self-contained re-proof of the near-quadratic $\mathrm{UC}_1$ vs $\mathrm{C}_0$ separation (Balodis et al.; Pabbaraju).

**How it works** $2n$ countries each field $n$ athletes; every pair of countries runs a race whose top-$n$ finishing order is recorded, with "non-athlete" spoilers marked $\bot$. An athlete is *champion* if it finished ahead of every athlete in all $2n-1$ of its races, was beaten by fewer than $n$ non-athletes in total, and its "proposal card" (a cumulative-sum list of how many non-athletes beat it per race) is well-formatted and consistent with the race records. Uniqueness follows since any two athletes share a race. A 1-certificate is the card plus the $<n$ race prefixes, so $\tilde O(n)$ bits. Hardness of 0-certificates: on the all-$\bot$/all-zero input, any certificate of size $n^2/2$ leaves (by averaging plus Markov) some athlete with untouched card and $<n$ touched positions in its races, which can then be promoted to champion. The randomized algorithm samples race winners per country to get $O(n)$ candidates, runs a pairwise elimination tournament ($O(\log n)$ per comparison), then verifies one certificate. Quantumly, the candidate list stays virtual; elimination becomes a reduction to $\mathtt{SINK}$ on a tournament graph, solved in $\tilde O(\sqrt n)$ queries via the king-finding algorithm of Mande–Paraashar–Saurabh (a sink, when it exists, is the unique king); final verification uses Grover searches plus a binary search over the cumulative-sum card to index the $<n$ positions needing a $\bot$ check.

**Why it matters** This settles a headline open problem in query complexity and completes the picture for $\mathrm{R}$ and $\mathrm{Q}$ versus $\mathrm{C}$. The construction is short and reusable; the $\mathtt{SINK}$/king-finding trick is a nice template for quantum speedups in "find the unique winner" subroutines.

**Caveats** The separations carry polylog slack, so exactly tight constants/exponents (à la Pabbaraju's log-free version) remain open. The hardness is entirely in $\mathrm{C}_0$; $\mathrm{C}_1$ is small, and the function is inherently asymmetric. Inputs are bit strings with $\log n$-bit labels, so the measures are bit-query measures, and the input length $\tilde O(n^3)$ is much larger than $\mathrm{C}$; no attempt is made to optimize $N$ or to obtain corresponding separations for related measures (e.g. block sensitivity, degree).

## 5. 2609.14031

[arXiv:2609.14031](https://arxiv.org/abs/2609.14031) · [SciRate](https://scirate.com/arxiv/2609.14031)



**TL;DR** The paper settles a long-standing open question (posed e.g. in Beigi–Shor-type discussions and by Beigi 2014): there is no dimension bound on the conditioning system in the definition of squashed entanglement. For the two-qubit partially dephased Bell state with coherence parameter strictly between 0 and 1, the authors show that from *any* extension on a $D$-dimensional system one can build an extension on at most $3D+2$ dimensions with strictly smaller conditional mutual information, so $E_{3D+2}(\rho_c)<E_D(\rho_c)$ for all $D$ and the infimum is never attained in finite dimension.

**The big picture** Squashed entanglement is one of the best-behaved entanglement measures — additive, faithful, continuous — but its definition involves minimizing over all possible "conditioning" side systems, with no known limit on how large that side system must be. This makes the quantity notoriously hard to compute, and it was unclear whether the difficulty was fundamental or an artifact of our ignorance. Here a very simple two-qubit mixed state is shown to require ever-larger conditioning systems: every candidate optimizer can be beaten by a modestly larger one. So the optimization genuinely has no finite cutoff, explaining why no algorithm based on truncating the side system can be exact.

**Key contributions**
- First proof that no cardinality bound exists for the squashed-entanglement optimization, via an explicit two-qubit counterexample (a dephased Bell pair).
- A "direct sum symmetrization" step: replacing the two Kraus-like blocks $M_i$ by $P_i=\tfrac{1}{\sqrt2}(\sqrt{M_iM_i^\dagger}\oplus\sqrt{M_i^\dagger M_i})$ leaves the CMI exactly invariant while never decreasing the coherence of the induced reduced state.
- A supporting trace inequality: $2|\mathrm{Tr}(A_0A_1^\dagger)|\le \mathrm{Tr}(\sqrt{A_0A_0^\dagger}\sqrt{A_1A_1^\dagger}+\sqrt{A_0^\dagger A_0}\sqrt{A_1^\dagger A_1})$ (AM–GM plus Cauchy–Schwarz on SVDs).
- A new application of "entropic log-singularity" ($t\log(1/t)$ entropy gain when mixing a rank-deficient state with a full-rank one) to strictly decrease CMI.

**How it works** Purifying a $D$-dimensional extension of $\rho_c$ gives $\ket{\omega}=\ket{00}|M_0\rangle\!\rangle+\ket{11}|M_1\rangle\!\rangle$, and the CMI reduces to $2S(M_0M_0^\dagger\oplus M_1M_1^\dagger)-S(\sum M_iM_i^\dagger)-S(\sum M_i^\dagger M_i)$; strong subadditivity shows it is strictly positive, equal to at least $2(1-h_2(\frac{1+c}{2}))$. After symmetrization the $P_i$ are positive with coherence $c'\ge c$, and the CMI becomes $2S(P_0^2\oplus P_1^2)-2S(P_0^2+P_1^2)$. Three cases: if $c'>c$, write $\rho_c$ as a mixture of $\rho_{c'}$ and the fully dephased $\rho_0$ and use a flag qubit, scaling CMI down by $c/c'$; if $c'=c$ with different kernels, perturb $P_0$ by $\epsilon\ketbra{v}{v}$ on $\ker P_0$ — coherence gains $O(\epsilon)$ while Audenaert–Fannes continuity bounds the CMI change by $O(\epsilon^2\log(1/\epsilon))$; if the kernels coincide, $\phi_{ABG}$ is rank-deficient while $\phi_{AG},\phi_{BG},\phi_G$ are full rank, so mixing in $t\,\rho_c\otimes \mathbb{I}/N$ costs only $O(t)$ in the marginals but gains $b\,t\log(1/t)$ in $S(ABG)$, strictly lowering the CMI.

**Why it matters** This closes a structural question and tells practitioners that finite-dimensional truncations of the squashed-entanglement infimum can only ever give strict upper bounds — no convergent finite-dimensional exact program exists for even this two-qubit state. Relevant to anyone computing or bounding squashed entanglement (quantum key distribution capacities, conditional mutual information / Markov-state approximations, entanglement measures).

**Caveats** The actual value of $E_{\mathrm{sq}}(\rho_c)$ is not determined, nor is the asymptotic scaling of $E_D(\rho_c)$ toward it (no quantitative rate). The factor $3D+2$ is an artifact of the construction and says nothing about optimal growth. The result is for one specific one-parameter family; whether non-attainment is generic for mixed states, and whether an infinite-dimensional separable extension attains the infimum in a limiting sense, remains open. Implications for hardness/computability are suggestive rather than proven here.
