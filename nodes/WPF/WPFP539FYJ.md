---
tag: WPFP539FYJ
kind: definition
name: Mark and recapture estimation
msc: [62P10, 62D05, 92D40]
defines: KDWGZRTY89
uses: [0SSS6ERQ0S, 0X3Y0ZSKNF]
sources:
  - url: https://en.wikipedia.org/wiki/Mark_and_recapture
---

## Definition

Consider a closed population of unknown size $N$: no births, deaths or migration between the two samples.
A first sample of $M$ individuals is caught, marked and released.
A second sample of $C$ individuals is caught later, and $R \ge 1$ of them carry a mark.
Assume that every individual has the same probability of being caught in the second sample and that marks are not lost.
The *Lincoln–Petersen estimator* of $N$ is the [[estimator|0SSS6ERQ0S]]
$$\hat N = \frac{M C}{R}.$$
*Mark and recapture estimation* is the estimation of $N$ from such data, by $\hat N$ or by one of its refinements.

## Remarks

Under the assumptions, given $N$, $M$ and $C$, the count $R$ has a [[hypergeometric distribution|0X3Y0ZSKNF]], with mean $C M / N$; setting $R$ equal to its mean gives $\hat N$.
Example: with $M = 100$, $C = 50$ and $R = 5$, $\hat N = 100 \cdot 50 / 5 = 1000$.
Non-example of the setting: if the marked animals avoid the traps after the first capture, the equal catchability assumption fails, $R$ tends to be too small, and $\hat N$ overestimates $N$.
The Lincoln–Petersen estimator is undefined when $R = 0$ and is biased; the Chapman estimator $\frac{(M + 1)(C + 1)}{R + 1} - 1$ is defined for all $R \ge 0$ and has smaller bias.
