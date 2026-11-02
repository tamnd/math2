---
tag: 7RP8XW5YH3
kind: example
name: Eisenstein series as a double series
msc: [40B05, 11F11]
instance_of: [PAXCH4FFSV]
uses: [EYREVY31BN, X6XGGH5FPW, 0W3K3QPEWT]
sources:
  - url: https://en.wikipedia.org/wiki/Eisenstein_series
---

## Example

Let $\tau$ be a point of the [[upper half-plane|X6XGGH5FPW]] and let $k \ge 3$ be an integer.
The [[Eisenstein series|EYREVY31BN]] $G_k(\tau) = \sum_{(m,n) \ne (0,0)} (m\tau + n)^{-k}$ is a [[double series|PAXCH4FFSV]] indexed by $\Z^2 \setminus \set{(0,0)}$.
It converges [[absolutely|0W3K3QPEWT]].
Check: since $1$ and $\tau$ are linearly independent over $\R$, there is $c > 0$ with $\abs{x\tau + y} \ge c \max(\abs{x}, \abs{y})$ for all real $x, y$.
For each integer $r \ge 1$ there are exactly $8r$ pairs $(m, n)$ with $\max(\abs{m}, \abs{n}) = r$.
So $\sum \abs{m\tau + n}^{-k} \le \sum_{r \ge 1} 8r \, (cr)^{-k} = 8 c^{-k} \sum_{r \ge 1} r^{1-k}$, which is finite because $k - 1 \ge 2$.
By absolute convergence, the sum does not depend on the order of the terms.
Summing by rows, by columns or over growing squares gives the same value.
For odd $k$ the terms for $(m,n)$ and $(-m,-n)$ cancel and $G_k = 0$, so the interesting cases are the even $k \ge 4$.

For $k = 2$ the same count gives the divergent bound $\sum 8r(cr)^{-2}$, and indeed the double series is not absolutely convergent.
Summing first over $n$ and then over $m$ still gives a value, but this function is not a modular form.
The order of summation matters here.

## Explanations

### L1 human

The Eisenstein series adds up one term for each point of a two-dimensional grid, so it is naturally a double series.
Counting the grid points on squares of growing size shows that the terms decay fast enough when $k \ge 3$.
Then the order in which the terms are added does not matter, and that is what makes the function well behaved.
