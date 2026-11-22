---
tag: C9JJD2AVJR
kind: definition
name: Pfaffian
msc: [15A15]
topics: [DTBK11SR77]
audience: grad
defines: NH5HWBPWS9
uses: [0PBY4E9GQF, 0NHK9MFFW9, 02DKV69ZH0, 0310REJJY8, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Pfaffian
---

## Definition

The Pfaffian of an alternating matrix of even size is a signed sum of products of its entries, one product for each way to split the indices into pairs.

Let $K$ be a [[commutative ring|0310REJJY8]], let $n \ge 1$, and let $A = (a_{ij})$ be a $2n \times 2n$ matrix over $K$.
Assume that $A$ is *alternating*: $a_{ji} = -a_{ij}$ and $a_{ii} = 0$ for all $i, j$.
Let $\Pi$ be the set of [[perfect matchings|0NHK9MFFW9]] of $\{1, \dots, 2n\}$, that is, the partitions of this set into $n$ pairs.
Write $M \in \Pi$ as $\{\{i_1, j_1\}, \dots, \{i_n, j_n\}\}$ with $i_k < j_k$ for each $k$, and let $\pi_M \in S_{2n}$ be the permutation
$$\pi_M = \begin{pmatrix} 1 & 2 & 3 & 4 & \cdots & 2n - 1 & 2n \\ i_1 & j_1 & i_2 & j_2 & \cdots & i_n & j_n \end{pmatrix}.$$
The *Pfaffian* of $A$ is
$$\operatorname{pf}(A) = \sum_{M \in \Pi} \operatorname{sgn}(\pi_M) \prod_{k=1}^{n} a_{i_k j_k},$$
where $\operatorname{sgn}$ is the [[sign of a permutation|02DKV69ZH0]].
For the empty matrix ($n = 0$) we set $\operatorname{pf} = 1$, and for an alternating matrix of odd size we set $\operatorname{pf} = 0$.

## Notation

Books write $\operatorname{pf}(A)$ or $\operatorname{Pf}(A)$.
We write $\Pi$ for the set of perfect matchings of $\{1, \dots, 2n\}$ and $\pi_M$ for the permutation attached to $M \in \Pi$.

## Remarks

Each condition of the definition has a job.
The size is even because a set with an odd number of elements has no perfect matching.
The condition $a_{ji} = -a_{ij}$ means that only the entries above the diagonal are needed, and it is what makes $\operatorname{pf}(A)^2 = \det A$ true.
The condition $a_{ii} = 0$ is automatic when $2$ is invertible in $K$, but over a ring such as $\mathbb{F}_2$ it is a real extra condition.
The rule $i_k < j_k$ picks one of the two orders inside each pair, so that each pair contributes the entry $a_{i_k j_k}$ above the diagonal.

The term of $M$ does not depend on the order in which we list the pairs.
Exchanging two pairs moves two positions in the second row of $\pi_M$ at once, which is a product of two transpositions, so the sign does not change.

For $n = 2$ the three matchings give
$$\operatorname{pf}(A) = a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23}.$$
For $M = \{\{1, 3\}, \{2, 4\}\}$, the permutation $\pi_M$ sends $1, 2, 3, 4$ to $1, 3, 2, 4$, which is one transposition, so its sign is $-1$.
For $M = \{\{1, 4\}, \{2, 3\}\}$, it sends $1, 2, 3, 4$ to $1, 4, 2, 3$, which is a cycle of length $3$, so its sign is $+1$.

A case that fails: the symmetric matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{R}$ has $a_{21} = 1 \ne -1 = -a_{12}$, so it is not alternating and it has no Pfaffian in this sense.

The main facts are the [[square identity|473MBZST4D]] $\operatorname{pf}(A)^2 = \det A$, where $\det$ is the [[determinant|00KDZRW4C0]], and the rule $\operatorname{pf}(B A B^{\mathsf{T}}) = \det(B) \operatorname{pf}(A)$ for every $2n \times 2n$ matrix $B$.
Over a field of characteristic other than $2$, alternating matrices are the same as [[skew-symmetric matrices|0PBY4E9GQF]].
The concept page on the [[Pfaffian|NH5HWBPWS9]] gives the uses.

## Explanations

### L1 human

The Pfaffian adds up, with signs, one product for each way to split the indices into pairs.
For four indices there are three ways, so there are three products.
It plays for alternating matrices the role that the determinant plays for all square matrices.

### L2 human

How many terms does the Pfaffian have?
The index $1$ has $2n - 1$ possible partners, then the smallest index left has $2n - 3$ possible partners, and so on.
So $\Pi$ has $(2n - 1)(2n - 3) \cdots 3 \cdot 1$ elements: $1$ for size $2$, $3$ for size $4$ and $5 \cdot 3 \cdot 1 = 15$ for size $6$.
Compare the $6! = 720$ terms of a $6 \times 6$ determinant.
For $a_{12} = 1$, $a_{13} = 2$, $a_{14} = 3$, $a_{23} = 4$, $a_{24} = 5$ and $a_{34} = 6$, the formula gives
$$\operatorname{pf}(A) = 1 \cdot 6 - 2 \cdot 5 + 3 \cdot 4 = 8.$$
Watch out: the sign of each term comes from $\pi_M$, not from the number of pairs or from the position of the entries.

### L3 human

The Pfaffian of the matrix of indeterminates $x_{ij}$ ($i < j$) is a polynomial with integer coefficients, so the definition makes sense over every commutative ring and commutes with ring homomorphisms.
Without matchings, put $\omega = \sum_{i < j} a_{ij}\, e_i \wedge e_j$; then $\omega^n = n! \operatorname{pf}(A)\, e_1 \wedge \dots \wedge e_{2n}$ in the exterior algebra.
