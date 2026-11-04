---
tag: 5VRNB5BEET
kind: proof
name: Proof that absolutely convergent series converge
msc: [40A05]
proves: 0Y123X48GA
uses: [0W3K3QPEWT, 06PVXMY0TH, 03HF5PMY5T, 0MX1HZBBXJ, 0N32V0E3XJ]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
    locator: Alternative proof using the Cauchy criterion and triangle inequality
---

## Proof

We use the Cauchy criterion for series.

1. By the definition of [[absolute convergence|0W3K3QPEWT]], the series $\sum \abs{a_n}$ converges. Let $T$ be its sum.
2. Let $\varepsilon > 0$. By the [[Cauchy criterion for series|06PVXMY0TH]] applied to $\sum \abs{a_n}$, there is $N$ with $\sum_{k=m+1}^{n} \abs{a_k} < \varepsilon$ for all $n > m \ge N$.
3. For such $m$ and $n$, the [[triangle inequality|03HF5PMY5T]], applied repeatedly, gives $\abs{\sum_{k=m+1}^{n} a_k} \le \sum_{k=m+1}^{n} \abs{a_k} < \varepsilon$.
4. By the Cauchy criterion for series again, $\sum a_n$ converges. Let $S$ be its sum and $s_N = \sum_{n=0}^{N} a_n$.
5. Let $t_N = \sum_{n=0}^{N} \abs{a_n}$. By the [[criterion for nonnegative series|0MX1HZBBXJ]], $T = \sup_N t_N$, so $t_N \le T$ for all $N$.
6. By the triangle inequality, $\abs{s_N} \le t_N \le T$. So $-T \le s_N \le T$ for every $N$.
7. Since $s_N \to S$ and [[limits preserve non-strict inequalities|0N32V0E3XJ]], $-T \le S \le T$.
8. So $\abs{\sum_{n=0}^{\infty} a_n} = \abs{S} \le T = \sum_{n=0}^{\infty} \abs{a_n}$.

## Idea

A block of terms $a_{m+1} + \cdots + a_n$ is never larger in absolute value than the same block of absolute values. If the blocks of absolute values become small, so do the original blocks, and the Cauchy criterion gives convergence.
