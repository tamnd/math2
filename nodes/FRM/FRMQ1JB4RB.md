---
tag: FRMQ1JB4RB
kind: example
name: Three lines in the plane with zero pairwise intersections that do not form a direct sum
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
not_instance_of:
  - target: 0XYYT5KNTX
    note: the three lines meet pairwise only in 0, but (1, 1) = (1, 0) + (0, 1) gives two expressions of one vector
illustrates: [FVKY28HHBC]
uses: [041JTZCK9Q, 0V33SPH7RR, 0RMKABS2S5]
sources:
  - book: isbn:9783031410253
    locator: Section 1C
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Internal direct sum
---

## Example

Let $U_1 = \R(1, 0)$, $U_2 = \R(0, 1)$ and $U_3 = \R(1, 1)$ in $\R^2$.
We check that the pairwise intersections are zero but the sum is not direct.

1. Pairwise intersections. Two different lines through $0$ meet only in $0$. So $U_1 \cap U_2$, $U_1 \cap U_3$ and $U_2 \cap U_3$ are all $\{0\}$.
2. Two expressions. The vector $(1, 1)$ is $0 + 0 + (1, 1)$ and also $(1, 0) + (0, 1) + 0$, with the terms in $U_1$, $U_2$, $U_3$ in this order.
3. So the expression is not unique, and the sum $U_1 + U_2 + U_3$ is not [[direct|041JTZCK9Q]].
4. The [[criterion for several subspaces|FVKY28HHBC]] finds the failure: $U_1 + U_2 = \R^2$, so $U_3 \cap (U_1 + U_2) = U_3 \ne \{0\}$.
5. Dimension count. $\dim U_1 + \dim U_2 + \dim U_3 = 3 > 2 = \dim \R^2$, so no three nonzero subspaces of $\R^2$ form a direct sum.

## Remarks

For two subspaces, a zero intersection is enough for a direct sum.
For three or more subspaces, it is not: the right test compares each subspace with the sum of the others.
The same three lines show that the lattice of subspaces is not distributive: $U_3 \cap (U_1 + U_2) = U_3$, but $(U_3 \cap U_1) + (U_3 \cap U_2) = \{0\}$.

## Explanations

### L1 human

Three lines through the origin in a plane never split the plane, even though any two of them cross only at the origin.
Two of the lines already fill the plane, so the third adds nothing new.

### L2 human

The trap is to extend the test for two subspaces by checking all pairs.
The correct extension is the test $U_i \cap (U_1 + \cdots + U_{i-1}) = \{0\}$, which here fails at $i = 3$.
