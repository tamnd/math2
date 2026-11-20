---
tag: D0K478FKER
kind: proof
name: Proof of the formula for the coefficients of the characteristic polynomial by multilinearity
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 0FRYPZ6D0X
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [039HF58KQ5, 0PPG793642, 0C08BQ3M05, 0Z4BWARC38, 07PTPSZPME, 0C3CFHDN6R, 0BT9BYWVRY, 016PE4VZ8Q, 05RWFKVTJ7, 0DPF6WRZW6, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Proof

We expand $\det(t I_n - A)$ by multilinearity in the rows, over the commutative ring $R = K[t]$, the [[polynomial ring|0Q9EZS90GY]].

1. Write $e_i$ for the $i$-th standard unit row of length $n$, and $r_i$ for row $i$ of $-A$. Then row $i$ of $t I_n - A$ is $t e_i + r_i$, by the definition of the [[characteristic polynomial|039HF58KQ5]].
2. For a subset $S \subseteq \{1, \dots, n\}$, let $N_S$ be the matrix whose row $i$ is $r_i$ for $i \in S$ and $e_i$ for $i \notin S$.
3. The determinant over $R$ is linear in each row, by [[multilinearity in rows|0PPG793642]]. Apply it to row $1$, then to row $2$, and so on up to row $n$.
4. Each application splits every term into two, one with $t e_i$ and one with $r_i$ in row $i$. After $n$ steps there is one term for each subset $S$, the set of rows with $r_i$.
5. In the term for $S$, the rows $i \notin S$ are $t e_i$. Linearity in each of these rows takes out a factor $t$. So $p_A(t) = \sum_{S} t^{n - |S|} \det N_S$.
6. Claim: $\det N_S = \det\big((-A)_S\big)$ for $S \ne \emptyset$, and $\det N_\emptyset = 1$.
7. For $S = \emptyset$, $N_\emptyset = I_n$, and $\det I_n = 1$ by the [[determinant of the identity|0Z4BWARC38]].
8. Let $S \ne \emptyset$ and let $i \notin S$. Row $i$ of $N_S$ is $e_i$, with a single nonzero entry $1$ in column $i$.
9. By the [[Laplace expansion|0C08BQ3M05]] along row $i$, $\det N_S = (-1)^{i+i} \cdot 1 \cdot M_{ii} = M_{ii}$, where $M_{ii}$ is the determinant of $N_S$ without row $i$ and column $i$.
10. In the smaller matrix, each remaining row $j \notin S$ is still a unit row with its $1$ on the diagonal, because the deleted column $i$ had a $0$ in row $j$.
11. Repeat steps 8 to 10 for each index outside $S$, by induction on $n - |S|$. What remains is the matrix of the rows $r_i$, $i \in S$, restricted to the columns in $S$. This is $(-A)_S$.
12. So $\det N_S = \det\big((-A)_S\big)$, which proves the claim.
13. The matrix $(-A)_S$ has size $|S|$, so $\det\big((-A)_S\big) = (-1)^{|S|} \det A_S$, by linearity in each of its $|S|$ rows.
14. Grouping the subsets by $k = |S|$ in step 5 gives $p_A(t) = \sum_{k=0}^{n} t^{n-k} (-1)^k \sum_{|S| = k} \det A_S = \sum_{k=0}^{n} (-1)^k E_k(A)\, t^{n-k}$.
15. For $k = 1$, the principal $1 \times 1$ minors are $a_{11}, \dots, a_{nn}$. So $E_1(A) = \tr A$, by the definition of the [[trace|07PTPSZPME]].
16. For $k = n$, the only subset is $S = \{1, \dots, n\}$, and $E_n(A) = \det A$.
17. Parts 3 and 4 of the statement are the cases $n = 2$ and $n = 3$ of step 14.

## Idea

Each row of $tI - A$ is a sum of two rows, $t e_i$ and a row of $-A$.
Expanding the determinant over all choices gives one term for each set $S$ of rows taken from $-A$.
The unit rows reduce the determinant to the principal minor of $-A$ on $S$, and the other rows contribute the factor $t^{n-|S|}$.

## Variants

- For the trace coefficient alone, the [[Leibniz formula|016PE4VZ8Q]] gives a short proof. A [[permutation|05RWFKVTJ7]] other than the identity moves at least two indices. So its term in $\det(tI - A)$ has [[degree|0DPF6WRZW6]] at most $n - 2$, and the coefficient of $t^{n-1}$ comes from $\prod_i (t - a_{ii})$ alone.
- When $K$ is a field and $p_A$ splits, the formula follows from triangularisation: $A$ is similar to a triangular matrix with diagonal $\lambda_1, \dots, \lambda_n$, and the coefficients of $\prod (t - \lambda_i)$ are the elementary symmetric polynomials. This proof needs a splitting field and does not work over a general commutative ring.
- The constant term alone follows by setting $t = 0$: $p_A(0) = \det(-A) = (-1)^n \det A$.
