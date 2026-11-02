---
tag: WXNCE8W5Q2
kind: definition
name: Pseudocomplement
msc: ["06D15"]
defines: WMR73J0S26
uses: [WH4SFAACAS]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudocomplement
---

## Definition

Let $L$ be a [[lattice|WH4SFAACAS]] with a least element $0$, and let $a \in L$.
An element $a^* \in L$ is a *pseudocomplement* of $a$ if for every $x \in L$,
$$a \wedge x = 0 \iff x \le a^*.$$
The lattice $L$ is *pseudocomplemented* if every element has a pseudocomplement.

## Remarks

Equivalently, $a^*$ is the greatest element of the set $\set{x \in L : a \wedge x = 0}$, so it is unique when it exists.
In a pseudocomplemented lattice, $a \le a^{**}$ and $a^{***} = a^*$ for all $a$.

Example: the open sets of a topological space $X$, ordered by inclusion.
For an open set $U$, put $U^* = \operatorname{int}(X \setminus U)$.
An open set $V$ satisfies $U \cap V = \emptyset$ exactly when $V \subseteq X \setminus U$, that is, when $V \subseteq \operatorname{int}(X \setminus U)$, since $V$ is open.

Non-example: in the diamond lattice $M_3$ with atoms $p, q, r$, the element $p$ has no pseudocomplement.
The elements $x$ with $p \wedge x = 0$ are $0$, $q$ and $r$, and this set has no greatest element, since $q \vee r = 1$ and $p \wedge 1 = p \ne 0$.
