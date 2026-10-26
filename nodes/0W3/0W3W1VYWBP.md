---
tag: 0W3W1VYWBP
kind: statement
role: theorem
name: Line integral as an integral over the parameter interval
aliases: [parametric-formula-for-line-integrals]
msc: [26B12]
uses: [0M50E4WYWJ, 0YS8RX87F4, 0D98771SM0, 00R1JDDV5X]
sources:
  - url: https://en.wikipedia.org/wiki/Line_integral
    locator: Derivation
  - url: https://en.wikipedia.org/wiki/Line_integral
    locator: Line integral of a vector field
---

## Statement

Let $\gamma \colon [a, b] \to \mathbb{R}^n$ be a $C^1$ curve with image $C$.
Let $f \colon C \to \mathbb{R}$ be continuous, and let $F \colon C \to \mathbb{R}^n$ be a continuous vector field.
Then
$$\int_\gamma f \, ds = \int_a^b f(\gamma(t)) \, \|\gamma'(t)\| \, dt, \qquad \int_\gamma F \cdot d\mathbf{r} = \int_a^b F(\gamma(t)) \cdot \gamma'(t) \, dt.$$

## Remarks

The left sides are the [[line integral of a scalar field|0M50E4WYWJ]] and the [[line integral of a vector field|0YS8RX87F4]]. The right sides are ordinary integrals in one variable.
The formula follows from $\Delta s_i = \int_{t_{i-1}}^{t_i} \|\gamma'(t)\| \, dt$, the mean value theorem for each component of $\gamma$, and the uniform continuity of $f \circ \gamma$ and $\gamma'$.
The formulas extend to piecewise $C^1$ curves, by summing over the pieces.
Example: for $F(x, y) = (-y, x)$ and $\gamma(t) = (\cos t, \sin t)$, $t \in [0, 2\pi]$, the integrand is $\sin^2 t + \cos^2 t = 1$, so $\int_\gamma F \cdot d\mathbf{r} = 2\pi$.

## Explanations

### L1 human

To compute a line integral, write the curve with a parameter $t$.
Then $ds$ becomes $\|\gamma'(t)\| \, dt$ and $d\mathbf{r}$ becomes $\gamma'(t) \, dt$, and the line integral is an ordinary integral in $t$.
