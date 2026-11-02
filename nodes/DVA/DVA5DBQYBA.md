---
tag: DVA5DBQYBA
kind: definition
name: Atomistic lattice
msc: [06B05]
defines: 99DVVV7BH2
uses: [WH4SFAACAS, 0AANKKNHS4, TTVCTW6TNC, J2T75ATRV5, 5SE8EMSDNY]
sources:
  - url: https://en.wikipedia.org/wiki/Atom_(order_theory)
---

## Definition

Let $L$ be a [[lattice|WH4SFAACAS]] with a [[least element|0AANKKNHS4]] $0$.
$L$ is *atomistic* if every $b \in L$ is the [[join|J2T75ATRV5]] in $L$ of the set $\set{a \in L : a \text{ is an atom and } a \le b}$.

## Remarks

The least element $0$ is the join of the empty set of atoms.
An atomistic lattice is [[atomic|5SE8EMSDNY]]: if $b \ne 0$ had no atom below it, $b$ would be the join of the empty set, that is $b = 0$.
Example: the power set of a set $X$ is atomistic, since every subset $B$ is the union of the singletons $\set{x}$ with $x \in B$.
Non-example: the chain $0 < 1 < 2$ is atomic, with the single atom $1$, but not atomistic.
The join of the atoms below $2$ is $1 \ne 2$.
