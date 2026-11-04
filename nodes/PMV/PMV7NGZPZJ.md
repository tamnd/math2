---
tag: PMV7NGZPZJ
kind: proof
name: Proof of cosh^2 - sinh^2 = 1
msc: [33B10]
proves: 06QCTRFBM0
uses: [0GWD21EWRW, 0EQFWKJ37J, 0RMVS7RXZX, 0E8HNVBCSP]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Useful relations
---

## Proof

We expand both squares with the definitions.

1. Let $x$ be a real number, and write $u = e^x$ and $v = e^{-x}$. Here $e^t = \exp(t)$ is the [[exponential function|0RMVS7RXZX]].
2. By the [[exponential of a sum|0E8HNVBCSP]], $u v = e^{x + (-x)} = e^0$.
3. In the series defining $\exp$, all terms with $n \ge 1$ vanish at $0$. So $e^0 = 1$, and $u v = 1$ by step 2.
4. By the definitions of the [[hyperbolic cosine|0EQFWKJ37J]] and the [[hyperbolic sine|0GWD21EWRW]], $\cosh x = \frac{u + v}{2}$ and $\sinh x = \frac{u - v}{2}$.
5. Expanding the squares gives $(u + v)^2 = u^2 + 2uv + v^2$ and $(u - v)^2 = u^2 - 2uv + v^2$.
6. By steps 4 and 5,
$$\cosh^2 x - \sinh^2 x = \frac{(u + v)^2 - (u - v)^2}{4} = \frac{4 u v}{4} = u v.$$
7. By steps 3 and 6, $\cosh^2 x - \sinh^2 x = 1$.

## Idea

Both functions are built from $e^x$ and $e^{-x}$. In the difference of the squares, the $e^{2x}$ and $e^{-2x}$ terms cancel. Only the cross term $e^x e^{-x} = 1$ survives.
