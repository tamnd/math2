---
tag: 82TX43QDNA
kind: proof
name: Proof of the equivalence of the three definitions of the determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: W3JN0WPZ10
methods: [0ASJVEFA9J, GQHHNV79PA]
uses: [0C3CFHDN6R, 1C8RRWHD45, 016PE4VZ8Q, 0C08BQ3M05, 0ZZQ2E1MTE, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Definitions
---

## Proof

We compare each of $L$, $D_n$ and $\det'$ with the axiomatic $\det$ of the [[theorem|W3JN0WPZ10]]: the first by uniqueness, the second by induction on $n$, and the third by transposition.

*The axiomatic determinant and the Leibniz sum.*

1. By part 1 of the [[existence and uniqueness theorem|1C8RRWHD45]], the sum $L$ is multilinear and alternating in the rows, and $L(I_n) = 1$.
2. By the [[definition|0C3CFHDN6R]], $\det$ is the only function with these three properties.
   So $\det A = L(A)$ for every $A$, which is the [[Leibniz formula|016PE4VZ8Q]].

*The axiomatic determinant and the Laplace recursion.*
We prove $D_n(A) = \det A$ for all $A \in M_n(K)$ by induction on $n$.

3. Let $n = 1$.
   Linearity in the single row gives $\det(a) = a \det(1) = a$, so $\det = D_1$.
4. Let $n \ge 2$, and assume that $D_{n-1}(B) = \det B$ for every $(n-1) \times (n-1)$ matrix $B$.
5. The [[Laplace expansion|0C08BQ3M05]] along row $1$ gives
$$\det A = \sum_{j=1}^n (-1)^{1+j} a_{1j} \det A_{1j}.$$
6. The induction hypothesis gives $\det A_{1j} = D_{n-1}(A_{1j})$ for each $j$.
7. Substituting step 6 into step 5 gives
$$\det A = \sum_{j=1}^n (-1)^{1+j} a_{1j}\, D_{n-1}(A_{1j}) = D_n(A).$$

*Rows and columns.*

8. Define $C(A) = \det(A^{\mathsf{T}})$, where $A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]].
   The columns of $A$ are the rows of $A^{\mathsf{T}}$, so $C$ is multilinear and alternating in the columns of $A$.
   Also $C(I_n) = \det I_n = 1$, since $I_n^{\mathsf{T}} = I_n$.
   So a function $\det'$ with the column properties exists.
9. Now let $\det'$ be any function that is multilinear and alternating in the columns, with $\det'(I_n) = 1$.
   Define $E(B) = \det'(B^{\mathsf{T}})$.
10. The rows of $B$ are the columns of $B^{\mathsf{T}}$, so $E$ is multilinear and alternating in the rows of $B$.
    Also $E(I_n) = \det'(I_n) = 1$.
11. By the uniqueness in the definition of $\det$, we get $E = \det$.
    So $\det'(A) = E(A^{\mathsf{T}}) = \det(A^{\mathsf{T}})$, using $(A^{\mathsf{T}})^{\mathsf{T}} = A$.
12. By the [[determinant of the transpose|0ZZQ2E1MTE]], $\det(A^{\mathsf{T}}) = \det A$.
    So $\det'(A) = \det A$, and in particular $\det'$ is unique.

Steps 2, 7 and 12 give $\det A = L(A) = D_n(A) = \det'(A)$.

## Idea

The rules single out one function, and the Leibniz sum obeys the rules, so the two must agree.
The Laplace expansion along the first row is a theorem about $\det$, and induction on $n$ turns that theorem into the recursive definition.
Transposition swaps rows and columns, so the column rules describe the function $A \mapsto \det A^{\mathsf{T}}$, and the transpose rule says that this is $\det A$ again.

## Variants

We can also start from the recursion and prove by induction that $D_n$ is multilinear, alternating and equal to $1$ on $I_n$.
Then uniqueness gives $D_n = \det$ at once.
This route is longer, because the alternating property for two equal rows that include row $1$ needs a separate argument.
Another route avoids the transpose rule: apply part 2 of the existence and uniqueness theorem to columns, which shows directly that the column version is again the Leibniz sum, now with $a_{\sigma(1) 1} \cdots a_{\sigma(n) n}$, and reindex by $\sigma^{-1}$.
