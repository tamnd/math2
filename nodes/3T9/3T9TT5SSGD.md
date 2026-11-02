---
tag: 3T9TT5SSGD
kind: conjecture
name: Uniform boundedness conjecture for preperiodic points
msc: [37P35, 37P15, 11G05]
uses: [MWBDFS2KJ5, ZT9A6JK8QF, BE4X0QG8XW]
about: [BE4X0QG8XW]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_dynamics
history:
  posed_by: "Patrick Morton and Joseph Silverman"
  first_stated: "1994"
---

## Statement

Let $N \ge 1$, $d \ge 2$ and $D \ge 1$ be integers.
There is a constant $B = B(N, d, D)$ with the following property.
Let $K$ be a [[number field|MWBDFS2KJ5]] with $[K : \Q] \le D$.
Let $\phi \colon \mathbb{P}^N \to \mathbb{P}^N$ be a morphism of degree $d$ defined over $K$.
Then the number of preperiodic points of $\phi$ in $\mathbb{P}^N(K)$ is at most $B$.

## Remarks

Here a point $P$ of [[projective space|ZT9A6JK8QF]] is preperiodic for $\phi$ when its forward orbit $\set{\phi^n(P) : n \ge 0}$ is finite, as in [[arithmetic dynamics|BE4X0QG8XW]].
For each single $\phi$, the set of preperiodic points in $\mathbb{P}^N(K)$ is finite by Northcott's theorem on heights.
The conjecture asks for a bound that depends only on $N$, $d$ and $D$.

The conjecture is open, even for the maps $\phi(z) = z^2 + c$ with $c \in \Q$ acting on $\mathbb{P}^1(\Q)$.

The case $N = 1$, $d = 4$ implies the uniform boundedness of torsion of elliptic curves, proved by Merel in 1996.
Indeed, let $E$ be an elliptic curve over $K$.
The $x$-coordinates of its torsion points are preperiodic points of the degree $4$ Lattès map that describes doubling on $E$.
At most two points of $E$ share an $x$-coordinate.

## Explanations

### L1 human

Fix a kind of polynomial or rational map, like $z \mapsto z^2 + c$, and a kind of number system, like the fractions.
For each single map, only finitely many fractions eventually repeat under iteration.
The conjecture says more: there is one bound on how many such fractions there can be, the same for all maps of that degree.
It is a dynamical version of famous finiteness results about elliptic curves.
