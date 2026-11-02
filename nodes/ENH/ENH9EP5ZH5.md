---
tag: ENH9EP5ZH5
kind: definition
name: Bornological space
msc: [46A08, 46A17]
defines: 4R6SQD60FN
uses: [B6GY2KJMWW, 3BAJ8ZTVPX, 02AS45T3H9, 2TDSHJJYS4, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Bornological_space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $E$ be a [[locally convex space|B6GY2KJMWW]] over $\mathbb{K}$.
A subset $A \subseteq E$ *absorbs* a subset $B \subseteq E$ if there is $r > 0$ such that $B \subseteq cA$ for every $c \in \mathbb{K}$ with $\abs{c} \ge r$.
$E$ is *bornological* if every [[convex|02AS45T3H9]] [[balanced|2TDSHJJYS4]] subset of $E$ that absorbs every [[bounded set|3BAJ8ZTVPX]] of $E$ is a [[neighbourhood|0ZCY0Z80B6]] of $0$.

## Remarks

Equivalently, $E$ is bornological if and only if every linear map from $E$ to a locally convex space that maps bounded sets to bounded sets is continuous.
Example: every normed space $E$ is bornological.
If a convex balanced set $A$ absorbs the closed unit ball $B$, then $B \subseteq c A$ for some $c > 0$, so $A$ contains the ball of radius $1 / c$.
More generally, every metrizable locally convex space is bornological.
Non-example: let $E$ be an infinite-dimensional Banach space with its weak topology $\sigma(E, E')$.
Its weakly bounded sets are norm bounded, by the uniform boundedness principle, so the closed unit ball absorbs all of them.
But the ball is not a weak neighbourhood of $0$, since every weak neighbourhood of $0$ contains a nonzero linear subspace.
