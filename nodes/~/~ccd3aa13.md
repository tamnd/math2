---
tag: ~ccd3aa13
kind: statement
role: theorem
name: Kummer's theorem
msc: [11B65]
uses: [~f525df69]
sources:
  - url: https://en.wikipedia.org/wiki/Kummer%27s_theorem
    locator: Statement
same_as:
  wikidata: Q6443980
  wikipedia: Kummer's theorem
---

## Statement

Let $p$ be a prime number, and let $m$ and $n$ be natural numbers.
Then $\nu_p \binom{m + n}{m}$ is the number of carries when one adds $m$ and $n$ in base $p$. Here $\nu_p$ is the [[p-adic valuation|~f525df69]].

## Remarks

For example, in base $2$, $3 + 1 = 11_2 + 1_2 = 100_2$ has $2$ carries, and $\binom{4}{1} = 4 = 2^2$.
The theorem follows from [[Legendre's formula|~48c549d4]] in the form with the digit sums $s_p$.
A consequence: $p \mid \binom{m+n}{m}$ if and only if there is at least one carry.

## History

Ernst Kummer proved the theorem in 1852.

## Explanations

### L1 human

Write $m$ and $n$ in base $p$ and add them by hand. Count how many times you carry a $1$.
That count is the exponent of $p$ in the binomial coefficient $\binom{m+n}{m}$.
For $p = 10$ the rule fails, because $10$ is not prime. The theorem needs a prime base.
