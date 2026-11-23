---
tag: WJ6XJD8V71
kind: example
name: Points on a circle, the pattern 1, 2, 4, 8, 16 breaks
msc: ["00A35", "05A15"]
topics: [X1NSTVGDNQ]
audience: school
not_instance_of:
  - target: FTBJX4G51S
    note: the first five special cases suggest the powers of 2, and the conjecture fails at the sixth case, which gives 31; special cases gave a false pattern
uses: [FTBJX4G51S, M225KZAV4F, 0GBZM0MT0F]
sources:
  - url: https://en.wikipedia.org/wiki/Dividing_a_circle_into_areas
    locator: lead section
---

## Example

Place $n$ points on a circle so that no three of the chords joining them meet at one point inside the circle.
Into how many regions $r(n)$ do all the chords cut the disc?
This is [[Moser's circle problem|M225KZAV4F]], and it shows how [[specialization|FTBJX4G51S]] can mislead.

1. With $1$ point there is no chord and $1$ region.
2. With $2$ points there is one chord and $2$ regions.
3. With $3$ points the chords form a triangle and there are $4$ regions.
4. With $4$ points the quadrilateral and its two diagonals give $8$ regions.
5. With $5$ points the pentagon and its five diagonals give $16$ regions.
6. The values $1, 2, 4, 8, 16$ suggest $r(n) = 2^{n-1}$.
7. We test the guess on $n = 6$, and a careful count gives $31$, not $32$.

So the conjecture drawn from five special cases is false.
The heuristic did its job of producing a conjecture, and the test on a new case did its job of refuting it.
The true count needs a reason, which we now give.

1. We add the chords one at a time.
   A new chord that crosses $c$ earlier chords at $c$ distinct points is cut into $c + 1$ pieces, and each piece splits one region, so it adds $c + 1$ regions.
2. We sum over all $\binom{n}{2}$ chords.
   Each chord contributes $1$, and each crossing point is counted once, by the later of its two chords, so $r(n) = 1 + \binom{n}{2} + P$, where $P$ is the number of crossing points.
3. We count the crossing points.
   Each crossing belongs to two chords whose four endpoints are four of the $n$ points, and each set of four points gives exactly one crossing, of the two diagonals of their quadrilateral.
   So $P = \binom{n}{4}$.
4. With [[binomial coefficients|0GBZM0MT0F]] the count is
   $$r(n) = 1 + \binom{n}{2} + \binom{n}{4},$$
   which gives $1, 2, 4, 8, 16, 31$ for $n = 1, \ldots, 6$.

## Remarks

Why does the formula agree with $2^{n-1}$ for five cases?
By Pascal's rule, $1 + \binom{n}{2} + \binom{n}{4} = \binom{n-1}{0} + \binom{n-1}{1} + \cdots + \binom{n-1}{4}$.
This is the whole row $n - 1$ of Pascal's triangle, with sum $2^{n-1}$, exactly when $n - 1 \le 4$.
For $n = 6$ the term $\binom{5}{5} = 1$ is missing, which gives $32 - 1 = 31$.
For large $n$ the count grows like $\frac{n^4}{24}$, far slower than $2^{n-1}$.

The condition on the chords matters too.
If the six points are the vertices of a regular hexagon, the three long diagonals meet at the center, and the count drops to $30$.
Other patterns of the same kind are in [[patterns that eventually fail|A2KSJSQSF6]].

## Explanations

### L1 human

Put points on a circle and join every pair with a straight line.
With $1$, $2$, $3$, $4$ and $5$ points, the circle is cut into $1$, $2$, $4$, $8$ and $16$ pieces.
It looks as if the number doubles each time.
With $6$ points it is $31$, not $32$.
So a pattern that holds five times can still be wrong, and only a proof makes it safe.

### L2 human

We check the identity of the remarks for $n = 5$ and $n = 6$.
For $n = 5$, both forms give $16$:
$$1 + \binom{5}{2} + \binom{5}{4} = 1 + 10 + 5 = 16, \qquad 1 + 4 + 6 + 4 + 1 = 16.$$
For $n = 6$, both forms give $31$:
$$1 + \binom{6}{2} + \binom{6}{4} = 1 + 15 + 15 = 31, \qquad 1 + 5 + 10 + 10 + 5 = 31.$$
The full row $5$ of Pascal's triangle sums to $32$, one more.

The typical use of the example is as a warning: test a pattern on a new case, and look for a reason before you believe it.
Watch out when you draw the case $n = 6$: points spaced evenly on the circle put three chords through the center and give $30$, a third value that hides the true pattern even more.
