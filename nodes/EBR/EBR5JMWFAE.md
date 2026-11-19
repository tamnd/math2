---
tag: EBR5JMWFAE
kind: example
name: Operations on equations that are not elementary row operations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: 04XWH28452
    note: scaling by zero and two simultaneous row additions are not elementary row operations, and both change the solution set
uses: [0DE5R5EB4D, K41GT10YM6]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
---

## Example

Consider the system $x + y = 3$, $x - y = 1$ over $\R$, with the unique solution $(2, 1)$.

1. Scale $R_2$ by $0$. The system becomes $x + y = 3$, $0 = 0$.
2. Now $(3, 0)$ is a solution, since $3 + 0 = 3$. But $3 - 0 \ne 1$, so the solution set grew.
3. Scaling by $0$ is not an [[elementary row operation|0DE5R5EB4D]], because the scale factor must be nonzero.
4. Next, replace $R_1$ by $R_1 + R_2$ and $R_2$ by $R_2 + R_1$ at the same time, both from the old rows.
5. The system becomes $2x = 4$, $2x = 4$.
6. Now $(2, 5)$ is a solution, since $2 \cdot 2 = 4$. But $2 + 5 \ne 3$, so the solution set grew again.
7. The two replacements together are not an elementary operation, and not a sequence of them, since the result cannot be undone.

## Remarks

Done one after the other, $R_1 \leftarrow R_1 + R_2$ gives $2x = 4$, and then $R_2 \leftarrow R_2 + R_1$ gives $3x - y = 5$.
That system still has the unique solution $(2, 1)$: $4 = 4$ and $6 - 1 = 5$.
So the danger in step 4 comes from using the old rows twice.

## Explanations

### L1 human

Multiplying an equation by zero throws it away, so we lose information.
Adding two equations to each other at the same moment can make both equations the same, and again we lose information.
Losing an equation means gaining solutions.

### L2 human

To stay safe:

1. Never multiply a row by $0$.
2. Do one operation at a time, and always use the current rows.
3. After each step, ask whether you can undo it.

A trap: computer code that updates several rows in one loop must use the rows as they are after each update.
