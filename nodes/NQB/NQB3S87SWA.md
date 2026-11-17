---
tag: NQB3S87SWA
kind: example
name: The one-way implication "if x > 2, then x^2 > 4" is not a biconditional
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0S6GMNJ62Y
    note: the implication is true in the row where the antecedent is false and the consequent is true, and a biconditional is false there
uses: [0S6GMNJ62Y, 0V6GAWTBYW, 0ZNX6DQ3EJ]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_biconditional
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
---

## Example

For a real number $x$, let $p$ be "$x > 2$" and let $q$ be "$x^2 > 4$".
The statement $S$: "for every real $x$, if $x > 2$, then $x^2 > 4$" is true, as the page [[a conditional with a hidden quantifier|FWXPGJBK97]] proves.
We show that $S$ is not the [[biconditional|0S6GMNJ62Y]] "for every real $x$, $x > 2$ if and only if $x^2 > 4$".

1. The truth tables of $p \to q$ and $p \leftrightarrow q$ differ in exactly one row: $p = \mathsf{F}$, $q = \mathsf{T}$. There $p \to q$ is true and $p \leftrightarrow q$ is false, by the [[definition of the biconditional|0V6GAWTBYW]].
2. Take $x = -3$. Then $x > 2$ is false, so $p$ is false.
3. Also $x^2 = 9 > 4$, so $q$ is true.
4. So $x = -3$ falls in the row of step 1. The implication $p \to q$ is true at $x = -3$, and the biconditional $p \leftrightarrow q$ is false there.
5. Hence the biconditional is false for $x = -3$, while the implication is true for every $x$.

So $S$ and the biconditional are different statements: the first is true and the second is false.

## Remarks

The example shows that a one-way implication and a biconditional differ only by the row $\mathsf{F}\mathsf{T}$.
A value of the variable in that row is exactly a counterexample to the converse $q \to p$.
Here $x = -3$ refutes the converse "if $x^2 > 4$, then $x > 2$".

If we restrict $x$ to the positive real numbers, then no value falls in the row $\mathsf{F}\mathsf{T}$.
For $x > 0$, the inequality $x^2 > 4$ gives $(x - 2)(x + 2) > 0$, and $x + 2 > 0$, so $x > 2$.
So on the positive reals the biconditional "$x > 2$ if and only if $x^2 > 4$" is true.
On all reals the correct biconditional is "$x^2 > 4$ if and only if $x > 2$ or $x < -2$".

## Explanations

### L1 human

"If a number is bigger than $2$, then its square is bigger than $4$" is true.
The reverse is not true: $-3$ is not bigger than $2$, but its square $9$ is bigger than $4$.
An "if and only if" sentence would need both directions.
So the one-way sentence is not an "if and only if" sentence.

### L2 human

We decide whether a given true implication $p \to q$ about a variable is in fact a biconditional.

1. Write the converse $q \to p$. Here it is "if $x^2 > 4$, then $x > 2$".
2. Look for a value with $q$ true and $p$ false. Here $x = -3$ works.
3. Such a value refutes the converse, so the biconditional is false.

The typical use of this test is in the reading of theorems: a theorem stated with "if" may not be reversible.
A trap: a student who checks only positive values, such as $x = 3$ and $x = 10$, finds no counterexample and wrongly concludes "if and only if".
