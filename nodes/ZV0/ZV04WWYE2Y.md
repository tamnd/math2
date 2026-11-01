---
tag: ZV04WWYE2Y
kind: definition
name: Artinian ring
msc: ["13E10", "16P20"]
defines: 20QEAM8AX2
uses: [0GYGHKX834, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Artinian_ring
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
The ring $R$ is *Artinian* if the set of its [[ideals|0MYSA6MYNA]], ordered by inclusion, satisfies the descending chain condition.
That is, for every chain $I_1 \supseteq I_2 \supseteq \cdots$ of ideals of $R$, there is an index $k$ with $I_n = I_k$ for all $n \ge k$.

## Remarks

Example: $\Z/n\Z$ for $n \ge 1$ is Artinian, because it has only finitely many ideals, so a decreasing chain takes only finitely many values.
Example: $k[x]/(x^2)$ over a field $k$ is Artinian, because every ideal is a $k$-subspace of a $2$-dimensional space.
Non-example: $\Z$ is not Artinian, because $(2) \supsetneq (4) \supsetneq (8) \supsetneq \cdots$ never stops.
Equivalently, $R$ is Artinian when it is an [[Artinian module|YQNZTQGP1X]] over itself, or when every nonempty set of ideals has a minimal element.
For a noncommutative ring one defines left Artinian and right Artinian rings with left and right ideals.

## Explanations

### L1 human

An Artinian ring is a ring with no endless decreasing chain of ideals.
Fields and finite rings are the simplest examples.
