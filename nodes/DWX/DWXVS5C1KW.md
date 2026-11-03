---
tag: DWXVS5C1KW
kind: definition
name: Nonlinear control
msc: [93C10, 93D15, 93B52]
defines: RZ94FKGZ5Z
uses: [ZPDTVZQN5K, 21FN2KSTJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_control
---

## Definition

Let $n, m, p \ge 1$.
Let $f \colon \R^n \times \R^m \to \R^n$ and $h \colon \R^n \to \R^p$ be maps that are not required to be linear.
A *nonlinear control system* is a [[control system|ZPDTVZQN5K]]
$$x'(t) = f(x(t), u(t)), \qquad y(t) = h(x(t)),$$
with state $x(t) \in \R^n$, input $u(t) \in \R^m$ and output $y(t) \in \R^p$.
*Nonlinear control* is the study of the stability, controllability and observability of such systems.
It also designs feedback laws $u = k(x)$ or $u = k(y)$ that give the closed loop a prescribed behaviour, such as global asymptotic stability of an equilibrium.

## Remarks

The [[linear systems|21FN2KSTJZ]] are the special case $f(x, u) = A x + B u$ and $h(x) = C x$ with constant matrices $A$, $B$, $C$.
An important intermediate class is the control-affine systems $x' = f(x) + g(x) u$, which are linear in $u$ but not in $x$.
Example: the pendulum $x_1' = x_2$, $x_2' = -\sin x_1 + u$ is control-affine and nonlinear, because $\sin$ is not linear.
Non-example of a nonlinear system in the strict sense: $x' = -x + u$ is linear, and linear methods describe it completely.
