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

Problem: find the least positive integer $n$ that leaves remainder $1$ when divided by $2$, $3$, $4$, $5$ and $6$, and is divisible by $7$.
Six conditions at once are many.
We [[vary the problem|KT5SASGTQ5]]: drop the last condition, solve the weaker problem, then restore the condition.

1. Without divisibility by $7$, the conditions say that $n - 1$ is divisible by $2$, $3$, $4$, $5$ and $6$.
2. This holds exactly when $n - 1$ is divisible by the [[least common multiple|007NPQX34K]] $\operatorname{lcm}(2, 3, 4, 5, 6) = 60$.
3. So the weaker problem has the solutions $n = 60k + 1$ with $k \geq 0$: $1, 61, 121, 181, 241, 301, \ldots$
4. Restore the dropped condition: $7 \mid 60k + 1$. Since $60 = 8 \cdot 7 + 4$, this is $4k + 1 \equiv 0 \pmod 7$, that is $4k \equiv 6 \pmod 7$.
5. Multiply by $2$, the inverse of $4$ modulo $7$: $k \equiv 12 \equiv 5 \pmod 7$.
6. The least such $k$ is $5$, so $n = 60 \cdot 5 + 1 = 301$.

Check: $301 = 7 \cdot 43$, and $300$ is divisible by $2$, $3$, $4$, $5$ and $6$.
A search over $1 \leq n < 1000$ gives the same least value, $301$.

## Remarks

The weaker problem has infinitely many solutions, but they form a simple family, an arithmetic progression.
Restoring the condition then selects members of the family.
This is the same pattern as dropping a condition in a geometric construction, where the family is a locus.

All solutions of the original problem are $n = 301 + 420 j$ with $j \geq 0$, since $k = 5 + 7j$ gives $60(5 + 7j) + 1 = 301 + 420j$.
The period $420 = \operatorname{lcm}(60, 7)$ agrees with the [[Chinese remainder theorem|0FNN9B4W64]], since $60$ and $7$ are coprime.

## Explanations

### L1 human

A basket of eggs: taken out $2$, $3$, $4$, $5$ or $6$ at a time, one egg is always left over, and taken out $7$ at a time, none is left.
First forget the sevens.
Then the number of eggs is one more than a common multiple of $2, 3, 4, 5, 6$, that is, one more than a multiple of $60$.
Now try $61, 121, 181, 241, 301$ in turn and keep the first one that $7$ divides.
That is $301 = 7 \cdot 43$.

### L2 human

We state the method for a system of conditions in which one condition is harder than the others.

1. Choose the condition to drop, so that the remaining ones are easy to solve together.
2. Describe all solutions of the weaker problem as a family with a parameter, here $n = 60k + 1$.
3. Write the dropped condition as a condition on the parameter, here $4k + 1 \equiv 0 \pmod 7$.
4. Solve for the parameter and substitute back.

The typical use: the easy conditions give a parametrised family, and the hard condition becomes an equation in the parameter.

A trap: in step 2 the conditions modulo $2, 3, 4, 5, 6$ combine to one condition modulo $60$, not modulo $2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 = 720$, since the moduli are not coprime.
