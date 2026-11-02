---
tag: CD6CAQ6XDN
kind: statement
role: theorem
name: Raabe's test
msc: [40A05]
uses: [0CVVKY7GY2, 0NBRP6093V, 9JQEWK5405]
about: [FJKV01J9F1]
sources:
  - url: https://en.wikipedia.org/wiki/Ratio_test
---

## Statement

Let $(a_n)$ be a sequence of positive real numbers, and put
$$R_n = n \left( \frac{a_n}{a_{n+1}} - 1 \right).$$

1. If there are $r > 1$ and $N$ with $R_n \ge r$ for all $n \ge N$, then $\sum a_n$ [[converges|0CVVKY7GY2]].
2. If there is $N$ with $R_n \le 1$ for all $n \ge N$, then $\sum a_n$ [[diverges|0NBRP6093V]].

In particular, if $R_n \to R$, the series converges when $R > 1$ and diverges when $R < 1$.

## Remarks

This is [[Kummer's test|9JQEWK5405]] with $c_n = n$.
Then $\rho_n = n a_n / a_{n+1} - (n + 1) = R_n - 1$, and $\sum 1/n$ diverges.
For $R = 1$ the limit form gives no answer, and [[Bertrand's test|6T3E3AXZT7]] can then help.
Example: let $a_1 = 1/2$ and $a_{n+1} = a_n (2n+1)/(2n+2)$, so $a_n = \frac{1 \cdot 3 \cdots (2n-1)}{2 \cdot 4 \cdots (2n)}$.
The [[ratio test|0QNY6ZBXPN]] fails, since $a_{n+1}/a_n \to 1$.
Here $R_n = n/(2n+1) \le 1$, so $\sum a_n$ diverges.
For $a_n = 1/n^p$ one gets $R_n \to p$, which recovers the [[p-series test|0ZNSSK8ZK1]] for $p \ne 1$.

## Explanations

### L1 human

Raabe's test is a sharper version of the ratio test.
It is used when the ratio of consecutive terms tends to $1$.
It measures how fast the ratio approaches $1$: a gap like $p/n$ with $p > 1$ means convergence.

### L2 human

The ratio test compares a series with a geometric series.
Raabe's test compares it with the $p$-series $\sum 1/n^p$ instead, through Kummer's test with weights $c_n = n$.
It settles many series whose terms are quotients of products, such as binomial and hypergeometric coefficients.
[[Gauss's test|A7MJXJERNY]] is a convenient form when $a_n / a_{n+1}$ has an expansion in powers of $1/n$.
