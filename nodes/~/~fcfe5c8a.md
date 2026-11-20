---
tag: ~fcfe5c8a
kind: example
name: The substitution x to minus x as an isometry of polynomials
msc: ["15A04", "46C05"]
topics: [AZS5BPF5H3]
audience: ug1
instance_of: [07SJXTWVQW, 06BRDF3F0E]
uses: [0717XXPWM6, 0VGSYBWHV2, 079D68S3AW]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
    locator: Linear isometry
  - url: https://en.wikipedia.org/wiki/Reflection_(mathematics)
    locator: lead section
---

## Example

Let $\mathcal{P}_2$ be the real vector space of polynomials of degree at most $2$, with the [[inner product|0VGSYBWHV2]]
$$\ip{p}{q} = \int_{-1}^{1} p(x)\,q(x)\,dx.$$
Let $T \colon \mathcal{P}_2 \to \mathcal{P}_2$ be the map $(Tp)(x) = p(-x)$.
We check that $T$ is a [[linear isometry|0717XXPWM6]], and that it is the reflection in the hyperplane orthogonal to $x$.

1. Linearity: $\big(T(ap + bq)\big)(x) = ap(-x) + bq(-x) = \big(aTp + bTq\big)(x)$.
2. Norms: $\norm{Tp}^2 = \int_{-1}^{1} p(-x)^2\,dx$. The substitution $t = -x$, $dt = -dx$ swaps the limits, so this integral is $\int_{-1}^{1} p(t)^2\,dt = \norm{p}^2$.
3. A check with $p(x) = 1 + x$: $\norm{p}^2 = \int_{-1}^{1} (1 + 2x + x^2)\,dx = 2 + 0 + \frac{2}{3} = \frac{8}{3}$.
4. And $Tp = 1 - x$ has $\norm{Tp}^2 = \int_{-1}^{1} (1 - 2x + x^2)\,dx = 2 - 0 + \frac{2}{3} = \frac{8}{3}$, the same value.
5. $T$ fixes $1$ and $x^2$, and $T(x) = -x$.
6. $\ip{x}{1} = \int_{-1}^{1} x\,dx = 0$ and $\ip{x}{x^2} = \int_{-1}^{1} x^3\,dx = 0$. So $1$ and $x^2$ lie in the [[orthogonal complement|079D68S3AW]] $x^\perp$.
7. $\dim \mathcal{P}_2 = 3$ and $x \neq 0$, so $x^\perp$ has dimension $2$. The independent vectors $1$ and $x^2$ span it.
8. So $T$ fixes the hyperplane $x^\perp$ pointwise and sends $x$ to $-x$. This is the [[reflection|06BRDF3F0E]] in $x^\perp$.

## Remarks

- The example shows that linear isometries occur in spaces of functions, not only in $\R^n$.
- In the basis $1, x, x^2$, the matrix of $T$ is $\operatorname{diag}(1, -1, 1)$, and $\det T = -1$.
- The basis $1, x, x^2$ is not orthonormal, because $\ip{1}{x^2} = \frac{2}{3}$. The isometry property does not depend on this basis.
- With the inner product $\int_{0}^{1} p(x)q(x)\,dx$, the map $T$ is not an isometry: $\norm{1 + x}^2 = \frac{7}{3}$ but $\norm{1 - x}^2 = \frac{1}{3}$.

## Explanations

### L1 human

The map turns the graph of a polynomial over, as in a mirror on the vertical axis.
The inner product measures a polynomial by the area under its square from $-1$ to $1$.
A mirror image of the graph has the same area under its square, because the interval from $-1$ to $1$ is symmetric.
So the map keeps the size of every polynomial.

### L2 human

Worked check of the last remark:

1. On $[0, 1]$: $\int_0^1 (1 + x)^2\,dx = \left[\frac{(1 + x)^3}{3}\right]_0^1 = \frac{8 - 1}{3} = \frac{7}{3}$.
2. $\int_0^1 (1 - x)^2\,dx = \left[-\frac{(1 - x)^3}{3}\right]_0^1 = 0 + \frac{1}{3} = \frac{1}{3}$.
3. The two values differ, so $p(x) \mapsto p(-x)$ is not an isometry for this inner product.

The typical use: symmetries of the interval give isometries of function spaces.
A trap: whether a map is an isometry depends on the inner product, not only on the map.
