---
tag: ZC6CHGS6Q2
kind: definition
name: Spacetime
msc: [83C05, 83A05, 53C50]
defines: 63ZKC7AFX2
uses: [F45VQ47GPV, BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Spacetime
---

## Definition

A *spacetime* is a pair $(M, g)$ such that:

1. $M$ is a connected four-dimensional [[smooth manifold|F45VQ47GPV]];
2. $g$ is a [[Lorentzian metric|BY4QYYS788]] on $M$, of signature $(-, +, +, +)$;
3. $(M, g)$ is time-oriented, that is, a continuous timelike vector field $T$ on $M$ is chosen.

A timelike or null tangent vector $v \neq 0$ is called future-directed if $g(v, T) < 0$.

## Remarks

Example: Minkowski space $\R^4$ with $g = -dt^2 + dx^2 + dy^2 + dz^2$, in units where $c = 1$, and $T = \partial_t$.
It is connected, $g$ has signature $(-, +, +, +)$ at each point, and $g(\partial_t, \partial_t) = -1 < 0$, so $\partial_t$ is timelike.
Non-example: $\R^4$ with the Euclidean metric $dt^2 + dx^2 + dy^2 + dz^2$ fails clause 2, since this metric has no timelike vectors.
Some authors drop connectedness or time orientation, or allow other dimensions; the definition above is the usual one in general relativity.
A Lorentzian manifold that admits no time orientation has a time-orientable double cover.
