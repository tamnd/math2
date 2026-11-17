---
tag: BH6XNGKBJY
kind: example
name: Checking many cases is not a generic proof
msc: ["97E50"]
topics: [VHGA6J4NZK]
audience: school
not_instance_of:
  - target: SG9XA69J64
    note: the student computes each case and records the result, but no step shows a reason that does not depend on the case
uses: [SG9XA69J64, YVNRVXJR68]
sources:
  - url: https://doi.org/10.1007/BF00312078
    locator: pages 277-289
---

## Example

The claim is: the sum of any three consecutive integers is divisible by $3$.
A student makes a table.

| Numbers | Sum | Sum divided by $3$ |
|---|---|---|
| $1, 2, 3$ | $6$ | $2$ |
| $2, 3, 4$ | $9$ | $3$ |
| $3, 4, 5$ | $12$ | $4$ |
| $10, 11, 12$ | $33$ | $11$ |
| $50, 51, 52$ | $153$ | $51$ |

The student writes: "It works every time, so it is true."
We check whether the argument is a [[generic proof|SG9XA69J64]].

1. Check the table: $6 = 3 \cdot 2$, $9 = 3 \cdot 3$, $12 = 3 \cdot 4$, $33 = 3 \cdot 11$, $153 = 3 \cdot 51$. Each entry is correct.
2. Look for a step that holds for each case: there is none. Each row is a separate computation.
3. Ask what the argument says about a case not in the table: nothing, except that the pattern has held so far.

So the argument is not a generic proof.
It is a check of five cases, an empirical argument in the sense of [[proof schemes|YVNRVXJR68]].

## Remarks

The table contains the reason, but the student does not see it: the last column is the middle number each time.
A teacher can use this to turn the table into a generic proof, by asking "what do you notice about the last column?".
Then the student can rewrite one row, such as $10 + 11 + 12 = (11 - 1) + 11 + (11 + 1) = 3 \cdot 11$.

## Explanations

### L1 human

The student checks five cases and finds that each sum is divisible by $3$.
But checking cases does not show why the rule works.
A generic proof would show, in one case, a reason that works in every case.

### L2 human

1. Ask whether any step of the argument works for all cases.
2. Here each step is a computation of one sum.
3. Conclude that the argument is a check of cases, not a generic proof.

A trap is to count the number of cases.
Five cases or five hundred cases make no difference: without a general reason, the argument is not a proof.
