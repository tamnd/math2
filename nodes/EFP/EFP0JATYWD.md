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

We multiply by a block triangular matrix to get the identity up to a factor $\det D$, and then we cancel that factor with the help of a polynomial variable.

1. Let $A, B, C, D$ be $n \times n$ matrices over the commutative ring $K$ with $CD = DC$, and let $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$.
   Let $N = \begin{pmatrix} D & 0 \\ -C & I_n \end{pmatrix}$.
2. Block matrices with the same splitting multiply block by block, by the definition of the [[matrix product|076JGP6R3T]].
   So
$$MN = \begin{pmatrix} AD - BC & B \\ CD - DC & D \end{pmatrix} = \begin{pmatrix} AD - BC & B \\ 0 & D \end{pmatrix},$$
   where the second equality uses $CD = DC$.
3. Both $N$ and $MN$ are block triangular.
   So the [[block triangular rule|0J9TVTNB4K]] gives $\det N = \det D \cdot \det I_n = \det D$ and $\det(MN) = \det(AD - BC) \det D$.
4. By [[multiplicativity|04CPJ6AF00]], $\det(MN) = \det M \cdot \det N$, so
$$\det M \cdot \det D = \det(AD - BC) \cdot \det D.$$
   If $\det D$ is a unit of $K$, we can cancel it, and we are done.
   In general we cannot, so we change $D$.
5. Let $x$ be a variable, and work in the [[polynomial ring|0Q9EZS90GY]] $K[x]$, which is commutative.
   Let $D_x = D + x I_n$.
   Then $C D_x = CD + xC = DC + xC = D_x C$, so $C$ and $D_x$ commute.
6. Steps 1 to 4 hold over $K[x]$ for $M_x = \begin{pmatrix} A & B \\ C & D_x \end{pmatrix}$.
   They give
$$\det M_x \cdot \det D_x = \det(A D_x - BC) \cdot \det D_x \quad \text{in } K[x].$$
7. In the [[Leibniz formula|016PE4VZ8Q]] for $\det D_x$, every entry of $D_x$ off the diagonal is a constant, and every diagonal entry has degree $1$ with leading coefficient $1$.
   So only the identity permutation gives a term of degree $n$, and $\det D_x = x^n + (\text{terms of lower degree})$ is a monic polynomial.
8. A monic polynomial is not a [[zero divisor|0K26YKNBSA]] in $K[x]$.
   Indeed, if $q \ne 0$ has leading term $c x^m$ with $c \ne 0$, then $(\det D_x)\, q$ has the term $c x^{n+m}$ of top degree, so it is not $0$.
9. Since $\det D_x$ is not a zero divisor, we can cancel it in step 6:
$$\det M_x = \det(A D_x - BC) \quad \text{in } K[x].$$
10. Evaluation at $x = 0$ is a ring homomorphism $K[x] \to K$.
   It sends $M_x$ to $M$ and $A D_x - BC$ to $AD - BC$.
11. By the [[naturality of the determinant|03Q7RE2HXR]] under ring homomorphisms, evaluation commutes with $\det$.
   So step 9 at $x = 0$ gives $\det M = \det(AD - BC)$.

## Idea

Multiplying $M$ on the right by $\begin{pmatrix} D & 0 \\ -C & I \end{pmatrix}$ clears the lower left block, because $C$ and $D$ commute.
The price is an extra factor $\det D$ on both sides of the identity.
When $\det D$ can be cancelled, we are done.
To make it cancellable in every case, replace $D$ by $D + xI$, whose determinant is a monic polynomial and so never a zero divisor.
Then set $x = 0$ to return to $D$.

For example, $D = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ is singular, but $\det(D + xI) = (1 + x)x = x^2 + x$ is monic and can be cancelled in $K[x]$.

## Variants

Over an infinite field there is a shorter way to remove the hypothesis that $D$ is invertible.
The polynomial $\det(D + tI)$ in $t$ has degree $n$, so it has at most $n$ roots, and $D + tI$ is invertible for all other $t$.
For those $t$, steps 1 to 4 give $\det M_t = \det(A(D + tI) - BC)$.
Both sides are polynomials in $t$ that agree at infinitely many points, so they are equal, and $t = 0$ gives the result.
Over $\mathbb{R}$ or $\mathbb{C}$ the same idea can be phrased as continuity: let $t$ tend to $0$.
