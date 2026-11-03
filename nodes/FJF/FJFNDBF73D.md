---
tag: FJFNDBF73D
kind: definition
name: Partial trace
msc: [81P16, 15A69, 47B10]
defines: SQ3J7AVMKM
uses: [HM2HHE3J51, EY0X2NKA3S, Z2CP530WDE, 0KZDNGA561, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_trace
---

## Definition

Let $\mathcal{H}_A$ and $\mathcal{H}_B$ be complex [[Hilbert spaces|HM2HHE3J51]] and let $\mathcal{T}(\mathcal{H})$ denote the [[trace class operators|Z2CP530WDE]] on a Hilbert space $\mathcal{H}$.
The *partial trace over $B$* is the unique linear map $\tr_B \colon \mathcal{T}(\mathcal{H}_A \otimes \mathcal{H}_B) \to \mathcal{T}(\mathcal{H}_A)$ such that
$$\tr\big(\tr_B(T)\, X\big) = \tr\big(T\,(X \otimes I_B)\big)$$
for every $T \in \mathcal{T}(\mathcal{H}_A \otimes \mathcal{H}_B)$ and every bounded operator $X$ on $\mathcal{H}_A$.
Here $\otimes$ is the [[tensor product|EY0X2NKA3S]], $I_B$ is the identity on $\mathcal{H}_B$, and $\tr$ is the [[trace|0KZDNGA561]].
If $(f_j)$ is an [[orthonormal basis|0S9GGTR0EX]] of $\mathcal{H}_B$, then
$$\langle u, \tr_B(T)\, v \rangle = \sum_j \langle u \otimes f_j, T (v \otimes f_j) \rangle \quad \text{for all } u, v \in \mathcal{H}_A.$$
The partial trace $\tr_A$ over $A$ is defined in the same way.

## Remarks

On product operators, $\tr_B(S \otimes R) = \tr(R)\, S$, and this property together with linearity and continuity determines $\tr_B$.
Example: let $\psi = (e_0 \otimes e_0 + e_1 \otimes e_1)/\sqrt2$ in $\C^2 \otimes \C^2$ and $T = \psi\psi^*$.
Then $T = \tfrac12 \sum_{i,j} e_i e_j^* \otimes e_i e_j^*$, and $\tr(e_i e_j^*) = 1$ if $i = j$ and $0$ otherwise, so $\tr_B(T) = \tfrac12 I$.
Non-example: on $\C^2 \otimes \C^2$, the map $T \mapsto \tr(T)\, I_A / \dim \mathcal{H}_A$ preserves the trace, but it fails the defining identity for $T = e_0e_0^* \otimes e_0e_0^*$ and $X = e_0e_0^*$, where the two sides are $1/2$ and $1$.
The partial trace maps positive operators to positive operators and preserves the trace, so it maps density operators to density operators.
