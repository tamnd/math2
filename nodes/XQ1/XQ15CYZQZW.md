---
tag: XQ15CYZQZW
kind: proof
name: Proof that every real number has a decimal expansion, with digits from the floor
msc: [11A63]
proves: 047KEVEZ9Q
uses: [06XY4X9430, 0YVRNEDSVG, 0R9B0B5458, 0C4JS9RF5M, 0M1MX28VXK, 0WH916TJNY, 09G6KHS6GY, 0RAM4E07NR, 0CVVKY7GY2, 0K0H5E3Z5N]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Decimal_representation
    locator: Finite decimal approximations
---

## Proof

1. Let $x \ge 0$ be real. For each natural number $k$, let $f_k = \floor{10^k x}$, the [[floor|0YVRNEDSVG]] of $10^k x$.
2. Let $a_0 = f_0 = \floor{x}$. Since $0$ is an [[integer|0C4JS9RF5M]] with $0 \le x$, we get $a_0 \ge 0$. So $a_0$ is a natural number.
3. For $k \ge 1$, let $d_k = f_k - 10 f_{k-1}$. This is an integer.
4. We show $0 \le d_k \le 9$. Let $u = 10^{k-1} x$ and $m = f_{k-1}$. By the [[characterization of the floor|0R9B0B5458]], $m \le u < m + 1$.
5. Multiply by $10$: $10 m \le 10^k x < 10 m + 10$.
6. The integer $10 m$ is at most $10^k x$, so $10 m \le f_k$, because $f_k$ is the greatest such integer. Hence $d_k \ge 0$.
7. Also $f_k \le 10^k x < 10 m + 10$. The integer $f_k$ is less than the integer $10m + 10$, so $f_k \le 10 m + 9$. Hence $d_k \le 9$.
8. For $K \ge 0$, let $s_K = a_0 + \sum_{k=1}^{K} d_k 10^{-k}$. We show $s_K = f_K / 10^K$ by induction on $K$.
9. For $K = 0$, $s_0 = a_0 = f_0$. If $s_{K-1} = f_{K-1}/10^{K-1}$, then $s_K = f_{K-1}/10^{K-1} + (f_K - 10 f_{K-1})/10^K = f_K / 10^K$.
10. By the characterization of the floor, $f_K \le 10^K x < f_K + 1$. Divide by $10^K$: $s_K \le x < s_K + 10^{-K}$. So $0 \le x - s_K < 10^{-K}$.
11. By [[Bernoulli's inequality|0M1MX28VXK]] with $9$ in place of $x$, $10^K = (1 + 9)^K \ge 1 + 9K > K$ for each $K$.
12. Let $\varepsilon > 0$. By the [[Archimedean property|0WH916TJNY]], there is $n \ge 1$ with $1/n < \varepsilon$.
13. For $K \ge n$, step 11 gives $10^K > K \ge n$, so $10^{-K} < 1/n < \varepsilon$. With step 10, $\abs{x - s_K} < \varepsilon$.
14. By the [[epsilon-N form of the limit|09G6KHS6GY]], $s_K \to x$ as $K \to \infty$.
15. The partial sums of the series $\sum_{k \ge 1} d_k 10^{-k}$ are $s_K - a_0$. By the [[limit of a sum|0RAM4E07NR]], with the constant sequence $-a_0$, they tend to $x - a_0$.
16. So the series [[converges|0CVVKY7GY2]], and its [[sum|0K0H5E3Z5N]] is $x - a_0$. That is, $x = a_0 + \sum_{k=1}^{\infty} d_k 10^{-k}$, with digits $d_k \in \set{0, \dots, 9}$ by steps 6 and 7.

## Idea

The truncation of $x$ to $K$ decimal places is $\floor{10^K x}/10^K$. Consecutive truncations differ by one digit, which lies between $0$ and $9$. The truncations are within $10^{-K}$ of $x$, so the series converges to $x$.
