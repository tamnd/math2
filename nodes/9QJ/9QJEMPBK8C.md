---
tag: 9QJEMPBK8C
kind: statement
role: theorem
name: Woltjer's theorem
msc: [78A30, 76W05]
uses: [5V4YEMZ0EA, AHEEC3Y5JF, XRED3C547P, 8PEMR2J7EF]
about: [5V4YEMZ0EA, AHEEC3Y5JF]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_helicity
  - url: https://en.wikipedia.org/wiki/Force-free_magnetic_field
---

## Statement

Let $V \subseteq \R^3$ be a bounded, simply connected open set with smooth boundary and outward unit normal $n$.
Consider smooth [[magnetic fields|XRED3C547P]] $B$ on the closure of $V$ with $\nabla \cdot B = 0$ in $V$ and $B \cdot n = 0$ on $\partial V$.
Let $\mathcal{H}(B)$ be the [[magnetic helicity|5V4YEMZ0EA]] of $B$ in $V$, and let $E(B) = \int_V \abs{B}^2 \, dV$.
Fix a number $h \neq 0$.
If $B$ minimizes $E$ among all such fields with $\mathcal{H}(B) = h$, then $B$ is a linear [[force-free field|AHEEC3Y5JF]]:
$$\nabla \times B = \alpha B \quad \text{in } V$$
for a constant $\alpha \neq 0$.

## Remarks

The proof uses a Lagrange multiplier.
Write $B = \nabla \times A$ with a [[vector potential|8PEMR2J7EF]] $A$ and vary $A$ by a smooth field $a$ with compact support in $V$.
Integration by parts gives $\delta E = 2 \int_V a \cdot (\nabla \times B) \, dV$ and $\delta \mathcal{H} = 2 \int_V a \cdot B \, dV$.
At a constrained minimum $\delta E = \alpha \, \delta \mathcal{H}$ for some constant $\alpha$ and all $a$, so $\nabla \times B = \alpha B$.
The constant is nonzero, since $\alpha = 0$ would make $B$ curl-free, and a curl-free, divergence-free field tangent to the boundary of a simply connected region is zero, which has helicity $0 \neq h$.

Woltjer also showed that the magnetic helicity of a perfectly conducting fluid in a region bounded by a magnetic surface is constant in time.
Together the two results suggest that a turbulent plasma loses energy while keeping its helicity, and settles into a linear force-free state.
This idea was developed into Taylor's theory of plasma relaxation.

## Explanations

### L1 human

Among all magnetic fields in a closed container with the same amount of twisting and linking, the one with the least energy has a special form.
In it the electric current flows along the field lines, with the same proportion everywhere.
So twisted fields cannot relax all the way to zero energy: the twist they carry forces a minimum, and that minimum is a force-free field.

### L2 human

The theorem is a variational characterization of linear force-free fields, also called Beltrami fields, as eigenfields of the curl operator.
In the language of operators, minimizing $\int \abs{B}^2$ with $\int A \cdot B$ fixed is a Rayleigh quotient problem for the inverse of the curl on divergence-free fields tangent to the boundary.
Helicity conservation in ideal magnetohydrodynamics makes this the natural end state of relaxation in solar flares, spheromaks and reversed-field pinches.
