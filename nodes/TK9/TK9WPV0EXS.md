---
tag: TK9WPV0EXS
kind: definition
name: Analytic continuation in several variables
msc: [32D05, 32A10]
defines: MZT3Y1X53W
uses: [507C34W0ZT, 02BH3MCBQB, 0SPE8WNWFV, 0JG9W3KA6B]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_continuation
---

## Definition

A *function element* in $\C^n$ is a pair $(U, f)$ where $U \subseteq \C^n$ is a nonempty connected [[open set|02BH3MCBQB]] and $f$ is a [[holomorphic function|507C34W0ZT]] on $U$.

1. A function element $(V, g)$ is a *direct analytic continuation* of $(U, f)$ if $U \cap V$ is nonempty and $f = g$ on some [[connected component|0JG9W3KA6B]] of $U \cap V$.
2. A function element $(V, g)$ is an *analytic continuation* of $(U, f)$ along a chain if a finite sequence of function elements runs from $(U_0, f_0) = (U, f)$ to $(U_k, f_k) = (V, g)$. Each $(U_j, f_j)$ must be a direct analytic continuation of $(U_{j-1}, f_{j-1})$.

If $V \supseteq U$ and $g = f$ on $U$, one says that $g$ is an analytic continuation of $f$ to $V$.

## Remarks

By the identity theorem, if $f$ and $g$ agree on a nonempty open subset of a component of $U \cap V$, they agree on that whole component.

Example: let $U = \set{z \in \C^2 : \operatorname{Re} z_1 > 0}$ and $f(z) = \log z_1$ with the principal branch.
Moving through half-spaces in the $z_1$-direction around the plane $z_1 = 0$ gives a chain of direct continuations that returns to $U$ with the function $\log z_1 + 2\pi i$.
So continuation along a closed chain need not give back the original function element.

Non-example: if $U \cap V$ is empty, then $(V, g)$ is never a direct analytic continuation of $(U, f)$, whatever $g$ is.

For $n = 1$ this is the usual [[analytic continuation|0M3YQJ81NB]] of a holomorphic function along a chain of discs or domains.
