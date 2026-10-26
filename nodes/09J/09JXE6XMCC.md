---
tag: 09JXE6XMCC
kind: statement
role: theorem
name: Sum of the totient over the divisors
aliases: [gauss-totient-sum]
msc: [11A25]
uses: [0VV04M41AN, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Divisor sum
---

## Statement

Let $n$ be a positive integer.
Then $\sum_{d \mid n} \varphi(d) = n$, where the sum runs over the positive divisors $d$ of $n$, and $\varphi$ is [[Euler's totient function|0VV04M41AN]].

## Remarks

The proof: sort the fractions $\frac{1}{n}, \frac{2}{n}, \dots, \frac{n}{n}$ by their denominators in lowest terms. For each divisor $d$ of $n$, exactly $\varphi(d)$ of them have the denominator $d$.
For example, for $n = 12$: $\varphi(1) + \varphi(2) + \varphi(3) + \varphi(4) + \varphi(6) + \varphi(12) = 1 + 1 + 2 + 2 + 2 + 4 = 12$.
With the [[Möbius inversion formula|07Q4TBTFVB]], the result gives $\varphi(n) = \sum_{d \mid n} \mu(d) \, n / d$.

## History

Gauss proved this identity in his Disquisitiones Arithmeticae of 1801.

## Explanations

### L1 human

Write the fractions $\frac{1}{6}, \frac{2}{6}, \dots, \frac{6}{6}$ in lowest terms: $\frac16, \frac13, \frac12, \frac23, \frac56, \frac11$.
The denominators $1, 2, 3, 6$ appear $1, 1, 2, 2$ times. These are $\varphi(1), \varphi(2), \varphi(3), \varphi(6)$, and their sum is $6$.
