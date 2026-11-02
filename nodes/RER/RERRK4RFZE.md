---
tag: RERRK4RFZE
kind: definition
name: Affine independence
msc: [51N10, 15A03]
defines: JWK49HMHYT
uses: [09XNAPTJQ7, 0CRMGPAH83, 0KJH6SRFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_space
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $P$ be an [[affine space|09XNAPTJQ7]] over $V$.
Let $p_0, \dots, p_k$ be points of $P$.
They are *affinely independent* if the vectors $p_1 - p_0, \dots, p_k - p_0$ of $V$ are [[linearly independent|0CRMGPAH83]].

## Remarks

Example: in $\R^2$, the points $(0,0)$, $(1,0)$, $(0,1)$ are affinely independent, since the vectors $(1,0)$ and $(0,1)$ are linearly independent.
Non-example: the points $(0,0)$, $(1,1)$, $(2,2)$ are not, since $(2,2) = 2 \cdot (1,1)$.
The condition does not depend on which point plays the role of $p_0$.
An equivalent form: for all $\lambda_0, \dots, \lambda_k \in F$ with $\sum_i \lambda_i = 0$ and $\sum_i \lambda_i (p_i - p_0) = 0$, all $\lambda_i$ are $0$.
Another equivalent form: no $p_j$ is an [[affine combination|0KJH6SRFZK]] of the other points.
In an affine space of dimension $n$, at most $n + 1$ points can be affinely independent.
