---
tag: 7GWJ6ZGY37
kind: proof
name: Proof of the limit of the cumulative distribution function at infinity
msc: ["60E05"]
proves: 0RJ5TZH6G0
uses: [0MXMS3AE13, 0DKRR22AEQ, 0X8HBKCSYB, 0XD22PBMWA, 0A3GWZ86AY, 09G6KHS6GY]
sources:
  - url: https://proofwiki.org/wiki/Limit_of_Cumulative_Distribution_Function_at_Positive_Infinity
---

## Proof

1. Let $X$ be a real [[random variable|0DKRR22AEQ]] on a probability space $(\Omega, \mathcal{F}, P)$, with [[cumulative distribution function|0MXMS3AE13]] $F_X(t) = P(X \le t)$.
2. For each integer $n \ge 1$ let $A_n = \set{X \le n}$. It is an event, because $(-\infty, n]$ is a Borel set, and $P(A_n) = F_X(n)$.
3. The events increase: if $X(\omega) \le n$, then $X(\omega) \le n + 1$. So $A_n \subseteq A_{n+1}$.
4. Their union is $\Omega$. Let $\omega \in \Omega$. The value $X(\omega)$ is a real number, so by the [[Archimedean property|0A3GWZ86AY]] there is $n \ge 1$ with $n > X(\omega)$. Then $\omega \in A_n$.
5. By [[continuity from below|0X8HBKCSYB]], $F_X(n) = P(A_n) \to P(\Omega) = 1$ as $n \to \infty$.
6. Let $\varepsilon > 0$. By [[the ε-N form of the limit|09G6KHS6GY]] and step 5, there is an integer $N \ge 1$ with $\abs{F_X(N) - 1} < \varepsilon$, that is, $F_X(N) > 1 - \varepsilon$.
7. Let $x \ge N$. The function $F_X$ is [[nondecreasing|0XD22PBMWA]], so $F_X(x) \ge F_X(N) > 1 - \varepsilon$. Also $F_X(x) \le 1$, because $F_X(x)$ is a probability.
8. So $\abs{F_X(x) - 1} < \varepsilon$ for all $x \ge N$. Since $\varepsilon > 0$ was arbitrary, $\lim_{x \to +\infty} F_X(x) = 1$.

## Idea

The events $\set{X \le n}$ grow and eventually catch every outcome, because $X$ takes only real values. Continuity from below makes their probabilities tend to $1$. Monotonicity of $F_X$ then carries the limit from the integers to all real $x$.
