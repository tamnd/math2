---
tag: 7HZCKQQNKD
kind: example
name: The condition x^2 = 4 is a disjunction, not a conjunction
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 025YZN3VJW
    note: the conjunction of x = 2 and x = -2 is false for every real x, while x^2 = 4 is true for two values; the condition is the disjunction of x = 2 and x = -2
uses: [025YZN3VJW, 0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_conjunction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_disjunction
    locator: lead section
---

## Example

A textbook says "the solutions of $x^2 = 4$ are $2$ and $-2$".
The word "and" suggests the [[conjunction|025YZN3VJW]] "$x = 2 \land x = -2$" as the condition on a real number $x$.
We check that $x^2 = 4$ is not this conjunction.

1. The conjunction $x = 2 \land x = -2$ is true only when both conjuncts are true.
2. If $x = 2$, then $x \ne -2$, because $2 \ne -2$.
   So no real $x$ makes both conjuncts true, and the conjunction is false for every $x$.
3. But $x^2 = 4$ is true at $x = 2$, because $2^2 = 4$, so the two conditions differ at $x = 2$.
4. The correct form comes from factoring:
   $$x^2 - 4 = (x - 2)(x + 2),$$
   and a product of real numbers is $0$ exactly when one factor is $0$.
   So $x^2 = 4$ is equivalent to the [[disjunction|0F72FK8EKB]] "$x = 2 \lor x = -2$".

## Remarks

The English "and" here joins two numbers in a list, not two conditions on one number $x$.
A true conjunction sits nearby: "$2$ is a solution and $-2$ is a solution" joins two propositions about the two numbers, and both are true.
The condition on the variable $x$, by contrast, is "$x = 2$ or $x = -2$".

In the language of sets, the solution set is the union $\{2\} \cup \{-2\} = \{2, -2\}$, which matches the disjunction.
The conjunction describes $\{2\} \cap \{-2\} = \varnothing$.
Add a second condition, as in "$x^2 = 4$ and $x > 0$", and a conjunction is correct: the only solution is $x = 2$.

## Explanations

### L1 human

"The answers are $2$ and $-2$" means that $2$ works and $-2$ also works.
It does not mean that one number is equal to $2$ and to $-2$ at once.
No number can be both.
For one unknown number $x$, the correct statement is "$x$ is $2$ or $x$ is $-2$".

### L2 human

Write the logical form of "the roots of $x^2 - 5x + 6 = 0$ are $2$ and $3$".
As a condition on $x$, factor $x^2 - 5x + 6 = (x - 2)(x - 3)$, so the equation holds exactly when $x = 2 \lor x = 3$.
As a statement about the numbers, it is "$2$ is a root, and $3$ is a root, and there is no other root".
Check the first two conjuncts: $4 - 10 + 6 = 0$ and $9 - 15 + 6 = 0$.
The last line of a solved equation should be a disjunction of the possible values.
Watch out: "$x = 2$ and $x = 3$" at the end of a solution is false for every $x$, even though both numbers are correct roots.
