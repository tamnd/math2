---
tag: GMPJ88PAQE
kind: definition
name: Automatic group
msc: [20F65, 20F10, 68Q45]
defines: J5XQRP1SNQ
uses: [G5S1M9, 0RP7VWQ0YN, VCHJVR9NGH]
sources:
  - url: https://en.wikipedia.org/wiki/Automatic_group
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $A$ be a finite [[generating set|0RP7VWQ0YN]] of $G$ closed under inverses.
For a word $w$ over $A$, write $\bar w$ for the element of $G$ it represents.
Let $\$$ be a new padding symbol.
For words $u, v$ over $A$, write $u$ and $v$ one above the other and fill the end of the shorter one with $\$$.
The result is a word over $(A \cup \set{\$})^2$, the padded pair $(u, v)^{\$}$.
An *automatic structure* on $G$ with respect to $A$ consists of finite automata $W$ over $A$ and $M_x$ over $(A \cup \set{\$})^2$ for $x \in A \cup \set{e}$, such that:

1. Every element of $G$ equals $\bar w$ for at least one word $w$ accepted by $W$.
2. For each $x \in A \cup \set{e}$ and all words $u, v$ accepted by $W$, the automaton $M_x$ accepts $(u, v)^{\$}$ if and only if $\bar u \, x = \bar v$ in $G$.

The group $G$ is *automatic* if it has an automatic structure with respect to some finite generating set.

## Remarks

Equivalently, $G$ is automatic if there is a regular language $L$ over $A$ mapping onto $G$ with the fellow traveller property.
This means there is a constant $k$ such that whenever $u, v \in L$ and $\bar u^{-1} \bar v \in A \cup \set{e}$, the prefixes $u(t)$ and $v(t)$ of length $t$ satisfy $d_A(\overline{u(t)}, \overline{v(t)}) \le k$ for all $t$, in the [[word metric|VCHJVR9NGH]].

Example: $G = \Z^2 = \langle a, b \rangle$ with $A = \set{a, a^{-1}, b, b^{-1}}$ and $L$ the set of words $a^m b^n$, $m, n \in \Z$, which is regular.
Two such words naming elements that differ by one generator differ by one in the exponent of $a$ or of $b$.
Their prefixes stay at distance at most $2$, so $L$ has the fellow traveller property.

Non-example: the integer Heisenberg group is not automatic.
It is finitely presented, but its Dehn function grows like $n^3$, while every automatic group satisfies a quadratic isoperimetric inequality.

Being automatic does not depend on the choice of the finite generating set.
