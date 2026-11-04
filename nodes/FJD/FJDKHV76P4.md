---
tag: FJDKHV76P4
kind: proof
name: Proof of Dirichlet's test by summation by parts
msc: [40A05]
proves: 0V9ME8GQE7
uses: [0KN22AAW5R, 0NB643K60Q, 06PVXMY0TH, 09G6KHS6GY, 03HF5PMY5T]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_test
    locator: Proof
---

## Proof

We use summation by parts and the Cauchy criterion.

1. Let $(a_n)_{n \ge 1}$ be [[monotone|0KN22AAW5R]] with $a_n \to 0$. Let $(b_n)_{n \ge 1}$ be real with $\abs{B_n} \le M$ for all $n$, where $B_n = \sum_{k=1}^{n} b_k$ is the $n$-th [[partial sum|0NB643K60Q]].
2. Put $B_0 = 0$. Then $b_k = B_k - B_{k-1}$ for all $k \ge 1$, and $\abs{B_k} \le M$ for all $k \ge 0$.
3. Let $n > m \ge 0$. Then
$$\sum_{k=m+1}^{n} a_k b_k = \sum_{k=m+1}^{n} a_k B_k - \sum_{k=m+1}^{n} a_k B_{k-1} = \sum_{k=m+1}^{n} a_k B_k - \sum_{k=m}^{n-1} a_{k+1} B_k.$$
4. Collecting the terms with the same $B_k$ in step 3 gives the summation by parts formula
$$\sum_{k=m+1}^{n} a_k b_k = a_n B_n - a_{m+1} B_m + \sum_{k=m+1}^{n-1} (a_k - a_{k+1}) B_k.$$
5. Since $(a_n)$ is monotone, the differences $a_k - a_{k+1}$ all have the same sign. So $\sum_{k=m+1}^{n-1} \abs{a_k - a_{k+1}} = \abs{\sum_{k=m+1}^{n-1} (a_k - a_{k+1})}$.
6. The last sum telescopes to $a_{m+1} - a_n$. So $\sum_{k=m+1}^{n-1} \abs{a_k - a_{k+1}} = \abs{a_{m+1} - a_n} \le \abs{a_{m+1}} + \abs{a_n}$.
7. By step 4, the [[triangle inequality|03HF5PMY5T]], $\abs{B_k} \le M$ and step 6,
$$\abs{\sum_{k=m+1}^{n} a_k b_k} \le M \abs{a_n} + M \abs{a_{m+1}} + M \left( \abs{a_{m+1}} + \abs{a_n} \right) = 2M \left( \abs{a_n} + \abs{a_{m+1}} \right).$$
8. Let $\varepsilon > 0$. Since $a_n \to 0$, the [[epsilon-N form of the limit|09G6KHS6GY]] gives $N \ge 1$ with $\abs{a_k} < \varepsilon / (4M + 1)$ for all $k \ge N$.
9. For $n > m \ge N$, both $n$ and $m + 1$ are at least $N$. So step 7 gives $\abs{\sum_{k=m+1}^{n} a_k b_k} \le 4M \varepsilon / (4M + 1) < \varepsilon$.
10. The Cauchy criterion is stated for series indexed from $0$. Adding the term $0$ at index $0$ leaves the partial sums unchanged.
11. By step 9 and the [[Cauchy criterion for series|06PVXMY0TH]], the series $\sum_{n=1}^{\infty} a_n b_n$ converges.

## Idea

Summation by parts moves the differences from $b_n$ to $a_n$. The partial sums $B_n$ are bounded, and the differences $a_k - a_{k+1}$ have one sign, so their absolute values telescope. Every block of the series is then bounded by a multiple of a few terms $\abs{a_n}$, which tend to $0$.
