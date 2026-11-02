---
tag: H5G7CNYZEB
kind: statement
role: theorem
name: Dvoretzky–Kiefer–Wolfowitz inequality
msc: [62G30, 62G15, 60F10]
uses: [A05WR6TEK5, 0AJN7WHBJZ, 0MXMS3AE13]
about: [A05WR6TEK5]
sources:
  - url: https://en.wikipedia.org/wiki/Dvoretzky%E2%80%93Kiefer%E2%80%93Wolfowitz_inequality
same_as:
  wikidata: Q5317822
  wikipedia: Dvoretzky–Kiefer–Wolfowitz inequality
---

## Statement

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with [[cumulative distribution function|0MXMS3AE13]] $F$.
Let $F_n(x) = \frac{1}{n} \#\set{i : X_i \le x}$ be their [[empirical distribution function|A05WR6TEK5]].
Then for every $\varepsilon > 0$,
$$P\Big( \sup_{x \in \R} \abs{F_n(x) - F(x)} > \varepsilon \Big) \le 2 e^{-2 n \varepsilon^2}.$$

## Remarks

Dvoretzky, Kiefer and Wolfowitz proved in 1956 a bound of the form $C e^{-2n\varepsilon^2}$ with an unspecified constant $C$.
Massart showed in 1990 that $C = 2$ works, and this constant cannot be lowered.
The reduction to the uniform law on $[0, 1]$ uses the quantile transform.
The variable $X_i$ has the same law as $Q(U_i)$, for $U_i$ uniform and $Q$ the quantile function of $F$.
The supremum can only shrink under this change.
The hard part is the sharp tail bound for the uniform case.

Example: a confidence band.
Given $\alpha \in (0, 1)$, put $\varepsilon = \sqrt{\ln(2/\alpha) / (2n)}$, so that $2e^{-2n\varepsilon^2} = \alpha$.
Then the band $F_n(x) \pm \varepsilon$ contains the whole graph of $F$ with probability at least $1 - \alpha$.
For $n = 1000$ and $\alpha = 0.05$, this gives $\varepsilon \approx 0.043$.

The bound needs no assumption on $F$: no continuity and no moments.
It does need independence and a common law; for dependent data $F_n$ can stay far from $F$.

## Explanations

### L1 human

The empirical distribution function of a sample is the natural guess for the true distribution function.
This inequality says how good the guess is, uniformly over all $x$ at once.
The chance that the guess is off by more than $\varepsilon$ anywhere decays like $e^{-2n\varepsilon^2}$, whatever the distribution is.
So a sample of a few thousand points pins down the whole distribution function to within a few hundredths.

### L2 human

The inequality is a quantitative form of the [[Glivenko–Cantelli theorem|E7B78X780X]].
Since $\sum_n 2e^{-2n\varepsilon^2} < \infty$, the Borel–Cantelli lemma gives $\sup_x \abs{F_n - F} \to 0$ almost surely.
It also bounds the tail of the [[Kolmogorov–Smirnov|YZYHWC6C5F]] statistic: $P(\sqrt{n} D_n > t) \le 2e^{-2t^2}$ for every $n$, which matches the leading term of the limiting Kolmogorov law.
It is a common tool in learning theory and in the analysis of nonparametric estimators, because it is non-asymptotic.
