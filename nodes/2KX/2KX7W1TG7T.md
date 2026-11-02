---
tag: 2KX7W1TG7T
kind: statement
role: theorem
name: Inverse transform sampling
msc: [65C10, "60E05"]
uses: [0H8H7ZTHW2, 0X60VE98HN, 0AREFQ9Z65, 0PNRKMRC55, 0E99F51GVB]
about: [0X60VE98HN]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_transform_sampling
same_as:
  wikidata: Q1377019
  wikipedia: Inverse transform sampling
---

## Statement

Let $F \colon \R \to [0, 1]$ be a [[cumulative distribution function|0H8H7ZTHW2]], that is, non-decreasing, right-continuous, with limits $0$ at $-\infty$ and $1$ at $+\infty$.
Let $F^{-1} \colon (0, 1) \to \R$ be its generalized inverse, the [[quantile function|0X60VE98HN]]
$$F^{-1}(u) = \inf \set{x \in \R : F(x) \ge u}.$$
Let $U$ be a [[random variable|0PNRKMRC55]] with the [[uniform distribution|0AREFQ9Z65]] on $(0, 1)$.
Then the random variable $X = F^{-1}(U)$ has cumulative distribution function $F$.

## Remarks

The key fact is that for $u \in (0, 1)$ and $x \in \R$, $F^{-1}(u) \le x$ if and only if $u \le F(x)$; this uses right-continuity of $F$, which makes the infimum attained.
Hence $P(X \le x) = P(U \le F(x)) = F(x)$.
Example: the [[exponential distribution|0E99F51GVB]] with rate $\lambda > 0$ has $F(x) = 1 - e^{-\lambda x}$ for $x \ge 0$, so $F^{-1}(u) = -\ln(1 - u)/\lambda$; since $1 - U$ is also uniform, $-\ln(U)/\lambda$ is exponential too.
Example: for a discrete distribution with values $x_1 < x_2 < \cdots$ and probabilities $p_1, p_2, \ldots$, the method returns $x_k$ when $p_1 + \cdots + p_{k-1} < U \le p_1 + \cdots + p_k$.
The generalized inverse is needed: when $F$ has jumps or flat parts, the ordinary inverse does not exist.
A converse holds when $F$ is continuous: then $F(X)$ is uniform on $(0, 1)$, the probability integral transform.

## Explanations

### L1 human

A computer can produce uniform random numbers between $0$ and $1$.
To get random numbers with any other distribution, feed each uniform number into the inverse of the distribution function.
Values of $u$ near $0$ give values from the lower tail, values near $1$ give the upper tail, and the shape of the distribution comes out exactly right.
For the exponential distribution this means $-\ln(u)/\lambda$.

### L2 human

The method is exact and uses one uniform number per sample, so it is the first choice whenever $F^{-1}$ has a closed form or a fast accurate approximation.
For the normal distribution there is no closed form, and one uses numerical approximations of $F^{-1}$ or other methods such as the Box–Muller transform or the ziggurat algorithm.
Being monotone in $U$, it preserves the order of the uniform inputs, which is useful for antithetic variates, for quasi-Monte Carlo and for coupling arguments.
It also explains copulas: any multivariate distribution is obtained from its copula by applying the marginal quantile functions coordinatewise.
