---
tag: F0XAMM2PPS
kind: example
name: Prüfer group
msc: [20K10]
instance_of: [ZXVBEPMTCN]
sources:
  - url: https://en.wikipedia.org/wiki/Prüfer_group
same_as:
  wikidata: Q2281199
  wikipedia: Prüfer group
---

## Example

Let $p$ be a [[prime|01826KMG2H]].
The *Prüfer $p$-group* is
$$\Z(p^\infty) = \Z[1/p] / \Z = \set{m/p^k + \Z : m \in \Z, \ k \ge 0},$$
a subgroup of $\Q/\Z$.
Equivalently, it is the group of all complex [[roots of unity|0S61N75H45]] of order a power of $p$, a subgroup of the [[circle group|04EAFVFTF7]].

It is a [[divisible group|ZXVBEPMTCN]].
Let $x = m/p^k + \Z$ and $n \ge 1$, and write $n = p^j r$ with $p \nmid r$.
Choose an integer $s$ with $rs \equiv 1 \pmod{p^{k+j}}$, and put $y = sm/p^{k+j} + \Z$.
Then $ny = rs \, m / p^k + \Z$, and $rs \, m/p^k - m/p^k = (rs - 1) m / p^k$ is an integer, because $p^{k+j}$ divides $rs - 1$; so $ny = x$.

## Remarks

The Prüfer group is the union of the chain of cyclic groups $\Z/p\Z \subset \Z/p^2\Z \subset \cdots$, where $\Z/p^k\Z$ is identified with $\set{m/p^k + \Z}$.
Its proper subgroups are exactly these finite cyclic groups, so it is not finitely generated.
It is a [[p-group|06QYRTX9KQ]] in the sense that every element has order a power of $p$.
Together with $\Q$, the Prüfer groups are the building blocks of all divisible groups.
Its Pontryagin dual is the group of [[p-adic integers|V6TJAFZ4MD]].

## Explanations

### L1 human

Take the circle and mark the points that you reach by rotating by $1/p$ of a turn, by $1/p^2$ of a turn, and so on.
Add all their combinations.
This set of rotations is the Prüfer group.
Every rotation in it can be split into $n$ equal smaller rotations that still lie in it.
It is infinite, but each of its proper subgroups is finite.
