---
tag: EWFW0P9KKC
kind: definition
name: Entropy solution
msc: [35L65, 35D30]
defines: 1A01A3EJRX
uses: [SJZX81A783, 0VW90BBSJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Conservation_law
---

## Definition

Let $n \ge 1$, let $f \colon \R \to \R^n$ be [[continuously differentiable|0VW90BBSJ4]], and let $g \colon \R^n \to \R$ be bounded and measurable.
Consider the scalar conservation law
$$u_t + \operatorname{div} f(u) = 0 \text{ in } \R^n \times (0, \infty), \qquad u(x, 0) = g(x).$$
A bounded measurable function $u \colon \R^n \times (0, \infty) \to \R$ is an *entropy solution* in the sense of Kruzhkov if the following holds.
For every real number $k$ and every nonnegative test function $\varphi \in C_c^\infty(\R^n \times \R)$,
$$\int_0^\infty \!\! \int_{\R^n} \Big( \abs{u - k} \, \varphi_t + \sgn(u - k) \big( f(u) - f(k) \big) \cdot \nabla_x \varphi \Big) \, dx \, dt + \int_{\R^n} \abs{g - k} \, \varphi(x, 0) \, dx \ge 0.$$

## Remarks

Take $k$ larger than $\sup \abs{u}$ and $\sup \abs{g}$, and then smaller than $-\sup \abs{u}$ and $-\sup \abs{g}$.
This gives two opposite inequalities whose combination says that $u$ is a [[weak solution|SJZX81A783]] of the initial value problem.
So every entropy solution is a weak solution.
Kruzhkov's theorem states that for each bounded measurable $g$ there is exactly one entropy solution, and that it depends continuously on $g$ in $L^1_{\mathrm{loc}}$.
Let $u$ be piecewise smooth in one space dimension, with $f$ strictly convex.
Then the condition is equivalent to the Rankine–Hugoniot jump condition together with the Lax condition $u_- > u_+$ across each shock.
Here $u_-$ and $u_+$ are the values to the left and to the right of the shock.

Example: for Burgers' equation, $n = 1$ and $f(u) = u^2/2$, with $g = 1$ for $x < 0$ and $g = 0$ for $x > 0$, the shock $u = 1$ for $x < t/2$ and $u = 0$ for $x > t/2$ is the entropy solution.
Its speed $1/2$ is $(f(1) - f(0))/(1 - 0)$, as Rankine–Hugoniot requires, and $u_- = 1 > 0 = u_+$.

Non-example: with $g = 0$ for $x < 0$ and $g = 1$ for $x > 0$, the shock $u = 0$ for $x < t/2$ and $u = 1$ for $x > t/2$ is a weak solution but not an entropy solution, because $u_- = 0 < 1 = u_+$.
The entropy solution is the rarefaction fan $u = 0$ for $x < 0$, $u = x/t$ for $0 \le x \le t$, and $u = 1$ for $x > t$.
