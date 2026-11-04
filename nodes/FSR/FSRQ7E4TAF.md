---
tag: FSRQ7E4TAF
kind: proof
name: Proof of the power series of the complex cosine
msc: [33B10]
proves: 0Z1G2F8DGY
uses: [0A7YDKRNR6, 054VXHMCA3, 0MX1HZBBXJ]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine
    locator: Series and polynomials
---

## Proof

We add the exponential series of $iz$ and $-iz$.

1. Fix $z \in \C$. The series $\sum_{m \ge 0} \abs{z}^m / m!$ converges, since the series of the [[complex exponential|054VXHMCA3]] converges absolutely at $z$.
2. The partial sums of $\sum_{n \ge 0} \abs{z}^{2n}/(2n)!$ are at most $\sum_{m \ge 0} \abs{z}^m / m!$, because they only omit nonnegative terms. A [[series of nonnegative terms with bounded partial sums converges|0MX1HZBBXJ]]. So $\sum_{n \ge 0} (-1)^n z^{2n}/(2n)!$ converges absolutely.
3. By definition, $e^{iz} = \sum_{m \ge 0} (iz)^m/m!$ and $e^{-iz} = \sum_{m \ge 0} (-iz)^m/m!$. Both series converge.
4. The sum of two convergent series converges to the sum of their sums. So $e^{iz} + e^{-iz} = \sum_{m \ge 0} c_m z^m / m!$ with $c_m = i^m + (-i)^m$.
5. Since $(-i)^m = (-1)^m i^m$, we have $c_m = i^m (1 + (-1)^m)$. So $c_m = 0$ for odd $m$. For $m = 2n$, $c_m = 2 i^{2n} = 2(-1)^n$.
6. Let $S_M$ be the partial sum of the series in step 4 up to $m = M$. By step 5, $S_{2N+1} = \sum_{n=0}^{N} 2 (-1)^n z^{2n}/(2n)!$.
7. The sequence $(S_M)$ converges to $e^{iz} + e^{-iz}$, so its subsequence $(S_{2N+1})$ has the same limit. Hence $\sum_{n=0}^{\infty} 2(-1)^n z^{2n}/(2n)! = e^{iz} + e^{-iz}$.
8. Dividing by $2$ and using the definition of the [[complex cosine|0A7YDKRNR6]], $\cos z = \sum_{n=0}^{\infty} (-1)^n z^{2n}/(2n)!$.

## Idea

In $e^{iz} + e^{-iz}$ the odd powers of $z$ come with $i^m$ and $-i^m$, so they cancel. The even powers double, and $i^{2n} = (-1)^n$ gives the alternating signs.
