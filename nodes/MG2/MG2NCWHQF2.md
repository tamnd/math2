---
tag: MG2NCWHQF2
kind: concept
name: Binomial proportion confidence interval
msc: [62F25]
specializes: [0S6T9KQNC0]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
same_as:
  wikidata: Q1781424
  wikipedia: Binomial proportion confidence interval
---

## Summary

A binomial proportion confidence interval is a [[confidence interval|0S6T9KQNC0]] for the success probability $p$ of a [[binomial distribution|0WCWA1KT3M]].
It is computed from the number of successes in $n$ trials.
Because the data are discrete, no interval has coverage exactly $1 - \alpha$ for every $p$.
So there are several standard intervals, such as the Wald, Wilson and Clopper–Pearson intervals, with different trade-offs between coverage and length.

## Explanations

### L1 human

You toss a coin $n$ times, see $x$ heads, and want a range of plausible values for the true probability of heads.
The simplest answer is the observed proportion plus or minus about two standard errors.
For $x = 40$ heads in $n = 100$ tosses, this gives roughly $0.40 \pm 0.10$, so the interval $[0.30, 0.50]$ at level about $95\%$.
This simple interval behaves badly when $p$ is near $0$ or $1$, which is why better intervals exist.
