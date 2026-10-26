---
tag: 0HY1MXMEN9
kind: statement
role: proposition
name: Totient of a prime
msc: [11A25]
uses: [0VV04M41AN, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Value of phi for a prime power argument
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]].
Then $\varphi(p) = p - 1$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].

## Remarks

The proof: the only divisors of $p$ are $1$ and $p$. So each of $1, \dots, p - 1$ is coprime to $p$, and $p$ is not.
The converse holds: if $n > 1$ and $\varphi(n) = n - 1$, then $n$ is prime.
The result is the case $k = 1$ of the [[totient of a prime power|0AVY8HKBGD]].

## Explanations

### L1 human

For a prime $p$, each number from $1$ to $p - 1$ has no common factor with $p$.
For example, $\varphi(7) = 6$, because $1, 2, 3, 4, 5, 6$ are all coprime to $7$.
