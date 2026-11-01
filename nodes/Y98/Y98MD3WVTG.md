---
tag: Y98MD3WVTG
kind: definition
name: Germ
msc: [54A20, 58A99]
defines: VZXF7RNFKS
uses: [0CQHFPGJ45, 0ZCY0Z80B6, 0G8VEZ3WTK, 0W95W33CMP]
sources:
  - url: https://en.wikipedia.org/wiki/Germ_(mathematics)
---

## Definition

Let $X$ and $Y$ be [[topological spaces|0CQHFPGJ45]] and let $x \in X$.
Consider pairs $(U, f)$, where $U$ is an open [[neighbourhood|0ZCY0Z80B6]] of $x$ and $f \colon U \to Y$ is a map.
Two such pairs $(U, f)$ and $(V, g)$ are *equivalent at $x$* if there is an open neighbourhood $W \subseteq U \cap V$ of $x$ with $f(w) = g(w)$ for all $w \in W$.
This is an [[equivalence relation|0G8VEZ3WTK]].
The *germ* of $(U, f)$ at $x$ is its [[equivalence class|0W95W33CMP]].

## Remarks

One often restricts to continuous, smooth or holomorphic maps, and writes $[f]_x$ for the germ.
The value $f(x)$ depends only on the germ, and so do derivatives of all orders at $x$ when $f$ is smooth.
More generally, let $\mathcal{F}$ be a filter on a set $S$.
Two maps on $S$ have the same germ along $\mathcal{F}$ if they agree on some member of $\mathcal{F}$.
The case above uses the neighbourhood filter of $x$.

Example: on $\R$, the maps $f(t) = t$ and $g(t) = \abs{t}$ have the same germ at $1$, since they agree on $W = (0, 2)$.

Non-example: on $\R$, let $f = 0$ and let $g(t) = e^{-1/t^2}$ for $t \ne 0$, with $g(0) = 0$.
Both are smooth, and all their derivatives agree at $0$.
Yet $g(t) \ne 0$ for every $t \ne 0$, so they agree on no neighbourhood of $0$, and their germs at $0$ differ.
