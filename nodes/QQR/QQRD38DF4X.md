---
tag: QQRD38DF4X
kind: definition
name: Haefliger structure
msc: [57R32, 57R30, 58H05]
defines: 8GYWYYBFWE
uses: [0CQHFPGJ45, VZXF7RNFKS, FH3C0T643F, 98HTB7MSPX, WSZ40H5E4T]
sources:
  - url: https://en.wikipedia.org/wiki/Haefliger_structure
---

## Definition

Let $q \ge 0$ be an integer.
Let $\Gamma_q$ be the [[groupoid|FH3C0T643F]] whose objects are the points of $\R^q$.
Its arrows from $a$ to $b$ are the [[germs|VZXF7RNFKS]] at $a$ of local diffeomorphisms $\phi$ of $\R^q$ with $\phi(a) = b$.
Give the set of arrows the sheaf topology, in which the germs at nearby points of one local diffeomorphism form an open set.
Let $X$ be a [[topological space|0CQHFPGJ45]].
A *$\Gamma_q$-cocycle* on $X$ is given by an open cover $(U_i)_{i \in I}$ of $X$ and continuous maps $\gamma_{ij} \colon U_i \cap U_j \to \Gamma_q$ such that
$$\gamma_{ik}(x) = \gamma_{ij}(x) \, \gamma_{jk}(x) \quad \text{for all } x \in U_i \cap U_j \cap U_k.$$
Two $\Gamma_q$-cocycles are equivalent if their union, over the disjoint union of the two index sets, is again a $\Gamma_q$-cocycle.
A *Haefliger structure* of codimension $q$ on $X$, or $\Gamma_q$-structure, is an equivalence class of $\Gamma_q$-cocycles.

## Remarks

The cocycle condition with $i = j = k$ shows that $\gamma_{ii}(x)$ is the germ of the identity at a point $f_i(x) \in \R^q$, and this defines continuous maps $f_i \colon U_i \to \R^q$.
The germ $\gamma_{ij}(x)$ goes from $f_j(x)$ to $f_i(x)$, so near $x$ the local maps satisfy $f_i = \phi \circ f_j$ for a representative $\phi$.
The same definition works with any topological groupoid in place of $\Gamma_q$.

Example: let $\mathcal{F}$ be a [[foliation|98HTB7MSPX]] of codimension $q$ of a manifold $X$, given by submersions $f_i \colon U_i \to \R^q$ with $f_i = g_{ij} \circ f_j$ on overlaps for local diffeomorphisms $g_{ij}$.
Taking $\gamma_{ij}(x)$ to be the germ of $g_{ij}$ at $f_j(x)$ gives a $\Gamma_q$-cocycle, since the transition maps compose as $g_{ik} = g_{ij} \circ g_{jk}$ near each point.
Another example: any continuous map $f \colon X \to \R^q$ gives a $\Gamma_q$-structure with one open set $U_1 = X$ and $\gamma_{11}(x)$ the germ of the identity at $f(x)$.

Non-example: let $X$ be a point, $U_1 = U_2 = X$, $\gamma_{11} = \gamma_{22} = \gamma_{21}$ the germ of the identity at $0$ and $\gamma_{12}$ the germ of $t \mapsto 2t$ at $0$.
The cocycle condition fails for $(i, j, k) = (1, 2, 1)$, since $\gamma_{12} \gamma_{21}$ is the germ of $t \mapsto 2t$ and not that of the identity.

Haefliger structures pull back along continuous maps.
For a CW complex $X$, homotopy classes of $\Gamma_q$-structures on $X$ correspond to homotopy classes of maps from $X$ into a [[classifying space|WSZ40H5E4T]] $B\Gamma_q$.

## Explanations

### L1 human

A Haefliger structure is the gluing data of a foliation, kept even where the local maps fail to be submersions.
