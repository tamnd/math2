---
tag: 0MHE4B1QCQ
kind: statement
role: theorem
name: Wronskian test for linear independence of solutions
msc: [34A30]
uses: [0N5NF1RGBP, 0EQZSAB9EC, 0GK68PZ6KH]
sources:
  - url: https://en.wikipedia.org/wiki/Wronskian
    locator: Application to linear differential equations
---

## Statement

Let $I$ be an open interval, let $a_0, \dots, a_{n-1} : I \to \mathbb{R}$ be continuous, and let $y_1, \dots, y_n$ be solutions on $I$ of the [[homogeneous linear equation|0EQZSAB9EC]] $y^{(n)} + a_{n-1}(x) y^{(n-1)} + \dots + a_0(x) y = 0$.
Let $W = W(y_1, \dots, y_n)$ be their [[Wronskian|0N5NF1RGBP]].
Then these three conditions are equivalent.
(a) The functions $y_1, \dots, y_n$ are linearly independent on $I$.
(b) There is a point $x_0 \in I$ with $W(x_0) \ne 0$.
(c) For each $x \in I$, $W(x) \ne 0$.

## Remarks

So the Wronskian of $n$ solutions is either zero at each point of $I$ or zero at no point of $I$. [[Abel's identity|0VGWKX2JHB]] gives the same result for $n = 2$.
For arbitrary functions, $W(x_0) \ne 0$ at one point still implies linear independence. But the converse fails: $x^2$ and $x |x|$ are linearly independent on $\mathbb{R}$, and their Wronskian is $0$ at each point.
Example: $e^{x}$ and $e^{-x}$ solve $y'' - y = 0$, and their Wronskian is $-2$, so they are independent.

## Explanations

### L1 human

To check that $n$ solutions are independent, compute one determinant at one point.
If it is not zero, the solutions are independent and form a basis of all solutions.
For solutions of a linear equation, the value at one point already decides the question.
