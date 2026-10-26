---
tag: ~ac796cdf
kind: definition
name: Order of cardinals
msc: ["03E10"]
defines: ~7628c77c
uses: [~ec7b0a04, ~3e705960]
sources:
  - url: https://en.wikipedia.org/wiki/Cardinal_number
    locator: Cardinal comparison
---

## Definition

Let $A$ and $B$ be [[sets|~bd92ceee]].
The cardinality of $A$ is at most the cardinality of $B$, written $|A| \le |B|$, when there is an [[injective function|~3e705960]] $f \colon A \to B$.
Write $|A| < |B|$ when $|A| \le |B|$ and $|A| \neq |B|$.

## Remarks

The relation does not depend on the choice of $A$ and $B$ in their classes of [[equinumerous|~cc0844c8]] sets.
It is reflexive and transitive. It is antisymmetric by the [[Schröder–Bernstein theorem|~5f17792e]].
With the axiom of choice, any two cardinals are comparable. See [[comparability of cardinals|~be610989]].

## Explanations

### L1 human

$|A| \le |B|$ means that $A$ fits into $B$ without two elements landing in the same place.
For example, $|\mathbb{N}| \le |\mathbb{R}|$, because $\mathbb{N}$ is a subset of $\mathbb{R}$.
