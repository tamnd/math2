---
tag: EYMHCPTZ8T
kind: definition
name: Dehn invariant
msc: [52B45, 51M20]
defines: S0TGRX3ARS
uses: [0325SGSJAR, 05HN08ZSRJ, F0HQXQ0HCD, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Dehn_invariant
---

## Definition

Let $P$ be a [[polyhedron|0325SGSJAR]] in $\R^3$.
For each edge $e$ of $P$, let $\ell(e)$ be its length and let $\theta(e)$ be the [[dihedral angle|05HN08ZSRJ]] of $P$ at $e$.
The *Dehn invariant* of $P$ is the element
$$D(P) = \sum_{e} \ell(e) \otimes \theta(e)$$
of the [[tensor product|F0HQXQ0HCD]] $\R \otimes_\Z (\R / \pi\Z)$ of [[abelian groups|082GHNPJ53]].
The sum runs over all edges of $P$.

## Remarks

Example: for the cube of side $a$, every dihedral angle is $\pi/2$.
So each edge gives $a \otimes \pi/2 = (a/2) \otimes \pi = 0$, and $D(\text{cube}) = 0$.
A polyhedron with nonzero invariant: the regular tetrahedron of side $a$ has dihedral angle $\arccos(1/3)$, which is not a rational multiple of $\pi$.
Its invariant $6a \otimes \arccos(1/3)$ is not $0$, since $\R \otimes_\Z (\R/\pi\Z)$ is isomorphic to the $\Q$-vector space $\R \otimes_\Q (\R/\Q\pi)$.
The invariant is additive: if $P$ is cut into polyhedra $P_1, \dots, P_k$, then $D(P) = D(P_1) + \cdots + D(P_k)$.
