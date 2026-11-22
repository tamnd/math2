---
tag: W4MHG5MZ1S
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
We check that $T$ is a [[linear isometry|0717XXPWM6]], and that it is the reflection in the hyperplane orthogonal to the polynomial $x$.

1. The map is linear, because $\big(T(ap + bq)\big)(x) = ap(-x) + bq(-x) = \big(aTp + bTq\big)(x)$.
2. It keeps norms. We have $\norm{Tp}^2 = \int_{-1}^{1} p(-x)^2\,dx$, and the substitution $t = -x$ turns this into $\int_{-1}^{1} p(t)^2\,dt = \norm{p}^2$.
3. As a check, take $p(x) = 1 + x$. Then $\norm{p}^2 = \int_{-1}^{1} (1 + 2x + x^2)\,dx = 2 + 0 + \tfrac{2}{3} = \tfrac{8}{3}$, and $Tp = 1 - x$ gives $\int_{-1}^{1} (1 - 2x + x^2)\,dx = \tfrac{8}{3}$ as well.
4. The map fixes $1$ and $x^2$, and it sends $x$ to $-x$.
5. The polynomials $1$ and $x^2$ are orthogonal to $x$, because $\int_{-1}^{1} x\,dx = 0$ and $\int_{-1}^{1} x^3\,dx = 0$. So they lie in the [[orthogonal complement|079D68S3AW]] $x^\perp$.
6. Since $\dim \mathcal{P}_2 = 3$ and $x \ne 0$, the complement $x^\perp$ has dimension $2$, and the independent polynomials $1$ and $x^2$ span it.
7. So $T$ fixes the hyperplane $x^\perp$ pointwise and sends $x$ to $-x$, which makes it the [[reflection|06BRDF3F0E]] in $x^\perp$.

## Remarks

The example shows that linear isometries live in spaces of functions as well as in $\R^n$.
In the basis $1, x, x^2$ the matrix of $T$ is $\operatorname{diag}(1, -1, 1)$, so $\det T = -1$, as for every reflection.
That basis is not orthonormal, since $\ip{1}{x^2} = \tfrac{2}{3}$, but the isometry property does not depend on the basis that we use to write the matrix.

The inner product matters, though.
With $\ip{p}{q} = \int_{0}^{1} p(x)q(x)\,dx$ the same map is no isometry: $\norm{1 + x}^2 = \tfrac{7}{3}$ but $\norm{1 - x}^2 = \tfrac{1}{3}$.
The interval $[0, 1]$ is not symmetric about $0$, so the substitution $t = -x$ moves it to $[-1, 0]$.

## Explanations

### L1 human

The map flips the graph of a polynomial over the vertical axis, as a mirror would.
The inner product measures a polynomial by the area under the graph of its square from $-1$ to $1$.
The flipped graph has the same area under its square, because the interval from $-1$ to $1$ is the same on both sides of $0$.
So the map keeps the size of every polynomial.

### L2 human

Here is the check of the second remark, on the interval $[0, 1]$.
Integrate both squares:
$$\int_0^1 (1 + x)^2\,dx = \left[\frac{(1 + x)^3}{3}\right]_0^1 = \frac{8 - 1}{3} = \frac{7}{3}, \qquad \int_0^1 (1 - x)^2\,dx = \left[-\frac{(1 - x)^3}{3}\right]_0^1 = \frac{1}{3}.$$
The two values differ, so $p(x) \mapsto p(-x)$ is not an isometry for this inner product.
Symmetries of the interval of integration give isometries of function spaces, and that is the typical source of such examples.
Watch out: whether a map is an isometry depends on the inner product, not only on the map.
