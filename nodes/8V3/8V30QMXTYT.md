---
tag: 8V30QMXTYT
kind: definition
name: Rational singularity
msc: [14B05, "14E15"]
defines: 98QASBAMEB
uses: [HV6YBS0YDH, EK261G1XP9, MB52NDA6WN, PQ6Q143ARJ, 9537RKBZPP, KA5890R9YM]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_singularity
---

## Definition

Let $k$ be a field of characteristic $0$ and let $X$ be a normal [[algebraic variety|HV6YBS0YDH]] over $k$ (see [[normal scheme|EK261G1XP9]]).
Let $f \colon Y \to X$ be a [[resolution of singularities|MB52NDA6WN]], that is, a [[proper|9537RKBZPP]] [[birational|KA5890R9YM]] morphism from a nonsingular variety $Y$.
The variety $X$ has *rational singularities* if
$$R^i f_* \mathcal{O}_Y = 0 \quad \text{for all } i > 0,$$
where $R^i f_*$ are the higher direct images, computed by [[sheaf cohomology|PQ6Q143ARJ]] on preimages of open sets.
A point $x \in X$ is a *rational singularity* if some open neighbourhood of $x$ has rational singularities.

## Remarks

The condition does not depend on the chosen resolution.
Since $X$ is normal and $f$ is proper and birational, one also has $f_* \mathcal{O}_Y = \mathcal{O}_X$, by Zariski's main theorem.
Every nonsingular variety has rational singularities, with $f = \id$.
Example: for the cone $X \colon xy = z^2$ in $\mathbb{A}^3$, the blow-up of the vertex is a resolution whose exceptional curve is $E \cong \mathbb{P}^1$ with normal bundle $\mathcal{O}(-2)$.
Here $Y$ is the total space of the line bundle $\mathcal{O}(-2)$ on $E$, and $X$ is affine, so $R^1 f_* \mathcal{O}_Y$ is determined by $H^1(Y, \mathcal{O}_Y) = \bigoplus_{m \ge 0} H^1(\mathbb{P}^1, \mathcal{O}(2m)) = 0$.
So the singularity is rational.
Non-example: for the cone $X \colon x^3 + y^3 + z^3 = 0$ over a smooth plane cubic $E$, the blow-up of the vertex is the total space of $\mathcal{O}_E(-1)$, and the same computation gives $H^1(Y, \mathcal{O}_Y) = \bigoplus_{m \ge 0} H^1(E, \mathcal{O}_E(m))$.
The term $m = 0$ is $H^1(E, \mathcal{O}_E) \cong k$, so $R^1 f_* \mathcal{O}_Y \ne 0$ and the singularity is not rational.
