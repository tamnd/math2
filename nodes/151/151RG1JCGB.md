---
tag: 151RG1JCGB
kind: statement
role: theorem
name: Beta function in terms of the gamma function
msc: ["33B15"]
uses: [8K9YQ1YGVS, 0H5SYBSED9]
about: [QHNWVSC6AQ, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_function
---

## Statement

Let $x$ and $y$ be complex numbers with $\operatorname{Re} x > 0$ and $\operatorname{Re} y > 0$.
Let $B(x, y) = \int_0^1 t^{x-1} (1-t)^{y-1}\, dt$ be the [[beta function|8K9YQ1YGVS]] and let $\Gamma$ be the [[gamma function|0H5SYBSED9]].
Then
$$B(x, y) = \frac{\Gamma(x)\, \Gamma(y)}{\Gamma(x + y)}.$$

## Remarks

Write $\Gamma(x)\Gamma(y)$ as the double integral $\int_0^\infty \int_0^\infty u^{x-1} v^{y-1} e^{-u-v}\, du\, dv$.
The change of variables $u = st$, $v = s(1-t)$ with $s > 0$ and $0 < t < 1$ has Jacobian $s$.
It turns the double integral into $\int_0^\infty s^{x+y-1} e^{-s}\, ds \cdot \int_0^1 t^{x-1}(1-t)^{y-1}\, dt = \Gamma(x+y)\, B(x, y)$.
Absolute convergence, which needs $\operatorname{Re} x > 0$ and $\operatorname{Re} y > 0$, justifies the change of order.

Example: $B(\frac12, \frac12) = \Gamma(\frac12)^2 / \Gamma(1) = (\sqrt{\pi})^2 = \pi$.
For positive integers $m, n$ the formula gives $B(m, n) = \frac{(m-1)!\,(n-1)!}{(m+n-1)!}$.

Without the condition on the real parts the integral defining $B$ diverges, for example at $x = 0$.
The right side still makes sense there, and it is used to extend $B$ to a meromorphic function of $x$ and $y$.

## Explanations

### L1 human

The beta function is an integral over the interval from $0$ to $1$, and the gamma function is an integral over the whole half line.
This theorem says that the beta function is a simple quotient of gamma values.
So every beta integral can be computed from values of the gamma function.
For whole numbers it becomes a formula with factorials.

### L2 human

The formula is the bridge between the two Euler integrals.
It shows at once that $B(x, y) = B(y, x)$ and gives the analytic continuation of $B$.
With $t = \sin^2 \theta$ it computes integrals $\int_0^{\pi/2} \sin^{a}\theta \cos^{b}\theta\, d\theta$, and with $x = y = \frac12$ it gives $\Gamma(\frac12) = \sqrt{\pi}$.
In probability it gives the normalising constant of the [[beta distribution|0EW824Z7G2]].
