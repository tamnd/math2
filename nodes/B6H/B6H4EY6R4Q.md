---
tag: B6H4EY6R4Q
kind: definition
name: Topological homogeneity
msc: [54H15, 22F30]
defines: A34VR4FMRE
uses: [0CQHFPGJ45, 0QT00PB5G2, 92700QAB5Y]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_space
---

## Definition

A [[topological space|0CQHFPGJ45]] $X$ is *homogeneous* if for all $x, y \in X$ there is a [[homeomorphism|0QT00PB5G2]] $h \colon X \to X$ with $h(x) = y$.

## Remarks

Example: every [[topological group|92700QAB5Y]] $G$ is homogeneous.
For $x, y \in G$, left translation by $y x^{-1}$ is a homeomorphism with inverse the translation by $x y^{-1}$, and it sends $x$ to $y$.
Non-example: the closed interval $[0, 1]$.
A homeomorphism $h$ with $h(0) = 1/2$ would restrict to a homeomorphism from $(0, 1]$, which is connected, onto $[0, 1] \setminus \set{1/2}$, which is not connected.
In the language of group actions, $X$ is homogeneous when its homeomorphism group acts transitively on $X$.
