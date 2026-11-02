---
tag: 3RQ2PT36KQ
kind: definition
name: Daniell integral
msc: [28C05, 28A25]
defines: 4KCBFQS9WR
uses: [05EGHEQZAW, 056FSKG32J]
sources:
  - url: https://en.wikipedia.org/wiki/Daniell_integral
---

## Definition

Let $X$ be a set and let $H$ be a set of functions $X \to \R$ with the following property.
$H$ is a [[vector space|05EGHEQZAW]] under pointwise operations, and $\max(h, 0) \in H$ for every $h \in H$.
A *Daniell integral*, or elementary integral, on $H$ is a map $I \colon H \to \R$ such that:

1. $I$ is linear.
2. $I$ is positive: $I(h) \ge 0$ for every $h \in H$ with $h \ge 0$.
3. If $h_1 \ge h_2 \ge \cdots$ in $H$ and $h_n \to 0$ [[pointwise|056FSKG32J]] on $X$, then $I(h_n) \to 0$.

## Remarks

Example: let $H$ be the continuous functions $\R \to \R$ with compact support, and $I(h) = \int h(x) \, dx$, the Riemann integral.
Linearity and positivity are clear.
For clause 3, all $h_n$ vanish outside a compact interval $K$ that contains the support of $h_1$.
By Dini's theorem $h_n \to 0$ uniformly on $K$, so $0 \le I(h_n) \le \max h_n \cdot \operatorname{length}(K) \to 0$.

Non-example: let $H$ be the convergent real sequences on $X = \N$, and $I(h) = \lim_{n \to \infty} h(n)$.
Clauses 1 and 2 hold.
Clause 3 fails: $h_n = \mathbf{1}_{\set{n, n+1, \dots}}$ decreases to $0$ pointwise, but $I(h_n) = 1$ for all $n$.

Daniell's construction extends $I$ to a class of integrable functions on which the monotone and dominated convergence theorems hold.
