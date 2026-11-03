---
kind: statement
msc:
- 34A30
name: Superposition for n solutions of a homogeneous linear ODE
role: theorem
sources:
- locator: ch-higher-order-ode.tex:967
  url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-higher-order-ode.tex#L967
tag: DDKKS61REG
uses:
- 0EQZSAB9EC
---

## Statement

Take a [[homogeneous linear equation|0EQZSAB9EC]] of order $n$. Suppose that $y_1, y_2, \dots, y_n$ are solutions of it. Pick any constants $C_1, C_2, \dots, C_n$. Then the function $C_1 y_1 + C_2 y_2 + \dots + C_n y_n$ is also a solution of the same equation.

## Remarks

The proof uses the linearity of the differential operator $L$ of the equation. It gives $L(\sum_j C_j y_j) = \sum_j C_j L y_j = 0$.

Linearity and homogeneity are both needed. For $y' = y^2$, the function $-1/x$ solves the equation on $x > 0$, but $-2/x$ does not.
