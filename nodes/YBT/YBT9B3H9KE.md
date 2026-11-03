---
tag: YBT9B3H9KE
kind: definition
name: Prefix code
msc: [94A45, 68P30]
defines: GNB3T6TD0M
uses: [BACPE6MVPZ, MWBRNBXW1Y, 1P6EP01HZF, RABRP2KG81]
sources:
  - url: https://en.wikipedia.org/wiki/Prefix_code
---

## Definition

Let $\Sigma$ be a finite [[alphabet|RABRP2KG81]] and let $\Sigma^*$ be the set of finite [[strings|1P6EP01HZF]] over $\Sigma$.
A string $u$ is a *prefix* of a string $w$ if $w = uv$ for some $v \in \Sigma^*$.
A [[variable-length code|BACPE6MVPZ]] $C \subseteq \Sigma^*$ is a *prefix code*, or *prefix-free code*, if no codeword of $C$ is a prefix of a different codeword of $C$.

## Remarks

Example: $C = \set{0, 10, 110, 111}$ over $\Sigma = \set{0, 1}$ is a prefix code.
The check: $0$ is not a prefix of the other words, which begin with $1$.
Also $10$ is not a prefix of $110$ or $111$, and $110$ and $111$ have the same length and differ.
Non-example: $\set{0, 01, 11}$ is not a prefix code, since $0$ is a prefix of $01$.
This code is still [[uniquely decodable|MWBRNBXW1Y]], so a uniquely decodable code need not be a prefix code.
Over a $D$-letter alphabet, a word is a path from the root of the rooted $D$-ary tree.
A prefix code is then a set of nodes of this tree in which no node lies below another.
Prefix codes are also called *instantaneous codes*.
