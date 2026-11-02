---
tag: YJ2VVJZBX4
kind: definition
name: Symmetric decreasing rearrangement
msc: [26D15, "46E30", 35B06]
defines: 2GRPCP5XK9
uses: [2Z2QVWZ262, YYNCJSR0PJ, BWS042NC2P]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_decreasing_rearrangement
---

## Definition

Let $\abs{\cdot}$ denote [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$.
For a measurable set $A \subseteq \R^n$ of finite measure, its *symmetric rearrangement* $A^*$ is the open ball centred at $0$ with $\abs{A^*} = \abs{A}$, and $A^* = \varnothing$ if $\abs{A} = 0$.
Let $f \colon \R^n \to \C$ be a [[measurable function|YYNCJSR0PJ]] that vanishes at infinity, that is, $\abs{\set{x : \abs{f(x)} > t}} < \infty$ for every $t > 0$.
The *symmetric decreasing rearrangement* of $f$ is the function $f^* \colon \R^n \to [0, \infty]$ given by
$$f^*(x) = \int_0^\infty \mathbf{1}_{\set{\abs{f} > t}^*}(x) \, dt,$$
where $\mathbf{1}_B$ is the indicator function of $B$.

## Remarks

The function $f^*$ is nonnegative, radial, non-increasing in $\abs{x}$ and lower semicontinuous.
For every $t > 0$, $\set{f^* > t} = \set{\abs{f} > t}^*$, so $f^*$ and $\abs{f}$ have the same distribution function, and $\norm{f^*}_p = \norm{f}_p$ for $1 \le p \le \infty$.
The Pólya–Szegő inequality states that $\norm{\nabla f^*}_2 \le \norm{\nabla f}_2$ for $f \in H^1(\R^n)$.
The Riesz rearrangement inequality states that $\iint f(x) g(x - y) h(y) \, dx \, dy \le \iint f^*(x) g^*(x - y) h^*(y) \, dx \, dy$ for nonnegative $f, g, h$.

Example: in $\R$, let $f = \mathbf{1}_{[1, 3]}$.
For $0 < t < 1$ the set $\set{f > t}$ is $[1, 3]$, of length $2$, so its rearrangement is $(-1, 1)$; for $t \ge 1$ it is empty.
Hence $f^* = \mathbf{1}_{(-1, 1)}$.

Non-example: the constant function $f = 1$ on $\R^n$ does not vanish at infinity, since $\set{f > 1/2}$ has infinite measure, so $f^*$ is not defined.

The one-variable [[decreasing rearrangement|BWS042NC2P]] $f^\sharp$ on $[0, \infty)$ is related by $f^*(x) = f^\sharp(\omega_n \abs{x}^n)$, where $\omega_n$ is the volume of the unit ball, up to values on a null set.
