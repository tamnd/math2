---
tag: 3D6JFMJGTK
kind: statement
role: theorem
name: Debreu's representation theorem
msc: [91B16, 91B08, 54F05]
uses: [JGP0Q56FRY, GZZS4MTDG9, 0CQHFPGJ45, 0Z2P41SVDP, 0V032VWTHD, 0VGFHTM75Y]
about: [GZZS4MTDG9]
sources:
  - url: https://en.wikipedia.org/wiki/Debreu%27s_representation_theorems
same_as:
  wikidata: Q22907698
  wikipedia: Debreu's representation theorems
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $\succsim$ be a [[preference relation|JGP0Q56FRY]] on $X$.
Assume that $\succsim$ is continuous: for every $x \in X$, the sets $\set{y \in X : y \succsim x}$ and $\set{y \in X : x \succsim y}$ are closed in $X$.
Assume also that $X$ has a countable base, or that $X$ is [[connected|0V032VWTHD]] and [[separable|0Z2P41SVDP]].
Then there is a [[continuous|0VGFHTM75Y]] [[utility function|GZZS4MTDG9]] $u \colon X \to \R$ for $\succsim$, that is, $x \succsim y \iff u(x) \ge u(y)$ for all $x, y \in X$.

## Remarks

In the connected and separable case, take a countable dense set $D$ and build a utility on $D$ as for countable sets.
Connectedness ensures that the order has no gaps, so this utility extends continuously.
In the case of a countable base, one first builds some utility $v$ and then corrects its gaps with Debreu's gap lemma, which gives an increasing $g$ with $g \circ v$ continuous.
For example, every continuous preference on a convex subset of $\R^n$ has a continuous utility, since such a set is connected and separable.
Continuity cannot be dropped: the lexicographic order on $\R^2$ is complete and transitive but not continuous, and it has no utility function at all.
The theorem is the main reason that consumer theory can work with continuous utility functions instead of preference relations.

## Explanations

### L1 human

If a person's tastes change smoothly, with no sudden jumps, then their tastes can be described by a continuous score.
Debreu's theorem makes this precise for a wide class of spaces of alternatives, including all convex sets of bundles of goods.

### L2 human

The theorem is the bridge between the axioms on preferences and the calculus methods of consumer theory.
Once a continuous utility exists, the Weierstrass extreme value theorem gives optimal choices on compact budget sets.
The separable and connected hypotheses together play the role that the countability of a domain plays in the elementary representation theorem for countable sets.
