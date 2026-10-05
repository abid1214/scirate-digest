# SciRate Daily Digest — 2026-10-05

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules

[arXiv:2610.03682](https://arxiv.org/abs/2610.03682) · [SciRate](https://scirate.com/arxiv/2610.03682)

*Oscar Higgott, Hasan Sayginel, Francisco J. H. Heras, Zhiyang He, Tomas Jochym-O'Connor, Andrew W. Senior, Lei M. Zhang, Thomas Edlich et al.*

**TL;DR** The authors build hyperbolic surface and color codes out of flat, surface-code-like planar modules (~70–120 qubits each) joined only by sparse, static long-range couplers at module boundaries, so that all negative curvature lives in the inter-module "seams." Circuit-level simulations with SI1000 noise at p=0.1% and 10× noisier seam gates (p_seam=1%) show ~10× fewer physical qubits per logical qubit than the surface code at a 1e-10 logical error rate, extrapolating to >30× (36 physical qubits per logical at distance 20–24), together with a logical-control scheme combining code automorphisms and a modular "ribbon extractor."

**The big picture** High-rate quantum error-correcting codes promise far cheaper fault tolerance than the surface code, but they typically demand dense, long, crossing wiring that is hard to fabricate on a chip. Meanwhile, chips must be split into modules anyway because of yield and size limits. This work shows that the module boundaries are exactly where the small number of exotic connections should go: each chip stays a flat, locally standard patch, and the handful of cables between chips supplies the curved geometry that gives the high encoding rate. The result is close to an order of magnitude or more saving in qubits, using hardware ingredients superconducting labs have already demonstrated separately.

**Key contributions**
- New families of semi-hyperbolic surface codes (qubits on dual-lattice vertices, rotated-surface-code style, balancing X/Z distance and allowing uniform module partitions) and, for the first time, semi-hyperbolic *color* codes via fine-graining triangular hyperbolic tilings with Euclidean hexagonal patches.
- Module partitions derived from the base tiling (quadrilateral/octagon for color codes), making each module a flat Euclidean tile with purely nearest-neighbor internal gates.
- Modular syndrome extraction: Bell-pair + flag measurement in the bulk, GHZ/cat states across seams, and multi-rate schedules measuring seam stabilizers once per three rounds — tolerant of slow, 10× noisier inter-module gates.
- Decoding with a retrained AlphaQubit variant (color codes) and correlated MWPM (surface codes).
- Logical control: symmetric canonical homology bases whose cycles lie in a single automorphism orbit (100 of 104 logicals for [[6400,104,30]]), O(L)-depth SWAP "walking" circuits implementing tiling rotations with one extra coupler seam per module side, and a distance-preserving modular ribbon extractor (~4.5× smaller than the memory, +22% qubits) measuring all 15 nontrivial products of four logicals on a cycle.
- A compiled 50-bit ripple-carry adder benchmark: 21,402 / 28,930 QEC cycles on the [[3600,104,22]] / [[6400,104,30]] memories.

**How it works** A closed hyperbolic surface from a triangle or quadrilateral Coxeter group is tiled, each face replaced by an L×L Euclidean patch; k is unchanged, d grows ~L, n grows ~L², preserving kd²/n while flattening locality. Automorphisms are rotations of the tiling that permute modules, letting one extractor reach hundreds of logical Paulis by teleporting operators under it in ≤6 moves (mean 4.4).

**Why it matters** It reframes modularity from a liability into the enabling resource for high-rate QLDPC codes, and claims better rate *and* distance than the two-gross bivariate bicycle code with mostly 2D-local connectivity — directly relevant to superconducting roadmaps.

**Caveats** The headline >30× figure comes from extrapolation to larger system sizes, not direct simulation. Walking-circuit cost is assessed only through a simplified stabilizer-dislocation model. Ribbon extractors are demonstrated only for quadrilateral-partition color codes. Real-time, sub-distance-parallel decoding remains unsolved, defect tolerance is assumed adaptable rather than shown, and no end-to-end algorithm resource estimate is given.

## 2. Scalable Passive QRAM

[arXiv:2610.03700](https://arxiv.org/abs/2610.03700) · [SciRate](https://scirate.com/arxiv/2610.03700)

*Siddhartha Jain, Alexander M. Dalzell, Connor T. Hann*

**TL;DR** The authors give an explicit time-independent, 4-local, degree-4 Hamiltonian on $O(N)$ qubits whose free evolution for a fixed time $\Theta(\log^2 N)$ implements a bucket-brigade QRAM query exactly, with active control touching only $O(\log N)$ qubits (hence $O(\log N)$ energy per query). The construction maps the bucket-brigade routing schedule onto a layered DAG and applies perfect-state-transfer couplings along it, so the correct output appears deterministically at a known time rather than as a history state; branch-isolation arguments give noise bounds depending on a $\Theta(\log^2 N)$ "footprint" rather than on $N$.

**The big picture** Classical memory is cheap because a query flips only a tiny fraction of the chip and the rest sits idle; quantum memory access, as usually conceived, requires actively pulsing every component because the controller cannot know which branch of the superposition is live, so the energy cost grows linearly with memory size. This paper shows, in principle, how to bake the routing into fixed, pre-manufactured couplings so that a query happens by itself once a single excitation is injected, with cost growing only polylogarithmically in memory size. That removes one of the standing objections to the "free QRAM" assumption underpinning many proposed quantum speedups for data-heavy problems.

**Key contributions**
- First QRAM proposal with polylogarithmic energy per query, resolving the main open problem of the Jaques–Rattew survey; the known $\Omega(N)$-spectral-norm no-go is evaded because the dynamics stay in a sector with only polylog excitations among $\Omega(N)$ modes.
- A circuit-to-Hamiltonian construction that avoids the usual clock pathologies: output fidelity 1 at a *prescribed* time $O(n^2)$, not $1/L$ overlap with a history state.
- Locality 4 and interaction degree 4 simultaneously, via "switch wire" registers that unroll each node's visit counter into unary slices.
- Continuous-time branch isolation, plus three noise theorems: thermal initialization suffices at $\beta g \gtrsim \log\log N + \log(m/\varepsilon)$; static Hamiltonian imprecision tolerance $\lambda_{\rm err}=O(\varepsilon/m^2\log^4 N)$; Lindbladian noise $\varepsilon_m = O(m^3\gamma\log^4 N)$.

**How it works** Address/bus/carrier values are dual-rail encoded; a single active "carrier" excitation doubles as the clock, its position in a layered DAG (many copies of the depth-$n$ tree) marking the step. Each address bit is loaded by descending from the root and deposited in a switch wire, costing $2k$ steps, giving total path length $L=2n^2+O(n)$. Terms come in three flavors — exchange (3-local), route (4-local, advances the switch slice while steering the carrier), leaf read (4-local, memory-controlled flip) — all weighted by the Christandl couplings $J_j=\tfrac{\Omega}{2}\sqrt{j(L-j+1)}$, so every address path, having equal length, completes simultaneously.

**Why it matters** It converts "passive QRAM is probably impossible" into "passive QRAM is an engineering problem," with concrete hardware targets: 4-body couplings are natural for Josephson elements, and a back-of-envelope 300 mm wafer estimate reaches $n=32$ (~500 MiB) at 14 mK with <10% query error.

**Caveats** Not *strongly* passive: fault-tolerant integration via distillation–teleportation still costs $\Omega(N)$ classical work, so the cheap-QRAM assumption is not fully vindicated. Long-range two-body terms are unavoidable and no qubit layout is given; the $\log^2$ runtime reflects inability to pipeline. Memory qubits are assumed noiseless and classical, and $\Omega(N)$ fabrication cost remains.

## 3. Unitary complexity in polynomial space

[arXiv:2610.03705](https://arxiv.org/abs/2610.03705) · [SciRate](https://scirate.com/arxiv/2610.03705)

*William Kretschmer, Ewin Tang*

**TL;DR** If quantum commitments (equivalently EFI pairs) exist, then either the unitary synthesis problem has no polynomial-time solution or BPP ≠ NEXP — so any unconditional construction of computationally secure quantum cryptography must settle a longstanding classical complexity question. The engine is a dichotomy: every unitary in unitaryPSPACE is either unsynthesizable relative to *any* classical oracle, or synthesizable in polynomial time with an NEXP-witness-search oracle. Along the way the paper rebuilds the definitions of unitaryP/unitaryPSPACE from first principles and proves unitaryPSPACE equals the class of unitaries with space-efficiently computable matrix entries.

**The big picture** Quantum cryptography might survive even in a world where all classical cryptography is broken, and so far nobody has shown that building a secure quantum commitment scheme requires proving any hard classical lower bound. This work closes part of that gap: it shows that an unconditional proof of quantum cryptographic security would have to resolve one of two decades-old open questions about classical computation. It also puts the young field of "unitary complexity theory" — which treats quantum transformations, rather than yes/no questions, as the objects of study — on a cleaner axiomatic footing, showing that earlier proposed definitions let uncomputable information hide in tiny phases and leak out under composition.

**Key contributions**
- Main dichotomy lemma: ∀𝒰 ∈ unitaryPSPACE, either 𝒰 ∉ unitaryP^ALL, or 𝒰 ∈ unitaryP^FNEXP. Hence a halting oracle is either useless or vast overkill for any such unitary.
- Corollaries: unitaryALL = unitaryP^ALL ⟹ unitaryPSPACE ⊆ unitaryP^FNEXP; a mere *oracle* separation unitaryP^PSPACE^L ≠ unitaryPSPACE^L would imply unitary synthesis fails or NC ≠ NP (non-relativizing).
- New definitions requiring polylog(1/ε) time/space scaling, ε uniform and independent of n, FPTEAS-computable gate entries, and the full oracle set U, U†, U*, Uᵀ (+controlled).
- unitaryPSPACE = unitaries whose entries admit an FPSEAS; consequently generic garbage erasure in PSPACE (up to global phase).
- Exact relations between clean and garbage-allowing classes: 𝒰 ∈ projective-unitaryP ⟺ 𝒰⊗𝒰† ∈ unitaryP ⟺ 𝒰⊗𝒰* ∈ unitaryP; and 𝒰 ∈ unitaryP ⟺ c-𝒰 ∈ projective-unitaryP.
- A unitary oracle relative to which garbage *cannot* be erased, via the nonexistence of a continuous section PU(N) → U(N).

**How it works** The dichotomy is a clean NEXP-verification argument: if 𝒰 ∈ unitaryP^L for some language L, an NEXP machine guesses L's truth table on polynomial-length inputs, brute-forces the oracle circuit's matrix in exponential time, and checks it against 𝒰's entries — computable in PSPACE ⊆ EXP by the entrywise characterization. Querying a valid witness then gives unitaryP^FNEXP. The entrywise characterization uses BQPSPACE = PSPACE plus amplitude estimation one way, and state synthesis plus Rosenthal's column-constructor-to-unitary compiler the other. Garbage-erasure identities exploit running the implementing circuit backwards on a known eigenstate (|0⟩ for c-U, the maximally entangled state for U⊗U*). The crypto link: unitaryPSPACE implements the optimal Helstrom measurement for an EFI pair, so unitaryP = unitaryPSPACE breaks it.

**Why it matters** This is the first result tying quantum commitments to concrete classical open problems, constraining the "Microcrypt" program, and it explains why a sought-after oracle with P = PSPACE but unitaryP ≠ unitaryPSPACE has resisted construction. The definitional work is likely to become the standard reference for unitary complexity.

**Caveats** The conclusion is a disjunction, not a lower bound — it's still consistent that unitary synthesis fails and commitments exist with no classical consequence. FNEXP is not known to be stronger than PSPACE, so "effective synthesis" remains slightly off. Classes are defined for total unitaries, not the partial isometries used in Uhlmann-type work, and the polylog(1/ε) requirement excludes algorithms (tomography, FPTASes) that prior definitions captured. Whether projective-unitaryP = unitaryP up to phase is left open, with no candidate separating language.

## 4. Hamiltonian locality testing and certification do not achieve the Heisenberg limit

[arXiv:2610.03205](https://arxiv.org/abs/2610.03205) · [SciRate](https://scirate.com/arxiv/2610.03205)

*Francisco Escudero Gutiérrez, Junseo Lee, Sebastian Zur*

**TL;DR** This paper proves the first Ω(1/ε²) total-evolution-time lower bounds for natural Hamiltonian testing problems in the forward-only (no inverse, no controlled access) time-evolution access model, showing that Hamiltonian locality testing and Hamiltonian certification in normalized Frobenius distance *cannot* reach the Heisenberg 1/ε scaling. The same technique reproves the Ω(1/ε²) lower bound for amplitude estimation with forward-only queries, now in the stronger continuous-time (fractional-query) model. All three follow from one technical result: there is an ensemble of random diagonal Hamiltonians with mean-zero, variance-ε² entries that needs Ω(1/ε²) evolution time to distinguish from the zero Hamiltonian.

**The big picture** A central goal in characterizing quantum hardware is to learn or verify the interactions governing a device by letting it evolve and measuring the outcome, and a large literature has shown that clever protocols can reach the optimal precision-versus-time tradeoff dictated by quantum metrology. This work shows that limit is not universal: for two natural verification tasks — checking whether an unknown interaction only couples few particles at a time, and checking whether it matches a known target — the metrological speedup is provably unavailable when you can only run time forward. The proof imports the adversary method from quantum query complexity into the continuous-time Hamiltonian setting, giving the field a new lower-bound tool where previously essentially none existed beyond the metrological bound.

**Key contributions**
- Matching Ω(1/ε²) lower bound for k-local testing (for k ≤ n/8, ε² ≥ 24·2⁻ⁿ), matching Kallaugher–Liang's upper bound.
- Matching Ω(1/ε²) for certification against a known target (ε² ≥ 3·2⁻ⁿ⁻¹), answering negatively Bluhm et al.'s question of whether locality assumptions were an artifact.
- Ω(1/ε²) for amplitude estimation in the continuous-time forward-query model, strengthening Tang–Wright.
- Adaptation of the continuous-time adversary method to forward-only Hamiltonian evolution, with an explicitly constructed progress function rather than an invocation of a general theorem.

**How it works** Diagonal Hamiltonians with Boolean entries correspond exactly to fractional phase queries, motivating query-complexity machinery. The hard ensemble has iid entries drawn from the spectral measure ν_ε of a block operator J_ε = [[0, ε⟨b|],[ε|b⟩, M]] acting on C⊕L²([−½,½]), where M is multiplication by ω and b a smooth normalized bump. This gives E[h]=0, E[h²]=ε², |h|≤1, so the ensemble is ε-far with constant probability. Crucially, the spread-out spectrum kills the easy attack: the ±ε ensemble satisfies U_H(π/ε)=−I and is distinguishable in O(1/ε) time by a Hadamard test (controlization is free). The adversary argument purifies the randomness into registers, and uses the two decay estimates ∫₀^∞|⟨b|e^{−iMτ}|b⟩|dτ ≤ C and ∫₀^∞|⟨b|e^{−iMτ}|r⟩|²dτ ≤ C_obs‖r‖² (from integration by parts and Plancherel) to build a correction operator G from convolution operators O, R, D. The progress function P(t)=1−Re⟨Ψ_Z|Ψ_F⟩+¼⟨Ψ_F|I⊗G|Ψ_F⟩ starts at 0, must reach Ω(1), and has derivative O(ε²λ(t)).

**Why it matters** Settles the complexity of Hamiltonian locality testing after several rounds of upper bounds, and delineates where Heisenberg scaling genuinely lives: structure (locality/sparsity) in *both* the target and the unknown, not just forward access, is what buys 1/ε.

**Caveats** Bounds require ε not exponentially small (1/ε = 2^{O(n)}); the exact constant c such that ε = 2^{−cn} still works is open, and the concurrent Fourier-analytic work of Allen et al. obtains Ω(√d/ε) in the high-precision regime, which the authors say their method can also recover. Hard instances are diagonal, so the bounds say nothing about restricted (e.g. geometrically local) Hamiltonian classes; sparsity testing remains open.

## 5. On The Complexity of Redundancy-Free Quantum Hamiltonians

[arXiv:2610.03697](https://arxiv.org/abs/2610.03697) · [SciRate](https://scirate.com/arxiv/2610.03697)

*Matthew B. Hastings, Alexander Schmidhuber*

**TL;DR** This paper maps the complexity landscape of "redundancy-free" Hamiltonians — sums of terms where any product containing a term an odd number of times is traceless (e.g. independent Pauli products) — and shows the controlling parameter is $\kappa=\beta^2 d$ ($d$ = degree of the anticommutation graph), not $\beta d$ as for generic Hamiltonians. A convergent polymer expansion gives a classical algorithm for the partition function at small $\kappa$, while at large $\kappa$ approximating the partition function is NP-hard (and ground-state energy estimation is QMA-complete), via a new "anticommutation glass" in which frustration comes purely from anticommutation.

**The big picture** A recent quantum algorithm splits the hard problem of preparing thermal states of quantum systems into a classical decoding step and the preparation of a special purified thermal state whose only structure is which terms commute or anticommute. How hard that second step is was the main open question. This work shows that stripping away all algebraic redundancy among the terms genuinely buys you something: the easy regime extends to temperatures quadratically lower than for generic systems, but not further — beyond that threshold, anticommutation alone is enough to manufacture glassy frustration and worst-case hardness.

**Key contributions**
- Polymer (cluster) expansion whose convergence hinges on every term appearing an even number of times, yielding convergence at $\beta\sim 1/\sqrt{d}$ rather than $1/d$; truncation at total support $W_{\rm tot}\sim\log(n/\epsilon)/\log(1/\kappa)$ gives runtime $O(n(n/\epsilon)^{O(\log d/\log \kappa^{-1})})$.
- The *anticommutation glass*: two commuting families ($X_i$ and $D_i=\prod_j Z_j^{A_{ij}}$, $A$ invertible over $\mathbb F_2$) with two competing "basins", supported by series expansion, path-integral QMC (with a non-local move flipping a single $Z$-type operator; hysteresis observed at $n=200$), and a toy two-level model where collective hopping/diagonal splitting $\sim\kappa^{-1/2}$.
- Formal NP-hardness: glasses on cubic graph vertices, ancilla-dressed couplings encoding MAXCUT; explicit matrices $A_v(x,y)=\delta_{xy}+\mathrm{tr}_{\mathbb F}(\alpha_v xy)$ over $\mathbb F_{4^s}$ with a 4-coloring; $n/2-1\le d\le 7n$, $\beta=\Theta(d^{-1/2})$, factor-2 approximation of the normalized $\mathcal Z$ is NP-hard.
- QMA-completeness of ground-state energy for redundancy-free Hamiltonians.
- Subexponential quantum TFD preparation at small $\kappa$; plus, of independent interest, a Feiguin–Klich-based polynomial-time TFD preparation for *general* degree-$d$ Hamiltonians at $\beta\lesssim 1/d$ with no lattice-dimension dependence (unlike prior work).
- HDQI robustness: pilot-state infidelity and decoder failure add ($D_{\rm tr}\le\sqrt{\varepsilon_p}+\sqrt{2r/\delta}$ for random signs), and $\mu_\beta$ is local-stochastic with rates $(\beta J_i/2)^2$ — quadratically better in $\beta$ than the generic polynomial-filter scheme.

**Why it matters** It identifies the precise temperature threshold at which HDQI's quantum step stops being easy, delimiting where the algorithm can plausibly give advantage, and introduces a clean model of purely anticommutation-induced glassiness.

**Caveats** The lower-bound construction needs degree growing with block size, so hardness is at $\beta=\Theta(d^{-1/2})$ with block $n$ fixed independent of graph size; the small-$\kappa$ classical algorithm is polynomial only for fixed $d,\kappa$. The glass's two-basin physics rests partly on numerics that visibly fail to equilibrate, and no polynomial-time quantum TFD algorithm is obtained at $\beta\lesssim 1/\sqrt d$ — a gap left open, along with whether effective *quantum* Ising models can be encoded.
