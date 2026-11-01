---
tag: Z2EWA10YMB
kind: definition
name: Horner's method
msc: [68W30, 13F20]
defines: FYBQ3Z52Z7
uses: [0GYGHKX834, 0Q9EZS90GY, 0GJ7T0NK49]
sources:
  - url: https://en.wikipedia.org/wiki/Horner%27s_method
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]], let $f = a_n x^n + \dots + a_1 x + a_0 \in R[x]$ with $n \ge 0$, and let $c \in R$.
Horner's method computes the elements $b_n, b_{n-1}, \dots, b_0$ of $R$ by
$$b_n = a_n, \qquad b_k = a_k + c \, b_{k+1} \quad (k = n - 1, \dots, 0),$$
and returns $b_0$.

## Remarks

The output is the value: $b_0 = f(c)$, see [[polynomial evaluation|0GJ7T0NK49]].
Moreover $f = (x - c)(b_n x^{n-1} + \dots + b_2 x + b_1) + b_0$, so the method also gives the quotient of $f$ by $x - c$.
Example: for $f = 2x^3 - 6x^2 + 2x - 1$ and $c = 3$, one gets $b_3 = 2$, $b_2 = 0$, $b_1 = 2$, $b_0 = 5$.
Check: $f(3) = 54 - 54 + 6 - 1 = 5$, and $f = (x - 3)(2x^2 + 2) + 5$.
Non-example: computing each power $c^k$ separately and then the sum gives the same value, but it is not Horner's method and uses more multiplications.
The method uses $n$ multiplications and $n$ additions.

## Explanations

### L1 human

Horner's method reads the coefficients from the top and, at each step, multiplies by $c$ and adds the next coefficient.
