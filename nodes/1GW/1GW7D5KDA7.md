---
tag: 1GW7D5KDA7
kind: definition
name: Differential flatness
msc: [93C10, 93B27, 93B18]
defines: 7AX68YJR8C
uses: [ZPDTVZQN5K, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Flatness_(systems_theory)
---

## Definition

Let $f \colon \R^n \times \R^m \to \R^n$ be smooth, and consider the [[control system|ZPDTVZQN5K]] $x' = f(x, u)$ with state $x \in \R^n$ and input $u \in \R^m$.
The system is *differentially flat* if there are integers $r, q \ge 0$ and [[smooth maps|0V33BNKZ9S]] $\varphi$, $\psi$, $\alpha$ with the following properties.

1. A *flat output* $y = \varphi(x, u, u', \dots, u^{(r)})$ with values in $\R^m$ is defined along every trajectory.
2. Along every trajectory, $x = \psi(y, y', \dots, y^{(q)})$ and $u = \alpha(y, y', \dots, y^{(q+1)})$.
3. For every smooth curve $t \mapsto y(t)$ in $\R^m$, the curves $x = \psi(y, \dots, y^{(q)})$ and $u = \alpha(y, \dots, y^{(q+1)})$ form a trajectory of the system.

## Remarks

Clause 3 says that the components of $y$ satisfy no differential equation among themselves, so the trajectories of the system are in one-to-one correspondence with smooth curves $y$.
Often the definition is local: the maps are defined on open sets, and the curves $y$ are restricted accordingly.
Example: for the pendulum $x_1' = x_2$, $x_2' = -\sin x_1 + u$, take $y = x_1$.
Then $x = (y, y')$ and $u = y'' + \sin y$, and for every smooth $y$ these curves solve the equations, so $y$ is a flat output.
Every controllable linear system $x' = A x + B u$ is flat; with one input, a flat output is the first coordinate of the controllable canonical form.
Non-example: $x_1' = u$, $x_2' = -x_2$ is not flat.
Write $x_2 = \psi_2(y, \dots, y^{(q)})$ for a flat output.
By clause 3, $\frac{d}{dt} \psi_2 = \sum_{i=0}^{q} \partial_{y^{(i)}} \psi_2 \, y^{(i+1)}$ equals $-\psi_2$ for every smooth curve $y$, and the values $y(t), \dots, y^{(q+1)}(t)$ can be prescribed freely.
Comparing the terms in $y^{(q+1)}, y^{(q)}, \dots, y'$ one after the other gives that all partial derivatives of $\psi_2$ vanish, and then $\psi_2 = 0$.
By clause 2, $x_2 \equiv 0$ along every trajectory, which fails for the trajectory with $u = 0$, $x_1 = 0$, $x_2(t) = e^{-t}$.
