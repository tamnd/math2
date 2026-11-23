---
tag: KG3RKYJRNY
kind: example
name: A homogeneous inequality reduced to one variable
msc: ["00A35", "26D05"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [DX2H7AD66G]
uses: [DX2H7AD66G, 2C3PAQ7H50, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_function
    locator: lead section
  - book: isbn:9780691164076
    locator: Part III
---

## Example

We prove
$$a^3 + b^3 \ge a^2 b + a b^2 \quad \text{for all real } a \ge 0,\ b \ge 0$$
by a [[reduction to a special case|DX2H7AD66G]], the case $b = 1$.

1. Both sides are [[homogeneous polynomials|2C3PAQ7H50]] of degree $3$.
   For $s > 0$, replacing $(a, b)$ by $(sa, sb)$ multiplies both sides by $s^3 > 0$, so the claim for $(sa, sb)$ is equivalent to the claim for $(a, b)$.
2. The case $b = 0$ reads $a^3 \ge 0$, which holds since $a \ge 0$.
   It comes first, because the scaling of step 3 needs $b > 0$.
3. For $b > 0$, take $s = 1/b$ and let $t = a / b \ge 0$; the claim becomes $t^3 + 1 \ge t^2 + t$, the case $b = 1$.
4. Factor: $t^3 - t^2 - t + 1 = t^2 (t - 1) - (t - 1) = (t - 1)(t^2 - 1) = (t - 1)^2 (t + 1)$.
5. Since $(t - 1)^2 \ge 0$ and $t + 1 > 0$, the product is not negative, so $t^3 + 1 \ge t^2 + t$.
6. By step 3 the claim holds for $b > 0$, and by step 2 for $b = 0$.

Check: at $t = 2$, $8 - 4 - 2 + 1 = 3$ and $(t - 1)^2 (t + 1) = 3$; at $a = 2$, $b = 1$, the two sides are $9$ and $6$.

## Remarks

Equality holds exactly when $a = b$.
The reduction removes one variable: one scaling fixes $b$, and $a$ survives as $t$.
Multiplying the factorization of step 4 by $b^3$ gives the direct proof $a^3 + b^3 - a^2 b - a b^2 = (a + b)(a - b)^2$.
The split of steps 2 and 3 is a [[proof by cases|0WCP0PVET6]], because no positive scaling reaches $b = 0$ from $b > 0$.

The hypothesis $a, b \ge 0$ is needed.
For $a = -2$ and $b = 1$ the left side is $-7$ and the right side is $4 - 2 = 2$, so the inequality fails.
In step 5 this is $t = -2$, where $t + 1 < 0$.

## Explanations

### L1 human

If you multiply $a$ and $b$ by the same positive number, both sides of the inequality are multiplied by its cube.
So only the ratio of $a$ to $b$ matters.
Choose units so that $b$ is $1$, and only one number, $t$, is left.
For one number, the claim becomes $(t - 1)^2 (t + 1) \ge 0$, a square times a positive number.

### L2 human

We use the same reduction for $a^4 + b^4 \ge a^3 b + a b^3$ with $a, b \ge 0$.

1. Both sides are homogeneous of degree $4$, and the case $b = 0$ reads $a^4 \ge 0$.
2. For $b > 0$ and $t = a / b$, the claim is $t^4 + 1 \ge t^3 + t$.
3. Factor: $t^4 - t^3 - t + 1 = t^3 (t - 1) - (t - 1) = (t - 1)(t^3 - 1)$.
4. Since $t^3 - 1 = (t - 1)(t^2 + t + 1)$ with $t^2 + t + 1 > 0$, the two factors have the same sign, so the product is not negative.
5. Check at $t = 2$: $16 + 1 = 17$ and $8 + 2 = 10$.

The method fits a polynomial inequality whose terms all have the same degree.
Watch out: setting both $a = 1$ and $b = 1$ proves only the case $a = b$.
