---
tag: 4AY3RMCTA3
kind: definition
name: Goldie ring
msc: [16P60, 16U20]
defines: QFDC3NYHJE
uses: [0B1261B5ED, HB4XDKJTW8, 0GZ6Y1H4RN, YXEVE39Q31, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Goldie%27s_theorem
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity.
For a subset $X \subseteq R$, the *right annihilator* of $X$ is $r(X) = \set{a \in R : x a = 0 \text{ for all } x \in X}$, a right ideal of $R$.
The ring $R$ is *right Goldie* if:

1. $R$ has finite right uniform dimension: there is no infinite family of nonzero right ideals $I_1, I_2, \ldots$ of $R$ whose sum is direct;
2. $R$ satisfies the [[ascending chain condition|0GZ6Y1H4RN]] on right annihilators: every increasing chain $r(X_1) \subseteq r(X_2) \subseteq \cdots$ is eventually constant.

Left Goldie rings are defined in the same way with left ideals and left [[annihilators|HB4XDKJTW8]].
A ring is *Goldie* if it is both right and left Goldie.

## Remarks

Example: a right [[Noetherian ring|0670T59HGE]] $R$ is right Goldie.
An infinite direct sum $I_1 \oplus I_2 \oplus \cdots$ of nonzero right ideals would give a strictly increasing chain $I_1 \subset I_1 \oplus I_2 \subset \cdots$, which is impossible.
Right annihilators are right ideals, so they satisfy the ascending chain condition.

Example: every commutative integral domain is Goldie, since two nonzero ideals $I, J$ always meet in the nonzero ideal $IJ$, and the only annihilators are $0$ and $R$.

Non-example: let $k$ be a field and $R = \prod_{n \ge 1} k$.
The ideals $I_n = k e_n$, where $e_n$ has $1$ in coordinate $n$ and $0$ elsewhere, are nonzero and their sum is direct, so clause 1 fails.

Clause 1 can be stated with [[uniform modules|YXEVE39Q31]]: $R_R$ has finite uniform dimension exactly when it contains an essential submodule that is a finite direct sum of uniform right ideals.
