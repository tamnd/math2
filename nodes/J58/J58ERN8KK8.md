---
tag: J58ERN8KK8
kind: definition
name: Simple module
msc: [16D60]
defines: G00C22AEDH
uses: [09VDS2W1E8, 0RGZ10DFPG]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_module
---

## Definition

Let $R$ be a ring and let $M$ be a left [[$R$-module|09VDS2W1E8]].
The module $M$ is *simple* if:

1. $M \ne 0$;
2. the only [[submodules|0RGZ10DFPG]] of $M$ are $0$ and $M$.

## Remarks

Equivalently, $M \ne 0$ and $M = Rm$ for every nonzero $m \in M$.
Example: for a prime $p$, the $\Z$-module $\Z/p\Z$ is simple.
The check: its submodules are subgroups, whose orders divide $p$, so they are $0$ or $\Z/p\Z$.
Example: for a field $K$, the column space $K^n$ is a simple $M_n(K)$-module, since any nonzero vector is sent to any other vector by some matrix.
Non-example: the $\Z$-module $\Z$ is not simple, since $2\Z$ is a submodule different from $0$ and $\Z$; clause 2 fails.
The zero module is not simple, by clause 1.
