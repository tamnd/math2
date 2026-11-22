---
tag: H8GK0ABYVC
kind: example
name: The count of colorings of K6 with a monochromatic triangle proves nothing
aliases: [count-of-colourings-of-k6-with-a-monochromatic-triangle]
msc: ["05D10", "05C55", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
not_instance_of:
  - target: 1KVSS0KRZA
    note: the bound on the number of bad colorings is 5 times the number of all colorings, so the strict inequality that the counting argument needs fails
uses: [1KVSS0KRZA, 03WKB2H474, 0GBZM0MT0F, 0K9QVPJYJF, 0NYM0ZGAK9, SAZNT80CG5]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem_on_friends_and_strangers
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ramsey%27s_theorem
    locator: lead section
---

## Example

Color each edge of the [[complete graph|03WKB2H474]] $K_6$ red or blue.
Call a coloring bad if some triangle has its three edges of one color.
We try to prove by a [[counting argument|1KVSS0KRZA]] that a coloring with no such triangle exists, and the count fails.

1. The graph $K_6$ has $\binom{6}{2} = 15$ edges, so there are $2^{15} = 32768$ colorings.
2. Fix one triangle.
   Its three edges are all red or all blue in $2 \cdot 2^{15 - 3} = 8192$ colorings, since the other $12$ edges are free.
3. There are $\binom{6}{3} = 20$ triangles, so by the union bound the number of bad colorings is at most
   $$20 \cdot 8192 = 163840.$$
4. This bound is $163840 = 5 \cdot 32768$, five times the number of all colorings.
5. So the count does not show that a good coloring exists, because the condition "fewer bad objects than objects" fails.

## Remarks

Here the conclusion is false as well.
By the [[theorem on friends and strangers|0NYM0ZGAK9]], every coloring of $K_6$ has a triangle of one color.
So no correct argument can give a good coloring of $K_6$.

A failed count does not prove that good objects do not exist.
For $K_5$, the same bound is $\binom{5}{3} \cdot 2^{1 - 3} = 10/4$ times the number of colorings, again too large.
But $K_5$ has a good coloring: color the five sides of a pentagon red and the five diagonals blue.
Each color class is then a $5$-cycle, and a $5$-cycle contains no triangle.
The union bound counts a coloring once for each bad triangle, and this overcount is large for small graphs.
The count is useful for large cliques, where it gives the [[lower bound for Ramsey numbers|SAZNT80CG5]].

## Explanations

### L1 human

Try to color the $15$ lines between $6$ points red and blue so that no triangle has one color.
A count of the bad colorings gives a number five times larger than the number of all colorings.
So the count shows nothing.
In this case nothing can work: every coloring of these $15$ lines has a triangle of one color.

### L2 human

We compare the count with the truth for triangles in $K_n$, for $n = 3, 4, 5, 6$.
The ratio of the bound to the number of all colorings is
$$\frac{\binom{n}{3} \cdot 2 \cdot 2^{\binom{n}{2} - 3}}{2^{\binom{n}{2}}} = \frac{\binom{n}{3}}{4}.$$
For $n = 3, 4, 5, 6$ the ratio is $1/4$, $1$, $5/2$ and $5$.
Only $n = 3$ gives a ratio below $1$, so the count proves only that $K_3$ has a good coloring.
The truth is that $K_3$, $K_4$ and $K_5$ have good colorings and $K_6$ has none, so the [[Ramsey number|0K9QVPJYJF]] $R(3, 3)$ is $6$.

The count works for large cliques, where one fixed clique is monochromatic with very small probability.
Watch out for two slips: a failed count is not a proof of nonexistence, and a ratio exactly equal to $1$, as for $n = 4$, is not enough.
