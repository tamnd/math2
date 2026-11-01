---
tag: W6E6M1QYH5
kind: definition
name: Prüfer domain
msc: [13F05]
defines: 2RDAA4PCK8
uses: [09S3PFBEPM, 0VF11ZTTMD, 0MYSA6MYNA, E190TAV2S6]
sources:
  - url: https://en.wikipedia.org/wiki/Pr%C3%BCfer_domain
---

## Definition

Let $R$ be an [[integral domain|09S3PFBEPM]] with [[field of fractions|0VF11ZTTMD]] $K$.
$R$ is a *Prüfer domain* if every nonzero finitely generated [[ideal|0MYSA6MYNA]] $I$ of $R$ is [[invertible|E190TAV2S6]].
That is, there is an $R$-submodule $J$ of $K$ with $IJ = R$.

## Remarks

Equivalent form: for every prime ideal $P$ of $R$, the localization $R_P$ is a valuation ring, that is, for every nonzero $x \in K$, $x \in R_P$ or $x^{-1} \in R_P$.
Example: every [[principal ideal domain|0RZYDVZ475]] is Prüfer; a nonzero ideal $aR$ has inverse $a^{-1}R$.
Non-example: in $\Z[x]$, the ideal $I = (2, x)$ is not invertible; the only $y \in \Q(x)$ with $yI \subseteq \Z[x]$ are the elements of $\Z[x]$, so any $J$ with $IJ \subseteq \Z[x]$ satisfies $IJ \subseteq I \ne \Z[x]$.
A Noetherian Prüfer domain is a Dedekind domain; a Prüfer domain that is a [[GCD domain|ACDEK1GD9G]] is a [[Bézout domain|HGEX40P0Z0]].
Prüfer domains are integrally closed.
