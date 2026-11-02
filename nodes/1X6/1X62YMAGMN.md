---
tag: 1X62YMAGMN
kind: definition
name: Balayage
msc: [31B15, 31C15, 31D05]
defines: NTFY23YDEJ
uses: [CFD7BPM51W, DCMFQ01QGS, DYR1QFNGNJ, B7948M365K, 909B1WYQ4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Balayage
---

## Definition

Let $n \ge 3$ and let $D \subset \R^n$ be a bounded domain whose boundary points are all [[regular|B7948M365K]].
For $x \in D$, let $\omega_x$ be the [[harmonic measure|CFD7BPM51W]] of $D$ at $x$, a Borel probability measure on $\partial D$.
Let $\mu$ be a finite positive [[Borel measure|DYR1QFNGNJ]] with compact support in $D$.
The *balayage* of $\mu$ onto $\partial D$ is the Borel measure $\mu'$ on $\partial D$ given by
$$\mu'(A) = \int_D \omega_x(A)\, d\mu(x) \qquad \text{for every Borel set } A \subseteq \partial D.$$

## Remarks

Write $U^\mu(y) = \int \abs{y - x}^{2-n}\, d\mu(x)$ for the [[Newtonian potential|DCMFQ01QGS]].
Then $\mu'(\partial D) = \mu(D)$ and $U^{\mu'} = U^\mu$ on $\R^n \setminus D$.
Indeed, for $y \notin \overline{D}$ the function $x \mapsto \abs{y - x}^{2-n}$ is harmonic on $D$ and continuous on $\overline{D}$, so it is the integral of its boundary values against $\omega_x$.
Inside $D$ one has $U^{\mu'} \le U^\mu$.
Example: let $D$ be the ball of radius $R$ about $0$ and $\mu = \delta_0$.
Then $\omega_0$ is the normalised surface measure on the sphere, so $\mu'$ is that measure.
Its potential is $\min(R^{2-n}, \abs{y}^{2-n})$, which equals $\abs{y}^{2-n} = U^{\delta_0}(y)$ for $\abs{y} \ge R$.
Non-example: $\mu$ itself is not a balayage of $\mu$ onto $\partial D$, since it is not carried by $\partial D$.
More generally, for any set $E \subseteq \R^n$ the balayage $\mu^E$ is the measure whose potential is the regularised [[reduced function|909B1WYQ4Q]] $\widehat{R}^E_{U^\mu}$.
