---
tag: 1Y9X1YW6GH
kind: statement
role: theorem
name: Loewner's torus inequality
msc: [53C23, 53C20]
uses: [PZCJV40M4K, Q61VFHCH2J]
about: [PZCJV40M4K]
sources:
  - url: https://en.wikipedia.org/wiki/Loewner%27s_torus_inequality
same_as:
  wikidata: Q3154012
  wikipedia: Loewner's torus inequality
---

## Statement

Let $g$ be a [[Riemannian metric|Q61VFHCH2J]] on the torus $T^2$.
Let $\operatorname{sys}(g)$ be its [[systole|PZCJV40M4K]] and $\operatorname{area}(g)$ its area.
Then
$$\operatorname{sys}(g)^2 \le \frac{2}{\sqrt{3}} \operatorname{area}(g).$$
Let $\Lambda_h \subset \R^2$ be the hexagonal lattice spanned by $(1, 0)$ and $(\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})$.
Equality holds exactly when $g$ is flat and isometric to a constant multiple of the metric of $\R^2 / \Lambda_h$.

## Remarks

By the uniformization theorem, $g$ is conformal to a flat metric $g_0$, so $g = f^2 g_0$ for a positive function $f$.
Averaging $f$ over the translations of the flat torus gives a flat metric.
By the Cauchy–Schwarz inequality its area is at most that of $g$, and by averaging lengths over translates of a closed geodesic its systole is at least that of $g$.
For a flat torus $\R^2 / \Lambda$, the claim is that the shortest nonzero vector $v$ of a lattice $\Lambda$ of covolume $A$ satisfies $\abs{v}^2 \le \tfrac{2}{\sqrt{3}} A$.
This follows by reduction of a basis of $\Lambda$, and the hexagonal lattice is the extreme case.

For the square torus $\R^2/\Z^2$ the two sides are $1$ and $2/\sqrt{3} \approx 1.155$.
For the hexagonal torus above, the systole is $1$ and the area is $\sqrt{3}/2$, so equality holds.

## Explanations

### L1 human

On any doughnut-shaped surface, take the shortest loop that goes around a hole.
The inequality says that the square of its length is at most about $1.155$ times the area.
So a surface whose short loops are all long must have a large area.
The best shape is the flat torus glued from a rhombus made of two equilateral triangles.

### L2 human

This is the first result of [[systolic geometry|PZCJV40M4K]], and the model for [[Gromov's systolic inequality|HB2K72PSZ6]] in higher dimensions.
The constant $2/\sqrt{3}$ is the Hermite constant $\gamma_2$ of the geometry of numbers.
The proof pattern, reduction to the most symmetric metrics in a conformal class by averaging, recurs in other optimal systolic inequalities.
