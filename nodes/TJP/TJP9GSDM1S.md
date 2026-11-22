---
tag: TJP9GSDM1S
kind: proof
name: Proof of the Vandermonde determinant by column operations
msc: ["15A15", "15B05"]
topics: [DTBK11SR77]
audience: ug1
proves: 0P84B554AS
methods: [0NTF6DMVAP]
uses: [016PE4VZ8Q, 01ZTQBK64Q, 0ZZQ2E1MTE, 0W809K6AW0, 0C08BQ3M05, 0SD528P0EK, 009CY8JXFX]
sources:
  - url: https://en.wikipedia.org/wiki/Vandermonde_matrix
    locator: "Third proof: row and column operations"
---

## Proof

We clear the first row by column operations, pull a factor out of each remaining row, and use induction on $n$.

1. For $x_1, \dots, x_n$ in the commutative ring $K$, write $V(x_1, \dots, x_n)$ for the matrix with entries $x_i^{\,j-1}$.
   Write $P(x_1, \dots, x_n) = \prod_{1 \le i < j \le n} (x_j - x_i)$.
2. Base case $n = 1$: $V(x_1) = (1)$, whose determinant is $1$ by the [[Leibniz formula|016PE4VZ8Q]] with one term.
   The product $P(x_1)$ is empty, so it is also $1$.
3. Induction step: let $n \ge 2$, and assume $\det V(y_1, \dots, y_{n-1}) = P(y_1, \dots, y_{n-1})$ for all $y_1, \dots, y_{n-1} \in K$.
4. Adding $c$ times one column to another column does not change the determinant.
   The reason is that this operation on $M$ is the row operation "add $c$ times one row to another" on the [[transpose|0W809K6AW0]] $M^{\mathsf{T}}$.
   That row operation keeps the determinant by the rule for [[adding a multiple of a row|01ZTQBK64Q]], and $\det M = \det M^{\mathsf{T}}$ by the rule for the [[determinant of a transpose|0ZZQ2E1MTE]].
5. Let $V = V(x_1, \dots, x_n)$.
   For $j = n, n-1, \dots, 2$, in this order, subtract $x_1$ times column $j - 1$ from column $j$.
   Call the result $V'$.
6. When column $j$ is changed, column $j - 1$ still has its original entries $x_i^{\,j-2}$, because we work from right to left.
   So for $j \ge 2$, column $j$ of $V'$ has the entries
$$x_i^{\,j-1} - x_1 x_i^{\,j-2} = (x_i - x_1)\, x_i^{\,j-2}.$$
7. Column $1$ of $V'$ is unchanged, with all entries $1$.
   By step 4, applied $n - 1$ times, $\det V' = \det V$.
8. Row $1$ of $V'$ is $(1, 0, \dots, 0)$, since $x_1 - x_1 = 0$.
   The [[Laplace expansion along row 1|0C08BQ3M05]] therefore has one term, and $\det V' = \det B$, where $B$ is the [[minor|0SD528P0EK]] matrix that deletes row 1 and column 1 of $V'$.
9. By step 6, $B$ is the $(n-1) \times (n-1)$ matrix with entries
$$B_{rs} = (x_{r+1} - x_1)\, x_{r+1}^{\,s-1} \qquad (1 \le r, s \le n - 1).$$
10. Let $W = V(x_2, \dots, x_n)$, with entries $W_{rs} = x_{r+1}^{\,s-1}$.
   Then row $r$ of $B$ is $(x_{r+1} - x_1)$ times row $r$ of $W$.
11. By the rule for [[scaling a row|009CY8JXFX]], applied to each of the $n - 1$ rows,
$$\det B = \prod_{r=1}^{n-1} (x_{r+1} - x_1) \cdot \det W = \prod_{j=2}^{n} (x_j - x_1) \cdot \det W.$$
12. By the induction hypothesis, $\det W = \prod_{2 \le i < j \le n} (x_j - x_i)$.
13. Steps 7, 8, 11 and 12 give
$$\det V = \prod_{j=2}^{n} (x_j - x_1) \cdot \prod_{2 \le i < j \le n} (x_j - x_i).$$
   The first product collects the pairs $i < j$ with $i = 1$, and the second collects the pairs with $i \ge 2$.
   So $\det V = \prod_{1 \le i < j \le n} (x_j - x_i)$, which completes the induction.

## Idea

Subtracting $x_1$ times each column from the next one turns the first row into $(1, 0, \dots, 0)$.
Every other row $i$ then reads $(1, (x_i - x_1), (x_i - x_1) x_i, \dots)$, so after the first entry it is $x_i - x_1$ times the row of a smaller Vandermonde matrix.
Pulling out these factors gives one difference for each pair that involves $x_1$, and induction supplies the differences of the other pairs.

For $n = 3$ the steps look like this:
$$\begin{pmatrix} 1 & x_1 & x_1^2 \\ 1 & x_2 & x_2^2 \\ 1 & x_3 & x_3^2 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & 0 \\ 1 & x_2 - x_1 & (x_2 - x_1) x_2 \\ 1 & x_3 - x_1 & (x_3 - x_1) x_3 \end{pmatrix},$$
and the remaining $2 \times 2$ determinant is $(x_2 - x_1)(x_3 - x_1)(x_3 - x_2)$.

## Variants

The same proof works with row operations on the transposed matrix, whose columns are $(1, x_i, \dots, x_i^{n-1})^{\mathsf{T}}$.
The [[proof by roots of polynomials|R653HXJ20N]] treats $\det V$ as a polynomial in $x_n$ and uses the bound on the number of roots of a polynomial over a field.
The column operations above use no division, so this proof works directly over every commutative ring, without the substitution step of the other proof.
