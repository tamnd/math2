---
tag: B2EMR1MA1H
kind: definition
name: Eulerian number
msc: [05A05, 11B83, 05A15]
defines: 5PS2496830
uses: [0BQMWCNS8S, 0RJMNEN3BJ]
sources:
  - url: https://en.wikipedia.org/wiki/Eulerian_number
---

## Definition

Let $n \ge 1$ be an integer and let $\pi$ be a [[permutation|0BQMWCNS8S]] of $\set{1, \ldots, n}$.
A *descent* of $\pi$ is an index $i$ with $1 \le i \le n - 1$ and $\pi(i) > \pi(i + 1)$.
For an integer $k$, the *Eulerian number* $A(n, k)$ is the number of permutations of $\set{1, \ldots, n}$ with exactly $k$ descents.

## Remarks

Example: for $n = 3$, the permutations in one-line notation are $123$, $132$, $213$, $231$, $312$ and $321$.
Their numbers of descents are $0, 1, 1, 1, 1, 2$, so $A(3, 0) = 1$, $A(3, 1) = 4$ and $A(3, 2) = 1$.

Non-example: the index $i = 3$ is not a descent of $\pi = 2\,4\,1\,3$, because $\pi(3) = 1 < 3 = \pi(4)$.
The descents of $\pi$ are only $i = 2$, so $\pi$ is counted by $A(4, 1)$.

Other notations are $\left\langle {n \atop k} \right\rangle$ and $E(n, k)$.
The numbers satisfy $A(n, k) = A(n, n - 1 - k)$ and $\sum_{k} A(n, k) = n!$.
They obey the recurrence $A(n, k) = (k + 1) A(n - 1, k) + (n - k) A(n - 1, k - 1)$.
An explicit formula is
$$A(n, k) = \sum_{j=0}^{k+1} (-1)^j \binom{n + 1}{j} (k + 1 - j)^n.$$
Worpitzky's identity states that $x^n = \sum_{k=0}^{n-1} A(n, k) \binom{x + k}{n}$ for $n \ge 1$.
