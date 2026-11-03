---
tag: 5X6G3Q5CSQ
kind: definition
name: Lie supergroup
msc: [58A50, "22E99"]
defines: 9DQB442K3Y
uses: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Supergroup_(physics)
---

## Definition

A *Lie supergroup* is a real [[supermanifold|Z0SB9HQBAJ]] $G$ with three morphisms of supermanifolds
$$m \colon G \times G \to G, \qquad i \colon G \to G, \qquad e \colon \R^{0|0} \to G,$$
called multiplication, inverse and unit.
These must make the following diagrams of morphisms commute:

1. associativity: $m \circ (m \times \id) = m \circ (\id \times m)$ as morphisms $G \times G \times G \to G$;
2. unit: $m \circ (e \times \id) = \id = m \circ (\id \times e)$, after identifying $\R^{0|0} \times G$ and $G \times \R^{0|0}$ with $G$;
3. inverse: $m \circ (i \times \id) \circ \Delta = e \circ \pi = m \circ (\id \times i) \circ \Delta$, where $\Delta \colon G \to G \times G$ is the diagonal and $\pi \colon G \to \R^{0|0}$ is the unique morphism to the point.

## Remarks

Example: on $\R^{1|1}$, with even coordinate $t$ and odd coordinate $\theta$, define $m$ by $(t, \theta)(t', \theta') = (t + t' + \theta\theta', \theta + \theta')$, inverse $(t, \theta) \mapsto (-t, -\theta)$ and unit $(0, 0)$.
Associativity holds since both bracketings give $(t + t' + t'' + \theta\theta' + \theta\theta'' + \theta'\theta'', \theta + \theta' + \theta'')$.
The inverse works since $(t, \theta)(-t, -\theta) = (-\theta\theta, 0) = (0, 0)$, as $\theta^2 = 0$.

Non-example: on $\R^{1|1}$ the law $(t, \theta)(t', \theta') = (tt', \theta + \theta')$ is associative with unit $(1, 0)$.
But it has no inverse morphism: on underlying points it is multiplication of real numbers, and $0$ has no inverse.

The underlying manifold of a Lie supergroup is an ordinary [[Lie group|7JBRGCVJRB]].
The left-invariant vector fields on $G$ form a [[Lie superalgebra|7CZ4Q5H78N]], the Lie superalgebra of $G$.
Ordinary Lie groups are the Lie supergroups with no odd coordinates.
