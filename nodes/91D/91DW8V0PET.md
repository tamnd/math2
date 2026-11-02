---
tag: 91DW8V0PET
kind: statement
role: theorem
name: Maximum modulus principle in several variables
msc: [32A10]
uses: [507C34W0ZT, 7GZ908QZ04, 048F2P90WR]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_modulus_principle
---

## Statement

Let $D \subseteq \C^n$ be a nonempty connected open set, and let $f$ be a [[holomorphic function|507C34W0ZT]] on $D$.
If there is a point $a \in D$ with $\abs{f(z)} \le \abs{f(a)}$ for all $z \in D$, then $f$ is constant on $D$.

## Remarks

For $z$ near $a$, the map $t \mapsto f(a + t(z - a))$ is a holomorphic function of one variable on a disc around $t = 0$ whose modulus has a maximum at $t = 0$.
By the one-variable [[maximum modulus principle|048F2P90WR]] it is constant, so $f$ is constant near $a$, and the [[identity theorem|7GZ908QZ04]] makes $f$ constant on $D$.
Consequence: if $D$ is bounded and $f$ is continuous on the closure $\overline{D}$ and holomorphic on $D$, then $\max_{\overline{D}} \abs{f}$ is attained on the boundary of $D$.
Connectedness is needed: on two disjoint balls, a function equal to $0$ on one and $1$ on the other attains its maximum modulus without being constant.
Example: on the unit polydisc of $\C^2$, $f(z) = z_1 z_2$ satisfies $\abs{f} < 1$ inside and reaches $\abs{f} = 1$ only where $\abs{z_1} = \abs{z_2} = 1$, on the distinguished boundary.

## Explanations

### L1 human

The size $\abs{f}$ of a non-constant holomorphic function never has a highest point inside its domain.
So on a bounded domain the largest value of $\abs{f}$ is found on the edge.
It is the same principle as in one variable, and it is proved by restricting to complex lines.

### L2 human

The proof is a typical way to pass from one to several variables: restrict to complex lines through a point and use the one-variable result.
For special domains the maximum is found on a much smaller part of the boundary.
On a polydisc it is the [[distinguished boundary|A6HN207Y2T]], an $n$-dimensional torus.
The study of these smallest sets leads to the Shilov boundary and to peak points.
