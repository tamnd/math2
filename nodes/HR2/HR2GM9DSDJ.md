---
tag: HR2GM9DSDJ
kind: definition
name: Hunt process
msc: [60J45, 60J25, 60J40]
defines: Z7T669BQ9B
uses: [0QH5ENKZM1, 0B77KZCQ51, WND87FBAKC, HNK1Y62G7V, 22735FGJV6, 4HS3C12472]
sources:
  - url: https://en.wikipedia.org/wiki/Hunt_process
---

## Definition

Let $E$ be a locally compact Hausdorff space with a countable base, and let $E_\Delta = E \cup \set{\Delta}$ be its one-point compactification; the point $\Delta$ is the cemetery.
Let $X = (X_t)_{t \ge 0}$ be a [[stochastic process|0QH5ENKZM1]] with values in $E_\Delta$, adapted to a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_t)$, with a family of probability measures $(P^x)_{x \in E_\Delta}$.
$X$ is a *Hunt process* if:

1. $X$ is a Markov process with respect to $(\mathcal{F}_t)$ under each $P^x$, with $P^x(X_0 = x) = 1$, and $\Delta$ is absorbing: $X_t = \Delta$ implies $X_s = \Delta$ for all $s \ge t$.
2. Each path $t \mapsto X_t$ is right-continuous on $[0, \infty)$ and has left limits in $E_\Delta$ on $(0, \infty)$.
3. $X$ has the strong [[Markov property|0B77KZCQ51]] at every [[stopping time|WND87FBAKC]] of $(\mathcal{F}_t)$, where $(\mathcal{F}_t)$ is right-continuous and suitably completed.
4. $X$ is quasi-left-continuous: if $T_n$ are stopping times increasing to $T$, then $X_{T_n} \to X_T$ almost surely on $\set{T < \infty}$, under each $P^x$.

## Remarks

The time $\zeta = \inf\set{t : X_t = \Delta}$ is the lifetime of the process.
Example: [[Brownian motion|22735FGJV6]] in $\R^d$ is a Hunt process, with $\zeta = \infty$; more generally every [[Feller process|4HS3C12472]] with right-continuous paths having left limits is a Hunt process.
Non-example: on $E = \R$, let the process move deterministically at unit speed, except that it jumps up by $1$ when it reaches the point $1$ from below.
It is a strong Markov process with right-continuous paths, but clause 4 fails.
Started at $0$, the stopping times $T_n = 1 - 1/n$ increase to $T = 1$, while $X_{T_n} \to 1$ and $X_T = 2$.
Quasi-left-continuity allows jumps only at totally inaccessible times, such as the jump times of a Poisson process.
