---
tag: ET6CYR090M
kind: example
name: Allen's thirteen interval relations on integer intervals
msc: ["03B44", "68T27"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [991B5RR6X4]
uses: [991B5RR6X4, 0FRXBVVR03, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
    locator: section Relations
---

## Example

### The table

Fix the interval $X = [a, b] = [2, 6]$ of the integers, and write $Y = [c, d]$ with $c < d$.
The table lists one $Y$ for each of the thirteen relations "$X$ r $Y$" of [[interval temporal logic|991B5RR6X4]].

| relation of $X$ to $Y$ | condition | $Y$ |
|---|---|---|
| before | $b < c$ | $[8, 9]$ |
| meets | $b = c$ | $[6, 9]$ |
| overlaps | $a < c < b < d$ | $[4, 9]$ |
| starts | $a = c$, $b < d$ | $[2, 9]$ |
| during | $c < a$, $b < d$ | $[0, 9]$ |
| finishes | $c < a$, $b = d$ | $[0, 6]$ |
| equals | $a = c$, $b = d$ | $[2, 6]$ |
| after | $d < a$ | $[0, 1]$ |
| met by | $d = a$ | $[0, 2]$ |
| overlapped by | $c < a < d < b$ | $[0, 4]$ |
| started by | $a = c$, $d < b$ | $[2, 4]$ |
| contains | $a < c$, $d < b$ | $[3, 5]$ |
| finished by | $a < c$, $b = d$ | $[4, 6]$ |

Check: for "overlaps", $2 < 4 < 6 < 9$, and for "overlapped by", $0 < 2 < 4 < 6$.

### Exactly one relation holds

For any intervals $[a, b]$ and $[c, d]$ of a [[linear order|0FRXBVVR03]], exactly one relation holds.
The proof is by cases.

1. Compare $b$ with $c$.
   If $b < c$, the relation is "before", and if $b = c$, it is "meets".
2. Otherwise $c < b$, and we compare $d$ with $a$.
   If $d < a$, the relation is "after", and if $d = a$, it is "met by".
3. Otherwise $c < b$ and $a < d$.
   Compare $a$ with $c$ (three cases) and $b$ with $d$ (three cases).
4. With $a < c$, the cases $b < d$, $b = d$ and $d < b$ give overlaps, finished by and contains.
5. With $a = c$, they give starts, equals and started by.
6. With $c < a$, they give during, finishes and overlapped by.
7. In step 4, "overlaps" needs $a < c < b < d$, and $c < b$ comes from step 2.
   The other cases are checked the same way.
8. The cases are disjoint and cover all possibilities, since a linear order compares any two points.
   So there are $4 + 9 = 13$ relations, and exactly one holds.

## Remarks

The example uses only that the order is linear, so the same analysis works over $\mathbb{Q}$ or $\mathbb{R}$.
Each relation is fixed by the relative order of the four endpoints, which is why there are exactly thirteen.
The six relations before, meets, overlaps, starts, during and finishes are paired with their inverses by swapping $X$ and $Y$.
The relation "equals" is its own inverse.
If $X$ is moved to $[2, 9]$, the table changes: for instance $Y = [4, 9]$ is now "finished by" instead of "overlaps".

## Explanations

### L1 human

Two meetings on the same day can relate in thirteen ways.
One can end before the other starts, end exactly when it starts, overlap it, start with it, lie inside it, end with it, or be the same.
With the reverse versions, that makes thirteen.

### L2 human

Draw $X$ as a bar from $2$ to $6$ on a number line.
For each relation, draw $Y$ as a second bar with the endpoints of the table, and read off which endpoints coincide and which come first.
Watch out: "overlaps" is not symmetric, since $X$ overlaps $Y$ means that $X$ starts first and ends first.
