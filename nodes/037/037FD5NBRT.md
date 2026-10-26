---
tag: 037FD5NBRT
kind: statement
role: theorem
name: Leibniz formula for pi
aliases: [madhava-leibniz-series]
msc: [40A05]
uses: [0PK8QH1W1V, 0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_formula_for_π
    locator: lead section
same_as:
  wikidata: Q97226587
  wikipedia: Leibniz formula for π
---

## Statement

The series $\sum_{n=0}^{\infty} \frac{(-1)^n}{2n + 1}$ converges, and
$$1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \frac{\pi}{4}.$$

## Remarks

The series converges by the [[alternating series test|0PK8QH1W1V]]. Its value comes from the [[power series of arctangent|0T32ME0A6H]] at $x = 1$, since $\arctan 1 = \pi/4$.
The convergence is very slow. The error after the terms up to $n = N$ is at most $1/(2N + 3)$.
Mathlib states it as a limit of partial sums, in `Real.tendsto_sum_pi_div_four`.

## History

Madhava of Sangamagrama or his school found the series in the 14th or 15th century. James Gregory found it again in 1671, and Leibniz in 1673.

## Explanations

### L1 human

Add and subtract the reciprocals of the odd numbers: $1 - 1/3 + 1/5 - \cdots$.
The result is a quarter of $\pi$, which links the odd numbers with circles.
