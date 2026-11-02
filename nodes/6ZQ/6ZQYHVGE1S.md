---
tag: 6ZQYHVGE1S
kind: definition
name: Balanced set
msc: [46A03, 52A07]
defines: 2TDSHJJYS4
uses: [05EGHEQZAW, 00S7C68D51]
sources:
  - url: https://en.wikipedia.org/wiki/Balanced_set
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $V$ be a [[vector space|05EGHEQZAW]] over $\mathbb{K}$.
A subset $A \subseteq V$ is *balanced* if $\lambda a \in A$ for every $a \in A$ and every $\lambda \in \mathbb{K}$ with $\abs{\lambda} \le 1$, where $\abs{\lambda}$ is the [[absolute value|00S7C68D51]].

## Remarks

In short, $\lambda A \subseteq A$ whenever $\abs{\lambda} \le 1$.
Balanced sets are also called *circled*.
A set that is both convex and balanced is called *absolutely convex*, or a *disk*.
Example: the closed unit ball $A = \set{x : \norm{x} \le 1}$ of a normed space is balanced, since $\norm{\lambda a} = \abs{\lambda} \norm{a} \le 1$ for $a \in A$ and $\abs{\lambda} \le 1$.
Non-example: in $\R$, the interval $[0, 1]$ is not balanced, since $1 \in [0, 1]$ but $(-1) \cdot 1 \notin [0, 1]$.
Over $\C$ the condition is stronger: the square $Q = \set{a + b i : \abs{a} \le 1, \abs{b} \le 1}$ is balanced in the real vector space $\C = \R^2$, but not in the complex vector space $\C$, since $1 + i \in Q$ while $e^{i \pi / 4} (1 + i) = \sqrt{2} \, i \notin Q$.
