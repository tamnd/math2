---
tag: NGYZK893VE
kind: definition
name: Krylov–Bogolyubov averaging
msc: [34C29, 70K65]
defines: 6TJ7YHP2HE
uses: [0NT64JV96A, 0ATF6Q0633, 0VW90BBSJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Krylov%E2%80%93Bogoliubov_averaging_method
---

## Definition

Let $D \subseteq \R^n$ be open, let $T > 0$, and let $f \colon D \times \R \to \R^n$ be [[continuously differentiable|0VW90BBSJ4]] and [[periodic|0ATF6Q0633]] of period $T$ in its last variable.
For a small parameter $\varepsilon > 0$, consider the [[differential equation|0NT64JV96A]] in standard form
$$x' = \varepsilon f(x, t).$$
The *averaged function* is
$$\bar f(y) = \frac{1}{T} \int_0^T f(y, t)\, dt, \qquad y \in D,$$
and the *averaged equation* is $y' = \varepsilon \bar f(y)$.
*Krylov–Bogolyubov averaging* is the method of approximating the solutions of the equation in standard form by the solutions of the averaged equation.

## Remarks

The first averaging theorem justifies the method.
Let $x$ and $y$ solve the two equations with $x(0) = y(0)$, and let $L > 0$ be such that $y(t)$ stays in a compact subset of $D$ for $0 \le t \le L/\varepsilon$.
Then there is a constant $C$, independent of $\varepsilon$, with $\norm{x(t) - y(t)} \le C \varepsilon$ for $0 \le t \le L/\varepsilon$ and all small $\varepsilon$.

Example: $f(x, t) = x \sin^2 t$ on $\R$ with $T = \pi$.
Then $\bar f(y) = \frac{1}{\pi} \int_0^\pi y \sin^2 t\, dt = \frac{1}{2} y$.
The solutions are $x(t) = x_0 e^{\varepsilon (t/2 - \sin(2t)/4)}$ and $y(t) = x_0 e^{\varepsilon t/2}$.
Their ratio is $e^{-\varepsilon \sin(2t)/4} = 1 + O(\varepsilon)$, so the difference is $O(\varepsilon)$ on intervals of length of order $1/\varepsilon$.

Non-example: $x' = \varepsilon x t$ is not periodic in $t$, so it is not in the standard form above, and there is no period over which to average.

Weakly nonlinear oscillators $u'' + u = \varepsilon h(u, u')$ are put in standard form by writing $u = r \cos(t + \phi)$, $u' = -r \sin(t + \phi)$ and using $(r, \phi)$ as the new unknowns.
