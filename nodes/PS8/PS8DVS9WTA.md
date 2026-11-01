---
tag: PS8DVS9WTA
kind: definition
name: Basic open set
msc: [14A05, 13A15]
defines: N6JX9BCKQP
uses: [FB45BHHA2J, 8SQK7RTB63, 00MHHZ9SNE, 0NA0732YAG]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_of_a_ring
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $f \in R$.
The *basic open set* (or *principal open set*) of $f$ is the subset
$$D(f) = \set{\mathfrak p \in \operatorname{Spec} R : f \notin \mathfrak p}$$
of the [[spectrum|FB45BHHA2J]] of $R$.
It is the complement of the closed set $V(\set{f})$ of the [[Zariski topology|8SQK7RTB63]], hence open.

## Remarks

The basic open sets have these properties, for $f, g \in R$:

1. $D(f) \cap D(g) = D(fg)$, since a [[prime ideal|00MHHZ9SNE]] contains $fg$ exactly when it contains $f$ or $g$;
2. each open set $X \setminus V(E)$ equals $\bigcup_{f \in E} D(f)$, so the sets $D(f)$ form a [[basis|0NA0732YAG]] of the topology;
3. $D(f) = \emptyset$ exactly when $f$ is [[nilpotent|0ZB2JG1M9C]], and $D(f) = \operatorname{Spec} R$ exactly when $f$ is a [[unit|0XVEZDE9J8]];
4. the map $\operatorname{Spec} R_f \to \operatorname{Spec} R$ induced by $R \to R_f$ is a homeomorphism onto $D(f)$; see [[prime ideals of a localization|W8QNZZ4QJS]].

Example: in $\operatorname{Spec} \Z$, the set $D(6)$ consists of $(0)$ and all $p\Z$ with $p \ne 2, 3$.

Non-example: not every open set is basic.
Let $k$ be a field and $R = k[x, y]$.
The set $U = \operatorname{Spec} R \setminus \set{(x, y)}$ is open, because $\set{(x,y)} = V(\set{x, y})$.
If $U = D(f)$, then $f \ne 0$ and $f$ is not a unit, since $U$ is neither empty nor everything.
Then an irreducible factor $g$ of $f$ generates a prime ideal $(g)$ that contains $f$, and $(g) \ne (x, y)$ because $(x,y)$ is not principal.
So $(g) \notin D(f)$ but $(g) \in U$, a contradiction.
