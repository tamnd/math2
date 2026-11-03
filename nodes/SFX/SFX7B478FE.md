---
tag: SFX7B478FE
kind: statement
role: theorem
name: Kraus representation of a channel
msc: [81P47, 46L07]
uses: [HM2HHE3J51, 10VZYJ4552, F1K9J81GCT, CGY299QMC3, X8K0Z7484R, EQG2K8ZFM4]
about: [10VZYJ4552, CGY299QMC3]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_operation
---

## Statement

Let $\mathcal{H}_A$ and $\mathcal{H}_B$ be complex [[Hilbert spaces|HM2HHE3J51]] of finite dimensions $n$ and $m$.
Let $\Phi$ be a linear map from the operators on $\mathcal{H}_A$ to the operators on $\mathcal{H}_B$.

1. $\Phi$ is [[completely positive|CGY299QMC3]] if and only if $\Phi(X) = \sum_{k=1}^r K_k X K_k^*$ for all $X$, for some linear maps $K_k \colon \mathcal{H}_A \to \mathcal{H}_B$ and $r \le nm$.
2. In that case, $\Phi$ preserves the trace if and only if $\sum_{k=1}^r K_k^* K_k = I_A$.
So $\Phi$ is a [[quantum channel|10VZYJ4552]] exactly when it has such a form with $\sum_k K_k^* K_k = I_A$.
3. Two families $(K_k)_{k \le r}$ and $(L_j)_{j \le r}$ give the same map if and only if $L_j = \sum_k u_{jk} K_k$ for a unitary matrix $(u_{jk})$.

## Remarks

The operators $K_k$ are called Kraus operators.
In part 3, families of different lengths are compared after padding the shorter one with zero operators.
Part 1 is part of [[Choi's theorem on completely positive maps|EQG2K8ZFM4]].
For the proof of 1, form the Choi matrix $C = \sum_{i,j} e_ie_j^* \otimes \Phi(e_ie_j^*)$, which is positive when $\Phi$ is completely positive.
Write $C = \sum_k v_kv_k^*$ with at most $nm$ vectors $v_k$, from its spectral decomposition, and reshape each $v_k$ into a map $K_k$.
The converse is direct, since each map $X \mapsto KXK^*$ is completely positive.
Part 2 follows from $\tr \Phi(X) = \tr\big(\sum_k K_k^*K_k\, X\big)$ for all $X$.
Example: the qubit dephasing channel $\Phi(X) = (1 - p)X + pZXZ$ has the Kraus operators $\sqrt{1 - p}\, I$ and $\sqrt{p}\, Z$, and indeed $(1 - p)I + pZ^2 = I$.
The decomposition is a finite-dimensional form of the [[Stinespring dilation theorem|X8K0Z7484R]].

## Explanations

### L1 human

Every quantum channel can be written as a sum of simple pieces $X \mapsto KXK^*$.
One can think of each piece as one possible way the environment acts on the system, with the conditions $\sum K_k^*K_k = I$ making sure that probabilities add up to one.
This is the standard way to write and compute with noise in quantum computing.

### L2 human

The theorem turns the abstract condition of complete positivity into a concrete formula, through the Choi matrix.
It is equivalent, in finite dimensions, to Stinespring's dilation: a channel is an isometry into a larger space followed by a partial trace.
The Kraus operators are far from unique, as part 3 shows, and the minimal number of them is the rank of the Choi matrix.
For [[quantum operations|F1K9J81GCT]] that may decrease the trace, the same holds with $\sum_k K_k^*K_k \le I$.
