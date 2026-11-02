---
tag: JY4ZN779YG
kind: example
name: Pell numbers
msc: [11B39, 39A06]
instance_of: [06MJC8YDYR]
sources:
  - url: https://en.wikipedia.org/wiki/Pell_number
same_as:
  wikidata: Q1386491
  wikipedia: Pell number
---

## Example

The *Pell numbers* $P_n$ are the [[solution|06MJC8YDYR]] of
$$P_{n+2} = 2 P_{n+1} + P_n \qquad (n \ge 0)$$
with $P_0 = 0$ and $P_1 = 1$.
The first terms are $0, 1, 2, 5, 12, 29, 70, 169, \dots$.
The characteristic polynomial $X^2 - 2X - 1$ has roots $1 \pm \sqrt{2}$, which gives
$$P_n = \frac{(1 + \sqrt{2})^n - (1 - \sqrt{2})^n}{2\sqrt{2}}.$$
Check: the formula solves the recurrence, since each root $q$ satisfies $q^2 = 2q + 1$; it gives $P_0 = 0$ and $P_1 = 2\sqrt{2}/(2\sqrt{2}) = 1$.
They form the [[Lucas sequence|DP39F5KQ2W]] $U_n(2, -1)$.

Let $H_n$ be the solution of the same recurrence with $H_0 = H_1 = 1$, so $H_n = 1, 1, 3, 7, 17, 41, 99, \dots$.
Then $H_n^2 - 2 P_n^2 = (-1)^n$.
For example $3^2 - 2 \cdot 2^2 = 1$ and $7^2 - 2 \cdot 5^2 = -1$.
So the pairs $(H_n, P_n)$ give solutions of the [[Pell equations|0Z0NE3J6JX]] $x^2 - 2y^2 = \pm 1$, and $H_n / P_n$ tends to $\sqrt{2}$.

## Explanations

### L1 human

Pell numbers grow like the Fibonacci numbers, but each term is twice the previous one plus the one before.
Their ratio $P_{n+1}/P_n$ tends to $1 + \sqrt{2}$, about $2.414$.
The fractions $1/1, 3/2, 7/5, 17/12, 41/29, \dots$ built from them are better and better approximations of $\sqrt{2}$.
For instance $17/12 \approx 1.41667$ while $\sqrt{2} \approx 1.41421$.
