---
tag: CAWK9DA1PH
kind: definition
name: Cohen–Macaulay ring
msc: [13H10, 13C14]
defines: N1QJQEGBFC
uses: [0670T59HGE, MZ02BKPHJA, M2RADBFW99, MVGBS3J1P7, 00MHHZ9SNE, X6JD4AG973]
sources:
  - url: https://en.wikipedia.org/wiki/Cohen–Macaulay_ring
---

## Definition

Let $(R, \mathfrak{m})$ be a commutative [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]].
Then $R$ is a *Cohen–Macaulay local ring* if $\operatorname{depth} R = \dim R$, where $\operatorname{depth}$ is the [[depth|M2RADBFW99]] with respect to $\mathfrak{m}$ and $\dim$ is the [[Krull dimension|MVGBS3J1P7]].
A commutative Noetherian ring $R$ is a *Cohen–Macaulay ring* if the [[localization|X6JD4AG973]] $R_{\mathfrak{p}}$ is a Cohen–Macaulay local ring for every [[prime ideal|00MHHZ9SNE]] $\mathfrak{p}$ of $R$.

## Remarks

For a Noetherian local ring one always has $\operatorname{depth} R \le \dim R$, so the condition is that the depth is as large as possible.
It suffices to test the localizations at maximal ideals, since localizations of Cohen–Macaulay local rings at primes are Cohen–Macaulay.
Example: every Noetherian local ring of dimension $0$ is Cohen–Macaulay, since then $\operatorname{depth} R = \dim R = 0$.
Example: $K[x_1, \ldots, x_n]$ localized at $(x_1, \ldots, x_n)$ is Cohen–Macaulay, since $x_1, \ldots, x_n$ is a regular sequence of length $n = \dim R$.
Non-example: $R = K[x,y]/(x^2, xy)$ localized at $(x, y)$ has dimension $1$, because its primes are $(x)$ and $(x, y)$, but depth $0$, because $x$ kills the maximal ideal.
For a local ring, Cohen–Macaulay is equivalent to: some (equivalently every) system of parameters is a regular sequence.
A finitely generated module $M \ne 0$ over a Noetherian local ring is a *Cohen–Macaulay module* if $\operatorname{depth} M = \dim M$.
