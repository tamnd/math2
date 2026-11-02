---
tag: BWMS6B1M5N
kind: definition
name: Excessive function
msc: [60J45, 31D05]
defines: 46436KE7NT
uses: [2AVNDP8BJP, 22735FGJV6, X4V2S56YQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Hunt_process
---

## Definition

Let $(E, \mathcal{E})$ be a measurable space.
Let $(P_t)_{t \ge 0}$ be a sub-Markov transition semigroup on $E$.
That is, each $P_t$ is a kernel as for a [[Markov kernel|2AVNDP8BJP]], except that the total mass satisfies $P_t(x, E) \le 1$, $P_0$ is the identity, and $P_s P_t = P_{s+t}$.
For a measurable $f \colon E \to [0, \infty]$, write $P_t f(x) = \int_E f(y) \, P_t(x, dy)$.
A measurable function $f \colon E \to [0, \infty]$ is *excessive* for $(P_t)$ if:

1. $P_t f \le f$ for every $t \ge 0$.
2. $P_t f(x) \to f(x)$ as $t \downarrow 0$, for every $x \in E$.

## Remarks

Under clause 1, $t \mapsto P_t f$ is decreasing, since $P_{t+s} f = P_t (P_s f) \le P_t f$; so the limit in clause 2 exists and is at most $f$.
A function with clause 1 alone is called supermedian; for $\alpha > 0$, the $\alpha$-excessive functions are those that are excessive for the semigroup $e^{-\alpha t} P_t$.
Example: let $(P_t)$ be the semigroup of [[Brownian motion|22735FGJV6]] in $\R^3$ and $f(x) = 1/\abs{x}$, with $f(0) = \infty$.
Then $f$ is a nonnegative [[superharmonic function|X4V2S56YQQ]], and averaging it against the Gaussian kernel gives $P_t f \le f$ with $P_t f \uparrow f$ as $t \downarrow 0$, so $f$ is excessive.
Non-example: for the same semigroup, let $f$ be the indicator of the single point $0$.
Then $P_t f = 0 \le f$, so clause 1 holds, but $P_t f(0) = 0$ does not tend to $f(0) = 1$, so clause 2 fails.
For Brownian motion in $\R^d$, the excessive functions are exactly the nonnegative superharmonic functions on $\R^d$, together with the constant $+\infty$.
