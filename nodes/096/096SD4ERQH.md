---
tag: 096SD4ERQH
kind: statement
role: theorem
name: Geometric solutions come from roots of the characteristic polynomial
msc: [39A06]
uses: [0ZV2YKKZ58, 0BWDJGQYST]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
    locator: Characteristic polynomial and roots
---

## Statement

Let $R$ be a commutative ring, let $E$ be a linear recurrence with constant coefficients over $R$, and let $q \in R$.
Then the sequence $(q^n)_{n \ge 0}$ is a [[solution|0ZV2YKKZ58]] of $E$ if and only if $q$ is a root of the [[characteristic polynomial|0BWDJGQYST]] $\chi_E$.

## Remarks

Proof idea: for the sequence $q^n$ the recurrence at index $n$ reads $q^n \chi_E(q) = 0$. At $n = 0$ this is $\chi_E(q) = 0$.
Over a field, if $\chi_E$ has $d$ distinct roots $q_1, \dots, q_d$, every solution is $u_n = a_1 q_1^n + \dots + a_d q_d^n$ with constants $a_i$.
[[Binet's formula|0404D8TN7Y]] is the case of the Fibonacci recurrence.

## Explanations

### L1 human

Try a solution of the form $u_n = q^n$. Put it into the recurrence and divide by $q^n$.
What is left is the equation $\chi_E(q) = 0$.
