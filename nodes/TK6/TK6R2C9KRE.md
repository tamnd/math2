---
tag: TK6R2C9KRE
kind: definition
name: Hyperreal number
msc: ["26E35", "03H05", "03C20"]
defines: 421QMTFG9T
uses: [08J2M1JYAG, J64Y3JC0RE, 0G9EKM0E15, 0G8VEZ3WTK, 0P3VCBDEE2, AX9Q86GB8M, 0XH79S06J3]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperreal_number
---

## Definition

Let $\mathcal{U}$ be a nonprincipal [[ultrafilter|J64Y3JC0RE]] on $\N$.
For [[sequences|0G9EKM0E15]] $a = (a_n)$ and $b = (b_n)$ of [[real numbers|08J2M1JYAG]], put $a \sim b$ if $\set{n \in \N : a_n = b_n} \in \mathcal{U}$.
This is an [[equivalence relation|0G8VEZ3WTK]]; write $[a]$ for the class of $a$.
The set of *hyperreal numbers* is ${}^*\R = \R^{\N} / {\sim}$, with the following structure.

1. $[a] + [b] = [(a_n + b_n)]$ and $[a] \cdot [b] = [(a_n b_n)]$.
2. $[a] < [b]$ if $\set{n \in \N : a_n < b_n} \in \mathcal{U}$.
3. Each real number $r$ is identified with the class of the constant sequence $(r, r, r, \dots)$.

A hyperreal $x$ is *infinitesimal* if $\abs{x} < r$ for every real $r > 0$, and *infinite* if $\abs{x} > r$ for every real $r$.

## Remarks

The operations and the order are well defined, and ${}^*\R$ is an [[ordered field|0P3VCBDEE2]] containing $\R$; it is the [[ultrapower|AX9Q86GB8M]] of $\R$ by $\mathcal{U}$.

Example: $\varepsilon = [(1/(n+1))]$ is a positive infinitesimal.
For a real $r > 0$, the set $\set{n : 1/(n+1) < r}$ is cofinite, and a nonprincipal ultrafilter contains every cofinite set, so $\varepsilon < r$.
Also $\varepsilon > 0$ because every term is positive.
So ${}^*\R$ is not [[Archimedean|0XH79S06J3]].

Non-example: if $\mathcal{U}$ is the principal ultrafilter of the sets containing a fixed $k \in \N$, then $[a] \mapsto a_k$ is an isomorphism onto $\R$, and there are no nonzero infinitesimals.

Under the continuum hypothesis, the ordered field ${}^*\R$ does not depend on the choice of $\mathcal{U}$, up to isomorphism.
