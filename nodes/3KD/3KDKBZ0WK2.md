---
tag: 3KDKBZ0WK2
kind: statement
role: proposition
name: Adjugate of a product
aliases: [product-rule-for-adjugates]
msc: ["15A09", "15A15"]
topics: [DTBK11SR77]
audience: ug2
about: [07W9H8QF38]
uses: [0GMPYM0NSR, 076JGP6R3T, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Properties
---

## Statement

The adjugate obeys the same algebraic rules as the inverse, up to powers of the determinant, and these rules hold even for singular matrices.
Let $K$ be a commutative ring, let $n \ge 2$, and let $A$ and $B$ be $n \times n$ matrices over $K$.
Let $\operatorname{adj}$ denote the [[adjugate|0GMPYM0NSR]].

1. $\operatorname{adj}(AB) = \operatorname{adj} B \operatorname{adj} A$.
2. $\operatorname{adj}(A^{\mathsf{T}}) = (\operatorname{adj} A)^{\mathsf{T}}$, where $A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]].
3. $\operatorname{adj}(cA) = c^{n-1} \operatorname{adj} A$ for every $c \in K$.
4. $\det(\operatorname{adj} A) = (\det A)^{n-1}$.

## Remarks

### A check with two shears

Take
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \qquad AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}.$$
The $2 \times 2$ rule (swap the diagonal, negate the rest) gives
$$\operatorname{adj} A = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \qquad \operatorname{adj} B = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}, \qquad \operatorname{adj}(AB) = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}.$$
Multiply in the reversed order:
$$\operatorname{adj} B \operatorname{adj} A = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix},$$
which agrees with $\operatorname{adj}(AB)$.

### Why the order is reversed

The order in part 1 cannot be kept.
For the same two matrices,
$$\operatorname{adj} A \operatorname{adj} B = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix},$$
which is not $\operatorname{adj}(AB)$.
The reason is the same as for inverses: when $A$ and $B$ are invertible, $\operatorname{adj} A = (\det A) A^{-1}$, and $(AB)^{-1} = B^{-1} A^{-1}$ reverses the order.

### The exponents

Part 3 has the exponent $n - 1$ because each entry of $\operatorname{adj}(cA)$ is a minor of size $n - 1$, and each of its $n - 1$ rows carries a factor $c$.
Part 4 has the exponent $n - 1$ as well.
For the matrix $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$ of determinant $-3$, the adjugate found in the [[worked example|BDHT6DBGC9]] has determinant
$$2 (33 - 36) - 4 (-6 + 18) - 3 (12 - 33) = -6 - 48 + 63 = 9 = (-3)^2.$$

### What it gives you

For invertible matrices, part 1 is the identity $\det(AB) (AB)^{-1} = (\det B) B^{-1} (\det A) A^{-1}$, so it adds nothing new there.
Its value is for singular matrices and for matrices over rings, where no inverse exists.
By induction, part 1 gives $\operatorname{adj}(A^k) = (\operatorname{adj} A)^k$ for every $k \ge 1$.

### The adjugate does not determine the matrix

For odd $n$, part 3 with $c = -1$ gives $\operatorname{adj}(-A) = (-1)^{n-1} \operatorname{adj} A = \operatorname{adj} A$, so $A$ and $-A$ have the same adjugate.
For $n \ge 3$, every matrix over a field of rank at most $n - 2$ has adjugate $0$, by the [[rank of the adjugate|9CJME5W96T]].

### Generalizations

Applying the adjugate twice gives $\operatorname{adj}(\operatorname{adj} A) = (\det A)^{n-2} A$ for $n \ge 2$.
For $n = 2$ this says that $\operatorname{adj}(\operatorname{adj} A) = A$, which you can see from the $2 \times 2$ rule.
The [[Cauchy-Binet formula|08WE2W7DYS]] gives the rule $C_k(AB) = C_k(A) C_k(B)$ for the compound matrices $C_k$ of $k \times k$ minors, and part 1 is its relative for $k = n - 1$, with the signs and the transpose of the adjugate reversing the order.

## Explanations

### L1 human

The adjugate of a product is the product of the adjugates in the opposite order.
This is the same rule as for inverses: to undo "first $B$, then $A$", you undo $A$ first and then $B$.
The surprise is that the rule still holds for matrices that have no inverse at all.

### L2 human

Here is a typical use: show that $\operatorname{adj} A$ is symmetric when $A$ is symmetric.
By part 2, $(\operatorname{adj} A)^{\mathsf{T}} = \operatorname{adj}(A^{\mathsf{T}}) = \operatorname{adj} A$.
For example, $A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ has $\operatorname{adj} A = \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$, which is symmetric.
In the same way, part 1 shows that the adjugate of an orthogonal matrix $Q$ over $\mathbb{R}$ satisfies $\operatorname{adj}(Q) \operatorname{adj}(Q^{\mathsf{T}}) = \operatorname{adj}(Q^{\mathsf{T}} Q) = \operatorname{adj}(I_n) = I_n$.
Watch out: part 4 has the exponent $n - 1$, not $n$; for $A = 2 I_3$ the adjugate is $4 I_3$, with determinant $64 = 8^2$.

### L3 human

Part 1 says that $A \mapsto \operatorname{adj} A$ reverses products on the multiplicative monoid $M_n(K)$, so it is an anti-homomorphism of monoids.
Structurally it comes from the functoriality of the exterior power $\Lambda^{n-1}$, together with the duality $\Lambda^{n-1} V \cong V^{*} \otimes \Lambda^n V$, which turns the order around.
The [[proof|GMSSYTZ7X7]] avoids this language and uses Cauchy-Binet and the generic matrix.
