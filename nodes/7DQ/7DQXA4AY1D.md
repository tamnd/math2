---
tag: 7DQXA4AY1D
kind: proof
name: Proof that row rank equals column rank by duality
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: 0TZAG60ZYT
methods: [0NTF6DMVAP]
uses: [7FA499AW3T, 0ZPB3180AY, 0W6M3PSD08, 0F0RPPJ2TT, 0EP73HK4C4, 0W809K6AW0, 0JGB7A6GTS]
sources:
  - book: isbn:9783031410253
    locator: Section 3F
---

## Proof

We read the column rank of $A$ as the rank of the map $x \mapsto Ax$ and the row rank as the rank of its dual map, and then use that a map and its dual have the same rank.
Let $A$ be an $m \times n$ matrix over a field $F$, and let $f \colon F^n \to F^m$ be the linear map $f(x) = Ax$.

1. The vector $Ax$ is the linear combination of the columns of $A$ with coefficients $x_1, \dots, x_n$.
2. So $\im f$ is the [[column space|0F0RPPJ2TT]] $\operatorname{Col}(A)$, and $\dim \operatorname{Col}(A) = \rank f$ by the definition of the [[rank|0JGB7A6GTS]].
3. The space $F^n$ is finite-dimensional, so part 4 of the theorem on the [[kernel and image of the dual map|7FA499AW3T]] gives $\rank f^* = \rank f$.
4. Let $\Phi_k \colon F^k \to (F^k)^*$ send a column $c$ to $\sum_j c_j e_j^*$, where $e_1^*, \dots, e_k^*$ is the [[dual basis|0W6M3PSD08]] of the standard basis. Since the $e_j^*$ form a basis, $\Phi_k$ is an isomorphism.
5. By the theorem on the [[matrix of the dual map|0ZPB3180AY]], $f^*$ has the matrix $A^{\mathsf{T}}$ in these dual bases, which means $f^*(\Phi_m(c)) = \Phi_n(A^{\mathsf{T}} c)$ for all $c \in F^m$.
6. Since $\Phi_m$ is onto, step 5 gives $\im f^* = \Phi_n(\operatorname{Col}(A^{\mathsf{T}}))$, by steps 1 and 2 applied to $A^{\mathsf{T}}$.
7. An isomorphism keeps the dimension of a subspace, so $\rank f^* = \dim \operatorname{Col}(A^{\mathsf{T}})$.
8. The columns of $A^{\mathsf{T}}$ are the rows of $A$ written as columns, by the definition of the [[transpose|0W809K6AW0]].
9. Writing rows as columns is a linear isomorphism from rows of length $n$ to $F^n$, and it sends the [[row space|0EP73HK4C4]] $\operatorname{Row}(A)$ onto $\operatorname{Col}(A^{\mathsf{T}})$. So $\dim \operatorname{Row}(A) = \dim \operatorname{Col}(A^{\mathsf{T}})$.
10. Steps 2, 3, 7 and 9 together give the chain below, which is the statement:
$$\dim \operatorname{Col}(A) = \rank f = \rank f^* = \dim \operatorname{Col}(A^{\mathsf{T}}) = \dim \operatorname{Row}(A).$$

## Idea

Column rank is about the outputs of $x \mapsto Ax$, and row rank is about the linear forms that the rows of $A$ define.
Those forms are exactly the pullbacks of the coordinate forms of $F^m$ under the dual map, so the row space is the image of $f^*$.
The theorem on the kernel and image of the dual map says that this image is the annihilator of $\ker f$, and the annihilator of $\ker f$ has dimension $n - \dim \ker f = \rank f$.
So the whole proof is the count $\dim (\ker f)^0 = n - \dim \ker f$, read in two ways.

## Variants

One can skip the transpose.
With forms written as rows, $f^*(y) = yA$, as in the example on [[the dual of a matrix map|QM8XZDS9TK]].
So $\im f^*$ is the set of all rows $yA$, which is $\operatorname{Row}(A)$, and step 3 finishes the proof at once.

Other proofs use row reduction to echelon form, a rank factorization $A = CR$, or orthogonality over $\R$; the statement [[row rank equals column rank|0TZAG60ZYT]] collects them.
