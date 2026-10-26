---
tag: 0CN97GADE5
kind: statement
role: theorem
name: Abel's test
msc: [40A05]
uses: [0CVVKY7GY2, 0KN22AAW5R, 05FQ3VGAR9]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%27s_test
    locator: Abel's test in real analysis
same_as:
  wikidata: Q479834
  wikipedia: Abel's test
---

## Statement

Let $\sum a_n$ be a [[convergent|0CVVKY7GY2]] real series.
Let $(b_n)$ be a [[monotone|0KN22AAW5R]] and [[bounded|05FQ3VGAR9]] real sequence.
Then the series $\sum a_n b_n$ converges.

## Remarks

The sequence $(b_n)$ converges to some $b$, by the [[monotone convergence theorem|0FM6N4R0VB]]. Then $\sum a_n b_n = \sum a_n (b_n - b) + b \sum a_n$.
The first series converges by [[Dirichlet's test|0V9ME8GQE7]], since $b_n - b$ is monotone with limit $0$.
The hypotheses on $\sum a_n$ are stronger than in Dirichlet's test, and those on $(b_n)$ are weaker.

## History

Niels Henrik Abel proved the test in 1826.

## Explanations

### L1 human

Multiplying the terms of a convergent series by a bounded monotone sequence of weights keeps convergence.
The weights settle down to a limit, so they cannot disturb the series too much.
