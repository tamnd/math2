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

We write each row of $tI - A$ as a sum of two rows, expand the determinant by multilinearity over the commutative ring $R = K[t]$, the [[polynomial ring|0Q9EZS90GY]], and identify each term as a principal minor.

*Expanding by rows.*

1. Write $e_i$ for the $i$-th standard unit row of length $n$, and $r_i$ for row $i$ of $-A$.
   By the definition of the [[characteristic polynomial|039HF58KQ5]], row $i$ of $t I_n - A$ is $t e_i + r_i$.
2. For a subset $S \subseteq \{1, \dots, n\}$, let $N_S$ be the matrix whose row $i$ is $r_i$ for $i \in S$ and $e_i$ for $i \notin S$.
3. The determinant over $R$ is linear in each row, by [[multilinearity in rows|0PPG793642]].
   Apply this to row $1$, then to row $2$, and so on up to row $n$.
4. Each application splits every term into two, one with $t e_i$ in row $i$ and one with $r_i$ in row $i$.
   After $n$ steps there is one term for each subset $S$, namely the set of rows that hold $r_i$.
5. In the term for $S$, each row $i \notin S$ is $t e_i$, and linearity in that row takes out a factor $t$.
   So
$$p_A(t) = \sum_{S \subseteq \{1, \dots, n\}} t^{n - |S|} \det N_S.$$

*Each term is a principal minor.*

6. We claim that $\det N_\emptyset = 1$ and that $\det N_S = \det\big((-A)_S\big)$ for $S \ne \emptyset$.
7. For $S = \emptyset$, the matrix $N_\emptyset$ is $I_n$, and $\det I_n = 1$ by the [[determinant of the identity|0Z4BWARC38]].
8. Let $S \ne \emptyset$ and let $i \notin S$.
   Row $i$ of $N_S$ is $e_i$, with a single nonzero entry $1$ in column $i$.
9. By the [[Laplace expansion|0C08BQ3M05]] along row $i$, $\det N_S = (-1)^{i+i} \cdot 1 \cdot M_{ii} = M_{ii}$, where $M_{ii}$ is the determinant of $N_S$ with row $i$ and column $i$ deleted.
10. In the smaller matrix, each remaining row $j \notin S$ is still a unit row with its $1$ on the diagonal, because the deleted column $i$ had a $0$ in row $j$.
11. Repeat steps 8 to 10 once for each index outside $S$, by induction on $n - |S|$.
    What remains is the matrix of the rows $r_i$ with $i \in S$, cut down to the columns in $S$, which is $(-A)_S$.
    This proves the claim.
12. The matrix $(-A)_S$ has size $|S|$, so linearity in each of its $|S|$ rows gives $\det\big((-A)_S\big) = (-1)^{|S|} \det A_S$.

*Collecting terms.*

13. Group the subsets in step 5 by their size $k = |S|$, and use steps 7, 11 and 12:
$$p_A(t) = \sum_{k=0}^{n} t^{n-k} (-1)^k \sum_{|S| = k} \det A_S = \sum_{k=0}^{n} (-1)^k E_k(A)\, t^{n-k}.$$
14. For $k = 1$, the principal $1 \times 1$ minors are $a_{11}, \dots, a_{nn}$, so $E_1(A) = \operatorname{tr} A$ by the definition of the [[trace|07PTPSZPME]].
15. For $k = n$, the only subset is $S = \{1, \dots, n\}$, so $E_n(A) = \det A$.
16. Parts 3 and 4 of the statement are the cases $n = 2$ and $n = 3$ of step 13.

## Idea

Each row of $tI - A$ is the sum of $t e_i$ and a row of $-A$.
Expanding the determinant over all choices gives one term for each set $S$ of rows that were taken from $-A$.
In that term the unit rows contribute the factor $t^{n-|S|}$, and they also cut the determinant down to the principal minor of $-A$ on $S$.
Collecting the terms by the size of $S$ gives the formula, and the sign $(-1)^k$ comes from the minus sign in $-A$.

## Variants

For the trace coefficient alone, the [[Leibniz formula|016PE4VZ8Q]] gives a short proof.
A [[permutation|05RWFKVTJ7]] other than the identity moves at least two indices, so its term in $\det(tI - A)$ has at most $n - 2$ diagonal factors and [[degree|0DPF6WRZW6]] at most $n - 2$.
So the coefficient of $t^{n-1}$ comes from the product $\prod_i (t - a_{ii})$ alone, and it is $-\sum_i a_{ii}$.

When $K$ is a field and $p_A$ splits, the formula for the coefficients in terms of eigenvalues also follows from triangularization.
Then $A$ is similar to a triangular matrix with diagonal $\lambda_1, \dots, \lambda_n$, and the coefficients of $\prod_i (t - \lambda_i)$ are the elementary symmetric polynomials of the $\lambda_i$, up to sign.
This route needs a splitting field and does not give the principal minors directly.

The constant term alone follows by putting $t = 0$: $p_A(0) = \det(-A) = (-1)^n \det A$.
