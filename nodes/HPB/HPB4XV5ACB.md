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

A monotone [[lattice path|040WY0TT2G]] from $(0, 0)$ to $(m, n)$ is a sequence of unit steps, each step $R = (1, 0)$ or $U = (0, 1)$, whose sum is $(m, n)$.
Such a path has exactly $m$ steps $R$ and $n$ steps $U$.
Let $L(m, n)$ be the number of these paths.
We prove $L(m, n) = \binom{m + n}{m}$ for all natural numbers $m$ and $n$, by a [[double induction|AABX4YPKRR]] on the sum $s = m + n$.
Here $\binom{a}{b}$ is the [[binomial coefficient|0GBZM0MT0F]], the number of $b$-element subsets of an $a$-element set.

1. Let $R(s)$ be the claim "$L(m, n) = \binom{m + n}{m}$ for all $m, n$ with $m + n = s$".
2. Base case $s = 0$: the only pair is $(0, 0)$. The only path is the empty sequence, so $L(0, 0) = 1 = \binom{0}{0}$.
3. Step: let $s \ge 1$, assume $R(s - 1)$, and let $m + n = s$.
4. Case $n = 0$: the only path is $m$ steps $R$, so $L(m, 0) = 1$. An $m$-element set has one $m$-element subset, so $\binom{m}{m} = 1$.
5. Case $m = 0$: the only path is $n$ steps $U$, so $L(0, n) = 1 = \binom{n}{0}$, because the empty set is the only $0$-element subset.
6. Case $m, n \ge 1$: each path ends with $R$ or with $U$. Deleting the last step $R$ gives a path to $(m - 1, n)$, and adding $R$ undoes this. So the paths that end with $R$ number $L(m - 1, n)$.
7. In the same way, the paths that end with $U$ number $L(m, n - 1)$.
8. The pairs $(m - 1, n)$ and $(m, n - 1)$ have the sum $s - 1$. By $R(s - 1)$, $L(m - 1, n) = \binom{s - 1}{m - 1}$ and $L(m, n - 1) = \binom{s - 1}{m}$.
9. By steps 6 to 8, $L(m, n) = \binom{s - 1}{m - 1} + \binom{s - 1}{m}$.
10. [[Pascal's rule|0YRG241HQQ]] with top index $s - 1$ and lower index $m - 1$ gives $\binom{s - 1}{m - 1} + \binom{s - 1}{m} = \binom{s}{m}$. This proves $R(s)$.
11. By induction on $s$, $R(s)$ holds for every $s$, so $L(m, n) = \binom{m + n}{m}$ for every pair.

The small values of $L(m, n)$ form Pascal's triangle, turned on its side.

| $L(m, n)$ | $n = 0$ | $n = 1$ | $n = 2$ | $n = 3$ |
|---|---|---|---|---|
| $m = 0$ | $1$ | $1$ | $1$ | $1$ |
| $m = 1$ | $1$ | $2$ | $3$ | $4$ |
| $m = 2$ | $1$ | $3$ | $6$ | $10$ |
| $m = 3$ | $1$ | $4$ | $10$ | $20$ |

For example, $L(2, 2) = 6 = \binom{4}{2}$: the paths are $RRUU$, $RURU$, $RUUR$, $URRU$, $URUR$ and $UURR$.

## Remarks

1. The induction is on $m + n$ because the step uses two pairs, and both have the sum $m + n - 1$. An induction on $m$ alone, with $n$ fixed, would not provide $L(m, n - 1)$.
2. A nested induction also works: an outer induction on $m$ of "$L(m, n) = \binom{m + n}{m}$ for every $n$", with an inner induction on $n$.
3. Steps 4 and 5 are the boundary cases. The rule of step 9 does not hold there, because one of the pairs $(m - 1, n)$ and $(m, n - 1)$ does not exist.
4. A bijective proof gives the same count with no induction: a path is fixed by the set of the $m$ positions, among $m + n$, that carry the step $R$.
5. For $m = n$, the result gives $\binom{2n}{n}$ paths from $(0, 0)$ to $(n, n)$, for example $\binom{6}{3} = 20$ for $n = 3$.

## Explanations

### L1 human

Walk on a grid of streets from one corner to another, always to the east or to the north.
To reach a point, the last step comes from the west or from the south.
So the number of ways to reach a point is the number of ways to reach the point to its west plus the number of ways to reach the point to its south.
For example, 3 ways reach the point $(2, 1)$ and 3 ways reach the point $(1, 2)$, so 6 ways reach $(2, 2)$.
The proof uses this rule and handles the points in order of their distance from the start.

### L2 human

We check step 9 at the pair $(3, 2)$, with $s = 5$.

1. The paths to $(3, 2)$ that end with $R$ correspond to the paths to $(2, 2)$. There are $L(2, 2) = 6$ of them.
2. The paths that end with $U$ correspond to the paths to $(3, 1)$. There are $L(3, 1) = 4$ of them.
3. So $L(3, 2) = 6 + 4 = 10$.
4. Pascal's rule gives $\binom{4}{2} + \binom{4}{3} = 6 + 4 = 10 = \binom{5}{3}$.

The typical use of this pattern is a count that satisfies a recursion in two variables, such as binomial coefficients, Stirling numbers or the entries of a dynamic programming table.
A trap is to apply the recursion on the boundary: $L(3, 0)$ is $1$, and it is not $L(2, 0) + L(3, -1)$.
