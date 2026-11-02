---
tag: FX5PWKCMBQ
kind: statement
role: theorem
name: Bipolar theorem
msc: [46A20, 46A55]
uses: [R68HNB5SVR, P6KHVSTPZV, 0FQSDC2EQ2, 2TDSHJJYS4, 0QEAJB91GZ]
about: [R68HNB5SVR, P6KHVSTPZV]
sources:
  - url: https://en.wikipedia.org/wiki/Bipolar_theorem
same_as:
  wikidata: Q4915488
  wikipedia: Bipolar theorem
---

## Statement

Let $\mathbb{K}$ be $\R$ or $\C$, and let $(X, Y, \langle \cdot, \cdot \rangle)$ be a [[dual pair|R68HNB5SVR]] over $\mathbb{K}$.
For $A \subseteq X$, its *polar* is $A^\circ = \set{y \in Y : \abs{\langle x, y \rangle} \le 1 \text{ for all } x \in A}$, and for $B \subseteq Y$, its polar is $B^\circ = \set{x \in X : \abs{\langle x, y \rangle} \le 1 \text{ for all } y \in B}$.
Let $A \subseteq X$, and let $C$ be the [[convex hull|0FQSDC2EQ2]] of $\set{\lambda a : a \in A, \lambda \in \mathbb{K}, \abs{\lambda} \le 1}$.
Then the bipolar $A^{\circ\circ} = (A^\circ)^\circ$ is the [[closure|0QEAJB91GZ]] of $C$ in the [[weak topology|P6KHVSTPZV]] $\sigma(X, Y)$.

## Remarks

The set described is the smallest $\sigma(X, Y)$-closed, convex and [[balanced|2TDSHJJYS4]] set containing $A$, the closed absolutely convex hull of $A$.
The bipolar contains $A$ and is convex, balanced and $\sigma(X, Y)$-closed, so it contains this hull.
For the reverse inclusion, take $x_0$ outside the hull.
The continuous dual of $(X, \sigma(X, Y))$ is $Y$, so the Hahn–Banach separation theorem gives $y \in Y$ with $\abs{\langle a, y \rangle} \le 1$ on the hull and $\abs{\langle x_0, y \rangle} > 1$.
Hence $x_0 \notin A^{\circ\circ}$.
Example: take a normed space $E$ with the pair $(E, E')$, and let $A$ be the open unit ball of $E$.
Then $A^\circ$ is the closed unit ball of $E'$, and $A^{\circ\circ}$ is the closed unit ball of $E$, the weak closure of the open ball.
Over $\R$ with one-sided polars $\set{y : \langle x, y \rangle \le 1}$, the bipolar is instead the closed convex hull of $A \cup \set{0}$.

## Explanations

### L1 human

The polar of a set collects all test vectors that keep the set inside the "unit band" $\abs{\langle x, y \rangle} \le 1$.
Taking the polar twice gives back the original set, filled in to be convex, symmetric and closed.
So a closed convex symmetric set is completely described by its polar.

### L2 human

The bipolar theorem is the convex-geometric form of the Hahn–Banach theorem for a dual pair.
It shows that every closed absolutely convex set is an intersection of "slabs" $\set{x : \abs{\langle x, y \rangle} \le 1}$.
It is the main tool in the proof of the [[Mackey–Arens theorem|RKKWS7CDNF]] and in describing equicontinuous sets and bounded sets through polars.
Combined with the [[Banach–Alaoglu theorem|1BXEJXQ2YT]], it describes the closed absolutely convex neighbourhoods of $0$.
Each of them is the polar of its own polar, which is a weak-\* compact absolutely convex set of the dual.
