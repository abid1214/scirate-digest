# SciRate Daily Digest — 2026-09-22

The top 5 papers on [SciRate](https://scirate.com/) today.

## 1. Lee-Yang theorem for fermions

[arXiv:2609.23942](https://arxiv.org/abs/2609.23942) · [SciRate](https://scirate.com/arxiv/2609.23942)

*Chaithanya Rayudu, Takahiro Misawa, Andrew Zhao, Jun Takahashi*

**TL;DR** The authors prove the first rigorous Lee–Yang zero-freeness theorem for interacting fermions: for quadratic Hamiltonians with positive-semidefinite hopping matrix $A$, arbitrary pairing $B$, and arbitrary attractive density-density interactions, all zeros of the partition function in the complex uniform-field plane lie in the strip $\mathrm{Re}(h)\in[-\lambda_{\max}(A),0]$ (on the imaginary axis when $A=0$). This yields a field-induced spectral gap $\geq h/8$ and hence a poly$(N,\|H\|,1/\epsilon)$-time quantum algorithm for ground-state energies of models including the attractive Hubbard model in a pairing field, bipartite repulsive Hubbard in a staggered Zeeman field, and the interacting Hofstadter model — the last of which has no known sign-problem-free representation.

**The big picture** A classic result in statistical physics says that for ferromagnetic magnets, the partition function never vanishes when an external field is present, which rigorously forbids phase transitions there and, more recently, has been used to certify that certain algorithms converge quickly. Analogous results existed for quantum spins but, surprisingly, not even for free fermions. This work closes that gap for a large family of interacting electron models, and converts the zero-freeness into a guaranteed energy gap whenever a suitable field is switched on — which in turn gives provable polynomial-time quantum algorithms for ground-state energies of strongly correlated fermion models that are otherwise intractable, including cases where quantum Monte Carlo suffers a sign problem.

**Key contributions**
- First Lee–Yang theorem for fermions (interacting and free), with explicit localization of zeros to a strip whose width is set by the largest hopping eigenvalue.
- Provable field-induced gap and efficient quantum ground-energy estimation for this class.
- Identification of physically important models inside the class via Bogoliubov/particle-hole/pseudospin maps, notably the interacting Hofstadter model (non-sign-problem-free ⇒ candidate for quantum advantage).
- Mapping of the relation between the Lee–Yang class and Majorana reflection positivity: they intersect on a real-$A$/imaginary-$B$ slice, and the PSD condition coincides exactly.
- A no-go argument: no gapped topologically ordered phase with field-stable ground-state degeneracy in these models; consistent with the resolved honeycomb-Hubbard "intermediate phase" debate.

**How it works** The Trotterized partition function is written as a multivariate polynomial in fugacity variables $u_{i,m}$ (one per mode per Trotter layer). For free fermions, its square becomes the determinant of a block "pencil" matrix $\mathfrak D$ built from $W=e^{-\epsilon Q}$ and diagonal $u$-matrices. Non-singularity in the open unit polydisc follows from the indefinite form $\Gamma=\mathrm{diag}(+1,-1)$: since $\{\Gamma,Q\}\succeq0$ (equivalent to $A\succeq0$), $W\Gamma W\preceq\Gamma$, so a null vector would force $\sum(1-|u|^2)|\phi|^2\le 0$. Interactions are added by noting that the interacting polynomial is exactly the Schur (coefficientwise) product of the free-fermion polynomial with a classical ferromagnetic Ising partition function; Asano-contraction-based stability of Schur products preserves polydisc zero-freeness. Hurwitz's theorem removes Trotterization; particle-hole conjugation gives the lower edge of the strip.

**Why it matters** Rigorous control of nonperturbative, strongly interacting fermions is rare; this adds a broad, physically relevant class to the tiny list of many-body problems with provable algorithmic guarantees, and gives a unifying analytic structure behind case-by-case sign-problem-free conditions.

**Caveats** The relevant field is not the physical chemical potential in general — it is a pairing or staggered field after a Bogoliubov/particle-hole rotation — so conclusions about absent transitions apply only in that specific field, not at zero field. Interactions must be attractive (after transformation) and density-density; $A\succeq0$ forces e.g. a large Zeeman field in the non-bipartite case (whose ground state is then trivially polarized). The gap scales as $h$, so precision is bought with polynomial, not logarithmic, cost; the algorithm is inherited from prior spin-model arguments rather than developed here. The topological-order no-go assumes degeneracy stability under weak perturbations, and no classical hardness is proven for the Hofstadter case.

## 2. Pauli-resolved virtual distillation

[arXiv:2609.24132](https://arxiv.org/abs/2609.24132) · [SciRate](https://scirate.com/arxiv/2609.24132)

*Si-Yuan Chen, Congcong Zheng, Kun Wang, Ming-Cheng Chen*

**TL;DR** The paper shows that the entire set of $4^n$ *squared* Pauli moments $[\mathrm{tr}(P\rho^m)]^2$ of a virtually distilled state can be estimated to additive error $\varepsilon$ from a *single* collective measurement setting on $2m$ replicas, using $O(m[n+\log(1/\delta)]/\varepsilon^2)$ copies — an exponential improvement over prior replica-shadow protocols that scale as $2^n$ or worse. The mechanism is a "paired cancellation" of anticommutation signs, formalized via a new SDP-computable incompatibility measure (the quantum Bernstein norm), and realized for $m=2$ by a *coherent* Bell difference sampling circuit; a separate $m$-replica mimicking-state protocol recovers the signs at $\varepsilon^{-4}$ cost with provably optimal replica count.

**The big picture** Error mitigation by virtual distillation reports expectation values on a purified version of a noisy state, but learning all its Pauli observables at once has been thought to demand exponentially many state copies. The authors show this barrier is really a measurement-incompatibility barrier, and that it evaporates once you pair up replicas so that the offending sign structure cancels — making the whole exponentially large observable family jointly measurable in one shot. They also supply a general, numerically computable yardstick for how incompatible any family of nonlinear state properties is, which reproduces known incompatibility and shadow-tomography bounds as special cases. This makes error-mitigated Hamiltonian estimation and magic certification of noisy states plausibly practical on near-term hardware.

**Key contributions**
- Explicit commuting family $O_P = T_P\,(C+C^\dagger)/2$ on $2m$ replicas, with $T_P=\frac1m\sum_i P_iP_{m+i}$ and $C$ the product of two $m$-cycles, satisfying $\|O_P\|_\infty\le1$ and $\mathrm{tr}(O_P\rho^{\otimes 2m})=[\mathrm{tr}(P\rho^m)]^2$.
- Coherent Bell difference sampling (CBDS) circuit + explicit decoding algorithm for $m=2$ (transversal CNOT/Hadamard layers, then adaptive computational-basis / GHZ-basis readout on the unresolved sector, $O(\log n)$ depth for the GHZ part).
- The $k$-replica quantum Bernstein norm $\|\mathcal F\|_k$: minimal unbiased-estimator range over all joint POVM+post-processing schemes; an SDP with strong duality, reducing to homogeneous robustness of incompatibility ($r_k^*=\max\{\|\mathcal F\|_k-1,0\}$) in the linear case, giving $\sqrt3$ for one qubit and $3^{n/2}$ for local Pauli measurements.
- Collapse theorem: $\|\{[\mathrm{tr}(P\rho^m)]^2\}\|_{2m}=1$ for all $m$ — the protocol is range-optimal.
- Signed-moment protocol: Bell sampling identifies large $q_P=\mathrm{tr}(P\rho P\rho)$, a random mimicking state $\chi$ is built, and a controlled cyclic permutation gives $\mathrm{tr}(P\rho^m)\mathrm{tr}(P\chi)$; $O(m[n+\log(1/\delta)]/\varepsilon^4)$ copies, matching the $\Omega(2^{n/2})$ lower bound barring $m$ replicas.

**How it works** The nonlinear functional is linearized as a $2m$-replica observable; the linearization is non-unique, and averaging the paired products $P_iP_{m+i}$ over the cycle produces representatives that commute because any $\pm$ sign from $PQ=-QP$ appears twice. A joint eigenbasis measurement then yields unit-range unbiased estimators for all targets simultaneously; Hoeffding plus a union bound over $4^n$ targets gives the $n$ (not $2^n$) scaling. Dual feasible points of the SDP, reduced by Clifford/unitary commutant symmetry, recover known lower bounds for Pauli shadow tomography and purity estimation.

**Why it matters** Concretely, $n=50$, $\varepsilon=0.05$, $\delta=0.01$ needs ~$6\times10^4$ rounds ($2.4\times10^5$ copies on 200 qubits) for all $4^{50}$ squared moments. Relevant to VQE measurement reduction, stabilizer-Rényi-entropy/magic certification of mixed states (even powers suffice), and to anyone studying replica-based shadow protocols or measurement incompatibility theory. CBDS is a genuinely new primitive: coherent rather than classical subtraction of Bell outcomes lifts accessible quantities from $\mathrm{tr}(P\rho)$ to $\mathrm{tr}(P\rho^2)$.

**Caveats** The signed-moment result is information-theoretic only — sampling the mimicking state requires a linear satisfiability program that need not be efficient; a computationally efficient signed protocol remains open. The $\varepsilon^{-4}$ dependence is worse than shot-noise, and dividing out $\mathrm{tr}(P\chi)$ presumes good overlap with the significant moments. Squared moments alone are insufficient for Hamiltonian energies. The scheme needs $2m$ coherent replicas plus transversal entangling gates; no noise-robustness or gate-error analysis of CBDS is given, and the normalization $\mathrm{tr}(\rho^m)$ is assumed constant/known for the PVD interpretation. Replica optimality holds only "for fixed $m$ in the stated lower-bound regime."

## 3. Wigner-positive quantum states can have lower entropy than the vacuum

[arXiv:2609.24670](https://arxiv.org/abs/2609.24670) · [SciRate](https://scirate.com/arxiv/2609.24670)

*Zacharie Van Herstraeten, Nicolas J. Cerf, Ulysse Chabaud*

**TL;DR** The authors disprove the Wigner entropy conjecture: there exist mixed Wigner-positive single-mode states whose Wigner (Shannon) entropy is strictly below the vacuum value $1+\ln\pi$. Two explicit analytic families do it — states in $\mathrm{span}\{|0\rangle,|n\rangle\}$ for every $n\ge3$ (entropy $1+\ln\pi+(2n-2^n)t+o(t)$) and a rank-2 state in $\mathrm{span}\{|0\rangle,|1\rangle,|2\rangle\}$ (deficit $-\tfrac23\epsilon^3$) — which also break the Wigner majorization conjecture and the Wigner–Rényi conjecture for all $0<\alpha<2$; they complete the picture by proving the conjecture *does* hold in $\mathrm{span}\{|0\rangle,|2\rangle\}$.

**The big picture** A longstanding conjecture held that among all quantum states whose phase-space quasiprobability is a genuine probability distribution, the vacuum (and squeezed/displaced versions of it) is the most concentrated, i.e. has the least phase-space entropy — a natural-looking strengthening of the entropic uncertainty principle. This work shows the conjecture is false: by blending a suitably chosen non-classical state with a second state that cancels the negative regions of its quasiprobability, one can keep a valid probability distribution while beating the vacuum, albeit by a tiny margin. The mechanism is that non-Gaussianity can buy more entropy reduction than the extra uncertainty caused by mixing, so the vacuum is not a universal phase-space concentration limit and existing partial proofs mark real boundaries rather than steps toward a theorem.

**Key contributions**
- Counterexamples with violations up to $\sim10^{-3}$ numerically ($\approx4\times10^{-5}$ analytically at $n=4$), existing arbitrarily close to the vacuum in trace distance.
- Corollary disproofs of Wigner majorization and of Wigner–Rényi $\alpha$-entropy bounds for $0<\alpha<2$, with explicit slope $C_{n,\alpha}=-2\sum_{k=1}^{n-2}[\binom{n-1}{k}-1]\big(\tfrac{2-\alpha}{\alpha}\big)^k<0$.
- Proof that every Wigner-positive state in $\mathrm{span}\{|0\rangle,|2\rangle\}$ (and in $\mathrm{span}\{|0\rangle,|1\rangle\}$) is a beam-splitter state, hence satisfies the bound — establishing minimality of the counterexamples.
- Physical diagnosis: $h(W_\rho)=h(W_0)+G-D$ with $G\simeq 2nt$ (Gaussification excess) and $D\simeq 2^n t$ (relative Wigner entropy/non-Gaussianity); violation begins exactly where $2^n>2n$, i.e. $n=3$.

**How it works** Using $h(W)-h(W_0)=2\langle\hat n\rangle-D(W\|W_0)$, they write $W=W_0(1+\delta)$ and expand. For $\rho_n(t,s)=(1-t)|0\rangle\langle0|+t|n\rangle\langle n|+s(|0\rangle\langle n|+\text{h.c.})$, Laguerre-polynomial positivity of the Wigner function caps the coherence at $s_n(t)$ with $s_n(t)^2=t+o(t)$ (an explicit admissible $\widetilde s_n(t)=\sqrt{t(1-t)(1-en t^{1/n})}$ is given via AM–GM bounds on Laguerre zeros). Dominated convergence with the global bound $0\le(1+z)\ln(1+z)-z\le z^2$ on $z\ge-1$ legitimizes term-by-term integration despite $\delta\to-1$ at Wigner zeros, giving $D=2^n t+o(t)$. The three-level family mixes a Wigner-negative displaced-like state $|\phi_\epsilon\rangle$ with $|2\rangle$ at weight $\epsilon^4$: their negativities live in disjoint phase-space annuli, and positivity is proved rigorously for $\epsilon\le1/100$, with moments computed to order $\epsilon^3$ (seventh-order Taylor control).

**Why it matters** Removes a candidate phase-space uncertainty principle from the toolbox of bosonic quantum information; the true infimum lies between $\ln(2\pi)$ and $1+\ln\pi$, a gap of $\ln(e/2)$. Also suggests certification applications: sub-vacuum Wigner entropy excludes passive states, Fock mixtures, beam-splitter states, and purity $\le2/e$.

**Caveats** Violations are extremely small and the optimal lower bound (and whether it is attained) remains open; counterexamples require high purity and nonzero Fock coherence; results are single-mode; a concurrent preprint reports similar counterexamples.

## 4. Entanglement Cost of Optimal Distributed Quantum State Purification

[arXiv:2609.23441](https://arxiv.org/abs/2609.23441) · [SciRate](https://scirate.com/arxiv/2609.23441)

*Jiayi Zhao, Chengkai Zhu, Xin Wang, Ge Bai*

**TL;DR** For the task of probabilistically distilling one higher-fidelity copy from two depolarized copies of an unknown bipartite pure state on $\mathbb{C}^d\otimes\mathbb{C}^d$, the authors compute the exact global (unrestricted CPTN) optimum of the Haar-averaged, success-probability-weighted fidelity gain, $G_\star=\tfrac12(1-\gamma+\gamma/D)\gamma(1-\gamma)(1-1/D)$ with $D=d^2$, and show its optimizer is unique (symmetric-subspace projection followed by discarding a copy). A single preshared EPR pair lets LOCC reproduce this exactly via a *distributed swap test*, and conversely any finite-dimensional resource attaining the benchmark — even under a PPT relaxation of LOCC — must carry at least one ebit of entanglement of formation, with equality cases pinned to EPR pairs up to local unitaries.

**The big picture** When noisy copies of a quantum state are shared between distant nodes, the best purification procedures involve joint processing across the nodes, which is precisely what a network cannot do for free. This paper settles exactly how much preshared entanglement two separated parties need to match the very best purification achievable by a fully joint device: one maximally entangled pair of qubits, no matter how large the local systems are, and no matter how strong the noise. Less entanglement provably cannot do it, and even having more entanglement does not help unless it has the right structure. This gives a clean, dimension-independent yardstick for budgeting entanglement in quantum networks and modular quantum computers.

**Key contributions**
- Closed-form global CPTN benchmark for two-copy blind purification under global depolarizing noise, in every local dimension, plus a proof that the optimizer is *unique*.
- An explicit LOCC protocol using one EPR pair that saturates it: local controlled-SWAPs controlled by the EPR halves, local Hadamards, local measurements, accept iff outcomes agree — a distributed swap test realizing $P_{\rm sym}(\cdot)P_{\rm sym}$.
- Converse: one-ebit lower bound on $E_{\rm F}$ of any finite-dimensional resource, proven for the strictly larger class of PPT instruments, extended to mixed resources by a convex-roof argument.
- Rigidity: pure one-ebit resources work iff Schmidt spectrum is $(1/2,1/2,0,\dots)$; all two-qubit resources (mixed included) work iff maximally entangled. A corollary exhibits pure states with *more* than one ebit that still fail — entanglement quantity alone is not the operational resource.
- Machine-checked proof of the pure-resource converse in Lean 4.

**How it works** The figure of merit $g_\psi=\langle\psi|\hat\sigma_\psi|\psi\rangle-p_\psi F(\psi,\mathcal N^\gamma(\psi))$, Haar-averaged, is linear in the success map's Choi operator, giving an SDP with performance operator $M$ built from Haar moments up to third order. $M$ commutes with $\overline U\otimes\overline U\otimes U$ and with the input-copy swap; mixed Schur–Weyl duality decomposes the three-leg Choi space into four blocks ($\mathrm{Ran}\,W_\pm$ of dimension $D$ each, plus two multiplicity-one blocks $\mathcal L_\pm$), with the swap parity killing the off-diagonal multiplicity block. The optimum sits on $P_{W_+}$ with weight $(D+1)/2$ — exactly the Choi operator of the EPR protocol's accepted map. Uniqueness then forces any attaining LOCC/PPT protocol to implement this same map; expanding the resource's Schmidt decomposition and imposing PPT positivity on the success and failure Choi operators yields a constraint on the Schmidt weights forcing $E\ge 1$.

**Why it matters** It cleanly separates the intrinsic entanglement cost of a distributed noise-reduction primitive from implementation overhead — relevant for anyone allocating entanglement budgets in modular architectures or repeater networks. The one-ebit threshold's independence of $d$ and $\gamma$ is striking: a two-dimensional coherent control register suffices to orchestrate collective purification of arbitrarily large local registers.

**Caveats** Restricted to $n=2$ copies and global depolarizing noise; the authors note the swap test is near-optimal for Pauli noise but poor for amplitude damping, and that symmetric projection's optimality for $n>2$ remains conjectural (their generalization costs $\log_2 n!$ ebits, possibly not tight). The merit function is a Haar average of a probability-weighted gain, not a worst-case or fidelity-only criterion. The sub-ebit entanglement–gain tradeoff is completely open. Full "only EPR" characterizations cover only pure one-ebit and two-qubit resources; higher-dimensional mixed resources with $E_{\rm F}\ge 1$ are not classified. Cost is measured by input $E_{\rm F}$ regardless of protocol outcome, ignoring possible resource recycling.

## 5. Modular fault-tolerant quantum computing on a non-CSS code

[arXiv:2609.22572](https://arxiv.org/abs/2609.22572) · [SciRate](https://scirate.com/arxiv/2609.22572)

*Robert Freund, Friederike Butt, César Benito, Ivan Pogorelov, Marcel Meyer, Alex Steiner, Alejandro Bermudez, Markus Müller et al.*

**TL;DR** The authors implement, on a 16-ion ⁴⁰Ca⁺ trapped-ion processor, the complete set of fault-tolerant logical primitives for the non-CSS perfect [[5,1,3]] code: flag-based state preparation, QEC with real-time feedback, fault-tolerant logical measurement, pieceably fault-tolerant CZ/CY between two code blocks, verified magic-state preparation, magic-state injection for a logical π/4 Y-rotation, and logical state teleportation between two code blocks with real-time Pauli corrections. They also introduce a logical Pauli process tomography with SPAM-error removal, reporting an 85 ± 8 % process fidelity for the logical non-Clifford gate.

**The big picture** Most experimental error-correction demonstrations use codes built from two classical codes, which makes logical operations easy because gates act qubit-by-qubit in parallel. The smallest code that can correct any single-qubit error does not have that structure, so every logical primitive — measuring a logical observable, entangling two blocks, preparing a magic resource state — needs a bespoke, carefully verified construction. This work builds and runs that full toolbox on a trapped-ion machine, including moving encoded information between two separate code blocks purely by measurement and classical feedback, the key connectivity primitive for modular machines. The same non-transversal techniques will be needed for the high-rate codes now favored for scaling, so the result is a testbed for that regime in the smallest possible footprint.

**Key contributions**
- First complete universal FT logical toolbox on a non-CSS code, including modular logical teleportation with real-time feedback.
- New single-flag circuits for the three logical-operator representations needed for FT logical measurement (previously two flags), and a single flag shared across a stabilizer pair.
- Novel non-FT magic-state ( |H_XZ⟩ ) preparation circuit plus verification and error detection, verified FT by exhaustive single-fault insertion.
- Pieceable (round-robin, 3 layers of CZ with interleaved error detection) logical CZ/CY, used for magic-state injection.
- Logical-level Pauli QPT: 4 parameters instead of 1023 physical ones, with a SPAM-inversion scheme valid when QEC (not postselection) is used, and a 5-parameter extension for non-Clifford gates.
- First measurement of logical "spectator" crosstalk in the 5-qubit code: a QEC cycle on one logical qubit raises the idling qubit's infidelity by ~20 % (relative).

**How it works** Logical readout maps three weight-3 representations of the logical operator onto flagged ancillas, then unencodes and destructively measures the data block; majority agreement plus syndrome-based correction gives a FT outcome. Teleportation measures X_L⊗X_L then Z_L, each at least twice, with flags and an intervening QEC round to handle the three distinct single-fault classes; mid-circuit measurements are bundled and corrections applied in real time. Monte Carlo simulations with experimentally calibrated rates (2-qubit 2 %, 350 µs; measurement 0.3 %, 1 ms; T₂ = 200 ms) track the data.

**Why it matters** It demonstrates that transversality is not a prerequisite for universal FT control, relevant to compact distance-3 encodings, magic-state cultivation, and selective logical addressing inside qLDPC blocks.

**Caveats** Fidelities are modest and heavily postselected: teleportation yields 21⁺⁷₋₅ % infidelity at a 0.035 % acceptance rate, magic-state injection 0.023 %, so these are proof-of-principle rather than scalable protocols. A single QEC round degrades memory (26.8 % infidelity) rather than improving it, dominated by 2-qubit-gate and mid-circuit-measurement errors. Logical QPT assumes Pauli noise, cannot separate preparation from measurement errors (gauge freedom), is invalid under postselection, and does not describe concatenated operations; the injection tomography error bars are large (+16/−3 %). Operations run sequentially, inflating idling dephasing.
