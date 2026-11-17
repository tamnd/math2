---
tag: JZ9PKJAMFN
kind: example
name: Division of 17 by 5 has a unique quotient and remainder
msc: ["97E40", "11A05"]
topics: [WMY13MXY3W]
audience: school
instance_of: [ACSC75R7R5]
uses: [ACSC75R7R5, 0CHQKZFK5S]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_division
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
---

## Example

The [[division algorithm|0CHQKZFK5S]] says that for integers $a$ and $b > 0$, there is exactly one pair of integers $(q, r)$ with $a = bq + r$ and $0 \leq r < b$.
We check this [[existence and uniqueness statement|ACSC75R7R5]] for $a = 17$ and $b = 5$.

1. Existence: take $q = 3$ and $r = 2$. Then $5 \cdot 3 + 2 = 17$, and $0 \leq 2 < 5$.
2. Uniqueness: let $(q, r)$ and $(q', r')$ both satisfy the conditions.
3. Then $5q + r = 5q' + r'$, so $5(q - q') = r' - r$.
4. From $0 \leq r < 5$ and $0 \leq r' < 5$, we get $-5 < r' - r < 5$.
5. So $r' - r$ is a multiple of $5$ strictly between $-5$ and $5$. The only such multiple is $0$.
6. So $r = r'$, and then $5(q - q') = 0$ gives $q = q'$. The pair $(3, 2)$ is the only one.

## Remarks

The condition $0 \leq r < 5$ is what makes the pair unique.
Without it, $17 = 5 \cdot 2 + 7$ and $17 = 5 \cdot 4 + (-3)$ are other ways to write $17$, so existence holds but uniqueness fails.
The uniqueness argument in steps 2 to 6 works for any $a$ and $b > 0$, with $5$ replaced by $b$.

Uniqueness justifies the names "the quotient" and "the remainder", and the notation $17 \bmod 5 = 2$.
For negative $a$ the same rule gives $-17 = 5 \cdot (-4) + 3$, so the remainder of $-17$ by $5$ is $3$, not $-2$.

## Explanations

### L1 human

Share $17$ sweets among $5$ children, with each child getting the same number.
Each child gets $3$ sweets, and $2$ are left over.
The leftover must be less than $5$, or else every child could get one more.
With that rule, there is only one answer: $3$ each and $2$ left.

### L2 human

We find the quotient and remainder of $a = 100$ by $b = 7$, and we note what the uniqueness proof gives.

1. The multiples of $7$ near $100$ are $98 = 7 \cdot 14$ and $105 = 7 \cdot 15$.
2. Take $q = 14$, the largest $q$ with $7q \leq 100$. Then $r = 100 - 98 = 2$, and $0 \leq 2 < 7$.
3. By the uniqueness argument, any other pair $(q', r')$ with $0 \leq r' < 7$ has $r' = 2$ and $q' = 14$.

The typical use of uniqueness is in proofs that compare two expressions: if $a = bq + r = bq' + r'$ with both remainders in range, then the quotients and the remainders agree.

A trap: a student who checks one pair proves existence only.
Uniqueness needs the argument with two arbitrary pairs.
