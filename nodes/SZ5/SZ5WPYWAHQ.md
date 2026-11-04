---
tag: SZ5WPYWAHQ
kind: proof
name: Proof of the term test
msc: [40A05]
proves: 0VVY4H92G2
uses: [0CVVKY7GY2, 0NB643K60Q, 0K0H5E3Z5N, 0XKWSSY8P2, 03HF5PMY5T]
sources:
  - url: https://en.wikipedia.org/wiki/Term_test
---

## Proof

1. Let $s_N = \sum_{n=0}^{N} a_n$ be the [[partial sums|0NB643K60Q]]. Since the series is a [[convergent series|0CVVKY7GY2]], $s_N \to S$ for a real number $S$, the [[sum of the series|0K0H5E3Z5N]].
2. For each $n \ge 1$, the partial sums satisfy $a_n = s_n - s_{n-1}$.
3. Let $\varepsilon > 0$. By the definition of the [[limit|0XKWSSY8P2]], there is $N$ with $\abs{s_m - S} < \varepsilon / 2$ for all $m \ge N$.
4. Let $n \ge N + 1$. Then both $n \ge N$ and $n - 1 \ge N$.
5. By step 2 and the [[triangle inequality|03HF5PMY5T]], $\abs{a_n} = \abs{(s_n - S) + (S - s_{n-1})} \le \abs{s_n - S} + \abs{s_{n-1} - S}$.
6. By steps 3 and 4, the right side of step 5 is less than $\varepsilon/2 + \varepsilon/2 = \varepsilon$.
7. So $\abs{a_n - 0} < \varepsilon$ for all $n \ge N + 1$. Since $\varepsilon > 0$ was arbitrary, $a_n \to 0$.
8. The second form is the contrapositive of the first. If $(a_n)$ does not converge to $0$, the series cannot converge, by steps 1 to 7. So it diverges.

## Idea

Each term is the difference of two consecutive partial sums. When the partial sums settle down to a limit, consecutive ones get close to each other, so their difference tends to $0$.
