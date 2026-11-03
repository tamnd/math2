---
tag: RCTTQH8RYF
kind: definition
name: Hamming weight
msc: [94B05, 94B25]
defines: K8ZHAQAK2B
uses: [RABRP2KG81, K5287V64FH, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_weight
---

## Definition

Let $\Sigma$ be a finite [[alphabet|RABRP2KG81]] with a distinguished symbol $0 \in \Sigma$, and let $n \ge 1$.
The *Hamming weight* of a word $x = (x_1, \dots, x_n) \in \Sigma^n$ is
$$\mathrm{wt}(x) = \abs{\set{i \in \set{1, \dots, n} : x_i \ne 0}}.$$

## Remarks

Example: $\mathrm{wt}(10110) = 3$, since exactly the positions $1$, $3$ and $4$ are nonzero.
Over $\F_3$, $\mathrm{wt}(0, 2, 1, 0) = 2$.

Non-example: on an alphabet with no distinguished symbol, such as $\set{a, b, c}$, the weight is not defined until one symbol is named zero.

In all cases $\mathrm{wt}(x) = d(x, 0)$, the [[Hamming distance|K5287V64FH]] to the zero word.
If $\Sigma = \F_q$ is a [[finite field|0ZXZ82FTX2]], then $d(x, y) = \mathrm{wt}(x - y)$ for all $x, y \in \F_q^n$.
The weight is a norm-like function: $\mathrm{wt}(x) = 0$ only for $x = 0$, $\mathrm{wt}(-x) = \mathrm{wt}(x)$, and $\mathrm{wt}(x + y) \le \mathrm{wt}(x) + \mathrm{wt}(y)$.
