---
tag: YXXTBTMPY5
kind: proof
name: Proof of the rank inequality for a product of matrices
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 02FDWY55AS
uses: [0ZC9YTXZRY, 03AJKXH1AV, 032Q9FB8MT, 0QW084460E, 0QK7FPE6VE, 0TZAG60ZYT, 09GK5PS824, 09DXWYRD43]
methods: [0NTF6DMVAP]
sources:
  - url: https://statisticaloddsandends.wordpress.com/2018/05/20/rank-of-ab/
---

## Proof

We compare column spaces to get $\rank(AB) \le \rank A$, and then we pass to transposes to get $\rank(AB) \le \rank B$.
Let $A = (a_{ij})$ be an $m \times n$ matrix and $B = (b_{jk})$ an $n \times p$ matrix over a field $F$, and let $\alpha_1, \dots, \alpha_n \in F^m$ be the columns of $A$.

1. By the definition of the [[matrix product|032Q9FB8MT]], entry $i$ of column $k$ of $AB$ is $\sum_{j=1}^n a_{ij} b_{jk}$.
So column $k$ of $AB$ is
$$\sum_{j=1}^n b_{jk} \alpha_j,$$
a combination of the columns of $A$.
2. Hence every column of $AB$ lies in the [[column space|03AJKXH1AV]] $\operatorname{Col}(A)$.
This is a subspace, so it also contains the span of those columns, and $\operatorname{Col}(AB) \subseteq \operatorname{Col}(A)$.
3. The space $F^m$ has dimension $m$, by the [[dimension of the coordinate space|0QK7FPE6VE]], so $\operatorname{Col}(A)$ is finite-dimensional.
A subspace of a finite-dimensional space has dimension at most that of the space, by the [[dimension of a subspace|0QW084460E]], so $\dim \operatorname{Col}(AB) \le \dim \operatorname{Col}(A)$.
4. By the definition of [[rank|0ZC9YTXZRY]], step 3 says $\rank(AB) \le \rank A$.
This holds for any two matrices whose product is defined.
5. By the [[transpose of a product|09GK5PS824]], the [[transpose|09DXWYRD43]] of $AB$ is $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$, the product of a $p \times n$ and an $n \times m$ matrix.
6. Step 4 applied to the product $B^{\mathsf{T}} A^{\mathsf{T}}$ gives $\rank(B^{\mathsf{T}} A^{\mathsf{T}}) \le \rank B^{\mathsf{T}}$.
7. By [[row rank equals column rank|0TZAG60ZYT]], a matrix and its transpose have the same rank, so step 6 reads $\rank(AB) \le \rank B$.
8. Steps 4 and 7 give $\rank(AB) \le \min(\rank A, \rank B)$.

## Idea

Every column of $AB$ is a combination of the columns of $A$, with coefficients taken from a column of $B$.
So $AB$ cannot have a larger column space than $A$.
Transposing makes $B$ the left factor, and transposing does not change rank, so the same argument bounds $\rank(AB)$ by $\rank B$.

## Variants

The bound $\rank(AB) \le \rank B$ also follows without transposes.
The map $x \mapsto Ax$ sends $\operatorname{Col}(B)$ onto $\operatorname{Col}(AB)$, since $A(Bx) = (AB)x$.
A linear map sends a spanning family to a spanning family, so the image of a subspace has dimension at most that of the subspace.
This version also measures the loss: by rank-nullity on $\operatorname{Col}(B)$, $\rank B - \rank(AB) = \dim(\operatorname{Col}(B) \cap \operatorname{Null}(A))$, and that is the start of the proof of the [[Frobenius inequality|GS8WE1ZYV9]].
