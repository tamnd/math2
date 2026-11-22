---
tag: 3WPWGE036Q
kind: proof
name: Proof of multiplicativity of the determinant by elementary matrices
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 04CPJ6AF00
methods: [0WCP0PVET6, DX2H7AD66G]
uses: [09YB3WQG38, 0K4VQB7HWR, F7F6AA3XQ7, FCM29NQ6DN, 0WF5AQYTW6, 0M79HRJCRR, 0Z4BWARC38]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Gaussian elimination
---

## Proof

We prove the rule first when $A$ is an elementary matrix, then write a general $A$ as a product of elementary matrices and its reduced row echelon form, and treat the two possible echelon forms separately.
This proof works over a field $F$; the [[proof by uniqueness|86J5B0YFNK]] covers every commutative ring.

*The rule for one elementary matrix.*

1. Let $E$ be an [[elementary matrix|0M79HRJCRR]] and let $M$ be any $n \times n$ matrix.
   By [[part 1 of the row operation lemma|F7F6AA3XQ7]], the product $EM$ arises from $M$ by one row operation.
2. By the [[effect of row operations|09YB3WQG38]], $\det(EM) = \kappa \det M$.
   Here $\kappa = -1$ for a swap of two rows, $\kappa = c$ for scaling a row by $c \ne 0$, and $\kappa = 1$ for adding a multiple of one row to another.
3. Take $M = I_n$ in step 2.
   By the [[determinant of the identity|0Z4BWARC38]], $\det I_n = 1$, so $\det E = \kappa$.
   Hence $\det(EM) = \det E \det M$ for every $M$.

*Reduction to the echelon form.*

4. By the [[existence of the reduced row echelon form|FCM29NQ6DN]], there are elementary matrices $E_1, \dots, E_k$ with $E_k \cdots E_1 A = R$, where $R$ is in [[reduced row echelon form|0WF5AQYTW6]].
5. By part 2 of the row operation lemma, each $E_r$ has an elementary inverse.
   So $A = G_1 G_2 \cdots G_k R$, where $G_r = E_r^{-1}$ is elementary.
6. Applying step 3 $k$ times gives
$$\det(AB) = \det G_1 \cdots \det G_k \, \det(RB).$$
7. The same computation with $B = I_n$ gives
$$\det A = \det G_1 \cdots \det G_k \, \det R.$$

*The two cases for $R$.*

8. Suppose $R = I_n$.
   Then $\det(RB) = \det B$ and $\det R = 1$, so steps 6 and 7 give $\det(AB) = \det A \det B$.
9. Suppose $R \ne I_n$.
   A square matrix in reduced row echelon form with $n$ pivots has its pivots on the diagonal, so it equals $I_n$.
   Hence $R$ has fewer than $n$ pivots, and its last row is zero.
10. Row $n$ of $RB$ is row $n$ of $R$ times $B$, so it is zero as well.
11. By the rule for a [[zero row|0K4VQB7HWR]], $\det R = 0$ and $\det(RB) = 0$.
12. Steps 6 and 7 then give $\det A = 0$ and $\det(AB) = 0$.
    So $\det(AB) = 0 = \det A \det B$.

In both cases $\det(AB) = \det A \det B$.

## Idea

For one elementary matrix, the product rule is just the effect of one row operation on the determinant.
Row reduction writes any $A$ as a product of elementary matrices times its reduced echelon form $R$, so the rule for $A$ reduces to the rule for $R$.
Either $R$ is the identity, and there is nothing left to prove, or $R$ has a zero row, and then both sides are $0$.

## Variants

This proof does not use the [[invertibility criterion|FBSAPTP1PR]]; it shows directly that $\det A = 0$ when $R \ne I_n$.
To pass from fields to an integral domain, embed the domain in its field of fractions.
For an arbitrary commutative ring, use the generic matrix argument.
Both sides of the rule are polynomials with integer coefficients in the entries $x_{ij}$ of $A$ and $y_{ij}$ of $B$.
The rule holds for matrices over the field $\mathbb{Q}(x_{ij}, y_{ij})$, so the two polynomials are equal in $\mathbb{Z}[x_{ij}, y_{ij}]$, and substituting entries from any commutative ring gives the rule there.
