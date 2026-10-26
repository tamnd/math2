---
tag: 05H4DDDYBZ
kind: statement
role: theorem
name: Root test
aliases: [cauchy-root-test]
msc: [40A05]
uses: [0P8BA7T7S5, 0W3K3QPEWT, 04Z5G0THN6, 01X5CVV1Q5]
sources:
  - url: https://en.wikipedia.org/wiki/Root_test
    locator: Root test explanation
same_as:
  wikidata: Q846705
  wikipedia: Root test
---

## Statement

Let $(a_n)$ be a real sequence and let $C = \limsup_{n \to \infty} |a_n|^{1/n}$, the [[limit superior|0P8BA7T7S5]], with the value $+\infty$ allowed.
If $C < 1$, then the series $\sum a_n$ converges [[absolutely|0W3K3QPEWT]].
If $C > 1$, then the series $\sum a_n$ diverges.

## Remarks

If $C < 1$, choose $q$ with $C < q < 1$. Then $|a_n| \le q^n$ for large $n$, and the [[comparison test|04Z5G0THN6]] with a [[geometric series|01X5CVV1Q5]] applies.
If $C > 1$, then $|a_n| > 1$ for infinitely many $n$, so the terms do not tend to $0$.
For $C = 1$ the test gives no answer.
The root test is stronger than the [[ratio test|0QNY6ZBXPN]]: when the ratio limit exists, the root limit exists and has the same value.

## Explanations

### L1 human

The $n$-th root of $|a_n|$ measures how fast the terms shrink, compared with a geometric sequence $q^n$.
If this rate is below $1$, the terms shrink like a convergent geometric series.
