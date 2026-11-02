---
tag: QD9H1WHHSW
kind: definition
name: Preservation of limits
msc: [18A35]
defines: H4MY8JN8W4
uses: [28NQ0KRHD3, HJK75HDWFE, 7TPBQPPN97, CHS5AFJGWE]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_(category_theory)
---

## Definition

Let $G \colon \mathcal{C} \to \mathcal{D}$ be a [[functor|28NQ0KRHD3]], and let $F \colon J \to \mathcal{C}$ be a [[diagram|HJK75HDWFE]].
For a [[cone|7TPBQPPN97]] $(L, (\lambda_j)_{j \in J})$ over $F$, the image $(G L, (G \lambda_j)_{j \in J})$ is a cone over $G \circ F$.
$G$ *preserves the limit* of $F$ if for every [[limit|CHS5AFJGWE]] cone $(L, \lambda)$ of $F$, the cone $(G L, G \lambda)$ is a limit cone of $G \circ F$.
$G$ *preserves limits* if it preserves the limit of every diagram $F \colon J \to \mathcal{C}$ with $J$ a small category.

## Remarks

A functor that preserves limits is also called *continuous*.
Dually, $G$ preserves colimits if it sends colimit cones to colimit cones.
Since limits are unique up to isomorphism, it suffices to check one limit cone of each diagram.

Example: the forgetful functor $U$ from groups to sets preserves products.
The product of groups $H \times K$ has underlying set $U H \times U K$, and the projections are the projections of sets.

Non-example: the functor $X \mapsto X \sqcup \set{*}$ from sets to sets does not preserve the terminal object.
The terminal object is a one-point set, which is the limit of the empty diagram, and its image has two points.

A related notion goes the other way.
$G$ *reflects* limits if every cone over $F$ whose image under $G$ is a limit cone is itself a limit cone.
