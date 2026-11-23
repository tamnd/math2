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

For a real number $x$, let $p$ be "$x \le 3$" and $q$ be "$x \ge 2$".
We show that the [[disjunction|0F72FK8EKB]] $p \lor q$ is true for every real $x$, by checking which rows of its truth table occur.

1. At $x = 0$, $p$ is T and $q$ is F.
   One disjunct is T, so $p \lor q$ is T.
2. At $x = 5$, $p$ is F and $q$ is T, so $p \lor q$ is T.
3. At $x = 2.5$, $p$ is T and $q$ is T.
   Both disjuncts are T, and the inclusive "or" makes $p \lor q$ T.
4. The row "$p$ F, $q$ F" would need $x > 3$ and $x < 2$, that is, $3 < x < 2$.
   No real number does that, so this row never occurs.
5. A disjunction is F only in that row, so $p \lor q$ is T for every real $x$.

## Remarks

The inclusive reading is what makes the statement true on the overlap: for every $x$ from $2$ to $3$ both parts hold, and the disjunction stays T.
With the exclusive reading, "$x \le 3$ or $x \ge 2$, but not both" would be F for each $x$ in $[2, 3]$.

In set language the example says
$$(-\infty, 3] \cup [2, \infty) = \mathbb{R},$$
a [[union|0X1GSWNBN1]] of two overlapping intervals.
Swap the numbers to "$x \le 2$ or $x \ge 3$" and the row FF occurs for every $x$ strictly between $2$ and $3$, where the disjunction becomes F.

## Explanations

### L1 human

Every number is "at most $3$" or "at least $2$".
Small numbers such as $0$ satisfy the first claim, and large numbers such as $5$ satisfy the second.
Numbers in the middle, such as $2.5$, satisfy both, and that is allowed.
So the "or" claim is true for every number.

### L2 human

For which real $x$ is "$x^2 < 1$ or $x > 0$" true?
The first part holds exactly for $-1 < x < 1$, and the second for $x > 0$.
The disjunction holds when at least one part holds, so on the union
$$(-1, 1) \cup (0, \infty) = (-1, \infty).$$
For $0 < x < 1$ both parts hold, and the inclusive "or" counts these values.
The solution set of a disjunction of conditions is the union of the solution sets.
Watch out: the two pieces overlap, so the union is one interval $(-1, \infty)$, not two separate pieces.
