---
tag: EWGV69Z2VZ
kind: example
name: A sum of eigenvectors that is not a generalized eigenvector
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
not_instance_of:
  - target: 01H6QKWGDH
    note: the vector (1, 1) is not killed by any power of A - λI for any scalar λ, since it has nonzero components for the two eigenvalues 1 and 2
  - target: 0AJ035ZTZE
    note: the line spanned by (1, 1) is not a generalized eigenspace of A, and it meets the two generalized eigenspaces only in 0
uses: [0SAAHC36J9, 0B5H4208Z9, 0BNEXSKNRV]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
---

## Example

Let $F$ be any field, let $A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ over $F$, and let $v = (1, 1) = e_1 + e_2$.
We show that $v$ is not a [[generalized eigenvector|0SAAHC36J9]] of $A$ for any $\lambda \in F$.
Every power of a diagonal matrix is diagonal, with the powers of the diagonal entries, so each step is one multiplication.

1. Take $\lambda = 1$.
   For $k \ge 1$ we get $(A - I)^k = \operatorname{diag}(0, 1)$, so $(A - I)^k v = (0, 1) \ne 0$.
2. Take $\lambda = 2$.
   For $k \ge 1$ we get $(A - 2I)^k = \operatorname{diag}((-1)^k, 0)$, so $(A - 2I)^k v = ((-1)^k, 0) \ne 0$.
3. Take $\lambda \ne 1, 2$.
   Then $A - \lambda I = \operatorname{diag}(1 - \lambda, 2 - \lambda)$ has two nonzero diagonal entries, so it is invertible.
   A power of an invertible matrix is invertible, so $(A - \lambda I)^k v \ne 0$ for all $k$.
4. So no power of any $A - \lambda I$ sends $v$ to $0$.

## Remarks

The vector $v$ is the sum of two [[eigenvectors|0B5H4208Z9]], $e_1$ for $1$ and $e_2$ for $2$.
So the generalized eigenvectors for different eigenvalues, together with $0$, do not form a subspace.
Only the vectors for one fixed $\lambda$, together with $0$, form a subspace, the [[generalized eigenspace|0AJ035ZTZE]].
A vector is a generalized eigenvector exactly when it is nonzero and lies in one generalized eigenspace.

The argument works in every field, because $1 - 2 = -1$ is never zero and $(-1)^k \ne 0$.
In characteristic $2$ the matrix becomes $\operatorname{diag}(1, 0)$, and the same steps apply with $2 = 0$.
If we change $A$ to the identity, then $v$ becomes an eigenvector for $1$, since both entries now carry the same eigenvalue.

## Explanations

### L1 human

The vector $(1, 1)$ mixes two directions that the matrix stretches by different amounts.
Removing the stretch by $1$ kills the first part, but the second part stays.
Removing the stretch by $2$ kills the second part, but the first part stays.
So no single choice of stretch factor sends the whole vector to zero.

### L2 human

Decide whether $w = (3, 0)$ and $u = (3, 5)$ are generalized eigenvectors of $A$.

1. We have $(A - I) w = (0, 0)$, so $w$ is a generalized eigenvector for $1$ of rank $1$.
2. For $u$, the part $3 e_1$ lies in the eigenspace for $1$, and the part $5 e_2$ lies in the eigenspace for $2$.
3. As in steps 1 and 2 above, $(A - I)^k u = (0, 5)$ and $(A - 2I)^k u = (3 (-1)^k, 0)$, and both are nonzero.
4. Step 3 of the example handles every other $\lambda$, so $u$ is not a generalized eigenvector.

The typical use is to remember that the generalized eigenspaces are independent, so a vector with two nonzero parts lies in none of them.
Watch out: a sum of generalized eigenvectors for one eigenvalue is again one, if it is nonzero, but a sum for two eigenvalues is not.

### L3 human

When $V = \bigoplus_\lambda V_\lambda$ is the [[decomposition into generalized eigenspaces|0Z3GDY89T5]], the generalized eigenvectors are the nonzero vectors with exactly one nonzero component.
The same holds for generalized weight vectors of different weights for a commuting family of maps.
