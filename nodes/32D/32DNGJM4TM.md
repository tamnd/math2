---
tag: 32DNGJM4TM
kind: definition
name: Bravais lattice
msc: [82D25, "74E15", 11H06]
defines: 2ASPT0SP6Z
uses: [WN9V7WSJKF]
sources:
  - url: https://en.wikipedia.org/wiki/Bravais_lattice
---

## Definition

Let $n \ge 1$, in physics usually $n \in \set{1, 2, 3}$.
A *Bravais lattice* in $\R^n$ is a set of the form
$$\Lambda = \set{m_1 a_1 + \cdots + m_n a_n : m_1, \dots, m_n \in \Z},$$
where $a_1, \dots, a_n$ are linearly independent vectors of $\R^n$, called *primitive vectors*.
Equivalently, it is a [[lattice|WN9V7WSJKF]] in $\R^n$: a discrete subgroup of $(\R^n, +)$ that spans $\R^n$.
The parallelepiped $\set{t_1 a_1 + \cdots + t_n a_n : 0 \le t_i < 1}$ is a *primitive cell*; its volume $\abs{\det(a_1, \dots, a_n)}$ does not depend on the choice of primitive vectors.

## Remarks

Example: the face-centred cubic lattice is the Bravais lattice with primitive vectors $a_1 = \tfrac{a}{2}(0, 1, 1)$, $a_2 = \tfrac{a}{2}(1, 0, 1)$, $a_3 = \tfrac{a}{2}(1, 1, 0)$ for some $a > 0$.
These vectors are independent, since $\det(a_1, a_2, a_3) = a^3/4 \ne 0$, so the primitive cell has volume $a^3/4$.

Non-example: the vertices of the honeycomb tiling of the plane do not form a Bravais lattice.
The set is not invariant under its own difference vectors.
If $x$ and $y$ are neighbouring vertices, the translation by $y - x$ maps $x$ to a vertex but maps $y$ to the centre of a hexagon.
The honeycomb is a triangular Bravais lattice with a basis of two points.

Bravais lattices are grouped into types by their point symmetry and centring.
There are $5$ types in dimension $2$ and $14$ types in dimension $3$.
