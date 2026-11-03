---
tag: 4THYQKV5PJ
kind: definition
name: Nilradical of a Lie algebra
msc: [17B05, 17B30]
defines: ET8Y1AR5YX
uses: [5JJYBJ6A8K, JWMTXQ8A3A, MEJ9PGMJ9H, 33MD21KMNP, G8FEGYDSNE, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Nilradical_of_a_Lie_algebra
---

## Definition

Let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
The *nilradical* of $\mathfrak g$, written $\operatorname{nil}(\mathfrak g)$, is the sum of all [[nilpotent|MEJ9PGMJ9H]] [[ideals|JWMTXQ8A3A]] of $\mathfrak g$.
It is itself a nilpotent ideal, so it is the unique largest nilpotent ideal of $\mathfrak g$.

## Remarks

The sum of two nilpotent ideals $\mathfrak a$ and $\mathfrak b$ is nilpotent: if $\mathfrak a^{m+1} = 0$ and $\mathfrak b^{n+1} = 0$ for the lower central series, then every bracket of $m + n + 1$ elements of $\mathfrak a + \mathfrak b$ is $0$.
Since nilpotent Lie algebras are solvable, $\operatorname{nil}(\mathfrak g) \subseteq \operatorname{rad}(\mathfrak g)$, the [[radical|33MD21KMNP]].
If $k$ has [[characteristic|1ZB13N78XW]] $0$, then $[\mathfrak g, \operatorname{rad}(\mathfrak g)] \subseteq \operatorname{nil}(\mathfrak g)$.

Example: in the two-dimensional Lie algebra with basis $x, y$ and $[x, y] = y$, the line $ky$ is an abelian ideal.
The whole algebra is not nilpotent, and it is the only ideal of dimension $2$, so $\operatorname{nil}(\mathfrak g) = ky$, while $\operatorname{rad}(\mathfrak g) = \mathfrak g$.

Example: for $\mathfrak g = \mathfrak{gl}_n(k)$, the [[general linear Lie algebra|G8FEGYDSNE]], with $k$ of characteristic $0$ and $n \ge 2$, the nilradical equals the radical, the scalar matrices $kI$.

Non-example: in the same two-dimensional algebra, the whole algebra $\mathfrak g$ is a solvable ideal containing $ky$, but it is not nilpotent, so it is not the nilradical.
