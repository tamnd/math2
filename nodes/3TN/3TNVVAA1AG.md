---
tag: 3TNVVAA1AG
kind: definition
name: Compact element
msc: [06B23, 06B35]
defines: 9F7TYES4KE
uses: [0QV2JS9RJ3, D9RY4667K6, 0R3H5PANRQ, D7A0ZGZT5S]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_element
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
An element $c \in P$ is *compact* if for every [[directed subset|D9RY4667K6]] $D \subseteq P$ that has a [[supremum|0R3H5PANRQ]] $\bigvee D$ in $P$ with $c \le \bigvee D$, there is $d \in D$ with $c \le d$.

## Remarks

In a [[complete lattice|D7A0ZGZT5S]] $L$, an element $c$ is compact if and only if for every $S \subseteq L$ with $c \le \bigvee S$ there is a finite $F \subseteq S$ with $c \le \bigvee F$.
Compact elements are also called finite elements, and in domain theory $c$ is compact exactly when $c \ll c$ for the way-below relation.
Example: in the power set of a set $X$, a finite set $c$ is compact.
If $c \subseteq \bigcup_{d \in D} d$ for a directed family $D$, each of the finitely many points of $c$ lies in some member of $D$.
Directedness then gives one member containing all of them.
Non-example: in the power set of $\N$, the set $\N$ is not compact.
It is the union of the directed family of sets $\set{0, \ldots, n}$ and lies in none of them.
The least element, when it exists, is always compact.
