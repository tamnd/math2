---
tag: ZD5XSYAT9W
kind: example
name: The inverse of a 3 by 3 matrix from its characteristic polynomial
msc: ["15A24", "15A09"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [R4CPYXFJEQ]
illustrates: [0F765KFC2J]
uses: [R4CPYXFJEQ, 0F765KFC2J, 039HF58KQ5, 0FRYPZ6D0X]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: Determinant and inverse matrix
  - book: isbn:9780134860244
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 & 0 \\ -1 & 3 & 0 \\ -1 & 1 & 1 \end{pmatrix},$$
the matrix of the [[3 by 3 example with a defective eigenvalue|18XQY67HMS]].
We find $A^{-1}$ by the method of [[inverse and powers by the Cayley-Hamilton theorem|R4CPYXFJEQ]].

1. The [[coefficients of the characteristic polynomial|0FRYPZ6D0X]] come from the trace, the principal $2 \times 2$ minors and the determinant.
   The trace is $1 + 3 + 1 = 5$.
   The principal minors are $1 \cdot 3 - 1 \cdot (-1) = 4$, then $1 \cdot 1 - 0 = 1$, then $3 \cdot 1 - 0 = 3$, with sum $8$.
   Expanding along the third column gives $\det A = 1 \cdot (3 + 1) = 4$.
2. So
$$p_A(t) = t^3 - 5t^2 + 8t - 4 = (t - 1)(t - 2)^2.$$
   Check: $(t - 1)(t^2 - 4t + 4) = t^3 - 5t^2 + 8t - 4$.
3. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^3 - 5A^2 + 8A - 4I = 0$, so $A (A^2 - 5A + 8I) = 4I$.
4. Square the matrix, row by column:
$$A^2 = \begin{pmatrix} 0 & 4 & 0 \\ -4 & 8 & 0 \\ -3 & 3 & 1 \end{pmatrix}.$$
5. Combine:
$$A^2 - 5A + 8I = \begin{pmatrix} 0 - 5 + 8 & 4 - 5 & 0 \\ -4 + 5 & 8 - 15 + 8 & 0 \\ -3 + 5 & 3 - 5 & 1 - 5 + 8 \end{pmatrix} = \begin{pmatrix} 3 & -1 & 0 \\ 1 & 1 & 0 \\ 2 & -2 & 4 \end{pmatrix}.$$
6. Divide by $4$:
$$A^{-1} = \tfrac{1}{4}(A^2 - 5A + 8I) = \begin{pmatrix} \tfrac{3}{4} & -\tfrac{1}{4} & 0 \\ \tfrac{1}{4} & \tfrac{1}{4} & 0 \\ \tfrac{1}{2} & -\tfrac{1}{2} & 1 \end{pmatrix}.$$
7. Check the rows of $A A^{-1}$.
   Row 1 is $(\tfrac{3}{4} + \tfrac{1}{4}, -\tfrac{1}{4} + \tfrac{1}{4}, 0) = (1, 0, 0)$.
   Row 2 is $(-\tfrac{3}{4} + \tfrac{3}{4}, \tfrac{1}{4} + \tfrac{3}{4}, 0) = (0, 1, 0)$.
   Row 3 is $(-\tfrac{3}{4} + \tfrac{1}{4} + \tfrac{1}{2}, \tfrac{1}{4} + \tfrac{1}{4} - \tfrac{1}{2}, 1) = (0, 0, 1)$.
   So $A A^{-1} = I$.

## Remarks

The constant term of $p_A$ is $-4 = (-1)^3 \det A$, and the sign comes from the odd size $n = 3$.
If you divide by $-4$ in step 6, you get $-A^{-1}$, and the check in step 7 gives $-I$.

The inverse needs $A^2$, and no formula of the form $aA + bI$ can work.
Such a formula would give $aA^2 + bA - I = 0$, a nonzero polynomial of degree at most $2$ that kills $A$.
But the eigenvalue $2$ is defective here, so the minimal polynomial is all of $(t - 1)(t - 2)^2$, of degree $3$.
For a matrix such as $\operatorname{diag}(1, 2, 2)$, with the same characteristic polynomial but minimal polynomial $(t - 1)(t - 2)$, the inverse is a combination of $A$ and $I$ alone: $A^{-1} = \tfrac{1}{2}(3I - A)$.

## Explanations

### L1 human

The characteristic polynomial gives the equation $A^3 - 5A^2 + 8A = 4I$.
Every term on the left has a factor $A$, so you can pull it out: $A$ times $(A^2 - 5A + 8I)$ equals $4I$.
Dividing by $4$ gives the inverse, and the only product you need is $A^2$.

### L2 human

The typical use is to invert a $3 \times 3$ matrix when $A^2$ is easy to compute, or to show that $A^{-1}$ is a polynomial in $A$.
The work is one matrix product, one linear combination and one division.
Watch out for the sign of the constant term: for odd $n$ it is $-\det A$, and confusing it with $\det A$ gives the negative of the inverse.
