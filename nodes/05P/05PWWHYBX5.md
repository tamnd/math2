---
tag: 05PWWHYBX5
kind: statement
role: theorem
name: Markov's inequality
msc: ["60E15"]
uses: [0DCT0QZVQ1, 0464Z0JP2E]
sources:
  - url: https://en.wikipedia.org/wiki/Markov's_inequality
    locator: Statement
same_as:
  wikidata: Q842436
  wikipedia: Markov's inequality
---

## Statement

Let $X$ be a random variable with values in $[0, \infty)$ and let $a > 0$. Then
$$P(X \ge a) \le \frac{E[X]}{a}.$$

## Remarks

Proof: $a \, 1_{\{X \ge a\}} \le X$ pointwise. Take expectations: $a \, P(X \ge a) \le E[X]$.
More generally, for each nondecreasing $g \colon [0, \infty) \to [0, \infty)$ with $g(a) > 0$, $P(X \ge a) \le E[g(X)]/g(a)$.
Applied to $(X - E[X])^2$, the inequality gives [[Chebyshev's inequality|02HZ1BK3MW]]. Applied to $e^{tX}$, it gives the [[Chernoff bound|014PEBGDYF]].

## History

The inequality is named after Andrey Markov. It appears earlier in the work of Pafnuty Chebyshev, the teacher of Markov.

## Explanations

### L1 human

A nonnegative quantity with a small average cannot often be large.
If the mean income is $30000$, then at most one person in five can have an income of $150000$ or more.
