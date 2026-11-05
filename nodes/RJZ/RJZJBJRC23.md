---
tag: RJZJBJRC23
kind: statement
role: proposition
name: Gandhi's formula
sources:
  - wikipedia: en:509009@r1362701401
    locator: Formula for primes, section Recurrence relations for primes > Gandhi's formula
    note: adopted
    mention: wikipedia://en/509009#JDBT
    sections: [Statement]
inventory: [GBYSNA6H7Y]
---

## Statement

In 1971, J. M. Gandhi proved that

$$p_n =\left\lfloor 1 - \log_{2}\left(s_{n-1}-\frac{1}{2}\right)\right\rfloor,$$

where $s_n = \sum_{d|p_n\#}\frac{\mu(d)}{2^d-1}$, $\mu$ is the [[Möbius function|0C8QENHYZW]] and $d$ runs through all divisors of $p_n\#$, the primorial of $p_n$. This formula should be seen as a [[recurrence relation|07TZV87Y0T]] for the prime numbers, expressing $p_n$ in terms of $p_1, p_2, \dots, p_{n-1}$.

This expression for $s_n$ given by Gandhi results from an application of a modified [[Sieve of Eratosthenes|0XM8ZA9RNM]] operating on the exponents of the powers of $\frac12$ in the sum $\sum_{k=1}^{\infty}\frac{1}{2^k}$ after $n$ steps. More precisely, Gandhi showed that $s_n = \frac1{2^1} + \frac1{2^{p_{n+1}}} + \dots$, where the dots represent terms with increasing exponents greater than $p_{n+1}$. There are analog recurrences where the process is done in a base $b$ other than $2$.

In 2025, a simpler expression for $s_n$ was published:

$s_n=\left\{\frac{1}{2^{p_n\#} -1}\prod _{i=1}^n \frac{2^{p_n\#}-2^{p_n\# /p_{i}}}{2^{p_n\#/p_{i}} -1}\right\}$, where $\{x\}$ denotes the fractional part of $x$.

It is based on a more clever use of the [[Sieve of Eratosthenes|0XM8ZA9RNM]] through the [[Chinese remainder theorem|0FNN9B4W64]].
