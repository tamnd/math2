---
tag: KRNBRFSKVE
kind: definition
name: Dual code
msc: [94B05]
defines: JA3DP8NM0A
uses: [E85KREWV60, 0S52TNNTH9, 8TXKFC5PRD, Y4JB44WWFG]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_code
---

## Definition

Let $C$ be a [[linear code|E85KREWV60]] of length $n$ over the finite field $\F_q$.
For $x, y \in \F_q^n$ let $x \cdot y = \sum_{i=1}^n x_i y_i$ be the [[dot product|0S52TNNTH9]].
The *dual code* of $C$ is
$$C^\perp = \set{x \in \F_q^n : x \cdot c = 0 \text{ for all } c \in C}.$$
The code $C$ is *self-orthogonal* if $C \subseteq C^\perp$ and *self-dual* if $C = C^\perp$.

## Remarks

$C^\perp$ is a linear code with $\dim C^\perp = n - \dim C$, and $(C^\perp)^\perp = C$.
A [[generator matrix|8TXKFC5PRD]] of $C$ is a [[parity-check matrix|Y4JB44WWFG]] of $C^\perp$, and a parity-check matrix of $C$ is a generator matrix of $C^\perp$.
Example: over $\F_2$, $\set{000, 111}^\perp = \set{000, 011, 101, 110}$, since $x \cdot 111 = x_1 + x_2 + x_3$ is zero exactly for the words of even weight.
Non-example: $\set{000, 111}$ is not self-orthogonal, since $111 \cdot 111 = 1 \ne 0$ in $\F_2$.
Unlike the orthogonal complement in $\R^n$, $C \cap C^\perp$ can be nonzero: the binary code $\set{00, 11}$ is self-dual, since $11 \cdot 11 = 0$ and both codes have dimension $1$.
