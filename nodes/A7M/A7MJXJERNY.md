---
tag: A7MJXJERNY
kind: statement
role: theorem
name: Gauss's test
msc: [40A05]
uses: [0CVVKY7GY2, 0NBRP6093V, CD6CAQ6XDN, 6T3E3AXZT7]
about: [FJKV01J9F1]
sources:
  - url: https://en.wikipedia.org/wiki/Ratio_test
---

## Statement

Let $(a_n)$ be a sequence of positive real numbers.
Assume that there are a real number $h$, a real number $s > 1$ and a bounded real sequence $(\beta_n)$ with
$$\frac{a_n}{a_{n+1}} = 1 + \frac{h}{n} + \frac{\beta_n}{n^s}$$
for all $n \ge 1$.
Then $\sum a_n$ [[converges|0CVVKY7GY2]] if $h > 1$, and [[diverges|0NBRP6093V]] if $h \le 1$.

## Remarks

The quantity of [[Raabe's test|CD6CAQ6XDN]] is $n(a_n/a_{n+1} - 1) = h + \beta_n n^{1-s}$, which tends to $h$.
So Raabe's test settles the cases $h > 1$ and $h < 1$.
For $h = 1$, the quantity of [[Bertrand's test|6T3E3AXZT7]] is $\beta_n n^{1-s} \ln n$, which tends to $0$, so the series diverges.
Example: let $a, b, c > 0$ and let $a_n$ be the $n$-th term of the hypergeometric series $\sum_n \frac{(a)_n (b)_n}{(c)_n \, n!}$, where $(x)_n = x(x+1)\cdots(x+n-1)$.
Then $a_n / a_{n+1} = \frac{(n + c)(n + 1)}{(n + a)(n + b)} = 1 + \frac{c + 1 - a - b}{n} + O(1/n^2)$.
So the series converges exactly when $c > a + b$.

## Explanations

### L1 human

Gauss's test reads off convergence from the expansion of the ratio $a_n / a_{n+1}$ in powers of $1/n$.
Only the coefficient $h$ of $1/n$ matters: above $1$ the series converges, otherwise it diverges.
It is the natural test for terms that are products of linear factors in $n$.

### L2 human

Gauss's test packages Raabe's test and Bertrand's test into one statement for ratios with an asymptotic expansion.
A classical application is the convergence of the hypergeometric series at $x = 1$, as in the example above.
The error term must be $O(1/n^s)$ with $s > 1$; an error like $1/(n \ln n)$ would hide the boundary case.
