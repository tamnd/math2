---
tag: W6AVEAW2WR
kind: statement
role: lemma
name: Five lemma
msc: ["18G35", "18E10"]
uses: [Y9CZ3MTNF1, JB7ZBFBA9C, WV898P4X16, Y2NP1JFR86, RVXDSY04KG, JMCKACGCQ0]
about: [JB7ZBFBA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Five_lemma
same_as:
  wikidata: Q1479523
  wikipedia: Five lemma
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]], such as the category of modules over a ring.
Consider a [[commutative diagram|WV898P4X16]]
$$\begin{array}{ccccccccc} A & \to & B & \to & C & \to & D & \to & E \\ \downarrow{\scriptstyle l} & & \downarrow{\scriptstyle m} & & \downarrow{\scriptstyle n} & & \downarrow{\scriptstyle p} & & \downarrow{\scriptstyle q} \\ A' & \to & B' & \to & C' & \to & D' & \to & E' \end{array}$$
in $\mathcal{A}$ whose two rows are [[exact|JB7ZBFBA9C]].
Suppose that $m$ and $p$ are isomorphisms, that $l$ is an [[epimorphism|RVXDSY04KG]] and that $q$ is a [[monomorphism|Y2NP1JFR86]].
Then $n$ is an isomorphism.

## Remarks

The lemma is the conjunction of the two halves of the [[four lemma|JMCKACGCQ0]].
The left four columns, with $m, p$ monomorphisms and $l$ an epimorphism, show that $n$ is a monomorphism.
The right four columns, with $m, p$ epimorphisms and $q$ a monomorphism, show that $n$ is an epimorphism.
Each half is a diagram chase.
A typical use: a map between two short exact sequences that is an isomorphism on the outer terms is an isomorphism on the middle term, by taking $A = A' = E = E' = 0$.
The existence of the map $n$ making the diagram commute is essential: $0 \to \Z/2\Z \to \Z/4\Z \to \Z/2\Z \to 0$ and $0 \to \Z/2\Z \to \Z/2\Z \oplus \Z/2\Z \to \Z/2\Z \to 0$ have isomorphic outer terms, but $\Z/4\Z \not\cong \Z/2\Z \oplus \Z/2\Z$.

## Explanations

### L1 human

Picture two exact rows of five objects, with vertical maps between them.
If the four outer vertical maps are isomorphisms, then so is the middle one.
In fact less is needed at the two ends: the far left map only needs to be onto, and the far right map only needs to be one-to-one.

### L2 human

The five lemma is used constantly to show that a natural map is an isomorphism.
One fits the map into a ladder of long exact sequences, for example in homology, where the other maps are already known to be isomorphisms.
This is how one proves that a map of spaces that induces isomorphisms on the homology of pieces induces an isomorphism on the whole, as in Mayer–Vietoris arguments.
It also proves the splitting lemma and the invariance of derived functors under the choice of resolution.
