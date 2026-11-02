---
tag: Z23FCT4WTZ
kind: definition
name: CR function
msc: [32V10, 32V05]
defines: JFKYYK2CEB
uses: [ZC78JKZX9S]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Definition

Let $(M, L)$ be a [[CR manifold|ZC78JKZX9S]], with $L \subseteq TM \otimes \C$ its CR structure and $\overline{L}$ the conjugate subbundle.
A function $f \colon M \to \C$ of class $C^1$ is a *CR function* if $X f = 0$ for every smooth section $X$ of $\overline{L}$.

## Remarks

The bundle $L$ plays the role of the holomorphic tangent vectors $\partial / \partial z_j$, so $\overline{L}$ plays the role of the $\partial / \partial \bar z_j$, and the condition says $\bar\partial_b f = 0$.
One also defines CR distributions by the same equations in the sense of distributions.

Example: let $M \subset \C^n$ be a real hypersurface with its induced CR structure, and let $F$ be holomorphic on a neighbourhood of $M$.
A section $X$ of $\overline{L}$ is a combination of the $\partial / \partial \bar z_j$ that is tangent to $M$.
So $X (F|_M) = (X F)|_M = 0$, and $F|_M$ is a CR function.

Non-example: on the unit sphere $S^3 \subset \C^2$, the bundle $\overline{L}$ is spanned by $\overline{Z} = z_2 \, \partial / \partial \bar z_1 - z_1 \, \partial / \partial \bar z_2$.
It is tangent to $S^3$, since $\overline{Z}(\abs{z_1}^2 + \abs{z_2}^2) = z_2 z_1 - z_1 z_2 = 0$.
For $f = \bar z_1$ one finds $\overline{Z} f = z_2$, which is not identically zero on $S^3$, so $\bar z_1$ is not a CR function.
