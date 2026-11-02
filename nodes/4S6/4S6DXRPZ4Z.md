---
tag: 4S6DXRPZ4Z
kind: definition
name: Essential submodule
msc: [16D10]
defines: 8MS51FASMX
uses: [09VDS2W1E8, 0RGZ10DFPG]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_extension
---

## Definition

Let $R$ be a ring and let $M$ be a left [[$R$-module|09VDS2W1E8]].
A [[submodule|0RGZ10DFPG]] $N$ of $M$ is *essential* in $M$ if $N \cap L \ne 0$ for every nonzero submodule $L$ of $M$.
In that case $M$ is called an *essential extension* of $N$.

## Remarks

Equivalently, for every nonzero $m \in M$ there is $r \in R$ with $rm \in N$ and $rm \ne 0$.
Notation: $N \subseteq_e M$ or $N \trianglelefteq_e M$, depending on the author.
Example: for $n \ne 0$, the submodule $n\Z$ is essential in the $\Z$-module $\Z$.
The check: a nonzero submodule $a\Z$ of $\Z$ contains $na \ne 0$, which lies in $n\Z$.
Non-example: $\Z \oplus 0$ is not essential in $\Z \oplus \Z$, since the nonzero submodule $0 \oplus \Z$ meets it only in $0$.
A nonzero direct summand $N \ne M$ is never essential, since its complement meets it in $0$.
