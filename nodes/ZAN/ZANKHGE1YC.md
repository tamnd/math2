---
tag: ZANKHGE1YC
kind: definition
name: Well-founded order
msc: [06A06, "03E20"]
defines: 55WD0H03CZ
uses: [0QV2JS9RJ3, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Well-founded_relation
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]], and write $x < y$ when $x \le y$ and $x \ne y$.
The order is *well-founded* when every nonempty subset $A \subseteq P$ has a minimal element, that is, an element $m \in A$ such that no $a \in A$ satisfies $a < m$.

## Remarks

Example: the set $\N^2$ with the product order, $(a, b) \le (c, d)$ when $a \le c$ and $b \le d$, is well-founded.
Check: in a nonempty $A \subseteq \N^2$, take the least first coordinate $a_0$ occurring in $A$, and then the least $b_0$ with $(a_0, b_0) \in A$; no element of $A$ is strictly below $(a_0, b_0)$.

Non-example: the set $\set{1/n : n \ge 1}$ of rational numbers with the usual order is not well-founded, since the whole set has no minimal element.

The order is well-founded exactly when the strict order $<$ is a [[well-founded relation|0DQPNJNPYK]].
With the axiom of dependent choice, the condition is equivalent to the absence of an infinite sequence $x_0 > x_1 > x_2 > \cdots$.
The same definition applies to a preorder, with $x < y$ meaning $x \le y$ and not $y \le x$.
