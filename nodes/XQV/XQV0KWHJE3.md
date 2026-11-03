---
tag: XQV0KWHJE3
kind: statement
role: proposition
name: Error threshold
msc: [92D15]
uses: [G3428M6P36, 0NT64JV96A]
about: [G3428M6P36]
sources:
  - url: https://en.wikipedia.org/wiki/Error_threshold_(evolution)
same_as:
  wikidata: Q5395724
  wikipedia: Error threshold (evolution)
---

## Statement

Consider the [[quasispecies model|G3428M6P36]] for sequences of length $L \ge 1$, with a master sequence of replication rate $\sigma > 1$ and all other sequences of replication rate $1$.
Let each site be copied correctly with probability $q \in (0, 1)$, independently, so that a copy of the master is error-free with probability $Q = q^L$.
Neglect back mutations to the master, and let $x_0(t)$ be the frequency of the master sequence, with $x_0(0) > 0$.

1. If $\sigma Q > 1$, then $x_0(t) \to (\sigma Q - 1)/(\sigma - 1) > 0$ as $t \to \infty$.
2. If $\sigma Q \le 1$, then $x_0(t) \to 0$ as $t \to \infty$.

In particular the master sequence persists if and only if $L < \ln \sigma / (-\ln q)$, and for $q$ close to $1$ this bound is approximately $\ln \sigma/(1 - q)$.

## Remarks

Without back mutations, the master frequency obeys the [[ordinary differential equation|0NT64JV96A]] $dx_0/dt = \sigma Q x_0 - \phi x_0$ with mean rate $\phi = \sigma x_0 + (1 - x_0)$.
This is the logistic equation $dx_0/dt = x_0 \big( (\sigma Q - 1) - (\sigma - 1) x_0 \big)$, whose solutions with $x_0(0) > 0$ tend to $\max(0, (\sigma Q - 1)/(\sigma - 1))$.
Example: with $\sigma = 10$ and error rate $1 - q = 10^{-4}$ per site, the master persists for $L$ up to about $\ln 10 / 10^{-4} \approx 23\,000$ sites.
The threshold $\sigma Q = 1$ means that the master must make on average at least one error-free copy per copy made by an average competitor.

## Explanations

### L1 human

A sequence that copies itself faster than its rivals still loses if its copies are too often faulty.
The error threshold is the error rate, or sequence length, beyond which the best sequence can no longer hold its ground and the population drifts over all sequences.
Longer genomes need more accurate copying.

### L2 human

The result helps explain why RNA viruses, with high mutation rates, have short genomes.
It also poses a puzzle for the origin of life: long genomes need accurate copying enzymes, and these need long genomes to encode them.
The calculation above neglects back mutations.
When they are included, the master frequency no longer drops exactly to zero, but for long sequences it becomes very small beyond the same threshold.
