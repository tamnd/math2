---
tag: EVM25ZY7BV
kind: example
name: Two upper triangular 2 × 2 matrices that commute
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [8G3X8MPG7E]
illustrates: [DS9TS6AFMW]
uses: [MX26N71ZD3, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: Examples
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix}$$
over $\mathbb{R}$.
We check that $A$ and $B$ commute, and then that the square formula from school algebra holds for them.

1. Multiply in the first order:
$$AB = \begin{pmatrix} 1 \cdot 3 + 2 \cdot 0 & 1 \cdot 5 + 2 \cdot 3 \\ 0 \cdot 3 + 1 \cdot 0 & 0 \cdot 5 + 1 \cdot 3 \end{pmatrix} = \begin{pmatrix} 3 & 11 \\ 0 & 3 \end{pmatrix}.$$
2. Multiply in the other order:
$$BA = \begin{pmatrix} 3 \cdot 1 + 5 \cdot 0 & 3 \cdot 2 + 5 \cdot 1 \\ 0 \cdot 1 + 3 \cdot 0 & 0 \cdot 2 + 3 \cdot 1 \end{pmatrix} = \begin{pmatrix} 3 & 11 \\ 0 & 3 \end{pmatrix}.$$
3. So $AB = BA$, and $A$ and $B$ [[commute|MX26N71ZD3]].
4. Now check the [[binomial theorem|DS9TS6AFMW]] for $m = 2$. The sum is $A + B = \begin{pmatrix} 4 & 7 \\ 0 & 4 \end{pmatrix}$, and
$$(A + B)^2 = \begin{pmatrix} 16 & 4 \cdot 7 + 7 \cdot 4 \\ 0 & 16 \end{pmatrix} = \begin{pmatrix} 16 & 56 \\ 0 & 16 \end{pmatrix}.$$
5. The three terms are $A^2 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$, $2AB = \begin{pmatrix} 6 & 22 \\ 0 & 6 \end{pmatrix}$ and $B^2 = \begin{pmatrix} 9 & 30 \\ 0 & 9 \end{pmatrix}$.
6. Their sum is
$$A^2 + 2AB + B^2 = \begin{pmatrix} 1 + 6 + 9 & 4 + 22 + 30 \\ 0 & 1 + 6 + 9 \end{pmatrix} = \begin{pmatrix} 16 & 56 \\ 0 & 16 \end{pmatrix},$$
which agrees with step 4.

## Remarks

The reason for the commuting is that $A = I + 2E_{12}$ and $B = 3I + 5E_{12}$ are both polynomials in the one [[matrix unit|A4HTT7JFD1]] $E_{12}$.
Every two matrices of the form $aI + bE_{12}$ commute, and their product is $(aI + bE_{12})(cI + dE_{12}) = ac I + (ad + bc) E_{12}$, because $E_{12}^2 = 0$.
Check: $a = 1$, $b = 2$, $c = 3$, $d = 5$ gives $3I + 11 E_{12}$, as in step 1.

If we change one diagonal entry, the commuting can break.
For $B' = \begin{pmatrix} 3 & 5 \\ 0 & 4 \end{pmatrix}$ the top right entries are $1 \cdot 5 + 2 \cdot 4 = 13$ in $AB'$ and $3 \cdot 2 + 5 \cdot 1 = 11$ in $B'A$.
Compare [[this non-example|60W7PZXBVB]], where the matrices do not commute and the square formula fails.

## Explanations

### L1 human

These two matrices can be multiplied in either order with the same result, $\begin{pmatrix} 3 & 11 \\ 0 & 3 \end{pmatrix}$.
So the usual square formula $(a + b)^2 = a^2 + 2ab + b^2$ works for them, and step 6 confirms it.

### L2 human

Both matrices have the form $aI + bE_{12}$, a scalar part plus a nilpotent part.
Two such matrices commute, because $I$ commutes with everything and $E_{12}$ commutes with itself.
Watch out: upper triangular matrices in general do not commute, as the matrix $B'$ in the Remarks shows; here it works because both diagonals are constant.
