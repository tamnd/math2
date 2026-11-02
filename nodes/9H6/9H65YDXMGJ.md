---
tag: 9H65YDXMGJ
kind: example
name: Laver table
msc: [20N02, "03E55"]
instance_of: [PDFC0MRYR8]
uses: [VEFE5WZMS3, X1FG7PSCTY]
sources:
  - url: https://en.wikipedia.org/wiki/Laver_table
same_as:
  wikidata: Q17144402
  wikipedia: Laver table
---

## Example

For $n \ge 0$, the *Laver table* $A_n$ is the set $\set{1, 2, \dots, 2^n}$ with the unique binary operation $\star$ such that:

1. $p \star 1 = p + 1$ for $p < 2^n$, and $2^n \star 1 = 1$;
2. $p \star (q \star r) = (p \star q) \star (p \star r)$ for all $p, q, r$.

So $A_n$ is a [[shelf|PDFC0MRYR8]]: clause 2 is [[left self-distributivity|VEFE5WZMS3]].
The table can be computed row by row from the bottom, where row $2^n$ is $2^n \star q = q$.
For $p < 2^n$ one uses $p \star (q + 1) = (p \star q) \star (p + 1)$, where $p \star q > p$ lies in a row already known.

For $n = 2$ this gives the table of $A_2$, with $p$ indexing rows and $q$ indexing columns:

| $\star$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 2 | 4 | 2 | 4 |
| 2 | 3 | 4 | 3 | 4 |
| 3 | 4 | 4 | 4 | 4 |
| 4 | 1 | 2 | 3 | 4 |

Check of one instance of clause 2: $1 \star (2 \star 1) = 1 \star 3 = 2$, and $(1 \star 2) \star (1 \star 1) = 4 \star 2 = 2$.
All $64$ instances of clause 2 hold in $A_2$.
The shelf $A_2$ is not a rack, since the row of $1$ takes only the values $2$ and $4$.

## Remarks

Each row of $A_n$ is periodic, and its period is a power of $2$.
Laver proved that, if a rank-into-rank [[large cardinal|X1FG7PSCTY]] exists, then the period of the row of $1$ in $A_n$ tends to infinity as $n$ grows.
No proof of this statement in ZFC alone is known.
The period of the row of $1$ grows extremely slowly: it is $2$ in $A_2$ and $4$ in $A_3$.
Dougherty showed that the least $n$ for which it reaches $32$, if there is one, is enormous.

## Explanations

### L1 human

A Laver table is a small multiplication table on the numbers $1$ to $2^n$.
It is fixed by two rules: multiplying by $1$ on the right adds one, and the operation distributes over itself.
These two rules leave no freedom, so each size has exactly one table.
The tables look like simple finite puzzles, but a basic fact about how their rows repeat has only been proved using axioms of infinity far beyond ordinary mathematics.
