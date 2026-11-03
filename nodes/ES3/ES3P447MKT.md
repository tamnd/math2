---
tag: ES3P447MKT
kind: definition
name: Mass in general relativity
msc: ["83C40", "83C30", "83C05"]
defines: DK861STN5E
uses: [3HTF65XMF7, XQNV97Z79Q, XYFKKJM9FD, 7V112F6KVB]
sources:
  - url: https://en.wikipedia.org/wiki/Mass_in_general_relativity
---

## Definition

Let $(M, g)$ be a solution of the Einstein equations that is [[asymptotically flat|3HTF65XMF7]].
The *mass* of $(M, g)$ is a quantity defined from the asymptotic behaviour of $g$, by one of the following definitions.

1. The [[ADM mass|XQNV97Z79Q]], defined by a surface integral at spatial infinity on an asymptotically flat initial data set.
2. The [[Bondi mass|XYFKKJM9FD]], a function of retarded time defined by an integral over a cut of future null infinity.
3. The [[Komar mass|7V112F6KVB]], defined when $g$ is stationary, by a surface integral of the derivative of the timelike Killing field.

## Remarks

The ADM mass is constant in time, while the Bondi mass does not increase, and it decreases when gravitational waves carry energy away.
For a stationary asymptotically flat vacuum spacetime outside a compact region, the Komar mass and the ADM mass agree.
Example: for the Schwarzschild metric $g = -(1 - 2M/r) dt^2 + (1 - 2M/r)^{-1} dr^2 + r^2 d\Omega^2$, all three definitions give $M$.
Non-example: de Sitter space is not asymptotically flat, so none of these definitions applies to it.
Several other definitions are quasi-local: they assign a mass to a closed 2-surface, such as the Hawking mass and the Brown–York mass.

## Explanations

### L1 human

The mass of a spacetime is read off from how quickly its metric approaches the flat metric far away.
