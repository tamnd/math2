---
tag: YXXTBTMPY5
kind: proof
name: Proof of the rank inequality for a product of matrices
msc: [15A03]
proves: 02FDWY55AS
uses: [0ZC9YTXZRY, 03AJKXH1AV, 032Q9FB8MT, 0QW084460E, 0QK7FPE6VE, 0TZAG60ZYT, 09GK5PS824, 09DXWYRD43]
sources:
  - url: https://statisticaloddsandends.wordpress.com/2018/05/20/rank-of-ab/
---

## Proof

We compare column spaces, and then pass to transposes for the second inequality.

1. Let $A = (a_{ij})$ be $m \times n$ and $B = (b_{jk})$ be $n \times p$. Let $\alpha_1, \dots, \alpha_n \in F^m$ be the columns of $A$.
2. By the definition of the [[matrix product|032Q9FB8MT]], entry $i$ of column $k$ of $AB$ is $\sum_{j=1}^n a_{ij} b_{jk}$. So column $k$ of $AB$ equals $\sum_{j=1}^n b_{jk} \alpha_j$.
3. Hence each column of $AB$ lies in the [[column space|03AJKXH1AV]] $\operatorname{Col}(A)$. Since $\operatorname{Col}(A)$ is a subspace, $\operatorname{Col}(AB) \subseteq \operatorname{Col}(A)$.
4. $F^m$ has dimension $m$ by [[the dimension of the coordinate space|0QK7FPE6VE]], so $\operatorname{Col}(A)$ is finite-dimensional by the [[dimension of a subspace|0QW084460E]].
5. Applying the dimension of a subspace inside $\operatorname{Col}(A)$ gives $\dim \operatorname{Col}(AB) \le \dim \operatorname{Col}(A)$. By the definition of [[rank|0ZC9YTXZRY]], $\rank(AB) \le \rank A$.
6. Step 5 holds for any two matrices whose product is defined.
7. By [[row rank equals column rank|0TZAG60ZYT]], $\rank(AB) = \rank\left((AB)^T\right)$, with the [[transpose|09DXWYRD43]].
8. By the [[transpose of a product|09GK5PS824]], $(AB)^T = B^T A^T$, where $B^T$ is $p \times n$ and $A^T$ is $n \times m$.
9. By step 6 applied to $B^T$ and $A^T$, $\rank(B^T A^T) \le \rank B^T$.
10. By row rank equals column rank again, $\rank B^T = \rank B$. So $\rank(AB) \le \rank B$.
11. By steps 5 and 10, $\rank(AB) \le \min(\rank A, \rank B)$.

## Idea

Every column of $AB$ is a combination of columns of $A$, so $AB$ cannot have a larger column space than $A$. Transposing turns $B$ into the left factor, and transposing does not change rank. So the same argument bounds $\rank(AB)$ by $\rank B$.
