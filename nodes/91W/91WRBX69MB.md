---
tag: 91WRBX69MB
kind: example
name: The integer order is categorical in no infinite cardinal
aliases: [theory-of-the-integer-order-is-not-categorical]
msc: ["03C35", "06A05"]
topics: [6XEXRME4C1]
audience: grad
not_instance_of:
  - target: 1JJCGNX240
    note: for every infinite cardinal kappa, the theory of the integer order has two non-isomorphic models of size kappa
  - target: A22K1X8GKD
    note: the integers and two copies of the integers are non-isomorphic countable models of the same complete theory
uses: [1JJCGNX240, JPE6BXFX3F, 72BMYXGFA8, P3B1V182N4, NJY30DQG3H, 0RDJK7EQYY]
sources:
  - book: isbn:9780521587136
---

## Example

Let $T = \operatorname{Th}(\Z, <)$, the set of first-order sentences in the signature $\set{<}$ that are true in the integers.
For a nonempty linear order $I$, let $\Z \cdot I$ be the [[ordered sum|NJY30DQG3H]] of copies of $\Z$ indexed by $I$: its elements are the pairs $(i, z)$ with $i \in I$ and $z \in \Z$, ordered first by $i$ and then by $z$.
We show that $T$ is not $\kappa$-categorical for any infinite cardinal $\kappa$.

1. Each $\Z \cdot I$ is a model of $T$. The strategy of [[this example|JPE6BXFX3F]] works for $\Z$ and $\Z \cdot I$, so Duplicator wins every finite game, and the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]] gives $\Z \cdot I \equiv \Z$.
2. In $\Z \cdot I$, call $u$ and $v$ *close* when only finitely many elements lie between them. The close pairs are exactly the pairs in the same copy $\set{i} \times \Z$.
3. Closeness is defined from $<$ alone, so an isomorphism $f : \Z \cdot I \to \Z \cdot J$ maps each copy onto a copy, and it keeps the order of the copies.
4. So $f$ induces an order isomorphism from $I$ onto $J$. In short, $\Z \cdot I \cong \Z \cdot J$ implies $I \cong J$.
5. Let $\kappa$ be an infinite cardinal, viewed as a limit [[ordinal|0RDJK7EQYY]], and let $I = \kappa$ and $J = \kappa + 1$. Then $\abs{\Z \cdot I} = \abs{\Z \cdot J} = \aleph_0 \cdot \kappa = \kappa$.
6. The order $\kappa$ has no greatest element, because it is a limit ordinal, and $\kappa + 1$ has the greatest element $\kappa$. So $I \not\cong J$.
7. By steps 4 and 6, $\Z \cdot I$ and $\Z \cdot J$ are non-isomorphic models of $T$ of size $\kappa$.

## Remarks

The theory $T$ is complete, because it is the theory of one structure, and it has no finite models.
So the converse of the [[Łoś-Vaught test|ZR7Y5C235P]] fails: a complete theory need not be categorical in any cardinal.
For $\kappa = \aleph_0$ the example says that $\Z$ and $\Z + \Z$ are elementarily equivalent and not isomorphic.
Every countable model of $T$ has the form $\Z \cdot I$ for a countable nonempty order $I$, and there are $2^{\aleph_0}$ countable orders up to isomorphism, so $T$ has $2^{\aleph_0}$ countable models.
The theory is still [[small|W6XM5NVNRP]]: an $n$-type is fixed by the order of the points and by the distances that are finite.

## Explanations

### L1 human

Think of the integers as an endless line of stepping stones.
A copy of the integers next to another copy looks the same to anyone who only checks finitely many stones at a time.
So the rules that the integers obey are also obeyed by two, three or infinitely many lines of stones placed one after another.
These worlds are different, because the number and the arrangement of the lines can be read off from the order.
So the rules never fix one world, in any size.

### L2 human

We do the case $\kappa = \aleph_0$ with $I = \set{0}$ and $J = \set{0, 1}$.

1. $\Z \cdot I$ is $\Z$, and $\Z \cdot J$ is $\Z + \Z$. Both are countable models of $T$ by step 1.
2. In $\Z$ any two elements are close, since only finitely many integers lie between them.
3. In $\Z + \Z$ the elements $(0, 0)$ and $(1, 0)$ are not close, since all $(0, z)$ with $z > 0$ lie between them.
4. An isomorphism keeps closeness, so it cannot map $\Z$ onto $\Z + \Z$.

The typical use is to show that a complete theory can have many models of each size.
A trap is to use the sentence "any two elements are close" to separate the models; it is not first-order, which is why the models are elementarily equivalent.
