---
tag: GAW3VCFYZV
kind: definition
name: Germ of a smooth function
msc: [58A05, 58K40, "26E10"]
defines: 7SWSRGDT4A
uses: [VZXF7RNFKS, F45VQ47GPV, 0V33BNKZ9S, 0ZCY0Z80B6, MZ02BKPHJA, 0PV74TR5FP]
sources:
  - url: https://en.wikipedia.org/wiki/Germ_(mathematics)
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $p \in M$.
Consider pairs $(U, f)$, where $U$ is an open [[neighbourhood|0ZCY0Z80B6]] of $p$ and $f \colon U \to \R$ is a [[smooth function|0V33BNKZ9S]].
Two pairs $(U, f)$ and $(V, g)$ are equivalent if there is an open neighbourhood $W \subseteq U \cap V$ of $p$ with $f = g$ on $W$.
The *germ at $p$* of $(U, f)$ is its equivalence class, written $[f]_p$.
This is the [[germ|VZXF7RNFKS]] of $f$ at $p$ in the general sense, for smooth real functions.

The set of germs at $p$ is written $C^\infty_p(M)$ or $\mathcal{E}_p$.
Sums and products of germs are defined by $[f]_p + [g]_p = [f + g]_p$ and $[f]_p [g]_p = [fg]_p$, with $f + g$ and $fg$ taken on $U \cap V$.

## Remarks

With these operations $\mathcal{E}_p$ is a commutative $\R$-algebra.
It is a [[local ring|MZ02BKPHJA]]: its unique [[maximal ideal|0PV74TR5FP]] $\mathfrak{m}_p$ consists of the germs with $f(p) = 0$.
Indeed, if $f(p) \ne 0$, then $f \ne 0$ on a neighbourhood of $p$ and $[1/f]_p$ is an inverse of $[f]_p$.
The value $f(p)$ and all partial derivatives of $f$ at $p$ in a chart depend only on the germ.

Example: on $M = \R$, let $f(x) = x^2$ on $\R$ and $g(x) = x^2$ on $(-1, 1)$.
They agree on $W = (-1, 1)$, so $[f]_0 = [g]_0$.

Non-example: let $f = 0$ on $\R$, and let $h(x) = e^{-1/x^2}$ for $x \ne 0$ with $h(0) = 0$.
All derivatives of $f$ and $h$ at $0$ agree, but $h(x) \ne 0$ for every $x \ne 0$.
So $f$ and $h$ agree on no neighbourhood of $0$, and $[f]_0 \ne [h]_0$.
A germ is thus finer information than the Taylor series at $p$.
