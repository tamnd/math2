---
tag: EFY92E7GC7
kind: definition
name: John ellipsoid
msc: [52A27, 52A40, 52A20]
defines: WNHXE7FCG4
uses: [437FSG3419, 0VD9ZSWWJG, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/John_ellipsoid
---

## Definition

Let $n \ge 1$ and let $B$ be the closed unit ball of $\R^n$.
An *ellipsoid* in $\R^n$ is a set $E = c + A B = \set{c + Ax : \abs{x} \le 1}$, where $c \in \R^n$ and $A$ is an invertible real $n \times n$ [[matrix|0VD9ZSWWJG]].
Its volume is $\abs{\det A}\, \kappa_n$, where $\kappa_n$ is the [[Lebesgue measure|2Z2QVWZ262]] of $B$.
Let $K \subseteq \R^n$ be a compact [[convex body|437FSG3419]] with nonempty interior.
The *John ellipsoid* of $K$ is the ellipsoid of maximal volume among all ellipsoids $E$ with $E \subseteq K$.

## Remarks

The [[Löwner–John theorem|TM5SYH4XHY]] shows that this ellipsoid exists and is unique.
The ellipsoid of minimal volume containing $K$ is the *Löwner ellipsoid* (or Löwner–John ellipsoid) of $K$.

Example: $K = [-1, 1]^2$.
Its John ellipsoid is the unit disk $B$.
The problem is invariant under the symmetries of the square, so by uniqueness the maximal ellipse is invariant under them too.
An ellipse invariant under rotation by $90°$ about the origin is a disk centered at $0$, and the largest such disk in $K$ is $B$.

Non-example: in the rectangle $K = [-2, 2] \times [-1, 1]$ the unit disk lies in $K$ but is not the John ellipsoid.
The ellipse $\set{(x, y) : x^2/4 + y^2 \le 1}$ also lies in $K$ and has area $2\pi > \pi$.

The condition that $K$ has nonempty interior is needed: otherwise every ellipsoid in $K$ would be degenerate, and no ellipsoid in the above sense lies in $K$.
