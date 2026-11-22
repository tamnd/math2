---
tag: B4TGR752QE
kind: proof
name: Proof that the transpose times a real matrix has the same rank
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug2
proves: FGPT52R1ZE
uses: [0PQ2GGY1QV, 09GK5PS824, 05HQYM0R4G, TR48YQGCCA, 0TZAG60ZYT, 0EWQEYRVA8]
methods: [MKHVRNW68H]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
---

## Proof

We show that $A$ and $A^{\mathsf{T}} A$ have the same null space, and then rank-nullity gives the same rank.
Let $A$ be a real $m \times n$ matrix.

1. We claim that $\operatorname{Null}(A^{\mathsf{T}} A) = \operatorname{Null}(A)$, where $\operatorname{Null}$ is the [[null space|0PQ2GGY1QV]].
If $Ax = 0$, then $A^{\mathsf{T}} A x = A^{\mathsf{T}} 0 = 0$, so $\operatorname{Null}(A) \subseteq \operatorname{Null}(A^{\mathsf{T}} A)$.
2. For the other inclusion, let $A^{\mathsf{T}} A x = 0$.
Multiplying on the left by $x^{\mathsf{T}}$ gives $x^{\mathsf{T}} A^{\mathsf{T}} A x = 0$.
3. By the [[transpose of a product|09GK5PS824]], $x^{\mathsf{T}} A^{\mathsf{T}} = (Ax)^{\mathsf{T}}$.
So with $y = Ax \in \mathbb{R}^m$, step 2 says that the [[dot product|05HQYM0R4G]] $y \cdot y = y^{\mathsf{T}} y$ is $0$.
4. The number $y \cdot y = y_1^2 + \dots + y_m^2$ is a sum of real squares, so it is $0$ only when every $y_i$ is $0$.
Hence $Ax = y = 0$, and the claim is proved.
5. Both $A$ and $A^{\mathsf{T}} A$ have $n$ columns, so the [[rank-nullity theorem for matrices|TR48YQGCCA]] gives
$$\rank(A^{\mathsf{T}} A) = n - \dim \operatorname{Null}(A^{\mathsf{T}} A) = n - \dim \operatorname{Null}(A) = \rank A.$$
6. The matrix $A^{\mathsf{T}}$ is again real, and $(A^{\mathsf{T}})^{\mathsf{T}} = A$, so step 5 applied to $A^{\mathsf{T}}$ gives $\rank(A A^{\mathsf{T}}) = \rank A^{\mathsf{T}}$.
7. By [[row rank equals column rank|0TZAG60ZYT]], $\rank A^{\mathsf{T}} = \rank A$, so $\rank(A A^{\mathsf{T}}) = \rank A$ as well, with rank as in the [[definition|0EWQEYRVA8]].

## Idea

The number $x^{\mathsf{T}} A^{\mathsf{T}} A x$ is the squared length of $Ax$.
So if $A^{\mathsf{T}} A$ kills $x$, then $Ax$ has length $0$ and $A$ kills $x$ too.
The two matrices kill the same vectors and have the same number of columns, and rank-nullity turns equal null spaces into equal ranks.
For example, with $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, both $A$ and $A^{\mathsf{T}} A = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$ kill exactly the multiples of $(1, -1)$, and both have rank $1$.

## Variants

Over $\mathbb{C}$, the same proof with the conjugate transpose $A^*$ and the Hermitian product $\langle y, y \rangle = \sum_i \lvert y_i \rvert^2$ gives $\rank(A^* A) = \rank A$.
Without conjugation the proof breaks at step 4, and the [[complex counterexample|AX5JTDETRA]] shows that the statement breaks too.
The singular value decomposition gives another proof.
The rank of $A$ is the number of its nonzero singular values, counted with multiplicity.
The rank of the symmetric matrix $A^{\mathsf{T}} A$ is the number of its nonzero eigenvalues, counted with multiplicity, and these eigenvalues are the squares of those singular values.
