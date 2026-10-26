---
tag: 0ZC7FYE0NZ
kind: statement
role: proposition
name: Orbits partition the set
msc: [20B05]
uses: [00F2JFA41J, 0YSE802YCQ]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Orbits and stabilizers
---

## Statement

Let a [[group|G5S1M9]] $G$ [[act|0WCY42EV9V]] on a set $X$.
The relation $x \sim y$ if and only if $y = g \cdot x$ for some $g \in G$ is an equivalence relation on $X$.
Its equivalence classes are the [[orbits|0YQPZB5Q1G]], so each point of $X$ lies in exactly one orbit.

## Remarks

Reflexivity uses $e \cdot x = x$, symmetry uses $x = g^{-1} \cdot (g \cdot x)$, and transitivity uses $h \cdot (g \cdot x) = (hg) \cdot x$.
If $X$ is finite, then $|X|$ is the sum of the sizes of the distinct orbits.
The [[cosets|03DEH43F4H]] of a subgroup and the [[conjugacy classes|0DEBXAJ5SA]] of a group are examples of orbits.

## Explanations

### L1 human

The group action cuts the set into separate pieces, the orbits.
Inside one piece, each point can reach each other point.
No point can reach a point of another piece.
