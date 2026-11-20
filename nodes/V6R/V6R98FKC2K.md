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

Let $\phi_C \colon W \to F^m$, $w \mapsto [w]_C$, be the coordinate map of $C$.

1. The [[coordinate map|059THXBRBB]] $\phi_C$ is linear.
2. Linearity of $\Phi$. Let $S, T \in \Hom_F(V, W)$ and $\lambda \in F$. Column $j$ of $[S + \lambda T]_{C,B}$ is $\phi_C\bigl((S + \lambda T)(b_j)\bigr)$, by the [[definition of the matrix|0YYMY95FWS]].
3. By the definition of the operations in the [[space of linear maps|0VPCJWGMP9]], $(S + \lambda T)(b_j) = S(b_j) + \lambda T(b_j)$.
4. By step 1, $\phi_C\bigl(S(b_j) + \lambda T(b_j)\bigr) = \phi_C(S(b_j)) + \lambda\, \phi_C(T(b_j))$. This is column $j$ of $[S]_{C,B} + \lambda [T]_{C,B}$.
5. So $\Phi(S + \lambda T) = \Phi(S) + \lambda \Phi(T)$, and $\Phi$ is linear.
6. Injectivity. Let $\Phi(T) = 0$. Then $[T(b_j)]_C = 0$ for each $j$. By the [[uniqueness of coordinates|E2ZRZGXSNX]], $T(b_j) = 0$ for each $j$.
7. The zero map also sends each $b_j$ to $0$. A linear map is determined by the images of a basis, by the [[theorem on bases and linear maps|0R8X9XA83A]]. So $T = 0$, and $\ker \Phi = \{0\}$.
8. Surjectivity. Let $A = (a_{ij})$ be an $m \times n$ matrix. By the same theorem, there is a linear map $T_A$ with $T_A(b_j) = \sum_{i=1}^m a_{ij} c_i$ for each $j$. This is the [[linear map of $A$|009892PZ30]].
9. Column $j$ of $[T_A]_{C,B}$ is $[T_A(b_j)]_C = (a_{1j}, \dots, a_{mj})$, which is column $j$ of $A$. So $\Phi(T_A) = A$.
10. By steps 5, 7 and 9, $\Phi$ is a bijective linear map, so it is a linear isomorphism. By step 9 and injectivity, its inverse is $A \mapsto T_A$.

## Idea

The matrix of a map lists the coordinates of the images of the basis vectors.
Coordinates are linear, so the matrix depends linearly on the map.
The images of a basis may be chosen freely and determine the map, so each matrix comes from exactly one map.

## Variants

- One can prove only injectivity and then compare dimensions, if $\dim \Hom_F(V, W) = mn$ is known from the [[theorem on its dimension|0Z9N1ER0W0]].
- One can also write $\Phi(T) = \phi_C \circ T \circ \phi_B^{-1}$, viewed as a map $F^n \to F^m$. Then $\Phi$ is a composition of two isomorphisms, and the [[matrix transformations of $F^n$|W6KB0J3SZZ]] identify $\Hom_F(F^n, F^m)$ with $M_{m \times n}(F)$.
