---
tag: XX51FGFAMY
kind: definition
name: Zero dynamics
msc: [93C10, 93B27, 93B18]
defines: W3N8APDEB9
uses: [115PDNE89R, PJWK0PKN6Q, 0299VCW1TH, 0N8NGKDZDZ]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_dynamics
---

## Definition

Let $W \subseteq \R^n$ be open, let $f, g \colon W \to \R^n$ be smooth vector fields and let $h \colon W \to \R$ be smooth.
Consider the system $x' = f(x) + g(x) u$, $y = h(x)$, and let $x_0 \in W$ be an [[equilibrium|0N8NGKDZDZ]] of $x' = f(x)$ with $h(x_0) = 0$.
Assume the system has [[relative degree|115PDNE89R]] $r < n$ at $x_0$, and write $L_f$, $L_g$ for [[Lie derivatives|PJWK0PKN6Q]].
Then there is an open neighbourhood $N$ of $x_0$ such that $L_g L_f^{r-1} h \ne 0$ on $N$ and
$$Z = \set{x \in N : h(x) = L_f h(x) = \cdots = L_f^{r-1} h(x) = 0}$$
is a submanifold of dimension $n - r$ containing $x_0$.
Put
$$u^*(x) = -\frac{L_f^r h(x)}{L_g L_f^{r-1} h(x)}, \qquad x \in N.$$
The vector field $f + g u^*$ is tangent to $Z$.
The *zero dynamics* of the system at $x_0$ is the restriction of the differential equation $x' = f(x) + g(x) u^*(x)$ to $Z$.

## Remarks

A solution of the system keeps $y \equiv 0$ near $x_0$ exactly when it stays in $Z$ and uses the input $u = u^*(x)$, so the zero dynamics describe all motions with zero output.
Example: for $x_1' = x_2$, $x_2' = u$, $y = x_1 + x_2$ one has $L_g h = 1$, so $r = 1$, $u^*(x) = -x_2$ and $Z = \set{x_1 + x_2 = 0}$.
On $Z$, the equation $x_1' = x_2 = -x_1$ is the zero dynamics; it is asymptotically stable, matching the zero $s = -1$ of the transfer function $(s + 1)/s^2$.
Non-example: with $y = x_1 - x_2$ instead, $L_g h = -1$, $u^* = x_2$, $Z = \set{x_1 = x_2}$ and the zero dynamics $x_1' = x_1$ is unstable, so this output does not give a [[minimum phase|7PWB4YS8PA]] system.
For a linear system with a minimal realization, the eigenvalues of the zero dynamics are the zeros of the transfer function.
In normal form coordinates $(\xi, \eta)$ with $\xi_i = L_f^{i-1} h$, the system reads $\xi_r' = L_f^r h + L_g L_f^{r-1} h\, u$, $\eta' = q(\xi, \eta)$, and the zero dynamics are $\eta' = q(0, \eta)$.
