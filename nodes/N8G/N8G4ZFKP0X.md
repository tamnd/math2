---
tag: N8G4ZFKP0X
kind: definition
name: Depth
msc: [13C15, 13D07]
defines: M2RADBFW99
uses: [0670T59HGE, 05QY1VEBYD, 096Z9MP2ME, 69R5R2FCS5, MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Depth_(ring_theory)
---

## Definition

Let $R$ be a commutative [[Noetherian ring|0670T59HGE]], let $I$ be an [[ideal|096Z9MP2ME]] of $R$, and let $M$ be a [[finitely generated|05QY1VEBYD]] $R$-module with $IM \ne M$.
The *$I$-depth* of $M$, written $\operatorname{depth}_I M$ or $\operatorname{grade}(I, M)$, is the length of a maximal [[$M$-regular sequence|69R5R2FCS5]] whose elements lie in $I$.
If $(R, \mathfrak{m})$ is a [[local ring|MZ02BKPHJA]], the *depth* of $M$ is $\operatorname{depth} M = \operatorname{depth}_{\mathfrak{m}} M$.

## Remarks

The definition makes sense because all maximal $M$-regular sequences in $I$ have the same length, a theorem of Rees.
That length is also $\min \set{i : \operatorname{Ext}^i_R(R/I, M) \ne 0}$.
If $IM = M$, one sets $\operatorname{depth}_I M = \infty$.
Example: for $R = K[x_1, \ldots, x_n]$ localized at $(x_1, \ldots, x_n)$, one has $\operatorname{depth} R = n$, with the maximal regular sequence $x_1, \ldots, x_n$.
Example: for $R = K[x,y]/(x^2, xy)$ localized at $\mathfrak{m} = (x, y)$, one has $\operatorname{depth} R = 0$, since $x \ne 0$ and $x \mathfrak{m} = 0$, so no element of $\mathfrak{m}$ is a non-zero-divisor.
For a nonzero finitely generated module over a Noetherian local ring, $\operatorname{depth} M \le \dim M$.
