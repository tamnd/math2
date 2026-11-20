---
tag: EJRDTJC390
kind: proof
name: Proof that the linear maps from Fⁿ to Fᵐ are the matrix transformations
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: W6KB0J3SZZ
methods: [0NTF6DMVAP, GQHHNV79PA]
uses: [0RJF668P1T, 0CCQV3884B, ZE36VEAY80, 0V7ZD6P7RK, STYEWH8R4E]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Matrices
  - book: isbn:9780321982384
    locator: Section 1.9
---

## Proof

Let $A$ be an $m \times n$ matrix with columns $a_1, \dots, a_n$.

1. By the definition of the [[matrix–vector product|0CCQV3884B]], $Ax = x_1 a_1 + \dots + x_n a_n$ for $x = (x_1, \dots, x_n)$.
2. For $x, y \in F^n$, step 1 gives $A(x + y) = \sum_j (x_j + y_j) a_j = \sum_j x_j a_j + \sum_j y_j a_j = Ax + Ay$.
3. For $c \in F$, step 1 gives $A(cx) = \sum_j (c x_j) a_j = c \sum_j x_j a_j = c\,Ax$.
4. Steps 2 and 3 are the two conditions of a [[linear map|0RJF668P1T]]. So $T_A$ is linear, which is part 1.
5. Now let $T \colon F^n \to F^m$ be linear. Let $A$ be the matrix with columns $T(e_1), \dots, T(e_n)$.
6. Each $x \in F^n$ is $x = x_1 e_1 + \dots + x_n e_n$, by the definition of the [[standard basis|0V7ZD6P7RK]].
7. Part 3 of the [[lemma on linear combinations|STYEWH8R4E]] gives $T(x) = x_1 T(e_1) + \dots + x_n T(e_n)$.
8. By step 1, the right side of step 7 is $Ax$. So $T(x) = Ax$ for each $x$, and this matrix has the form in part 3.
9. For uniqueness, let $B$ be a matrix with $T(x) = Bx$ for all $x$.
10. By step 1, $B e_j$ is the $j$-th column of $B$. Also $B e_j = T(e_j)$, which is the $j$-th column of $A$.
11. So $A$ and $B$ have the same columns, and $A = B$. This proves part 2.

## Idea

Each vector of $F^n$ is a combination of the standard basis vectors with its own entries as coefficients.
A linear map keeps this combination, so it is fixed by the $n$ vectors $T(e_j)$.
Putting these vectors side by side gives the matrix.

## Variants

- Part 1 is also the statement that the [[matrix–vector product is linear|ZE36VEAY80]], proved there entry by entry.
- Part 2 is a special case of the [[theorem on bases|0R8X9XA83A]]: a linear map is fixed by its values on any basis.
