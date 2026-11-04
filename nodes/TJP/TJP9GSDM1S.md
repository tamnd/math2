---
tag: TJP9GSDM1S
kind: proof
name: Proof of the Vandermonde determinant by column operations
msc: [15A15, 15B05]
proves: 0P84B554AS
uses: [016PE4VZ8Q, 01ZTQBK64Q, 0ZZQ2E1MTE, 0W809K6AW0, 0C08BQ3M05, 0SD528P0EK, 009CY8JXFX]
sources:
  - url: https://en.wikipedia.org/wiki/Vandermonde_matrix
    locator: "Third proof: row and column operations"
---

## Proof

We argue by induction on $n$.

1. For $x_1, \dots, x_n \in K$, write $V(x_1, \dots, x_n)$ for the matrix with entries $x_i^{\,j-1}$, and $P(x_1, \dots, x_n) = \prod_{1 \le i < j \le n} (x_j - x_i)$.
2. Base case $n = 1$: $V(x_1) = (1)$. By the [[Leibniz formula|016PE4VZ8Q]] with one term, its determinant is $1$. The product $P(x_1)$ is empty, so it is also $1$.
3. Induction step: let $n \ge 2$, and assume $\det V(y_1, \dots, y_{n-1}) = P(y_1, \dots, y_{n-1})$ for all $y_1, \dots, y_{n-1} \in K$.
4. Column operations: let $M'$ result from a square matrix $M$ when $c$ times column $k$ is added to column $l$, with $k \ne l$.
5. Then the [[transpose|0W809K6AW0]] $M'^T$ results from $M^T$ when $c$ times row $k$ is added to row $l$.
6. By the rule for [[adding a multiple of a row|01ZTQBK64Q]] and the rule for the [[determinant of a transpose|0ZZQ2E1MTE]], $\det M' = \det M'^T = \det M^T = \det M$.
7. Let $V = V(x_1, \dots, x_n)$. For $j = n, n-1, \dots, 2$, in this order, subtract $x_1$ times column $j - 1$ from column $j$. Call the result $V'$.
8. When column $j$ is changed, column $j - 1$ has not been changed yet. So column $j$ of $V'$ has entries $x_i^{\,j-1} - x_1 x_i^{\,j-2} = (x_i - x_1)\, x_i^{\,j-2}$ for $j \ge 2$.
9. Column $1$ of $V'$ is unchanged, with all entries $1$. By step 6, applied $n - 1$ times, $\det V' = \det V$.
10. Row $1$ of $V'$ is $(1, 0, \dots, 0)$, since $x_1 - x_1 = 0$.
11. By the [[Laplace expansion along row $1$|0C08BQ3M05]], $\det V' = 1 \cdot (-1)^{1+1} M'_{11} = M'_{11}$, where $M'_{11}$ is a first [[minor|0SD528P0EK]] of $V'$.
12. $M'_{11} = \det B$, where $B$ is the $(n-1) \times (n-1)$ matrix with entries $B_{rs} = (x_{r+1} - x_1)\, x_{r+1}^{\,s-1}$ for $1 \le r, s \le n-1$.
13. Let $W = V(x_2, \dots, x_n)$, with entries $W_{rs} = x_{r+1}^{\,s-1}$. Row $r$ of $B$ is $(x_{r+1} - x_1)$ times row $r$ of $W$.
14. By the rule for [[scaling a row|009CY8JXFX]], applied to each of the $n - 1$ rows, $\det B = \prod_{r=1}^{n-1} (x_{r+1} - x_1) \cdot \det W$.
15. By the induction hypothesis, $\det W = P(x_2, \dots, x_n) = \prod_{2 \le i < j \le n} (x_j - x_i)$.
16. By steps 9 to 15, $\det V = \prod_{j=2}^{n} (x_j - x_1) \cdot \prod_{2 \le i < j \le n} (x_j - x_i)$.
17. The pairs $i < j$ with $i = 1$ give the first product, and the pairs with $i \ge 2$ give the second. So $\det V = \prod_{1 \le i < j \le n} (x_j - x_i)$.

## Idea

Subtracting $x_1$ times each column from the next clears the first row except for a $1$. What is left has a factor $x_i - x_1$ in each row and is otherwise a smaller Vandermonde matrix. Induction then collects one factor $x_j - x_i$ for each pair $i < j$.
