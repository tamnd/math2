---
tag: KMBHAYAGZ9
kind: definition
name: Fréchet mean
msc: [62R20, 62R30]
defines: E3GQVC04BC
uses: [0VKD1TP7F3, 0WQNRCNY3M, 0PNRKMRC55, 03Y6AQ2S0J]
sources:
  - url: https://en.wikipedia.org/wiki/Fréchet_mean
---

## Definition

Let $(M, d)$ be a [[metric space|0VKD1TP7F3]] and let $X$ be a random element of $M$ with $E[d(X, q)^2] < \infty$ for some $q \in M$.
The *Fréchet function* of $X$ is $F(p) = E[d(X, p)^2]$ for $p \in M$, an [[expected value|0WQNRCNY3M]].
A *Fréchet mean* of $X$ is a point $\mu \in M$ with
$$F(\mu) = \inf_{p \in M} F(p).$$
For points $x_1, \dots, x_n \in M$ and weights $w_i > 0$, a *Fréchet mean* is a minimiser of $p \mapsto \sum_{i=1}^{n} w_i \, d(x_i, p)^2$; with equal weights it is the *sample Fréchet mean*.

## Remarks

The condition on $q$ and the triangle inequality give $F(p) < \infty$ for every $p$.
The set of Fréchet means may be empty or have several points.
On a complete Riemannian manifold a local minimiser of $F$ is called a Karcher mean.
Replacing $d^2$ by $d$ gives the Fréchet median.

Example: in $M = \R^k$ with the Euclidean distance, $\sum_i \norm{x_i - p}^2 = \sum_i \norm{x_i - \bar x}^2 + n \norm{\bar x - p}^2$, where $\bar x$ is the [[sample mean|03Y6AQ2S0J]].
So the sample Fréchet mean is unique and equals $\bar x$.

Non-uniqueness: on the unit sphere with the great-circle distance, take two antipodal points $x$ and $-x$.
If $p$ is at distance $\theta$ from $x$, it is at distance $\pi - \theta$ from $-x$, and $\theta^2 + (\pi - \theta)^2$ is smallest exactly at $\theta = \pi/2$.
So every point of the equator between them is a Fréchet mean, and the "midpoint" is not a single point.

Non-example: if $X$ is real with the Cauchy distribution, then $E[(X - q)^2] = \infty$ for every $q \in \R$.
The moment condition fails, $F$ is infinite everywhere, and $X$ has no Fréchet mean, just as it has no ordinary mean.
