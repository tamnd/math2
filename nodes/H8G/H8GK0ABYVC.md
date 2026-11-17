---
tag: H8GK0ABYVC
kind: example
name: The count of colourings of K6 with a monochromatic triangle proves nothing
msc: ["05D10", "05C55", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
not_instance_of:
  - target: 1KVSS0KRZA
    note: the bound on the number of bad colourings is 5 times the number of all colourings, so the strict inequality that the counting argument needs fails
uses: [1KVSS0KRZA, 03WKB2H474, 0GBZM0MT0F, 0K9QVPJYJF, 0NYM0ZGAK9, SAZNT80CG5]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem_on_friends_and_strangers
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ramsey%27s_theorem
    locator: lead section
---

## Example

Colour each edge of the [[complete graph|03WKB2H474]] $K_6$ red or blue.
A colouring is bad if some triangle has its three edges of one colour.
We try to prove by a [[counting argument|1KVSS0KRZA]] that a colouring with no bad triangle exists, and the count fails.

1. The graph $K_6$ has $\binom{6}{2} = 15$ edges, so there are $2^{15} = 32768$ colourings.
2. Fix one triangle. Its three edges are all red or all blue in $2 \cdot 2^{15 - 3} = 8192$ colourings.
3. There are $\binom{6}{3} = 20$ triangles, so the number of bad colourings is at most $20 \cdot 8192 = 163840$.
4. The bound $163840 = 5 \cdot 32768$ is larger than the number of all colourings.
5. So the count does not show that a good colouring exists. The condition "fewer bad objects than objects" fails.

## Remarks

Here the conclusion is also false.
By the [[theorem on friends and strangers|0NYM0ZGAK9]], every colouring of $K_6$ has a triangle of one colour.
So no correct argument can give a good colouring of $K_6$.

A failed count does not prove that good objects do not exist.
For $K_5$, the same bound is $\binom{5}{3} \cdot 2^{1 - 3} = 10/4$ times the number of colourings, which is again too large.
But $K_5$ has a good colouring: colour the five sides of a pentagon red and the five diagonals blue.
The union bound counts a colouring once for each bad triangle, and this overcount is large for small graphs.
For triangles, the count works only for $n = 3$, where $\binom{3}{3} \cdot 2^{1 - 3} = 1/4 < 1$.
The count is useful for large $k$, where it gives the [[lower bound for Ramsey numbers|SAZNT80CG5]].

## Explanations

### L1 human

We try to colour the $15$ lines between $6$ points so that no triangle has one colour.
A count of the bad colourings gives a number five times larger than the number of all colourings.
So the count shows nothing.
In this case nothing can work: every colouring of these $15$ lines has a triangle of one colour.

### L2 human

We compare the count with the truth for the triangle and $K_n$, with $n = 3, 4, 5, 6$.

1. The ratio of the bound to the number of all colourings is $\binom{n}{3} \cdot 2^{1 - 3} = \binom{n}{3}/4$.
2. For $n = 3, 4, 5, 6$, the ratio is $1/4$, $1$, $5/2$ and $5$.
3. Only $n = 3$ gives a ratio less than $1$. So the count proves only that $K_3$ has a good colouring.
4. The truth is that $K_3$, $K_4$ and $K_5$ have good colourings, and $K_6$ has none. So the [[Ramsey number|0K9QVPJYJF]] $R(3, 3)$ is $6$.

The typical use of the count is for large cliques, where the probability that one clique has one colour is very small.
A trap is to read a failed count as a proof of nonexistence.
For $n = 4$ the ratio is exactly $1$, and a ratio equal to $1$ is not enough.
