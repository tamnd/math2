---
tag: WWAPSGGSAG
kind: proof
name: Proof of the p-series test by Cauchy condensation
msc: [40A05]
proves: 0ZNSSK8ZK1
uses: [0B96KMDDD1, 0VVY4H92G2, 01X5CVV1Q5, 0TV07AQT62, 0044CPHJBV, 0E8HNVBCSP, 0KN2V7840E, 0K2FNY6DYV, 0CVVKY7GY2]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_condensation_test
    locator: Examples
---

## Proof

For $n \ge 1$, write $n^{-p} = e^{-p \ln n}$, as in the definition of [[real exponentiation|0TV07AQT62]].

1. The [[natural logarithm|0044CPHJBV]] is strictly increasing. Indeed, if $0 < x < y$ and $\ln x \ge \ln y$, then $x = e^{\ln x} \ge e^{\ln y} = y$, since [[exp is strictly increasing|0KN2V7840E]]. This is impossible.
2. Since $e^0 = 1$, we have $\ln 1 = 0$. By step 1, $\ln n \ge 0$ for $n \ge 1$, and $\ln 2 > 0$.
3. Case $p \le 0$. For $n \ge 1$, $-p \ln n \ge 0$, so $n^{-p} \ge e^0 = 1$ by the monotonicity of exp. The terms do not tend to $0$, so the series diverges by the [[term test|0VVY4H92G2]].
4. Case $p > 0$. If $1 \le m < n$, then $-p \ln m > -p \ln n$ by step 1. So $m^{-p} > n^{-p}$, and the terms $a_n = n^{-p}$ form a decreasing sequence of positive numbers.
5. By the [[Cauchy condensation test|0B96KMDDD1]], $\sum a_n$ converges if and only if $\sum_{k \ge 0} 2^k a_{2^k}$ converges.
6. By the [[logarithm of a product|0K2FNY6DYV]], $\ln(2^k) = k \ln 2$. So $a_{2^k} = e^{-pk \ln 2}$ and $2^k = e^{k \ln 2}$.
7. By the [[exponential of a sum|0E8HNVBCSP]], $2^k a_{2^k} = e^{k(1-p)\ln 2} = r^k$ with $r = e^{(1-p)\ln 2} > 0$.
8. If $p > 1$, then $(1-p)\ln 2 < 0$ by step 2, so $0 < r < e^0 = 1$. The [[geometric series|01X5CVV1Q5]] $\sum r^k$ converges. By step 5, $\sum n^{-p}$ converges.
9. If $0 < p \le 1$, then $(1-p) \ln 2 \ge 0$, so $r \ge 1$ and $r^k \ge 1$ for all $k$. The condensed series diverges by the term test. By step 5, $\sum n^{-p}$ diverges.
10. Steps 3, 8 and 9 show that the series [[converges|0CVVKY7GY2]] exactly when $p > 1$.

## Idea

For $p \le 0$ the terms do not even tend to $0$. For $p > 0$ the terms decrease, so Cauchy condensation applies. It turns the series into the geometric series with ratio $2^{1-p}$, which converges exactly when this ratio is below $1$, that is, when $p > 1$.
