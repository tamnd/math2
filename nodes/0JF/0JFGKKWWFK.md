---
tag: 0JFGKKWWFK
kind: definition
name: Residue
aliases: [residue-of-a-function]
msc: ["30E20"]
defines: 0PHN07KVQT
uses: [0TYB3HM9KE, 06WHRARZKY, 0T7ABX4CWE]
sources:
  - url: https://en.wikipedia.org/wiki/Residue_(complex_analysis)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Residue_(complex_analysis)
    locator: Generalization to Laurent series
---

## Definition

Let $c \in \mathbb{C}$, let $r > 0$, and let $f$ be [[holomorphic|0DG0Z72CQD]] on the punctured disc $0 < |z - c| < r$, so that $c$ is an [[isolated singularity|0TYB3HM9KE]] of $f$.
Let $f(z) = \sum_{n \in \mathbb{Z}} a_n (z - c)^n$ be the [[Laurent expansion|06WHRARZKY]] of $f$ on this punctured disc.
The residue of $f$ at $c$ is the coefficient
$$\operatorname{Res}(f, c) = a_{-1}.$$

## Remarks

For each $\rho$ with $0 < \rho < r$, $\operatorname{Res}(f, c) = \frac{1}{2 \pi i} \oint_{|z - c| = \rho} f(z) \, dz$. This follows from the coefficient formula for $n = -1$.
The residue is $0$ at a [[removable singularity|0P18JC72RE]]. It can be $0$ at a pole too: $\operatorname{Res}(1/z^2, 0) = 0$.
For example, $\operatorname{Res}(1/z, 0) = 1$ and $\operatorname{Res}(e^{1/z}, 0) = 1$.
Residues at simple poles are easy to compute, see [[residue at a simple pole|01991NCP7H]].

## Explanations

### L1 human

When you integrate a Laurent series term by term around a small circle, every term gives $0$ except the term $a_{-1}/(z - c)$, which gives $2 \pi i a_{-1}$.
So the residue is the one coefficient that the integral remembers.
