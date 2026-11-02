---
tag: DVAWCZWT3B
kind: definition
name: Dirichlet-to-Neumann operator
msc: [35J25, 35R30, 35S05]
defines: W783KDGT8E
uses: [S8RG6N1PRT, 8D56GQ4AG8, GS3KT2H645, M4CEZ5K9HP, Z2T5R88QDB, FF27N0BWTP]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Steklov_operator
---

## Definition

Let $\Omega \subset \R^n$, $n \ge 2$, be a bounded connected open set with smooth boundary $\partial\Omega$ and outward unit normal $\nu$.
Let $H^{1/2}(\partial\Omega)$ and $H^{-1/2}(\partial\Omega)$ be the boundary [[Sobolev spaces|M4CEZ5K9HP]] of order $\tfrac12$ and $-\tfrac12$.
For $f \in H^{1/2}(\partial\Omega)$, let $u_f \in H^1(\Omega)$ be the weak solution of the [[Dirichlet problem|8D56GQ4AG8]]
$$\Delta u = 0 \text{ in } \Omega, \qquad u = f \text{ on } \partial\Omega.$$
The boundary condition is taken in the sense of the [[trace operator|Z2T5R88QDB]].
The *Dirichlet-to-Neumann operator* is the map
$$\Lambda \colon H^{1/2}(\partial\Omega) \to H^{-1/2}(\partial\Omega), \qquad \Lambda f = \partial_\nu u_f|_{\partial\Omega}.$$
More generally, let $\gamma$ be measurable on $\Omega$ with $c \le \gamma \le c^{-1}$ for some $c > 0$.
The operator $\Lambda_\gamma$ uses the equation $\nabla \cdot (\gamma \nabla u) = 0$ and the weakly defined [[Neumann data|GS3KT2H645]] $\gamma \, \partial_\nu u|_{\partial\Omega}$.

## Remarks

Example: let $\Omega$ be the unit disk and $f(\theta) = e^{ik\theta}$ with $k \in \Z$.
Then $u_f = r^{\abs{k}} e^{ik\theta}$ is harmonic, and $\partial_r u_f = \abs{k}$ at $r = 1$, so $\Lambda f = \abs{k} f$.
Thus on the circle $\Lambda = (-\partial_\theta^2)^{1/2}$.
Non-example: replacing $\Delta u = 0$ by $\Delta u + \lambda u = 0$, where $\lambda$ is a Dirichlet eigenvalue of $-\Delta$ on $\Omega$, does not define a map, because the boundary value problem has no unique solution.
In general $\Lambda$ is self-adjoint and nonnegative on $L^2(\partial\Omega)$, with kernel the constants, and it is a first-order elliptic [[pseudo-differential operator|FF27N0BWTP]] with principal symbol $\abs{\xi}$.
It is also called the Poincaré–Steklov operator, and the weak form is $\int_{\partial\Omega} (\Lambda f) \, g = \int_\Omega \nabla u_f \cdot \nabla u_g$.
