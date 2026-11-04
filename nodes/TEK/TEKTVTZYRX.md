---
tag: TEKTVTZYRX
kind: proof
name: Proof that the Möbius function is the inverse of the constant function 1
msc: [11A25]
proves: 0ASC73QEQT
uses: [0C8QENHYZW, 0KH1N66QWW, 004JW7A2N5, 0YVVXT3A0B, 084HH1NDCB, 0EHWPWGHB2]
sources:
  - url: https://en.wikipedia.org/wiki/M%C3%B6bius_function
    locator: Proof of the formula for the sum of μ over divisors
---

## Proof

1. Let $n$ be a positive integer. By the definition of the [[Dirichlet convolution|0KH1N66QWW]], $(\mu * \mathbf{1})(n) = \sum_{d \mid n} \mu(d) \mathbf{1}(n/d) = \sum_{d \mid n} \mu(d)$.
2. Case $n = 1$. The only divisor is $d = 1$. No prime square divides $1$, so $1$ is [[squarefree|004JW7A2N5]], and $\omega(1) = 0$. So the sum is $\mu(1) = (-1)^0 = 1$.
3. Case $n > 1$. By the [[fundamental theorem of arithmetic|084HH1NDCB]], $n = p_1^{e_1} \cdots p_k^{e_k}$ with distinct primes $p_i$, exponents $e_i \ge 1$, and $k \ge 1$.
4. By the definition of the [[Möbius function|0C8QENHYZW]], $\mu(d) = 0$ unless $d$ is squarefree. So only squarefree divisors $d$ of $n$ contribute to the sum.
5. A divisor of $n$ has the form $p_1^{c_1} \cdots p_k^{c_k}$ with $0 \le c_i \le e_i$. It is squarefree exactly when each $c_i$ is $0$ or $1$.
6. So the squarefree divisors of $n$ are the products $d_S = \prod_{i \in S} p_i$, one for each subset $S$ of $\set{1, \dots, k}$. Distinct subsets give distinct divisors, by uniqueness of factorization.
7. The divisor $d_S$ has exactly $\abs{S}$ distinct prime factors, so $\omega(d_S) = \abs{S}$ (see [[the number of distinct prime factors|0YVVXT3A0B]]). Hence $\mu(d_S) = (-1)^{\abs{S}}$.
8. There are $\binom{k}{j}$ subsets $S$ with $\abs{S} = j$. So
$$\sum_{d \mid n} \mu(d) = \sum_{j=0}^{k} \binom{k}{j} (-1)^j.$$
9. By the [[binomial theorem|0EHWPWGHB2]] with $x = -1$ and $y = 1$, this sum equals $(1 - 1)^k = 0$, since $k \ge 1$.
10. So $(\mu * \mathbf{1})(n)$ is $1$ for $n = 1$ and $0$ for $n > 1$. That is, $\mu * \mathbf{1} = \varepsilon$.

## Idea

Only squarefree divisors count, and these correspond to subsets of the distinct primes of $n$. The sign $(-1)^{\abs{S}}$ then turns the sum into $(1-1)^k$ by the binomial theorem. This vanishes as soon as $n$ has a prime factor.
