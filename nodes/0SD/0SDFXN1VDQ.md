---
tag: 0SDFXN1VDQ
kind: definition
name: Dihedral angle
msc: [51N20]
defines: 05HN08ZSRJ
uses: [0V3XAMF3C1, 0WQJJCCTC8, 0ZEHZY85E6]
sources:
  - url: https://en.wikipedia.org/wiki/Dihedral_angle
    locator: Mathematical background
inventory: [8132PFDS1P]
---

## Definition

Let $P_1$ and $P_2$ be two [[planes|0V3XAMF3C1]] in $\mathbb{R}^3$ that meet in a line. Let $n_1$ and $n_2$ be [[normal vectors|0WQJJCCTC8]] of $P_1$ and $P_2$, and let $\cdot$ be the dot product.
The dihedral angle between $P_1$ and $P_2$ is the unique real number $\varphi$ with $0 \leq \varphi \leq \pi / 2$ such that
$$\cos \varphi = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|}.$$

## Remarks

The value does not depend on the choice of the normal vectors. The absolute value is necessary because $-n_1$ is also a normal vector of $P_1$.
For two half-planes with a common edge line, the dihedral angle is in $[0, \pi]$. Take a point $O$ on the edge. Let $u_1$ and $u_2$ be vectors that are perpendicular to the edge and point from $O$ into the two half-planes. The dihedral angle is the [[angle between $u_1$ and $u_2$|0ZEHZY85E6]].
For the planes $z = 0$ and $x = 0$, the normal vectors $(0, 0, 1)$ and $(1, 0, 0)$ have dot product $0$, so the dihedral angle is $\pi / 2$.
The dihedral angles of a polyhedron are the angles between the planes of two faces with a common edge, measured inside the solid.

## Explanations

### L1 human

Open a book partly. The two covers are half-planes that meet along the spine. The dihedral angle is how far the book is open: $0$ when it is closed and $\pi$ when it lies flat.
