---
tag: E291NNAMF9
kind: definition
name: Arithmetic coding
msc: [94A29, 68P30, 94A45]
defines: BG1TG1WY7Q
uses: [GNB3T6TD0M, 0D6J4B671D, 00MRN0FARV]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_coding
---

## Definition

Let $\mathcal{X} = \set{a_1, \dots, a_m}$ be an ordered finite alphabet and $p$ a [[probability mass function|0D6J4B671D]] on $\mathcal{X}$ with $p(a_k) > 0$ for all $k$.
Put $F(a_k) = \sum_{j < k} p(a_j)$.
For a message $x = x_1 x_2 \cdots x_n \in \mathcal{X}^n$, define intervals $[\lambda_t, \lambda_t + w_t)$ by $\lambda_0 = 0$, $w_0 = 1$ and, for $t = 1, \dots, n$,
$$\lambda_t = \lambda_{t-1} + w_{t-1} F(x_t), \qquad w_t = w_{t-1}\, p(x_t).$$
Let $P = w_n = \prod_{t} p(x_t)$ and $\ell = \ceil{\log_2 (1/P)} + 1$.
The *arithmetic code* of $x$ is the string of the first $\ell$ binary digits of $\lambda_n + P/2$ after the point.

## Remarks

The intervals of distinct messages of length $n$ are disjoint, and the dyadic interval named by the codeword lies inside the interval of $x$.
So the code is a [[prefix code|GNB3T6TD0M]] on $\mathcal{X}^n$, with length less than $\log_2(1/P) + 2$.
For [[i.i.d.|00MRN0FARV]] symbols with law $p$, the expected length is less than $n$ times the entropy of $p$, plus $2$.
Example: let $p(a) = 3/4$, $p(b) = 1/4$, so $F(a) = 0$, $F(b) = 3/4$.
For $x = ab$, the intervals are $[0, 3/4)$ and then $[9/16, 12/16)$, so $P = 3/16$ and $\ell = 3 + 1 = 4$.
The midpoint $21/32$ is $0.10101$ in binary, so the codeword is $1010$.
Its dyadic interval $[10/16, 11/16)$ lies inside $[9/16, 12/16)$, as required.
Non-example: taking only $\ceil{\log_2(1/P)} = 3$ digits of the left end $9/16 = 0.1001$ gives $0.100 = 1/2$, which lies outside the interval of $x$.
Practical coders use finite-precision integer arithmetic and emit digits as soon as they are fixed; the version above is the exact one.
