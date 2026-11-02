---
tag: XBJEDC18B1
kind: statement
role: lemma
name: Cotlar–Stein lemma
msc: [42B20, 47B38]
uses: [HM2HHE3J51, 6HSJBJ8TTQ, 06EKW1AKXF]
about: [06EKW1AKXF]
sources:
  - url: https://en.wikipedia.org/wiki/Cotlar%E2%80%93Stein_lemma
same_as:
  wikidata: Q5175397
  wikipedia: Cotlar–Stein lemma
---

## Statement

Let $H_1$ and $H_2$ be [[Hilbert spaces|HM2HHE3J51]], let $N \ge 1$, and let $T_1, \dots, T_N \colon H_1 \to H_2$ be bounded linear operators.
Write $T_i^*$ for the [[adjoint|6HSJBJ8TTQ]] of $T_i$ and $\norm{\cdot}$ for the [[operator norm|06EKW1AKXF]].
Let $A \ge 0$ and assume that
$$\sup_{i} \sum_{j=1}^{N} \norm{T_i^* T_j}^{1/2} \le A \quad \text{and} \quad \sup_{i} \sum_{j=1}^{N} \norm{T_i T_j^*}^{1/2} \le A.$$
Then
$$\Big\Vert \sum_{i=1}^{N} T_i \Big\Vert \le A.$$

## Remarks

The bound does not depend on $N$.
So let $(T_i)$ be an infinite sequence with the same two hypotheses.
Then the partial sums are bounded by $A$, and the series $\sum_i T_i$ converges in the strong operator topology to an operator of norm at most $A$.

Idea of the proof.
Let $T = \sum_i T_i$ and let $m \ge 1$.
Since $\norm{T}^{2m} = \norm{(T^* T)^m}$, expand $(T^*T)^m$ as a sum of $N^{2m}$ products $T_{i_1}^* T_{i_2} T_{i_3}^* \cdots T_{i_{2m}}$.
Bound each product in two ways, by grouping the factors in pairs $T_{i_1}^* T_{i_2}, T_{i_3}^* T_{i_4}, \dots$ or in pairs $T_{i_2} T_{i_3}^*, \dots$, and take the geometric mean of the two bounds.
Summing over the indices gives $\norm{T}^{2m} \le N A^{2m}$, and letting $m \to \infty$ gives $\norm{T} \le A$.

Example.
If $T_i^* T_j = 0$ and $T_i T_j^* = 0$ for all $i \ne j$, the operators act on mutually orthogonal pieces.
The two hypotheses then reduce to $\norm{T_i} \le A$ for each $i$, and the lemma gives $\norm{\sum_i T_i} \le \max_i \norm{T_i}$.

One hypothesis alone is not enough.
Let $(e_k)$ be an orthonormal basis of a Hilbert space $H$ of dimension at least $N$, and let $T_i x = \ip{x, e_1} e_i$ for $i = 1, \dots, N$.
Then $T_i^* T_j = 0$ for $i \ne j$ and $\norm{T_i^* T_i} = 1$, so the first sum equals $1$.
But $\norm{T_i T_j^*} = 1$ for all $i, j$, so the second sum is $N$.
Indeed $\sum_i T_i$ sends $e_1$ to $e_1 + \cdots + e_N$, so its norm is $\sqrt{N}$.

## Explanations

### L1 human

Adding many operators can make a large operator, even if each piece is small.
The lemma says that this does not happen when the pieces are almost orthogonal to each other, both on the input side and on the output side.
The amount of interaction between two pieces is measured by $\norm{T_i^* T_j}$ and $\norm{T_i T_j^*}$, and these must decay fast enough.

### L2 human

The lemma is the basic tool of almost orthogonality in harmonic analysis.
A singular integral or pseudodifferential operator is cut into pieces that live at one scale or one frequency band, and the lemma gives $L^2$ boundedness of the sum.
A classical use is the proof of the Calderón–Vaillancourt theorem on pseudodifferential operators.
It only works on Hilbert spaces, since the proof uses the identity $\norm{T}^2 = \norm{T^*T}$.
