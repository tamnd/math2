---
tag: WEGEXJBX26
kind: definition
name: Fundamental domain
msc: ["22F10", "28C10", "22E40"]
defines: KNJA2NEZ9F
uses: [0WCY42EV9V, P15VQS5DJ9, 556WBDAHNP, 01TQB88H4C, 0YQPZB5Q1G]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_domain
---

## Definition

Let $(X, \mathcal{A}, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $G$ be a [[countable|01TQB88H4C]] group that [[acts|0WCY42EV9V]] on $X$ by [[measure-preserving|556WBDAHNP]] measurable maps $x \mapsto gx$.
A measurable set $F \subseteq X$ is a *fundamental domain* for this action if:

1. the translates cover almost all of $X$: $\mu\big(X \setminus \bigcup_{g \in G} gF\big) = 0$;
2. distinct translates are almost disjoint: $\mu(gF \cap hF) = 0$ for all $g, h \in G$ with $g \ne h$.

## Remarks

Example: $G = \Z$ acting on $X = \R$ with Lebesgue measure by $n \cdot x = x + n$, and $F = [0, 1)$.
The translates $F + n = [n, n+1)$ cover $\R$ and are pairwise disjoint, so both clauses hold.

Non-example: for the same action, $F = [0, 2)$ covers $\R$ but fails clause 2, since $F \cap (F + 1) = [1, 2)$ has measure $1$.

Without a measure, a *strict fundamental domain* is a set that meets each [[orbit|0YQPZB5Q1G]] in exactly one point.
In geometry one often asks instead for a closed region $D$ whose translates cover $X$ and whose interiors are pairwise disjoint.
Any two measurable fundamental domains of the same action have the same measure.
