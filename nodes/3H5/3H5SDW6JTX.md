---
tag: 3H5SDW6JTX
kind: definition
name: Co-Heyting algebra
msc: ["06D20", "03G10"]
defines: 6G03V0BVZT
uses: [72V1Z82M5F, NG943XNQWH]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
---

## Definition

Let $(L, \vee, \wedge, 0, 1)$ be a [[bounded lattice|72V1Z82M5F]] with order $\le$.
A *co-Heyting algebra* structure on $L$ is a binary operation $\setminus$ on $L$ such that for all $a, b, c \in L$,
$$a \setminus b \le c \iff a \le b \vee c.$$
So $a \setminus b$ is the least element $c$ with $a \le b \vee c$.
A *co-Heyting algebra* is a bounded lattice with such an operation.

## Remarks

The operation is unique when it exists, since it is a least element.
A bounded lattice is a co-Heyting algebra if and only if its order dual is a [[Heyting algebra|NG943XNQWH]].
The element $\neg a = 1 \setminus a$ is called the supplement of $a$; it is the least $c$ with $a \vee c = 1$.

Example: let $X$ be a topological space and $L$ its family of closed sets, ordered by inclusion.
For closed $A, B$, put $A \setminus B = \overline{A - B}$, the closure of the set difference.
If $A \subseteq B \cup C$ with $C$ closed, then $A - B \subseteq C$, so $\overline{A - B} \subseteq C$.
If $\overline{A - B} \subseteq C$, then $A \subseteq B \cup (A - B) \subseteq B \cup C$.
So the defining equivalence holds.

Non-example: the diamond lattice $M_3$, with atoms $p, q, r$, is bounded but has no such operation.
Every co-Heyting algebra is distributive, and $M_3$ is not, since $p \vee (q \wedge r) = p$ while $(p \vee q) \wedge (p \vee r) = 1$.
Directly: the elements $c$ with $1 \le p \vee c$ are $q$, $r$ and $1$, and they have no least one.

In Mathlib the notion is `CoheytingAlgebra`, with difference `\` and supplement `￢`.
