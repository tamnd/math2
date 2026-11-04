---
about:
- FF2P7ER3QT
kind: statement
msc:
- 32U05
name: Plurisubharmonic functions are preserved by holomorphic pullback
role: theorem
sources:
- url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L7647
  locator: scv.tex:7647
tag: SJJ5PPDAWH
uses:
- FF2P7ER3QT
- 507C34W0ZT
---

## Statement

Let $U \subset \C^n$ and $V \subset \C^m$ be open sets. Let $g \colon U \to V$ be a [[holomorphic|507C34W0ZT]] map. Let $f \colon V \to \R \cup \{-\infty\}$ be a [[plurisubharmonic function|FF2P7ER3QT]].

Then the composition $f \circ g \colon U \to \R \cup \{-\infty\}$ is plurisubharmonic on $U$.

## Remarks

The class of plurisubharmonic functions is stable under pullback by holomorphic maps, even when the dimensions $n$ and $m$ differ.

For example, if $f(w) = \log\abs{w_1}$ on $\C^m$ and $g$ is holomorphic, then $\log\abs{g_1}$ is plurisubharmonic on $U$.
