# SciRate Daily Digest — 2026-09-04

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Quantum thermalization achieves optimal approximate quantum error correction

[arXiv:2609.04121](https://arxiv.org/abs/2609.04121) · [SciRate](https://scirate.com/arxiv/2609.04121)

*Aditi Venkatesh, Richard R. Allen, Saúl Pilatowsky-Cameo, Bingtian Ye, Soonwon Choi*

**TL;DR** The authors show that the late-time states of a generic thermalizing many-body Hamiltonian form an approximate quantum error-correcting code, and that this code is asymptotically optimal: numerically extracted erasure thresholds for several ergodic Hamiltonians collapse onto the universal curve p⋆ = (s−r)/2s (s = thermal entropy density, r = rate), which at infinite temperature is the quantum Singleton bound and at finite temperature is proven to be the entropic quantum Singleton bound. They also introduce "Scrooge codes" — a Gibbs-state analogue of Haar-random codes — and prove these saturate that entropic bound.

**The big picture** Chaotic quantum systems naturally hide the memory of their initial conditions from any local observer, which is exactly what an error-correcting code does on purpose. This work makes that analogy operational by treating time evolution itself as the encoder and asking, quantitatively, how much information can be protected against how much loss. The answer is that thermalization is not merely a decent encoder but an asymptotically optimal one at every temperature, hitting the same fundamental limits as idealized random encodings that would take exponentially deep circuits to build. It also pins down exactly how conservation laws degrade this protection: they leak only classical information, and only once codeword charges differ by more than typical thermal fluctuations.

**Key contributions**
- Rigorous observation: if all codespace states are ε-thermalized on region E, the code is erasure-correctable with diamond error 2√(ε·min{K,2^|E|}).
- A worst-case-from-average-case reduction: uniform average-case correctability against exponentially many noise channels yields a single subcode of the same asymptotic rate that is worst-case (diamond-norm) correctable, so decoupling I(E:R) suffices as a certificate.
- Empirical universal rate–distance–entropy law p⋆ = (s−r)/2s, Hamiltonian-independent.
- Scrooge codes (K = 2^{rN} Scrooge samples, Löwdin-orthonormalized) and a theorem that they decouple for all p < p⋆, saturating the entropic Singleton bound under an "entropy-concentrated spectrum" assumption.
- Identification of energy leakage as purely classical: I(E:R), energy-measurement-restricted mutual information, and the Jensen–Shannon divergence of local-energy distributions coincide for p ≤ 1/2; correctability survives energy gaps o(√N).

**How it works** Exact-diagonalization evolution (N = 12–20, mixed-field Ising plus two other chaotic models) of energy-window-matched orthogonal product states to t ∼ N²/J, with finite-size scaling collapses of I(E:R) yielding p⋆ (e.g. p⋆ ≈ 0.417 at r = 0.1667, ν ≈ 1). Analytically, a mixture of K Scrooge codewords reduces to a single Scrooge state with parent g_β ⊗ I_K/K, shifting the Page curve by rN qubits with slope s; the turnover of S(B) sets p⋆, with crossover width O(1/sN).

**Why it matters** It supplies a code-theoretic, operationally meaningful diagnostic of ergodicity, complements ETH-based codes with dynamically preparable codewords, and delivers a new optimal finite-temperature AQEC family. Relevant to quantum chaos, holography-adjacent entropy arguments, and AQEC theory.

**Caveats** Numerics reach only N ≤ 20, so the universal curve is an extrapolation from modest finite-size collapses; the optimality theorem needs entropy-concentrated spectra for the relevant reduced Gibbs states and s(β) > 0. Only erasure noise is treated; the average-to-worst-case reduction sacrifices a subextensive number of logical qubits. Timescales for the onset of correctability (thermalization vs. scrambling) are left open, as are non-Abelian symmetries and hydrodynamic slow modes.

## 2. On the geometry and typicality of quantum magic

[arXiv:2609.03944](https://arxiv.org/abs/2609.03944) · [SciRate](https://scirate.com/arxiv/2609.03944)

*Zhenhuan Liu, Z-Wen Liu*

**TL;DR** The authors prove a dimension-independent purity threshold for magic-freeness: every $n$-qubit state with $\mathrm{Tr}(\rho^2)\le 1/(d-a_*)$, $a_*=0.458327\ldots$, is a mixture of stabilizer states — within a constant of the conjectured optimum $1/(d-1/2)$. Feeding this inradius into asymptotic convex geometry, they pin the stabilizer polytope's volume radius to $\Theta(1/d)$ up to a $\log d$ factor, locate the magic/no-magic transition for random induced states at environment dimension between $\Omega(d^2/\log^2 d)$ and $O(d^2)$, and lift the facet-count lower bound from $\exp[\Omega(\log^2 d)]$ to $\exp[\Omega(d^2/\log^2 d)]$.

**The big picture** The set of quantum states with no "magic" — the resource that stabilizer circuits cannot produce and that fault-tolerant computers must distill — is a convex polytope whose shape has been poorly understood despite its central role. This work measures that shape quantitatively: how large a ball of nearly maximally mixed states is guaranteed magic-free, how much total volume the magic-free set occupies, and how many linear inequalities are needed to describe it exactly. The answers show the polytope is close to as geometrically complex as any object with that many corners in that many dimensions can be, and that magic in a randomly generated subsystem survives coupling to an environment roughly twice its own size — parametrically more robust than entanglement.

**Key contributions**
- Universal purity bound $1/(d-a_*)$ for magic-freeness with $a_*=0.458327\ldots$, closing the gap to the conjectured $1/2$ to a dimension-independent constant; removes a conjectural assumption in prior work on single-copy magic detection hardness (requires $\widetilde\Omega(k)$ observables).
- Volume radius of the centered polytope determined to within $O(\log d)$: between $\Omega(1/d)$ and $O(\log d/d)$; contrast with separable states, where inradius $\Theta(1/d)$ and volume radius $\Theta(d^{-3/4})$ differ parametrically.
- Sharp threshold for magic in Haar-induced states at $k_\star\in[\Omega(d^2/\log^2 d),\,O(d^2)]$, versus $d^{3/2}$ for entanglement — hence a broad regime of separable-but-magical typical states.
- Facet count $\exp[\Omega(d^2/\log^2 d)]\le F_d\le \exp[O(d^2\log^2 d)]$: doubly exponential in $n$.

**How it works** The inradius reduces to bounding $Q_d=\max\mathrm{Tr}(A^2)$ over trace-one operators with nonnegative overlap on all stabilizer states (the polar body). A "Pauli compression" recursion restricts $A$ to the $\pm1$ eigenspaces of a Pauli via Clifford isometries, relating $Q_d$ to $Q_{d/2}$; summing over all non-identity Paulis yields $d(q-M)\le 2t-Mq-1$ with $t=\mathrm{Tr}(A^3)$, closed using a sharp two-value spectral bound on the third moment. Starting from the exact $Q_4=2$, exact-rational iteration to $d=2^{24}$ plus a geometric-series tail bound gives $Q_d<2.181847$ uniformly. The global results then combine the Carl–Pajor few-vertex volume estimate ($\log N_d=\Theta(\log^2 d)$ vertices in dimension $d^2-1$), Bourgain–Milman reverse Santaló, Urysohn's inequality, and the Aubrun–Szarek–Ye Gaussian approximation for induced measures; the small-$k$ regimes ($k<d$, $d\le k<d\log d$) are handled separately by rank/support and density-comparison arguments.

**Why it matters** Gives sharp, usable criteria for when mixed states are certifiably magic-free (relevant to noise thresholds, thermal states, benchmarking) and formalizes why exact facet-based magic witnesses are hopeless. The magic-vs-entanglement threshold separation is a concrete statement that magic outlives entanglement under generic mixing.

**Caveats** The remaining constant gap ($a_*$ vs. $1/2$) is unresolved; $k_\star$ and $\log F_d$ are each fixed only up to polylog factors. Results are qubit-specific (odd prime qudits behave differently: exact inradius corresponds to $1/(d-1/d)$). The threshold is for the Haar-induced ensemble, not physically motivated ensembles (Gibbs states, local circuits), which the authors flag as open. The inradius proof leans on a finite machine-checked rational certificate up to $d=2^{24}$.

## 3. Quantum low-density lattice codes

[arXiv:2609.03021](https://arxiv.org/abs/2609.03021) · [SciRate](https://scirate.com/arxiv/2609.03021)

*Timo Hillmann, Jens Eisert, Francesco Arzani*

**TL;DR** The authors port classical low-density lattice codes (LDLCs) — the lattice analogue of LDPC codes — into the multimode GKP setting, arguing that decodability should dictate code design rather than the reverse. A "magic square" LDLC rescaled to satisfy the integer symplectic Gram condition gives valid but exponentially over-encoded GKP codes; a dimension-reduction procedure that appends two dense rows to the sparse generator yields single-qubit codes whose Euclidean distances and Gaussian-displacement logical error rates match or beat rotated surface codes concatenated with hexagonal GKP at equal (or even smaller) mode count. Separately, they show a fully analog, linear-time message-passing decoder gives thresholds for GKP-repetition and small GKP-simplex codes.

**The big picture** Encoding a qubit into an oscillator using grid states is equivalent to choosing a lattice in phase space, and correcting errors is equivalent to finding the nearest lattice point — a problem so hard it underpins post-quantum cryptography. Most work sidesteps this by gluing single-mode grid codes onto ordinary qubit codes, which throws away some of the continuous information the hardware provides. Here the authors invert the design order: they build lattices that a fast approximate nearest-point algorithm is known to handle well, then check whether the resulting quantum codes are any good. They find such codes can outperform standard concatenated constructions at the same number of oscillators, and that a natively continuous decoder is competitive with hybrid ones.

**Key contributions**
- A construction of GKP codes from randomly generated magic-square LDLCs (choose degree a perfect square, set the generator to the rescaled sparse parity-check matrix), plus a variant from qudit CSS codes via a rescaled Construction A.
- A dimension-reduction algorithm using the symplectic canonical form and invariant factors, splitting one factor across two rows to collapse an exponentially large logical dimension down to a single qubit while raising distance; implemented in exact rational arithmetic.
- Numerical evidence that reduced codes at 15–17 modes beat a 25-mode surface-code baseline in Monte-Carlo CVP-decoded logical error rate, with the gap widening at low noise.
- An OSD-style post-processor for lattice decoding: pick the least-reliable coordinates, LLL-reduce the induced sublattice basis, and do a bounded search around the Babai solution.
- Two decoder implementations (quantized and Gaussian-mixture with list-sphere variable-node updates) released as `LatticeDecoder.jl`/`SymplecticGKP.jl`.

**Why it matters** Native, non-concatenated GKP codes have been largely unexplored precisely because decoding is intractable; this gives a concrete recipe and open tooling. The co-design message — that efficient decoding should be a design constraint, not an afterthought — is relevant beyond bosonic codes.

**Caveats** The reduced codes are *almost*-LDLC: two dense checks create short cycles, and no message-passing decoder was found that works on them, so the distance/error-rate comparisons rely on brute-force CVP feasible only to about 17 modes (dual bases have orthogonality defect ~10¹¹). The performance claims are therefore about intrinsic code quality, not an operational decoder. Noise is idealized i.i.d. Gaussian displacement, single-shot, with no finite-squeezing or measurement error. Sommer's convergence theory does not extend to the irregular quantum case; the analog decoder shows error floors traced to approximate message representation, and the authors state they do not yet understand how to make it work broadly.

## 4. Distinctness threshold for pseudorandom unitaries

[arXiv:2609.03065](https://arxiv.org/abs/2609.03065) · [SciRate](https://scirate.com/arxiv/2609.03065)

*Asad Raza, Jens Eisert, Bill Fefferman*

**TL;DR** The paper isolates "distinctness" — concentration of the $t$-query output on the collision-free subspace for *arbitrary* (including entangled) inputs — as a necessary condition for any pseudorandom unitary in the parallel forward-query model, and shows it is strictly weaker than being a unitary or even a state 1-design. Replacing the Clifford/2-design layer in the $PFC$ construction with such distinct-but-non-design ensembles (a depth-1 layer of single-qubit Cliffords, or a ternary-phase-times-Hadamard ensemble) still yields non-adaptive PRUs, and failure of distinctness gives a Bell-state distinguisher that rules out phase–Hadamard PRU candidates whose phase functions have codomain $K \le N/n^{\omega(1)}$.

**The big picture** Quantum pseudorandomness comes in a statistical flavour (ensembles that mimic truly random dynamics to a fixed number of copies) and a computational flavour (ensembles that only fool efficient observers). Every known construction of the computational object bolts a cryptographic layer on top of a statistically random layer, leaving open whether the statistical ingredient is truly needed. Here the authors identify a much weaker, operational property — roughly, that repeated queries almost never produce colliding measurement outcomes even on entangled inputs — prove it is unavoidable for computational pseudorandomness, and show it alone suffices to drive existing constructions. This separates the two notions of randomness, cheapens constructions to constant depth, gives a simple test for ruling out candidate constructions, and clarifies which physical resources pseudorandomness really demands.

**Key contributions**
- Proof that any PRU must be $\negl(n)$-distinct on efficiently preparable inputs (weakest query model ⇒ applies a fortiori to stronger ones).
- Equivalence of $\delta$-distinctness with "entangled anticoncentration" (2-copy collisions on arbitrary bipartite inputs) for $t=\poly(n)$, $\delta=\negl(n)$; one direction is exact, the reverse loses a factor $t^2$.
- An explicit $O(t^2/N)$-distinct ensemble, $HF_\mathbb{C}$ (4-wise independent ternary phase, then Hadamard), that is *not even a state 1-design* ($HF|0\rangle=|+\rangle$) — matching the design-based bound and showing anticoncentration↔state-2-design equivalence is architecture-dependent.
- Depth-1 PRU layer: a tensor product of single-qubit Cliffords is $(2/3)^n$-EAC, so $PF\bigotimes_i C_i$ is a PRU, saving the $\log n$ depth of the global Clifford.
- Imaginarity $\ge 1-\delta$ and coherence $\ge \ln(1/\delta)$ follow already from distinctness, recovering Haug et al.'s PRU resource bounds at a weaker level.
- "Bell overlap" as the true obstruction to real-valued pseudorandomness: real ensembles ($PF_\mathbb{R}C_\mathbb{R}$, $PF_\mathbb{R}HF_\mathbb{R}$) are PRUs on all inputs with Bell overlap $\le N/n^{\omega(1)}$ — covering all separable states (answering Brakerski–Magrafta), all PPT states, and many NPT/maximally entangled ones (beyond Grevink et al.).
- No-go: JLS's alternating phase–Hadamard conjecture fails for phase functions $[N]\to[K]$ unless $\log K > n-\omega(\log n)$.

**How it works** Necessity is a contrapositive: a collision above negligible probability is itself an efficient distinguisher from Haar (where collisions are $O(t^2/N)$). The projector chain $\Pi^{\mathrm{eq}}_{ij}\preceq\overline{\Pi}^{\mathrm{dist}}\preceq\sum_{i<j}\Pi^{\mathrm{eq}}_{ij}$ gives the two-way distinctness/EAC translation. Distinctness of $HF$ is a 2-copy $F$-twirl computation with cube roots of unity, derandomized via Zhandry's $2t$-wise independence theorem. Sufficiency plugs into Metger–Poremba–Sinha–Yuen: $\|\mathcal{M}^{(t)}_{PFD}-\mathcal{M}^{(t)}_{\mathrm{Haar}}\|_\diamond = O(\sqrt\delta + t^2/N)$ for any $\delta$-distinct $D$. Resource bounds come from the maximally entangled witness: $\mathrm{tr}[\Pi^{\mathrm{eq}}\mathbb{E}U^{\otimes2}\Phi U^{\otimes2\dagger}]$ evaluates to $|\mathrm{tr}[U^\dagger U^*]|^2/N^2$, so distinctness directly forces imaginarity. The JLS obstruction is a finer analysis of Bell-in/Bell-out projection, exploiting that the Bell projector lies outside the distinct subspace and that small-codomain phases fail to suppress it.

**Why it matters** This gives a modular decomposition of PRU security: a cheap collision-suppression layer plus classical cryptography, rather than "a design plus cryptography". Practically it removes a $\log n$ depth factor and yields real-valued PRUs on physically natural input classes; conceptually it supplies a cheap, checkable no-go test and a clean separation between statistical and computational quantum pseudorandomness. Relevant to cryptographers, complexity theorists studying random-circuit sampling/anticoncentration, and anyone using designs where only collision suppression is needed.

**Caveats** All results are confined to non-adaptive, forward-query security; adaptive/inverse-access analogues of distinctness are open. Distinctness is necessary and (within $PFC$-type templates) sufficient, but not shown sufficient in general. The constructions do not extend past $t\approx\sqrt N$ (gentle-measurement loss in the $PFC$ analysis), where Brakerski–Yuen's collision attack applies. The JLS result does not refute the original conjecture ($K=N$). Real PRU security is input-restricted, and whether the new distinct ensembles are "non-plussed" distinct (needed to drop $F$) is unresolved.

## 5. Computing with qLDPC Codes by Climbing the Chain Map Hierarchy

[arXiv:2609.02999](https://arxiv.org/abs/2609.02999) · [SciRate](https://scirate.com/arxiv/2609.02999)

*Rahul Sahay, David M. Long, Vedika Khemani*

**TL;DR** The authors show that the space of physical circuits implementing a given logical Clifford (or higher Clifford-hierarchy) gate between CSS codes is itself the space of chains of an auxiliary chain complex — which turns out to be just the tensor product (hypergraph product) of the constituent code complexes. Logical gate classes are then homology classes, "Clifford stabilizers" are boundaries (null-homotopies), and deforming a logical Pauli in the auxiliary code deforms the gate circuit. Using this they find constant-depth implementations of the *full* Clifford group on the 2D toric code (including addressable single-qubit Hadamard/S and intra-block CZ/CNOT) and addressable CCZ on any triple of logical qubits of 3D toric code blocks.

**The big picture** Quantum error-correcting codes that pack many logical qubits into one block are now well understood as memories, thanks to a homological language in which logical operators are homology classes and equivalent implementations differ by boundaries. Logical *gates*, by contrast, have been a grab-bag of ad hoc constructions — transversal tricks, folding, code surgery, cup products — with no unifying organizing principle. This work extends the homological picture to gates at every level of the Clifford hierarchy, so that finding a low-depth implementation of a desired logical operation becomes the familiar exercise of deforming a logical operator in a larger auxiliary code. The immediate payoff is new gates on codes as simple and well-studied as the toric code, where previously even a single-qubit Hadamard required elaborate ancilla scaffolding.

**Key contributions**
- The *chain map complex* $\mathcal{C}^{[2]}$: degree-0 chains are all CZ-type circuits between codes $C_\bullet,D_\bullet$; cycles are chain maps (code-space-preserving gates); boundaries are logically trivial "Clifford stabilizers" (null-homotopies); $H_0$ labels logical actions. Crucially $\mathcal{C}^{[2]}\cong D_\bullet\otimes C_\bullet$.
- Iteration up the Clifford hierarchy: $\mathcal{C}^{[3]}\cong D_\bullet\otimes C_\bullet\otimes B_\bullet$ for CCZ-type gates, and so on — the *chain map hierarchy*.
- New transversal gates: entire logical Clifford group on any number of 2D toric code blocks, including within one block; addressable CCZ on any triple of logical qubits across 3D toric code blocks; addressable Clifford and non-Clifford gates in fracton code families with extensively many logicals.
- A universal parameterization of cup products and cup-product cohomology invariants, yielding cup products outside existing parameterizations; unification with code surgery/measurement gadgets.
- An informal extension of Bravyi–König no-go arguments to nonlocal constant-depth circuits.

**How it works** A Clifford acting between two CSS codes is a chain map $\phi_\bullet:C^\bullet\to D_\bullet$; the degree-0 component $\phi_0$ literally lists the physical CZ pairings, and sparsity of $\phi_0$ means constant depth. Dropping the commutativity requirement gives the full graded vector space of maps (left-diagonal, downward, right-diagonal), with a boundary operator $\partial^{[2]}_1(Q)=\partial Q+Q\mathrm{d}$; its kernel at degree 0 is exactly the chain-map condition. Under the isomorphism to the tensor product, logical CZ gates on two 2D toric codes are read off as sheet-like logical $Z$ operators of the 4D toric code: a supported plaquette at $(x,y,z,w)$ means a physical CZ between qubit $(x,y)$ of one block and $(z,w)$ of the other. "Tenting" the sheet — an ordinary stabilizer deformation — reduces a distance-scaling-depth gate to constant depth and yields an addressable logical CZ.

**Why it matters** This gives qLDPC gate design the same tool-chest (homological products, deformation, distance intuition) that made memory design tractable, and turns "does a transversal gate exist?" into a homology computation. Relevant to anyone designing fault-tolerant architectures for high-rate codes or hunting addressable non-Clifford gates.

**Caveats** The framework covers $\mathsf{C}^{\ell}Z$/$\mathsf{C}^{\ell}X$-type gates and certain intra-block gates (e.g. $S$), not arbitrary logical unitaries; sparsity of a representative cycle (hence constant depth) is not guaranteed by homology alone and must be found by search/deformation. The no-go generalization is explicitly informal. Fault-tolerance/threshold behavior of the new toric-code Clifford and 3D CCZ gates — e.g. error spreading from nonlocal constant-depth circuits — is not analyzed in the excerpt.
