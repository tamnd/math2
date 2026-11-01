---
tag: MRRQEEP3T8
kind: definition
name: Iwasawa theory
msc: [11R23]
defines: Y2SPPSQ5D4
uses: [MWBDFS2KJ5, 0QMZAQ6QQ4, 0XTY86BZKY, V6TJAFZ4MD, WQ46BD3ARY, NN77VYSGXR]
sources:
  - url: https://en.wikipedia.org/wiki/Iwasawa_theory
---

## Definition

Let $p$ be a prime number, and let $K$ be an [[algebraic number field|MWBDFS2KJ5]].
Let $\Z_p$ be the [[p-adic integers|V6TJAFZ4MD]] with their additive group and $p$-adic topology.
A *$\Z_p$-extension* of $K$ is a [[Galois extension|0QMZAQ6QQ4]] $K_\infty/K$ inside a fixed algebraic closure such that the following holds.
Its [[Galois group|0XTY86BZKY]], with the Krull topology, is isomorphic to $\Z_p$ as a topological group.
For $n \ge 0$, the $n$-th *layer* $K_n$ is the fixed field of the closed subgroup corresponding to $p^n \Z_p$.
Then $\Gal(K_n/K) \cong \Z/p^n\Z$ and $K_\infty = \bigcup_n K_n$.
The *Iwasawa algebra* is $\Lambda = \Z_p[\![T]\!]$, the ring of formal power series over $\Z_p$.
Fix a topological generator $\gamma$ of $\Gal(K_\infty/K)$.
Then $\Lambda$ acts on each compact $\Z_p$-module with a continuous action of $\Gal(K_\infty/K)$, with $T$ acting as $\gamma - 1$.
Iwasawa theory is the study of such $\Lambda$-modules attached to $\Z_p$-extensions.
Let $A_n$ be the $p$-part of the [[ideal class group|WQ46BD3ARY]] of $K_n$.
The main such module is $X = \varprojlim_n A_n$, the inverse limit under the norm maps.

## Remarks

Iwasawa's theorem: there are integers $\lambda \ge 0$, $\mu \ge 0$ and $\nu$ such that $\abs{A_n} = p^{\mu p^n + \lambda n + \nu}$ for all sufficiently large $n$.
For a finite abelian extension $K$ of $\Q$ and its cyclotomic $\Z_p$-extension, Ferrero and Washington proved $\mu = 0$.

Example: let $p$ be odd.
The Galois group of $\bigcup_n \Q(\zeta_{p^n})$ over $\Q$ is $\Z_p^\times \cong \mu_{p-1} \times (1 + p\Z_p)$.
As a topological group, $1 + p\Z_p$ is isomorphic to $\Z_p$.
So the fixed field of the factor $\mu_{p-1}$ is a $\Z_p$-extension of $\Q$, the *cyclotomic* $\Z_p$-extension.
Its layer $K_1$ is the unique subfield of degree $p$ of the [[cyclotomic field|NN77VYSGXR]] $\Q(\zeta_{p^2})$.

Non-example: for $p$ odd, $\bigcup_n \Q(\zeta_{p^n})$ itself is not a $\Z_p$-extension of $\Q$.
Its Galois group $\Z_p^\times$ has the nontrivial finite subgroup $\mu_{p-1}$, while $\Z_p$ has no nonzero element of finite order.
It is, however, a $\Z_p$-extension of $\Q(\zeta_p)$.
