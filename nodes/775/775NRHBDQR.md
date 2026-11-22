---
tag: 775NRHBDQR
kind: example
name: The inverse of a 2 by 2 matrix from its characteristic polynomial
msc: ["15A24", "15A09"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [R4CPYXFJEQ]
illustrates: [0F765KFC2J]
uses: [R4CPYXFJEQ, 0F765KFC2J, 039HF58KQ5, 0ENVM493VK]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: Determinant and inverse matrix
  - book: isbn:9780134860244
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ over $\mathbb{Q}$.
We find $A^{-1}$ by the method of [[inverse and powers by the Cayley-Hamilton theorem|R4CPYXFJEQ]], and then check it two ways.

1. The trace is $1 + 4 = 5$ and the determinant is $4 - 6 = -2$, so $p_A(t) = t^2 - 5t - 2$.
   The [[definition of the characteristic polynomial|039HF58KQ5]] gives the same answer:
$$\det(tI - A) = (t - 1)(t - 4) - 6 = t^2 - 5t - 2.$$
2. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^2 - 5A - 2I = 0$.
3. Move $2I$ to the right and factor out $A$ on the left:
$$A (A - 5I) = 2I, \qquad \text{so} \qquad A \cdot \tfrac{1}{2}(A - 5I) = I.$$
4. Hence
$$A^{-1} = \tfrac{1}{2}(A - 5I) = \tfrac{1}{2} \begin{pmatrix} -4 & 2 \\ 3 & -1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ \tfrac{3}{2} & -\tfrac{1}{2} \end{pmatrix}.$$
5. Check by multiplying:
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} -2 & 1 \\ \tfrac{3}{2} & -\tfrac{1}{2} \end{pmatrix} = \begin{pmatrix} -2 + 3 & 1 - 1 \\ -6 + 6 & 3 - 2 \end{pmatrix} = I.$$
6. Check with the [[inverse by the adjugate|0ENVM493VK]]:
$$A^{-1} = \frac{1}{-2} \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix},$$
   which is the same matrix.

## Remarks

The two answers agree for a reason.
For any invertible $2 \times 2$ matrix the theorem reads $A^2 - (\operatorname{tr} A) A + (\det A) I = 0$, and the same steps give
$$A^{-1} = \frac{1}{\det A} \left( (\operatorname{tr} A) I - A \right).$$
With $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the matrix $(a + d) I - A$ is $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, which is exactly the adjugate.

Here the constant term of $p_A$ is $-2 = \det A$, with no change of sign, because $n = 2$ is even.
If we change the entry $4$ to $6$, the determinant becomes $0$, the polynomial becomes $t^2 - 7t$, and step 3 has no multiple of $I$ to divide by, as in the [[singular example|H7CPHN6GGK]].

## Explanations

### L1 human

The theorem gives the equation $A^2 - 5A - 2I = 0$ for this matrix.
Move the $2I$ to the other side and pull out one factor $A$: you get $A$ times $(A - 5I)$ equals $2I$.
Divide by $2$, and the matrix $\tfrac{1}{2}(A - 5I)$ is the one that undoes $A$.

### L2 human

The typical use is a quick inverse of a small matrix without row reduction, and for size $2$ it is the formula "swap the diagonal, negate the rest, divide by the determinant".
For size $3$ the same idea needs $A^2$, as in the [[3 by 3 example|ZD5XSYAT9W]].
Watch out: do not drop the identity and write $A - 5$; a number cannot be subtracted from a matrix, and the correct term is $A - 5I$.
