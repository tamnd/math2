---
tag: MY491MR2PJ
kind: statement
role: theorem
name: Hermite–Genocchi formula
msc: [65D05, 41A05]
uses: [N5ZHV4HWDC, YX1DJK2QAG, 2Z2QVWZ262, 0V1EJCT8G6]
about: [N5ZHV4HWDC]
sources:
  - url: https://en.wikipedia.org/wiki/Divided_differences
---

## Statement

Let $n \ge 1$, let $I \subseteq \R$ be an interval, and let $f \colon I \to \R$ be $n$ times continuously differentiable.
Let $x_0, \dots, x_n \in I$ be pairwise distinct.
Let $\Sigma_n = \set{(t_1, \dots, t_n) \in \R^n : t_i \ge 0, \ t_1 + \cdots + t_n \le 1}$ and set $t_0 = 1 - t_1 - \cdots - t_n$.
Then the [[divided difference|N5ZHV4HWDC]] of $f$ is
$$f[x_0, \dots, x_n] = \int_{\Sigma_n} f^{(n)}(t_0 x_0 + t_1 x_1 + \cdots + t_n x_n) \, dt_1 \cdots dt_n,$$
where the integral is with respect to [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$.

## Remarks

The point $t_0 x_0 + \cdots + t_n x_n$ runs over the convex hull of the nodes, so the integrand is defined.
For $n = 1$ the formula reads $\frac{f(x_1) - f(x_0)}{x_1 - x_0} = \int_0^1 f'(x_0 + t(x_1 - x_0)) \, dt$, which is the fundamental theorem of calculus.
The general case follows by induction on $n$: integrating over the last variable and using the case $n - 1$ reproduces the recursion that defines divided differences.

Since $\Sigma_n$ is a [[simplex|YX1DJK2QAG]] of volume $1/n!$, the formula gives $f[x_0, \dots, x_n] = f^{(n)}(\xi)/n!$ for some $\xi$ between the smallest and largest node.
This is a form of the [[mean value theorem for divided differences|BQJ9C1CD5X]].
The right side is a continuous function of $(x_0, \dots, x_n)$ even when nodes coincide.
So it serves as the definition of divided differences with repeated nodes, which is what [[Hermite interpolation|9Z50M2WPTP]] uses.

## Explanations

### L1 human

A divided difference is a ratio of differences of values.
The formula says that it is also an average of a high derivative of $f$, taken over all weighted mixtures of the nodes.
So divided differences are smoothed derivatives.

### L2 human

The formula shows at once that $f[x_0, \dots, x_n]$ is symmetric in the nodes and depends continuously on them.
Letting all nodes tend to one point $x$ gives $f[x, \dots, x] = f^{(n)}(x)/n!$, the Taylor coefficient.
It is the bridge between [[Newton interpolation|9W77FPTM9E]] and [[Taylor polynomials|0HFSFVMWQB]].
