---
tag: ~e06fbfe4
kind: example
name: Reversing a sequence of row operations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [006BHFWMAP]
uses: [095DDGZF16, ~6410ee51]
sources:
  - url: https://en.wikipedia.org/wiki/Row_equivalence
    locator: lead section
---

## Example

Let $M = \left[\begin{array}{cc|c} 1 & 1 & 3 \\ 1 & -1 & 1 \end{array}\right]$, the system $x + y = 3$, $x - y = 1$.

1. $R_2 \leftarrow R_2 - R_1$ gives $(0, -2 \mid -2)$.
2. $R_2 \leftarrow -\tfrac12 R_2$ gives $(0, 1 \mid 1)$.
3. $R_1 \leftarrow R_1 - R_2$ gives $(1, 0 \mid 2)$.
4. So $M$ is [[row equivalent|095DDGZF16]] to $N = \left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & 1 \end{array}\right]$, and the solution is $(2, 1)$.
5. Back from $N$: undo step 3 by $R_1 \leftarrow R_1 + R_2$, which gives $(1, 1 \mid 3)$.
6. Undo step 2 by $R_2 \leftarrow -2R_2$, which gives $(0, -2 \mid -2)$.
7. Undo step 1 by $R_2 \leftarrow R_2 + R_1$, which gives $(1, -1 \mid 1)$.
8. The result is $M$ again. So $N$ is row equivalent to $M$, as symmetry predicts.
9. Check the solution: $2 + 1 = 3$ and $2 - 1 = 1$.

## Remarks

The inverse steps come in the reverse order, like taking off shoes and socks.
Each inverse step has the same type as the step it undoes, by [[the theorem on row operations|~6410ee51]].

## Explanations

### L1 human

If you walk from home to school by three turns, you walk back by the same turns in the reverse order.
Row moves work the same way.

### L2 human

1. Write down each step as you reduce.
2. To go back, invert each step: a swap stays a swap, scaling by $c$ becomes scaling by $1/c$, and adding $c R_j$ becomes adding $-c R_j$.
3. Apply the inverses from the last step to the first.

A trap: undoing the steps in the original order usually does not give back the original matrix.
