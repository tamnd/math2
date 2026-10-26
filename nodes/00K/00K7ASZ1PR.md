---
tag: 00K7ASZ1PR
kind: counterexample
name: Non-uniqueness for a non-Lipschitz equation
msc: [34A12]
uses: [0P6KRD5B7A, 055VVSN00V, 075VBY4K4X, 098YP831QY]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Example of non-uniqueness
---

## Counterexample

For a real number $x$, let $x^{1/3}$ be its real cube root and let $x^{2/3} = \left(x^{1/3}\right)^2$.
Consider the [[initial value problem|075VBY4K4X]] $x'(t) = 3\, x(t)^{2/3}$, $x(0) = 0$, on $\mathbb{R}$.
The constant function $x(t) = 0$ is a solution.
The function $x(t) = t^3$ is also a solution, because its derivative is $3t^2 = 3 \left(t^3\right)^{2/3}$.
More generally, for each $c \ge 0$, the function equal to $0$ for $t < c$ and to $(t - c)^3$ for $t \ge c$ is a solution.
So the problem has infinitely many solutions on every interval that contains $0$ in its interior.

## Remarks

The right side $f(x) = 3 x^{2/3}$ is continuous, so the [[Peano existence theorem|098YP831QY]] applies.
The function $f$ is not Lipschitz on any neighbourhood of $0$: the quotient $f(x)/x = 3 x^{-1/3}$ is unbounded as $x \to 0$. So the [[Picard–Lindelöf theorem|0P6KRD5B7A]] does not apply.
For an initial value $x(0) = x_0 \neq 0$, the field is $C^1$ near $x_0$, and the solution is unique near $t = 0$.

## Explanations

### L1 human

A solution can rest at $0$ for any length of time and then leave.
The field is so steep near $0$ that the equation cannot tell when the departure must happen.
This shows that continuity alone does not give uniqueness.
