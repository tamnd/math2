---
tag: J0NR3YRW07
kind: definition
name: Numerical analysis
msc: [65-01, 65G50]
defines: B6E54YTR64
uses: [0G9EKM0E15, 05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_analysis
---

## Definition

*Numerical analysis* is the branch of mathematics that studies algorithms for computing approximate values of quantities defined by problems of continuous mathematics.
Its objects are the following.

1. A *problem*: a map $f$ from data $x$ to an exact answer $y = f(x)$, such as a root or an integral.
2. A *numerical method*: a finite procedure, or a [[sequence|0G9EKM0E15]] of them, that computes an approximation $\tilde y$ of $y$ from $x$ by arithmetic operations.
3. An *error analysis*: a bound on the error $\tilde y - y$, or a proof that the approximations have [[limit|05M5SWSZZD]] $y$, together with the cost of the method.

## Remarks

Example: the problem is to compute $\sqrt{2}$, and the method is the iteration $x_{k+1} = (x_k + 2/x_k)/2$ from $x_0 = 1$.
The error analysis shows that $x_k \to \sqrt{2}$ and that the error is roughly squared at each step.
Non-example: the symbolic simplification $\int_0^1 2x \, dx = 1$ by an antiderivative is exact computation, not an approximation, so it is not a numerical method in this sense.
The error of a method has two parts: the error of the method in exact arithmetic, and the error caused by rounding in a computer.
