---
tag: AXND5JRQAZ
kind: definition
name: Stiff equation
msc: [65L04, 34A99]
defines: RR5FCG92PN
uses: [0P97V20RW7, 0JARTXX4XP, 0BQAA2BK3Q, 047NDTEPCV]
sources:
  - url: https://en.wikipedia.org/wiki/Stiff_equation
---

## Definition

Stiffness is not a single precise condition; the definition below is the standard working one.
Let $I$ be an interval and consider an [[ordinary differential equation|0P97V20RW7]] $y' = f(t, y)$ with $f$ continuously differentiable, on $I$.
The equation is *stiff* on $I$ if explicit methods such as the [[Euler method|0JARTXX4XP]] need much smaller steps than accuracy requires.
The reason is that larger steps make the numerical solution unstable.
Consider a linear system $y' = A y + g(t)$ with a constant $n \times n$ matrix $A$.
Assume its [[eigenvalues|0BQAA2BK3Q]] $\lambda_1, \dots, \lambda_n$ all have $\operatorname{Re} \lambda_i < 0$.
A common measure is then the stiffness ratio
$$\frac{\max_i \abs{\operatorname{Re} \lambda_i}}{\min_i \abs{\operatorname{Re} \lambda_i}},$$
and the system is called stiff when this ratio is large.

## Remarks

Example: $y' = -1000\,(y - \cos t)$.
On the test equation $y' = \lambda y$, the Euler method gives $y_{k+1} = (1 + h\lambda)\, y_k$, which stays bounded only if $\abs{1 + h\lambda} \le 1$.
For $\lambda = -1000$ this forces $h \le 0.002$, although after a short time every solution is close to the smooth particular solution $\frac{10^6}{10^6 + 1} \cos t + \frac{10^3}{10^6 + 1} \sin t$, which is nearly $\cos t$.
The implicit Euler method $y_{k+1} = (1 - h\lambda)^{-1} y_k$ is stable for all $h > 0$ when $\lambda < 0$.
Non-example: $y' = -y$ is not stiff, since its stability bound $h \le 2$ is far larger than the steps needed for accuracy.
For nonlinear equations one uses the eigenvalues of the [[Jacobian matrix|047NDTEPCV]] $\partial f / \partial y$ along the solution.
