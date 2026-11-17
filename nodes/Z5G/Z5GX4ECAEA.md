---
tag: Z5GX4ECAEA
kind: example
name: Regions cut out by lines in the plane, found from small cases
msc: ["00A35", "52C30"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [FTBJX4G51S]
uses: [FTBJX4G51S, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Lazy_caterer%27s_sequence
    locator: lead section
---

## Example

Problem: $n$ lines lie in the plane in general position, that is, no two are parallel and no three pass through one point.
Into how many regions $R(n)$ do they divide the plane?
We use [[specialization|FTBJX4G51S]].

1. $n = 0$: the plane is one region, $R(0) = 1$.
2. $n = 1$: one line gives two half-planes, $R(1) = 2$.
3. $n = 2$: two crossing lines give $4$ regions.
4. $n = 3$: a figure of three lines in general position shows a bounded triangle, $3$ regions that touch it along a side, and $3$ regions that touch it at a corner, so $R(3) = 7$.
5. $n = 4$: a careful figure gives $R(4) = 11$.
6. The pattern. The values $1, 2, 4, 7, 11$ have differences $1, 2, 3, 4$. This suggests $R(n) = R(n - 1) + n$.
7. Look at the case $n = 4$ for the reason. The fourth line crosses the three earlier lines in $3$ points, and these points cut it into $4$ pieces. Each piece runs through one old region and splits it into two, so $4$ regions are added.
8. The general argument. The $n$-th line crosses each of the $n - 1$ earlier lines, since no two lines are parallel, and the $n - 1$ crossing points are distinct, since no three lines meet in a point. So the line is cut into $n$ pieces, and each piece splits one region. Hence $R(n) = R(n - 1) + n$.
9. Solve the recursion. By [[induction|0ASJVEFA9J]] from $R(0) = 1$: $R(n) = 1 + (1 + 2 + \cdots + n) = 1 + \frac{n(n + 1)}{2}$.
10. Test: $R(4) = 1 + 10 = 11$ and $R(5) = 1 + 15 = 16$.

## Remarks

The special cases did two jobs.
Steps 1 to 6 gave the form of the answer, and step 7 gave the argument, which step 8 states without special values.
Each piece of the new line in step 7 is a segment or a ray, and the count of pieces, one more than the number of crossing points, is the same for every $n$.

If two of the lines are parallel, the count drops: three lines with two parallel give $6$ regions, not $7$.
So the condition "general position" is used in step 8, and the special cases with general position do not show what happens without it.

## Explanations

### L1 human

Cut a large sheet of paper with straight lines that all cross each other.
One line gives $2$ pieces, two lines give $4$, three lines give $7$, four lines give $11$.
The jumps are $1$, $2$, $3$, $4$: each new line adds one more piece than the last line did.
The reason: the new line crosses all the old lines, and each part of it between two crossings splits one piece into two.

### L2 human

We use the result for a related question: how many of the regions are bounded?

1. Specialize: $n = 1$ and $n = 2$ give $0$ bounded regions, $n = 3$ gives $1$, $n = 4$ gives $3$.
2. The unbounded regions: far away, the $n$ lines look like $2n$ rays from one point, so there are $2n$ unbounded regions.
3. So the bounded regions number $1 + \frac{n(n+1)}{2} - 2n = \frac{(n - 1)(n - 2)}{2}$.
4. Test: $n = 3$ gives $1$ and $n = 4$ gives $3$, as in step 1.

The typical use: special cases suggest a count, and a structural reason, here the $2n$ directions at infinity, proves it.

A trap: a hand-drawn figure for $n = 5$ often has three lines nearly through one point, and then a small region is missed.
