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

Put $n$ points on a circle, join each pair by a chord, and count the regions into which the chords cut the disc.
Choose the points so that no three chords pass through one point inside the circle.
This is [[Moser's circle problem|M225KZAV4F]].

1. For $n = 1$ there is no chord, and there is $1$ region.
2. For $n = 2$ there is one chord, and there are $2$ regions.
3. For $n = 3$ the three chords form a triangle, and there are $4$ regions.
4. For $n = 4$ the two diagonals cross once, and there are $8$ regions.
5. For $n = 5$ a careful drawing gives $16$ regions.
6. The pattern $1, 2, 4, 8, 16$ suggests the formula $2^{n-1}$, and so $32$ regions for $n = 6$.
7. A careful drawing for $n = 6$ gives $31$ regions. So the guess $2^{n-1}$ is false, and this is an instance of [[proof by example|ZX6ERT3SW7]] gone wrong.

The correct count is a theorem.
The number of regions is $R(n) = 1 + \binom{n}{2} + \binom{n}{4}$.

1. Start with the disc, which is $1$ region, and draw the $\binom{n}{2}$ chords one at a time.
2. A new chord that crosses $k$ chords already drawn passes through $k$ distinct crossing points, since no three chords meet at one point. These points cut the new chord into $k + 1$ pieces.
3. Each piece divides one old region into two. So the new chord adds $k + 1$ regions.
4. Summing over all chords, the total of the "$+1$" terms is $\binom{n}{2}$.
5. Each crossing point lies on exactly two chords, and it is counted once, when the second of the two chords is drawn. So the total of the "$k$" terms is the number of crossing points.
6. Each crossing point is the crossing of the two diagonals of a quadrilateral whose vertices are $4$ of the $n$ points. Each choice of $4$ points gives exactly one crossing. So there are $\binom{n}{4}$ crossing points.
7. So $R(n) = 1 + \binom{n}{2} + \binom{n}{4}$.

The values for $n = 1$ to $8$ are $1, 2, 4, 8, 16, 31, 57, 99$.
For $n = 6$: $1 + 15 + 15 = 31$.

## Remarks

The example shows that five matching terms of a sequence do not determine it.
The two formulas agree for $n \le 5$ for a reason: $2^{n-1} = \sum_{j=0}^{n-1}\binom{n-1}{j}$ and $1 + \binom{n}{2} + \binom{n}{4} = \sum_{j=0}^{4}\binom{n-1}{j}$, so they differ only by terms with $j \ge 5$, which vanish when $n \le 5$.
For $n = 10$ the two formulas give $256$ and $512$.
If the points are placed regularly, three chords can pass through one point: for the regular hexagon, the three long diagonals meet at the centre, and the count drops to $30$.

## Explanations

### L1 human

Mark points on a circle and join every pair with a straight line.
With $1, 2, 3, 4, 5$ points, the circle falls into $1, 2, 4, 8, 16$ pieces.
The numbers double each time, so we expect $32$ pieces for $6$ points.
But a careful drawing with $6$ points gives only $31$ pieces.
A pattern that holds five times can still break.

### L2 human

We check the identity of the remark for $n = 6$.

1. $2^{5} = \binom{5}{0} + \binom{5}{1} + \binom{5}{2} + \binom{5}{3} + \binom{5}{4} + \binom{5}{5} = 1 + 5 + 10 + 10 + 5 + 1 = 32$.
2. The first five terms give $1 + 5 + 10 + 10 + 5 = 31$.
3. By the formula, $R(6) = 1 + \binom{6}{2} + \binom{6}{4} = 1 + 15 + 15 = 31$, which agrees.
4. The difference $32 - 31 = 1$ is the last term $\binom{5}{5}$.

The typical use of this example is to show that a few values of a sequence do not fix the sequence.
A trap is to test the guess on a drawing with regular points, which gives $30$ for $n = 6$ and hides the reason for the correct count.
