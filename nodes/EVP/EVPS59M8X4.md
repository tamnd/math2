---
tag: EVPS59M8X4
kind: definition
name: Separably closed field
msc: [12F10]
defines: 8B57B7EGK4
uses: [0QA8CHH8MG, 03J8BS7FMV, 0N019F6RE9, 02SJG1HC32]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_closure
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]].
The field $K$ is *separably closed* if every [[separable polynomial|03J8BS7FMV]] $f \in K[x]$ of degree at least $1$ has a root in $K$.

## Remarks

The following are equivalent for a field $K$:

1. $K$ is separably closed;
2. every separable polynomial in $K[x]$ splits into linear factors over $K$;
3. $K$ has no [[separable extension|0N019F6RE9]] of degree greater than $1$.

Every [[algebraically closed field|02SJG1HC32]] is separably closed.
A field is algebraically closed if and only if it is separably closed and perfect.

Example: the separable closure $K^{\mathrm{sep}}$ of $K = \F_p(t)$ is separably closed but not algebraically closed.
Check: the roots of a separable polynomial over $K^{\mathrm{sep}}$ are separable over $K^{\mathrm{sep}}$, hence over $K$, so they lie in $K^{\mathrm{sep}}$.
But the root $t^{1/p}$ of $x^p - t$ is not separable over $K$.

Non-example: a finite field $\F_q$ is not separably closed.
The polynomial $x^q - x - 1$ is separable, since its derivative is $-1$, and it has no root in $\F_q$, since $a^q - a - 1 = -1$ for every $a \in \F_q$.
