---
tag: JQ6FJH2TP8
kind: example
name: Diamond lattice M3
msc: [06C05, 06D05]
instance_of: [QX7WZ92QAK]
not_instance_of:
  - target: 0HM0HQCK6N
    note: meet does not distribute over join for the three middle elements
uses: [WH4SFAACAS, QX7WZ92QAK, 0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Distributive_lattice
---

## Example

The *diamond lattice* $M_3$ has five elements $0, a, b, c, 1$.
Its order is $0 < a < 1$, $0 < b < 1$ and $0 < c < 1$, with $a$, $b$, $c$ pairwise incomparable.
The join of any two distinct elements among $a, b, c$ is $1$ and their meet is $0$, so $M_3$ is a [[lattice|WH4SFAACAS]].

$M_3$ is a [[modular lattice|QX7WZ92QAK]].
If $u \le v$ and $u = v$, or $u = 0$, or $v = 1$, the modular law $u \vee (x \wedge v) = (u \vee x) \wedge v$ reduces to a trivial identity; these cases cover all comparable pairs.
For example, with $u = 0$ both sides equal $x \wedge v$, and with $v = 1$ both sides equal $u \vee x$.

$M_3$ is not a [[distributive lattice|0HM0HQCK6N]].
Indeed $a \wedge (b \vee c) = a \wedge 1 = a$, while $(a \wedge b) \vee (a \wedge c) = 0 \vee 0 = 0$.

## Remarks

$M_3$ is isomorphic to the lattice of subspaces of the plane $\F_2^2$ over the field with two elements: the zero subspace, the three lines and the whole plane.
By the [[M3–N5 characterization of distributivity|C6GH4VHAMQ]], a lattice is distributive exactly when it has no sublattice isomorphic to $M_3$ or to the [[pentagon lattice N5|DHC8TZXGYS]].

## Explanations

### L1 human

Draw a diamond with an extra middle point: a bottom, a top and three points side by side in between.
Each middle point meets each other one at the bottom and joins it at the top.
So $a$ meets "$b$ or $c$" in $a$ itself, but $a$ meets $b$ and meets $c$ only in the bottom.
This is the simplest place where meet does not distribute over join, although the weaker modular law still holds.
