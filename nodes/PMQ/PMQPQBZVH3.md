---
tag: PMQPQBZVH3
kind: example
name: Redundant parameters for a line
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
not_instance_of:
  - target: KQT68YPHD1
    note: The description covers the right set, but it has two parameters for a line, so different parameter values give the same solution
uses: [KQT68YPHD1, 0CRMGPAH83]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
---

## Example

Consider the system $x - y = 1$, $z = 0$ over $\R$ in the unknowns $x, y, z$.
Look at the description
$$S' = \set{(1, 0, 0) + s(1, 1, 0) + t(2, 2, 0) : s, t \in \R}.$$

1. Every point of $S'$ is $(1 + s + 2t, s + 2t, 0)$.
2. It solves the system: $(1 + s + 2t) - (s + 2t) = 1$ and $z = 0$.
3. Conversely, a solution has $y = u$ for some $u$, $x = 1 + u$ and $z = 0$, and it is the point of $S'$ with $s = u$, $t = 0$.
4. So $S'$ is the full solution set, a line.
5. But $(s, t) = (2, 0)$ and $(s, t) = (0, 1)$ both give the point $(3, 2, 0)$.
6. So the map $(s, t) \mapsto$ point is not injective, and $S'$ is not a [[parametric form|KQT68YPHD1]] in the sense of the row reduction.

The parametric form from the RREF has one free variable $y = t$, and it is $(1, 0, 0) + t(1, 1, 0)$.

## Remarks

The direction vectors $(1, 1, 0)$ and $(2, 2, 0)$ are not [[linearly independent|0CRMGPAH83]], because the second is twice the first.
The parametric form from row reduction always has independent direction vectors, one for each free variable.

## Explanations

### L1 human

A line needs only one parameter.
Here we used two, and the second direction is a multiple of the first.
So many pairs of parameters give the same point.

### L2 human

1. Write the points of the description in coordinates.
2. Check that they solve the system and that every solution appears.
3. Find two parameter pairs with the same point.
4. Compare with the parametric form from the RREF, which has one parameter.

The typical use is to test whether a description by parameters is the standard one.
A trap: counting parameters to find the dimension gives $2$ here, which is wrong; the dimension is the number of independent directions.
