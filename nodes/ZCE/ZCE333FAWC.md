---
tag: ZCE333FAWC
kind: definition
name: Regular cardinal
msc: ["03E10", "03E04"]
defines: 13ZV2F8JAR
uses: [0QKPNZKNEA, NTE5C260S1]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_cardinal
---

## Definition

Let $\kappa$ be an infinite [[cardinal|0QKPNZKNEA]], identified with the least ordinal of its cardinality.
The cardinal $\kappa$ is regular if its [[cofinality|NTE5C260S1]] is $\kappa$, that is, $\operatorname{cf}(\kappa) = \kappa$.
It is singular if $\operatorname{cf}(\kappa) < \kappa$.

## Remarks

Example: in ZFC, every infinite successor cardinal $\kappa^+$ is regular.
Check: if $\kappa^+$ were the union of fewer than $\kappa^+$ sets each of size less than $\kappa^+$, it would have size at most $\kappa \cdot \kappa = \kappa$, using the axiom of choice.
Non-example: $\aleph_\omega$ is singular, since $\set{\aleph_n : n < \omega}$ is a cofinal subset of order type $\omega$.
Equivalently, in ZFC, $\kappa$ is regular if and only if it is not the union of fewer than $\kappa$ sets each of cardinality less than $\kappa$.
$\aleph_0$ is regular, and a limit cardinal $\aleph_\lambda$ with $\lambda$ a limit ordinal has cofinality $\operatorname{cf}(\lambda)$.
A regular uncountable limit cardinal is called weakly inaccessible; its existence cannot be proved in ZFC, if ZFC is consistent.
