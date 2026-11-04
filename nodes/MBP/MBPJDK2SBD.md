---
tag: MBPJDK2SBD
kind: proof
name: Proof that metrizable spaces are normal by distance functions
msc: ["54E35"]
proves: 0AD0BZ49DW
uses: [0AJ646N339, 09KDHB82SG, 07TXYYVYZR, 0A6YRNZB2R, 0G5AV9Q4RR, 0DC3MPR7C9, 01M6CW9VM6, 063W5JMY85, 04KFTA34C5]
sources:
  - url: https://proofwiki.org/wiki/Metric_Space_is_T4
---

## Proof

We separate the two closed sets by comparing the distances to them.

1. Since $X$ is [[metrizable|09KDHB82SG]], choose a [[metric|063W5JMY85]] $d$ on $X$ whose [[metric topology|0A6YRNZB2R]] is the topology of $X$. Let $A, B \subseteq X$ be disjoint [[closed sets|0G5AV9Q4RR]].
2. If $A = \varnothing$, take $U = \varnothing$ and $V = X$. If $B = \varnothing$, take $U = X$ and $V = \varnothing$. From now on let $A$ and $B$ be nonempty.
3. For nonempty $C \subseteq X$, write $d(x, C)$ for the [[distance from x to C|07TXYYVYZR]]. The metric axioms give $d \ge 0$, so $d(x, C) \ge 0$.
4. Claim: $d(y, C) \le d(y, x) + d(x, C)$ for all $x, y \in X$. For each $c \in C$, the [[triangle inequality|01M6CW9VM6]] gives $d(y, C) \le d(y, c) \le d(y, x) + d(x, c)$.
5. So $d(y, C) - d(y, x)$ is a lower bound of $\set{d(x, c) : c \in C}$. By the definition of the [[infimum|04KFTA34C5]], it is at most $d(x, C)$. This proves the claim.
6. Claim: if $C$ is closed and $x \notin C$, then $d(x, C) > 0$. The set $X \setminus C$ is open and contains $x$, so some [[open ball|0DC3MPR7C9]] $B(x, r)$ with $r > 0$ misses $C$.
7. Then $d(x, c) \ge r$ for each $c \in C$, so $d(x, C) \ge r > 0$.
8. Let $U = \set{x : d(x, A) < d(x, B)}$ and $V = \set{x : d(x, B) < d(x, A)}$. No point satisfies both inequalities, so $U \cap V = \varnothing$.
9. Let $a \in A$. Then $d(a, A) = 0$, since $d(a, a) = 0$. Since $a \notin B$ and $B$ is closed, step 6 gives $d(a, B) > 0$. So $a \in U$, and $A \subseteq U$.
10. In the same way, $B \subseteq V$.
11. We show that $U$ is open. Let $x \in U$ and $\eta = d(x, B) - d(x, A) > 0$. Let $y \in B(x, \eta / 2)$.
12. By step 4, $d(y, A) \le d(x, A) + d(x, y)$. Also by step 4, $d(x, B) \le d(x, y) + d(y, B)$, so $d(y, B) \ge d(x, B) - d(x, y)$.
13. Subtracting, $d(y, B) - d(y, A) \ge \eta - 2 d(x, y) > 0$. So $y \in U$.
14. Thus $B(x, \eta / 2) \subseteq U$ for each $x \in U$, and $U$ is open in the metric topology. In the same way, $V$ is open.
15. So $U$ and $V$ are disjoint open sets with $A \subseteq U$ and $B \subseteq V$. Hence $X$ is [[normal|0AJ646N339]].

## Idea

Put each point on the side of the closed set it is nearer to. Points of $A$ are at distance $0$ from $A$ and at a positive distance from the closed set $B$, so they land on the side of $A$. Distances to a set change by at most the distance moved, so a strict inequality survives small moves, and both sides are open.
