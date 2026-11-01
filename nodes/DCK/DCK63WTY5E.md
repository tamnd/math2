---
tag: DCK63WTY5E
kind: statement
role: theorem
name: Marchenko–Pastur law
msc: [60B20, 15B52, 62H10]
uses: [0BQAA2BK3Q, 00MRN0FARV, 0SRYJGXKR4]
about: [0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Marchenko–Pastur_distribution
---

## Statement

Let $(Y_{ij})_{i, j \ge 1}$ be [[independent and identically distributed|00MRN0FARV]] real random variables with mean $0$ and variance $1$.
Let $p = p(n)$ be positive integers with $p / n \to y \in (0, \infty)$ as $n \to \infty$.
Let $X_n$ be the $p \times n$ matrix $(Y_{ij})_{i \le p, j \le n}$, let $S_n = \frac1n X_n X_n^{\mathsf{T}}$, and let $\mu_n = \frac1p \sum_{k=1}^p \delta_{\lambda_k}$, where $\lambda_1, \ldots, \lambda_p$ are the [[eigenvalues|0BQAA2BK3Q]] of $S_n$.
Let $a = (1 - \sqrt y)^2$ and $b = (1 + \sqrt y)^2$.
Then, almost surely, $\mu_n$ [[converges weakly|0SRYJGXKR4]] to the Marchenko–Pastur distribution with ratio $y$, the probability measure
$$\nu_y(dx) = \frac{1}{2\pi x y} \sqrt{(b - x)(x - a)} \, \mathbf{1}_{[a, b]}(x) \, dx + \Big(1 - \frac1y\Big)^{+} \delta_0(dx),$$
where $t^{+} = \max(t, 0)$.

## Remarks

The proof can use the moment method or the Stieltjes transform.
The Stieltjes transform $m(z) = \int \frac{\nu_y(dx)}{x - z}$ of the limit solves the quadratic equation $y z m^2 + (z + y - 1) m + 1 = 0$, and inverting it gives the density.
When $y > 1$ the matrix $S_n$ has rank at most $n < p$, which explains the atom of mass $1 - 1/y$ at $0$.
The limit has mean $1$ and second moment $1 + y$.
Example: for $y = 1$ the support is $[0, 4]$ and the density is $\frac{1}{2\pi} \sqrt{(4 - x)/x}$.

## Explanations

### L1 human

Take $n$ independent samples of a vector of $p$ independent standard measurements and form the sample covariance matrix.
If $p$ is small compared with $n$, its eigenvalues are all close to $1$, the true value.
If $p$ and $n$ are both large and comparable, the eigenvalues spread over an interval around $1$ with a definite shape, the Marchenko–Pastur law.

### L2 human

It is the analogue of the [[Wigner semicircle law|3QTT95DMFH]] for sample covariance matrices.
In high-dimensional statistics it shows that the sample covariance matrix is a poor estimate of the true covariance when $p/n$ is not small.
Eigenvalues of data that fall outside $[a, b]$ are read as signals that are not pure noise.
