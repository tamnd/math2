---
tag: ANYDPD4HXZ
kind: object
name: Freudenthal magic square
msc: [17B25, 17C40, 17A35]
uses: [KJ145M3CVT, 1MSMVDRAVD, 57J7MHA8CN, 9QT1JR4KNY, 9YFX87K2VY, 250J3R9W97, G127K65CSX]
sources:
  - url: https://en.wikipedia.org/wiki/Freudenthal_magic_square
same_as:
  wikidata: Q5503261
  wikipedia: Freudenthal magic square
---

## Description

The four real normed division algebras are $\R$, $\C$, $\mathbb{H}$ (quaternions) and $\mathbb{O}$ ([[octonions|KJ145M3CVT]]).
Let $A$ and $B$ be two of them, of dimensions $a$ and $b$.
Let $J = H_3(B)$ be the Jordan algebra of $3 \times 3$ Hermitian matrices over $B$, of dimension $3 + 3b$; for $B = \mathbb{O}$ it is the [[Albert algebra|1MSMVDRAVD]].
Let $A_0$ and $J_0$ be the subspaces of elements of trace zero, of dimensions $a - 1$ and $3b + 2$.
The Tits construction gives a Lie algebra
$$L(A, B) = \operatorname{Der}(A) \oplus (A_0 \otimes J_0) \oplus \operatorname{Der}(J),$$
where $\operatorname{Der}$ denotes the algebra of [[derivations|57J7MHA8CN]].
The magic square lists the complexifications of these Lie algebras, by the type of their Dynkin diagram:

| | $\R$ | $\C$ | $\mathbb{H}$ | $\mathbb{O}$ |
|---|---|---|---|---|
| $\R$ | $A_1$ | $A_2$ | $C_3$ | $F_4$ |
| $\C$ | $A_2$ | $A_2 \times A_2$ | $A_5$ | $E_6$ |
| $\mathbb{H}$ | $C_3$ | $A_5$ | $D_6$ | $E_7$ |
| $\mathbb{O}$ | $F_4$ | $E_6$ | $E_7$ | $E_8$ |

Check of dimensions: $\operatorname{Der}(A)$ has dimension $0, 0, 3, 14$, and $\operatorname{Der}(H_3(B))$ has dimension $3, 8, 21, 52$ for $B = \R, \C, \mathbb{H}, \mathbb{O}$.
For $A = B = \mathbb{O}$ this gives $14 + 7 \cdot 26 + 52 = 248$, the dimension of [[$E_8$|9QT1JR4KNY]].
For $A = \mathbb{H}$ and $B = \mathbb{O}$ it gives $3 + 3 \cdot 26 + 52 = 133$, the dimension of [[$E_7$|9YFX87K2VY]].
For $A = \R$ the middle term vanishes and $L(\R, B) = \operatorname{Der}(H_3(B))$; for $B = \mathbb{O}$ this is [[$F_4$|G127K65CSX]] of dimension $52$.

## Remarks

The square is symmetric in $A$ and $B$, although the Tits construction is not.
Vinberg gave a construction that treats $A$ and $B$ in the same way and so makes the symmetry visible.
The last row and column contain four of the five exceptional Lie algebras: $F_4$, [[$E_6$|250J3R9W97]], $E_7$ and $E_8$.
With the real division algebras as input, the construction gives particular real forms.
For example, the first row consists of the compact algebras $\mathfrak{so}(3)$, $\mathfrak{su}(3)$, $\mathfrak{sp}(3)$ and $\mathfrak{f}_4$, while the other rows contain noncompact real forms.

## Explanations

### L1 human

The magic square is a $4 \times 4$ table of Lie algebras.
Its rows and columns are labelled by the real numbers, the complex numbers, the quaternions and the octonions.
Each entry is built from the two number systems of its row and column.
The surprise is that the table is symmetric, and that the exceptional Lie algebras $F_4$, $E_6$, $E_7$ and $E_8$ appear in the last row.
