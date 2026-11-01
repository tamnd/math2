---
tag: C9JJD2AVJR
kind: definition
name: Pfaffian
msc: [15A15]
defines: NH5HWBPWS9
uses: [0PBY4E9GQF, 0NHK9MFFW9, 02DKV69ZH0, 0310REJJY8, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Pfaffian
---

## Definition

Let $K$ be a [[commutative ring|0310REJJY8]], let $n \ge 1$, and let $A = (a_{ij})$ be a $2n \times 2n$ matrix over $K$.
Assume that $A$ is alternating: $a_{ji} = -a_{ij}$ and $a_{ii} = 0$ for all $i, j$.
Let $\Pi$ be the set of [[perfect matchings|0NHK9MFFW9]] of $\set{1, \dots, 2n}$, that is, partitions into $n$ pairs.
Write $M \in \Pi$ as $\set{\set{i_1, j_1}, \dots, \set{i_n, j_n}}$ with $i_k < j_k$, and let $\pi_M$ be the permutation $1 \mapsto i_1, 2 \mapsto j_1, \dots, 2n-1 \mapsto i_n, 2n \mapsto j_n$.
The *Pfaffian* of $A$ is
$$\operatorname{pf}(A) = \sum_{M \in \Pi} \sgn(\pi_M) \prod_{k=1}^{n} a_{i_k j_k},$$
where $\sgn$ is the [[sign of a permutation|02DKV69ZH0]].

## Remarks

The term of $M$ does not depend on the order in which the pairs are listed, because exchanging two pairs is an even permutation.
For an alternating matrix of odd size, the Pfaffian is set to $0$.

Example: for $n = 2$ there are three matchings, and
$$\operatorname{pf}(A) = a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23}.$$
For the matching $\set{\set{1,3}, \set{2,4}}$, the permutation $\pi_M$ is $1 \mapsto 1, 2 \mapsto 3, 3 \mapsto 2, 4 \mapsto 4$, a transposition, so its sign is $-1$.

Non-example: the symmetric matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is not alternating, because $a_{21} \ne -a_{12}$ unless $2 = 0$ in $K$, so it has no Pfaffian in this sense.

The main facts are $\operatorname{pf}(A)^2 = \det A$ and $\operatorname{pf}(B A B^T) = \det(B) \operatorname{pf}(A)$ for every $2n \times 2n$ matrix $B$, where $\det$ is the [[determinant|00KDZRW4C0]].
Alternating matrices over a field are the same as [[skew-symmetric matrices|0PBY4E9GQF]] when the characteristic is not $2$.

## Explanations

### L1 human

The Pfaffian adds up, with signs, one product for each way to split the indices into pairs.
It plays for skew-symmetric matrices the role that the determinant plays for all square matrices.
