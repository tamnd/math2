---
tag: YT45QJKPNK
kind: definition
name: Product order
msc: [06A06]
defines: K0AWJK6NZH
uses: [0QV2JS9RJ3, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Product_order
---

## Definition

Let $I$ be a set and let $(P_i, \le_i)$ be a [[partially ordered set|0QV2JS9RJ3]] for each $i \in I$.
The *product order* on the [[Cartesian product|09CEDJYBKP]] $\prod_{i \in I} P_i$ is the relation $\le$ given by
$$x \le y \iff x_i \le_i y_i \text{ for all } i \in I.$$

## Remarks

It is a partial order: reflexivity, antisymmetry and transitivity hold in each coordinate, hence for tuples.
For two factors, $(a, b) \le (a', b')$ means $a \le a'$ and $b \le b'$.
Example: in $\N \times \N$, $(1, 2) \le (3, 2)$, since $1 \le 3$ and $2 \le 2$.
Non-example: $(1, 2)$ and $(2, 1)$ are incomparable, since the first coordinate rises and the second falls.
For finitely many factors, the product order is contained in the lexicographic order on the same set, which is total when all factors are total.
The power set of a set $I$, ordered by inclusion, is isomorphic to the product order on $\set{0, 1}^I$.
