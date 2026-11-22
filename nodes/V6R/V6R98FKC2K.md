---
tag: V6R98FKC2K
kind: proof
name: Proof that linear maps correspond to matrices
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
proves: Q3EDKTZ6TA
uses: [0YYMY95FWS, 009892PZ30, 0VPCJWGMP9, 0R8X9XA83A, E2ZRZGXSNX, 059THXBRBB]
methods: [DD2P85Y8E9]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Matrices
---

## Proof

We show that $\Phi$ is linear, then injective, then surjective, and we identify the inverse.
Let $\phi_C \colon W \to F^m$, $w \mapsto [w]_C$, be the coordinate map of $C$.

1. The [[coordinate map|059THXBRBB]] $\phi_C$ is a linear isomorphism.
2. For linearity, let $S, T \in \Hom_F(V, W)$ and $\lambda \in F$; by the [[definition of the matrix|0YYMY95FWS]], column $j$ of $[S + \lambda T]_{C,B}$ is $\phi_C\bigl((S + \lambda T)(b_j)\bigr)$.
3. By the definition of the operations in the [[space of linear maps|0VPCJWGMP9]], $(S + \lambda T)(b_j) = S(b_j) + \lambda\, T(b_j)$.
4. Since $\phi_C$ is linear by step 1,
$$\phi_C\bigl(S(b_j) + \lambda\, T(b_j)\bigr) = \phi_C(S(b_j)) + \lambda\, \phi_C(T(b_j)),$$
and the right side is column $j$ of $[S]_{C,B} + \lambda [T]_{C,B}$.
5. All columns agree, so $\Phi(S + \lambda T) = \Phi(S) + \lambda\, \Phi(T)$, and $\Phi$ is linear.
6. For injectivity, let $\Phi(T) = 0$; then $[T(b_j)]_C = 0$ for each $j$, and $T(b_j) = 0$ by the [[uniqueness of coordinates|E2ZRZGXSNX]].
7. The zero map also sends each $b_j$ to $0$, and a linear map is determined by its values on a basis, by the [[theorem on bases and linear maps|0R8X9XA83A]], so $T = 0$ and $\ker \Phi = \{0\}$.
8. For surjectivity, let $A = (a_{ij})$ be an $m \times n$ matrix; by the same theorem there is a linear map $T_A$ with $T_A(b_j) = \sum_{i=1}^m a_{ij} c_i$ for each $j$, the [[linear map of A|009892PZ30]].
9. Column $j$ of $[T_A]_{C,B}$ is $[T_A(b_j)]_C = (a_{1j}, \dots, a_{mj})$, which is column $j$ of $A$, so $\Phi(T_A) = A$.
10. By steps 5, 7 and 9, $\Phi$ is a bijective linear map, so it is a linear isomorphism, and step 9 shows that its inverse is $A \mapsto T_A$.

## Idea

The matrix of a map lists the coordinates of the images of the basis vectors.
Taking coordinates is linear, so the matrix depends linearly on the map.
The images of a basis can be chosen freely, and they determine the map, so each matrix comes from exactly one map.
In short, a linear map is the same as a free choice of $n$ vectors in $W$, and each vector is the same as a column of $m$ numbers.

## Variants

If the dimension $\dim \Hom_F(V, W) = mn$ is already known from the [[theorem on its dimension|0Z9N1ER0W0]], it is enough to prove linearity and injectivity.
An injective linear map between spaces of the same finite dimension is then bijective.

Another proof writes $\Phi(T)$ as the standard matrix of $\phi_C \circ T \circ \phi_B^{-1} \colon F^n \to F^m$.
The map $T \mapsto \phi_C \circ T \circ \phi_B^{-1}$ is a linear isomorphism $\Hom(V, W) \to \Hom(F^n, F^m)$, with inverse $S \mapsto \phi_C^{-1} \circ S \circ \phi_B$.
The theorem on [[matrix transformations of Fⁿ|W6KB0J3SZZ]] then identifies $\Hom_F(F^n, F^m)$ with $M_{m \times n}(F)$, and $\Phi$ is the composite of the two isomorphisms.
