---
tag: 9MXPNHHMT1
kind: definition
name: Frobenius algebra
msc: [16L60, 16D50]
defines: 8EVP1K2CZH
uses: [04C5ZBG1WT, 3CTW1P4HBP, 0SQZMXB6GP, 01NHFZF2SK]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_algebra
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $A$ be a finite-dimensional [[associative algebra|3CTW1P4HBP]] over $k$ with identity.
The algebra $A$ is a *Frobenius algebra* if there is a [[bilinear form|0SQZMXB6GP]] $\sigma \colon A \times A \to k$ such that:

1. $\sigma$ is [[nondegenerate|01NHFZF2SK]];
2. $\sigma(ab, c) = \sigma(a, bc)$ for all $a, b, c \in A$.

## Remarks

Example: the matrix algebra $M_n(k)$ with $\sigma(a, b) = \tr(ab)$.
Clause 2 holds because both sides equal $\tr(abc)$.
Clause 1 holds because $\tr(a E_{ji}) = a_{ij}$ for the matrix unit $E_{ji}$, so $\sigma(a, \cdot) = 0$ forces $a = 0$.
Another example is the group algebra $k[G]$ of a finite group $G$, with $\sigma(a, b)$ the coefficient of the identity element of $G$ in $ab$.
Non-example: $A = k[x, y]/(x^2, xy, y^2)$, with basis $1, x, y$, is not Frobenius.
If $\sigma$ satisfies clause 2, then $\sigma(a, b) = \lambda(ab)$ for the linear form $\lambda = \sigma(1, \cdot)$.
The plane spanned by $x$ and $y$ meets $\ker \lambda$ in some nonzero $u = \alpha x + \beta y$.
Since $ub \in k u$ for every $b \in A$, $\sigma(u, b) = 0$ for all $b$, and clause 1 fails.
Equivalent forms: $A$ is Frobenius if and only if some linear form $\lambda \colon A \to k$ has a kernel that contains no nonzero left ideal.
This holds if and only if $A \cong \Hom_k(A, k)$ as left $A$-modules.
If moreover $\sigma$ is symmetric, $A$ is called a symmetric algebra.
