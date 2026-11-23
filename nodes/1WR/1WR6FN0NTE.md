---
tag: 1WR6FN0NTE
kind: example
name: Nicomachus's theorem as a picture
msc: ["00A35", "11B83"]
topics: [1BTHSHST4M]
audience: school
instance_of: [V6ESFEFKJC]
uses: [V6ESFEFKJC, 23WBA59VWP, WHN4CBYZXD, EE2Y5SNFME]
sources:
  - url: https://en.wikipedia.org/wiki/Squared_triangular_number
    locator: History
  - url: https://en.wikipedia.org/wiki/Squared_triangular_number
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Proof_without_words
    locator: lead section
---

## Example

Add the first cubes and look at the totals: $1 = 1^2$, $1 + 8 = 3^2$, $1 + 8 + 27 = 6^2$ and $1 + 8 + 27 + 64 = 10^2$.
The numbers $1, 3, 6, 10$ are the [[triangular numbers|WHN4CBYZXD]] $T_k = 1 + 2 + \dots + k = \frac{k(k + 1)}{2}$, with $T_0 = 0$.
[[Nicomachus's theorem|23WBA59VWP]] states the pattern: for every integer $n \ge 1$,
$$1^3 + 2^3 + \dots + n^3 = T_n^2 = (1 + 2 + \dots + n)^2.$$
The picture is a square of side $T_n$, cut into $n$ L-shaped layers.
Layer $k$ is the part of the square of side $T_k$ outside the square of side $T_{k-1}$, with both squares in the same corner.
A drawing shows one value of $n$; it does not show why each layer has area exactly $k^3$, and the steps below give that reason for every $k$.

1. Place all the squares with a common corner at the origin, so that layer $k$ is the set of points of $[0, T_k]^2$ that are not in $[0, T_{k-1})^2$.
2. The squares $[0, T_k]^2$ are nested and grow with $k$, so the layers for $k = 1, \dots, n$ cover $[0, T_n]^2$ and overlap only along edges.
3. Layer $k$ has width $T_k - T_{k-1} = k$, because $T_k$ is $T_{k-1}$ plus the term $k$.
4. Layer $k$ is the union of a strip of size $k \times T_k$ and a strip of size $T_{k-1} \times k$, which meet only along an edge.
   So its area is $k T_k + k T_{k-1} = k (T_k + T_{k-1})$.
5. Compute the sum of two neighboring triangular numbers:
   $$T_k + T_{k-1} = \frac{k(k + 1)}{2} + \frac{(k - 1)k}{2} = \frac{2k^2}{2} = k^2.$$
6. By steps 4 and 5, layer $k$ has area $k \cdot k^2 = k^3$.
7. By step 2, the area $T_n^2$ of the whole square is the sum of the areas of the layers, so $T_n^2 = 1^3 + 2^3 + \dots + n^3$.
8. Check for $n = 4$: $1 + 8 + 27 + 64 = 100$ and $T_4 = 10$, so $T_4^2 = 100$.

## Remarks

The picture can show more than an area.
Layer $k$ can be cut into $k$ squares of side $k$, so it looks like $k$ copies of a $k \times k$ square, which is $k^3$.
The strip of size $k \times T_k$ holds $T_k / k = \frac{k + 1}{2}$ such squares, and the strip of size $T_{k-1} \times k$ holds $\frac{k - 1}{2}$ of them.
For odd $k$ both numbers are whole, and the layer splits into exactly $k$ squares.
For even $k$ each strip ends with half a square, and the two halves make one more square.
For example, when $k = 2$ the $2 \times 3$ strip holds one $2 \times 2$ square and a $2 \times 1$ half, and the $1 \times 2$ strip is the other half.

Nicomachus of Gerasa, who lived about 60 to 120 CE, gave a pattern in his *Introduction to Arithmetic* that leads to the theorem.
He grouped the odd numbers as $1$, then $3 + 5$, then $7 + 9 + 11$, and observed that the groups add up to $1^3, 2^3, 3^3, \dots$.
This gives a second proof with [[the picture of the odd numbers|EE2Y5SNFME]].
Group $k$ has $k$ odd numbers, so the first $k$ groups hold the first $T_k$ odd numbers, whose sum is $T_k^2$.
So group $k$ adds up to
$$T_k^2 - T_{k-1}^2 = (T_k - T_{k-1})(T_k + T_{k-1}) = k \cdot k^2 = k^3,$$
by steps 3 and 5.

## Explanations

### L1 human

Add the first few cubes: $1$, then $1 + 8 = 9$, then $1 + 8 + 27 = 36$, then $1 + 8 + 27 + 64 = 100$.
Every answer is a square: $1 \times 1$, $3 \times 3$, $6 \times 6$ and $10 \times 10$.
Draw a $10 \times 10$ square, and inside it squares of side $1$, $3$ and $6$ in the same corner.
The band between the $6 \times 6$ square and the $10 \times 10$ square has width $4$ and area $100 - 36 = 64$, which is $4 \times 4 \times 4$.
Each band is one cube, so the cubes fill the big square.

### L2 human

We check the layers for $n = 3$, where $T_1 = 1$, $T_2 = 3$ and $T_3 = 6$.
Layer $1$ is the $1 \times 1$ square, of area $1 = 1^3$.
Layer $2$ is a $2 \times 3$ strip and a $1 \times 2$ strip, of area $6 + 2 = 8 = 2^3$.
Layer $3$ is a $3 \times 6$ strip and a $3 \times 3$ strip, of area $18 + 9 = 27 = 3^3$.
The total is
$$1 + 8 + 27 = 36 = 6^2,$$
the area of the big square.
The typical use of the picture is to see why a sum of cubes is a square, which a proof by induction checks but does not explain.
Watch out at step 5: the width of layer $k$ is $k$, but its outer side is $T_k$ and not $k^2$, and the area $k^3$ comes from the identity $T_k + T_{k-1} = k^2$.
