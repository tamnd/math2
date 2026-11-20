---
tag: 7YSM0NJQX1
kind: example
name: A 3 × 3 determinant by three methods
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [00KDZRW4C0]
uses: [016PE4VZ8Q, 0C08BQ3M05, 09YB3WQG38, 0K1KKMFHYH, W3JN0WPZ10]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: 3 × 3 matrices
---

## Example

Let $A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 2 \end{pmatrix}$ over $\mathbb{Q}$.
We compute $\det A$ by the three definitions of the [[equivalence theorem|W3JN0WPZ10]].

**Leibniz formula.**

1. The [[Leibniz formula|016PE4VZ8Q]] has one term for each $\sigma \in S_3$, of the form $\sgn(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} a_{3 \sigma(3)}$.
2. Even permutations: the identity gives $2 \cdot 3 \cdot 2 = 12$; $(1\,2\,3)$ gives $a_{12} a_{23} a_{31} = 0 \cdot 2 \cdot 1 = 0$; $(1\,3\,2)$ gives $a_{13} a_{21} a_{32} = 1 \cdot 1 \cdot 1 = 1$.
3. Odd permutations: $(1\,3)$ gives $a_{13} a_{22} a_{31} = 3$; $(2\,3)$ gives $a_{11} a_{23} a_{32} = 4$; $(1\,2)$ gives $a_{12} a_{21} a_{33} = 0$.
4. So $\det A = 12 + 0 + 1 - 3 - 4 - 0 = 6$.

**Laplace expansion along row 1.**

5. By the [[Laplace expansion|0C08BQ3M05]], $\det A = 2 \det \begin{pmatrix} 3 & 2 \\ 1 & 2 \end{pmatrix} - 0 \cdot \det \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix} + 1 \cdot \det \begin{pmatrix} 1 & 3 \\ 1 & 1 \end{pmatrix}$.
6. The $2 \times 2$ determinants are $6 - 2 = 4$ and $1 - 3 = -2$.
7. So $\det A = 2 \cdot 4 + 1 \cdot (-2) = 6$.

**Row reduction.**

8. Subtract $\tfrac{1}{2}$ of row $1$ from rows $2$ and $3$. The rows become $(2, 0, 1)$, $(0, 3, \tfrac{3}{2})$ and $(0, 1, \tfrac{3}{2})$.
9. Subtract $\tfrac{1}{3}$ of row $2$ from row $3$. Row $3$ becomes $(0, 0, \tfrac{3}{2} - \tfrac{1}{2}) = (0, 0, 1)$.
10. Each step adds a multiple of one row to another row, so it keeps the determinant, by the [[effect of row operations|09YB3WQG38]].
11. The result is upper triangular, so by the [[triangular rule|0K1KKMFHYH]] $\det A = 2 \cdot 3 \cdot 1 = 6$.

The three methods give the same value $6$.

## Remarks

The Leibniz formula needs $3! = 6$ products of $3$ entries.
The Laplace expansion along row $1$ uses the zero entry $a_{12}$ to skip one minor.
Row reduction needs about $n^3/3$ multiplications for an $n \times n$ matrix, so it is the method of choice for large $n$.
If $a_{33}$ changes from $2$ to $1$, the determinant becomes $6 - 6 = 0$, because the cofactor of $a_{33}$ is $2 \cdot 3 - 0 \cdot 1 = 6$.

## Explanations

### L1 human

The determinant of a $3 \times 3$ table can be found in several ways.
We add and subtract six products, or we break the table into three small $2 \times 2$ tables, or we clear the entries below the diagonal.
All three ways give $6$ here.

### L2 human

The three computations check each other, which is a good habit for hand work.
A trap: in the Laplace expansion the signs alternate $+, -, +$ along row $1$, and forgetting the minus sign of the middle term gives a wrong answer when $a_{12} \neq 0$.
