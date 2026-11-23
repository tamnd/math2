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

We find a [[greatest common divisor|Q75YRG25JK]] of $f = x^3 - 1$ and $g = x^2 - 1$ over $\mathbb{Q}$ by [[analogy|7KDT0R1HF2]] with the integers, and we run the integer version beside it.

1. We recall the integer method.
   The [[Euclidean algorithm|0TRNT4X7J0]] replaces the pair $(a, b)$ by $(b, r)$, where $a = qb + r$ and $0 \le r < b$, until the remainder is $0$.
2. We set up the correspondence.
   Integers match polynomials, and the size of a remainder matches its degree.
   The [[division algorithm for polynomials|0MES3KS0ZC]] gives $f = qg + r$ with $r = 0$ or $\deg r < \deg g$, which is the analogue of $0 \le r < b$.
3. We check the step that the method rests on.
   The common divisors of $(a, b)$ are the common divisors of $(b, r)$, because $r = a - qb$ and $a = qb + r$.
   This uses only addition and multiplication, so it holds for polynomials as well.
4. We divide $f$ by $g$:
   $$x^3 - 1 = x \cdot (x^2 - 1) + (x - 1).$$
5. We divide $g$ by the remainder:
   $$x^2 - 1 = (x + 1)(x - 1) + 0.$$
6. The last nonzero remainder is $x - 1$, so $\gcd(x^3 - 1, x^2 - 1) = x - 1$, up to a nonzero constant factor.
7. We check by factoring.
   We have $x^3 - 1 = (x - 1)(x^2 + x + 1)$ and $x^2 - 1 = (x - 1)(x + 1)$.
   The cofactors have no common root, since the only root of $x + 1$ is $-1$ and $(-1)^2 + (-1) + 1 = 1 \ne 0$.

## Remarks

The analogy shows up in plain numbers.
At $x = 10$ the two polynomials become $999$ and $99$, and the integer algorithm runs the same way:
$$999 = 10 \cdot 99 + 9, \qquad 99 = 11 \cdot 9 + 0.$$
So $\gcd(999, 99) = 9$, which is $x - 1$ at $x = 10$, and the quotients $10$ and $11$ are the values of $x$ and $x + 1$.

Two parts of the integer argument needed a new check.
The algorithm stops because the degree of the remainder falls at each step, as the size of the remainder falls for integers.
The answer is unique only up to a nonzero constant, just as the integer answer is unique only up to sign, because the nonzero constants are the units of $\mathbb{Q}[x]$.
The structure that both settings share is a [[Euclidean domain|023VY493K0]].

## Explanations

### L1 human

To find the largest number that divides both $999$ and $99$, divide and keep the remainder.
$999$ divided by $99$ leaves $9$, and $99$ divided by $9$ leaves $0$, so the answer is $9$.
Polynomials can also be divided with a remainder, so the same method finds their largest common factor.
For $x^3 - 1$ and $x^2 - 1$ it gives $x - 1$.
The numbers $999 = 10^3 - 1$ and $99 = 10^2 - 1$ are these polynomials at $x = 10$, and $9$ is $x - 1$ at $x = 10$.

### L2 human

We run the same analogy on $x^6 - 1$ and $x^4 - 1$.
Divide, then divide again:
$$x^6 - 1 = x^2 (x^4 - 1) + (x^2 - 1), \qquad x^4 - 1 = (x^2 + 1)(x^2 - 1) + 0.$$
So the greatest common divisor is $x^2 - 1$.
The integer shadow at $x = 2$ is $\gcd(63, 15) = 3 = 2^2 - 1$.

This is the typical use of the analogy: copy the integer method step by step, and check again only the steps that use special properties of integers.
Watch out for constants: over $\mathbb{Q}$, the greatest common divisor of $2x - 2$ and $x^2 - 1$ is $x - 1$ up to a constant, so $2x - 2$ is an equally good answer, but $2$ is wrong, since $2$ is a unit and divides everything.
