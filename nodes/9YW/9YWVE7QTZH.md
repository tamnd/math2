---
tag: 9YWVE7QTZH
kind: example
name: The greatest common divisor of two polynomials by analogy with integers
msc: ["00A35", "12E05"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [7KDT0R1HF2]
uses: [7KDT0R1HF2, 0TRNT4X7J0, 0MES3KS0ZC, Q75YRG25JK]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_greatest_common_divisor
    locator: lead section
---

## Example

Problem: find a [[greatest common divisor|Q75YRG25JK]] of the polynomials $f = x^3 - 1$ and $g = x^2 - 1$ with rational coefficients.
We solve it by [[analogy|7KDT0R1HF2]] with the integers.

1. The analogous problem. For integers, the [[Euclidean algorithm|0TRNT4X7J0]] finds $\gcd(a, b)$ by division with remainder: replace $(a, b)$ by $(b, r)$, where $a = qb + r$ and $0 \le r < b$.
2. The correspondence. Integers match polynomials, and the size $|r|$ matches the degree of $r$. The [[division algorithm for polynomials|0MES3KS0ZC]] gives $f = qg + r$ with $r = 0$ or $\deg r < \deg g$.
3. The key fact that transfers. In both settings, the common divisors of $(a, b)$ are the common divisors of $(b, r)$, because $r = a - qb$ and $a = qb + r$.
4. Divide $f$ by $g$: $x^3 - 1 = x \cdot (x^2 - 1) + (x - 1)$.
5. Divide $g$ by the remainder: $x^2 - 1 = (x + 1)(x - 1) + 0$.
6. The last nonzero remainder is $x - 1$, so $\gcd(x^3 - 1, x^2 - 1) = x - 1$, up to a nonzero constant factor.
7. Check: $x^3 - 1 = (x - 1)(x^2 + x + 1)$ and $x^2 - 1 = (x - 1)(x + 1)$, and the cofactors $x^2 + x + 1$ and $x + 1$ have no common root, since $(-1)^2 + (-1) + 1 = 1 \ne 0$.

## Remarks

The analogy can be seen in numbers.
At $x = 10$ the polynomials become $999$ and $99$, and the integer algorithm runs in the same way: $999 = 10 \cdot 99 + 9$, then $99 = 11 \cdot 9 + 0$, so $\gcd(999, 99) = 9 = 10 - 1$.
The quotients $10$ and $11$ are the values of $x$ and $x + 1$ at $x = 10$.

Step 3 is the step that must be checked in the new setting.
It uses only the ring operations, so it transfers.
The termination of the algorithm also transfers, since the degree of the remainder decreases strictly.
One change is needed: the gcd of polynomials is unique only up to a nonzero constant factor, as the gcd of integers is unique only up to sign.
The common structure behind the analogy is a [[Euclidean domain|023VY493K0]].

## Explanations

### L1 human

To find the largest number that divides both $999$ and $99$, we divide and keep the remainder: $999$ divided by $99$ leaves $9$, and $99$ divided by $9$ leaves $0$, so the answer is $9$.
Polynomials can be divided with a remainder in the same way as numbers.
So the same method finds the largest common factor of two polynomials.
For $x^3 - 1$ and $x^2 - 1$ it gives $x - 1$.
The numbers $999 = 10^3 - 1$ and $99 = 10^2 - 1$ are these polynomials at $x = 10$, and the answer $9$ is $x - 1$ at $x = 10$.

### L2 human

We use the same analogy on $f = x^6 - 1$ and $g = x^4 - 1$.

1. Divide: $x^6 - 1 = x^2 (x^4 - 1) + (x^2 - 1)$.
2. Divide: $x^4 - 1 = (x^2 + 1)(x^2 - 1) + 0$.
3. So $\gcd(x^6 - 1, x^4 - 1) = x^2 - 1$.
4. The integer analogue at $x = 2$: $\gcd(63, 15) = 3 = 2^2 - 1$.

The typical use: a method known for integers is copied step by step, and only the steps that use special properties of integers are checked again.

A trap: the gcd of $2x - 2$ and $x^2 - 1$ over $\mathbb{Q}$ is $x - 1$, not $2x - 2$ and not $2$; constants are units for polynomials over a field, as $-1$ is a unit for the integers.
