---
tag: F0QRCDYBXK
kind: definition
name: Pluripolar set
msc: [32U15, 32U20]
defines: N0MAGPW8AP
uses: [FF2P7ER3QT]
sources:
  - url: https://en.wikipedia.org/wiki/Pluripolar_set
---

## Definition

Let $E \subseteq \C^n$.
The set $E$ is *pluripolar* if each point $a \in E$ has an open neighbourhood $U$ with the following property.
There is a [[plurisubharmonic function|FF2P7ER3QT]] $u$ on $U$, not identically $-\infty$ on any component of $U$, such that
$$E \cap U \subseteq \set{z \in U : u(z) = -\infty}.$$
The set $E$ is *complete pluripolar* in an open set $\Omega$ if $E = \set{z \in \Omega : u(z) = -\infty}$ for some function $u$ of the following kind.
The function $u$ is plurisubharmonic on $\Omega$ and not identically $-\infty$ on any component of $\Omega$.

## Remarks

Some authors call the sets of the first definition locally pluripolar, and call $E$ globally pluripolar if one function $u$ plurisubharmonic on all of $\C^n$, not identically $-\infty$, has $E \subseteq \set{u = -\infty}$.
By [[Josefson's theorem|V6XSDT5C21]] the two notions agree.
Example: $E = \set{z \in \C^2 : z_1 = 0}$ is pluripolar; take $U = \C^2$ and $u(z) = \log\abs{z_1}$, which is plurisubharmonic and equals $-\infty$ exactly on $E$.
Non-example: $\R^n \subset \C^n$ is not pluripolar.
For $n = 1$: if $u$ is subharmonic near a point of $\R$ and $u = -\infty$ on an interval, then $u \equiv -\infty$ near that point, since intervals are not [[polar|C95QJ7YH5T]].
Applying this on complex lines parallel to the coordinate axes, one coordinate at a time, gives the general case.
For $n = 1$, pluripolar sets are exactly polar sets.
