---
tag: G8DBMWQSDB
kind: definition
name: Calderón projector
msc: [35S15, 35J40, 58J40]
defines: K4XSSPWHCP
uses: [B4TTNHSTRX, K2NK9A8M5F, Z2T5R88QDB, FF27N0BWTP, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Calder%C3%B3n_projector
---

## Definition

Let $\Omega \subset \R^n$ be a bounded open set with smooth boundary $\Gamma = \partial\Omega$ and outward unit normal $\nu$.
Let $P$ be an [[elliptic|B4TTNHSTRX]] linear differential operator of order $2m$ with smooth coefficients on a neighbourhood $U$ of $\overline{\Omega}$.
Assume $P$ has a [[fundamental solution|K2NK9A8M5F]] $E$ on $U$, that is, $P E = \delta$ in the sense of distributions.
For $u$ smooth up to $\Gamma$, let $\gamma u = (u|_\Gamma, \partial_\nu u|_\Gamma, \ldots, \partial_\nu^{2m-1} u|_\Gamma)$ be its Cauchy data, given by the [[trace operator|Z2T5R88QDB]].
Green's formula for $P$ gives a potential operator $K$, built from $E$, such that $u = K(\gamma u)$ in $\Omega$ whenever $Pu = 0$ in $\Omega$.
Let $\gamma_+$ take the Cauchy data of a function on $\Omega$ as limits from inside.
The *Calderón projector* of $P$ and $\Omega$ is the operator $C = \gamma_+ K$ on $2m$-tuples of functions on $\Gamma$.

## Remarks

$C$ is a $2m \times 2m$ matrix of [[pseudo-differential operators|FF27N0BWTP]] on $\Gamma$, $C^2 = C$, and its range is the space of Cauchy data $\gamma u$ of the solutions of $Pu = 0$ in $\Omega$.
If $E$ is only a parametrix, then $C$ is a projection up to smoothing operators, which is enough for most uses.
Example: for $P = -\Delta$ ($m = 1$), $C$ acts on pairs $(f, g)$.
Its four entries are, up to signs and the factor $\tfrac12 I$, the double layer, single layer, hypersingular and adjoint double layer operators.
A pair $(f, g)$ is fixed by $C$ exactly when $f = u|_\Gamma$ and $g = \partial_\nu u|_\Gamma$ for a [[harmonic function|0DEB0JMN0W]] $u$ on $\Omega$.
Non-example: the identity on pairs $(f, g)$ is a projection, but its range is too large.
On the unit disk it contains $(0, 1)$, which is not Cauchy data of a harmonic $u$, since $u = 0$ on the circle forces $u = 0$.
