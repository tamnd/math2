---
tag: 4DBGACFER8
kind: definition
name: Block code
msc: [94B25, 94B05]
defines: EFGYF9P0PN
uses: [RABRP2KG81, 1P6EP01HZF, 0BJR9QR08E, 0BBTH3YSZA]
sources:
  - url: https://en.wikipedia.org/wiki/Block_code
---

## Definition

Let $\Sigma$ be a [[finite|0BBTH3YSZA]] [[alphabet|RABRP2KG81]] with $q \ge 2$ symbols and let $n \ge 1$ be an integer.
A *block code* of length $n$ over $\Sigma$ is a [[subset|0BJR9QR08E]] $C \subseteq \Sigma^n$ with at least two elements.
Its elements are the codewords, [[strings|1P6EP01HZF]] of length $n$ over $\Sigma$.
An encoding map for $C$ is a bijection $E \colon M \to C$ from a set $M$ of messages.
The *rate* of $C$ is $R = \log_q \abs{C} / n$.

## Remarks

Example: the binary even-weight code $C = \set{000, 011, 101, 110} \subseteq \set{0,1}^3$ is a block code of length $3$ with $4$ codewords.
Its rate is $\log_2 4 / 3 = 2/3$.

Non-example: the set $\set{0, 10, 11}$ of binary words is not a block code, since its words have different lengths.
It is a [[prefix code|GNB3T6TD0M]], a kind of variable-length code.

A block code with $M$ codewords is often called an $(n, M)$ code, or $(n, M, d)$ code when its minimum distance $d$ is also given.
When $\Sigma$ is a finite field and $C$ is a linear subspace of $\Sigma^n$ of dimension $k$, the code is linear, with rate $k / n$.
The rate lies in $(0, 1]$, and it equals $1$ only for $C = \Sigma^n$, which has no redundancy.
