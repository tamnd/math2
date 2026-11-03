---
tag: BG5DE2ZHQ6
kind: definition
name: Weyl chamber
msc: ["17B22", "20F55"]
defines: 1EYQZNA69W
uses: [AVVV93CASN, CSBM217V1N, YT1ZJ2S4EE, 0JG9W3KA6B]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl_group
---

## Definition

Let $\Phi$ be a [[root system|AVVV93CASN]] in a Euclidean space $E$ with inner product $(\cdot, \cdot)$.
For $\alpha \in \Phi$, let $H_\alpha = \set{x \in E : (x, \alpha) = 0}$.
A *Weyl chamber* of $\Phi$ is a [[connected component|0JG9W3KA6B]] of the open set $E \setminus \bigcup_{\alpha \in \Phi} H_\alpha$.

## Remarks

Each chamber is an open convex cone: for any $\gamma$ in the chamber $C$, it equals $\set{x \in E : (x, \alpha) (\gamma, \alpha) > 0 \text{ for all } \alpha \in \Phi}$.
Example: for $A_1 = \set{\pm \alpha}$ in $E = \R$, the only hyperplane is $H_\alpha = \set{0}$, and the chambers are $(0, \infty)$ and $(-\infty, 0)$.
Non-example: the closed half-line $[0, \infty)$ is not a chamber, since it meets $H_\alpha$.
For a base $\Delta$ of [[simple roots|CSBM217V1N]], the set $\set{x \in E : (x, \alpha) > 0 \text{ for all } \alpha \in \Delta}$ is a chamber, the *fundamental chamber* of $\Delta$; this gives a bijection between bases and chambers.
The [[Weyl group|YT1ZJ2S4EE]] acts simply transitively on the set of chambers.

## Explanations

### L1 human

The mirrors orthogonal to the roots cut space into open pieces, and the Weyl chambers are these pieces.
Choosing a chamber is the same as choosing a set of simple roots.
