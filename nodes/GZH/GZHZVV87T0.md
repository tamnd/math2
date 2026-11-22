---
tag: GZHZVV87T0
kind: example
name: The greatest common divisor is unique
msc: ["00A35", "11A05"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [5P955TVSS2]
uses: [5P955TVSS2, 0C8WYW4KYQ, 0PG2H7WKGG, 0DQVHMYAGA]
sources:
  - url: https://en.wikipedia.org/wiki/Greatest_common_divisor
    locator: Definition
---

## Example

Let $a$ and $b$ be integers, not both $0$.
We use this definition of the [[greatest common divisor|0C8WYW4KYQ]]: $\gcd(a, b)$ is the integer $d \ge 0$ such that $d \mid a$, $d \mid b$, and every common divisor of $a$ and $b$ divides $d$.
The word "the" makes this a [[definite description|5P955TVSS2]], so we prove existence and uniqueness before we use the name.

1. Existence.
   The set of positive integers of the form $ax + by$ with integers $x, y$ is nonempty, because $a^2 + b^2 > 0$ is one of them.
   Let $d = ax + by$ be its least element.
   Divide: $a = qd + r$ with $0 \le r < d$.
   Then $r = a(1 - qx) + b(-qy)$ has the same form, so $r > 0$ would contradict the choice of $d$.
   So $r = 0$ and $d \mid a$, and in the same way $d \mid b$.
   This is the argument behind [[Bézout's identity|0DQVHMYAGA]].
2. The number $d$ satisfies the last condition.
   If $c \mid a$ and $c \mid b$, then $c$ divides $ax + by = d$.
3. Uniqueness.
   Let $d \ge 0$ and $d' \ge 0$ both satisfy the definition.
   Each is a common divisor, so the last condition for $d$ gives $d' \mid d$, and the last condition for $d'$ gives $d \mid d'$.
4. Neither number is $0$.
   If $d = 0$, then $d \mid a$ forces $a = 0$ and $d \mid b$ forces $b = 0$, which the hypothesis excludes.
5. Write $d = k d'$ and $d' = l d$ with integers $k, l$.
   Then $d = k l d$, and since $d \ne 0$ we get $k l = 1$, so $k = \pm 1$.
6. So $d = \pm d'$, and since both are positive, $d = d'$.

## Remarks

The sign condition $d \ge 0$ is the extra condition that makes "the" legal.
Without it, both $d$ and $-d$ satisfy the divisibility conditions, and step 6 would stop at $d = \pm d'$.

The school definition, "the largest common divisor", has an easier uniqueness proof, since a finite set of integers has at most one largest element.
Its existence proof needs the common divisors to form a finite nonempty set: $1$ is always one, and each is at most $\max(|a|, |b|)$ in size.
The two definitions give the same number, because the $d$ above is a common divisor and every common divisor $c$ divides $d$, so $|c| \le d$.
The divisibility definition is the one that generalizes to rings, where "largest" has no meaning.
In a general integral domain a gcd is unique only up to multiplication by a unit, so books there write "a gcd".

## Explanations

### L1 human

The greatest common divisor of $12$ and $18$ is the largest number that divides both.
The positive numbers that divide both are $1$, $2$, $3$ and $6$.
The largest of them is $6$.
A list of numbers has only one largest member, so "the greatest common divisor" names exactly one number.

### L2 human

Uniqueness gives a way to check a computed gcd: show that the candidate satisfies the definition, and uniqueness does the rest.
The [[Euclidean algorithm|0TRNT4X7J0]] for $84$ and $36$ takes two divisions:
$$84 = 2 \cdot 36 + 12, \qquad 36 = 3 \cdot 12.$$
It returns $12$, and $12 \mid 84$ and $12 \mid 36$ hold.
Every common divisor of $84$ and $36$ divides $12$, because
$$12 = 84 - 2 \cdot 36.$$
So $12$ satisfies the definition, and $\gcd(84, 36) = 12$ by uniqueness.

Watch out: being a common divisor is not enough.
The number $6$ divides $84$ and $36$, but the common divisor $12$ does not divide $6$, so $6$ fails the last condition.
