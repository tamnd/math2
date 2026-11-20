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

Let $K$ be a commutative ring, let $n \ge 2$, and let $A$, $B$ be $n \times n$ matrices over $K$.
Let $\operatorname{adj}$ be the [[adjugate|0GMPYM0NSR]].

1. $\operatorname{adj}(AB) = \operatorname{adj} B \operatorname{adj} A$.
2. $\operatorname{adj}(A^{T}) = (\operatorname{adj} A)^{T}$, for the [[transpose|0W809K6AW0]].
3. $\operatorname{adj}(cA) = c^{n-1} \operatorname{adj} A$ for $c \in K$.
4. $\det(\operatorname{adj} A) = (\det A)^{n-1}$.

## Remarks

### Why each hypothesis is needed

The order in part 1 is reversed, as for inverses; $\operatorname{adj}(AB) = \operatorname{adj} A \operatorname{adj} B$ fails in general.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, $\operatorname{adj} A \operatorname{adj} B = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, but $\operatorname{adj}(AB) = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.

### Consequences

- For invertible $A$ and $B$, part 1 is $(\det AB)(AB)^{-1} = (\det B) B^{-1} (\det A) A^{-1}$.
- Part 1 holds for singular matrices too, where inverses do not exist.
- $\operatorname{adj}(A^k) = (\operatorname{adj} A)^k$ for $k \ge 1$.

### Converse

The adjugate does not determine the matrix.
For odd $n$, part 3 gives $\operatorname{adj}(-A) = (-1)^{n-1} \operatorname{adj} A = \operatorname{adj} A$.
For $n \ge 3$, every matrix of rank at most $n - 2$ has adjugate $0$, by the [[rank of the adjugate|9CJME5W96T]].

### Generalizations

The same proof with the [[Cauchy-Binet formula|08WE2W7DYS]] for $k \times k$ minors shows that the compound matrices satisfy $C_k(AB) = C_k(A) C_k(B)$.
For $n \ge 3$, $\operatorname{adj}(\operatorname{adj} A) = (\det A)^{n-2} A$.

## Explanations

### L1 human

The adjugate of a product is the product of the adjugates in the opposite order.
This is the same rule as for inverses, and it holds even when no inverse exists.

### L2 human

Check part 1 for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.

1. $AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, so $\operatorname{adj}(AB) = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
2. $\operatorname{adj} B = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$ and $\operatorname{adj} A = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.
3. $\operatorname{adj} B \operatorname{adj} A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, which agrees with step 1.

The typical use is in proofs over rings, where inverses are not available.
A trap: part 4 has exponent $n - 1$, not $n$.

### L3 human

Part 1 says that $A \mapsto \operatorname{adj} A$ is an anti-homomorphism of the multiplicative monoid $M_n(K)$.
It is the functoriality of $\Lambda^{n-1}$, combined with the duality $\Lambda^{n-1} V \cong V^{*} \otimes \Lambda^n V$, which reverses the order.
