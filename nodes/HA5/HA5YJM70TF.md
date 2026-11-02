---
tag: HA5YJM70TF
kind: definition
name: Yang–Mills equations
msc: [70S15, 81T13, 53C07]
defines: JJWETW5AT8
uses: [8E37E74XVP, NJ21PN5ZGJ, ZAJFW1S078, 1Y4WX4XQWJ, 5FZDQQHQKM, Q61VFHCH2J]
sources:
  - url: https://en.wikipedia.org/wiki/Yang–Mills_equations
---

## Definition

Let $(M, g)$ be an oriented [[Riemannian manifold|Q61VFHCH2J]] of dimension $n$.
Let $G$ be a compact Lie group with Lie algebra $\mathfrak{g}$, and let $P \to M$ be a [[principal $G$-bundle|8E37E74XVP]].
Let $A$ be a [[connection|NJ21PN5ZGJ]] on $P$ with [[curvature|ZAJFW1S078]] $F_A$, a $2$-form on $M$ with values in the adjoint bundle $\mathrm{ad}\, P = P \times_G \mathfrak{g}$.
Let $d_A$ be the exterior [[covariant derivative|5FZDQQHQKM]] of $A$ on $\mathrm{ad}\, P$-valued forms, and let $\star$ be the [[Hodge star operator|1Y4WX4XQWJ]] of $g$.
The connection $A$ satisfies the *Yang–Mills equations* if
$$d_A \star F_A = 0.$$
Such a connection is called a *Yang–Mills connection*.

## Remarks

The equation is equivalent to $d_A^* F_A = 0$, where $d_A^*$ is the formal adjoint of $d_A$.
Every connection also satisfies the Bianchi identity $d_A F_A = 0$.
For compact $M$, the Yang–Mills connections are the critical points of the Yang–Mills functional $\mathrm{YM}(A) = \tfrac{1}{2} \int_M \abs{F_A}^2 \, d\mathrm{vol}_g$, where the norm uses an invariant inner product on $\mathfrak{g}$.

Example: a flat connection, with $F_A = 0$, satisfies the equations.
On a four-manifold, a connection with $\star F_A = \pm F_A$, an instanton or anti-instanton, also satisfies them, because $d_A \star F_A = \pm d_A F_A = 0$ by the Bianchi identity.

Non-example: let $M = \R^4$ with the Euclidean metric and $G = U(1)$, so that $d_A = d$, and take $A = i x_1^2 \, dx_2$.
Then $F_A = 2i x_1 \, dx_1 \wedge dx_2$, $\star F_A = 2i x_1 \, dx_3 \wedge dx_4$, and $d \star F_A = 2i \, dx_1 \wedge dx_3 \wedge dx_4 \ne 0$.

For $G = U(1)$ and a Lorentzian metric the equations are Maxwell's equations in vacuum.
