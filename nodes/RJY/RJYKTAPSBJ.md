---
tag: RJYKTAPSBJ
kind: example
name: Dihedral quandle
msc: [57K12, 20N02]
instance_of: [X74VY86TSX]
uses: [03VFZ2WETT, 0JZ27DMJ5D, QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Racks_and_quandles
---

## Example

Let $n \ge 1$ and let $R_n = \Z/n\Z$ be the [[integers modulo $n$|03VFZ2WETT]], with
$$a \triangleright b = 2a - b.$$
Then $(R_n, \triangleright)$ is a [[quandle|X74VY86TSX]], the *dihedral quandle* of order $n$.

Check of the three axioms:

1. Self-distributivity: $a \triangleright (b \triangleright c) = 2a - 2b + c$ and $(a \triangleright b) \triangleright (a \triangleright c) = 2(2a - b) - (2a - c) = 2a - 2b + c$.
2. For fixed $a$ and $b$, the equation $a \triangleright c = b$ has the unique solution $c = 2a - b$.
3. Idempotence: $a \triangleright a = 2a - a = a$.

The name comes from the [[dihedral group|0JZ27DMJ5D]] $D_n$.
Let $s_a$ be the reflection $x \mapsto 2a - x$ of $\Z/n\Z$.
Then $s_a s_b s_a^{-1} = s_{2a - b}$, so the operation of $R_n$ is conjugation of reflections.
For odd $n$ the map $a \mapsto s_a$ is injective, and $R_n$ is the conjugacy class of reflections in $D_n$ with conjugation.

## Remarks

Colourings of a [[knot|QYEAZTYGPT]] diagram by $R_3$ are the Fox $3$-colourings: at each crossing, the three arcs carry either one colour or three different colours.
The trefoil has $9$ colourings by $R_3$, three of them constant, while the unknot has only the $3$ constant ones.
Since the number of colourings is a knot invariant, the trefoil is knotted.
In Mathlib this quandle is `Quandle.Dihedral`.

## Explanations

### L1 human

Place $n$ points evenly on a circle and reflect the circle in the line through point $a$ and the centre.
Point $b$ moves to point $2a - b$.
The dihedral quandle records exactly this rule.
These simple quandles already detect interesting knots, through the familiar game of colouring a knot diagram with three colours.
