---
tag: VP6RN56Z5A
kind: example
name: The truth table of ((p → q) ∧ (q → r)) → (p → r)
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [05RSK4Q657]
uses: [05RSK4Q657, 0ZNX6DQ3EJ, 0M28ASWG8T, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Truth_table
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Example

Let $\varphi$ be the formula $((p \to q) \land (q \to r)) \to (p \to r)$.
We build its [[truth table|05RSK4Q657]] and show that $\varphi$ is a [[tautology|05006AJ7DZ]].

1. The variables are $p$, $q$, $r$, so the table has $2^3 = 8$ rows in the standard order.
2. The subformulas, from the smallest to the largest, are $p \to q$, $q \to r$, $(p \to q) \land (q \to r)$, $p \to r$ and $\varphi$.
3. The columns of $p \to q$, $q \to r$ and $p \to r$ use the table of [[material implication|0ZNX6DQ3EJ]]: each is $\mathsf{F}$ only when its antecedent is $\mathsf{T}$ and its consequent is $\mathsf{F}$.
4. The column of $(p \to q) \land (q \to r)$ uses the table of [[conjunction|0M28ASWG8T]]: it is $\mathsf{T}$ only when both columns of step 3 are $\mathsf{T}$.
5. The column of $\varphi$ uses the table of implication with the columns of steps 4 and 3.

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $(p \to q) \land (q \to r)$ | $p \to r$ | $\varphi$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | T | F | T | F | F | F | T |
| T | F | T | F | T | F | T | T |
| T | F | F | F | T | F | F | T |
| F | T | T | T | T | T | T | T |
| F | T | F | T | F | F | T | T |
| F | F | T | T | T | T | T | T |
| F | F | F | T | T | T | T | T |

6. The last column is $\mathsf{T}$ in all $8$ rows, so $\varphi$ is a tautology.

## Remarks

The example shows the full method on a formula with three variables.
The formula $\varphi$ is the law behind [[hypothetical syllogism|7MT8CPCEM4]]: from $p \to q$ and $q \to r$ we may infer $p \to r$.

The rows where $\varphi$ could fail are those where $p \to r$ is false.
Only the rows $\mathsf{T}\mathsf{T}\mathsf{F}$ and $\mathsf{T}\mathsf{F}\mathsf{F}$ have $p \to r$ false, and in both the antecedent of $\varphi$ is false.
So a short cut that checks only these two rows reaches the same answer.

If we replace the conclusion $p \to r$ by $r \to p$, the formula is no longer a tautology.
In the row $\mathsf{F}\mathsf{F}\mathsf{T}$, the antecedent is $\mathsf{T}$ and $r \to p$ is $\mathsf{T} \to \mathsf{F} = \mathsf{F}$.

## Explanations

### L1 human

The formula says: if $p$ leads to $q$, and $q$ leads to $r$, then $p$ leads to $r$.
For example: if rain makes the grass wet, and wet grass makes shoes wet, then rain makes shoes wet.
The table checks all $8$ ways to make $p$, $q$ and $r$ true or false.
In each of the $8$ cases the whole formula comes out true.
So the chain rule for "if ... then" never fails.

### L2 human

We use the same table to test whether $(p \to q) \land (q \to r)$ is equivalent to $p \to r$.

1. Compare the column of $(p \to q) \land (q \to r)$ with the column of $p \to r$.
2. In the row $\mathsf{T}\mathsf{F}\mathsf{T}$, the first is $\mathsf{F}$ and the second is $\mathsf{T}$.
3. The columns differ in this row, so the two formulas are not equivalent.

The typical use of a single table is to answer several questions at once.
One formula implies another exactly when no row has the first true and the second false.
A trap: the chain implies $p \to r$, but $p \to r$ does not imply the chain, as step 2 shows.
