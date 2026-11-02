---
tag: THSVFE7YER
kind: statement
role: theorem
name: Siu's semicontinuity theorem
msc: [32U25, 32U40]
uses: [WVB60RKC3Z, BYJHP6A906, JSGWAN2RJV, GB7M582M5Y, AN0BYRKNRA, FF2P7ER3QT, TPSH4ETK67, G5JKJEAKZ9]
about: [WVB60RKC3Z, BYJHP6A906]
sources:
  - url: https://en.wikipedia.org/wiki/Lelong_number
---

## Statement

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of dimension $n$ and let $0 \le p \le n$.
Let $T$ be a closed [[positive current|BYJHP6A906]] on $X$ of bidimension $(p, p)$, that is, of bidegree $(n - p, n - p)$.
For $x \in X$ let $\nu(T, x)$ be the [[Lelong number|WVB60RKC3Z]] of $T$ at $x$.
Then for every real $c > 0$ the set
$$E_c(T) = \set{x \in X : \nu(T, x) \ge c}$$
is a closed [[analytic subset|GB7M582M5Y]] of $X$ of [[dimension|AN0BYRKNRA]] at most $p$.

## Remarks

That $E_c(T)$ is closed is elementary, since $x \mapsto \nu(T, x)$ is upper semicontinuous.
The content is that $E_c(T)$ is analytic.
Siu's original proof was long; a shorter proof by Demailly writes $E_c(T)$ locally as a common zero set of holomorphic functions built with [[Hörmander's L2 estimates|TPSH4ETK67]].

Example: let $A \subseteq X$ be an analytic subset of pure dimension $p$ and $T = [A]$ its current of integration.
By [[Thie's theorem|G5JKJEAKZ9]], $\nu([A], x)$ is the multiplicity of $A$ at $x$, so $E_c([A])$ is the set of points of multiplicity at least $c$, an analytic set.

For a [[plurisubharmonic function|FF2P7ER3QT]] $u$ on an open set of $\C^n$, apply the theorem to $T = dd^c u$ with $p = n - 1$: the sets $\set{x : \nu(u, x) \ge c}$ are analytic of dimension at most $n - 1$.

## Explanations

### L1 human

The Lelong number measures how singular a current is at a point.
The theorem says that the points where this singularity is at least a given size are not scattered at random.
They form an analytic set, cut out locally by holomorphic equations.

### L2 human

The theorem is the starting point of Siu's decomposition of a closed positive current.
It writes the current as a countable sum of currents of integration over analytic sets plus a residual part.
For the residual part, the upper level sets of Lelong numbers have smaller dimension.
It is used with multiplier ideals and with regularization of currents in the study of positivity of line bundles.
