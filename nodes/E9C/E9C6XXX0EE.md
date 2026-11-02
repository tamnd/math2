---
tag: E9C6XXX0EE
kind: definition
name: Standard part function
msc: ["26E35", "03H05"]
defines: 1ZBY4W4E81
uses: [421QMTFG9T, 08J2M1JYAG, 0R3H5PANRQ, 0VTH8KPCG2]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_part_function
---

## Definition

Let ${}^*\R$ be a field of [[hyperreal numbers|421QMTFG9T]] containing the [[real numbers|08J2M1JYAG]].
A hyperreal $x$ is *finite* if $\abs{x} < r$ for some real $r$.
For each finite $x$ there is exactly one real number $r$ such that $x - r$ is infinitesimal.
This $r$ is the *standard part* of $x$, written $\operatorname{st}(x)$.
The *standard part function* is the map $\operatorname{st}$ from the set of finite hyperreals to $\R$.

## Remarks

Existence: $\operatorname{st}(x)$ is the [[supremum|0R3H5PANRQ]] of the set $\set{q \in \R : q < x}$, which is nonempty and bounded above when $x$ is finite.
Uniqueness: if $x - r$ and $x - r'$ are infinitesimal for reals $r$ and $r'$, then $r - r'$ is a real infinitesimal, so $r = r'$.

Example: for a positive infinitesimal $\varepsilon$, $\operatorname{st}(3 + \varepsilon) = 3$, since $(3 + \varepsilon) - 3 = \varepsilon$ is infinitesimal.

Non-example: $H = 1/\varepsilon$ is not finite, and for every real $r$ the difference $H - r$ is larger than $1$, so it is not infinitesimal and $H$ has no standard part.

The finite hyperreals form a subring of ${}^*\R$, and $\operatorname{st}$ is a [[ring homomorphism|0VTH8KPCG2]] onto $\R$ whose kernel is the set of infinitesimals.
It is also monotone: $x \le y$ implies $\operatorname{st}(x) \le \operatorname{st}(y)$.
