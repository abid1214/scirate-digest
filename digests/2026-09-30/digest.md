# SciRate Daily Digest — 2026-09-30

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Towards verifiable quantum advantage with random circuits: Observables that survive concentration

[arXiv:2609.37890](https://arxiv.org/abs/2609.37890) · [SciRate](https://scirate.com/arxiv/2609.37890)

*Antonio A. Mele, Francesco A. Mele, Jarrod R. McClean, Thomas E. O'Brien*

**TL;DR** The paper proves that out-of-time-order correlators in local random circuits retain inverse-polynomial circuit-to-circuit variance at system-scale depths, ruling out concentration as an obstruction to OTOC-based verifiable quantum advantage. For 1D Haar brickwork circuits it pins the first-order OTOC transition at depth $d_\star = 5n/3$ with diffusive width $\Theta(\sqrt n)$, variance $\Omega(n^{-1/2})$, and $\Theta(n^{3/2})$ individually influential gates confined to an "eye"-shaped spacetime region — which in turn yields a $\mathrm{poly}(n)\,2^{O(\sqrt{n\log n})}$ classical algorithm for the infinite-temperature case.

**The big picture** Random circuits are the workhorse of quantum advantage claims, but sampling-based demonstrations are hard to check, while measurable quantities tend to become nearly identical for every circuit, making the specific circuit irrelevant. Recent hardware experiments measuring scrambling correlators were proposed as a verifiable alternative, yet no one had shown that the instance-to-instance signal survives as machines grow. This work proves it does, across broad families of local random circuits in any fixed dimension, and identifies exactly where in the circuit the signal lives — which also reveals the first rigorous classical speedup for computing these quantities in one dimension.

**Key contributions**
- A "slope-to-variance" principle: if the ensemble-mean observable changes by $\Delta$ over a depth window of width $W$, some depth in the window has variance $\Omega(\Delta^2/W^2)$ — sidestepping the need to compute second circuit moments of $\mathrm{OTOC}^{(2)}$, which are analytically inaccessible.
- Variance $\ge 1/\mathrm{poly}(n)$ for all fixed-order OTOCs, any fixed spatial dimension, arbitrary input states, and hardware-relevant ensembles (fixed iSWAP/fSim/CZ entanglers with Haar single-qubit layers), over $\Omega(\log n)$ consecutive depths.
- Sharp 1D endpoint analysis: Gaussian front profile with $5/\sqrt n$ error, variance $\Omega(n^{-1/2})$ throughout the $O(\sqrt n)$ window, and an analytic proof of the eye-shaped region of $\Theta(n^{3/2})$ gates each contributing $\Omega(n^{-2})$.
- Subexponential classical estimator exploiting Gaussian-tail decay of gate influence outside an enlarged eye of width $O(\sqrt{n\log(n/\epsilon\delta)})$.

**How it works** Before the deterministic Heisenberg light cone of $B$ reaches $M$, the OTOC is exactly 1; design convergence forces the Haar mean to $O_k(2^{-2n})$ (proven via a Weingarten calculation where only even-cycle permutations survive and the dominant term is killed by a sign/parity argument). Hence $\Delta = \Omega(1)$ over polynomial depth. A local reverse-variance bound converts a per-gate change in conditional mean into conditional variance, and the law of total variance lifts it globally. In 1D, the Haar-averaged Pauli-string right endpoint maps to a biased random walk with velocity $3/5$, giving the front location and diffusive broadening.

**Why it matters** This supplies the missing rigorous foundation for the Google Quantum AI OTOC advantage proposal, and identifies OTOCs as the first experimentally estimable circuit function provably escaping barren-plateau-style concentration in deep generic circuits — potentially useful as variational objectives.

**Caveats** Classical hardness remains entirely open; indeed the paper's own algorithm chips away at it. Lower bounds on variance only — no upper bounds, so the $\Omega(n^{-1/2})$ scaling may not be tight. The gate-level macroscopic-influence result and the simulation algorithm apply only to the first-order, infinite-temperature, 1D endpoint case; the general theorem is existential in depth (though scannable) and gives no gate-level structure. Noise is not modeled.

## 2. Optimal Ground-State Preparation with a Guiding State

[arXiv:2609.38091](https://arxiv.org/abs/2609.38091) · [SciRate](https://scirate.com/arxiv/2609.38091)

*Stacey Jeffery, Rolando D. Somma, Freek Witteveen, Ronald de Wolf*

**TL;DR** Given a unitary implementing $e^{iH}$, a guiding-state preparation unitary $A$ with overlap $\gamma$ onto a unique ground state, and an energy estimate accurate to $\delta=\Delta/3$, the authors prepare an $\varepsilon$-approximation of the ground state using $O((1/\gamma+\log(1/\varepsilon))/\Delta)$ (controlled) calls to $U=e^{iH}$ and $U^\dagger$ and $O(1/\gamma)$ calls to $A$. Combined with prior optimal ground-state-energy estimation, this gives $O(\log(1/\varepsilon)/(\gamma\Delta))$ overall, matching the known lower bound and shaving the $\log(1/\gamma)$ factor of previous methods. Two independent proofs are given.

**The big picture** Preparing the lowest-energy state of a quantum system is a central primitive in quantum algorithms for chemistry and materials, and the standard recipe — guess a trial state from physical intuition, filter out everything but the ground component, then amplify — has long carried a spurious logarithmic overhead. The overhead arises because the filtering subroutine is only approximately correct, and naively suppressing its errors costs extra whenever it is invoked many times inside amplification. This work removes that overhead in two ways: by carefully scheduling error suppression against amplification rounds so that false positives are pushed down exactly as fast as they are amplified, and by recasting the whole procedure in a compositional algorithmic framework where approximate subroutines can be represented exactly and composed for free. The resulting cost is provably optimal, closing the gap between energy estimation and state preparation.

**Key contributions**
- Optimal query complexity for guided ground-state preparation, matching the $\Omega(\log(1/\varepsilon)/(\gamma\Delta))$ lower bound; the $\log(1/\varepsilon)$ accuracy cost is additive in $1/\gamma$, not multiplicative, once an energy estimate is in hand.
- A first algorithm adapting "quantum search with bounded-error inputs" to an *unknown* eigenbasis: recursion $A_{\ell+1}=Q^c_{\eta_{\ell+1}}(B\otimes I)(A_\ell\otimes I)$ with schedule $\eta_\ell=2^{-\ell}/100$, $L=\lfloor\log_3(1/\gamma)\rfloor$; the marked-amplitude ratio contracts as $b_\ell/a_\ell\lesssim(1/100)^{\ell-1}2^{-\ell(\ell-1)/2}$ while $a_\ell$ grows by $\approx3$ per round.
- A transducer for LCU $\sum_j p_j U^j$ using *one* controlled call to $U$, $U^\dagger$, with transduction complexity $\sum_j p_j|j|$ — finite even for infinite Fourier expansions, via a history-state catalyst.
- A transducer for amplitude amplification with $W=O(1/\sqrt{\mu})$ and only additive counter-register overhead, improving the space of prior constructions by a log factor.
- An explicit filter $f_\delta=\frac{1}{2\pi}g_\delta\!*\!g_\delta$ from a cosine taper, with $\hat f_\delta[j]=c_j^2\ge0$, $\sum_j p_j=1$, $\sum_j|j|p_j\le\pi/(2\delta)$, and a gate-efficient Prepare using a grid superposition, exact amplitude amplification and QFT ($O(\log^2 J)$ gates).

**How it works** Both routes mark the ground space using the energy estimate and then amplify. Route 1 replaces exact marking with $Q_\eta$ (repeated phase estimation plus majority vote, $O(\log(1/\eta)/\delta)$ queries) and interleaves progressively sharper marking with amplitude amplification steps whose cost grows as $3^\ell$, so $\sum_\ell 3^{L-\ell}\log(1/\eta_\ell)/\delta=O(1/(\gamma\delta))$. Trying all recursion depths handles unknown true overlap. Route 2 composes the LCU-filter transducer (which applies $f_\delta(H)$, an approximate ground-space projector) with the amplitude-amplification transducer; exact composition avoids error reduction, and the final transducer is converted to an algorithm via Las Vegas query counting. Final accuracy boosting reuses $Q_\varepsilon$ once, costing $O(\log(1/\varepsilon)/\delta)$.

**Why it matters** Ground-state preparation is the dominant subroutine in quantum simulation pipelines; an unconditional constant-factor-optimal bound settles its query complexity in the guided, gapped, unique-ground-state model. The LCU and amplitude-amplification transducers are reusable primitives likely relevant beyond this problem, and the space improvement matters for near-term-ish resource estimates.

**Caveats** Assumes a unique ground state, a known spectral gap $\Delta$ (or a $\delta=\Delta/3$-accurate energy estimate), all eigenvalues in $[0,\pi]$, and black-box access to $e^{iH}$ — the cost of Hamiltonian simulation and of $A$ itself is not accounted for. Success is only with constant probability (the output state is $\varepsilon$-close conditioned on success). Degenerate or gapless settings, and gate-complexity optimality, remain open; the truncated construction requires mild arithmetic conditions on $J,\delta$. An independent concurrent work obtains comparable query-optimality.

## 3. Ultra-high-distance quantum memories from amplified qLDPC codes

[arXiv:2609.37231](https://arxiv.org/abs/2609.37231) · [SciRate](https://scirate.com/arxiv/2609.37231)

*Zijian Liang, Boren Gu, Yu-An Chen, Jens Eisert, Zongyuan Wang*

**TL;DR** The paper introduces "distance amplifiers": a modular tensor-product (coupled-layer) construction that multiplies a qLDPC code's distance by a small amplifier code's distance while adding, rather than multiplying, check weights. Crucially, it supplies a *fault-response certificate* — a compositional, recursively transferable lower bound on circuit-level distance — proving that under a prescribed staged-joint syndrome-extraction schedule the circuit distances also multiply, for flagged [[4,2,2]], canonical hypergraph-product, and rotated-surface amplifiers. Example: four [[4,2,2]] steps on an [[18,4,4]] bivariate-bicycle seed give [[13320,64,64]] with certified d_circ ≥ 48 and check weight ≤ 14.

**The big picture** A code that looks well protected on paper can be much weaker in practice, because a single fault in the measurement circuit that reads out the error syndromes can spread into many correlated data errors; verifying the true circuit-level protection by brute-force search becomes infeasible as codes grow. This work gives a recipe for building large, highly protected memories by repeatedly combining a small code with a larger one, together with a certificate that can be proved once for the small building block and then automatically carried through every combination step. The result is a systematic path to very large certified distances without ever running an expensive search on the big circuit, and with sparsity and individually addressable logical qubits preserved.

**Key contributions**
- Tensor-product "amplifier" framework: ñ = n·n_A + m_Z·m_X^A + m_X·m_Z^A, k̃ = k·k_A, certified distance gain α_P, and w(Q⊗A) ≤ w(Q)+w(A) — linear weight growth versus exponential for concatenation.
- The fault-response certificate: a decomposition-based quantity D_P ≤ d_circ,P that (unlike circuit distance) composes, since it bounds costs of *incomplete* fault histories with unrestricted ordinary syndromes but retained flag constraints.
- Theorem: D_P^A·D_P^Q ≤ d_circ,P(S̃) ≤ d_P^A·d_circ,P(S_Q), with the certificate itself inherited, hence recursion without re-searching; exact multiplication when the seed certificate is attained.
- Verified transferable certificates D_P^A = d_P^A for three amplifier families (flags for [[4,2,2]]; slice structure for HGP; hook-ordering transverse to logical strings for rotated surface).
- Overhead benchmarks β = log α_A / log c_A (≈0.39–0.43, i.e. d ~ n^0.43), plus explicit logical addressing, lifted SWAP automorphisms, and complete/selective surgery lifts via Cone(f⊗I) ≅ Cone(f)⊗A.

**How it works** Each amplifier qubit carries a copy of the base code; amplifier checks couple corresponding data qubits, with two extra "side" registers (indexed by base-check × amplifier-check pairs) added so all checks commute — the central truncation of the tensor chain complex. Extraction runs base-code circuits in parallel, then amplifier circuits, then two ordered side-coupling windows, deferring syndrome readout and measuring inherited flags before side tails. Lower bounds come from *contracting* a product logical along d_P^A disjoint amplifier representatives; disjointness plus a weight condition on gadget responses ensures fault costs add without double counting, so each contraction pays at least D_P^Q.

**Why it matters** It decouples "proving the circuit is good" from "making the code big," an increasingly binding constraint as qLDPC circuits outgrow distance-search tools, and it keeps LDPC sparsity at fixed depth — directly relevant to architects choosing between concatenation and product constructions.

**Caveats** Memory only: ideal encoded input, perfect final checks, no initialization/logical-operation analysis; surgery fault tolerance left open. The showcased seed's certificate (3) is below its circuit distance (4), so multiplication is not exact there (bounds 48–64, 57–76). Overhead exponent β < 1/2 and rate falls with each step (e.g. ×2/5 per [[4,2,2]] step). Weights grow linearly under unrestricted recursion; benchmarks ignore ancillas, depth, and decoding. Simulations cover only three levels with BP+LSD, noiseless idling, p ∈ [0.1%, 0.6%], and rely on extrapolated fits; no threshold or product-aware decoder yet.

## 4. Universal quantum coding

[arXiv:2609.38038](https://arxiv.org/abs/2609.38038) · [SciRate](https://scirate.com/arxiv/2609.38038)

*Jacopo Rizzo, Ludovico Lami, Jens Eisert, Lorenzo Leone*

**TL;DR** The authors show that the irreducible symmetric-group (Specht/permutation) registers appearing in the local Schur–Weyl decomposition of many copies of an *unknown* bipartite mixed state are exactly maximally entangled, and that the unknown environment acts on them only through Clebsch–Gordan branching errors whose structure is purely representation-theoretic. Correcting these errors with a fixed, state-independent recovery yields one-way LOCC distillation at the hashing (coherent-information) rate with exponentially vanishing error and the optimal second-order term, plus an analogous universal code for unknown channels that recovers the compound-channel quantum capacity.

**The big picture** Standard optimal protocols for purifying noisy entanglement or sending quantum information over a noisy channel are tailored to the particular state or channel, so in practice one must first learn the system. This work shows that the symmetry of many identical copies alone already carves out perfect entangled code spaces, and that the unknown noise only reweights a fixed, universal catalogue of correctable error patterns. As a result, a single decoder that knows nothing about the source except a rank bound and an entropy promise performs as well as the best state-aware protocol, even to the leading fluctuation correction. Conceptually, it separates the cost of characterizing a quantum system from the cost of using it optimally.

**Key contributions**
- A tripartite Schur–Weyl purification identity resolving copies of a purification into permutation and unitary registers via dual Clebsch–Gordan intertwiners with Kronecker multiplicities.
- Identification of permutation sectors as maximally entangled code spaces with branchwise conditional min-entropy exactly log(d_μ/d_ν) ≈ k·I(A⟩B).
- A state-independent "reference Schur channel" (flat over admissible error sectors) whose polar/transpose recovery works for the true channel; an approximate Knill–Laflamme condition in this basis.
- A Schur–Weyl information spectrum (ε-quantile of the packing ratio log d_μ/V_{λμ}(d_ν)) controlling finite-copy yield, bounded by Petz–Rényi conditional entropies H↓_{1+s}(A|E) with O(log k) overhead.
- Second-order achievability I(A⟩B) + √(V/k)Φ⁻¹(ε) − O(log k/k), matching known achievability and, for maximally correlated states, the converse.
- Sample complexity Õ(r_A r_B r_AB/δ²) for near-coherent-information rates; Õ(r_AB⁴2^{2R}/δ^{5+2/(α−1)}) under a sandwiched Rényi promise with no local-rank dependence; poly(n) copies achieve min{H̃↑_α(A|E), log n} for poly-rank n-qubit states.
- Exact local recoverability of both marginals; local-unitary invariance; a universal channel coding theorem with a threshold on I_c(ξ,N).

**How it works** Both parties apply an (efficiently implementable) Schur transform and measure sector labels λ, μ; Alice sends λ. Conditioned on labels, the state is the Choi state of a channel on a maximally entangled permutation register whose Kraus operators are √d_ν-weighted projected branch intertwiners. Alice encodes with a 2-design on the Specht register and measures into K-dimensional code blocks (transpose trick); Bob applies the polar recovery of the reference channel. Averaged infidelity is bounded by an error-volume packing criterion K ≪ d_μ/V_{λμ}(d_ν), whose statistics reduce, via a coupling to i.i.d. sums of log ρ_E − log ρ_B outcomes, to Petz–Rényi and Berry–Esseen estimates. For channels, the same encoder is inserted directly into the input permutation register; permutation covariance makes Bob's output-label distribution state- and code-independent, and a covering argument extends the guarantee to whole channel families.

**Why it matters** This turns Schur–Weyl duality from a technical simplification into an operational error-correction principle, giving tomography-free, dimension-independent-in-rank protocols relevant to entanglement distribution, adaptive/unknown-noise error correction, and learning-versus-using separations. Second-order optimality without a √k universality penalty is, to the authors' knowledge, new for universal distillation.

**Caveats** Bob's polar recovery is not known to be efficiently implementable (only Alice's encoder is poly-time); guarantees require a supplied global-rank ceiling and are i.i.d.; overhead constants depend on fixed ranks/dimensions, so bounds are not uniform as α↓1; second-order optimality is matched by a converse only for maximally correlated states with positive information variance; marginal reconstruction holds for local marginals after outcome averaging, not for bipartite correlations; sample-efficient rates are certified by Rényi quantities that can be strictly below coherent information.

## 5. One-dimensional quantum Gibbs states in constant circuit depth

[arXiv:2609.35973](https://arxiv.org/abs/2609.35973) · [SciRate](https://scirate.com/arxiv/2609.35973)

*Saúl Pilatowsky-Cameo, Georgios Styliaris, Ainesh Bakshi, Daniel Malz*

**TL;DR** The Gibbs state of any 1D geometrically local spin-chain Hamiltonian, at any constant inverse temperature β, is *exactly* a classical mixture of states that factorize over contiguous blocks of at most C_β = exp(exp(exp(16r)·β̃)) qubits, each block factor being an MPS of bond dimension ≤ C_β. Consequently 1D Gibbs states can be prepared exactly by ensembles of nearest-neighbor unitary circuits of depth independent of N (with poly(N,1/ε) classical sampling), improving on the previous best polylog-depth 1D result. The same machinery yields constant bounds on entanglement depth/width, exact vanishing of localizable entanglement beyond a constant distance, a thermalization corollary, and a fermionic analogue with Gaussian states dressed by constant-depth parity-preserving circuits.

**The big picture** Thermal equilibrium states of one-dimensional quantum matter are known to be weakly correlated, but exactly how much genuinely quantum structure they retain — and how hard they are to make on a quantum computer — has remained unsettled. This work shows that at any fixed temperature above zero such a state is nothing more than a random mixture of states that are entangled only within short, contiguous chunks of the chain, with the chunk length set by temperature alone. That simultaneously gives a preparation recipe whose quantum cost does not grow with the length of the chain, and a sharp statement that no entanglement of any kind — including entanglement that could be extracted by measuring intermediate sites and communicating classically — survives beyond a fixed distance.

**Key contributions**
- Exact block-separability of 1D Gibbs states at *all* constant temperatures (previously only known in the high-temperature regime), with explicit constants.
- Constant-depth (in N) exact preparation ensemble; poly-time classical sampler for the circuit descriptions.
- Entanglement depth and width ≤ C_β; exact "spatial sudden death" of localizable/assisted entanglement beyond C_β — strictly stronger than separability of the reduced state after tracing out the middle (cf. the GHZ counterexample given).
- Thermalization at any constant temperature for translation-invariant chains with nondegenerate gaps, with fluctuations O(N^{-1/2+δ}).
- Fermionic version via Jordan–Wigner: mixture of Gaussian states acted on by blockwise constant-depth fermionic circuits.

**How it works** A two-sided "entanglement bulk decomposition" (extending Bakshi et al. to interior sites and rings by folding) writes e^{-βH} = M e^{-βH_{\setminus k}} X with M local on m = exp[rβ̃(2240)^{2r}] sites and X a quasilocal perturbation of the identity with decay γ = 1/112. Iterating at spacing m leaves a staircase of QPIs, which is provably separable, so the bulk becomes ⊗_j G_j. Each G_j is split into a midpoint-factorized positive piece G_j' plus Δ_j ≼ (1−e^{−7m})G_j; grouping L = e^{9m} blocks into a superblock, the unique cut-free term ⊗Δ_j is exponentially suppressed and can be absorbed with G_{j_0}', using that 1+K is a positive combination of stabilizer product states when ‖K‖ ≤ 4^{−m}. Every superblock thus acquires a cut not crossed by any M_j. Sampling: QPI-tree sampling, then a forward–backward transfer-matrix sweep on the resulting classical nearest-neighbor ring distribution over cut positions, then spectral sampling within blocks.

**Why it matters** This closes the gap between high-temperature separability results and finite temperature in 1D, settles the depth complexity of 1D thermal state preparation up to β-dependence, and rules out finite-temperature topological order in 1D in the strongest sense (strictly local gates, pure-state mixtures). Relevant to Gibbs samplers, quantum metrology (entanglement depth bounds quantum Fisher information), and tensor-network/classical simulation.

**Caveats** The block size and depth scale doubly exponentially in β; optimality is open (the authors ask for matching lower bounds). Constants are astronomically large in practice (c_r = e^{16r}). Results are strictly 1D with bounded-range, bounded-norm terms on qubits (qudits claimed straightforward; bosons open); 2D remains open. Preparation is exact only in the idealized decomposition — the sampler incurs trace-norm error ε. The thermalization corollary inherits translation invariance and nondegenerate-gap assumptions and is an infinite-time-average statement.
