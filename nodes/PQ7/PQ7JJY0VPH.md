---
tag: PQ7JJY0VPH
kind: concept
name: Symplectic vector space
msc: ["15A63", "53D05"]
topics: [DYAK7YMK7B]
audience: grad
specializes: [000AYPA9AJ]
uses: [0DGDS5XY84, 01NHFZF2SK, ~a52a9f11, 01TXN7ETH2, ~0d389e21]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Standard symplectic space
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Subspaces
  - url: https://en.wikipedia.org/wiki/Symplectic_group
    locator: lead section
  - book: isbn:9780387728285
    locator: Chapter 11
same_as:
  wikidata: Q766774
  wikipedia: Symplectic vector space
---

## Summary

Let $F$ be a field.
A symplectic vector space is a finite-dimensional vector space $V$ over $F$ with a symplectic form: an [[alternating bilinear form|0DGDS5XY84]] $\omega$ that is [[nondegenerate|01NHFZF2SK]].
By the [[classification of alternating forms|~a52a9f11]], $\dim V = 2m$ is even, and $V$ has a basis $(e_1, \dots, e_m, f_1, \dots, f_m)$ with $\omega(e_i, f_j) = \delta_{ij}$ and $\omega(e_i, e_j) = \omega(f_i, f_j) = 0$.
A Lagrangian subspace is a subspace $L$ with $L^\perp = L$; each has dimension $m$, by the [[statement on Lagrangian subspaces|~95ea40c5]].
The [[formal definition|W5FHT07SJJ]] states the axioms.
Symplectic vector spaces are the linear model of phase space in classical mechanics and of the tangent spaces of symplectic manifolds.

## Motivation

On $\R^2$, the determinant $\omega(x, y) = x_1 y_2 - x_2 y_1$ gives the signed area of the parallelogram spanned by $x$ and $y$.
In mechanics, a state is a pair of a position $q$ and a momentum $p$.
The motion keeps the sum of the signed areas in the planes $(q_i, p_i)$.
So we want spaces with a bilinear form that measures signed area instead of length.
Such a form is alternating, since a vector spans no area with itself, and nondegenerate, so that it sees every direction.
Unlike inner products, all such forms of one dimension are alike, so the theory has one standard model in each even dimension.

## Notation

- The form is usually written $\omega$, and the space $(V, \omega)$.
- The standard space is $F^{2m}$ with $\omega(x, y) = x^T J y$, $J = \begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}$. Some books use the order $(e_1, f_1, e_2, f_2, \dots)$ and the matrix $J_2 \oplus \dots \oplus J_2$ with $J_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
- $W^\omega$ or $W^\perp$ is the symplectic complement of a subspace $W$. A subspace is isotropic when $W \subseteq W^\perp$, coisotropic when $W^\perp \subseteq W$, Lagrangian when $W = W^\perp$, and symplectic when $W \cap W^\perp = \{0\}$.
- The group of linear maps $T$ with $\omega(Tx, Ty) = \omega(x, y)$ is the [[symplectic group|X12FS2JAP0]] $\operatorname{Sp}(V, \omega)$ or $\operatorname{Sp}_{2m}(F)$.

## Remarks

### Examples

- [[The determinant form on $F^2$|~d5093041]] makes $F^2$ a symplectic plane, for every field $F$.
- [[$\Q^4$ with the alternating matrix of Pfaffian $8$|~b44ceee3]] is a symplectic space, with an explicit symplectic basis.
- For each finite-dimensional space $U$, the space $U \oplus U^*$ with $\omega((x, \varphi), (y, \psi)) = \psi(x) - \varphi(y)$ is symplectic, and $U$ and $U^*$ are Lagrangian subspaces.
- $\C^m$ with $\omega(x, y) = \operatorname{Im} \sum_i x_i \bar y_i$, viewed as a real space of dimension $2m$, is a real symplectic space.

### Non-examples

- [[The alternating form on $\Q^3$ with radical $(1, 0, 1)$|~35320308]] is not symplectic, because it is degenerate. No alternating form on a space of odd dimension is symplectic.
- [[The form $x_1 y_1 + x_2 y_2$ on $\mathbb{F}_2^2$|~45504b21]] is nondegenerate and skew-symmetric, but not alternating, so it is not symplectic.
- An inner product is not symplectic, because $\langle v, v \rangle > 0$ for $v \neq 0$, while a symplectic form has $\omega(v, v) = 0$.

### Basic properties

- $\dim V$ is even, and all symplectic spaces of the same dimension are isometric, by the classification of alternating forms.
- Every nonzero vector is [[isotropic|~0d389e21]], and every line is an isotropic subspace.
- For each subspace $W$, $\dim W + \dim W^\perp = \dim V$ and $(W^\perp)^\perp = W$, but $W \cap W^\perp$ can be nonzero.
- Isotropic subspaces have dimension at most $m$, Lagrangian subspaces have dimension exactly $m$, and every isotropic subspace lies in a Lagrangian one, by the [[statement on Lagrangian subspaces|~95ea40c5]].
- Each symplectic map $T \in \operatorname{Sp}_{2m}(F)$ satisfies $T^T J T = J$ in matrices, and $\det T = 1$. The symplectic group is treated in Lie theory.

### History

Hermann Weyl introduced the name "symplectic group".
He chose it to replace the older names "line complex group" and "Abelian linear group", and the Greek word is the analog of the Latin "complex".

### Common errors

- Assuming that the symplectic complement behaves like an orthogonal complement. A Lagrangian subspace is its own complement.
- Writing the standard matrix with the wrong order of the basis. Check whether a book uses $(e_1, \dots, e_m, f_1, \dots, f_m)$ or $(e_1, f_1, \dots)$.
- Taking a skew-symmetric form in characteristic $2$ for a symplectic one. The definition requires $\omega(v, v) = 0$.

## Explanations

### L1 human

A symplectic form measures signed areas, not lengths.
Every vector has area zero with itself, and every nonzero vector has nonzero area with some other vector.
The space always splits into planes, each with the area form of the plane, so the dimension is even.
All symplectic spaces of the same dimension look the same.

### L2 human

We check that $\R^4$ with $\omega(x, y) = x_1 y_3 + x_2 y_4 - x_3 y_1 - x_4 y_2$ is symplectic, and we find a Lagrangian subspace.

1. The matrix is $J = \begin{pmatrix} 0 & I_2 \\ -I_2 & 0 \end{pmatrix}$, with $J^T = -J$ and zero diagonal. So $\omega$ is alternating.
2. $\det J = 1 \neq 0$, so $\omega$ is nondegenerate.
3. Let $L = \operatorname{span}(e_1, e_2)$. Then $\omega(e_1, e_2) = 0$, so $L$ is isotropic.
4. $\dim L = 2 = \frac12 \dim \R^4$, so $L$ is Lagrangian.
5. The plane $W = \operatorname{span}(e_1, e_3)$ is not isotropic, since $\omega(e_1, e_3) = 1$. It is a symplectic subspace.

The typical use is the standard basis: it turns every computation in a symplectic space into one with the matrix $J$.
A trap: a Lagrangian subspace is not "orthogonal to its complement" in the Euclidean sense; it is its own symplectic complement.

### L3 human

A symplectic manifold is a manifold whose tangent spaces are symplectic vector spaces, with a closed form; the [[topic on linear symplectic algebra|X64DP99JRZ]] in symplectic geometry develops this side.
The Lagrangian Grassmannian, the space of Lagrangian subspaces of $\R^{2m}$, is $U(m) / O(m)$, and its topology gives the Maslov index.
Over finite fields, the symplectic groups divided by their centers are, with a few small exceptions, finite simple groups of Lie type.
