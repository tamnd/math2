---
tag: 0EPD87YVG8
kind: statement
role: proposition
name: Continuous image of a connected set is connected
msc: [54D05]
uses: [0R37DFJKFW, 0SY9ECQ19Q, 0FGCFY1AZX]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Theorems
---

## Statement

Let $X$ and $Y$ be [[topological spaces|0CNQXVBHCX]], let $f \colon X \to Y$ be [[continuous|0SY9ECQ19Q]] and let $S \subseteq X$ be [[connected|0R37DFJKFW]].
Then $f(S)$ is connected.

## Remarks

Proof: if open sets $U$ and $V$ split $f(S)$, then the [[preimages|0FGCFY1AZX]] $f^{-1}(U)$ and $f^{-1}(V)$ are open and split $S$.
Thus connectedness is a [[topological property|02SMVGC690]].
For $Y = \mathbb{R}$, this gives the [[intermediate value theorem|098C0KZZAP]].
For example, the circle is connected, because it is the image of $[0, 1]$ under $t \mapsto (\cos 2\pi t, \sin 2\pi t)$.

## Explanations

### L1 human

A continuous map cannot break a space that is in one piece into separate pieces.
