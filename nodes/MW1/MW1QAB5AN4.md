---
tag: MW1QAB5AN4
kind: definition
name: Runge domain
msc: ["32E30"]
defines: A3R53S95KP
uses: [507C34W0ZT, 07GNX8GCYP, 08VZ57PT26, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Runge%27s_theorem
---

## Definition

Let $D \subseteq \C^n$ be an [[open set|02BH3MCBQB]].
Then $D$ is a *Runge domain* if the following holds for every [[holomorphic function|507C34W0ZT]] $f$ on $D$.
For every compact set $K \subseteq D$ and every $\varepsilon > 0$ there is a [[polynomial|07GNX8GCYP]] $p$ in $z_1, \dots, z_n$ with $\abs{f(z) - p(z)} < \varepsilon$ for all $z \in K$.

Equivalently, the polynomials are dense in the space of holomorphic functions on $D$ for the topology of [[uniform convergence|08VZ57PT26]] on compact subsets.

## Remarks

Example: the unit polydisc $\Delta^n$.
Every holomorphic $f$ on $\Delta^n$ is the sum of its Taylor series at $0$, and this series converges uniformly on each compact subset of $\Delta^n$; its partial sums are polynomials.
More generally every convex open set is a Runge domain, by the [[Oka–Weil theorem|7AWZJNQGT2]] applied to the convex hull of $K$, which is compact and polynomially convex.

Non-example: $D = \set{z \in \C^n : 1 < \abs{z_1} < 2}$ and $f(z) = 1/z_1$.
On the compact circle $K = \set{\abs{z_1} = 3/2, \ z_2 = \cdots = z_n = 0}$, every polynomial $p$ satisfies $\int_{\abs{\zeta} = 3/2} p(\zeta, 0, \dots, 0) \, d\zeta = 0$, while the same integral of $f$ is $2\pi i$.
So $f$ is not a uniform limit of polynomials on $K$.

For $n = 1$, [[Runge's theorem|6DG4CTGXJD]] gives a complete answer.
An open set $D \subseteq \C$ is a Runge domain exactly when every connected component of $D$ is simply connected.
