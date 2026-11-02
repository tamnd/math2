---
tag: XQTHXW4F1R
kind: definition
name: Laplace transform method for convolution equations
msc: [45D05, "45E10", 44A10]
defines: EHGECREYB4
uses: [SNFYTC1TTA, 0V49JEZW06, 0JNMJEDD93, 07WBTX1MHA]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Definition

Let $k$ and $f$ be locally integrable functions on $[0, \infty)$ whose [[Laplace transforms|0V49JEZW06]] $\hat k(p) = \int_0^\infty e^{-pt} k(t) \, dt$ and $\hat f(p)$ converge absolutely for $\operatorname{Re} p > c$, for some real $c$.
Consider the [[Volterra equation of convolution type|SNFYTC1TTA]]
$$x(t) = f(t) + \int_0^t k(t - s) \, x(s) \, ds, \quad t \ge 0.$$
The *Laplace transform method* for this equation consists of the following steps.

1. Assume that the solution $x$ has a Laplace transform $\hat x$, and apply the [[convolution theorem|0JNMJEDD93]] to get $\hat x(p) = \hat f(p) + \hat k(p) \, \hat x(p)$.
2. Solve: $\hat x(p) = \dfrac{\hat f(p)}{1 - \hat k(p)}$ for $\operatorname{Re} p$ large enough that $\hat k(p) \ne 1$.
3. Recover $x$ as the [[inverse Laplace transform|07WBTX1MHA]] of $\hat x$, and check that it solves the equation.

For an equation of the first kind $\int_0^t k(t - s) \, x(s) \, ds = f(t)$, step 2 becomes $\hat x = \hat f / \hat k$.

## Remarks

Example: $x(t) = t - \int_0^t (t - s) \, x(s) \, ds$, with $k(u) = -u$ and $f(t) = t$.
Here $\hat k(p) = -1/p^2$ and $\hat f(p) = 1/p^2$, so $\hat x(p) = \frac{1/p^2}{1 + 1/p^2} = \frac{1}{p^2 + 1}$ and $x = \sin$.
Check: $\int_0^t (t - s) \sin s \, ds = t - \sin t$, so the right side is $\sin t$.
Non-example: the method does not apply directly to $x(t) = 1 + \int_0^t ts \, x(s) \, ds$, since the kernel $ts$ is not a function of $t - s$, and the transform of the integral term is not a product.
The step 1 assumption is harmless when $k$ and $f$ are as above: the unique locally integrable solution then has a Laplace transform for $\operatorname{Re} p$ large.
The function $r$ with $\hat r = \hat k / (1 - \hat k)$ is the resolvent kernel, and $x = f + r * f$.
