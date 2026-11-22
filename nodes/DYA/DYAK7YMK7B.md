---
tag: DYAK7YMK7B
kind: topic
name: Bilinear and sesquilinear forms
msc: ["15A63"]
topics: [GN8GYSDZFX]
---

## Summary

A bilinear form pairs two vectors to a number and is linear in each of them, and it is what remains of the dot product when you give up symmetry and positivity.
The story starts with the dot product, the signed area $x_1 y_2 - x_2 y_1$ and the trace pairing $\operatorname{tr}(XY)$, which all have this one property in common.
In a basis a form becomes a square matrix, and a change of basis replaces the matrix $A$ by $P^{\mathsf{T}} A P$, so the right equivalence of matrices is congruence and not similarity.
Two families then carry most of the theory.
Symmetric forms give lengths and orthogonal geometry, alternating forms give areas and symplectic geometry, and these are the only forms for which orthogonality is a symmetric relation.
Nondegeneracy and orthogonal complements come next, then isotropic vectors and the hyperbolic plane, since outside characteristic $2$ every isotropic vector of a nondegenerate symmetric form lies in a hyperbolic plane.
Over $\mathbb{C}$, conjugating one slot gives sesquilinear and Hermitian forms, the setting of complex inner products.
The sub-area ends with the classification of alternating forms by their rank and with symplectic vector spaces.
Its last pages are the theorems of Witt: outside characteristic $2$, a nondegenerate symmetric form splits into hyperbolic planes and an anisotropic part, and that part is unique up to isometry.
It is a part of [[linear algebra|GN8GYSDZFX]], and it leads to quadratic forms, the classical groups and symplectic geometry.

## Remarks

### Reading order

1. [[Bilinear form|0SQZMXB6GP]]: the definition, the four standard examples, and how to test a formula for bilinearity.
2. [[Matrix of a bilinear form|0QK6K857HS]]: how a form becomes the product $x^{\mathsf{T}} A y$ and what the matrix tells you about the form.
3. [[Change of basis for bilinear forms|0SPYAGE7T0]]: why the matrix changes to $P^{\mathsf{T}} A P$, and why the rank of a form is well defined.
4. [[Congruent matrices|WJWNYSQKK8]]: the equivalence relation of congruence and how it differs from similarity.
5. [[Symmetric bilinear form|0AXZNE5XNH]]: forms with $B(x, y) = B(y, x)$, symmetric matrices, and inner products as a special case.
6. [[Alternating bilinear form|0DGDS5XY84]]: forms with $B(v, v) = 0$, and why skew-symmetric is a weaker condition in characteristic $2$.
7. [[Reflexive bilinear forms|M0G958M917]]: why orthogonality is symmetric only for symmetric and alternating forms.
8. [[Nondegenerate bilinear form|01NHFZF2SK]]: the radical, and the tests by the matrix and by the map into the dual space.
9. [[Orthogonality for a bilinear form|01TXN7ETH2]]: orthogonal complements, their dimensions, and subspaces that meet their own complement.
10. [[Isotropic vectors and subspaces|MZHFGPV1YT]]: nonzero vectors with $B(v, v) = 0$, and anisotropic forms.
11. [[Hyperbolic plane|1X5PZSK44P]]: the plane with matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and why every isotropic vector lies in one.
12. [[Sesquilinear form|054YEQ0Y8M]]: forms over $\mathbb{C}$ with one conjugate-linear slot, and the two conventions for that slot.
13. [[Hermitian form|48P4A1CX85]]: sesquilinear forms with real values $h(v, v)$, Hermitian matrices, and complex inner products.
14. [[Classification of alternating forms|V8KKHKXXB3]]: symplectic bases, and why the rank of an alternating form is even.
15. [[Symplectic vector space|PQ7JJY0VPH]]: nondegenerate alternating forms, even dimension, and Lagrangian subspaces.
16. [[Witt decomposition and Witt index|BPMRSPB6GD]]: a symmetric form as hyperbolic planes plus an anisotropic part.
17. [[Witt's theorem|CCB8VNQCV0]]: cancellation, the extension of isometries between subspaces, and the uniqueness of the anisotropic part.

### Prerequisites

- [[Dual spaces and duality|9K7FFF26QR]]: the dual space $V^*$, dual bases and annihilators.
- [[Matrices of linear maps, rank and change of basis|S6559D61BP]]: coordinates, the rank of a matrix, and change of basis matrices.
- [[Inner product spaces|1D4JTZ9VS3]]: the main example of a symmetric or Hermitian form, and the source of the slot convention for complex forms.
