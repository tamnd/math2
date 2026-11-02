---
tag: WAE4ZGJXJ7
kind: statement
role: theorem
name: Cameron–Martin theorem
msc: [28C20, 60G15, 60J65]
uses: [5Z00K7K1HY, 22735FGJV6, P0DV2TCH1N, 3N66TM3TSQ, P0P21KDV6E, EBGECZNCV5, 1NTKG64F7N]
about: [5Z00K7K1HY, P0DV2TCH1N]
sources:
  - url: https://en.wikipedia.org/wiki/Cameron%E2%80%93Martin_theorem
same_as:
  wikidata: Q5026435
  wikipedia: Cameron–Martin theorem
---

## Statement

Let $T > 0$ and let $C_0 = C_0([0, T])$ be the [[classical Wiener space|5Z00K7K1HY]] of continuous functions $\omega \colon [0, T] \to \R$ with $\omega(0) = 0$.
Let $W$ be Wiener measure on $C_0$, the law of a [[Wiener process|22735FGJV6]] on $[0, T]$.
Let $H$ be the Cameron–Martin space: the set of absolutely continuous $h \in C_0$ with $h' \in L^2([0, T])$.
For $h \in C_0$, let $W_h$ be the [[pushforward|3N66TM3TSQ]] of $W$ under the translation $\omega \mapsto \omega + h$.

1. If $h \in H$, then $W_h$ and $W$ are [[mutually absolutely continuous|P0P21KDV6E]], and for $W$-almost every $\omega$
$$\frac{dW_h}{dW}(\omega) = \exp\left( \int_0^T h'(t) \, d\omega(t) - \frac12 \int_0^T h'(t)^2 \, dt \right).$$
2. If $h \notin H$, then $W_h$ and $W$ are [[mutually singular|EBGECZNCV5]].

## Remarks

Here $dW_h / dW$ is the [[Radon–Nikodym derivative|1NTKG64F7N]], and $\int_0^T h'(t) \, d\omega(t)$ is the Wiener integral of the deterministic function $h'$, defined as an $L^2(W)$ limit.
In one dimension the formula is a direct computation: the density of $N(a, 1)$ with respect to $N(0, 1)$ is $e^{a x - a^2/2}$.
The general case reduces to finite-dimensional projections of the path, since the Wiener integral is a normal variable with variance $\int_0^T h'(t)^2 \, dt$.

Example: for $h(t) = c t$, one has $h' = c$, and the density is $\exp(c\, \omega(T) - c^2 T / 2)$.
So Brownian motion with drift $c$ has a law equivalent to that of Brownian motion on $[0, T]$.

The analogous result holds for every centered [[Gaussian measure|P0DV2TCH1N]] on a separable Banach space, with $H$ its Cameron–Martin space.
In infinite dimensions $H$ has measure zero, so most translations give singular measures.

## Explanations

### L1 human

Shifting a Brownian path by a fixed function changes its law.
If the shift is smooth enough, with square-integrable derivative, the new law has a density with respect to the old one, given by an explicit formula.
If the shift is rougher, the two laws live on disjoint sets of paths.

### L2 human

The theorem is the starting point of Girsanov's theorem, where the deterministic shift is replaced by an adapted random drift.
It shows that Wiener measure is quasi-invariant only along the directions of $H$, which is a dense subspace of measure zero.
Integration by parts on Wiener space, the base of Malliavin calculus, comes from differentiating the density in $h$.
