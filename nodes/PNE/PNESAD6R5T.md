---
tag: PNESAD6R5T
kind: example
name: Airy equation
msc: [34B30, 33C10, 34M03]
illustrates: [QK2J038VB4, 08RT9GDDPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Airy_function
---

## Example

The *Airy equation* is
$$y'' - z\, y = 0.$$
Its coefficients are polynomials, so every point of $\C$ is an [[ordinary point|QK2J038VB4]], and all solutions are entire functions.
A [[power series solution|08RT9GDDPQ]] $y = \sum_{k \ge 0} a_k z^k$ gives $2 a_2 = 0$ and
$$(k + 2)(k + 1)\, a_{k+2} = a_{k-1} \quad \text{for } k \ge 1.$$
With $a_0 = 1$ and $a_1 = 0$ one gets $y_1 = 1 + \frac{z^3}{6} + \frac{z^6}{180} + \cdots$.
With $a_0 = 0$ and $a_1 = 1$ one gets $y_2 = z + \frac{z^4}{12} + \frac{z^7}{504} + \cdots$.
They are linearly independent, since their Wronskian at $0$ is $y_1(0) y_2'(0) - y_1'(0) y_2(0) = 1$.

## Remarks

The standard solutions are the Airy functions $\operatorname{Ai}$ and $\operatorname{Bi}$, which are fixed linear combinations of $y_1$ and $y_2$.
For real $x \to +\infty$, $\operatorname{Ai}(x)$ decays like $\exp\left( -\frac{2}{3} x^{3/2} \right)$ up to a power of $x$, and $\operatorname{Bi}(x)$ grows like $\exp\left( \frac{2}{3} x^{3/2} \right)$.
For $x \to -\infty$, both oscillate with an amplitude that decays like $\abs{x}^{-1/4}$.
The point $\infty$ is an irregular singular point, and $\operatorname{Ai}$ is the classical example of the [[Stokes phenomenon|TTGF8KCA8C]].

## Explanations

### L1 human

The Airy equation is the simplest equation whose solutions switch from oscillating to growing or decaying.
For $x < 0$ it behaves like $y'' = -\abs{x} y$, a spring, so solutions wiggle.
For $x > 0$ it behaves like $y'' = x y$, so solutions grow or decay exponentially.
It describes light near a rainbow caustic and a quantum particle near a turning point.
