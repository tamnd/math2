---
tag: HE4YBMV76N
kind: definition
name: Finitely generated projective module
msc: [13C10, 16D40]
defines: HQA9YHDSH5
uses: [0B1261B5ED, 0NZ8JA25WK, 05QY1VEBYD, BFFA03GE3V, 0DZ9DKAKZR]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_module
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $P$ be a left [[$R$-module|0NZ8JA25WK]].
The module $P$ is a *finitely generated projective module* if it is [[finitely generated|05QY1VEBYD]] and [[projective|BFFA03GE3V]].

## Remarks

The following are equivalent for a left $R$-module $P$:

1. $P$ is finitely generated and projective.
2. There are an integer $n \ge 0$ and a left $R$-module $Q$ with $P \oplus Q \cong R^n$.
3. $P \cong R^n e$ for some $n \ge 0$ and some idempotent matrix $e \in M_n(R)$, where $R^n$ is the module of row vectors.

From 1 to 2: a surjection $R^n \to P$ splits because $P$ is projective.
From 2 to 3: take $e$ to be the projection of $R^n$ onto $P$ along $Q$.

Example: let $R = \Z/6\Z$ and $P = \Z/2\Z$, an $R$-module through $R \to \Z/2\Z$.
By the Chinese remainder theorem $R \cong \Z/2\Z \oplus \Z/3\Z$ as $R$-modules, so $P$ is a direct summand of $R^1$ and is finitely generated projective.
It is not [[free|0DZ9DKAKZR]], since it has $2$ elements and a free $R$-module of finite rank $m$ has $6^m$ elements.

Non-example: the module $\Z/2\Z$ over $R = \Z$ is finitely generated but not projective.
It is not a direct summand of any $\Z^n$, because $\Z^n$ has no nonzero element of finite order.
The free module $R^{(\N)}$ with a basis indexed by $\N$ is projective but not finitely generated when $R \neq 0$.
