---
tag: XS3VFNSY9N
kind: definition
name: Separable degree
msc: [12F10, 12F15]
defines: H5YX5B7GVM
uses: [09EYMKMSB9, 02SJG1HC32, EZVN87C88J, 0GS74FGFEK]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_extension
---

## Definition

Let $L/K$ be an [[algebraic extension|09EYMKMSB9]].
Let $\Omega$ be an [[algebraically closed field|02SJG1HC32]] and let $\sigma \colon K \to \Omega$ be a [[field homomorphism|EZVN87C88J]].
The *separable degree* $[L:K]_s$ of $L/K$ is the cardinality of the set of field homomorphisms $\tau \colon L \to \Omega$ with $\tau|_K = \sigma$.
This cardinality does not depend on the choice of $\Omega$ and $\sigma$.

## Remarks

Let $L/K$ be finite.
Then $[L:K]_s$ divides the [[degree|0GS74FGFEK]] $[L:K]$.
If $K$ has characteristic $p > 0$, the quotient $[L:K]_i = [L:K] / [L:K]_s$ is a power of $p$, called the inseparable degree; in characteristic $0$ it is $1$.
The extension $L/K$ is separable if and only if $[L:K]_s = [L:K]$.
Separable degree is multiplicative in towers: $[M:K]_s = [M:L]_s [L:K]_s$.
It equals the degree over $K$ of the [[separable closure|JJ91A1V8NQ]] of $K$ in $L$.

Example: $L = \Q(\sqrt{2})$ over $\Q$ with $\Omega = \C$.
Check: an embedding is determined by the image of $\sqrt{2}$, which must be a root of $x^2 - 2$, so there are exactly $2$ embeddings and $[L:\Q]_s = 2 = [L:\Q]$.

Non-example of the equality $[L:K]_s = [L:K]$: let $K = \F_p(t)$ and $L = K(s)$ with $s^p = t$.
Over an algebraic closure, $x^p - t = (x - s)^p$ has one root, so $[L:K]_s = 1$ while $[L:K] = p$.
