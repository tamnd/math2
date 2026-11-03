---
tag: 7AZKYYGEEG
kind: statement
role: theorem
name: Stable age distribution
msc: [92D25, 15B48]
uses: [RNVHT5BTQS, 62NS7PV1M9, 0BQAA2BK3Q, 0N6960W0BV, 7Q60BB01YG]
about: [RNVHT5BTQS]
sources:
  - url: https://en.wikipedia.org/wiki/Leslie_matrix
---

## Statement

Let $L$ be a $k \times k$ [[Leslie matrix|RNVHT5BTQS]] with fecundities $f_1, \ldots, f_k \ge 0$ and survival probabilities $s_1, \ldots, s_{k-1} > 0$.
Assume that $f_k > 0$ and that the greatest common divisor of the indices $i$ with $f_i > 0$ is $1$.
Put $\ell_1 = 1$ and $\ell_i = s_1 s_2 \cdots s_{i-1}$ for $2 \le i \le k$.
Then:

1. $L$ has a unique positive [[eigenvalue|0BQAA2BK3Q]] $\lambda$, and it is a simple eigenvalue.
   It is the unique positive solution of $\sum_{i=1}^{k} f_i \ell_i \lambda^{-i} = 1$, and $\abs{\mu} < \lambda$ for every other eigenvalue $\mu$ of $L$.
2. The vector $v$ with entries $v_i = \ell_i \lambda^{-(i-1)}$ is a positive [[eigenvector|0N6960W0BV]] of $L$ for $\lambda$.
3. For every nonzero $n(0) \in \R_{\ge 0}^k$, the solution $n(t) = L^t n(0)$ satisfies
$$\lim_{t \to \infty} \frac{n(t)}{\lambda^t} = c \, v \quad \text{for some } c > 0, \qquad \lim_{t \to \infty} \frac{n(t)}{\sum_i n_i(t)} = \frac{v}{\sum_i v_i}.$$

The vector $v / \sum_i v_i$ is called the *stable age distribution*.

## Remarks

The condition $f_k > 0$ makes $L$ [[irreducible|7Q60BB01YG]], since the classes form the cycle $1 \to 2 \to \cdots \to k \to 1$.
The gcd condition makes $L$ primitive, that is, some power $L^m$ has all entries positive.
The [[Perron–Frobenius theorem|62NS7PV1M9]] applied to $L^m$ gives parts 1 and 2, and the gap $\abs{\mu} < \lambda$ gives the convergence in part 3 with $c = w \cdot n(0) / (w \cdot v)$, where $w$ is a positive left eigenvector.
Example: for $L = \begin{pmatrix} 1 & 2 \\ 0.5 & 0 \end{pmatrix}$, $\lambda = (1 + \sqrt 5)/2$ and $v = (1, 0.5/\lambda) \approx (1, 0.309)$, so in the long run about $76\%$ of the population is in the first class.
Without the gcd condition the conclusion can fail: for $L = \begin{pmatrix} 0 & 2 \\ 0.5 & 0 \end{pmatrix}$ the eigenvalues are $1$ and $-1$, and from $n(0) = (1, 0)$ the population alternates between $(1, 0)$ and $(0, 0.5)$.

## Explanations

### L1 human

Start an age-structured population in any way, with many old animals or only newborns.
After enough generations the shares of the age groups stop changing, and the whole population grows by the same factor $\lambda$ each step.
The initial state is forgotten: only the overall size remembers it.

### L2 human

This is the main theorem about Leslie models and an application of Perron–Frobenius theory.
The growth factor $\lambda$ decides the fate of the population: it grows if $\lambda > 1$ and declines if $\lambda < 1$.
The equation $\sum_i f_i \ell_i \lambda^{-i} = 1$ is the discrete Euler–Lotka equation, and $R_0 = \sum_i f_i \ell_i$, the expected number of offspring of a newborn, satisfies $\lambda > 1$ if and only if $R_0 > 1$.
The same argument works for any primitive projection matrix of a [[matrix population model|WS9M7HY0FE]].
