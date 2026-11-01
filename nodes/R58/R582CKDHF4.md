---
tag: R582CKDHF4
kind: definition
name: Permanent
msc: [15A15]
defines: X9B1XETBPF
uses: [0JXZKX526R, 0515A6D2Y1, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Permanent_(mathematics)
---

## Definition

Let $K$ be a [[commutative ring|0310REJJY8]], and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $K$.
The *permanent* of $A$ is
$$\operatorname{perm}(A) = \sum_{\sigma \in S_n} \prod_{i=1}^{n} a_{i, \sigma(i)},$$
where $S_n$ is the [[symmetric group|0515A6D2Y1]] of permutations of $\set{1, \dots, n}$.

## Remarks

Example: for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, the two permutations give $\operatorname{perm}(A) = 1 \cdot 4 + 2 \cdot 3 = 10$, while $\det A = -2$.

The permanent is not multiplicative, unlike the [[determinant|00KDZRW4C0]].
For $J = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $\operatorname{perm}(J) = 2$, but $J^2 = 2J$ has permanent $8 \ne 2 \cdot 2$.

The permanent is linear in each row and each column, and it does not change when rows or columns are permuted.
If $A$ is the $0/1$ biadjacency matrix of a [[bipartite graph|0ZVQKTRKVQ]] with $n$ vertices on each side, then $\operatorname{perm}(A)$ is the number of [[perfect matchings|0NHK9MFFW9]] of the graph.
The permanent of the $n \times n$ all-ones matrix is $n!$.

## Explanations

### L1 human

The permanent is computed like the determinant, but every term gets a plus sign.
This small change makes it lose most of the good algebraic properties of the determinant.
