---
tag: 07Q4TBTFVB
kind: statement
role: theorem
name: Möbius inversion formula
msc: [11A25]
uses: [0C8QENHYZW, 0ASC73QEQT, 0KH1N66QWW]
sources:
  - url: https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula
    locator: Statement of the formula
same_as:
  wikidata: Q1072771
  wikipedia: Möbius inversion formula
---

## Statement

Let $f$ and $g$ be arithmetic functions.
Then $g(n) = \sum_{d \mid n} f(d)$ for all positive integers $n$ if and only if
$$f(n) = \sum_{d \mid n} \mu(d) \, g\!\left(\frac{n}{d}\right)$$
for all positive integers $n$. Here $\mu$ is the [[Möbius function|0C8QENHYZW]].

## Remarks

In terms of the [[Dirichlet convolution|0KH1N66QWW]], the statement is: $g = f * \mathbf{1}$ if and only if $f = g * \mu$.
The proof uses [[$\mu * \mathbf{1} = \varepsilon$|0ASC73QEQT]] and the associativity of $*$.
For example, the [[sum of the totient over the divisors|09JXE6XMCC]] gives $\sum_{d \mid n} \varphi(d) = n$. So $\varphi(n) = \sum_{d \mid n} \mu(d) \, n/d$.

## History

August Ferdinand Möbius introduced the formula into number theory in 1832.

## Explanations

### L1 human

If you know all the divisor sums of $f$, the formula recovers $f$ itself.
It undoes the operation "sum over the divisors", as subtraction undoes addition.
