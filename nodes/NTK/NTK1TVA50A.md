---
tag: NTK1TVA50A
kind: statement
role: theorem
name: Švarc–Milnor lemma
msc: [20F65, 51F30]
uses: [0VKD1TP7F3, 0RN765S7DH, 0WCY42EV9V, 02HPP5VCZH, 082DWWXMRJ, VCHJVR9NGH, 6FKYSH729T]
about: [6FKYSH729T, 082DWWXMRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Švarc–Milnor_lemma
same_as:
  wikidata: Q11085263
  wikipedia: Švarc–Milnor lemma
---

## Statement

Let $X$ be a [[proper metric space|0RN765S7DH]] that is geodesic: any two points $x, y$ are joined by a path of length $d(x, y)$.
Let a group $G$ [[act|0WCY42EV9V]] on $X$ by [[isometries|02HPP5VCZH]].
Assume that the action is proper: for every compact set $K \subseteq X$, the set $\set{g \in G : gK \cap K \neq \emptyset}$ is finite.
Assume also that the action is cocompact: there is a compact set $K \subseteq X$ with $GK = X$.
Then:

1. $G$ is [[finitely generated|082DWWXMRJ]].
2. Let $S$ be a finite generating set of $G$ and $x_0 \in X$. Then the orbit map $g \mapsto g x_0$ is a [[quasi-isometry|6FKYSH729T]] from $G$, with the [[word metric|VCHJVR9NGH]] of $S$, to $X$.

## Remarks

Idea of the proof.
Choose a closed ball $B$ around $x_0$ whose translates cover $X$, and let $S$ be the finite set of $g$ with $gB \cap B \neq \emptyset$.
A geodesic from $x_0$ to $g x_0$ can be cut into short pieces, and consecutive pieces lie in translates of $B$ that meet.
This writes $g$ as a word in $S$ of length at most a linear function of $d(x_0, g x_0)$.
The other inequality holds because each generator moves $x_0$ by a bounded distance.

Example: $\Z^n$ acts on $\R^n$ by translations, properly and cocompactly, so $\Z^n$ with its standard word metric is quasi-isometric to $\R^n$.
Example: the fundamental group of a closed Riemannian manifold acts on the universal cover in this way, so the group and the universal cover are quasi-isometric.

Cocompactness is necessary.
The group $\Z$ acts properly on $\R^2$ by $n \cdot (a, b) = (a + n, b)$.
But the orbit of a point lies on a line, which is not within bounded distance of every point of the plane, so the orbit map is not a quasi-isometry.

## Explanations

### L1 human

Suppose a group moves the points of a nice space around, without piling up, and the moved copies of one bounded region cover the space.
Then the group and the space have the same large-scale shape.
So one can study a group by looking at a space it acts on, and conversely.
For instance, the grid $\Z^2$ and the plane look the same from far away.

### L2 human

The lemma is the bridge between groups and geometry in [[geometric group theory|2T3218RXTD]].
It shows that the quasi-isometry class of a finitely generated group does not depend on the generating set.
It also equals the class of any space on which the group acts properly and cocompactly.
For instance, the fundamental group of a closed hyperbolic surface is quasi-isometric to the hyperbolic plane, and so it is a [[hyperbolic group|JWJ8YPR7EB]].
Large-scale invariants of spaces, such as [[growth|4CMRM3975W]], hyperbolicity or the number of ends, thus become invariants of groups.
