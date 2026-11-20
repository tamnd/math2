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

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
Let $U$ be a $T$-[[invariant subspace|0ACX5QT8TE]] of $V$.
The *restriction* of $T$ to $U$ is the endomorphism
$$T|_U \colon U \to U, \qquad T|_U(u) = T(u).$$
The *quotient operator* of $T$ on the [[quotient space|0BR3FY5Q8M]] $V / U$ is the endomorphism
$$\bar T \colon V / U \to V / U, \qquad \bar T(v + U) = T(v) + U.$$

## Notation

The quotient operator is also written $T_{V/U}$ or $T/U$, and it is also called the *induced map*.
With the [[quotient map|0N4F5FMQZW]] $\pi$, it is characterized by $\bar T \circ \pi = \pi \circ T$.

## Remarks

The restriction is defined because $T(u) \in U$ for $u \in U$, and it is linear because $T$ is linear.
The quotient operator is well defined: if $v + U = v' + U$, then $v - v' \in U$, so $T(v) - T(v') = T(v - v') \in U$, and $T(v) + U = T(v') + U$.
It is linear, since $\bar T((v + U) + c(w + U)) = T(v + cw) + U = (T(v) + U) + c(T(w) + U)$.
Both definitions need the invariance of $U$, see the [[non-example of a subspace that is not invariant|B448MTVVJW]].
The relation of their matrices and characteristic polynomials to those of $T$ is the [[block triangular form|ENVF51H5S3]].

## Explanations

### L1 human

If a map keeps a subspace inside itself, then it is also a map of that subspace, and this smaller map is the restriction.
If we then treat all vectors of the subspace as zero, the map still makes sense, and this is the quotient operator.
For a map of space that keeps the floor in place, the restriction acts on the floor, and the quotient operator acts on heights.

### L2 human

Let $T(x, y) = (x + 2y, 3y)$ on $\R^2$ and $U = \R e_1$.

1. $T(e_1) = e_1$, so $U$ is invariant and $T|_U = \id_U$.
2. The quotient $\R^2 / U$ has the basis $e_2 + U$.
3. $\bar T(e_2 + U) = (2, 3) + U = 3 e_2 + U$, since $(2, 0) \in U$. So $\bar T$ is multiplication by $3$.
4. The characteristic polynomial of $T$ is $(t - 1)(t - 3)$, the product of those of $T|_U$ and $\bar T$.

The trap is to think that $e_2$ is an eigenvector of $T$ because $e_2 + U$ is an eigenvector of $\bar T$: in fact $T(e_2) = (2, 3)$.

### L3 human

In module language, $U$ is an $F[x]$-submodule of $V$, and $T|_U$ and $\bar T$ are the actions of $x$ on the submodule and on the quotient module.
