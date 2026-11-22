---
tag: KXT9JRCYRT
kind: proof
name: Proof of the rational canonical form from the cyclic decomposition theorem
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
proves: 042JWAR3Q0
methods: [0NTF6DMVAP]
uses: [R3Z20J19BR, 5VYBJYPYMW, XYR7GPH20K, 0MKRHZB3WS, 0MQXVZEBMT, 027KDW2K72, HWKZ8DM8P0]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
    locator: General case and theory
  - book: isbn:9780135367971
    locator: Section 7.2
---

## Proof

We write the matrix of $A$ in a basis adapted to a cyclic decomposition, and we get uniqueness by turning any block matrix of companion matrices back into a cyclic decomposition.

*Existence.*

1. Let $T \colon F^n \to F^n$ be the map $T(v) = Av$.
   The [[cyclic decomposition theorem|R3Z20J19BR]] gives $F^n = Z(v_1) \oplus \cdots \oplus Z(v_r)$ with monic nonconstant annihilators $d_1 \mid \cdots \mid d_r$.
2. Let $k_i = \deg d_i$.
   By the [[lemma on cyclic subspaces|5VYBJYPYMW]], the vectors $v_i, A v_i, \dots, A^{k_i - 1} v_i$ are a basis of $Z(v_i)$.
3. The union $\mathcal{B}$ of these bases, taken in the order $i = 1, \dots, r$, is a basis of $F^n$, because the sum is direct.
4. Each $Z(v_i)$ is $A$-invariant, so the matrix of $T$ in $\mathcal{B}$ is block diagonal, and its $i$-th block is the matrix of the restriction $T|_{Z(v_i)}$.
5. The same lemma says that this block is the companion matrix $C(d_i)$.
   So the matrix of $T$ in $\mathcal{B}$ is $R = C(d_1) \oplus \cdots \oplus C(d_r)$.
6. Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] whose columns are the vectors of $\mathcal{B}$.
   The [[change of basis formula|0MQXVZEBMT]] gives $R = P^{-1} A P$, which proves existence.

*Uniqueness.*

7. Suppose that $A = Q R' Q^{-1}$ with $Q$ invertible and $R' = C(f_1) \oplus \cdots \oplus C(f_s)$, where $f_1 \mid \cdots \mid f_s$ are monic and nonconstant.
8. Let $u_j$ be the standard basis vector at the first position of the block $C(f_j)$.
   By the [[theorem on companion matrices|XYR7GPH20K]], the first basis vector is a cyclic vector of a companion matrix, so the coordinates of block $j$ form the cyclic subspace $Z(u_j; R')$.
   The same theorem says that the minimal polynomial of $C(f_j)$ is $f_j$, so the annihilator of $u_j$ is $f_j$.
9. So $F^n = Z(u_1; R') \oplus \cdots \oplus Z(u_s; R')$ with annihilators $f_1 \mid \cdots \mid f_s$.
10. From $A Q = Q R'$ we get $A^k Q = Q R'^k$ for every $k$, so $f(A) Q u = Q f(R') u$ for every polynomial $f$ and every vector $u$.
    So $Q$ maps $Z(u_j; R')$ onto $Z(Q u_j; A)$, and $Q u_j$ has the $A$-annihilator $f_j$.
11. Since $Q$ is invertible, step 9 gives $F^n = Z(Q u_1; A) \oplus \cdots \oplus Z(Q u_s; A)$ with annihilators $f_1 \mid \cdots \mid f_s$.
12. The uniqueness part of the cyclic decomposition theorem gives $s = r$ and $f_j = d_j$ for every $j$, so $R' = R$.

*The two polynomials and the similarity criterion.*

13. The cyclic decomposition theorem also says that $d_r = m_A$ and $d_1 \cdots d_r = \chi_A$, and by step 12 these $d_i$ are the polynomials of the form.
14. Let $A, B \in M_n(F)$.
    If they have the same rational canonical form $R$, then $A \sim R$ and $B \sim R$, so $A \sim B$, because [[similarity is an equivalence relation|HWKZ8DM8P0]].
15. If $A \sim B$, let $R_B$ be the form of $B$.
    Then $A \sim B \sim R_B$, so $R_B$ is a rational canonical form of $A$, and step 12 gives $R_B = R_A$.

## Idea

A decomposition into cyclic subspaces hands us a basis, and in that basis the matrix is a block diagonal matrix of companion matrices.
The argument also runs backwards.
Each block matrix of companion matrices comes with its own decomposition into cyclic subspaces, with the polynomials of the blocks as annihilators, and a similarity carries this decomposition over to $A$.
So the uniqueness of the form is the uniqueness of the invariant factors, and nothing more.

## Variants

The [[theorem on the characteristic matrix|92VZF0QRM8]] gives a second proof of uniqueness.
The Smith normal form of $xI - C(d)$ is $\operatorname{diag}(1, \dots, 1, d)$, so the form $R$ fixes the Smith normal form of $xI - R$, which equals that of $xI - A$ and is unique.
Hoffman and Kunze derive the form from their proof of the cyclic decomposition theorem by admissible subspaces, with no modules.
