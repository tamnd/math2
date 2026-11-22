---
tag: F890ZBVDZV
kind: proof
name: Proof of subadditivity of the rank
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 5M6SX7JN01
uses: [0EWQEYRVA8, 0F0RPPJ2TT, 06HTJNCMPA, 0QW084460E]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
---

## Proof

We put the column space of $A + B$ inside the sum of the column spaces of $A$ and $B$, and then we bound the dimension of that sum.
Let $A$ and $B$ be $m \times n$ matrices over a field $F$, and let $a_j$ and $b_j$ be column $j$ of $A$ and of $B$.

1. Column $j$ of $A + B$ is $a_j + b_j$, by the definition of the sum of matrices.
2. By the [[definition of the column space|0F0RPPJ2TT]], $a_j \in \operatorname{Col}(A)$ and $b_j \in \operatorname{Col}(B)$, so $a_j + b_j \in \operatorname{Col}(A) + \operatorname{Col}(B)$.
3. The sum $\operatorname{Col}(A) + \operatorname{Col}(B)$ is a subspace of $F^m$ that contains every column of $A + B$, so it contains their span $\operatorname{Col}(A + B)$.
4. By the [[dimension of a subspace|0QW084460E]],
$$\dim \operatorname{Col}(A + B) \le \dim\bigl(\operatorname{Col}(A) + \operatorname{Col}(B)\bigr).$$
5. By the [[dimension formula for a sum|06HTJNCMPA]],
$$\dim\bigl(\operatorname{Col}(A) + \operatorname{Col}(B)\bigr) = \dim \operatorname{Col}(A) + \dim \operatorname{Col}(B) - \dim\bigl(\operatorname{Col}(A) \cap \operatorname{Col}(B)\bigr).$$
6. The last term is at least $0$, so steps 4 and 5 give $\dim \operatorname{Col}(A + B) \le \dim \operatorname{Col}(A) + \dim \operatorname{Col}(B)$.
By the [[definition of rank|0EWQEYRVA8]], this is $\rank(A + B) \le \rank A + \rank B$.

## Idea

The columns of $A + B$ are sums of columns of $A$ and of $B$, so they live in the space that the two column spaces span together.
That space has dimension at most the sum of the two dimensions, with a loss equal to the dimension of the overlap.
For example, if $\operatorname{Col}(A)$ and $\operatorname{Col}(B)$ are the same line, then $\operatorname{Col}(A + B)$ lies on that line, and the rank of $A + B$ is at most $1$, not $2$.

## Variants

A second proof uses the [[rank factorization|5JGAG62VN8]].
Write $A$ as a sum of $\rank A$ matrices of rank $1$ and $B$ as a sum of $\rank B$ of them.
Then $A + B$ is a sum of $\rank A + \rank B$ matrices of the form $uv^{\mathsf{T}}$, so it equals $CR$ with an inner size of $\rank A + \rank B$, and the [[rank of a product|02FDWY55AS]] bounds its rank by that number.
A third proof writes $A + B = \begin{pmatrix} A & B \end{pmatrix} \begin{pmatrix} I_n \\ I_n \end{pmatrix}$ and uses that the block matrix $\begin{pmatrix} A & B \end{pmatrix}$ has rank at most $\rank A + \rank B$.
