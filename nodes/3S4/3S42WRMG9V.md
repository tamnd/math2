---
tag: 3S42WRMG9V
kind: definition
name: Leavitt path algebra
msc: [16S88, 16S10]
defines: 9NZ9FY1S7C
uses: [04C5ZBG1WT, 0KFYGSHHF5, 2P3Y2FRCSZ, 0CD87SFM2N, 2PYANBGXFD, QMY5JTZZB8, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Leavitt_path_algebra
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] and let $E = (E^0, E^1, s, r)$ be a [[directed graph|0KFYGSHHF5]], with vertex set $E^0$, edge set $E^1$, and source and range maps $s, r \colon E^1 \to E^0$.
For each edge $e$ take a new symbol $e^*$, called a ghost edge.
The *Leavitt path algebra* $L_K(E)$ is the quotient of the [[free algebra|2P3Y2FRCSZ]] over $K$ on the set $E^0 \cup E^1 \cup \set{e^* : e \in E^1}$ by the [[two-sided ideal|0CD87SFM2N]] of these relations:

1. $v w = \delta_{v, w} v$ for all $v, w \in E^0$.
2. $s(e) e = e = e \, r(e)$ for all $e \in E^1$.
3. $r(e) e^* = e^* = e^* s(e)$ for all $e \in E^1$.
4. $e^* f = \delta_{e, f} \, r(e)$ for all $e, f \in E^1$.
5. $v = \sum_{e \in E^1, \, s(e) = v} e e^*$ for every vertex $v$ that is the source of at least one and at most finitely many edges.

Here $\delta_{a, b}$ is $1$ if $a = b$ and $0$ otherwise.

## Remarks

Relations 4 and 5 are the Cuntz–Krieger relations.
The algebra has an identity, $\sum_{v \in E^0} v$, exactly when $E^0$ is finite.
Relations 1 and 2 alone define the [[path algebra|2PYANBGXFD]] of $E$, which maps into $L_K(E)$.
Example: let $E$ have one vertex $v$ and one loop $e$.
Relation 4 gives $e^* e = v$ and relation 5 gives $e e^* = v$, with $v$ the identity, so $L_K(E)$ is the [[Laurent polynomial ring|QMY5JTZZB8]] $K[x, x^{-1}]$ with $x = e$ and $x^{-1} = e^*$.
Example: if $E$ is $u \to v$ with one edge $e$, then $L_K(E)$ is isomorphic to the [[matrix ring|0FHVPRAE60]] $M_2(K)$, via $u \mapsto E_{11}$, $v \mapsto E_{22}$, $e \mapsto E_{12}$ and $e^* \mapsto E_{21}$.
Example: one vertex with $n \ge 2$ loops gives the Leavitt algebra $L(1, n)$, in which the free module of rank $1$ is isomorphic to the free module of rank $n$.
Non-example: in the path algebra of the one-loop graph, the element $e$ has no inverse, since every product of $e$ with a combination of paths has no constant term.
Relation 4 needs the ghost edge $e^*$.
