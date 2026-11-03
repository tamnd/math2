---
tag: ZZX81RS79S
kind: definition
name: Critical path method
msc: [90B35, 90C35]
defines: NV50C8A51N
uses: [0SXHBTNM9T, 03NAMV1DHJ, HMK2MT9FYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Critical_path_method
---

## Definition

A *project* is a finite set $A$ of activities with a duration $d_a \ge 0$ for each $a \in A$.
Its precedence relation is given by an [[acyclic directed graph|0SXHBTNM9T]] on $A$.
An edge $p \to a$ means that $a$ cannot start before $p$ ends.
Processing the activities in a [[topological order|HMK2MT9FYZ]], the *critical path method* computes:

1. The *earliest start* $\mathrm{ES}(a)$, equal to $0$ if $a$ has no predecessor, and otherwise to the largest $\mathrm{ES}(p) + d_p$ over predecessors $p$ of $a$.
2. The *project duration* $D$, the largest $\mathrm{ES}(a) + d_a$ over all $a \in A$.
3. The *latest finish* $\mathrm{LF}(a)$, equal to $D$ if $a$ has no successor, and otherwise to the smallest $\mathrm{LF}(q) - d_q$ over successors $q$ of $a$.
4. The *slack* $\mathrm{LF}(a) - d_a - \mathrm{ES}(a) \ge 0$ of each activity.

An activity is *critical* if its slack is $0$.
A *critical path* is a directed [[path|03NAMV1DHJ]] of the graph whose total duration is $D$.

## Remarks

$D$ is the largest total duration of a directed path, so a critical path is a longest path in the graph.
Longest paths are easy here because the graph has no directed cycle.
Every activity on a critical path is critical, and every schedule that respects the precedences takes at least $D$.
Starting each activity at its earliest start gives a schedule of length exactly $D$.

Example: activities $f$ (duration $3$), $w$ (duration $5$), $r$ (duration $2$) and $g$ (duration $4$), with edges $f \to w$ and $w \to r$.
Then $\mathrm{ES}(f) = 0$, $\mathrm{ES}(w) = 3$, $\mathrm{ES}(r) = 8$, $\mathrm{ES}(g) = 0$, and $D = 10$.
The slacks are $0$ for $f, w, r$ and $10 - 4 - 0 = 6$ for $g$, so $f \to w \to r$ is the critical path.

Non-example: if one adds the edge $r \to f$, the precedence graph has the cycle $f \to w \to r \to f$.
It is no longer acyclic, no activity of the cycle can start first, and earliest starts are not defined.

The arrows can also be drawn with activities on the edges of an event graph; both forms give the same critical path.
