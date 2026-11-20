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

1. Let $T \colon F^n \to F^n$ be $T(v) = Av$. By the [[cyclic decomposition theorem|R3Z20J19BR]], $F^n = Z(v_1) \oplus \cdots \oplus Z(v_r)$ with monic nonconstant annihilators $d_1 \mid \cdots \mid d_r$.
2. Let $k_i = \deg d_i$. By part 3 of the [[lemma on cyclic subspaces|5VYBJYPYMW]], $v_i, A v_i, \dots, A^{k_i - 1} v_i$ is a basis of $Z(v_i)$.
3. The union $\mathcal{B}$ of these bases, in the order $i = 1, \dots, r$, is a basis of $F^n$, since the sum is direct.
4. Each $Z(v_i)$ is $A$-invariant, so the matrix of $T$ in $\mathcal{B}$ is block diagonal, with the matrix of $T|_{Z(v_i)}$ as the $i$-th block.
5. By part 5 of the lemma on cyclic subspaces, this block is $C(d_i)$. So the matrix of $T$ in $\mathcal{B}$ is $R = C(d_1) \oplus \cdots \oplus C(d_r)$.
6. Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] whose columns are the vectors of $\mathcal{B}$. By the [[change of basis formula|0MQXVZEBMT]], $R = P^{-1} A P$. This proves existence.
7. Uniqueness. Let $A = Q R' Q^{-1}$ with $R' = C(f_1) \oplus \cdots \oplus C(f_s)$, $Q$ invertible, and $f_1 \mid \cdots \mid f_s$ monic and nonconstant.
8. Let $u_j$ be the standard basis vector at the first position of the block $C(f_j)$. By part 1 of the [[theorem on companion matrices|XYR7GPH20K]], the block $j$ coordinates form the cyclic subspace $Z(u_j; R')$. By part 2 of that theorem, the annihilator of $u_j$ is the minimal polynomial $f_j$ of $C(f_j)$.
9. So $F^n = Z(u_1; R') \oplus \cdots \oplus Z(u_s; R')$ with annihilators $f_1 \mid \cdots \mid f_s$.
10. Since $A Q = Q R'$, we have $f(A) Q u = Q f(R') u$ for all $f$ and $u$. So $Q$ maps $Z(u_j; R')$ onto $Z(Q u_j; A)$, and $Q u_j$ has $A$-annihilator $f_j$.
11. So $F^n = Z(Q u_1; A) \oplus \cdots \oplus Z(Q u_s; A)$ with annihilators $f_1 \mid \cdots \mid f_s$.
12. By the uniqueness part of the cyclic decomposition theorem, $s = r$ and $f_j = d_j$ for all $j$. So $R' = R$.
13. By steps 6 and 12, the last two claims of the statement follow from the cyclic decomposition theorem: $d_r = m_A$ and $d_1 \cdots d_r = \chi_A$.
14. Let $A, B \in M_n(F)$. If they have the same rational canonical form $R$, then $A \sim R \sim B$, and $A \sim B$ since [[similarity is an equivalence relation|HWKZ8DM8P0]].
15. If $A \sim B$, the form $R_B$ of $B$ satisfies $A \sim B \sim R_B$, so $R_B$ is a rational canonical form of $A$, and $R_B = R_A$ by step 12.

## Idea

A decomposition into cyclic subspaces gives a basis in which the matrix is a block diagonal matrix of companion matrices.
Conversely, each such block matrix comes with a decomposition of $F^n$ into cyclic subspaces with the same annihilators.
So uniqueness of the form is uniqueness of the invariant factors.

## Variants

With the [[theorem on the characteristic matrix|92VZF0QRM8]], the uniqueness can be proved by the Smith normal form: $xI - C(d)$ has Smith normal form $\operatorname{diag}(1, \dots, 1, d)$, so the form $R$ determines the Smith normal form of $xI - A$, which is unique.
Hoffman and Kunze derive the form from their admissible subspace proof of the cyclic decomposition theorem.
