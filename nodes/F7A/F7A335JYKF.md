---
tag: F7A335JYKF
kind: definition
name: Whittaker transform
msc: [44A20, 33C15]
defines: VZ3BHDB5QZ
uses: [YCK709QB06, 7EFDMJSVDP]
sources:
  - url: https://en.wikipedia.org/wiki/Whittaker_function
---

## Definition

Fix complex parameters $\kappa$ and $\mu$, and let $W_{\kappa, \mu}$ be the [[Whittaker function|7EFDMJSVDP]] on $(0, \infty)$.
Let $k(z) = e^{-z/2} z^{-\kappa} W_{\kappa, \mu}(z)$ for $z > 0$.
Let $f \colon (0, \infty) \to \C$ be such that the integral below converges for $y$ in a set $Y \subseteq (0, \infty)$.
The *Whittaker transform* of $f$, in this normalization, is the function
$$g(y) = \int_0^\infty k(xy)\, f(x)\, dx, \qquad y \in Y.$$

## Remarks

Other authors put other powers of $xy$ and other exponential factors in front of $W_{\kappa, \mu}(xy)$; the name covers this whole family of kernels.

Example: for $\kappa = \mu + 1/2$ one has $W_{\mu + 1/2, \mu}(z) = e^{-z/2} z^{\mu + 1/2}$.
Then $k(z) = e^{-z/2} z^{-\mu - 1/2} e^{-z/2} z^{\mu + 1/2} = e^{-z}$, and the transform is the [[Laplace transform|0V49JEZW06]] $g(y) = \int_0^\infty e^{-xy} f(x)\, dx$.

Non-example: $W_{\kappa, \mu}(z)$ behaves like $e^{-z/2} z^{\kappa}$ as $z \to \infty$, so $k(xy)$ behaves like $e^{-xy}$ for large $x$.
Hence $f(x) = e^{x^2}$ gives a divergent integral for every $y > 0$ and has no Whittaker transform.
