---
tag: ECB3W5EVK3
kind: definition
name: Quantale
msc: ["06F07"]
defines: DA619M38C3
uses: [D7A0ZGZT5S, 0V3CFG1KK9, 0GYGHKX834, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Quantale
---

## Definition

Let $Q$ be a [[complete lattice|D7A0ZGZT5S]], with join $\bigvee$ of arbitrary subsets.
Let $\cdot$ be a binary operation on $Q$ such that $(Q, \cdot)$ is a [[semigroup|0V3CFG1KK9]].
The structure $(Q, \cdot)$ is a *quantale* if for every $a \in Q$ and every family $(b_i)_{i \in I}$ of elements of $Q$,
$$a \cdot \bigvee_{i \in I} b_i = \bigvee_{i \in I} (a \cdot b_i) \quad \text{and} \quad \Big(\bigvee_{i \in I} b_i\Big) \cdot a = \bigvee_{i \in I} (b_i \cdot a).$$
The index set $I$ may be empty.

## Remarks

Example: the [[ideals|0MYSA6MYNA]] of a [[commutative ring|0GYGHKX834]] $R$, ordered by inclusion, with the product of ideals, form a quantale.
The join of a family of ideals is their sum, and $J \sum_i K_i = \sum_i J K_i$ because the product of ideals distributes over sums.
Example: a complete lattice in which $\wedge$ distributes over arbitrary joins is a quantale with $a \cdot b = a \wedge b$; these are the frames.
Non-example: on the two-element lattice $\set{0, 1}$, let $a \cdot b = 1$ for all $a, b$.
This is associative, but for the empty family $a \cdot \bigvee \emptyset = a \cdot 0 = 1 \ne 0 = \bigvee \emptyset$, so distributivity fails.
The case $I = \emptyset$ says that $a \cdot 0 = 0 \cdot a = 0$, where $0$ is the least element.
A quantale is *unital* if the semigroup has an identity element, and *commutative* if the multiplication is commutative.
