---
tag: WCSZYPBZY4
kind: example
name: Laplace transform method for the heat equation
msc: [44A10, 35K05, 35A22]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, VP2HN86VAG, TZ3CT1YA9B, 0JRW4X1MDC]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Example

Consider the [[heat equation|VP2HN86VAG]] on the half-line, for an unknown function $u(x, t)$ with $x > 0$ and $t > 0$:
$$u_t = u_{xx}, \qquad u(x, 0) = 0, \qquad u(0, t) = 1, \qquad u \text{ bounded}.$$
This models a cold rod, initially at temperature $0$, whose end $x = 0$ is held at temperature $1$ from time $0$ on.
Let $U(x, s) = \int_0^\infty u(x, t) e^{-s t} \, dt$ be the [[Laplace transform|05XT5AVJBK]] in the time variable, for real $s > 0$.
Since $u(x, 0) = 0$, the transform of $u_t$ is $s U$, so the equation becomes the ordinary differential equation $U_{xx} = s U$ in $x$.
Its solutions are $U = A(s) e^{-x \sqrt{s}} + B(s) e^{x \sqrt{s}}$.
Boundedness in $x$ forces $B(s) = 0$, and the boundary condition gives $U(0, s) = \mathcal{L}\{1\}(s) = 1/s$, so $A(s) = 1/s$.
Hence $U(x, s) = e^{-x \sqrt{s}} / s$.
The table pair $\mathcal{L}\{\operatorname{erfc}(x / (2 \sqrt{t}))\}(s) = e^{-x \sqrt{s}} / s$, for fixed $x > 0$, gives the [[inverse transform|0JRW4X1MDC]]:
$$u(x, t) = \operatorname{erfc}\left(\frac{x}{2 \sqrt{t}}\right),$$
where $\operatorname{erfc}$ is the [[complementary error function|TZ3CT1YA9B]].
Check: as $t \to 0^+$ with $x > 0$ fixed, $\operatorname{erfc}(x/(2\sqrt{t})) \to \operatorname{erfc}(+\infty) = 0$; at $x = 0$, $\operatorname{erfc}(0) = 1$; and $0 \le u \le 1$ for $x \ge 0$, so $u$ is bounded.

## Explanations

### L1 human

The Laplace transform in time removes the time derivative from the heat equation.
What is left is an ordinary differential equation in space, which one can solve by hand.
Transforming back gives the temperature profile $\operatorname{erfc}(x / (2 \sqrt{t}))$: the heat front spreads like $\sqrt{t}$.
