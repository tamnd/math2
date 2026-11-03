---
tag: 1Z4EH2QQF0
kind: example
name: Fano plane multiplication of octonions
msc: [17A75, 17D05, "51E15"]
illustrates: [1HRMT3DSX2]
uses: [QQ8GW1ASZM, 1HRMT3DSX2]
sources:
  - url: https://en.wikipedia.org/wiki/Fano_plane
---

## Example

The [[octonions|1HRMT3DSX2]] $\mathbb O$ have a real basis $1, e_1, \dots, e_7$.
The products of the units $e_i$ are encoded by the [[Fano plane|QQ8GW1ASZM]].
Its points are $1, \dots, 7$ and its $7$ lines are
$$\set{i, i + 1, i + 3}, \quad i = 1, \dots, 7,$$
where indices are taken modulo $7$ in $\set{1, \dots, 7}$.
Each line is given the cyclic order $(i, i + 1, i + 3)$.
The multiplication rules are:

1. $e_i^2 = -1$ for each $i$.
2. $e_i e_j = -e_j e_i$ for $i \ne j$.
3. If $(a, b, c)$ is a line in its cyclic order, then $e_a e_b = e_c$, $e_b e_c = e_a$ and $e_c e_a = e_b$.

Since every two points lie on exactly one line, rules 2 and 3 give each product $e_i e_j$ with $i \ne j$ exactly once.
The lines are $\set{1,2,4}$, $\set{2,3,5}$, $\set{3,4,6}$, $\set{4,5,7}$, $\set{5,6,1}$, $\set{6,7,2}$, $\set{7,1,3}$; every pair of points occurs in exactly one of them.

Check of non-associativity: the lines $(1,2,4)$ and $(3,4,6)$ give $(e_1 e_2) e_3 = e_4 e_3 = -e_6$.
The lines $(2,3,5)$ and $(5,6,1)$ give $e_1 (e_2 e_3) = e_1 e_5 = e_6$.
So $(e_1 e_2) e_3 = -e_1 (e_2 e_3)$.

## Remarks

Each line $\set{a, b, c}$ spans, with $1$, a subalgebra $\R \oplus \R e_a \oplus \R e_b \oplus \R e_c$ isomorphic to the quaternions, with $e_a, e_b, e_c$ in the roles of $i, j, k$.
For three distinct units not on a common line, as in the check, the products anti-associate.
Other labellings of the points are common in the literature.
Not every choice of orientations of the lines gives the octonions, so the orientation must be fixed with care.

## Explanations

### L1 human

Multiplying the seven imaginary octonion units would need a table with $49$ entries.
The Fano plane, a figure with seven points and seven lines of three points, stores the whole table.
Two units multiply to the third unit on their line, with a plus sign if one follows the arrow of the line and a minus sign otherwise.
Each line behaves like the quaternion units $i, j, k$, but units from different lines do not associate.
