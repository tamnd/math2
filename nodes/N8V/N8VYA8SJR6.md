---
tag: N8VYA8SJR6
kind: definition
name: Paradoxical decomposition
msc: ["43A07", "03E25", "20F65"]
defines: XRCN826T16
uses: [G5S1M9, 0WCY42EV9V]
sources:
  - url: https://en.wikipedia.org/wiki/Paradoxical_set
---

## Definition

Let $G$ be a [[group|G5S1M9]] acting on a set $X$ by a [[group action|0WCY42EV9V]], and let $E \subseteq X$.
A *paradoxical decomposition* of $E$ consists of:

1. pairwise disjoint subsets $A_1, \ldots, A_n, B_1, \ldots, B_m$ of $E$;
2. elements $g_1, \ldots, g_n$ and $h_1, \ldots, h_m$ of $G$;

such that
$$E = \bigcup_{i=1}^{n} g_i A_i = \bigcup_{j=1}^{m} h_j B_j.$$
The set $E$ is *$G$-paradoxical* if it has a paradoxical decomposition.
A group $G$ is *paradoxical* if it is $G$-paradoxical for its action on itself by left multiplication.

## Remarks

Example: let $G = X = F_2$, the free group on $a, b$, acting by left multiplication.
Let $W(x)$ be the set of reduced words that begin with the letter $x$.
The four sets $W(a), W(a^{-1}), W(b), W(b^{-1})$ are pairwise disjoint.
A reduced word $w$ not in $W(a)$ gives the reduced word $a^{-1} w \in W(a^{-1})$, so $F_2 = W(a) \cup a W(a^{-1})$, and likewise $F_2 = W(b) \cup b W(b^{-1})$.
So $F_2$ is paradoxical, with $n = m = 2$.

Non-example: a finite nonempty set $E$ is never paradoxical, for any action.
The pieces satisfy $\abs{E} \le \sum_i \abs{A_i}$ and $\abs{E} \le \sum_j \abs{B_j}$, so $2\abs{E} \le \sum_i \abs{A_i} + \sum_j \abs{B_j} \le \abs{E}$, which forces $E = \emptyset$.

In the definition one can ask the pieces $g_i A_i$ to be pairwise disjoint too, and likewise the $h_j B_j$; this gives the same notion.
