---
tag: 0S4EMDQS2F
kind: statement
role: theorem
name: Abel's theorem
aliases: [abel-limit-theorem]
msc: [40A30]
uses: [0VP56B4EMX, 0CVVKY7GY2, 0909PWZR62]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%27s_theorem
    locator: Theorem
same_as:
  wikidata: Q318767
  wikipedia: Abel's theorem
---

## Statement

Let $(a_n)$ be a real sequence such that the series $\sum_{n=0}^{\infty} a_n$ [[converges|0CVVKY7GY2]].
Let $G(x) = \sum_{n=0}^{\infty} a_n x^n$ for $-1 < x < 1$.
Then $G(x) \to \sum_{n=0}^{\infty} a_n$ as $x \to 1$ from the left.

## Remarks

The [[power series|0VP56B4EMX]] converges on $(-1, 1)$, since its radius of convergence is at least $1$.
The theorem gives the sum of the [[alternating harmonic series|0JQ5Y3WWVE]]. Apply it to the [[Mercator series|0YZXNE3HFR]] for $\ln(1 + x)$.
The converse fails. For $a_n = (-1)^n$, $G(x) = 1/(1 + x) \to 1/2$, but $\sum (-1)^n$ diverges.
Mathlib states it as `Real.tendsto_tsum_powerSeries_nhdsWithin_lt`.

## Explanations

### L1 human

A power series that converges at the endpoint $x = 1$ is continuous there from the left.
So its value at $1$ is the limit of its values inside the interval.
