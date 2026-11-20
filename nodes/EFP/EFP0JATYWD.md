---
tag: EFP0JATYWD
kind: proof
name: Proof of the block determinant with commuting blocks
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: T4TRMJHX3S
methods: [0NTF6DMVAP]
uses: [01AXG9KZQF, 076JGP6R3T, 0J9TVTNB4K, 04CPJ6AF00, 016PE4VZ8Q, 03Q7RE2HXR, 0Q9EZS90GY, 0K26YKNBSA]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Determinant
---

## Proof

We multiply by a block triangular matrix, and we remove the need for $\det D$ to be cancellable with a polynomial variable.

1. Let $A, B, C, D$ be $n \times n$ over the commutative ring $K$ with $CD = DC$, and let $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$.
2. Let $N = \begin{pmatrix} D & 0 \\ -C & I_n \end{pmatrix}$.
3. Block matrices multiply block by block, by the definition of the [[matrix product|076JGP6R3T]].
4. So $MN = \begin{pmatrix} AD - BC & B \\ CD - DC & D \end{pmatrix} = \begin{pmatrix} AD - BC & B \\ 0 & D \end{pmatrix}$, since $CD = DC$.
5. By the [[block triangular rule|0J9TVTNB4K]], $\det N = \det D$ and $\det(MN) = \det(AD - BC) \det D$.
6. By [[multiplicativity|04CPJ6AF00]], $\det M \cdot \det D = \det(AD - BC) \cdot \det D$.
7. Now let $x$ be a variable, and work in the [[polynomial ring|0Q9EZS90GY]] $K[x]$.
8. Let $D_x = D + x I_n$; then $C D_x = CD + xC = DC + xC = D_x C$.
9. Steps 1 to 6 hold over $K[x]$ for $M_x = \begin{pmatrix} A & B \\ C & D_x \end{pmatrix}$, so $\det M_x \det D_x = \det(A D_x - BC) \det D_x$.
10. In the [[Leibniz formula|016PE4VZ8Q]] for $\det D_x$, only the identity permutation gives degree $n$ in $x$.
11. So $\det D_x = x^n + (\text{terms of lower degree})$ is a monic polynomial.
12. Let $q \ne 0$ in $K[x]$, with leading term $c x^m$ and $c \ne 0$.
13. Then $(\det D_x)\, q$ has the term $c x^{n+m}$, so it is not $0$.
14. So $\det D_x$ is not a [[zero divisor|0K26YKNBSA]], and step 9 gives $\det M_x = \det(A D_x - BC)$ in $K[x]$.
15. Evaluation at $x = 0$ is a ring homomorphism $K[x] \to K$ that sends $M_x$ to $M$ and $A D_x - BC$ to $AD - BC$.
16. By [[naturality of the determinant|03Q7RE2HXR]] under ring homomorphisms, $\det M = \det(AD - BC)$.

## Idea

Multiplying $M$ on the right by $\begin{pmatrix} D & 0 \\ -C & I \end{pmatrix}$ makes it block triangular, at the cost of a factor $\det D$.
To cancel this factor, replace $D$ by $D + xI$, whose determinant is monic, and then set $x = 0$.

## Variants

Over a field, an alternative to steps 7 to 16 is continuity or a finite-set argument: $\det(D + tI) \ne 0$ for all but $n$ values of $t$.
Both sides are polynomials in $t$ that agree at infinitely many points when the field is infinite, so they agree at $t = 0$.
