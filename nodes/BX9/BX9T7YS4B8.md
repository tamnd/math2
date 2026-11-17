---
tag: BX9T7YS4B8
kind: example
name: '"x ≤ 3 or x ≥ 2" is true for every real x'
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0F72FK8EKB]
uses: [0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_disjunction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
---

## Example

For a real number $x$, let $p$ be "$x \leq 3$" and $q$ be "$x \geq 2$".
We show that the [[disjunction|0F72FK8EKB]] $p \lor q$ is true for every real $x$, and we check the rows of its truth table.

1. $x = 0$: $p$ is T and $q$ is F. One disjunct is T, so $p \lor q$ is T.
2. $x = 5$: $p$ is F and $q$ is T. So $p \lor q$ is T.
3. $x = 2.5$: $p$ is T and $q$ is T. Both disjuncts are T, and the inclusive "or" gives $p \lor q$ T.
4. The row "$p$ F, $q$ F" would need $x > 3$ and $x < 2$. Such an $x$ would satisfy $3 < x < 2$, which is impossible. So this row never occurs.
5. The disjunction is false only in that row, so $p \lor q$ is true for every real $x$.

## Remarks

The example shows the inclusive reading at work: for every $x$ from $2$ to $3$, both parts are true, and the disjunction stays true.
With the exclusive reading, "$x \leq 3$ or $x \geq 2$, but not both" would be false for each $x$ in the interval $[2, 3]$.

In the language of sets, the example says $(-\infty, 3] \cup [2, \infty) = \mathbb{R}$, a [[union|0X1GSWNBN1]] of two overlapping intervals.
If we change the numbers to "$x \leq 2$ or $x \geq 3$", the row FF occurs for $x$ strictly between $2$ and $3$, and the disjunction becomes false there.

## Explanations

### L1 human

Every number is "at most $3$" or "at least $2$".
Small numbers such as $0$ satisfy the first claim.
Large numbers such as $5$ satisfy the second claim.
Numbers in the middle, such as $2.5$, satisfy both, and that is allowed.
So the "or" claim is true for every number.

### L2 human

We decide for which real $x$ the statement "$x^2 < 1$ or $x > 0$" is true.

1. $x^2 < 1$ holds exactly for $-1 < x < 1$.
2. $x > 0$ holds for the positive numbers.
3. The disjunction holds when at least one holds: for $-1 < x < 1$, or for $x > 0$.
4. Together this is $x > -1$. For $0 < x < 1$ both parts hold, and the inclusive "or" counts these values.

The typical use is to describe the set of solutions of a disjunction of conditions as a union of the solution sets.

A trap: the union of $(-1, 1)$ and $(0, \infty)$ is $(-1, \infty)$, not two separate pieces, because the pieces overlap.
