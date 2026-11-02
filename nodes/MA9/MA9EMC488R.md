---
tag: MA9EMC488R
kind: definition
name: Convergence tests
msc: [40A05]
defines: FJKV01J9F1
uses: [0JH4MN4K1C, 0CVVKY7GY2, 0NBRP6093V]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_tests
---

## Definition

Let $P$ be a property of real or complex sequences $(a_n)$.
The property $P$ is a convergence test if every [[series|0JH4MN4K1C]] $\sum a_n$ whose terms have $P$ is [[convergent|0CVVKY7GY2]].
It is a divergence test if every series $\sum a_n$ whose terms have $P$ is [[divergent|0NBRP6093V]].

## Remarks

Example: the property "there are $q < 1$ and $N$ with $\abs{a_{n+1}} \le q \abs{a_n}$ for all $n \ge N$" is a convergence test.
Indeed $\abs{a_n} \le \abs{a_N} q^{n - N}$ for $n \ge N$, and the [[comparison test|04Z5G0THN6]] with a [[geometric series|01X5CVV1Q5]] gives convergence.
Non-example: the property "$a_n \to 0$" is not a convergence test.
The terms $1/n$ of the [[harmonic series|0CXTMAY5PX]] tend to $0$, but the series diverges.
Its negation "$a_n \not\to 0$" is a divergence test.
A test is inconclusive on a series when the series has neither the property of the test nor the property of its companion divergence test.

## Explanations

### L1 human

A convergence test is a sufficient condition: when it holds, convergence is certain.
When it does not hold, nothing follows unless another test applies.
