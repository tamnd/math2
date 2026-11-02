---
tag: A8R7V30ANX
kind: definition
name: Ideal of compact operators
msc: [47L20, 47B07, 46L05]
defines: 2WAZF1RV2Y
uses: [HM2HHE3J51, M2NEP1K5AE, BMDG4JQPEH, 0CD87SFM2N]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_operator_on_Hilbert_space
---

## Definition

Let $H$ be a [[Hilbert space|HM2HHE3J51]] and let $\mathcal{B}(H)$ be the [[algebra of bounded operators|BMDG4JQPEH]] on $H$ with the operator norm.
The *ideal of compact operators* on $H$ is the set
$$\mathcal{K}(H) = \set{T \in \mathcal{B}(H) : T \text{ is a compact operator}},$$
with compactness in the sense of [[compact operators|M2NEP1K5AE]].
It is a norm-closed [[two-sided ideal|0CD87SFM2N]] of $\mathcal{B}(H)$ and is closed under taking adjoints.

## Remarks

Example: on $H = \ell^2$, the diagonal operator with entries $1, 1/2, 1/3, \ldots$ belongs to $\mathcal{K}(H)$, since it is the norm limit of its finite-rank truncations.
For any bounded $A$, the products $AT$ and $TA$ are again in $\mathcal{K}(H)$.
Indeed, a bounded operator maps bounded sets to bounded sets and relatively compact sets to relatively compact sets.

Non-example: if $H$ is infinite-dimensional, the identity $I$ is not in $\mathcal{K}(H)$, since an orthonormal sequence has no convergent subsequence; so $\mathcal{K}(H)$ is a proper ideal.
If $H$ is finite-dimensional, every operator is compact and $\mathcal{K}(H) = \mathcal{B}(H)$.

Other notations are $\mathcal{K}$ and $\mathcal{B}_0(H)$.
On a Hilbert space, $\mathcal{K}(H)$ equals the norm closure of the finite-rank operators.
