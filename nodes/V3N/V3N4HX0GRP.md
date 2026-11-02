---
tag: V3N4HX0GRP
kind: definition
name: No small subgroups
msc: ["22A05", "22E05", "22D05"]
defines: HPMAJV2RDY
uses: [92700QAB5Y, 0ZCY0Z80B6, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/No_small_subgroup
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] with identity $e$.
The group $G$ has *no small subgroups* if some [[neighbourhood|0ZCY0Z80B6]] $U$ of $e$ has this property.
The only [[subgroup|0X1JXT47GA]] $H$ of $G$ with $H \subseteq U$ is $H = \set{e}$.

## Remarks

Example: $G = (\R, +)$ with $U = (-1, 1)$.
If $H \subseteq U$ is a subgroup and $x \in H$ with $x \ne 0$, then $nx \in H$ for every integer $n$, and $\abs{nx} \ge 1$ for $n \ge 1/\abs{x}$, so $nx \notin U$.
Hence $H = \set{0}$.
The same argument with the exponential map shows that every [[Lie group|7JBRGCVJRB]] has no small subgroups.

Non-example: the group $\Z_p$ of [[p-adic integers|V6TJAFZ4MD]].
Every neighbourhood of $0$ contains a ball $p^n \Z_p$ for some $n$, and $p^n \Z_p$ is a subgroup different from $\set{0}$.

The property is often abbreviated NSS.
By the Gleason–Yamabe theorem, a locally compact group has no small subgroups if and only if it is a Lie group.
