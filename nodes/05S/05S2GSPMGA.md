---
tag: 05S2GSPMGA
kind: statement
role: theorem
name: Harmonic numbers grow like log n
msc: [11B83, 26A12]
uses: [0D2Y6G4C4S, 0044CPHJBV, 0K1N1Y4EGZ, 0FM6N4R0VB, 00SB5EA3VW]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_number
    locator: Harmonic numbers for real and complex values
  - url: https://en.wikipedia.org/wiki/Euler%27s_constant
    locator: Analysis
---

## Statement

Let $H_n = \sum_{k=1}^{n} \frac{1}{k}$ be the [[harmonic numbers|0D2Y6G4C4S]].
Then the limit $\lim_{n \to \infty} (H_n - \ln n)$ exists, and it lies in $[0, 1]$.
In particular, $H_n \sim \ln n$ as $n \to \infty$.

## Remarks

Let $a_n = H_n - \ln n$. Since $\ln(n + 1) - \ln n = \int_n^{n+1} \frac{dt}{t}$ lies between $\frac{1}{n+1}$ and $\frac{1}{n}$, the sequence $a_n$ decreases. Also $a_n \ge H_n - \ln(n + 1) \ge 0$.
The [[monotone convergence theorem|0FM6N4R0VB]] gives the limit. It is the [[Euler–Mascheroni constant|00C5P9JZBK]] $\gamma$.
The symbol $\sim$ is [[asymptotic equivalence|00SB5EA3VW]]. Mathlib states the limit as `Real.tendsto_harmonic_sub_log`.

## Explanations

### L1 human

The sum $1 + 1/2 + \cdots + 1/n$ is close to the area under $1/x$ from $1$ to $n$, which is $\ln n$.
The error tends to a constant.
