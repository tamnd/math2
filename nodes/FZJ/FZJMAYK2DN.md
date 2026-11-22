---
tag: FZJMAYK2DN
kind: example
name: Dodgson condensation of a 4 × 4 matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
instance_of: [RQ44FKS5QM]
uses: [F7D849A4RZ, 541X51GQTV, KWW7519E58]
sources:
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
---

## Example

Let
$$M = \begin{pmatrix} 2 & 1 & 3 & 1 \\ 1 & 2 & 1 & 3 \\ 3 & 1 & 2 & 1 \\ 1 & 3 & 1 & 2 \end{pmatrix}$$
over $\mathbb{Q}$.
We follow the [[definition of condensation|F7D849A4RZ]] and find $\det M = 21$ in three steps.

1. Step 1 takes the $2 \times 2$ determinant of each block of four neighboring entries.
   In the first two rows the three blocks give $2 \cdot 2 - 1 \cdot 1 = 3$, then $1 \cdot 1 - 3 \cdot 2 = -5$, then $3 \cdot 3 - 1 \cdot 1 = 8$.
   Rows $2, 3$ give $-5, 3, -5$, and rows $3, 4$ give $8, -5, 3$ in the same way, so
$$M^{(1)} = \begin{pmatrix} 3 & -5 & 8 \\ -5 & 3 & -5 \\ 8 & -5 & 3 \end{pmatrix}.$$
2. Step 2 takes the four connected $2 \times 2$ determinants of $M^{(1)}$ and divides each by the matching entry of the interior of $M$, which is $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$:
$$\frac{3 \cdot 3 - (-5)(-5)}{2} = -8, \quad \frac{(-5)(-5) - 8 \cdot 3}{1} = 1, \quad \frac{(-5)(-5) - 3 \cdot 8}{1} = 1, \quad \frac{3 \cdot 3 - (-5)(-5)}{2} = -8.$$
   So
$$M^{(2)} = \begin{pmatrix} -8 & 1 \\ 1 & -8 \end{pmatrix}.$$
3. Step 3 takes the determinant of $M^{(2)}$ and divides it by the interior of $M^{(1)}$, which is the single entry $3$:
$$M^{(3)} = \frac{(-8)(-8) - 1 \cdot 1}{3} = \frac{63}{3} = 21.$$
4. So condensation gives $\det M = 21$.

## Remarks

### A check by another method

The [[general Laplace expansion|541X51GQTV]] along rows $1$ and $2$ has one term for each pair of columns.
Each term is a signed product of a $2 \times 2$ minor from rows $1, 2$ and the complementary minor from rows $3, 4$:
$$3 \cdot 3 - (-1)(-1) + 5 \cdot (-5) + (-5) \cdot 5 - 1 \cdot 1 + 8 \cdot 8 = 9 - 1 - 25 - 25 - 1 + 64 = 21.$$
The pairs of columns are taken in the order $\{1, 2\}, \{1, 3\}, \{1, 4\}, \{2, 3\}, \{2, 4\}, \{3, 4\}$, with the signs $+, -, +, +, -, +$.
The two methods agree.

### What the example shows

Every division in steps 2 and 3 is exact, as the [[Desnanot-Jacobi identity|KWW7519E58]] predicts, because each quotient is a connected minor of $M$.
For example, the entry $-8$ in the top left of $M^{(2)}$ is the top left $3 \times 3$ minor of $M$, and expansion along its first row gives $2 \cdot 3 - 1 \cdot (-1) + 3 \cdot (-5) = -8$.

### What changes when an entry changes

If the entry $2$ in position $(2, 2)$ of $M$ is replaced by $0$, then the first division of step 2 is by $0$, and the method stops with $0/0$.
The [[non-example|AD6GEXKCB1]] shows this failure on a $3 \times 3$ matrix and repairs it by moving a row.

## Explanations

### L1 human

Condensation turns a $4 \times 4$ table into a $3 \times 3$ table, then a $2 \times 2$ table, and then a single number.
Each new number is a small $2 \times 2$ determinant of neighbors.
From the second round on, it is divided by a number from two rounds back.
Here the last number is $21$, and it is the determinant.

### L2 human

The typical use is a hand computation for an integer matrix whose interior has no zero entry.
Since the divisions are exact, a fraction at any step tells you that an earlier step has an arithmetic error.
Watch out: in step 2 the divisors come from $M$ itself, two steps back, and not from $M^{(1)}$; dividing the first entry by the central entry $3$ of $M^{(1)}$ would give the fraction $-16/3$.
