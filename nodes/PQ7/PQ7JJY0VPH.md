---
tag: PQ7JJY0VPH
kind: concept
name: Symplectic vector space
msc: ["15A63", "53D05"]
topics: [DYAK7YMK7B]
audience: grad
specializes: [000AYPA9AJ]
uses: [0DGDS5XY84, 01NHFZF2SK, V8KKHKXXB3, 01TXN7ETH2, MZHFGPV1YT]
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

A symplectic vector space is a space with a rule for signed area in place of a rule for length.
The rule gives zero for a vector paired with itself, and it sees every nonzero vector, so the space always splits into planes and has even dimension.
Let $F$ be a field.
A *symplectic vector space* is a finite-dimensional vector space $V$ over $F$ together with a *symplectic form*: an [[alternating bilinear form|0DGDS5XY84]] $\omega$ on $V$ that is [[nondegenerate|01NHFZF2SK]].
By the [[classification of alternating forms|V8KKHKXXB3]], $\dim V = 2m$ is even, and $V$ has a basis $(e_1, \dots, e_m, f_1, \dots, f_m)$ with
$$\omega(e_i, f_j) = \delta_{ij}, \qquad \omega(e_i, e_j) = \omega(f_i, f_j) = 0.$$
A *Lagrangian subspace* is a subspace $L$ with $L^\perp = L$, and each one has dimension $m$, by the [[statement on Lagrangian subspaces|30PND47YCP]].
The [[formal definition|W5FHT07SJJ]] states the axioms.

## Motivation

On $\mathbb{R}^2$ the determinant $\omega(x, y) = x_1 y_2 - x_2 y_1$ is the signed area of the parallelogram on $x$ and $y$.
In classical mechanics a state of a particle on a line is a pair $(q, p)$ of a position and a momentum.
The motion of a mechanical system keeps the total signed area in the planes $(q_i, p_i)$, and this fact is the linear core of Hamiltonian mechanics.
So we want a bilinear form that measures signed area.
Such a form must be alternating, since a vector spans no area with itself, and nondegenerate, so that no direction is invisible to it.

Unlike inner products, all symplectic forms of one dimension are alike, so the theory has a single standard model in each even dimension.
The ideas return in the [[symplectic group|X12FS2JAP0]] of Lie theory and in symplectic manifolds, whose tangent spaces are symplectic vector spaces.

## Notation

The form is usually written $\omega$, and the space is written $(V, \omega)$.
The standard space is $F^{2m}$ with $\omega(x, y) = x^{\mathsf{T}} J y$ and $J = \begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}$.
Some books order the basis as $(e_1, f_1, e_2, f_2, \dots)$ and get the block matrix $J_2 \oplus \dots \oplus J_2$ with $J_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, so check the order before you compare matrices.
The symplectic complement of a subspace $W$ is $W^\perp = \{ v : \omega(w, v) = 0 \text{ for all } w \in W \}$, also written $W^\omega$.
A subspace $W$ is *isotropic* when $W \subseteq W^\perp$, *coisotropic* when $W^\perp \subseteq W$, *Lagrangian* when $W = W^\perp$, and *symplectic* when $W \cap W^\perp = \{0\}$.
The linear maps $T$ with $\omega(Tx, Ty) = \omega(x, y)$ form the symplectic group $\operatorname{Sp}(V, \omega)$, or $\operatorname{Sp}_{2m}(F)$.

## Remarks

### The symplectic plane

The smallest case already shows the main features.
On $F^2$ the [[determinant form|8K74K4BF5H]] $\omega(x, y) = x_1 y_2 - x_2 y_1$ has the matrix $J_2$.
It is alternating, since $\omega(x, x) = x_1 x_2 - x_2 x_1 = 0$, and nondegenerate, since $\det J_2 = 1$.
Every line $L = \operatorname{span}(v)$ is Lagrangian.
Indeed $\omega(v, v) = 0$ gives $L \subseteq L^\perp$, and the dimension formula gives $\dim L^\perp = 2 - 1 = 1$, so $L^\perp = L$.
This works over every field, including $\mathbb{F}_2$.

### More examples

The space $\mathbb{Q}^4$ with the [[alternating matrix of Pfaffian 8|C8S4RH68S0]] is symplectic, and an explicit symplectic basis can be computed for it.
For every finite-dimensional space $U$ with [[dual space|07JBSZE0V4]] $U^*$, the space $U \oplus U^*$ with
$$\omega((x, \varphi), (y, \psi)) = \psi(x) - \varphi(y)$$
is symplectic, and $U$ and $U^*$ are two Lagrangian subspaces.
On $\mathbb{C}^m$, viewed as a real space of dimension $2m$, the form $\omega(x, y) = \operatorname{Im} \sum_i x_i \overline{y_i}$ is symplectic.
It is alternating because $\sum_i x_i \overline{x_i}$ is real, and it is nondegenerate because $\omega(x, ix) = -\sum_i \lvert x_i \rvert^2$.

### What it is not

A degenerate alternating form is not symplectic.
The [[alternating form on the rational 3-space|J16BA48F44]] has a nonzero radical, and in fact no alternating form on a space of odd dimension is nondegenerate.
The [[form $x_1 y_1 + x_2 y_2$ over the field with two elements|1V7NMPCSK9]] is nondegenerate and skew-symmetric, but $\omega(e_1, e_1) = 1$, so it is not alternating and not symplectic.
An inner product is never symplectic, because it has $\langle v, v \rangle > 0$ for $v \neq 0$, while a symplectic form has $\omega(v, v) = 0$.

### The rules you can use

All symplectic spaces of the same dimension are isometric, by the classification of alternating forms.
Every vector is [[isotropic|MZHFGPV1YT]], so every line is an isotropic subspace.
For every subspace $W$, nondegeneracy gives $\dim W + \dim W^\perp = \dim V$ and $(W^\perp)^\perp = W$, by the [[dimension statement for orthogonal complements|M2JH84VEY9]].
An isotropic subspace has dimension at most $m$, and every isotropic subspace lies in a Lagrangian one, by the statement on Lagrangian subspaces.
In matrices, a symplectic map satisfies $T^{\mathsf{T}} J T = J$, and its determinant is $1$, because the Pfaffian rule gives $\operatorname{pf}(J) = \operatorname{pf}(T^{\mathsf{T}} J T) = \det T \cdot \operatorname{pf}(J)$.

### Watch out

The symplectic complement does not behave like an orthogonal complement in Euclidean space.
In the plane above, $L = \operatorname{span}(e_1)$ has $L^\perp = L$, so $L + L^\perp$ is not the whole space.
Do not assume $V = W \oplus W^\perp$; it holds only when $W$ is a symplectic subspace.
A second trap is characteristic $2$: there a skew-symmetric form need not be alternating, and the definition requires $\omega(v, v) = 0$.

### History

Hermann Weyl introduced the name "symplectic" for the group of a nondegenerate alternating form.
He chose the Greek word as the counterpart of the Latin word "complex", because the older name of the group referred to line complexes.

### Try it

First, is $\omega(x, y) = x_1 y_2 - x_2 y_1 + x_3 y_4 - x_4 y_3$ on $\mathbb{R}^4$ symplectic?
Yes: its matrix is $J_2 \oplus J_2$, which is alternating with determinant $1$.

Second, find a Lagrangian subspace for the same form.
The plane $\operatorname{span}(e_1, e_3)$ works, since $\omega(e_1, e_3) = 0$ and its dimension is $2 = \tfrac{1}{2} \cdot 4$.

## Explanations

### L1 human

A symplectic form measures signed areas, not lengths.
For two arrows in the plane, it gives the area of the parallelogram they span, with a sign for the order.
For $(2, 0)$ and $(1, 3)$ it gives $2 \cdot 3 - 0 \cdot 1 = 6$, and in the other order it gives $-6$.
Every arrow has area zero with itself, and every nonzero arrow has nonzero area with some other arrow.
Larger symplectic spaces are stacks of such planes, so their dimension is always even.

### L2 human

Here is a typical check: is $\mathbb{R}^4$ with $\omega(x, y) = x_1 y_3 + x_2 y_4 - x_3 y_1 - x_4 y_2$ symplectic, and what is a Lagrangian subspace?
The matrix of $\omega$ is
$$J = \begin{pmatrix} 0 & I_2 \\ -I_2 & 0 \end{pmatrix},$$
with $J^{\mathsf{T}} = -J$ and a zero diagonal, so $\omega$ is alternating.
Its determinant is $1 \neq 0$, so $\omega$ is nondegenerate, and the space is symplectic.
The plane $L = \operatorname{span}(e_1, e_2)$ has $\omega(e_1, e_2) = 0$, so it is isotropic, and $\dim L = 2$ is half of $4$, so it is Lagrangian.
The plane $W = \operatorname{span}(e_1, e_3)$ is not isotropic, since $\omega(e_1, e_3) = 1$; it is a symplectic subspace.
In the standard basis every computation becomes a computation with $J$, which is why one finds such a basis first.

### L3 human

A symplectic manifold is a manifold with a closed nondegenerate $2$-form, so each of its tangent spaces is a symplectic vector space; the topic on [[linear symplectic algebra|X64DP99JRZ]] in symplectic geometry starts from there.
The Lagrangian subspaces of $\mathbb{R}^{2m}$ form the Lagrangian Grassmannian $U(m) / O(m)$, of dimension $m(m + 1) / 2$, and its topology gives the [[Maslov index|91KJT4TXG8]].
Over finite fields, the symplectic groups modulo their centers are finite simple groups of Lie type, apart from a few small cases.
For symmetric forms the analogue of a symplectic basis is the [[Witt decomposition|BPMRSPB6GD]], where an anisotropic part can remain.
