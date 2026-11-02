---
tag: 2RH4DB8KWW
kind: definition
name: Point spectrum
msc: [47A10]
defines: 7FNVA0Q6YQ
uses: [BMKATJ802A, 0BQAA2BK3Q, 0S23E6YE83]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)
    locator: Point spectrum
---

## Definition

Let $X$ be a complex Banach space with identity map $I$, and let $T \colon X \to X$ be a bounded operator.
The *point spectrum* of $T$ is the set
$$\sigma_p(T) = \set{\lambda \in \C : \ker(T - \lambda I) \ne \set{0}},$$
the set of [[eigenvalues|0BQAA2BK3Q]] of $T$.

## Remarks

Here $\ker$ is the [[kernel|0S23E6YE83]].
The point spectrum is a subset of the [[spectrum|BMKATJ802A]] $\sigma(T)$, and for $X = \C^n$ the two are equal.

Example: let $L(x_1, x_2, \ldots) = (x_2, x_3, \ldots)$ be the left shift on $\ell^2$.
For $\abs{\lambda} < 1$, the vector $x = (1, \lambda, \lambda^2, \ldots)$ is in $\ell^2$ and $Lx = \lambda x$, so $\lambda \in \sigma_p(L)$.
Conversely $Lx = \lambda x$ forces $x_{n+1} = \lambda x_n$, so $x = x_1 (1, \lambda, \lambda^2, \ldots)$, which is in $\ell^2$ with $x \ne 0$ only if $\abs{\lambda} < 1$; thus $\sigma_p(L)$ is the open unit disc.

Non-example: for the diagonal operator $D(x_n) = (x_n / n)$ on $\ell^2$, $0 \in \sigma(D)$ but $0 \notin \sigma_p(D)$, since $Dx = 0$ forces $x = 0$.

The point spectrum need not be closed, and it can be empty, as for the right shift on $\ell^2$.
