---
tag: 0PFPWKBDTJ
kind: definition
name: Restriction and quotient operators
msc: ["15A04", "47A15"]
topics: [Z6S6PWMJPH]
audience: ug1
defines: 0KN7EPH7Z0
uses: [0EP59ESQ94, 0SVR29SV1V, 0J0SK5FF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Definition

An invariant subspace gives two new linear maps: the original map on the subspace, and the map it induces on the quotient space.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
Let $U$ be a $T$-[[invariant subspace|0ACX5QT8TE]] of $V$.
The *restriction* of $T$ to $U$ is the endomorphism
$$T|_U \colon U \to U, \qquad T|_U(u) = T(u).$$
The *quotient operator* of $T$ on the [[quotient space|0BR3FY5Q8M]] $V / U$ is the endomorphism
$$\bar T \colon V / U \to V / U, \qquad \bar T(v + U) = T(v) + U.$$

## Notation

The quotient operator is also written $T_{V/U}$ or $T/U$, and it is also called the *induced map*.
With the [[quotient map|0N4F5FMQZW]] $\pi \colon V \to V / U$, it is the unique linear map with $\bar T \circ \pi = \pi \circ T$.

## Remarks

Each part of the definition uses the invariance of $U$ in its own way.
The restriction has $U$ as its target, and that is allowed only because $T(u) \in U$ for $u \in U$.
Its linearity comes from the linearity of $T$.

The quotient operator is defined on cosets, so we must check that the value does not depend on the representative.
If $v + U = v' + U$, then $v - v' \in U$, so invariance gives $T(v) - T(v') = T(v - v') \in U$, and hence $T(v) + U = T(v') + U$.
It is linear, since
$$\bar T\big((v + U) + c(w + U)\big) = T(v + cw) + U = \big(T(v) + U\big) + c\big(T(w) + U\big).$$

For a small example, let $T(x, y) = (x, 2y)$ and $U = \R e_1$: the restriction is the identity of $U$, and the quotient operator is multiplication by $2$ on the line $\R^2 / U$.
For a failing case, keep $U = \R e_1$ but take $T(x, y) = (x, x + y)$: then $T(e_1) = (1, 1) \notin U$, and the [[rule gives two values on one coset|B448MTVVJW]].
The [[concept page|0KN7EPH7Z0]] works through larger examples, and the [[block triangular form|ENVF51H5S3]] relates the matrices and characteristic polynomials of both maps to those of $T$.

## Explanations

### L1 human

If a map keeps a subspace inside itself, then it is also a map of that subspace, and this smaller map is the restriction.
If we then treat all vectors of the subspace as zero, the map still makes sense, and this is the quotient operator.
For a map of space that keeps the floor in place, the restriction acts on the floor, and the quotient operator acts on heights.

### L2 human

Let $T(x, y) = (x + 2y, 3y)$ on $\R^2$ and $U = \R e_1$.
Since $T(e_1) = e_1$, the line $U$ is invariant and $T|_U = \id_U$.
The quotient $\R^2 / U$ has the basis $e_2 + U$, and
$$\bar T(e_2 + U) = (2, 3) + U = 3 e_2 + U,$$
because $(2, 0) \in U$.
So $\bar T$ is multiplication by $3$, and the characteristic polynomial $(t - 1)(t - 3)$ of $T$ is the product of those of $T|_U$ and $\bar T$.
Watch out: $e_2 + U$ is an eigenvector of $\bar T$, but $e_2$ is not an eigenvector of $T$, since $T(e_2) = (2, 3)$.

### L3 human

In module language, $U$ is an $F[x]$-submodule of $V$, and $T|_U$ and $\bar T$ are the actions of $x$ on the submodule and on the quotient module.
