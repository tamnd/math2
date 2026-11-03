---
tag: NJ41GD4C0R
kind: definition
name: Transfer matrix method
msc: [82B20, 82B23]
defines: EXX6S3K5Z5
uses: [07PTPSZPME, 0BQAA2BK3Q, GYNMZ9201M]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer-matrix_method_(statistical_mechanics)
---

## Definition

Let $S$ be a finite set of single-site states, let $E \colon S \times S \to \R$ be a nearest-neighbour energy and let $\beta \ge 0$ be the inverse temperature.
Consider the periodic chain of $N$ sites with energy
$$H(s_1, \dots, s_N) = \sum_{i=1}^{N} E(s_i, s_{i+1}), \qquad s_{N+1} = s_1.$$
The *transfer matrix* is the $S \times S$ matrix $T$ with entries $T_{a b} = e^{-\beta E(a, b)}$.
The *transfer matrix method* is the evaluation of the partition function through the identity
$$Z_N = \sum_{s \in S^N} e^{-\beta H(s)} = \tr(T^N),$$
which follows by expanding the [[trace|07PTPSZPME]] of the matrix product.

## Remarks

If $\lambda_1 \ge \abs{\lambda_2} \ge \dots$ are the [[eigenvalues|0BQAA2BK3Q]] of $T$, then $Z_N = \sum_k \lambda_k^N$.
Since $T$ has positive entries, the Perron–Frobenius theorem makes $\lambda_1$ simple and strictly larger than the other moduli, so $-\beta f = \lim_N \frac{1}{N} \log Z_N = \log \lambda_1$.
Connected correlations typically decay like $(\abs{\lambda_2}/\lambda_1)^r$ at distance $r$, so the correlation length is $1/\log(\lambda_1/\abs{\lambda_2})$.
Example: the Ising chain with $E(a, b) = -J a b - h (a + b)/2$ on $S = \set{-1, +1}$ has
$$T = \begin{pmatrix} e^{\beta (J + h)} & e^{-\beta J} \\ e^{-\beta J} & e^{\beta (J - h)} \end{pmatrix},$$
and for $h = 0$ its eigenvalues are $2 \cosh \beta J$ and $2 \sinh \beta J$.
Non-example: a chain in which each site interacts with all other sites is not covered.
Its energy is not a sum of terms in neighbouring pairs, and one would need states of unbounded size.
In two dimensions one takes $S$ to be the set of configurations of a whole row, which turns the method into a large eigenvalue problem.
