---
tag: HS0R4H5SAW
kind: definition
name: Generalized Boolean algebra
msc: ["06E75", "06E20"]
defines: ZK1MHTQGS9
uses: [0T36P6TXQ6, 06GKBTAA5E]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_algebra_(structure)
---

## Definition

Let $L$ be a [[distributive lattice|0T36P6TXQ6]] with meet $\wedge$, join $\vee$ and a least element $0$.
The lattice $L$ is a *generalized Boolean algebra* if for all $a, b \in L$ there is an element $x \in L$ such that
$$(a \wedge b) \vee x = a \quad \text{and} \quad (a \wedge b) \wedge x = 0.$$
The element $x$ is unique by distributivity.
It is the *relative complement* of $b$ in $a$, written $a \setminus b$.

## Remarks

Example: the finite subsets of $\N$, ordered by inclusion, form a generalized Boolean algebra.
For finite sets $a$ and $b$, the set $x = a \setminus b$ is finite, $(a \cap b) \cup x = a$, and $(a \cap b) \cap x = \emptyset$.
This lattice has no greatest element, so it is not a [[Boolean algebra|06GKBTAA5E]].
Non-example: the chain $0 < 1 < 2$ is a distributive lattice with least element $0$, but for $a = 2$ and $b = 1$ there is no $x$ with $1 \vee x = 2$ and $1 \wedge x = 0$.
Indeed $1 \vee x = 2$ forces $x = 2$, and then $1 \wedge x = 1 \ne 0$.
Equivalently, a distributive lattice with $0$ is a generalized Boolean algebra if and only if each interval $[0, a]$ is a Boolean algebra.
A generalized Boolean algebra with a greatest element is the same as a Boolean algebra.
