---
tag: B448MTVVJW
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
We check that $U$ is not invariant, and then we see the formula for the quotient operator break.

1. $U$ is not [[invariant|0ACX5QT8TE]], because $T(e_1) = (1, 1)$ is not a multiple of $e_1$.
2. So $u \mapsto T(u)$ is a map from $U$ to $\R^2$, but not a map from $U$ to $U$, and the restriction $T|_U$ is not defined.
3. Try to define $\bar T(v + U) = T(v) + U$.
   The vectors $0$ and $e_1$ represent the same coset, since $e_1 - 0 \in U$.
4. The rule gives $T(0) + U = U$ for the first representative and $T(e_1) + U = (1, 1) + U = e_2 + U$ for the second.
5. The cosets $U$ and $e_2 + U$ differ, since $e_2 \notin U$.
   So the rule gives two values on one coset, and there is no [[quotient operator|0KN7EPH7Z0]].
6. In the basis $e_1, e_2$, the lower left entry of the matrix is $1$, not $0$, so the matrix is not block upper triangular for $U$.

## Remarks

The example shows that both halves of the [[definition of restriction and quotient operators|0PFPWKBDTJ]] need the invariance of $U$.
The failure is not a failure of the map $T$: it is a failure of the chosen line.
If we take $U = \R e_2$ instead, then $T(e_2) = e_2$, so $U$ is invariant, $T|_U$ is the identity, and the quotient operator on $\R^2 / U$ is also the identity, since $T(e_1) + U = e_1 + e_2 + U = e_1 + U$.
The L2 explanation shows that $\R e_2$ is the only invariant line of $T$, so every other line fails in the same way as $\R e_1$.

## Explanations

### L1 human

The quotient operator treats all vectors of $U$ as zero.
This works only if the map sends vectors that count as zero to vectors that count as zero.
Here the map sends $e_1$, which counts as zero, to $(1, 1)$, which does not.
So the map cannot be passed to the quotient.

### L2 human

We find every invariant line of $T$.
A line $\R v$ with $v = (a, b) \ne 0$ is invariant exactly when $T v = \lambda v$ for some $\lambda$, that is,
$$a = \lambda a, \qquad a + b = \lambda b.$$
If $a \ne 0$, the first equation gives $\lambda = 1$, and then the second gives $a + b = b$, so $a = 0$, which is a contradiction.
So $a = 0$, and the only invariant line is $\R e_2$.
Watch out: choosing a complement $W$ of $U$ and calling "$T$ on $W$" the quotient operator does not help, because $T$ need not map $W$ to $W$.
