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

Fix the interval $X = [2, 6]$ of the integers, and write $Y = [c, d]$ with $c < d$.
The table lists one $Y$ for each of Allen's thirteen relations "$X$ r $Y$" of [[interval temporal logic|991B5RR6X4]].

| relation of $X$ to $Y$ | condition on $[a, b] = [2, 6]$ and $[c, d]$ | $Y$ |
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

We show that for any intervals $[a, b]$ and $[c, d]$ of a [[linear order|0FRXBVVR03]], exactly one relation holds.
The proof is by cases.

1. Compare $b$ with $c$. If $b < c$, the relation is "before". If $b = c$, it is "meets".
2. Otherwise $c < b$. Compare $d$ with $a$. If $d < a$, the relation is "after". If $d = a$, it is "met by".
3. Otherwise $c < b$ and $a < d$. Compare $a$ with $c$ (three cases) and $b$ with $d$ (three cases).
4. The nine combinations give: ($a < c$, $b < d$) overlaps; ($a < c$, $b = d$) finished by; ($a < c$, $d < b$) contains.
5. Next: ($a = c$, $b < d$) starts; ($a = c$, $b = d$) equals; ($a = c$, $d < b$) started by.
6. Last: ($c < a$, $b < d$) during; ($c < a$, $b = d$) finishes; ($c < a$, $d < b$) overlapped by.
7. In step 4, "overlaps" needs $a < c < b < d$. Here $c < b$ comes from step 2. The other cases are checked the same way.
8. The cases of steps 1 to 6 are disjoint and cover all possibilities, since a linear order compares any two points. So $4 + 9 = 13$ relations, and exactly one holds.

## Remarks

The example uses only that the order is linear, so the same analysis works over $\mathbb{Q}$ or $\mathbb{R}$.
Each relation is fixed by the relative order of the four endpoints, which is why there are exactly thirteen.
The six relations with "$X$ before, meets, overlaps, starts, during, finishes $Y$" and their inverses are paired by swapping $X$ and $Y$; "equals" is its own inverse.

## Explanations

### L1 human

Two meetings on the same day can relate in thirteen ways.
One can end before the other starts, end exactly when it starts, overlap it, start with it, lie inside it, end with it, or be the same.
With the reverse versions, that makes thirteen.

### L2 human

1. Draw $X$ as a bar from $2$ to $6$ on a number line.
2. For each relation, draw $Y$ as a second bar with the endpoints of the table.
3. Read off which endpoints coincide and which come first.

A trap: "overlaps" is not symmetric; $X$ overlaps $Y$ means that $X$ starts first and ends first.
