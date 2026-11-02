---
tag: JTXSC68JZE
kind: definition
name: Lie subgroup
msc: ["22E15", "22E60"]
defines: NM8XCPS1Q3
uses: [7JBRGCVJRB, 0X1JXT47GA, 6RW68JGBHC, VKFW27WXEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]].
A *Lie subgroup* of $G$ is a [[subgroup|0X1JXT47GA]] $H$ of $G$ together with a topology and a smooth structure on $H$ such that:

1. $H$ with this structure is a Lie group;
2. the inclusion map $H \to G$ is an [[immersion|6RW68JGBHC]].

If moreover the inclusion is a homeomorphism onto $H$ with the subspace topology, then $H$ is an *embedded Lie subgroup*.
Equivalently, $H$ is an embedded [[submanifold|VKFW27WXEZ]] of $G$.

## Remarks

Example: in the torus $T = S^1 \times S^1$, let $\alpha$ be irrational and $H = \set{(e^{it}, e^{i\alpha t}) : t \in \R}$, with the topology and smooth structure of $\R$ transported by $t \mapsto (e^{it}, e^{i\alpha t})$.
This map is an injective homomorphism, since $\alpha$ is irrational, and its derivative $(i e^{it}, i\alpha e^{i\alpha t})$ never vanishes, so it is an immersion.
So $H$ is a Lie subgroup, but not an embedded one: $H$ is dense in $T$.

Non-example: the circle $C = \set{z \in \C : \abs{z} = 2}$ is an embedded submanifold of the Lie group $\C^\times$, but it is not a subgroup, since $2 \cdot 2 = 4 \notin C$.

Some authors use "Lie subgroup" only for embedded Lie subgroups, and call the general ones immersed or virtual Lie subgroups.
An embedded Lie subgroup is always closed in $G$.
