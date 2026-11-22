---
tag: HPB4XV5ACB
kind: example
name: Counting lattice paths by induction on m + n
msc: ["00A35", "05A10"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [AABX4YPKRR]
uses: [040WY0TT2G, 0GBZM0MT0F, 0YRG241HQQ, AABX4YPKRR]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_path
    locator: Combinations and NE lattice paths
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Induction on more than one counter
---

## Example

A monotone [[lattice path|040WY0TT2G]] from $(0, 0)$ to $(m, n)$ is a sequence of unit steps, each $R = (1, 0)$ or $U = (0, 1)$, whose sum is $(m, n)$.
Such a path has exactly $m$ steps $R$ and $n$ steps $U$.
Let $L(m, n)$ be the number of these paths, and let $\binom{a}{b}$ be the [[binomial coefficient|0GBZM0MT0F]], the number of $b$-element subsets of an $a$-element set.
We prove that $L(m, n) = \binom{m + n}{m}$ for all natural numbers $m$ and $n$, by a [[double induction|AABX4YPKRR]] on the sum $s = m + n$.
Let $R(s)$ be the claim "$L(m, n) = \binom{m + n}{m}$ for all pairs with $m + n = s$".

1. Base case $s = 0$.
   The only pair is $(0, 0)$, and its only path is the empty sequence, so $L(0, 0) = 1 = \binom{0}{0}$.
2. Step.
   Let $s \ge 1$, assume $R(s - 1)$, and take a pair with $m + n = s$.
3. Boundary case $n = 0$.
   The only path is $m$ steps $R$, so $L(m, 0) = 1$, and $\binom{m}{m} = 1$ because an $m$-element set has one $m$-element subset.
4. Boundary case $m = 0$.
   The only path is $n$ steps $U$, so $L(0, n) = 1 = \binom{n}{0}$, because the empty set is the only $0$-element subset.
5. Inner case $m, n \ge 1$: sort the paths by their last step.
   Deleting a last step $R$ gives a path to $(m - 1, n)$, and adding $R$ undoes this, so $L(m - 1, n)$ paths end with $R$.
   In the same way, $L(m, n - 1)$ paths end with $U$.
6. Both pairs $(m - 1, n)$ and $(m, n - 1)$ have the sum $s - 1$, so $R(s - 1)$ applies to them:
   $$L(m, n) = L(m - 1, n) + L(m, n - 1) = \binom{s - 1}{m - 1} + \binom{s - 1}{m}.$$
7. [[Pascal's rule|0YRG241HQQ]] with top index $s - 1$ turns the right side into $\binom{s}{m}$.
   This proves $R(s)$.
8. By induction on $s$, $R(s)$ holds for every $s$, and every pair $(m, n)$ is covered by $R(m + n)$.

The small values form Pascal's triangle, turned on its side.

| $L(m, n)$ | $n = 0$ | $n = 1$ | $n = 2$ | $n = 3$ |
|---|---|---|---|---|
| $m = 0$ | $1$ | $1$ | $1$ | $1$ |
| $m = 1$ | $1$ | $2$ | $3$ | $4$ |
| $m = 2$ | $1$ | $3$ | $6$ | $10$ |
| $m = 3$ | $1$ | $4$ | $10$ | $20$ |

Check: $L(2, 2) = 6 = \binom{4}{2}$, and the six paths are $RRUU$, $RURU$, $RUUR$, $URRU$, $URUR$ and $UURR$.

## Remarks

The induction runs on $m + n$ because the step uses two pairs, and both have the sum $m + n - 1$.
An induction on $m$ alone, with $n$ fixed, would not provide $L(m, n - 1)$.
A nested induction also works: an outer induction on $m$ of the claim "$L(m, n) = \binom{m + n}{m}$ for every $n$", with an inner induction on $n$.

Steps 3 and 4 matter.
The recursion of step 6 does not hold on the boundary, because one of the pairs $(m - 1, n)$ and $(m, n - 1)$ does not exist there.

A bijective proof gives the same count without induction.
A path is fixed by the set of the $m$ positions, among its $m + n$ steps, that carry $R$, and there are $\binom{m + n}{m}$ such sets.
For $m = n$ the result counts the paths from $(0, 0)$ to $(n, n)$, for example $\binom{6}{3} = 20$ for $n = 3$, which matches the corner of the table.

## Explanations

### L1 human

Walk on a grid of streets from one corner to another, always east or north.
Your last step into a point comes from the point to its west or from the point to its south.
So the number of ways to reach a point is the number of ways to reach its west neighbor plus the number of ways to reach its south neighbor.
For example, $3$ ways reach $(2, 1)$ and $3$ ways reach $(1, 2)$, so $6$ ways reach $(2, 2)$.
The proof uses this rule and handles the points in order of their distance from the start.

### L2 human

We check step 6 at the pair $(3, 2)$, where $s = 5$.
The paths to $(3, 2)$ that end with $R$ match the paths to $(2, 2)$, and there are $6$ of them.
The paths that end with $U$ match the paths to $(3, 1)$, and there are $4$ of them.
So
$$L(3, 2) = 6 + 4 = 10, \qquad \binom{4}{2} + \binom{4}{3} = 6 + 4 = 10 = \binom{5}{3}.$$
The same pattern proves facts about any count with a recursion in two variables, such as Stirling numbers or the entries of a dynamic programming table.
Watch out for the boundary: $L(3, 0)$ is $1$, and the recursion would ask for the meaningless value $L(3, -1)$.
