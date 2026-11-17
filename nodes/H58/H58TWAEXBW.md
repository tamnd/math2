---
tag: H58TWAEXBW
kind: example
name: A shortest red-blue matching has no crossing segments
msc: ["00A35", "52C99"]
topics: [GB14W4SYPK]
audience: school
instance_of: [MD3MRG90W4]
uses: [MD3MRG90W4, 03HF5PMY5T, 0AFNNTRTJE, VQ4Q2V45RP]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle_inequality
    locator: lead section
---

## Example

Let $n$ red points and $n$ blue points lie in the [[Euclidean plane|0XW7V9ZZ05]], with no three of the $2n$ points [[collinear|0AFNNTRTJE]].
We show that the points can be joined in red-blue pairs by $n$ [[segments|VQ4Q2V45RP]] such that no two segments cross.

1. A red-blue [[matching|0MJ04A50QW]] pairs each red point with one blue point. There are $n!$ such matchings, a finite number.
2. The total length of a matching is the sum of the lengths of its $n$ segments. A finite nonempty set of real numbers has a least element, so some matching $M$ has the least total length.
3. Suppose two segments $R_1 B_1$ and $R_2 B_2$ of $M$ cross at a point $O$. The point $O$ is not an end of either segment, since an end on the other segment would make three points collinear. Then $|R_1 B_1| = |R_1 O| + |O B_1|$ and $|R_2 B_2| = |R_2 O| + |O B_2|$.
4. Replace these two segments by $R_1 B_2$ and $R_2 B_1$. The result is again a red-blue matching $M'$.
5. By the [[triangle inequality|03HF5PMY5T]], $|R_1 B_2| \le |R_1 O| + |O B_2|$ and $|R_2 B_1| \le |R_2 O| + |O B_1|$.
6. The first inequality is strict. Equality would put $O$ on the segment $R_1 B_2$, so $R_1$, $O$ and $B_2$ would lie on one line. That line is the line $R_2 B_2$, since it contains $O$ and $B_2$. Then $R_1$, $R_2$ and $B_2$ would be collinear, which the hypothesis excludes.
7. Adding steps 3, 5 and 6 gives $|R_1 B_2| + |R_2 B_1| < |R_1 B_1| + |R_2 B_2|$. So $M'$ is shorter than $M$, against the choice of $M$.
8. So no two segments of $M$ cross.

## Remarks

The example shows the [[extremal principle|MD3MRG90W4]] in geometry.
The quantity is the total length, and a crossing allows a swap that makes the total strictly smaller.
Step 2 is the existence part, and it uses only that the number of matchings is finite.

The hypothesis that no three points are collinear is needed in step 6.
It also matters for the result.
Take the red points $(0, 0)$ and $(1, 0)$ and the blue points $(2, 0)$ and $(3, 0)$ on one line.
Every matching has two segments that overlap on the part from $(1, 0)$ to $(2, 0)$, so no matching has disjoint segments.
When the numbers of red and blue points differ, no red-blue matching covers all the points, and the question changes.

## Explanations

### L1 human

Some red dots and the same number of blue dots lie on a page, and we want to pair each red dot with a blue dot by straight lines that never cross.
Among all ways to pair them, pick one where the total length of the lines is as small as possible.
If two of its lines crossed, we could swap the partners of those two pairs.
The two new lines are shorter in total, by the rule that a straight line is the shortest way between two points.
That would beat the shortest pairing, which is impossible, so the shortest pairing has no crossings.

### L2 human

We test the swap on the four corners of a square with side $2$.

1. Let $R_1 = (0, 0)$, $R_2 = (0, 2)$, $B_1 = (2, 2)$ and $B_2 = (2, 0)$. No three of them are collinear.
2. The matching $\{R_1 B_1, R_2 B_2\}$ uses the two diagonals, which cross at $(1, 1)$. Its total length is $2\sqrt{8} = 4\sqrt{2} \approx 5.66$.
3. The swap gives $\{R_1 B_2, R_2 B_1\}$, the bottom and top sides, with total length $2 + 2 = 4$.
4. The new matching is shorter and has no crossing. There are only $2! = 2$ matchings, so it is the shortest one.

The typical use is a swap that removes one defect and strictly lowers a total.
The trap is to claim that one swap removes all crossings: a swap can create new crossings with other segments, and only the choice of a shortest matching avoids this problem.
