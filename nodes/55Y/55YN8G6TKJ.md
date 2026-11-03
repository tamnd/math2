---
tag: 55YN8G6TKJ
kind: definition
name: Koiter's imperfection sensitivity theory
msc: [74G60, 74G10, 74K25]
defines: MA18D6QTV3
uses: [4GAM4KXSM8, 50W7AQMS5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Buckling
---

## Definition

Consider a conservative elastic structure with load parameter $\lambda$ that [[buckles|4GAM4KXSM8]] at $\lambda_c > 0$ with a single buckling mode $u_1$.
Let $\xi$ be the amplitude of the mode.
The initial post-buckling path of the perfect structure has the expansion
$$\frac{\lambda}{\lambda_c} = 1 + a \xi + b \xi^2 + \cdots.$$
The post-buckling coefficients $a$ and $b$ are computed from the third and fourth variations of the potential energy.
Let the structure carry an initial imperfection of amplitude $\varepsilon$ in the shape of $u_1$, and let $\lambda_s(\varepsilon)$ be its maximum load, when it exists.
*Koiter's imperfection sensitivity theory* is the asymptotic analysis of this situation for small $\abs{\varepsilon}$.
Its main conclusions are:

1. If $a \ne 0$ (asymmetric bifurcation), then for imperfections of one sign $1 - \lambda_s / \lambda_c$ is of order $\abs{\varepsilon}^{1/2}$.
2. If $a = 0$ and $b < 0$ (unstable symmetric bifurcation), then $1 - \lambda_s / \lambda_c$ is of order $\abs{\varepsilon}^{2/3}$.
3. If $a = 0$ and $b > 0$ (stable symmetric bifurcation), then the imperfect structure has no maximum load near $\lambda_c$ and the structure is imperfection-insensitive.

## Remarks

Example: the axially compressed thin cylindrical shell has a strongly unstable post-buckling behaviour.
The theory classes it as highly imperfection-sensitive, which matches tests where such shells fail well below $\lambda_c$.

Non-example: a flat plate compressed in its plane has $a = 0$ and $b > 0$.
Case 3 applies, so the plate is not imperfection-sensitive in this sense, and it can carry loads above $\lambda_c$ after buckling.

The structures of cases 1 and 2 are called imperfection-sensitive.
The fractional exponents $1/2$ and $2/3$ explain why a very small imperfection already produces a large loss of strength.
