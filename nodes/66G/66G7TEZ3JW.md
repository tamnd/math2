---
tag: 66G7TEZ3JW
kind: definition
name: Energy functional on paths
msc: ["58E10", 53C22]
defines: Q12AB1MJ64
uses: [7CBT4SM83Y, 0TH78S7GBZ]
sources:
  - url: https://en.wikipedia.org/wiki/Geodesic
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] and let $a < b$.
For a continuous, piecewise smooth path $\omega \colon [a, b] \to M$, the *energy* of $\omega$ is
$$E(\omega) = \frac{1}{2} \int_a^b g\big(\dot\omega(t), \dot\omega(t)\big) \, dt.$$
For $p, q \in M$, the *energy functional on paths* from $p$ to $q$ is the function $E$ on the set of such paths with $\omega(a) = p$ and $\omega(b) = q$.

## Remarks

Some authors omit the factor $\frac{1}{2}$.
With the [[length|0TH78S7GBZ]] $L(\omega) = \int_a^b \abs{\dot\omega} \, dt$, the Cauchy–Schwarz inequality gives $L(\omega)^2 \le 2 (b - a) E(\omega)$, with equality if and only if $\omega$ has constant speed.
The critical points of $E$ among paths with fixed ends are the geodesics from $p$ to $q$ parametrized on $[a, b]$.
A minimizer of $E$ is a length-minimizing geodesic with constant speed.
To apply Morse theory one extends $E$ to paths of Sobolev class $H^1$, which form a Hilbert manifold.

Example: in $\R^n$ with the Euclidean metric, the path $\omega(t) = p + t(q - p)$ on $[0, 1]$ has $E(\omega) = \frac{1}{2} \abs{q - p}^2$, and $L(\omega)^2 = 2 E(\omega)$, so it has constant speed.

Non-example: the reparametrization $\sigma(t) = p + t^2 (q - p)$ of the same segment has $E(\sigma) = \frac{2}{3} \abs{q - p}^2 > \frac{1}{2} \abs{q - p}^2$.
It has the same length but is not a critical point of $E$, since its speed is not constant.
