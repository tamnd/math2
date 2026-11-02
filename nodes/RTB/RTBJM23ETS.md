---
tag: RTBJM23ETS
kind: statement
role: theorem
name: Petrov–Galerkin method
msc: [65N30, 65N12]
uses: [HM2HHE3J51, 0SQZMXB6GP, 4A82S5FVRT, Y5B0PEBKE8]
about: [Y5B0PEBKE8]
sources:
  - url: https://en.wikipedia.org/wiki/Petrov%E2%80%93Galerkin_method
---

## Statement

Let $U$ and $V$ be real [[Hilbert spaces|HM2HHE3J51]].
Let $a \colon U \times V \to \R$ be a [[bilinear form|0SQZMXB6GP]] with $\abs{a(w, v)} \le M \norm{w}_U \norm{v}_V$ for all $w \in U$ and $v \in V$, and let $f$ be in the [[continuous dual space|4A82S5FVRT]] $V'$.
Let $u \in U$ satisfy $a(u, v) = f(v)$ for all $v \in V$.
Let $U_h \subseteq U$ (trial space) and $V_h \subseteq V$ (test space) be finite-dimensional subspaces of the same dimension, with
$$\beta_h = \inf_{w \in U_h \setminus \set{0}} \ \sup_{v \in V_h \setminus \set{0}} \frac{a(w, v)}{\norm{w}_U \norm{v}_V} > 0.$$
Then there is a unique $u_h \in U_h$ with $a(u_h, v) = f(v)$ for all $v \in V_h$, and
$$\norm{u - u_h}_U \le \Big( 1 + \frac{M}{\beta_h} \Big) \inf_{w \in U_h} \norm{u - w}_U.$$

## Remarks

In bases of $U_h$ and $V_h$ the discrete problem is a square linear system.
The condition $\beta_h > 0$ says that $a(w, v) = 0$ for all $v \in V_h$ forces $w = 0$, so the system matrix is injective and therefore invertible.
Subtracting the equations gives $a(u - u_h, v) = 0$ for all $v \in V_h$.
For $w \in U_h$ this gives $\beta_h \norm{u_h - w} \le \sup_{v} a(u_h - w, v) / \norm{v} = \sup_{v} a(u - w, v) / \norm{v} \le M \norm{u - w}$.
The triangle inequality $\norm{u - u_h} \le \norm{u - w} + \norm{w - u_h}$ then gives the bound.

The case $U = V$ and $U_h = V_h$ is the [[Galerkin method|Y5B0PEBKE8]]; there, coercivity with constant $\alpha$ gives $\beta_h \ge \alpha$.
Example: in the streamline upwind Petrov–Galerkin method for $-\varepsilon u'' + u' = f$, each test function is a trial hat function plus a multiple of its derivative, which adds stabilisation along the flow.

A positive $\beta_h$ is needed: with $\beta_h = 0$ the discrete system is singular, and with $\beta_h \to 0$ along a family of meshes the bound degenerates.

## Explanations

### L1 human

In the Galerkin method one searches and tests in the same space of functions.
The Petrov–Galerkin method allows two different spaces: one where the approximate solution lives, and one that is used to test the equation.
The theorem says that the method works, and gives a nearly best approximation, as long as the two spaces fit together well, as measured by the number $\beta_h$.

### L2 human

The theorem is the discrete half of the Babuška theory of problems that are well posed but not coercive.
It explains why different test spaces can stabilise convection-dominated problems and why some choices of spaces fail.
Its constant $1 + M / \beta_h$ can be improved to $M / \beta_h$ in Hilbert spaces, a result of Xu and Zikatanov.
For saddle-point problems, the analogous condition is the [[Ladyzhenskaya–Babuška–Brezzi condition|SC5FV3GHV5]].
