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

Take $n$ lines in the plane in general position: no two are parallel and no three pass through one point.
Into how many regions $R(n)$ do they cut the plane?
We find the answer by [[specialization|FTBJX4G51S]] and then prove it.

1. With no lines, the plane is one region, so $R(0) = 1$.
2. One line cuts the plane into two half-planes, so $R(1) = 2$.
3. Two crossing lines give $R(2) = 4$.
4. Three lines give a bounded triangle, $3$ regions that touch it along a side and $3$ that touch it at a corner, so $R(3) = 7$.
5. A careful figure of four lines gives $R(4) = 11$.
6. The values $1, 2, 4, 7, 11$ have differences $1, 2, 3, 4$, which suggests $R(n) = R(n - 1) + n$.
7. We look at the case $n = 4$ for a reason.
   The fourth line crosses the three earlier lines in $3$ points, which cut it into $4$ pieces.
   Each piece runs through one old region and splits it into two, so the fourth line adds $4$ regions.
8. We state the reason with no special values.
   The $n$-th line crosses each of the $n - 1$ earlier lines, since no two lines are parallel, and the crossing points are distinct, since no three lines meet in a point.
   So the line is cut into $n$ pieces, each piece splits one region, and $R(n) = R(n - 1) + n$.
9. We solve the recursion by [[induction|0ASJVEFA9J]] from $R(0) = 1$:
   $$R(n) = 1 + (1 + 2 + \cdots + n) = 1 + \frac{n(n + 1)}{2}.$$
10. We test the formula on new cases: $R(4) = 1 + 10 = 11$ and $R(5) = 1 + 15 = 16$.

## Remarks

The special cases did two different jobs.
Steps 1 to 6 gave the form of the answer, and step 7 gave the argument, which step 8 then states without special values.
The argument works for every $n$ because each piece of the new line is a segment or a ray, and the number of pieces is always one more than the number of crossing points.

Change a condition and the count changes.
Three lines with two of them parallel give $6$ regions, not $7$.
The second line, parallel to the first, crosses nothing and adds only $1$ region, so the plane has $3$ regions, and the third line then adds $3$.
So the condition "no two parallel" is used in step 8, and special cases in general position say nothing about the other cases.

## Explanations

### L1 human

Cut a large sheet of paper with straight cuts that all cross each other.
One cut gives $2$ pieces, two cuts give $4$, three cuts give $7$ and four cuts give $11$.
The jumps are $1$, $2$, $3$, $4$, so each new cut adds one more piece than the cut before it.
The reason is that the new cut crosses all the old cuts, and each part of it between two crossings splits one piece into two.

### L2 human

We use the result on a related question: how many of the regions are bounded?
Small cases give $0$ bounded regions for $n = 1$ and $n = 2$, then $1$ for $n = 3$ and $3$ for $n = 4$.
Far away from all crossing points, the $n$ lines look like $2n$ rays from one point, so there are $2n$ unbounded regions.
The bounded regions are the rest:
$$1 + \frac{n(n + 1)}{2} - 2n = \frac{n^2 - 3n + 2}{2} = \frac{(n - 1)(n - 2)}{2}.$$
Check: $n = 3$ gives $1$ and $n = 4$ gives $3$, as in the small cases.

This is the typical use: special cases suggest a count, and a structural reason, here the $2n$ directions far away, proves it.
Watch out for hand-drawn figures: a figure of five lines often has three lines nearly through one point, and then a small region is easy to miss.
