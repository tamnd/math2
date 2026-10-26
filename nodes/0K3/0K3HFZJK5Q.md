---
tag: 0K3HFZJK5Q
kind: concept
name: Solving initial value problems with the Laplace transform
msc: [44A10, 34A30]
uses: [05XT5AVJBK, 0K090GVHVN, 0JRW4X1MDC, 075VBY4K4X, 0A6PGTTP2A]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
    locator: Transform of a function's derivative
---

## Summary

To solve an [[initial value problem|075VBY4K4X]] for a [[linear equation with constant coefficients|0A6PGTTP2A]], one applies the [[Laplace transform|05XT5AVJBK]] to both sides of the equation.
The [[rule for derivatives|0K090GVHVN]] turns the equation and the initial values into one algebraic equation for the transform $Y(s)$ of the unknown $y(t)$.
One solves this equation for $Y(s)$ and then finds $y = \mathcal{L}^{-1}\{Y\}$ with the [[inverse Laplace transform|0JRW4X1MDC]].

## Remarks

Example: for $y'' + y = 0$, $y(0) = 0$, $y'(0) = 1$, the transform gives $s^2 Y(s) - 1 + Y(s) = 0$. So $Y(s) = 1/(s^2 + 1)$ and $y(t) = \sin t$.
For $a_n y^{(n)} + \cdots + a_0 y = g(t)$ with zero initial values, $Y(s) = G(s) / P(s)$, where $P(s) = a_n s^n + \cdots + a_0$ and $G$ is the transform of $g$. The [[convolution theorem|0JNMJEDD93]] gives $y = h * g$ with $h = \mathcal{L}^{-1}\{1/P\}$.
The method handles discontinuous forcing, such as a [[step function|09C4JP7Y0M]], and impulses, such as a [[Dirac delta|0KPHENZ5S7]].

## Explanations

### L1 human

The Laplace transform turns a differential equation into an algebra problem.
We solve the algebra problem, which is often easy, and then transform back to get the solution.
The initial values are built in from the start, so there are no constants to find at the end.
