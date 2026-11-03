---
tag: RYAQP17PHH
kind: statement
role: proposition
name: Phyllotaxis and the golden angle
msc: [92C80, 11J70, 11K06]
uses: [0SC8T7548D, 0DZXAXEJQ9, 04P2RJ4WPS, 0GA9K57A39]
about: [0SC8T7548D]
sources:
  - url: https://en.wikipedia.org/wiki/Phyllotaxis
  - url: https://en.wikipedia.org/wiki/Golden_angle
---

## Statement

Let $\varphi = (1 + \sqrt 5)/2$ be the [[golden ratio|0SC8T7548D]], and let $(F_n)_{n \ge 0}$ be the [[Fibonacci sequence|0GA9K57A39]] with $F_0 = 0$ and $F_1 = 1$.
The *golden angle* is the angle $\alpha = 2\pi / \varphi^2$, which equals $2\pi (2 - \varphi) \approx 137.508^\circ$.

1. The fraction of a full turn $\alpha / (2\pi) = 1/\varphi^2$ is an [[irrational number|0DZXAXEJQ9]].
2. Its [[continued fraction|04P2RJ4WPS]] expansion is $[0; 2, 1, 1, 1, \dots]$, with all partial quotients after the first equal to $1$.
3. Its convergents are the ratios $F_n / F_{n+2}$ for $n \ge 1$, namely $1/2, 1/3, 2/5, 3/8, 5/13, \dots$.

## Remarks

The proof uses $\varphi^2 = \varphi + 1$, which gives $1/\varphi^2 = 2 - \varphi$ and $1/\varphi^2 = 1/(2 + 1/\varphi)$.
Since $1/\varphi = [0; 1, 1, 1, \dots]$, the expansion follows, and the convergents of $[0; 1, 1, \dots]$ are $F_n / F_{n+1}$, which turns into $F_n / F_{n+2}$ after the shift.
In phyllotaxis, successive leaves or seeds are often placed at a constant divergence angle close to $\alpha$.
In Vogel's model of a sunflower head, seed $k$ sits at polar angle $k \alpha$ and radius $c \sqrt k$.
The convergents explain the spirals one sees.
Seeds whose indices differ by a Fibonacci number $F_m$ are close in angle, since $F_m \alpha / (2\pi)$ is close to the integer $F_{m-2}$.
So the eye picks out families of $F_m$ spirals, with consecutive Fibonacci counts such as $21$ and $34$, or $34$ and $55$.
All partial quotients are $1$ from some point on.
So $1/\varphi^2$ is as badly approximable by rationals as a number can be, in the sense of [[Hurwitz's theorem|3RDB8B5GFA]].
As a result the angles $k \alpha$ spread evenly around the circle without lining up.

## Explanations

### L1 human

Many plants place each new leaf or seed about $137.5^\circ$ around from the previous one.
This angle splits the full turn in the golden ratio.
The golden ratio is the irrational number that is hardest to approximate by fractions.
So seeds placed this way never stack up in a few straight rows, and they pack the head of a sunflower densely.
The spirals that one sees come in Fibonacci numbers because the best fractions near the golden angle are ratios of Fibonacci numbers.

### L2 human

The statement is pure number theory.
The biology is the observation that divergence angles near $\alpha$ are common.
Models in which each new primordium appears where there is most room tend to produce such angles.
For any divergence angle $\beta$, the points $k \beta$ with $1 \le k \le N$ cut the circle into arcs of at most three lengths.
This is the three-distance theorem, and the continued fraction of $\beta / (2\pi)$ decides these lengths.
Other angles with expansions ending in all ones, such as $2\pi/(\varphi + 2)$, give the less common Lucas-type patterns.
