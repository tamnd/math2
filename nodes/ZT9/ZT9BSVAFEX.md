---
tag: ZT9BSVAFEX
kind: definition
name: Pushforward measure
msc: [28A12, 28A20]
defines: 3N66TM3TSQ
uses: [PR11BZQQPG, YYNCJSR0PJ, N4KDT83V3S]
sources:
  - url: https://en.wikipedia.org/wiki/Pushforward_measure
---

## Definition

Let $(X, \Sigma)$ and $(Y, \mathcal{T})$ be [[measurable spaces|N4KDT83V3S]], let $\mu$ be a [[measure|PR11BZQQPG]] on $(X, \Sigma)$, and let $f \colon X \to Y$ be a [[measurable function|YYNCJSR0PJ]].
The *pushforward* of $\mu$ along $f$ is the map $f_* \mu \colon \mathcal{T} \to [0, \infty]$ given by
$$(f_* \mu)(B) = \mu\big(f^{-1}(B)\big) \quad \text{for } B \in \mathcal{T}.$$

## Remarks

The set $f^{-1}(B)$ lies in $\Sigma$ because $f$ is measurable, so the formula makes sense.
The map $f_* \mu$ is a measure: $f^{-1}(\varnothing) = \varnothing$, and the preimage of a disjoint union of sets $B_n$ is the disjoint union of the sets $f^{-1}(B_n)$.
Other notations are $\mu \circ f^{-1}$ and $f_\# \mu$.
Example: let $\mu$ be the measure on $\R$ with $\mu(A) = $ number of points of $A \cap \set{-1, 1}$, and $f(x) = x^2$.
Then $f_* \mu$ gives mass $2$ to the point $1$, since $f^{-1}(\set{1}) = \set{-1, 1}$.
Non-example: if $f$ is not measurable, some $f^{-1}(B)$ is outside $\Sigma$, and the formula does not define $f_* \mu$ on all of $\mathcal{T}$.
For a measurable $g \colon Y \to [0, \infty]$ the change of variables formula holds:
$$\int_Y g \, d(f_* \mu) = \int_X (g \circ f) \, d\mu.$$
