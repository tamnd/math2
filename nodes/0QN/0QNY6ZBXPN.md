---
tag: 0QNY6ZBXPN
kind: statement
role: theorem
name: Ratio test
aliases: [d-alembert-ratio-test]
msc: [40A05]
uses: [0W3K3QPEWT, 04Z5G0THN6, 01X5CVV1Q5]
sources:
  - url: https://en.wikipedia.org/wiki/Ratio_test
    locator: The test
same_as:
  wikidata: Q165638
  wikipedia: Ratio test
---

## Statement

Let $(a_n)$ be a real sequence with $a_n \ne 0$ for all $n$.
Assume that $|a_{n+1}| / |a_n| \to L$ as $n \to \infty$, for a real number $L$ with $L < 1$.
Then the series $\sum a_n$ converges [[absolutely|0W3K3QPEWT]].

## Remarks

Choose $q$ with $L < q < 1$. For $n \ge N$ we get $|a_{n+1}| \le q |a_n|$, so $|a_n| \le |a_N| q^{n-N}$. The [[comparison test|04Z5G0THN6]] with a [[geometric series|01X5CVV1Q5]] gives the result.
For $L > 1$ the series diverges, as the [[divergence part of the ratio test|08AM0KRCZ1]] states.
For $L = 1$ the test gives no answer. The series $\sum 1/n$ diverges and $\sum 1/n^2$ converges, and both have $L = 1$.
For example, $\sum x^n / n!$ converges for each real $x$, since the ratio is $|x|/(n+1) \to 0$.

## Explanations

### L1 human

If each term is eventually less than a fixed fraction $q < 1$ of the term before, the terms shrink at least as fast as $q^n$.
So the series behaves at least as well as a convergent geometric series.
