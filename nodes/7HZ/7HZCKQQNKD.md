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
We check that the condition $x^2 = 4$ is not this conjunction.

1. The conjunction $x = 2 \land x = -2$ is true only when both conjuncts are true.
2. If $x = 2$, then $x \neq -2$, because $2 \neq -2$. So no real $x$ makes both conjuncts true.
3. So $x = 2 \land x = -2$ is false for every real $x$.
4. But $x^2 = 4$ is true for $x = 2$, because $2^2 = 4$. So the two conditions differ at $x = 2$.
5. The correct form: $x^2 - 4 = (x - 2)(x + 2)$, and a product of real numbers is $0$ exactly when one factor is $0$. So $x^2 = 4$ is equivalent to the [[disjunction|0F72FK8EKB]] "$x = 2 \lor x = -2$".

## Remarks

The example shows a common gap between English and logical form.
In "the solutions are $2$ and $-2$", the word "and" joins two numbers in a list, not two conditions on one number $x$.
There is a correct conjunction nearby: "$2$ is a solution and $-2$ is a solution" is a conjunction of two propositions, and it is true.
It is a statement about the two numbers, while "$x = 2$ or $x = -2$" is a condition on the variable $x$.

In the language of sets, the solution set is $\{2\} \cup \{-2\} = \{2, -2\}$, a union, which matches the disjunction.
The set described by the conjunction is $\{2\} \cap \{-2\} = \varnothing$.

If we change the equation to the system "$x^2 = 4$ and $x > 0$", then a conjunction is correct, and the only solution is $x = 2$.

## Explanations

### L1 human

"The answers are $2$ and $-2$" means that $2$ works and $-2$ also works.
It does not mean that one number is equal to $2$ and to $-2$ at once.
No number can be both.
For one unknown number $x$, the correct statement is "$x$ is $2$ or $x$ is $-2$".

### L2 human

We write the logical form of "the roots of $x^2 - 5x + 6 = 0$ are $2$ and $3$".

1. As a condition on $x$: $x^2 - 5x + 6 = (x - 2)(x - 3)$, so the equation holds exactly when $x = 2 \lor x = 3$.
2. As a statement about the numbers: "$2$ is a root $\land$ $3$ is a root $\land$ there is no other root".
3. Check the first conjunct: $4 - 10 + 6 = 0$. Check the second: $9 - 15 + 6 = 0$.

The typical use of this care is in solving equations, where the final line must be a disjunction of the possible values.

A trap: writing "$x = 2$ and $x = 3$" at the end of a solution is a false statement for every $x$, even though both numbers are correct roots.
