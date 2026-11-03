---
tag: B3DM1AYBVE
kind: definition
name: Decision problem
msc: [68Q01, 03D35]
defines: YAVW1XHNFH
uses: [5VRS8PJEFT, FS5W99H8SA]
sources:
  - url: https://en.wikipedia.org/wiki/Decision_problem
---

## Definition

Let $\Sigma$ be an alphabet.
A *decision problem* over $\Sigma$ is a [[formal language|5VRS8PJEFT]] $L \subseteq \Sigma^*$.
Its instances are the strings $w \in \Sigma^*$, the yes-instances are the strings in $L$, and the no-instances are the strings not in $L$.

More generally, a decision problem is given by a set $I$ of instances and a subset $Y \subseteq I$ of yes-instances.
With an [[encoding|FS5W99H8SA]] $e \colon I \to \Sigma^*$, it corresponds to the language $e(Y) \subseteq \Sigma^*$.

## Remarks

Example: PRIMES is the set of binary numerals of prime numbers, a language over $\set{0, 1}$.
The string $111$ is a yes-instance, since $7$ is prime, and $110$ is a no-instance, since $6$ is not.
Non-example: computing the greatest common divisor of two numbers is not a decision problem.
Its answers are numbers, not yes or no.
It is a function problem; a related decision problem asks whether the greatest common divisor of $a$ and $b$ equals $1$.
For computability, the choice of a reasonable encoding does not matter.
For complexity, the encoding should not inflate the input.
Writing $n$ in unary instead of binary can change a running time from exponential to polynomial in the input length.
