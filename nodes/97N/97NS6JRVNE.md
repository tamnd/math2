---
tag: 97NS6JRVNE
kind: definition
name: Final topology
msc: [54A10, 54B15]
defines: 6ERJRRZK32
uses: [0CQHFPGJ45, 0VGFHTM75Y, 01AHG4G9RT, 02BH3MCBQB, 072J68M6HX]
sources:
  - url: https://en.wikipedia.org/wiki/Final_topology
---

## Definition

Let $Y$ be a set, let $I$ be a set, and for each $i \in I$ let $X_i$ be a [[topological space|0CQHFPGJ45]] and $f_i \colon X_i \to Y$ a map.
The *final topology* on $Y$ for the family $(f_i)_{i \in I}$ is the set of all $U \subseteq Y$ with the following property.
For every $i \in I$, the [[preimage|01AHG4G9RT]] $f_i^{-1}(U)$ is [[open|02BH3MCBQB]] in $X_i$.

## Remarks

This family of sets is a topology, because preimages commute with unions and intersections.
It is the [[finest|072J68M6HX]] topology on $Y$ for which every $f_i$ is [[continuous|0VGFHTM75Y]].
Universal property: for a topological space $Z$, a map $g \colon Y \to Z$ is continuous for the final topology if and only if $g \circ f_i$ is continuous for every $i$.

Example: for a surjection $q \colon X \to Y$ from a space $X$, the final topology for $q$ is the [[quotient topology|0NQ1H2X495]].
Example: for the injections of the pieces into a disjoint union, the final topology is the [[disjoint union topology|ZXJKSB30WF]].

Non-example: let $q \colon \R \to \R$ be the identity, with the usual topology on the source.
The trivial topology $\set{\varnothing, \R}$ on the target makes $q$ continuous but is not the final topology.
The set $(0, 1)$ has an open preimage, yet it is not open in the trivial topology.

The final topology is also called the strong topology or the coinduced topology for the family.
