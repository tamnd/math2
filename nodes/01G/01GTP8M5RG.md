---
tag: 01GTP8M5RG
kind: definition
name: Order of cardinals
msc: ["03E10"]
defines: 022RSX714V
uses: [0JTGRV4WT4, 0PVG1CRAJN]
sources:
  - url: https://en.wikipedia.org/wiki/Cardinal_number
    locator: Cardinal comparison
---

## Definition

Let $A$ and $B$ be [[sets|0SJ3RX9TXA]].
The cardinality of $A$ is at most the cardinality of $B$, written $|A| \le |B|$, when there is an [[injective function|0PVG1CRAJN]] $f \colon A \to B$.
Write $|A| < |B|$ when $|A| \le |B|$ and $|A| \neq |B|$.

## Remarks

The relation does not depend on the choice of $A$ and $B$ in their classes of [[equinumerous|08EJHHMB5R]] sets.
It is reflexive and transitive. It is antisymmetric by the [[Schröder–Bernstein theorem|0A9V6RKQG6]].
With the axiom of choice, any two cardinals are comparable. See [[comparability of cardinals|0YBHSJMN3J]].

## Explanations

### L1 human

$|A| \le |B|$ means that $A$ fits into $B$ without two elements landing in the same place.
For example, $|\mathbb{N}| \le |\mathbb{R}|$, because $\mathbb{N}$ is a subset of $\mathbb{R}$.
