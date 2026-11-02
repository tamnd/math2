---
tag: MX38D5Z5NY
kind: definition
name: Piecewise linear manifold
msc: [57Q99, 57Q25]
defines: 15MKGRNM9K
uses: [QQQ9B1DK4P, J7P32JQTVE, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Piecewise_linear_manifold
---

## Definition

Let $n \ge 0$ and let $U$ and $V$ be [[open subsets|02BH3MCBQB]] of $\R^n$.
A map $f \colon U \to V$ is *piecewise linear* if $U$ is a union of a locally finite family of [[simplices|YX1DJK2QAG]] in $\R^n$ with $f$ affine on each.
Any two simplices of the family must meet in a common face or not at all.
Let $M$ be a [[topological manifold|QQQ9B1DK4P]] of dimension $n$.
A *PL atlas* on $M$ is an [[atlas|J7P32JQTVE]] of dimension $n$ all of whose transition maps are piecewise linear.
Two PL atlases are *equivalent* if their union is a PL atlas.
A *piecewise linear manifold* is a topological manifold together with an equivalence class of PL atlases, called a *PL structure*.

## Remarks

The boundary $Q$ of the square $[0,1]^2$ is a PL manifold of dimension $1$.
For each vertex $v$, let $U_v$ be the union of $v$ and the two open edges at $v$.
Unfold $U_v$ onto an open interval of $\R$ by a map that sends $v$ to $0$ and is affine on each of the two edges.
These four charts cover $Q$, and each transition map is affine on each of finitely many intervals, so it is piecewise linear.

The two stereographic charts $x/(1 - y)$ and $x/(1 + y)$ of the unit circle $S^1$ do not form a PL atlas.
Their transition map $t \mapsto 1/t$ on $\R \setminus \set{0}$ is not affine on any interval.
The circle does have a PL structure, carried over from $Q$ by a homeomorphism $Q \to S^1$.

Every smooth manifold has a PL structure, unique up to PL homeomorphism, by a theorem of J. H. C. Whitehead.
Every topological manifold of dimension at most $3$ has a unique PL structure, while in higher dimensions a manifold may have none or several.
Equivalently, a PL manifold of dimension $n$ is the realization of a combinatorial manifold.
This is a simplicial complex in which the link of each vertex is PL homeomorphic to the boundary of an $n$-simplex.
