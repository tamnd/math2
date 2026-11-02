---
tag: 2V7JHTRMTA
kind: definition
name: Absorbing set
msc: [46A03, 52A07]
defines: NM1BCK3ZX9
uses: [05EGHEQZAW, 00S7C68D51]
sources:
  - url: https://en.wikipedia.org/wiki/Absorbing_set
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $V$ be a [[vector space|05EGHEQZAW]] over $\mathbb{K}$.
A subset $A \subseteq V$ is *absorbing* if the following holds.
For every $x \in V$ there is $r > 0$ such that $x \in c A$ for every $c \in \mathbb{K}$ with [[absolute value|00S7C68D51]] $\abs{c} \ge r$.

## Remarks

An absorbing set $A$ contains $0$: for $x = 0$ there is $c \ne 0$ with $0 \in cA$, so $0 = c a$ for some $a \in A$, and then $a = 0$.
If $A$ is [[balanced|2TDSHJJYS4]], then $A$ is absorbing if and only if for every $x \in V$ there is $t > 0$ with $t x \in A$.
Example: the open unit ball $A = \set{x : \norm{x} < 1}$ of a normed space is absorbing; for $x \in V$ take $r = \norm{x} + 1$, and then $\norm{x / c} < 1$ whenever $\abs{c} \ge r$.
Non-example: in $\R^2$, the axis $A = \R \times \set{0}$ is not absorbing, because $(0, 1) \notin c A$ for every $c$.
In a [[topological vector space|T32W553W95]] every neighbourhood of $0$ is absorbing, since $c \mapsto c^{-1} x$ is continuous and tends to $0$.
