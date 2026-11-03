---
tag: QPBYBTD3NF
kind: definition
name: Gold code
msc: [94A55, 94A05, 11T71]
defines: 53YA8BDBTQ
uses: [H32KMWJ90G]
sources:
  - url: https://en.wikipedia.org/wiki/Gold_code
---

## Definition

Let $n \ge 3$ be an integer with $n \not\equiv 0 \pmod 4$, and let $N = 2^n - 1$.
For binary sequences $u, v$ of period $N$, let $\theta_{u,v}(\tau) = \sum_{j=0}^{N-1} (-1)^{u_j + v_{j+\tau}}$ be their periodic cross-correlation at shift $\tau$, and let $T^\tau v$ be the shifted sequence $(v_{j+\tau})_{j \ge 0}$.

1. A *preferred pair* is a pair $(u, v)$ of binary [[maximum length sequences|H32KMWJ90G]] of period $N$ with $v_j = u_{qj}$ for all $j$, for some $q$ as follows. Here $q = 2^k + 1$ or $q = 2^{2k} - 2^k + 1$ for an integer $k \ge 1$. Moreover $\gcd(n, k) = 1$ if $n$ is odd, and $\gcd(n, k) = 2$ if $n \equiv 2 \pmod 4$.
2. The *Gold code* of a preferred pair $(u, v)$ is the set of $N + 2$ sequences
$$\set{u, \; v} \cup \set{u + T^\tau v : 0 \le \tau \le N - 1},$$
with addition taken termwise in $\F_2$.

## Remarks

Let $t(n) = 1 + 2^{\lfloor (n + 2)/2 \rfloor}$.
Gold's theorem says that for a preferred pair the cross-correlation $\theta_{u,v}(\tau)$ takes only the three values $-1$, $-t(n)$ and $t(n) - 2$.
It follows that any two distinct sequences of the Gold code have periodic cross-correlation in $\set{-1, -t(n), t(n) - 2}$ at every shift.

Example: for $n = 3$, $N = 7$, let $u$ be the m-sequence $1, 0, 0, 1, 0, 1, 1, \dots$ of $s_j = s_{j-2} + s_{j-3}$, and let $v_j = u_{3j}$, which is $q = 2^1 + 1$ with $k = 1$ and $\gcd(3, 1) = 1$.
Since $\gcd(3, 7) = 1$, the sequence $v$ is again an m-sequence of period $7$, and $(u, v)$ is a preferred pair.
Here $t(3) = 5$, so the Gold code consists of $9$ sequences of period $7$ with cross-correlations in $\set{-1, -5, 3}$.

Non-example: for $n = 4$, $N = 15$, the hypothesis $n \not\equiv 0 \pmod 4$ fails, and indeed no preferred pairs of period $15$ exist.
