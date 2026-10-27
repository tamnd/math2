---
tag: 0WETJCKNRG
kind: statement
role: theorem
name: Euclid–Euler theorem
msc: [11A25]
uses: [0SB7Q8SYSF, 06GPJF9V7M, 009QCP5T3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem
    locator: Statement and examples
  - url: https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem
    locator: History
same_as:
  wikidata: Q18206266
  wikipedia: Euclid–Euler theorem
inventory: [BJ9RZ2D7BP]
---

## Statement

Let $n$ be an even positive integer.
Then $n$ is a [[perfect number|0SB7Q8SYSF]] if and only if $n = 2^{p-1} (2^p - 1)$, where $2^p - 1$ is a [[Mersenne prime|06GPJF9V7M]].

## Remarks

The primes $2^p - 1$ for $p = 2, 3, 5, 7$ give the perfect numbers $6$, $28$, $496$ and $8128$.
So the even perfect numbers correspond one to one to the Mersenne primes.
The proof uses the multiplicativity of the [[sum of divisors|009QCP5T3Z]]: $\sigma(2^{p-1} q) = (2^p - 1)(q + 1)$ for an odd prime $q$.

## History

Euclid proved in the Elements that $2^{p-1}(2^p - 1)$ is perfect when $2^p - 1$ is prime.
Ibn al-Haytham conjectured the converse around 1000 CE.
Euler proved the converse in the 18th century, in a paper published after his death.

## Explanations

### L1 human

Euclid found a recipe for perfect numbers: take a prime of the form $2^p - 1$ and multiply it by $2^{p-1}$.
Euler showed that the recipe gives every even perfect number.
Whether an odd perfect number exists is still unknown.
