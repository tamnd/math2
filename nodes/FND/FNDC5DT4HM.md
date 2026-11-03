---
tag: FNDC5DT4HM
kind: definition
name: Amortized analysis
msc: [68W40, 68P05]
defines: CPK0J4X52Y
uses: [2TSJFYVFS8]
sources:
  - url: https://en.wikipedia.org/wiki/Amortized_analysis
---

## Definition

Consider a data structure with initial state $D_0$ and a set of operations on it.
For a sequence of operations $o_1, \dots, o_m$, let $D_i$ be the state after $o_i$ and let $c_i \ge 0$ be the actual cost of $o_i$.
Numbers $\hat{c}_1, \dots, \hat{c}_m$ are *amortized costs* for the sequence if
$$\sum_{i=1}^{j} c_i \le \sum_{i=1}^{j} \hat{c}_i \quad \text{for every } j = 1, \dots, m.$$
In the *potential method*, one fixes a function $\Phi$ from states to $\R$ with $\Phi(D) \ge \Phi(D_0)$ for every reachable state $D$, and sets
$$\hat{c}_i = c_i + \Phi(D_i) - \Phi(D_{i-1}).$$
The sum telescopes to $\sum_{i \le j} \hat{c}_i = \sum_{i \le j} c_i + \Phi(D_j) - \Phi(D_0) \ge \sum_{i \le j} c_i$, so these are amortized costs.

## Remarks

Example: a binary counter starting at $0$, where an increment flips bits and costs the number of flipped bits.
Take $\Phi$ to be the number of $1$ bits, so $\Phi \ge 0 = \Phi(D_0)$.
An increment that flips $t$ trailing $1$ bits to $0$ and one $0$ bit to $1$ has $c_i = t + 1$ and $\Phi(D_i) - \Phi(D_{i-1}) = 1 - t$, so $\hat{c}_i = 2$.
Hence $m$ increments cost at most $2m$, although a single increment can cost about $\log_2 m$.

Non-example: for the same counter with a decrement operation allowed, the potential method with this $\Phi$ gives no constant bound.
Alternating increment and decrement at $2^k - 1$ and $2^k$ flips $k + 1$ bits each time, so the actual average cost per operation is $k + 1$ and no constant amortized cost exists.
