---
tag: J9ZY817SRC
kind: example
name: Abel equation of the first kind
msc: [34A34, 34A05]
instance_of: [0NT64JV96A]
uses: [0P97V20RW7, 0E1ZZBHZ3Z, 0V4E623THY]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_equation_of_the_first_kind
same_as:
  wikidata: Q3730861
  wikipedia: Abel equation of the first kind
---

## Example

Let $f_0, f_1, f_2, f_3$ be continuous functions on an open interval $I$, with $f_3$ not identically zero.
The *Abel equation of the first kind* is the first-order [[ordinary differential equation|0P97V20RW7]]
$$y' = f_3(x)\, y^3 + f_2(x)\, y^2 + f_1(x)\, y + f_0(x).$$
Its right side is a cubic polynomial in $y$.
When $f_3 = 0$ it would be a [[Riccati equation|0E1ZZBHZ3Z]], so the Abel equation is the next case after the Riccati equation.

Instance: $y' = y^3$, with $f_3 = 1$ and $f_0 = f_1 = f_2 = 0$.
It is [[separable|0V4E623THY]], and its nonzero solutions are $y = \pm (C - 2x)^{-1/2}$ for $x < C/2$.
Check: for $y = (C - 2x)^{-1/2}$, $y' = -\tfrac12 (C - 2x)^{-3/2} \cdot (-2) = (C - 2x)^{-3/2} = y^3$.
The solution tends to infinity as $x \to C/2$, so it exists only on the interval $(-\infty, C/2)$, which is bounded on the right.

## Explanations

### L1 human

The Abel equation of the first kind says that the slope of $y$ is a cubic polynomial in $y$ whose coefficients depend on $x$.
Unlike linear equations and many Riccati equations, it usually has no solution in closed form.
The example $y' = y^3$ shows a typical nonlinear effect: solutions can blow up in finite time.
