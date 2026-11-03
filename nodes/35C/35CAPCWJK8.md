---
tag: 35CAPCWJK8
kind: proof
name: Proof that the Cesàro means of a convergent sequence converge
msc: [40G05]
proves: 0RDRPBMNAC
uses: [0P0DJHBGBB, 09G6KHS6GY, 03HF5PMY5T, 0A3GWZ86AY]
sources:
  - url: https://proofwiki.org/wiki/Cesàro_Mean
---

## Proof

1. Let $\varepsilon > 0$. By the [[epsilon-N definition|09G6KHS6GY]], there is an integer $N_0$ with $|a_k - L| < \varepsilon/2$ for all $k \ge N_0$.
Let $N = \max(N_0, 1)$. Then $N \ge 1$, and $|a_k - L| < \varepsilon/2$ for all $k > N$.
2. Let $A = \sum_{k=1}^{N} |a_k - L|$. This is a fixed real number with $A \ge 0$.
3. For $n \ge 1$, the [[Cesàro mean|0P0DJHBGBB]] satisfies
$$\sigma_n - L = \frac{1}{n} \sum_{k=1}^{n} a_k - \frac{1}{n} \sum_{k=1}^{n} L = \frac{1}{n} \sum_{k=1}^{n} (a_k - L).$$
4. Let $n > N$. By the [[triangle inequality|03HF5PMY5T]] and step 3,
$$|\sigma_n - L| \le \frac{1}{n} \sum_{k=1}^{N} |a_k - L| + \frac{1}{n} \sum_{k=N+1}^{n} |a_k - L|.$$
5. The first sum equals $A$. Each of the $n - N$ terms of the second sum is less than $\varepsilon/2$, by step 1. So
$$|\sigma_n - L| \le \frac{A}{n} + \frac{n - N}{n} \cdot \frac{\varepsilon}{2} \le \frac{A}{n} + \frac{\varepsilon}{2}.$$
6. By the [[Archimedean property|0A3GWZ86AY]], there is an integer $M > \max(N, 2A/\varepsilon)$.
7. Let $n \ge M$. Then $n > N$, and $A/n \le A/M < \varepsilon/2$. If $A = 0$, this holds because $\varepsilon/2 > 0$.
8. By steps 5 and 7, $|\sigma_n - L| < \varepsilon/2 + \varepsilon/2 = \varepsilon$ for all $n \ge M$.
9. By the epsilon-N definition, $\sigma_n \to L$.

## Idea

Split the average into the first $N$ terms and the rest. The first part is a fixed amount divided by $n$, so it becomes small. The rest consists of terms that are already within $\varepsilon/2$ of $L$, and their average is too.
