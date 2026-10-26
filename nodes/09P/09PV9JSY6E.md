---
tag: 09PV9JSY6E
kind: definition
name: Prüfer sequence
msc: [05C05]
defines: 0GDQRETR59
uses: [0MJ0JS72DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Prüfer_sequence
    locator: Algorithm to convert a  tree into a Prüfer sequence
---

## Definition

Let $n \ge 2$ be an integer and let $T$ be a [[tree|0MJ0JS72DZ]] with vertex set $\{1, \dots, n\}$.
The Prüfer sequence of $T$ is the sequence $(a_1, \dots, a_{n-2})$ that this process gives.
Let $T_0 = T$. For $i = 1, \dots, n - 2$, let $\ell_i$ be the leaf of $T_{i-1}$ with the smallest label.
Let $a_i$ be the unique neighbour of $\ell_i$ in $T_{i-1}$, and let $T_i = T_{i-1} - \ell_i$.

## Remarks

The map $T \mapsto (a_1, \dots, a_{n-2})$ is a bijection from the labelled trees on $\{1, \dots, n\}$ to $\{1, \dots, n\}^{n-2}$. This proves [[Cayley's formula|0M2SSGSYPE]].
A vertex $v$ appears $\deg(v) - 1$ times in the sequence. Thus the leaves are the labels that do not appear.
Example: the star with centre $1$ on $\{1, 2, 3, 4\}$ has the sequence $(1, 1)$.

## Explanations

### L1 human

Remove the smallest leaf again and again, and each time write down the vertex it was attached to.
Stop when two vertices are left. The list of $n - 2$ numbers fixes the tree.
