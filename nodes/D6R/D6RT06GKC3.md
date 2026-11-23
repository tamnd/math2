---
tag: D6RT06GKC3
kind: example
name: A substitution instance of p → (q → p)
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [05006AJ7DZ]
uses: [05006AJ7DZ, 05RSK4Q657, 0ZNX6DQ3EJ]
sources:
  - url: https://en.wikipedia.org/wiki/Tautology_(logic)
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

The formula $p \to (q \to p)$ says "if $p$ is true, then anything implies $p$".
We use it to show that $(r \land s) \to (\neg r \to (r \land s))$ is a [[tautology|05006AJ7DZ]], first by substitution and then by a [[truth table|05RSK4Q657]].

1. The formula $p \to (q \to p)$ is a tautology.
   It is false only if $p$ is T and $q \to p$ is F, but $q \to p$ is T when $p$ is T.
2. Replace $p$ by $r \land s$ at both occurrences, and replace $q$ by $\neg r$.
3. The result is $(r \land s) \to (\neg r \to (r \land s))$.
4. A substitution instance of a tautology is a tautology, so this formula is a tautology.

We check the result directly with the rows TT, TF, FT, FF for $r$ and $s$.

| $r$ | $s$ | $r \land s$ | $\neg r$ | $\neg r \to (r \land s)$ | whole formula |
|---|---|---|---|---|---|
| T | T | T | F | T | T |
| T | F | F | F | T | T |
| F | T | F | T | F | T |
| F | F | F | T | F | T |

5. The last column is T in every row, as step 4 predicts.

## Remarks

### Why substitution works

Any values of $r$ and $s$ give values to $r \land s$ and $\neg r$, and these values form a row of the table of $p \to (q \to p)$.
Every row of that table is T, so the substituted formula is T in every row.
Two different variables may be replaced by the same formula: replacing both $p$ and $q$ by $p$ gives the tautology $p \to (p \to p)$.

### The replacement must be uniform

Each variable must be replaced by the same formula at every occurrence.
Replacing the first $p$ by $r$, the second $p$ by $s$, and $q$ by $r$ gives $r \to (r \to s)$.
When $r$ is T and $s$ is F, its value is $\mathrm{T} \to (\mathrm{T} \to \mathrm{F}) = \mathrm{T} \to \mathrm{F} = \mathrm{F}$, so it is not a tautology.

## Explanations

### L1 human

The formula $p \to (q \to p)$ says: if $p$ is true, then anything implies $p$.
It is true for every choice of $p$ and $q$.
So it stays true when $p$ and $q$ stand for longer statements, such as "$r$ and $s$" and "not $r$".
This saves a new table: the shape alone shows that the long formula is always true.

### L2 human

We use substitution to show that $\neg\neg(a \lor b) \to (a \lor b)$ is a tautology.

1. The formula $\neg\neg p \to p$ is a tautology.
   If $p$ is T the consequent is T, and if $p$ is F the antecedent is F.
2. Replace $p$ by $a \lor b$ at both occurrences.
3. The result is $\neg\neg(a \lor b) \to (a \lor b)$, so it is a tautology.

Substitution lets a known law, such as a De Morgan law, apply to compound formulas without new tables.
Watch out: substitution goes from a tautology to its instances, not back.
The formula $p \to p$ is a tautology, but $p \to q$ is not.
