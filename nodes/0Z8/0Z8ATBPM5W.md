---
tag: 0Z8ATBPM5W
kind: counterexample
name: The complex conjugate is not holomorphic
aliases: [z-conjugate-is-not-holomorphic]
msc: [30A99]
uses: [0BJV24C4SY, 0D1C9Y1EXA, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Holomorphic_function
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
    locator: Independence of the complex conjugate
---

## Counterexample

Let $f : \mathbb{C} \to \mathbb{C}$ be the [[complex conjugate|0BJV24C4SY]] map, $f(z) = \bar z$.
The function $f$ is continuous, but it is not [[complex differentiable|0D1C9Y1EXA]] at any point $z_0 \in \mathbb{C}$.
Thus $f$ is not [[holomorphic|0DG0Z72CQD]] on any nonempty open set.
Proof: the difference quotient at $z_0$ is
$$\frac{f(z_0 + h) - f(z_0)}{h} = \frac{\bar h}{h}.$$
It is $1$ for each real $h \neq 0$ and $-1$ for each purely imaginary $h \neq 0$. So it has no limit as $h \to 0$.

## Remarks

The real and imaginary parts $u = x$ and $v = -y$ are differentiable, but $u_x = 1$ and $v_y = -1$. So the [[Cauchy–Riemann equations|0T71SSYZ39]] fail at each point.
As a map of $\mathbb{R}^2$, $f$ is the reflection in the real axis. It is real linear but not complex linear.
For the same reason, $\operatorname{Re} z$, $\operatorname{Im} z$ and $|z|$ are not holomorphic on any nonempty open set.

## Explanations

### L1 human

As a map of the plane, conjugation is a mirror, and it is very smooth.
But a complex derivative must be the same in each direction, and conjugation fixes the real direction and reverses the imaginary direction.
So the quotient gives $1$ in one direction and $-1$ in the other, and there is no complex derivative.
