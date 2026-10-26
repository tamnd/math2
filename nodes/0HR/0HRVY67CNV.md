---
tag: 0HRVY67CNV
kind: statement
role: theorem
name: Solutions for repeated roots
msc: [34A30]
uses: [0QDXMG46QW, 0H4KNNCHPY, 0A6PGTTP2A, 0HJ0HDA6W7]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_equation_(calculus)
    locator: Repeated real roots
---

## Statement

Let $a_0, \dots, a_{n-1}$ be real numbers, and let $p(r) = r^n + a_{n-1} r^{n-1} + \dots + a_0$ be the [[characteristic polynomial|0QDXMG46QW]] of the equation $y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_0 y = 0$.
Let $r$ be a real root of $p$ of multiplicity $m \ge 1$.
Then the $m$ functions $e^{r x}, x e^{r x}, \dots, x^{m-1} e^{r x}$ are linearly independent solutions of the equation on $\mathbb{R}$.
If all the roots of $p$ are real, the union of these families over the distinct roots of $p$ is a [[fundamental system|0H4KNNCHPY]].

## Remarks

For order $2$: if $r$ is a double root of $r^2 + a_1 r + a_0$, the solutions are $(c_1 + c_2 x) e^{r x}$.
Example: $y'' - 2 y' + y = 0$ has $p(r) = (r - 1)^2$, so its solutions are $(c_1 + c_2 x) e^{x}$.
The same result holds for complex roots, with complex solutions. For the real form, see [[complex conjugate roots|0BEZX8F2XW]].

## Explanations

### L1 human

A double root gives only one exponential, but we need two solutions.
The extra solution is the exponential times $x$.
A root of multiplicity $m$ gives the exponential times $1, x, \dots, x^{m-1}$.
