---
tag: SZ6MEVM89M
kind: counterexample
name: Hadamard's example of ill-posedness
msc: [35R25, "35J05"]
uses: [W09B9NZ9B5, S8RG6N1PRT]
sources:
  - url: https://en.wikipedia.org/wiki/Well-posed_problem
---

## Counterexample

Consider the Cauchy problem for the [[Laplace equation|S8RG6N1PRT]] in the half-plane $y > 0$:
$$\partial_x^2 u + \partial_y^2 u = 0 \ \text{ for } y > 0, \qquad u(x, 0) = 0, \qquad \partial_y u(x, 0) = g(x).$$
For an integer $n \ge 1$, take the datum $g_n(x) = \frac{1}{n} \sin(n x)$.
The function
$$u_n(x, y) = \frac{1}{n^2} \sinh(n y) \sin(n x)$$
solves the problem.
Indeed $\partial_x^2 u_n = -n^2 u_n$ and $\partial_y^2 u_n = n^2 u_n$, so the Laplace equation holds.
Also $u_n(x, 0) = 0$, since $\sinh 0 = 0$, and $\partial_y u_n(x, 0) = \frac{1}{n} \cosh(0) \sin(n x) = g_n(x)$.
The data tend to $0$ uniformly: $\sup_x \abs{g_n(x)} = 1/n \to 0$.
For the zero datum $g = 0$ the solution is $u = 0$.
But for every fixed $y > 0$, $\sup_x \abs{u_n(x, y)} = \sinh(n y) / n^2 \to \infty$.
So the solution does not depend continuously on the data, and the problem is not [[well posed|W09B9NZ9B5]].

## Remarks

Uniqueness holds here, by [[Holmgren's uniqueness theorem|1VVKF0Y19B]], so the failure is only in the continuous dependence.
The same holds with any norm on the data that involves finitely many derivatives, since the $k$-th derivative of $g_n$ has size $n^{k-1}$, while $\sinh(n y)$ grows exponentially in $n$.
The example also explains why the [[Cauchy–Kovalevskaya theorem|97HMV9BT2W]], which does give a solution for analytic data, is not a well-posedness result.
The natural problems for the Laplace equation are boundary value problems such as the Dirichlet problem, which are well posed.

## Explanations

### L1 human

For the Laplace equation one may not prescribe both the value and the slope of the solution along a line.
Data that are tiny, but oscillate fast, produce solutions that become enormous a short distance away.
So arbitrarily small errors in the data can cause arbitrarily large errors in the solution.
