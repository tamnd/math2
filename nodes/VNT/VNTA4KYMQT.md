---
tag: VNTA4KYMQT
kind: definition
name: Densely defined operator
msc: [47A05, 47B25]
defines: BCJHNHKQFG
uses: [KRJX5RA0PW, 0BSJSX7ME2]
sources:
  - url: https://en.wikipedia.org/wiki/Densely_defined_operator
---

## Definition

Let $X$ and $Y$ be normed spaces, and let $T$ be an [[unbounded operator|KRJX5RA0PW]] from $X$ to $Y$ with domain $D(T)$.
The operator $T$ is *densely defined* if $D(T)$ is a [[dense subset|0BSJSX7ME2]] of $X$, that is, the closure of $D(T)$ in $X$ is $X$.

## Remarks

Example: on $X = C[0, 1]$ with the supremum norm, let $D(T)$ be the space of polynomials and $Tp = p'$.
By the Weierstrass approximation theorem, every continuous function on $[0, 1]$ is a uniform limit of polynomials, so $T$ is densely defined.

Non-example: on $X = L^2(0, 1)$, let $D(T)$ be the closed subspace of functions that vanish almost everywhere on $(0, \tfrac12)$, and $Tf = f$.
The closure of $D(T)$ is $D(T)$ itself, which is not $X$, so $T$ is not densely defined.

A bounded operator that is densely defined extends uniquely to a bounded operator on all of $X$ when $Y$ is a Banach space.
