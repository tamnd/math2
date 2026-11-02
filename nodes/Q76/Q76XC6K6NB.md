---
tag: Q76XC6K6NB
kind: definition
name: Modular lattice
msc: [06C05, 06B05]
defines: QX7WZ92QAK
uses: [WH4SFAACAS, J2T75ATRV5]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_lattice
---

## Definition

Let $(L, \vee, \wedge)$ be a [[lattice|WH4SFAACAS]] with [[join and meet|J2T75ATRV5]] $\vee$ and $\wedge$ and order $\le$.
The lattice $L$ is *modular* if for all $a, b, x \in L$ with $a \le b$,
$$a \vee (x \wedge b) = (a \vee x) \wedge b.$$

## Remarks

The inequality $a \vee (x \wedge b) \le (a \vee x) \wedge b$ holds in every lattice when $a \le b$, so only the reverse inequality is a condition.
Equivalently, $L$ satisfies the identity $((a \wedge b) \vee x) \wedge b = (a \wedge b) \vee (x \wedge b)$ for all $a, b, x \in L$, so the modular lattices form a variety.

Example: the lattice of subspaces of a vector space $V$ is modular.
If $A \subseteq B$ and $X$ are subspaces, and $b = a + x \in (A + X) \cap B$ with $a \in A$, $x \in X$, then $x = b - a \in B$, so $b \in A + (X \cap B)$.

Non-example: the [[pentagon lattice N5|DHC8TZXGYS]] with $0 < a < c < 1$ and $b$ incomparable to $a$ and $c$.
Here $a \le c$, but $a \vee (b \wedge c) = a \vee 0 = a$ while $(a \vee b) \wedge c = 1 \wedge c = c$.

Every [[distributive lattice|0HM0HQCK6N]] is modular.
The [[diamond lattice M3|JQ6FJH2TP8]] is modular but not distributive.
