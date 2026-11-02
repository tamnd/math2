---
tag: QTVP4WP1XX
kind: statement
role: proposition
name: Iterative refinement
msc: [65F05, 65G50]
uses: [0GT4WWGWH2, 0EB9N0S33C, 06EKW1AKXF, AB3S6MHJ8X, 0RKG5YW66Y]
about: [0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Iterative_refinement
same_as:
  wikidata: Q6094420
  wikipedia: Iterative refinement
---

## Statement

Let $A$ be an [[invertible|0EB9N0S33C]] $n \times n$ real or complex matrix, and let $b$ be a vector.
Let $x = A^{-1} b$ be the solution of the [[linear system|0GT4WWGWH2]] $Ax = b$.
Fix a vector norm and its [[operator norm|06EKW1AKXF]], and a number $\eta$ with $0 \le \eta < 1/2$.
*Iterative refinement* starts from an approximation $x_0$ and repeats, for $m = 0, 1, 2, \dots$:

1. compute the residual $r_m = b - A x_m$;
2. compute a correction $d_m$ with $(A + E_m) d_m = r_m$, for some matrix $E_m$ with $\norm{A^{-1}} \norm{E_m} \le \eta$;
3. set $x_{m+1} = x_m + d_m$.

Then, if the residuals and updates are computed exactly,
$$\norm{x_{m+1} - x} \le \frac{\eta}{1 - \eta} \norm{x_m - x}$$
for all $m$, so $x_m \to x$ linearly with rate at most $\eta / (1 - \eta) < 1$.

## Remarks

Let $e_m = x - x_m$, so that $r_m = A e_m$.
Then $e_{m+1} = e_m - (A + E_m)^{-1} A e_m = (A + E_m)^{-1} E_m e_m$.
Since $\norm{A^{-1} E_m} \le \eta < 1$, the matrix $A + E_m = A(I + A^{-1} E_m)$ is invertible with $\norm{(A + E_m)^{-1}} \le \norm{A^{-1}} / (1 - \eta)$, which gives the bound.
The matrix $E_m$ models the error of an inexact solver, such as a computed [[LU decomposition|0RKG5YW66Y]] reused at each step, or a solve in lower precision.
If the solver is too inaccurate, so that $\eta \ge 1/2$, the bound gives no contraction and the process can diverge.
This happens when the [[condition number|AB3S6MHJ8X]] of $A$ times the solver's relative accuracy is not small.
In floating-point practice, the residual is the critical step: computing $r_m$ in higher precision lets refinement reach a solution accurate to the working precision, even for fairly ill-conditioned $A$.
In exact arithmetic with $E_m = 0$, one step gives the exact solution.

## Explanations

### L1 human

Solve the system approximately, then check how far off you are by computing the residual $b - Ax$.
The residual is itself the right-hand side of a system for the error, so solve that system approximately too, and add the correction.
Each round removes most of the remaining error, as long as the solver is not too crude.

### L2 human

Iterative refinement turns a cheap or low-precision solver into an accurate one.
It reuses one factorization of $A$, so each extra round costs only $O(n^2)$ operations after the $O(n^3)$ factorization.
Modern mixed-precision solvers factor in low precision and refine in higher precision to get both speed and accuracy.
