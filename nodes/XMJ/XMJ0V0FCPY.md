---
tag: XMJ0V0FCPY
kind: definition
name: Associated bundle
msc: [55R10, 57R22]
defines: NVVGA3KEWE
uses: [8E37E74XVP, 0WCY42EV9V, 0BR3FY5Q8M, 0GBG8B49AA]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_bundle
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] and let $\pi \colon P \to B$ be a [[principal $G$-bundle|8E37E74XVP]], with $G$ acting on $P$ from the right.
Let $F$ be a topological space with a continuous left [[action|0WCY42EV9V]] of $G$.
On $P \times F$, with the [[product topology|0GBG8B49AA]], let $G$ act by $g \cdot (p, f) = (p g^{-1}, g f)$.
The *associated bundle* with fiber $F$ is the [[quotient space|0BR3FY5Q8M]]
$$P \times_G F = (P \times F) / G,$$
together with the map $\pi_F \colon P \times_G F \to B$, $\pi_F([p, f]) = \pi(p)$.

## Remarks

The map $\pi_F$ is well defined because $\pi(p g^{-1}) = \pi(p)$.
It is a fiber bundle with fiber $F$: a local trivialization $\pi^{-1}(U) \cong U \times G$ of $P$ induces $\pi_F^{-1}(U) \cong U \times F$.
The class $[p, f]$ is also written $p \times_G f$; in it, $[p g, f] = [p, g f]$.

Example: let $G = \Z/2\Z$ and $P = S^1 \to S^1$, $z \mapsto z^2$, a principal $G$-bundle where the generator acts by $z \mapsto -z$.
Let the generator act on $F = \R$ by $t \mapsto -t$.
Then $P \times_G \R$ is the quotient of $S^1 \times \R$ by $(z, t) \sim (-z, -t)$, which is the open Möbius band, a nontrivial line bundle over the circle.

Non-example: the product $P \times F$ itself, with the map $(p, f) \mapsto \pi(p)$, is not the associated bundle when $G$ is nontrivial.
Its fibers are copies of $G \times F$, not of $F$, because the quotient by $G$ was not taken.

If $F = \R^n$ with $G = GL_n(\R)$ acting linearly, then $P \times_G \R^n$ is a real vector bundle of rank $n$.
