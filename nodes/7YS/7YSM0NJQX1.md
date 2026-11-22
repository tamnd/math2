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

Let
$$A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 2 \end{pmatrix}$$
over $\mathbb{Q}$.
We compute its [[determinant|00KDZRW4C0]] by the three definitions of the [[equivalence theorem|W3JN0WPZ10]], and we get $6$ each time.

*The Leibniz formula.*
The [[Leibniz formula|016PE4VZ8Q]] has one term $\operatorname{sgn}(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} a_{3 \sigma(3)}$ for each of the six permutations $\sigma$ of $\{1, 2, 3\}$.

1. The three even permutations are the identity, $(1\,2\,3)$ and $(1\,3\,2)$.
   They give $a_{11} a_{22} a_{33} = 2 \cdot 3 \cdot 2 = 12$, then $a_{12} a_{23} a_{31} = 0 \cdot 2 \cdot 1 = 0$, then $a_{13} a_{21} a_{32} = 1 \cdot 1 \cdot 1 = 1$.
2. The three odd permutations are $(1\,3)$, $(2\,3)$ and $(1\,2)$.
   They give $a_{13} a_{22} a_{31} = 1 \cdot 3 \cdot 1 = 3$, then $a_{11} a_{23} a_{32} = 2 \cdot 2 \cdot 1 = 4$, then $a_{12} a_{21} a_{33} = 0$.
3. Add the even terms and subtract the odd terms:
$$\det A = 12 + 0 + 1 - 3 - 4 - 0 = 6.$$

*The Laplace recursion along row 1.*

4. The [[Laplace expansion|0C08BQ3M05]] along row $1$ uses the signs $+, -, +$:
$$\det A = 2 \begin{vmatrix} 3 & 2 \\ 1 & 2 \end{vmatrix} - 0 \begin{vmatrix} 1 & 2 \\ 1 & 2 \end{vmatrix} + 1 \begin{vmatrix} 1 & 3 \\ 1 & 1 \end{vmatrix}.$$
5. The two minors that we need are $3 \cdot 2 - 2 \cdot 1 = 4$ and $1 \cdot 1 - 3 \cdot 1 = -2$.
6. So $\det A = 2 \cdot 4 + 1 \cdot (-2) = 6$.

*Row reduction.*

7. Subtract $\tfrac{1}{2}$ times row $1$ from rows $2$ and $3$.
   The rows become $(2, 0, 1)$, $(0, 3, \tfrac{3}{2})$ and $(0, 1, \tfrac{3}{2})$.
8. Subtract $\tfrac{1}{3}$ times row $2$ from row $3$.
   Row $3$ becomes $(0, 0, \tfrac{3}{2} - \tfrac{1}{2}) = (0, 0, 1)$.
9. Each step adds a multiple of one row to another row, so it keeps the determinant, by the [[effect of row operations|09YB3WQG38]].
10. The result is upper triangular, so the [[triangular rule|0K1KKMFHYH]] gives $\det A = 2 \cdot 3 \cdot 1 = 6$.

## Remarks

The three methods cost different amounts of work.
The Leibniz formula needs $3! = 6$ products of three entries, and the zero entry $a_{12}$ kills two of them.
The Laplace expansion along row $1$ uses the same zero to skip one minor.
Row reduction needs about $n^3/3$ multiplications for an $n \times n$ matrix, so it is the method of choice when $n$ is large.

Change one entry and see what happens.
If $a_{33}$ changes from $2$ to $1$, the determinant drops by the cofactor of $a_{33}$, which is $2 \cdot 3 - 0 \cdot 1 = 6$.
So the new determinant is $6 - 6 = 0$, and the new matrix is not invertible.
Check: with $a_{33} = 1$, row $2$ minus row $3$ is $(0, 2, 1)$, and row $3$ minus $\tfrac{1}{2}$ times row $1$ is $(0, 1, \tfrac{1}{2})$, half of it, so the rows are dependent.

## Explanations

### L1 human

A $3 \times 3$ determinant can be found in several ways.
We can add and subtract six products of three numbers.
We can break the table into three small $2 \times 2$ tables along the first row.
Or we can clear the entries below the diagonal and multiply what is left on the diagonal.
All three ways give $6$ for this table.

### L2 human

The three computations check each other, and that is a good habit for hand work.
When two methods disagree, the usual cause is a sign.
Watch out: in the Laplace expansion the signs along row $1$ are $+, -, +$.
If you forget the minus sign of the middle term, you get a wrong answer whenever $a_{12}$ and its minor are both nonzero.
Here $a_{12} = 0$, so this matrix cannot reveal the mistake, and a second method is the safer check.
