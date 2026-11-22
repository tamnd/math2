---
tag: 16WRFVDYB0
kind: example
name: The inner product adjoint is not the dual map
msc: ["15A04", "15A63"]
topics: [9K7FFF26QR]
audience: ug2
not_instance_of:
  - target: 0AZ5ARP287
    note: for the inner product with Gram matrix diag(1, 2) on R^2, the adjoint of A = E12 is a map R^2 to R^2 with matrix G^-1 A^T G, which differs from the transpose A^T
uses: [0C2TQMW5A1, 0ST8QF9T3T, 0NB0AWGJBW, 0W809K6AW0, 04GYPXDXNH]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Relation to the Hermitian adjoint
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Definition for bounded operators between Hilbert spaces
---

## Example

Let $V = \R^2$ with the [[inner product|0NB0AWGJBW]] $\langle v, w \rangle = v^{\mathsf{T}} G w$, where $G = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$, so that $\langle v, w \rangle = v_1 w_1 + 2 v_2 w_2$.
Let $f(x) = Ax$ with $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
We compare the [[adjoint|0ST8QF9T3T]] $f^\dagger$, the map $V \to V$ with $\langle f v, w \rangle = \langle v, f^\dagger w \rangle$ for all $v, w$, with the [[dual map|0C2TQMW5A1]] $f^*$.

1. The dual map $f^* \colon V^* \to V^*$ is defined with no inner product, and in the dual of the standard basis its matrix is $A^{\mathsf{T}} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
2. The adjoint is a map $V \to V$; let $M$ be its matrix. The defining condition reads $(Av)^{\mathsf{T}} G w = v^{\mathsf{T}} G M w$ for all $v, w$.
3. The left side is $v^{\mathsf{T}} A^{\mathsf{T}} G w$. Two matrices that give the same value for all $v$ and $w$ are equal, so $A^{\mathsf{T}} G = G M$, and $M = G^{-1} A^{\mathsf{T}} G$.
4. First compute $A^{\mathsf{T}} G = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
5. Then $M = \begin{pmatrix} 1 & 0 \\ 0 & \tfrac{1}{2} \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ \tfrac{1}{2} & 0 \end{pmatrix}$.
6. Check with $v = e_2$ and $w = e_1$. On one side $\langle A e_2, e_1 \rangle = \langle e_1, e_1 \rangle = 1$. On the other side $\langle e_2, M e_1 \rangle = \langle e_2, \tfrac{1}{2} e_2 \rangle = \tfrac{1}{2} \cdot 2 = 1$.
7. So $M \ne A^{\mathsf{T}}$. The adjoint and the dual map act on different spaces, and here even their matrices differ.

## Remarks

The example shows that the two "reverses" of a linear map are different objects.
The dual map is fixed by $f$ alone, while the adjoint changes when the inner product changes.

The two are linked by the Riesz map $R \colon V \to V^*$, $R(w) = \langle w, \cdot \rangle$, which is an isomorphism by the [[Riesz representation theorem|04GYPXDXNH]].
For each $w$, the form $f^*(R w)$ sends $v$ to $\langle w, f v \rangle = \langle f^\dagger w, v \rangle$, so $f^*(R w) = R(f^\dagger w)$.
So $f^\dagger = R^{-1} \circ f^* \circ R$, and the Riesz map depends on the inner product.

What changes when $G$ changes?
For the dot product, $G = I$, and the formula gives $M = A^{\mathsf{T}}$.
The same holds in any orthonormal basis, and this is why many books identify the two maps and write $f^*$ for both.
The [[transpose|0W809K6AW0]] of a matrix is the matrix of the dual map in dual bases for every basis, but it is the matrix of the adjoint only in orthonormal bases.

## Explanations

### L1 human

The dual map and the adjoint are two different ways to reverse a linear map.
The dual map acts on measuring rules and needs nothing extra.
The adjoint acts on vectors, and it needs a way to measure lengths and angles, an inner product.
With the usual dot product the two have the same matrix.
With the inner product $v_1 w_1 + 2 v_2 w_2$, the example shows a map where they differ.

### L2 human

Here is the general recipe for an inner product $\langle v, w \rangle = v^{\mathsf{T}} G w$ on $\R^n$.
Write the condition $\langle A v, w \rangle = \langle v, M w \rangle$ as $v^{\mathsf{T}} A^{\mathsf{T}} G w = v^{\mathsf{T}} G M w$, and solve:
$$M = G^{-1} A^{\mathsf{T}} G.$$
Compare with $A^{\mathsf{T}}$, the matrix of the dual map.
The two agree for every $A$ exactly when $G$ commutes with every $A^{\mathsf{T}}$, which forces $G$ to be a positive multiple of $I$.
Watch out: older books write $f^*$ for both maps, so check which one is meant before you use a formula.
