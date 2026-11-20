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
We find $A^{-1}$ by the method of [[inverse and powers by the Cayley-Hamilton theorem|R4CPYXFJEQ]].

1. $\tr A = 5$ and $\det A = 4 - 6 = -2$. So $p_A(t) = t^2 - 5t - 2$.
2. Second method: $\det(tI - A) = (t - 1)(t - 4) - 6 = t^2 - 5t - 2$.
3. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^2 - 5A - 2I = 0$.
4. Rewrite this as $A(A - 5I) = 2I$. So $A \cdot \frac{1}{2}(A - 5I) = I$.
5. Hence $A^{-1} = \frac{1}{2}(A - 5I) = \frac{1}{2}\begin{pmatrix} -4 & 2 \\ 3 & -1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$.
6. Check: $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix} = \begin{pmatrix} -2 + 3 & 1 - 1 \\ -6 + 6 & 3 - 2 \end{pmatrix} = I$.
7. Second check, by the [[inverse in terms of the adjugate|0ENVM493VK]]: $A^{-1} = \frac{1}{-2}\begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}$, which is the same matrix.

## Remarks

- For every invertible $2 \times 2$ matrix, the method gives $A^{-1} = \frac{1}{\det A}\big((\tr A)I - A\big)$. This is the adjugate formula.
- The constant term of $p_A$ is $-2 = \det A$ here, because $n = 2$ is even.

## Explanations

### L1 human

The Cayley-Hamilton theorem gives the equation $A^2 - 5A - 2I = 0$.
Moving $2I$ to the other side and factoring out $A$ gives $A$ times a matrix equal to $2I$.
Dividing by $2$ gives the inverse.

### L2 human

The typical use is a quick inverse of a small matrix without row reduction.
A trap is to forget the identity matrix, and write $A - 5$ instead of $A - 5I$.
