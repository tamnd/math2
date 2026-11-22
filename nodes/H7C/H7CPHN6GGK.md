---
tag: H7CPHN6GGK
kind: example
name: A singular matrix has no inverse from the Cayley-Hamilton theorem
msc: ["15A24", "15A09"]
topics: [6R1D6QPY3S]
audience: ug1
not_instance_of:
  - target: R4CPYXFJEQ
    note: The constant term of the characteristic polynomial is 0, so the Cayley-Hamilton formula for the inverse cannot be used
uses: [R4CPYXFJEQ, 0F765KFC2J, 039HF58KQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: Determinant and inverse matrix
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ over $\mathbb{Q}$.
We show that the [[inverse formula from the Cayley-Hamilton theorem|R4CPYXFJEQ]] breaks down, and that it must.

1. The trace is $5$ and the determinant is $4 - 4 = 0$, so $p_A(t) = t^2 - 5t$, with constant term $c_0 = 0$.
   The [[definition of the characteristic polynomial|039HF58KQ5]] agrees:
$$\det(tI - A) = (t - 1)(t - 4) - 4 = t^2 - 5t.$$
2. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^2 = 5A$.
   Check:
$$A^2 = \begin{pmatrix} 1 + 4 & 2 + 8 \\ 2 + 8 & 4 + 16 \end{pmatrix} = \begin{pmatrix} 5 & 10 \\ 10 & 20 \end{pmatrix} = 5A.$$
3. The equation reads $A (A - 5I) = 0$.
   For an invertible matrix the method would produce $A \cdot X = c I$ with $c \ne 0$, but here the right side has no multiple of $I$, so there is nothing to divide by.
4. The failure is forced, because $A$ has no inverse at all.
   The second column is twice the first, so
$$A \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 - 2 \\ 4 - 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix},$$
   and a matrix that sends a nonzero vector to $0$ cannot be undone.

## Remarks

The formula for $A^{-1}$ works exactly when $c_0 = (-1)^n \det A$ is not zero, so the test $c_0 \ne 0$ is the same as the test $\det A \ne 0$.
Change the entry $4$ to $5$: then $\det A = 1$, the polynomial is $t^2 - 6t + 1$, and the method gives $A^{-1} = 6I - A = \begin{pmatrix} 5 & -2 \\ -2 & 1 \end{pmatrix}$.

The reduction of powers still works for a singular matrix.
From $A^2 = 5A$ we get $A^3 = 5A^2 = 25A$, and in general $A^k = 5^{k-1} A$ for every $k \ge 1$.
The matrix $\tfrac{1}{5} A$ is therefore a projection, since its square is itself.

## Explanations

### L1 human

For this matrix the theorem gives $A^2 = 5A$.
To find an inverse, you would want an equation of the form "$A$ times something equals the identity", and here there is no identity term to isolate.
That matches the fact that $A$ squashes the plane onto a line and so cannot be undone.

### L2 human

The lesson is to check $c_0 \ne 0$, or $\det A \ne 0$, before using the inverse formula.
Watch out for a tempting slip: cancelling $A$ from both sides of $A^2 = 5A$ to conclude $A = 5I$.
Cancelling needs $A^{-1}$, which does not exist, and indeed $A \ne 5I$.
