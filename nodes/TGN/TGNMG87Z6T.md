---
tag: TGNMG87Z6T
kind: definition
name: Join-prime element
msc: [06B05]
defines: 9H61HXXJ11
uses: [WH4SFAACAS, J2T75ATRV5, 0AANKKNHS4, ZHRQ0AT8PM, 0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_element
---

## Definition

Let $(L, \vee, \wedge)$ be a [[lattice|WH4SFAACAS]] with order $\le$.
An element $a \in L$ is *join-prime* if:

1. $a$ is not a [[least element|0AANKKNHS4]] of $L$;
2. for all $b, c \in L$, if $a \le b \vee c$, then $a \le b$ or $a \le c$.

## Remarks

Every join-prime element is [[join-irreducible|ZHRQ0AT8PM]]: if $a = b \vee c$, then $a \le b$ or $a \le c$, and since $b, c \le a$ this gives $a = b$ or $a = c$.
In a [[distributive lattice|0HM0HQCK6N]] the converse holds: if $a$ is join-irreducible and $a \le b \vee c$, then $a = a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$, so $a = a \wedge b$ or $a = a \wedge c$.
Example: in the power set of a set, a singleton $\set{x}$ is join-prime, since $x \in B \cup C$ implies $x \in B$ or $x \in C$.
Non-example: in the diamond lattice $M_3 = \set{0, a, b, c, 1}$, where $a$, $b$, $c$ are pairwise incomparable and the join of any two of them is $1$, the element $a$ is join-irreducible.
It is not join-prime, because $a \le b \vee c = 1$ while $a \not\le b$ and $a \not\le c$.
Meet-prime elements are defined dually.
