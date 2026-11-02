---
tag: SBQVGQPXT1
kind: definition
name: Control system
msc: [93C15, 34H05, 93C10]
defines: ZPDTVZQN5K
uses: [0NT64JV96A, 0AW1E6YTJY, ZT6F4C2YHK]
sources:
  - url: https://en.wikipedia.org/wiki/Control_theory
---

## Definition

Let $n, m \ge 1$, and let $U \subseteq \R^m$ be a nonempty closed set, the control set.
Let $f \colon \R^n \times U \to \R^n$ be continuous and locally [[Lipschitz|0AW1E6YTJY]] in $x$, locally uniformly in $u$.
The *control system* given by $f$ is the equation
$$x'(t) = f(x(t), u(t)).$$
An *admissible control* on an interval $[0, T]$ is a measurable, essentially bounded function $u \colon [0, T] \to U$.
A *trajectory* for $u$ is an [[absolutely continuous|ZT6F4C2YHK]] function $x \colon [0, T] \to \R^n$ that satisfies the equation for almost every $t \in [0, T]$.
Often a control system also has an output $y(t) = h(x(t))$ with a map $h \colon \R^n \to \R^p$.

## Remarks

Fix an admissible control $u$ and an initial state $x(0) = x_0$.
Then the equation is an [[ordinary differential equation|0NT64JV96A]] in the sense of Carathéodory, and it has a unique trajectory on some interval $[0, \tau)$.
The most important case is the linear system $x' = A x + B u$ with matrices $A \in \R^{n \times n}$ and $B \in \R^{n \times m}$.
Example: the double integrator $x_1' = x_2$, $x_2' = u$ with $U = [-1, 1]$ is linear, with $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$; the control $u = 1$ on $[0, 1)$ and $u = -1$ on $[1, 2]$ is admissible.
Non-example: $u(t) = 1/t$ for $t \in (0, 1]$ is not an admissible control for $U = \R$ on $[0, 1]$, because it is not essentially bounded.
Some authors allow locally integrable controls, or controls of a smaller class such as piecewise continuous ones.
