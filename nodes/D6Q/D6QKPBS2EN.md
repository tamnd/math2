---
tag: D6QKPBS2EN
kind: statement
role: theorem
name: Post's inversion formula
msc: [44A10]
uses: [05XT5AVJBK, VEPJN1NK3C]
about: [07WBTX1MHA]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$.
Assume that the Laplace integral of $f$ converges at some real number $s_0$, and let $F$ be the [[Laplace transform|05XT5AVJBK]] of $f$.
Then for every $t > 0$ at which $f$ is continuous,
$$f(t) = \lim_{k \to \infty} \frac{(-1)^k}{k!} \left(\frac{k}{t}\right)^{k+1} F^{(k)}\!\left(\frac{k}{t}\right),$$
where $F^{(k)}$ is the $k$-th derivative of $F$ on the real half-line $s > s_0$.

## Remarks

By [[differentiation in the transform variable|VEPJN1NK3C]], $\frac{(-1)^k}{k!} \left(\frac{k}{t}\right)^{k+1} F^{(k)}\!\left(\frac{k}{t}\right) = \int_0^\infty f(u) \, \frac{1}{k!} \left(\frac{k}{t}\right)^{k+1} u^k e^{-k u / t} \, du$.
The kernel in this integral is a probability density in $u$ (a gamma density) with mean $t (k+1)/k$ and variance $t^2 (k+1)/k^2$.
As $k \to \infty$ it concentrates at $u = t$, so the integral tends to $f(t)$ at points of continuity.
Example: for $f(t) = e^{-t}$, $F(s) = 1/(s + 1)$ and $\frac{(-1)^k}{k!} F^{(k)}(s) = (s+1)^{-k-1}$, so the expression is $\left(\frac{k/t}{k/t + 1}\right)^{k+1} = \left(1 + \frac{t}{k}\right)^{-k-1} \to e^{-t}$.

## Explanations

### L1 human

This formula recovers a function from its Laplace transform using only values of the transform and its derivatives at real points.
No complex integration is needed.
The price is that one needs derivatives of very high order.

### L2 human

The formula matters in theory, for example in the theory of semigroups, where it gives the exponential formula for $T(t)$.
Numerically it is poor: high derivatives amplify small errors, which reflects the [[ill-posedness of real Laplace inversion|TRTN840ZB0]].
The method of proof, a kernel that concentrates at one point, is the same as in many approximation theorems.
