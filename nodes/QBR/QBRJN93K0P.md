---
tag: QBRJN93K0P
kind: definition
name: Annihilator method
msc: [34A30, 44A45]
defines: 794N251WY8
uses: [0QQRP17Z7S, BB15T3J891, 0XRB469Z32, 0Y6TH5PQVS]
sources:
  - url: https://en.wikipedia.org/wiki/Annihilator_method
---

## Definition

Let $D = d/dt$ be the [[differentiation operator|BB15T3J891]], and let $L = a_n D^n + \dots + a_1 D + a_0$ with $a_0, \dots, a_n \in \C$ and $a_n \ne 0$.
Let $f$ be a function on $\R$, and let $A(D) = b_m D^m + \dots + b_0$ be a nonzero polynomial in $D$ with constant coefficients.
If $A(D) f = 0$, then $A$ is an *annihilator* of $f$.
The *annihilator method* for $L y = f$ consists of these steps.

1. Find an annihilator $A$ of $f$.
2. Solve the homogeneous equation $A(D) L(D) y = 0$ by the roots of the polynomial $A(r) L(r)$. A root $r$ of multiplicity $k$ gives $e^{rt}, t e^{rt}, \dots, t^{k-1} e^{rt}$.
3. Remove from this solution the terms that already solve $L y = 0$, and keep the remaining terms with unknown coefficients as a trial function $y_p$.
4. Substitute $y_p$ into $L y = f$ and solve the resulting linear equations for the coefficients.

## Remarks

The functions with an annihilator are exactly the finite sums of terms $t^k e^{\alpha t}$, $t^k e^{\alpha t} \cos \beta t$ and $t^k e^{\alpha t} \sin \beta t$.
For instance, $t^k e^{\alpha t}$ is annihilated by $(D - \alpha)^{k+1}$, and $e^{\alpha t} \cos \beta t$ by $(D - \alpha)^2 + \beta^2$.
Step 4 always has a solution, which justifies the trial functions of the [[method of undetermined coefficients|0XRB469Z32]].

Example: $y'' - y = e^t$.
Here $L = D^2 - 1$ and $A = D - 1$, and $A L = (D - 1)^2 (D + 1)$ gives the solutions $e^t, t e^t, e^{-t}$.
Removing $e^t$ and $e^{-t}$, which solve $L y = 0$, leaves $y_p = c\, t e^t$.
Then $y_p'' - y_p = c (t + 2) e^t - c t e^t = 2c \, e^t$, so $c = 1/2$ and $y_p = \frac{1}{2} t e^t$.

Non-example: $f(t) = 1/t$ on $(0, \infty)$ is not a finite sum of the terms above, so it has no annihilator.
So the method does not apply to $y'' - y = 1/t$, and [[variation of parameters|0Y6TH5PQVS]] is used instead.
