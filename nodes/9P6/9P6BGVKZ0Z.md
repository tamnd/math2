---
tag: 9P6BGVKZ0Z
kind: proof
name: Proof of the root test
msc: [40A05]
proves: 05H4DDDYBZ
uses: [0P8BA7T7S5, 0W3K3QPEWT, 0MX1HZBBXJ, 05APWSX53S, 0M8TGGP9JP, 0VVY4H92G2, 05FQ3VGAR9]
sources:
  - url: https://en.wikipedia.org/wiki/Root_test
    locator: Proof
---

## Proof

Let $x_n = \abs{a_n}^{1/n}$ for $n \ge 1$. The term $a_0$ is a single term, and it does not affect convergence. Each $x_n \ge 0$, and $\abs{a_n} = x_n^n$.
The value $C = +\infty$ means that $(x_n)$ is not bounded above. Otherwise $(x_n)$ is a [[bounded sequence|05FQ3VGAR9]], and by the definition of the [[limit superior|0P8BA7T7S5]], $C = \inf_{N \ge 1} u_N$ with $u_N = \sup_{k \ge N} x_k$.

1. Assume $C < 1$. Then $C$ is a real number, and $C \ge 0$ because every $x_k \ge 0$. Let $r = (C + 1)/2$, so $C < r < 1$ and $r > 0$.
2. Since $C = \inf_N u_N < r$, there is $N \ge 1$ with $u_N < r$. So $x_k < r$ for every $k \ge N$.
3. Then $\abs{a_k} = x_k^k < r^k$ for $k \ge N$.
4. Let $M \ge N$. By step 3 and the [[sum of a finite geometric series|05APWSX53S]], $\sum_{k=N}^{M} \abs{a_k} \le \sum_{k=0}^{M} r^k = \frac{1 - r^{M+1}}{1 - r} \le \frac{1}{1 - r}$.
5. So every partial sum of $\sum \abs{a_n}$ is at most $\sum_{k=0}^{N-1} \abs{a_k} + 1/(1-r)$.
6. By the [[criterion for nonnegative series|0MX1HZBBXJ]], $\sum \abs{a_n}$ converges. So $\sum a_n$ converges [[absolutely|0W3K3QPEWT]].
7. Now assume $C > 1$. We claim that for each $N \ge 1$ there is $k \ge N$ with $x_k > 1$.
8. If $C = +\infty$, then $(x_n)$ is not bounded above. If $x_k \le 1$ for all $k \ge N$, then $\max(x_1, \dots, x_{N-1}, 1)$ would bound $(x_n)$ above. So some $k \ge N$ has $x_k > 1$.
9. If $C$ is a real number, then $u_N \ge C > 1$, since $C$ is the infimum of the $u_N$. By the [[approximation property of the supremum|0M8TGGP9JP]] with $c = 1 < u_N$, some $k \ge N$ has $x_k > 1$.
10. By steps 7 to 9, there are infinitely many $k$ with $x_k > 1$, and so with $\abs{a_k} = x_k^k > 1$.
11. Hence $(a_n)$ does not tend to $0$: no tail of the sequence stays in the interval $(-1, 1)$.
12. By the [[term test|0VVY4H92G2]], $\sum a_n$ diverges.

## Idea

If the $n$-th roots of $\abs{a_n}$ are eventually below some $r < 1$, then $\abs{a_n} < r^n$ and a geometric series dominates. If they exceed $1$ infinitely often, then infinitely many terms have absolute value above $1$, so the terms cannot tend to $0$.
