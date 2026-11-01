---
tag: 2HWB7P1DZN
kind: object
name: Finite projective plane
msc: ["51E15", 05B25]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_plane
    locator: Finite projective planes
---

## Description

A finite projective plane is a finite set of points with a family of subsets, called lines, with three properties.
Every two distinct points lie on exactly one line, and every two distinct lines meet in exactly one point.
There are four points with no three on a line.
Each such plane has an order: an integer $n \ge 2$ such that each line has $n + 1$ points and each point lies on $n + 1$ lines.
A plane of order $n$ has $n^2 + n + 1$ points and $n^2 + n + 1$ lines.

The standard construction is $PG(2, q)$ for a prime power $q$.
Let $\F_q$ be the [[finite field|08RTDHX1SK]] with $q$ elements.
The points are the $1$-dimensional [[subspaces|0EPTJA5QV4]] of $\F_q^3$ and the lines are its $2$-dimensional subspaces, with incidence given by inclusion.
Check: there are $(q^3 - 1)/(q - 1) = q^2 + q + 1$ points.
Two distinct $1$-dimensional subspaces span exactly one $2$-dimensional subspace.
Two distinct $2$-dimensional subspaces $U, W$ satisfy $\dim(U \cap W) = 2 + 2 - \dim(U + W) = 1$, so they meet in exactly one point.
The four points spanned by $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ and $(1,1,1)$ have no three on a line.
So $PG(2, q)$ is a projective plane of order $q$.

## Remarks

A projective plane of order $n$ is the same thing as a [[Steiner system|7BPSC4T4M3]] $S(2, n + 1, n^2 + n + 1)$, a symmetric [[block design|4JCSS2Z1BA]].
The plane of order $2$ is the [[Fano plane|QQ8GW1ASZM]].
A projective plane of order $n$ exists if and only if there are $n - 1$ [[mutually orthogonal Latin squares|H6TN6BADVY]] of order $n$.
Every prime power is the order of a plane.
The [[Bruck–Ryser–Chowla theorem|R43K0GTTDS]] rules out the orders $6$, $14$, $21$ and many more.
A long computer search by Lam and others, finished in 1989, showed that there is no plane of order $10$.
No plane of an order that is not a prime power is known.

## Explanations

### L1 human

A finite projective plane is a small geometry with finitely many points in which any two points lie on one line.
Unlike in the usual plane, any two lines meet.
There are no parallel lines.
The smallest one has $7$ points and $7$ lines, each line with $3$ points.
