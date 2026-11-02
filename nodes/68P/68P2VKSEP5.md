---
tag: 68P2VKSEP5
kind: concept
name: q-gamma function
msc: ["33D05"]
sources:
  - url: https://en.wikipedia.org/wiki/Q-gamma_function
same_as:
  wikidata: Q7265303
  wikipedia: Q-gamma function
---

## Summary

The $q$-gamma function $\Gamma_q$ is a [[q-analog|GFSDMJHHVA]] of the [[gamma function|0H5SYBSED9]].
It is a quotient of two [[q-Pochhammer symbols|Y1X8ZZQ7VM]] and satisfies $\Gamma_q(x + 1) = [x]_q\, \Gamma_q(x)$, where $[x]_q = \frac{1 - q^x}{1 - q}$ is the $q$-number.
As $q \to 1^-$ it tends to $\Gamma(x)$.
It appears throughout the theory of basic hypergeometric series.

## Explanations

### L1 human

In $q$-analogs, a number $n$ is replaced by $[n]_q = 1 + q + \cdots + q^{n-1}$, which becomes $n$ again when $q = 1$.
The $q$-factorial is then $[1]_q [2]_q \cdots [n]_q$.
The $q$-gamma function fills in this $q$-factorial between the whole numbers, as the gamma function does for the factorial.
For example, $\Gamma_q(3) = [2]_q = 1 + q$, which is $2 = 2!$ when $q = 1$.
