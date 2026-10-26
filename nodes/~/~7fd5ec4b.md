---
tag: ~7fd5ec4b
kind: statement
role: theorem
name: Fraction in lowest terms
aliases: [irreducible-fraction, reduced-fraction]
msc: [11A05]
uses: [~e25d26db, ~3fed16db]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_fraction
    locator: Uniqueness
  - url: https://en.wikipedia.org/wiki/Rational_number
    locator: Irreducible fraction
---

## Statement

Let $q$ be a [[rational number|~e25d26db]].
Then there is exactly one pair of [[integers|~3fed16db]] $a$ and $b$ with $b > 0$, $\gcd(a, b) = 1$ and $q = a / b$.

## Remarks

The fraction $a / b$ is the irreducible fraction, or the fraction in lowest terms, of $q$.
To find it from any fraction $c / d$ with $d \neq 0$, divide $c$ and $d$ by $\pm \gcd(c, d)$, with the sign that makes the denominator positive.
For example, $-6 / -4$ has lowest terms $3 / 2$.

## Explanations

### L1 human

You can simplify each fraction until the top and the bottom have no common factor larger than $1$.
For example, $12 / 18$ becomes $2 / 3$ when you divide both numbers by $6$.
The result does not depend on the order of the simplification steps.
