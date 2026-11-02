---
tag: 4GRWMXWJNZ
kind: definition
name: Semisimple module
msc: [16D60]
defines: N3MRHDKDGC
uses: [09VDS2W1E8, 0RGZ10DFPG, G00C22AEDH]
sources:
  - url: https://en.wikipedia.org/wiki/Semisimple_module
---

## Definition

Let $R$ be a ring and let $M$ be a left [[$R$-module|09VDS2W1E8]].
The module $M$ is *semisimple* if there is a family $(S_i)_{i \in I}$ of [[simple|G00C22AEDH]] [[submodules|0RGZ10DFPG]] of $M$ such that $M = \bigoplus_{i \in I} S_i$.

## Remarks

The empty family is allowed, so the zero module is semisimple.
Equivalently, $M$ is a sum of simple submodules, or every submodule of $M$ is a direct summand.
Example: the $\Z$-module $\Z/6\Z$ is semisimple.
The check: $\Z/6\Z = \set{0, 3} \oplus \set{0, 2, 4}$, and these subgroups have prime orders $2$ and $3$, so they are simple.
Non-example: the $\Z$-module $\Z/4\Z$ is not semisimple.
Its only simple submodule is $\set{0, 2}$, so every sum of simple submodules lies inside $\set{0, 2} \ne \Z/4\Z$.
Every vector space over a field, or over a division ring, is semisimple, as the direct sum of the lines spanned by the vectors of a basis.
