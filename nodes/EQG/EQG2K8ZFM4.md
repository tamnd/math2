---
tag: EQG2K8ZFM4
kind: statement
role: theorem
name: Choi's theorem on completely positive maps
msc: [46L07, 15B48, 81P47]
uses: [CGY299QMC3, 01MMVW8CKC, 0N7ENQRCXN, 0FHVPRAE60]
about: [CGY299QMC3]
sources:
  - url: https://en.wikipedia.org/wiki/Choi%27s_theorem_on_completely_positive_maps
same_as:
  wikidata: Q5103861
  wikipedia: Choi's theorem on completely positive maps
---

## Statement

Let $n, m \ge 1$, and let $\Phi \colon M_n(\C) \to M_m(\C)$ be a linear map between [[matrix rings|0FHVPRAE60]].
Let $E_{ij} \in M_n(\C)$ be the matrix units, and let
$$C_\Phi = \sum_{i,j=1}^{n} E_{ij} \otimes \Phi(E_{ij}) \in M_n(\C) \otimes M_m(\C) \cong M_{nm}(\C)$$
be the Choi matrix of $\Phi$, where $\otimes$ is the [[Kronecker product|0N7ENQRCXN]].
The following are equivalent:

1. $\Phi$ is [[completely positive|CGY299QMC3]];
2. $\Phi$ is $n$-positive;
3. $C_\Phi$ is [[positive semidefinite|01MMVW8CKC]];
4. there are $m \times n$ complex matrices $V_1, \ldots, V_r$, with $r \le nm$, such that $\Phi(a) = \sum_{k=1}^{r} V_k a V_k^*$ for all $a \in M_n(\C)$.

## Remarks

Proof idea: $1 \Rightarrow 2$ is clear, and $2 \Rightarrow 3$ holds because $C_\Phi = \Phi_n(x)$ for the positive block matrix $x = [E_{ij}]_{i,j}$.
For $3 \Rightarrow 4$, write $C_\Phi = \sum_k v_k v_k^*$ with at most $nm$ vectors $v_k \in \C^{nm}$, using the spectral decomposition, and reshape each $v_k$ into an $m \times n$ matrix $V_k$.
For $4 \Rightarrow 1$, each map $a \mapsto V a V^*$ is completely positive, and sums of completely positive maps are completely positive.

Example: for the transpose $\Phi(a) = a^T$ on $M_2(\C)$, the Choi matrix is the swap matrix on $\C^2 \otimes \C^2$, which has eigenvalue $-1$.
So the transpose is not completely positive, although it is positive.
The matrices $V_k$ in clause 4 are called Kraus operators.

## Explanations

### L1 human

Complete positivity is a condition about infinitely many matrix sizes, so it looks hard to check.
Choi's theorem reduces it to a single test: build one $nm \times nm$ matrix from $\Phi$ and check that it has no negative eigenvalue.
It also gives a concrete formula for every completely positive map between matrix algebras.

### L2 human

The theorem is the finite-dimensional form of the [[Stinespring dilation theorem|X8K0Z7484R]].
In quantum information, it gives the Kraus representation of quantum channels; the channel is trace-preserving exactly when $\sum_k V_k^* V_k = I$.
The correspondence $\Phi \mapsto C_\Phi$ between maps and matrices is the Choi–Jamiołkowski isomorphism, and condition 2 shows that $n$-positivity already implies complete positivity for maps defined on $M_n(\C)$.
