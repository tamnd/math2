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

Let $A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ over any field $F$, and let $v = (1, 1) = e_1 + e_2$.
Then $v$ is not a [[generalized eigenvector|0SAAHC36J9]] of $A$ for any $\lambda \in F$.

1. For $k \ge 1$, $(A - I)^k = \operatorname{diag}(0, 1)$, so $(A - I)^k v = (0, 1) \ne 0$.
2. For $k \ge 1$, $(A - 2I)^k = \operatorname{diag}((-1)^k, 0)$, so $(A - 2I)^k v = ((-1)^k, 0) \ne 0$.
3. For $\lambda \ne 1, 2$, the matrix $A - \lambda I = \operatorname{diag}(1 - \lambda, 2 - \lambda)$ is invertible. So $(A - \lambda I)^k v \ne 0$ for all $k$.
4. So no power of any $A - \lambda I$ kills $v$.

## Remarks

The vector $v$ is a sum of two [[eigenvectors|0B5H4208Z9]], $e_1$ for $1$ and $e_2$ for $2$.
So the generalized eigenvectors for different eigenvalues, together with $0$, do not form a subspace.
Only the vectors for one fixed $\lambda$, together with $0$, form a subspace, the [[generalized eigenspace|0AJ035ZTZE]].
The argument works in every characteristic, since $1 \ne 2$ in every field and $(-1)^k \ne 0$.
A vector is a generalized eigenvector exactly when it is nonzero and lies in one generalized eigenspace.

## Explanations

### L1 human

The vector $(1, 1)$ mixes two directions that the matrix stretches by different amounts.
Removing the stretch by $1$ kills the first part, but the second part stays.
Removing the stretch by $2$ kills the second part, but the first part stays.
So no single choice of stretch factor sends the whole vector to zero.

### L2 human

Decide whether $w = (3, 0)$ and $u = (3, 5)$ are generalized eigenvectors of $A$.

1. $(A - I) w = (0, 0)$, so $w$ is a generalized eigenvector for $1$ of rank $1$.
2. For $u$, the component $3 e_1$ lies in the eigenspace for $1$, and $5 e_2$ lies in the eigenspace for $2$.
3. By the argument of steps 1 to 3, no power of any $A - \lambda I$ kills $u$.

The typical use is to remember that the generalized eigenspaces are independent: a vector with two nonzero components is in none of them.
The trap is to think that a sum of generalized eigenvectors is again one, as it is for a single eigenvalue.

### L3 human

In the decomposition $V = \bigoplus_\lambda V_\lambda$ into generalized eigenspaces, the generalized eigenvectors are the nonzero vectors with exactly one nonzero component.
For a Lie algebra, the same holds for generalized weight vectors of different weights.
