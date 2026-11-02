---
tag: 4T7D0T5GJA
kind: object
name: Sobol sequence
msc: [11K38, 11K45, 65C05]
instance_of: [XSPX1KW9AQ]
uses: [XSPX1KW9AQ, HQ7KMZYPSQ, ABSRB2KXA6]
sources:
  - url: https://en.wikipedia.org/wiki/Sobol_sequence
same_as:
  wikidata: Q7550116
  wikipedia: Sobol sequence
---

## Description

A *Sobol sequence* is a sequence of points in $[0,1)^s$ built from binary digits.
For each coordinate $j = 1, \ldots, s$ one fixes direction numbers $v_{j,1}, v_{j,2}, \ldots \in (0,1)$, constructed as follows.

1. Choose a [[primitive polynomial over $\F_2$|HQ7KMZYPSQ]] $x^{d} + c_1 x^{d-1} + \cdots + c_{d-1} x + 1$ of degree $d = d_j$, with different polynomials for different $j$.
2. Choose odd integers $m_1, \ldots, m_d$ with $m_k < 2^k$.
3. For $k > d$ set $m_k = 2 c_1 m_{k-1} \oplus 2^2 c_2 m_{k-2} \oplus \cdots \oplus 2^{d-1} c_{d-1} m_{k-d+1} \oplus 2^d m_{k-d} \oplus m_{k-d}$, where $\oplus$ is the bitwise exclusive or of binary integers.
4. Set $v_{j,k} = m_k / 2^k$.

Write $n \ge 0$ in binary as $n = \sum_{k \ge 1} \beta_k 2^{k-1}$ with $\beta_k \in \set{0,1}$.
The $j$-th coordinate of the $n$-th point is
$$x_{n,j} = \beta_1 v_{j,1} \oplus \beta_2 v_{j,2} \oplus \cdots,$$
where $\oplus$ now acts digit by digit on binary expansions.
The first coordinate usually takes $v_{1,k} = 2^{-k}$, which gives the van der Corput sequence in base $2$.

## Remarks

Take $s = 2$, the van der Corput sequence in the first coordinate, and the polynomial $x + 1$ with $m_1 = 1$ in the second.
The recurrence gives $m_k = 2 m_{k-1} \oplus m_{k-1}$, so $m_1, m_2, m_3 = 1, 3, 5$ and $v_{2,k} = 1/2, 3/4, 5/8$.
The points for $n = 0, 1, 2, 3$ are $(0,0)$, $(1/2, 1/2)$, $(1/4, 3/4)$, $(3/4, 1/4)$; for $n = 3$ the second coordinate is $0.10_2 \oplus 0.11_2 = 0.01_2 = 1/4$.
Each of the four squares of side $1/2$ contains exactly one of these points.
So does each vertical strip of width $1/4$ and each horizontal strip of height $1/4$.
In general Sobol sequences are $(t,s)$-sequences in base $2$ in the sense of Niederreiter, and their star discrepancy is $O\big((\log N)^s / N\big)$.
So they are [[low-discrepancy sequences|XSPX1KW9AQ]], widely used in [[quasi-Monte Carlo methods|ABSRB2KXA6]].
The quality of the points in practice depends on the choice of the initial numbers $m_k$.
Because the construction uses only bit operations, the points are very fast to generate, especially in Gray code order.

## Explanations

### L1 human

A Sobol sequence is a list of points that fills a square or a cube very evenly.
Each coordinate is made by combining a few fixed binary fractions, chosen by the binary digits of the point's index.
The construction makes the first $2^m$ points, for each $m$, spread out evenly over grids of small boxes.
For example, the first four points in the plane put one point in each quarter of the unit square.
These points serve as sample points for computing averages of functions with high accuracy.
