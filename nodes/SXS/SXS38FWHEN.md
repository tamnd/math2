---
tag: SXS38FWHEN
kind: definition
name: Newton polytope
msc: [14M25, 52B20, 14T10]
defines: CYTTX8KHC8
uses: [0FQSDC2EQ2, 07GNX8GCYP, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_polytope
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] and let $f = \sum_{a \in \Z^n} c_a x^a$ be a Laurent polynomial in $x_1, \dots, x_n$ over $K$, where $x^a = x_1^{a_1} \cdots x_n^{a_n}$ and only finitely many $c_a$ are nonzero.
The *support* of $f$ is $\operatorname{supp}(f) = \set{a \in \Z^n : c_a \ne 0}$.
The *Newton polytope* of $f$ is the [[convex hull|0FQSDC2EQ2]]
$$\operatorname{Newt}(f) = \operatorname{conv}(\operatorname{supp}(f)) \subseteq \R^n.$$

## Remarks

The Newton polytope is a lattice polytope: its vertices lie in $\Z^n$, and each vertex is the exponent of a monomial of $f$.
For nonzero $f, g$, one has $\operatorname{Newt}(fg) = \operatorname{Newt}(f) + \operatorname{Newt}(g)$, the Minkowski sum.

Example: for $f = 1 + x + y + xy$ the support is $\set{(0,0), (1,0), (0,1), (1,1)}$ and $\operatorname{Newt}(f)$ is the unit square.
Indeed $f = (1 + x)(1 + y)$, and the unit square is the Minkowski sum of the segments $[0,1] \times \set{0}$ and $\set{0} \times [0, 1]$.

Non-example: for $f = x^2 - (x - 1)(x + 1) = 1$, the support is $\set{0}$, not $\set{0, 1, 2}$.
The Newton polytope uses the monomials that remain after simplification, so $\operatorname{Newt}(f)$ is the single point $0$ and not the segment $[0, 2]$.

In one variable, the Newton polytope of $f$ is the segment from the lowest to the highest exponent.
