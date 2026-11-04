---
tag: BCQMW8E17F
kind: proof
name: Proof of the alternating series test
msc: [40A05]
proves: 0PK8QH1W1V
uses: [0KN22AAW5R, 0FM6N4R0VB, 0XKWSSY8P2, 0N32V0E3XJ, 0VHAVXW08V, 0RAM4E07NR, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_series_test
    locator: Proof
---

## Proof

We show that the even and the odd [[partial sums|0NB643K60Q]] are monotone and squeeze the sum.

1. For $m \le n$, $b_n \le b_m$, since $(b_n)$ is decreasing, as a [[monotone sequence|0KN22AAW5R]]. Since $b_n \to 0$ and [[limits preserve non-strict inequalities|0N32V0E3XJ]], $0 \le b_m$ for every $m$.
2. For each $m$, $s_{2m+2} = s_{2m} - (b_{2m+1} - b_{2m+2}) \le s_{2m}$. So $(s_{2m})$ is decreasing.
3. For each $m$, $s_{2m+3} = s_{2m+1} + (b_{2m+2} - b_{2m+3}) \ge s_{2m+1}$. So $(s_{2m+1})$ is increasing.
4. For each $m$, $s_{2m+1} = s_{2m} - b_{2m+1} \le s_{2m}$.
5. By steps 2 to 4, $s_1 \le s_{2m+1} \le s_{2m} \le s_0$ for every $m$.
6. By the [[monotone convergence theorem|0FM6N4R0VB]], $(s_{2m+1})$ converges to $O = \sup_m s_{2m+1}$. Applied to $(-s_{2m})$, it shows that $(s_{2m})$ converges to $E = \inf_m s_{2m}$.
7. Since $b_{2m+1} \to 0$ by [[subsequences of a convergent sequence|0VHAVXW08V]], step 4 and the [[limit of a sum|0RAM4E07NR]] give $O = E - 0 = E$. Call this number $S$.
8. Let $\varepsilon > 0$. There is $K$ with $\abs{s_{2m} - S} < \varepsilon$ and $\abs{s_{2m+1} - S} < \varepsilon$ for all $m \ge K$. So $\abs{s_N - S} < \varepsilon$ for all $N \ge 2K$.
9. So $s_N \to S$, by the definition of the [[limit|0XKWSSY8P2]], and the series converges with sum $S$.
10. By step 6, $s_{2m+1} \le S \le s_{2m}$ for every $m$, because $S$ is the supremum of the odd sums and the infimum of the even sums.
11. Let $N = 2m$ be even. By step 10, $s_{2m+1} \le S \le s_{2m}$. So $\abs{S - s_N} = s_{2m} - S \le s_{2m} - s_{2m+1} = b_{2m+1} = b_{N+1}$.
12. Let $N = 2m + 1$ be odd. By step 10 with $m + 1$, $s_{2m+1} \le S \le s_{2m+2}$. So $\abs{S - s_N} = S - s_{2m+1} \le s_{2m+2} - s_{2m+1} = b_{2m+2} = b_{N+1}$.
13. Steps 11 and 12 give $\abs{S - s_N} \le b_{N+1}$ for each $N$.

## Idea

The partial sums zigzag: down by $b_1$, up by $b_2$, down by $b_3$, and so on, with shrinking steps. So the even sums decrease, the odd sums increase, and the two families squeeze a common limit. The limit always lies between two consecutive partial sums, which gives the error bound.
