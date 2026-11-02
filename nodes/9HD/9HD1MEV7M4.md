---
tag: 9HD1MEV7M4
kind: definition
name: Meijer G-function transforms
msc: [44A20, 33C60]
defines: C0BCHX106R
uses: [YCK709QB06, 19JNNN5KV7]
sources:
  - url: https://en.wikipedia.org/wiki/Meijer_G-function
---

## Definition

Fix integers $0 \le m \le q$ and $0 \le n \le p$, and complex parameters $a_1, \dots, a_p$ and $b_1, \dots, b_q$.
Let $G(z) = G^{m,n}_{p,q}(z \mid a_1, \dots, a_p; b_1, \dots, b_q)$ be the [[Meijer G-function|19JNNN5KV7]] with these parameters.
Let $f \colon (0, \infty) \to \C$ be such that the integral below converges for $y$ in a set $Y \subseteq (0, \infty)$.
The *G-transform* of $f$ with these parameters is the function
$$g(y) = \int_0^\infty G(xy)\, f(x)\, dx, \qquad y \in Y.$$

## Remarks

Example: $G^{1,0}_{0,1}(z \mid -; 0) = e^{-z}$, so with $m = q = 1$, $n = p = 0$ and $b_1 = 0$ the G-transform is the [[Laplace transform|0V49JEZW06]] $g(y) = \int_0^\infty e^{-xy} f(x)\, dx$.
Example: $G^{1,1}_{1,1}(z \mid 0; 0) = (1 + z)^{-1}$, so another choice gives the transform $\int_0^\infty f(x) (1 + xy)^{-1}\, dx$, which is a form of the [[Stieltjes transform|RG1HFAYD98]].
Example: $G^{1,0}_{0,2}(z \mid -; \nu/2, -\nu/2) = J_\nu(2\sqrt{z})$, a Bessel function kernel.

Non-example: for the Laplace case, $f(x) = e^{x^2}$ gives a divergent integral for every $y > 0$, so it has no G-transform with these parameters.

The [[Mellin transform|N5PVGRJE1T]] turns the G-transform into a product: if $\mathcal{M}$ denotes the Mellin transform, then formally $\mathcal{M} g(s) = \mathcal{M} G(s)\, \mathcal{M} f(1 - s)$, and
$$\mathcal{M} G(s) = \frac{\prod_{j=1}^{m} \Gamma(b_j + s) \prod_{j=1}^{n} \Gamma(1 - a_j - s)}{\prod_{j=m+1}^{q} \Gamma(1 - b_j - s) \prod_{j=n+1}^{p} \Gamma(a_j + s)}.$$
