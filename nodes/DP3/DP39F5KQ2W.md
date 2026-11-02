---
tag: DP39F5KQ2W
kind: example
name: Lucas sequence
msc: [11B39, 39A06]
instance_of: [06MJC8YDYR]
sources:
  - url: https://en.wikipedia.org/wiki/Lucas_sequence
same_as:
  wikidata: Q1759646
  wikipedia: Lucas sequence
---

## Example

Fix integers $P$ and $Q$.
The *Lucas sequences* $U_n(P, Q)$ and $V_n(P, Q)$ are the [[solutions|06MJC8YDYR]] of the recurrence
$$x_{n+2} = P\, x_{n+1} - Q\, x_n \qquad (n \ge 0)$$
with initial values $U_0 = 0$, $U_1 = 1$ and $V_0 = 2$, $V_1 = P$.
The [[characteristic polynomial|0YA7X86K05]] is $X^2 - P X + Q$.
If its discriminant $D = P^2 - 4Q$ is not $0$, let $a, b$ be its two distinct complex roots; then
$$U_n = \frac{a^n - b^n}{a - b}, \qquad V_n = a^n + b^n.$$
Check: both formulas solve the recurrence, since $a^{n+2} = P a^{n+1} - Q a^n$ and likewise for $b$, and they give $U_0 = 0$, $U_1 = 1$, $V_0 = 2$, $V_1 = a + b = P$.

Special cases:

1. $P = 1$, $Q = -1$: $U_n$ are the [[Fibonacci numbers|0GA9K57A39]] $0, 1, 1, 2, 3, 5, \dots$ and $V_n$ are the Lucas numbers $2, 1, 3, 4, 7, 11, \dots$.
2. $P = 2$, $Q = -1$: $U_n$ are the [[Pell numbers|JY4ZN779YG]] $0, 1, 2, 5, 12, 29, \dots$.
3. $P = 3$, $Q = 2$: $U_n = 2^n - 1$, the Mersenne numbers $0, 1, 3, 7, 15, \dots$, since the roots are $2$ and $1$.

## Explanations

### L1 human

A Lucas sequence is a two-parameter family that contains the Fibonacci numbers and many of their relatives.
Each term is $P$ times the previous term minus $Q$ times the one before.
Changing $P$ and $Q$ gives the Fibonacci numbers, the Pell numbers, or the numbers $2^n - 1$.
Because they share one formula, facts proved once for Lucas sequences hold for all of these at the same time.
They are used in primality tests, for example the [[Lucas–Lehmer test|061BTYA0RN]] for [[Mersenne primes|0F3Z22M2GT]].
