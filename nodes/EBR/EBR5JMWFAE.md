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

Two moves that look harmless can create false solutions.
Consider over $\mathbb{R}$ the system
$$x + y = 3, \qquad x - y = 1,$$
whose only solution is $(2, 1)$.

1. Scale $R_2$ by $0$. The system becomes $x + y = 3$, $0 = 0$.
2. Now $(3, 0)$ is a solution, since $3 + 0 = 3$. But $3 - 0 \ne 1$, so the solution set grew.
3. Scaling by $0$ is not an [[elementary row operation|0DE5R5EB4D]], because the scale factor must be nonzero.
4. Next, start again from the original system and replace $R_1$ by $R_1 + R_2$ and $R_2$ by $R_2 + R_1$ at the same time, both computed from the old rows.
5. Both new equations are $2x = 4$.
6. Now $(2, 5)$ is a solution, since $2 \cdot 2 = 4$. But $2 + 5 \ne 3$, so the solution set grew again.
7. The double replacement is not an elementary operation, and not a sequence of them. Elementary operations keep the solution set, by the [[theorem on row operations|K41GT10YM6]], and this move changed it.

## Remarks

Done one after the other, the two replacements are harmless.
First $R_1 \leftarrow R_1 + R_2$ gives $2x = 4$.
Then $R_2 \leftarrow R_2 + R_1$, with the new $R_1$, gives $3x - y = 5$.
That system still has the unique solution $(2, 1)$, since $4 = 4$ and $6 - 1 = 5$.
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

Watch out: computer code that updates several rows in one loop must use the rows as they are after each update.
