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

Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

1. $\tr A = 5$ and $\det A = 4 - 4 = 0$. So $p_A(t) = t^2 - 5t$, with constant term $c_0 = 0$.
2. Second method: $\det(tI - A) = (t - 1)(t - 4) - 4 = t^2 - 5t$.
3. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^2 = 5A$. Check: $A^2 = \begin{pmatrix} 5 & 10 \\ 10 & 20 \end{pmatrix} = 5A$.
4. This gives $A(A - 5I) = 0$, with no multiple of $I$ on the right side. So the [[inverse formula|R4CPYXFJEQ]] has nothing to divide by.
5. In fact $A$ has no inverse: $A(2, -1) = (0, 0)$.

## Remarks

- The formula for $A^{-1}$ works exactly when $c_0 = (-1)^n \det A \ne 0$.
- The reduction of powers still works: $A^k = 5^{k-1}A$ for $k \ge 1$.

## Explanations

### L1 human

For this matrix, the Cayley-Hamilton theorem gives $A^2 = 5A$.
There is no constant term to move to the other side.
This matches the fact that $A$ is not invertible.

### L2 human

The typical lesson is to check $c_0 \ne 0$ before using the inverse formula.
A trap is to divide $A^2 = 5A$ by $A$ and conclude $A = 5I$.
