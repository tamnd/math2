---
tag: 09GK3DE0WV
kind: definition
name: Dihedral group
msc: [20B25]
defines: 0JZ27DMJ5D
uses: [0ZG3Z5JZ85, 0RG9SPQSWM]
sources:
  - url: https://en.wikipedia.org/wiki/Dihedral_group
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Dihedral_group
    locator: Other definitions
---

## Definition

Let $n \geq 3$ be an integer.
Let $P$ be a regular $n$-gon in the plane with centre $0$.
The dihedral group $D_n$ is the group of all isometries of the plane that map $P$ onto itself, with composition as the operation.
Let $r$ be the rotation by the angle $2\pi/n$ about $0$, and let $s$ be a reflection in a line of symmetry of the polygon.

## Remarks

The elements of $D_n$ are the rotations $e, r, \dots, r^{n-1}$ and the reflections $s, rs, \dots, r^{n-1}s$.
The relations $r^n = e$, $s^2 = e$ and $srs^{-1} = r^{-1}$ hold, and these relations give a presentation of $D_n$.
In abstract algebra, many authors write $D_{2n}$ for this group, so the index is the order and not the number of sides.
The group $D_n$ is not abelian, and it is a [[semidirect product|0H3WZXCZNF]] of $\langle r \rangle$ and $\langle s \rangle$.

## Explanations

### L1 human

Take a regular polygon and look at all the ways to pick it up and put it back in the same outline.
You can turn it, and you can flip it over.
These motions form the dihedral group, and turning after a flip is not the same as flipping after a turn.
