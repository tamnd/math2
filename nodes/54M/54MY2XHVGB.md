---
tag: 54MY2XHVGB
kind: object
name: Halton sequence
msc: [11K38, 11K45, 65C05]
instance_of: [XSPX1KW9AQ]
uses: [XSPX1KW9AQ, 01826KMG2H, ABSRB2KXA6]
sources:
  - url: https://en.wikipedia.org/wiki/Halton_sequence
same_as:
  wikidata: Q5643679
  wikipedia: Halton sequence
---

## Description

Let $b \ge 2$ be an integer.
Each integer $n \ge 0$ has a unique base-$b$ expansion $n = \sum_{k \ge 0} a_k b^k$ with digits $a_k \in \set{0, \ldots, b-1}$, almost all zero.
The *radical inverse* in base $b$ is
$$\varphi_b(n) = \sum_{k \ge 0} a_k \, b^{-k-1} \in [0,1).$$
It mirrors the digits of $n$ at the radix point.
The sequence $(\varphi_b(n))_{n \ge 0}$ is the van der Corput sequence in base $b$.
Let $s \ge 1$ and let $b_1, \ldots, b_s \ge 2$ be pairwise coprime integers.
The *Halton sequence* in these bases is the sequence of points
$$x_n = \big(\varphi_{b_1}(n), \ldots, \varphi_{b_s}(n)\big) \in [0,1)^s, \qquad n = 0, 1, 2, \ldots$$
The usual choice is $b_1, \ldots, b_s$ the first $s$ [[prime numbers|01826KMG2H]].

## Remarks

In bases $2$ and $3$, the points for $n = 1, 2, 3, 4$ are $(1/2, 1/3)$, $(1/4, 2/3)$, $(3/4, 1/9)$, $(1/8, 4/9)$.
For example $3 = 10_3$ in base $3$, so $\varphi_3(3) = 0.01_3 = 1/9$.
For pairwise coprime bases, the star discrepancy of the first $N$ points is $O\big((\log N)^s / N\big)$, with a constant depending on $s$ and the bases.
So the Halton sequence is a [[low-discrepancy sequence|XSPX1KW9AQ]], and it is a standard point set for [[quasi-Monte Carlo methods|ABSRB2KXA6]].
The coprimality condition matters: with $b_1 = b_2 = 2$, all points lie on the diagonal of the unit square, which they do not fill.
In high dimension the coordinates with large bases are correlated for moderate $N$, and scrambled variants are used in practice.

## Explanations

### L1 human

Write the counting numbers $1, 2, 3, \ldots$ in base $2$ and read each one backwards after a binary point.
This gives $1/2, 1/4, 3/4, 1/8, 5/8, \ldots$, and each new point falls into one of the largest gaps left by the earlier ones.
Do the same in base $3$, base $5$, and so on, and use the results as the coordinates of a point.
The points fill a square or cube far more evenly than random points do.
This makes them good sample points for computing averages.
