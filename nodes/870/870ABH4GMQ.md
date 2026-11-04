---
tag: 870ABH4GMQ
kind: proof
name: Proof that an intersection of closed sets of a metric space is closed
msc: ["54E35"]
proves: 09YMV8H4X5
uses: [063W5JMY85, 0G5AV9Q4RR, 0839XNQXDK, 05GK32H72H, 0B1FSS1VZW, 0HEF46RPEK]
sources:
  - url: https://proofwiki.org/wiki/Intersection_of_Closed_Sets_is_Closed_in_Topological_Space
---

## Proof

1. Let $(X, d)$ be a [[metric space|063W5JMY85]], let $I$ be a nonempty set, and let $(F_i)_{i \in I}$ be a family of [[closed subsets|0G5AV9Q4RR]] of $X$.
2. Put $F = \bigcap_{i \in I} F_i$, the [[intersection|0839XNQXDK]] of the family.
3. We claim that $X \setminus F = \bigcup_{i \in I} (X \setminus F_i)$, a [[union|05GK32H72H]] of [[complements|0B1FSS1VZW]].
4. Let $x \in X$. Then $x \notin F$ if and only if $x \notin F_j$ for some $j \in I$.
5. This holds if and only if $x \in X \setminus F_j$ for some $j \in I$, that is, $x \in \bigcup_{i \in I} (X \setminus F_i)$. This proves the claim.
6. Each $F_i$ is closed, so each $X \setminus F_i$ is open, by the definition of a closed set.
7. By [[union of open sets is open|0HEF46RPEK]], the set $\bigcup_{i \in I} (X \setminus F_i)$ is open. By step 3, $X \setminus F$ is open.
8. By the definition of a closed set, $F$ is closed in $X$.

## Idea

Complements turn intersections into unions. A union of open sets is open, so the complement of the intersection is open. That is what it means for the intersection to be closed.
