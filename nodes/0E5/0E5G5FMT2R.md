---
tag: 0E5G5FMT2R
kind: statement
role: theorem
name: Law of total probability
aliases: [rule-of-elimination]
msc: [60A05]
uses: [0FJB06AD2P, 09CCE86A6D]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_total_probability
    locator: Statement
same_as:
  wikidata: Q1989192
  wikipedia: Law of total probability
---

## Statement

Let $(\Omega, \mathcal{F}, P)$ be a probability space.
Let $B_1, B_2, \dots$ be a finite or countable family of pairwise disjoint events with $\bigcup_i B_i = \Omega$ and $P(B_i) > 0$ for each $i$.
Then for each event $A$,
$$P(A) = \sum_{i} P(A \mid B_i) \, P(B_i).$$

## Remarks

The events $B_i$ form a [[partition|09CCE86A6D]] of $\Omega$ into events of positive probability. The proof uses $A = \bigcup_i (A \cap B_i)$, countable additivity and the [[multiplication rule|0BS3RMX8HM]].
The case of two events $B$ and $B^c$ is the [[law of total probability for an event and its complement|0W62TKMW7V]].
Example: urn $1$ has $2$ red balls of $5$ and urn $2$ has $3$ red balls of $4$. Choose an urn with a fair coin and draw one ball. The ball is red with probability $\frac12 \cdot \frac25 + \frac12 \cdot \frac34 = \frac{23}{40}$.

## Explanations

### L1 human

Split the world into cases that do not overlap.
The chance of $A$ is the average of its chances in the cases, weighted by the chances of the cases.
