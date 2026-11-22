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
We show that the points can be joined in red-blue pairs by $n$ [[segments|VQ4Q2V45RP]] so that no two segments cross.
The proof uses the [[extremal principle|MD3MRG90W4]] with the total length as the quantity.

1. A red-blue [[matching|0MJ04A50QW]] pairs each red point with one blue point, each blue point used once.
   There are $n!$ such matchings, a finite and nonempty set.
2. The total length of a matching is the sum of the lengths of its $n$ segments.
   A finite nonempty set of real numbers has a least element, so some matching $M$ has the least total length.
3. Suppose two segments $R_1 B_1$ and $R_2 B_2$ of $M$ cross at a point $O$.
   The point $O$ is not an end of either segment, because an end on the other segment would put three of the points on one line.
   So $O$ splits both segments:
   $$|R_1 B_1| = |R_1 O| + |O B_1|, \qquad |R_2 B_2| = |R_2 O| + |O B_2|.$$
4. Replace these two segments by $R_1 B_2$ and $R_2 B_1$.
   The result $M'$ is again a red-blue matching.
5. By the [[triangle inequality|03HF5PMY5T]] in the triangles $R_1 O B_2$ and $R_2 O B_1$,
   $$|R_1 B_2| \le |R_1 O| + |O B_2|, \qquad |R_2 B_1| \le |R_2 O| + |O B_1|.$$
6. The first inequality is strict.
   Equality would put $O$ on the segment $R_1 B_2$, so $R_1$, $O$ and $B_2$ would lie on one line.
   That line is the line $R_2 B_2$, since it contains $O$ and $B_2$, and then $R_1$, $R_2$ and $B_2$ would be collinear, which the hypothesis excludes.
7. Add the two inequalities of step 5 and use steps 3 and 6:
   $$|R_1 B_2| + |R_2 B_1| < |R_1 B_1| + |R_2 B_2|.$$
   So $M'$ is shorter than $M$, against the choice of $M$.
8. Therefore no two segments of $M$ cross.

## Remarks

The quantity is the total length, and a crossing allows a swap that makes the total strictly smaller.
Step 2 is the existence part of the [[extremal principle|MD3MRG90W4]], and it uses only that the number of matchings is finite.
The swap of step 4 may create new crossings with other segments, and this does not matter: the shortest matching has no crossing at all, so no sequence of swaps needs to be followed.

The hypothesis that no three points are collinear does two jobs.
It makes the inequality of step 6 strict, and it is also needed for the result itself.
Take the red points $(0, 0)$ and $(1, 0)$ and the blue points $(2, 0)$ and $(3, 0)$, all on one line.
In each of the two matchings, both segments contain the piece from $(1, 0)$ to $(2, 0)$, so no matching has disjoint segments.
When the numbers of red and blue points differ, no red-blue matching uses all the points, and the question changes.

## Explanations

### L1 human

Some red dots and the same number of blue dots lie on a page, and you want to pair each red dot with a blue dot by straight lines that never cross.
Among all ways to pair them, pick one where the total length of the lines is as small as possible.
If two of its lines crossed, you could swap the partners of those two pairs.
The two new lines are shorter in total, because a straight line is the shortest way between two points.
That would beat the shortest pairing, which is impossible, so the shortest pairing has no crossings.

### L2 human

We test the swap on the four corners of a square with side $2$.
Let $R_1 = (0, 0)$, $R_2 = (0, 2)$, $B_1 = (2, 2)$ and $B_2 = (2, 0)$, and no three of them are collinear.
The matching $\{R_1 B_1, R_2 B_2\}$ uses the two diagonals, which cross at $(1, 1)$, and its total length is
$$2\sqrt{2^2 + 2^2} = 4\sqrt{2} \approx 5.66.$$
The swap gives $\{R_1 B_2, R_2 B_1\}$, the bottom and the top sides, with total length $2 + 2 = 4$.
There are only $2! = 2$ matchings, so this second one is the shortest, and it has no crossing.

Check the strict inequality of step 6 with numbers: $|R_1 B_2| = 2$, while $|R_1 O| + |O B_2| = \sqrt{2} + \sqrt{2} \approx 2.83$.
The typical use of the method is a swap that removes one defect and strictly lowers a total.
Watch out: it is wrong to argue "swap crossing pairs until none is left" without a reason why the process stops.
The total length gives that reason too, since it drops at each swap and takes only $n!$ values, and this is the [[monovariant|TP3GC5J08D]] form of the same proof.
