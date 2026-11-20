---
tag: ~cdde18e6
kind: example
name: No quotient operator for a subspace that is not invariant
msc: ["15A04"]
topics: [Z6S6PWMJPH]
audience: ug1
not_instance_of:
  - target: 0KN7EPH7Z0
    note: the line spanned by e1 is not invariant, so the rule v + U to T(v) + U gives two different values on one coset and defines no quotient operator
  - target: 0ACX5QT8TE
    note: T sends e1 to e1 + e2, which is not on the line spanned by e1
uses: [0PFPWKBDTJ, 0EP59ESQ94, 0SVR29SV1V]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
---

## Example

Let $T(x, y) = (x, x + y)$ on $\R^2$, with the matrix $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, and let $U = \R e_1$.

1. $U$ is not [[invariant|0ACX5QT8TE]]: $T(e_1) = (1, 1)$ is not a multiple of $e_1$.
2. So $u \mapsto T(u)$ is a map from $U$ to $\R^2$, but not a map from $U$ to $U$, and the restriction $T|_U$ is not defined.
3. Try to define $\bar T(v + U) = T(v) + U$. The vectors $0$ and $e_1$ represent the same coset, since $e_1 - 0 \in U$.
4. But $T(0) + U = U$, while $T(e_1) + U = (1, 1) + U = e_2 + U$.
5. The cosets $U$ and $e_2 + U$ differ, since $e_2 \notin U$. So the rule gives two values on one coset, and there is no [[quotient operator|0KN7EPH7Z0]].
6. In the basis $(e_1, e_2)$, the lower left entry of the matrix is $1$, not $0$, so the matrix is not block upper triangular.

## Remarks

The example shows that both halves of the definition of restriction and quotient operators need the invariance of $U$.
If we take $U = \R e_2$ instead, then $T(e_2) = e_2$, so $U$ is invariant, and the quotient operator on $\R^2 / U$ is the identity.
In general, the line $\R(a, b)$ is invariant under this $T$ only when $a = 0$, since $T(a, b) = (a, a + b)$ is a multiple of $(a, b)$ only then.

## Explanations

### L1 human

The quotient operator treats all vectors of $U$ as zero.
This only works if the map sends zero-like vectors to zero-like vectors.
Here the map sends $e_1$, which counts as zero, to a vector that does not count as zero.
So the map cannot be passed to the quotient.

### L2 human

We check every line through $0$.

1. Let $v = (a, b) \ne 0$. Then $T v = (a, a + b)$.
2. If $T v = \lambda v$, then $a = \lambda a$ and $a + b = \lambda b$.
3. If $a \ne 0$, then $\lambda = 1$ and $a + b = b$, so $a = 0$, a contradiction.
4. So $a = 0$, and the only invariant line is $\R e_2$.

The trap is to choose a complement $W$ of $U$ and call $T|_W$ the quotient operator, although $T|_W$ need not map $W$ to $W$.
