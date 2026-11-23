---
tag: 57YGZR5YNR
kind: example
name: The least number that leaves remainder 1 on division by 2 to 6 and is divisible by 7
msc: ["00A35", "11A07"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [KT5SASGTQ5]
uses: [KT5SASGTQ5, 007NPQX34K, 0FNN9B4W64]
sources:
  - url: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Least_common_multiple
    locator: lead section
---

## Example

We look for the least positive integer $n$ that leaves remainder $1$ when divided by $2$, $3$, $4$, $5$ and $6$, and is divisible by $7$.
Six conditions at once are many, so we [[vary the problem|KT5SASGTQ5]]: drop the last condition, solve the weaker problem, and then restore the condition.

1. Without divisibility by $7$, the conditions say that $2$, $3$, $4$, $5$ and $6$ all divide $n - 1$.
2. This holds exactly when the [[least common multiple|007NPQX34K]] $\operatorname{lcm}(2, 3, 4, 5, 6) = 60$ divides $n - 1$.
3. So the weaker problem has the solutions $n = 60k + 1$ with $k \ge 0$, that is $1, 61, 121, 181, 241, 301, \dots$
4. Restore the dropped condition $7 \mid 60k + 1$.
   Since $60 = 8 \cdot 7 + 4$, it reads $4k + 1 \equiv 0 \pmod 7$, that is $4k \equiv 6 \pmod 7$.
5. Multiply by $2$, the inverse of $4$ modulo $7$, to get $k \equiv 12 \equiv 5 \pmod 7$.
6. The least such $k$ is $5$, so
   $$n = 60 \cdot 5 + 1 = 301.$$

Check: $301 = 7 \cdot 43$, and $300$ is divisible by $2$, $3$, $4$, $5$ and $6$.

## Remarks

The weaker problem has infinitely many solutions, but they form a simple family, an arithmetic progression, and the restored condition picks members out of it.
That is the same pattern as dropping a condition in a geometric construction, where the family is a locus.

All solutions of the original problem are $n = 301 + 420j$ with $j \ge 0$, since $k = 5 + 7j$ gives $60(5 + 7j) + 1 = 301 + 420j$.
The period $420 = \operatorname{lcm}(60, 7)$ agrees with the [[Chinese remainder theorem|0FNN9B4W64]], because $60$ and $7$ are coprime.

The choice of the condition to drop matters.
Dropping a different condition, say the remainder on division by $5$, leaves a family with period $\operatorname{lcm}(2, 3, 4, 6, 7) = 84$, which is less convenient but leads to the same answer.

## Explanations

### L1 human

A basket holds some eggs.
Taken out $2$, $3$, $4$, $5$ or $6$ at a time, one egg is always left over, and taken out $7$ at a time, none is left.
First forget the sevens: then the number of eggs is one more than a multiple of $60$.
Now try $61, 121, 181, 241, 301$ in turn and keep the first one that $7$ divides, which is $301 = 7 \cdot 43$.

### L2 human

The method works for any system of conditions in which one condition is harder than the others.
Choose the condition to drop, so that the others are easy to solve together.
Describe all solutions of the weaker problem as a family with a parameter, here $n = 60k + 1$.
Write the dropped condition as a condition on the parameter, here $4k + 1 \equiv 0 \pmod 7$, then solve for the parameter and substitute back.

Watch the step that combines the easy conditions.
The conditions modulo $2$, $3$, $4$, $5$ and $6$ combine to one condition modulo $60$, not modulo $2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 = 720$, because the moduli are not coprime.
