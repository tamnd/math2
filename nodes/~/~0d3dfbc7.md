---
tag: ~0d3dfbc7
kind: statement
role: proposition
name: Orbits partition the set
msc: [20B05]
uses: [~83f43154, ~1ff21cb1]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Orbits and stabilizers
---

## Statement

Let a [[group|G5S1M9]] $G$ [[act|~0ceb002c]] on a set $X$.
The relation $x \sim y$ if and only if $y = g \cdot x$ for some $g \in G$ is an equivalence relation on $X$.
Its equivalence classes are the [[orbits|~401e0177]], so each point of $X$ lies in exactly one orbit.

## Remarks

Reflexivity uses $e \cdot x = x$, symmetry uses $x = g^{-1} \cdot (g \cdot x)$, and transitivity uses $h \cdot (g \cdot x) = (hg) \cdot x$.
If $X$ is finite, then $|X|$ is the sum of the sizes of the distinct orbits.
The [[cosets|~9c4c9f74]] of a subgroup and the [[conjugacy classes|~a445ebec]] of a group are examples of orbits.

## Explanations

### L1 human

The group action cuts the set into separate pieces, the orbits.
Inside one piece, each point can reach each other point.
No point can reach a point of another piece.
