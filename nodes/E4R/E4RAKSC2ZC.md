---
tag: E4RAKSC2ZC
kind: example
name: Regions of a circle cut by chords do not double
aliases: [circle-regions-1-2-4-8-16-31]
msc: ["00A35", "05A10"]
topics: [T6QQ749DM5]
audience: school
instance_of: [ZX6ERT3SW7]
uses: [ZX6ERT3SW7, M225KZAV4F]
sources:
  - url: https://en.wikipedia.org/wiki/Dividing_a_circle_into_areas
    locator: lead section
---

## Example

Put $n$ points on a circle, join every pair by a chord, and count the regions of the disc.
Place the points so that no three chords meet at one inside point; this is [[Moser's circle problem|M225KZAV4F]].
Here is a tempting argument; draw along and find the flaw.

> For $n = 1, 2, 3, 4, 5$ points the counts are $1, 2, 4, 8, 16$.
> The count doubles each time, so $n$ points give $2^{n-1}$ regions, and $6$ points give $32$.

A careful drawing for $n = 6$ shows $31$ regions, so the formula $2^{n-1}$ is false.
The argument is [[proof by example|ZX6ERT3SW7]]: five matching values were taken as a proof.

The correct count is a theorem: $R(n) = 1 + \binom{n}{2} + \binom{n}{4}$.

1. Start with the disc, which is $1$ region, and draw the $\binom{n}{2}$ chords one at a time.
2. A new chord that crosses $k$ chords already drawn passes through $k$ distinct crossing points, since no three chords meet at a point. These points cut it into $k + 1$ pieces.
3. Each piece splits one old region into two, so the new chord adds $k + 1$ regions.
4. Summed over all chords, the "$+1$" terms give $\binom{n}{2}$.
5. Each crossing point lies on exactly two chords and is counted once, when the later of the two is drawn. So the "$k$" terms add up to the number of crossing points.
6. Each crossing point is where the two diagonals of a quadrilateral with vertices among the $n$ points cross, and each choice of $4$ points gives exactly one crossing. So there are $\binom{n}{4}$ crossing points.

The values for $n = 1$ to $8$ are $1, 2, 4, 8, 16, 31, 57, 99$, and for $n = 6$ the formula gives $1 + 15 + 15 = 31$.

## Remarks

The two formulas agree for $n \le 5$ for a reason, and seeing it removes the mystery.
By the binomial theorem, $2^{n-1} = \sum_{j=0}^{n-1}\binom{n-1}{j}$, while Pascal's rule turns the correct count into $1 + \binom{n}{2} + \binom{n}{4} = \sum_{j=0}^{4}\binom{n-1}{j}$.
So the formulas differ only by the terms with $j \ge 5$, which vanish when $n \le 5$.
After that they drift apart fast: for $n = 10$ they give $256$ and $512$.
Watch out for regular placements, where three chords can meet at one point: in the regular hexagon the three long diagonals meet at the center, and the count drops to $30$.

## Explanations

### L1 human

Mark points on a circle and join every pair with a straight line.
With $1, 2, 3, 4, 5$ points the circle falls into $1, 2, 4, 8, 16$ pieces.
The numbers double each time, so we expect $32$ pieces for $6$ points.
A careful drawing gives only $31$.
A pattern that holds five times in a row can still break.

### L2 human

We check the identity of the Remarks for $n = 6$.
The full row of Pascal's triangle gives $2^5 = 1 + 5 + 10 + 10 + 5 + 1 = 32$.
The first five terms give $1 + 5 + 10 + 10 + 5 = 31$.
The formula gives $R(6) = 1 + \binom{6}{2} + \binom{6}{4} = 1 + 15 + 15 = 31$, which agrees.
The missing region is the last term, $\binom{5}{5} = 1$.

The typical use of this example is to show that a few values of a sequence do not fix the sequence.
Watch out for a test drawing with equally spaced points, which gives $30$ for $n = 6$ and hides the reason for the correct count.
