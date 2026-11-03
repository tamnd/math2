---
tag: AMQDSPVZ5K
kind: definition
name: Simple Lie algebra
msc: [17B20]
defines: XDAXWHBNSZ
uses: [5JJYBJ6A8K, JWMTXQ8A3A, N43CM5H99K, 1ZAT1Z967A, G8FEGYDSNE]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_Lie_algebra
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
The Lie algebra $\mathfrak g$ is *simple* if:

1. $\mathfrak g$ is not [[abelian|N43CM5H99K]];
2. the only [[ideals|JWMTXQ8A3A]] of $\mathfrak g$ are $0$ and $\mathfrak g$.

## Remarks

Example: the [[special linear Lie algebra|1ZAT1Z967A]] $\mathfrak{sl}_2(k)$ with $\operatorname{char} k \ne 2$, basis $e, h, f$ and $[h, e] = 2e$, $[h, f] = -2f$, $[e, f] = h$.
It is not abelian.
Let $I$ be a nonzero ideal and $u = ae + bh + cf \in I$ nonzero.
Then $[e, [e, u]] = -2c\, e$ and $[f, [f, u]] = -2a\, f$ lie in $I$; if $a \ne 0$ or $c \ne 0$, then $I$ contains $e$ or $f$, and bracketing with $f$ or $e$ gives $h$ and then all of $\mathfrak{sl}_2(k)$.
If $a = c = 0$, then $h \in I$, and $e = \tfrac12 [h, e]$ and $f = -\tfrac12 [h, f]$ lie in $I$.
So $I = \mathfrak{sl}_2(k)$.

Non-example: the [[general linear Lie algebra|G8FEGYDSNE]] $\mathfrak{gl}_n(k)$ with $n \ge 2$ is not abelian, but it fails clause 2: the scalar matrices form a nonzero proper ideal.

Clause 1 excludes the one-dimensional Lie algebra, which has no ideals other than $0$ and itself.
For a nonzero $\mathfrak g$, clause 1 can be replaced by $[\mathfrak g, \mathfrak g] \ne 0$, and then clause 2 forces $[\mathfrak g, \mathfrak g] = \mathfrak g$.
