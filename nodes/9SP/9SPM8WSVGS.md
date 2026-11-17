---
tag: 9SPM8WSVGS
kind: example
name: (p ∧ (p → q)) → q is a tautology
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [05006AJ7DZ]
uses: [05006AJ7DZ, 05RSK4Q657, 0ZNX6DQ3EJ, 0M28ASWG8T, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Example

We show that the formula $(p \land (p \to q)) \to q$ is a [[tautology|05006AJ7DZ]] by a [[truth table|05RSK4Q657]].

1. There are $2$ variables, so there are $4$ rows: $\mathsf{T}\mathsf{T}$, $\mathsf{T}\mathsf{F}$, $\mathsf{F}\mathsf{T}$, $\mathsf{F}\mathsf{F}$.
2. The column of $p \to q$ follows the table of [[material implication|0ZNX6DQ3EJ]]: $\mathsf{T}, \mathsf{F}, \mathsf{T}, \mathsf{T}$.
3. The column of $p \land (p \to q)$ follows the table of [[conjunction|0M28ASWG8T]]: $\mathsf{T}, \mathsf{F}, \mathsf{F}, \mathsf{F}$.
4. The last column combines step 3 and the column of $q$ by the table of implication.

| $p$ | $q$ | $p \to q$ | $p \land (p \to q)$ | $(p \land (p \to q)) \to q$ |
|---|---|---|---|---|
| T | T | T | T | T |
| T | F | F | F | T |
| F | T | T | F | T |
| F | F | T | F | T |

5. The last column is $\mathsf{T}$ in all $4$ rows, so the formula is a tautology.

## Remarks

The formula is the law behind [[modus ponens|0Y0MQYST0M]]: from $p$ and $p \to q$, infer $q$.
In the metalanguage, $\models (p \land (p \to q)) \to q$, and equivalently $p,\ p \to q \models q$.
The only row where the antecedent $p \land (p \to q)$ is true is $\mathsf{T}\mathsf{T}$, and there $q$ is true.
So the assume-false method gives the same result in one line.

By substitution, every formula of the form $(\varphi \land (\varphi \to \psi)) \to \psi$ is a tautology.
For example, $((r \lor s) \land ((r \lor s) \to \neg r)) \to \neg r$ is a tautology without a new table.

## Explanations

### L1 human

The formula says: if $p$ is true, and $p$ implies $q$, then $q$ is true.
For example: if it is Sunday, and on Sundays the shop is closed, then the shop is closed.
The table checks all $4$ cases for $p$ and $q$.
The whole formula is true in each case, so it is a tautology.

### L2 human

We compare the formula with a similar one that is not a tautology: $(q \land (p \to q)) \to p$.

1. In the row $p = \mathsf{F}$, $q = \mathsf{T}$, the implication $p \to q$ is $\mathsf{T}$.
2. So the antecedent $q \land (p \to q)$ is $\mathsf{T}$, and the consequent $p$ is $\mathsf{F}$.
3. The formula is $\mathsf{F}$ in this row, so it is not a tautology.

This second formula is the form of the fallacy of [[affirming the consequent|J7KFCFQRBT]].
The typical use of the tautology is to justify each step of a proof that applies a known implication.
A trap: the order matters; $p$ and $p \to q$ give $q$, but $q$ and $p \to q$ do not give $p$.
