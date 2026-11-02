---
tag: APGRBE5DW9
kind: statement
role: theorem
name: Jean Taylor's theorem on soap film singularities
msc: [49Q05, 49Q20, 53A10]
uses: [381RB634WS, Q1TGZK8RN6, 012PBA0FMD, JFX8ASQS3E]
about: [381RB634WS]
sources:
  - url: https://en.wikipedia.org/wiki/Plateau%27s_laws
---

## Statement

Let $S \subseteq \R^3$ be a closed set such that $\mathcal{H}^2(S \cap K) < \infty$ for every compact set $K$, where $\mathcal{H}^2$ is the $2$-dimensional [[Hausdorff measure|Q1TGZK8RN6]].
Let $\delta > 0$, $C > 0$ and $\alpha > 0$.
Suppose that $S$ is almost minimizing in the sense of Almgren: for every Lipschitz map $\phi \colon \R^3 \to \R^3$, with $W = \set{x : \phi(x) \ne x}$ and $r = \operatorname{diam}(W \cup \phi(W)) < \delta$,
$$\mathcal{H}^2(S \cap W) \le (1 + C r^\alpha) \, \mathcal{H}^2(\phi(S \cap W)).$$
Then every point of $S$ has a neighbourhood $U$ with the following property.
The set $S \cap U$ is the image, under a $C^{1,\beta}$ diffeomorphism with $\beta > 0$, of an open piece of one of these three cones:

1. a plane;
2. the cone $Y$: three closed half-planes with a common boundary line, meeting along it at angles of $120^\circ$;
3. the cone $T$ over the six edges of a regular [[tetrahedron|JFX8ASQS3E]] centred at the origin, whose six sectors meet in threes along four rays.

## Remarks

Jean Taylor proved the theorem in 1976, using the regularity theory of Almgren.
The main step is to classify the minimizing cones.
A tangent cone of $S$ at a point is a cone over a network of arcs of great circles on the unit sphere.
The minimizing condition leaves only the three cones above.
Then an epiperimetric inequality shows that $S$ approaches its tangent cone at a rate that is a power of the radius, which gives the $C^{1,\beta}$ parametrization.
Soap films and clusters of soap bubbles are modelled by such almost-minimizing sets, so the theorem proves [[Plateau's laws|381RB634WS]] within this model.
For example, take a soap film on a wire frame shaped like the edges of a regular tetrahedron.
It consists of six flat triangles meeting at the centre, a piece of the cone $T$.

## Explanations

### L1 human

Soap films can meet along edges and at corners, but only in a few ways.
Take any surface that cannot reduce its area by small deformations.
Taylor's theorem says that near each point it looks like a bent copy of one of three models.
The models are a plane, three sheets meeting along an edge at $120^\circ$, and the tetrahedral corner where four such edges meet.
This turns the old experimental rules of Plateau into a theorem.

### L2 human

The theorem is a model case of the classification of singularities in geometric variational problems.
Its ingredients, the tangent cone classification and the epiperimetric inequality, have since been used for other problems, such as the regularity of free boundaries.
The almost-minimizing condition is flexible: it covers films spanning wires, bubbles enclosing fixed volumes, and films with small external forces.
