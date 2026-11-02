---
tag: N1H5NV5X0Z
kind: definition
name: Uniserial module
msc: [16D70, 16P70]
defines: Z1045A0V29
uses: [0NZ8JA25WK, 05WDSN597C, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Serial_module
---

## Definition

Let $R$ be a ring and let $M$ be a right $R$-[[module|0NZ8JA25WK]].
The module $M$ is *uniserial* if its set of [[submodules|05WDSN597C]] is [[totally ordered|0FRXBVVR03]] by inclusion.
That is, for any two submodules $N$ and $L$ of $M$, either $N \subseteq L$ or $L \subseteq N$.
Left uniserial modules are defined in the same way.

## Remarks

Example: for a prime $p$ and $n \ge 1$, the $\Z$-module $\Z/p^n\Z$ is uniserial.
Its submodules are the subgroups $p^i\Z/p^n\Z$ for $0 \le i \le n$, and $p^i\Z/p^n\Z \supseteq p^j\Z/p^n\Z$ when $i \le j$.
In the same way, $k[x]/(x^n)$ is uniserial as a module over itself, for a field $k$.

Non-example: the $\Z$-module $\Z$ is not uniserial.
Its submodules $2\Z$ and $3\Z$ are not comparable, since $2 \notin 3\Z$ and $3 \notin 2\Z$.

A nonzero uniserial module is indecomposable, since two nonzero submodules always meet in the smaller one, which is nonzero.
A uniserial module of finite length has exactly one composition series.
