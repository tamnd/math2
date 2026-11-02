---
tag: QJNS6RJ743
kind: definition
name: Left-orderable group
msc: ["20F60", "06F15"]
defines: F1WYS82NNB
uses: [G5S1M9, 0316AYH1SC, ZZFFBXDTWN, VQ4SSKS53D]
sources:
  - url: https://en.wikipedia.org/wiki/Linearly_ordered_group
---

## Definition

Let $G$ be a [[group|G5S1M9]].
A *left order* on $G$ is a [[total order|0316AYH1SC]] $\le$ on $G$ such that for all $a, b, c \in G$,
$$a \le b \implies ca \le cb.$$
The group $G$ is *left-orderable* if it has a left order.

## Remarks

Every [[orderable group|ZZFFBXDTWN]] is left-orderable.
Example: the Klein bottle group $K = \langle a, b \mid b a b^{-1} = a^{-1} \rangle$ is left-orderable but not orderable.
Every element of $K$ is $b^n a^m$ for unique integers $n, m$.
Set $b^n a^m \le b^{n'} a^{m'}$ when $n < n'$, or $n = n'$ and $m \le m'$.
Left multiplication by $b$ adds $1$ to $n$, and left multiplication by $a$ sends $b^n a^m$ to $b^n a^{m + (-1)^n}$.
Both keep this order, so it is a left order.
In a two-sided order, $a > e$ would give $a^{-1} = b a b^{-1} > e$, which contradicts $a > e$.
The case $a < e$ is the same, so $K$ is not orderable.
Non-example: a group with an element $g \ne e$ of finite order $n$ is not left-orderable, since $e < g$ gives $e < g < g^2 < \cdots < g^n = e$.
If $g < e$, the same argument applies to $g^{-1}$.
So a left-orderable group is a [[torsion-free group|VQ4SSKS53D]].
Equivalently, $G$ is left-orderable if and only if it has a subsemigroup $P$ with $G = P \sqcup \set{e} \sqcup P^{-1}$.
