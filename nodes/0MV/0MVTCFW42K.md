---
tag: 0MVTCFW42K
kind: statement
role: proposition
name: Exponentials dominate powers in sequences
msc: [26A12]
uses: [0XKWSSY8P2, 0TZK91NQE3]
sources:
  - url: https://en.wikipedia.org/wiki/Big_O_notation
    locator: Exponentials dominate powers
---

## Statement

Let $k$ be a natural number and let $r$ be a real number with $r > 1$.
Then
$$\lim_{n \to \infty} \frac{n^k}{r^n} = 0.$$

## Remarks

For $k = 1$ and $r = 2$, it says $n / 2^n \to 0$. The terms are $1/2, 2/4, 3/8, 4/16, \dots$.
One proof uses the ratio of consecutive terms. The ratio $\frac{(n+1)^k}{n^k} \cdot \frac{1}{r}$ tends to $1/r < 1$, so the terms eventually shrink by a fixed factor.
In the language of [[little o notation|04TSHB9H8D]], it says $n^k = o(r^n)$.
The node [[exponential growth beats polynomial growth|0CT6CBGTYY]] gives the version for real variables.

## Explanations

### L1 human

A power such as $n^{10}$ grows fast, but an exponential such as $1.01^n$ grows faster in the end.
For small $n$ the power can be much larger. For large $n$ the exponential always wins.
