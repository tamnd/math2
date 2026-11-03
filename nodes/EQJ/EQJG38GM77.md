---
tag: EQJG38GM77
kind: definition
name: Feedback
msc: [93B52, 93D15]
defines: 7NYES2D0Z4
uses: [ZPDTVZQN5K]
sources:
  - url: https://en.wikipedia.org/wiki/Feedback
---

## Definition

Let $x' = f(x, u)$, $y = h(x)$ be a [[control system|ZPDTVZQN5K]] with state $x \in \R^n$, input $u \in \R^m$ and output $y \in \R^p$.

1. A *static output feedback* is a map $k \colon \R^p \to \R^m$; it sets $u(t) = k(y(t))$, and the *closed-loop system* is $x' = f(x, k(h(x)))$.
2. A *state feedback* is a map $k \colon \R^n \to \R^m$; it sets $u(t) = k(x(t))$, and the closed-loop system is $x' = f(x, k(x))$.
3. A *dynamic feedback* is a second control system $z' = g(z, y)$, $u = k(z, y)$, the controller, driven by the output $y$. The closed-loop system is the coupled system for $(x, z)$.

## Remarks

In each case the input is computed from measured quantities while the system runs.
This distinguishes feedback from open-loop control, where $u$ is a fixed function of time chosen in advance.
Example: for $x' = x + u$ with $y = x$, the state feedback $k(x) = -2x$ gives the closed loop $x' = -x$, whose solutions $x(t) = e^{-t} x(0)$ tend to $0$.
Non-example: the open-loop input $u(t) = -2 e^{-t} x_0$ steers the same system from the known state $x_0$ along $x(t) = e^{-t} x_0$.
It is not a feedback, because it is not computed from $x$ or $y$, and a small error in $x_0$ then grows like $e^{t}$.
In block diagrams one often writes negative feedback with a reference $r$: the controller acts on the error $e = r - y$.
