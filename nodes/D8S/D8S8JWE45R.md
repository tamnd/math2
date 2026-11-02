---
tag: D8S8JWE45R
kind: statement
role: theorem
name: Domain of convergence of a power series
msc: [32A05, 32Q02]
uses: [R3QTCPTJK7, 6YT8ZM6B0F, WA0SE56FVH, EHWH6EF4QY, 507C34W0ZT]
about: [R3QTCPTJK7, EHWH6EF4QY]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Statement

Let $\sum_{\alpha \in \N^n} c_\alpha z^\alpha$ be a [[power series in several variables|R3QTCPTJK7]] with centre $0$.
Let $S$ be the set of points of $\C^n$ where it converges, and let $D$ be the interior of $S$, its *domain of convergence*.
Suppose that $D$ is nonempty.
Then:

1. $D$ is a complete [[Reinhardt domain|WA0SE56FVH]].
2. $D$ is [[logarithmically convex|EHWH6EF4QY]].
3. The series converges absolutely and uniformly on every compact subset of $D$, and its sum is a [[holomorphic function|507C34W0ZT]] on $D$.

## Remarks

If $z \in D$, there is a point $w \in S$ with $\abs{w_j} > \abs{z_j}$ for all $j$.
Then [[Abel's lemma|6YT8ZM6B0F]] gives convergence on the polydisc $\set{\abs{w'_j} < \abs{w_j}}$, which contains $z$ and every $w'$ with $\abs{w'_j} \le \abs{z_j}$.
This gives the first and third parts.
For the second part, suppose the terms are bounded by $M$ at $z$ and at $w$, and let $0 \le t \le 1$.
If $\abs{u_j} = \abs{z_j}^{1-t} \abs{w_j}^{t}$ for all $j$, then $\abs{c_\alpha u^\alpha} = \abs{c_\alpha z^\alpha}^{1-t} \abs{c_\alpha w^\alpha}^{t} \le M$.
So the set of logarithms of absolute values is convex.
Example: the series $\sum_{k \ge 0} (z_1 z_2)^k$ has domain of convergence $\set{\abs{z_1 z_2} < 1}$, whose image under $z \mapsto (\log\abs{z_1}, \log\abs{z_2})$ is the half-plane $x_1 + x_2 < 0$.
This domain is unbounded and is not a polydisc, which never happens for $n = 1$, where the domain of convergence is a disc or the whole plane.
Conversely, every logarithmically convex complete Reinhardt domain with centre $0$ is the domain of convergence of some power series.

## Explanations

### L1 human

In one variable, a power series converges on a disc, and the disc is fixed by one number, the radius of convergence.
In several variables, the region of convergence can have many shapes.
The theorem says which shapes can occur.
They are symmetric under rotating each coordinate, they are "filled in" towards the origin, and they become convex after taking logarithms of absolute values.

### L2 human

This result explains why Reinhardt domains and logarithmic convexity appear so early in the theory.
It is a first example of the convexity conditions that characterise domains of holomorphy.
For instance, a holomorphic function on a complete Reinhardt domain $D$ with centre $0$ has a power series at $0$ that converges on all of $D$.
Hence it converges on the smallest logarithmically convex complete Reinhardt domain containing $D$.
So the holomorphic functions on a complete Reinhardt domain that is not logarithmically convex, such as a union of two crossed polydiscs, all extend to a larger domain.
