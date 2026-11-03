---
tag: 1V8DM3ZQMV
kind: example
name: Haar measure on the p-adic numbers
msc: [43A05, 11S80, 28C10]
instance_of: [VY0HXD3GC4]
uses: [BT6T702C28, V6TJAFZ4MD, WGN82TCEF2, KB792QTG4F]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_number
---

## Example

Let $p$ be a prime, and let $\Q_p$ be the field of [[p-adic numbers|BT6T702C28]] with the [[p-adic absolute value|WGN82TCEF2]] $\abs{\cdot}_p$.
Let $\Z_p = \set{x : \abs{x}_p \le 1}$ be the ring of [[p-adic integers|V6TJAFZ4MD]].
The additive group $(\Q_p, +)$ is locally compact, and $\Z_p$ is a compact open subgroup.
By the [[existence and uniqueness of Haar measure|KB792QTG4F]], there is a unique Haar measure $\mu$ on $(\Q_p, +)$ with $\mu(\Z_p) = 1$.

Its values on balls follow from invariance alone.
For $k \ge 0$, the subgroup $p^k \Z_p$ has index $p^k$ in $\Z_p$, so $\Z_p$ is a disjoint union of $p^k$ translates of $p^k \Z_p$.
These translates have equal measure, hence $\mu(a + p^k \Z_p) = p^{-k}$ for every $a \in \Q_p$.
For $k < 0$, the ball $p^k \Z_p$ is a disjoint union of $p^{-k}$ translates of $\Z_p$, so again $\mu(a + p^k \Z_p) = p^{-k}$.
Since $\abs{p^k}_p = p^{-k}$, the ball $\set{x : \abs{x - a}_p \le p^{-k}}$ has measure equal to its radius $p^{-k}$.

More generally, $\mu(cA) = \abs{c}_p \, \mu(A)$ for every $c \in \Q_p$ with $c \ne 0$ and every Borel set $A$.

## Explanations

### L1 human

In the $p$-adic numbers, the balls are nested groups: each ball of radius $1$ splits into exactly $p$ smaller balls of radius $1/p$.
A fair measure must give all these smaller balls the same size, so each gets $1/p$ of the size of the big ball.
Repeating, a ball of radius $p^{-k}$ has measure $p^{-k}$.
So on $\Q_p$, the Haar measure of a ball is just its radius, and this measure is the base of integration in $p$-adic analysis and number theory.
