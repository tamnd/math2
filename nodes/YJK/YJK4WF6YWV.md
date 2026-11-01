---
tag: YJK4WF6YWV
kind: definition
name: Ramification group
msc: [11S15, 11S20]
defines: BQJ9ZX9P3V
uses: [J85FZEQG38, 0QMZAQ6QQ4, 0XTY86BZKY, 0X1JXT47GA, MGM3CNJW9V, NJ3APQ8BHH]
sources:
  - url: https://en.wikipedia.org/wiki/Ramification_group
---

## Definition

Let $L / K$ be a finite [[Galois extension|0QMZAQ6QQ4]] of non-Archimedean [[local fields|J85FZEQG38]], with [[Galois group|0XTY86BZKY]] $G$.
Let $\mathcal{O}_L$ be the valuation ring of $L$ and let $v_L$ be the normalized discrete valuation of $L$, with $v_L(L^\times) = \Z$.
For an integer $i \ge -1$, the $i$-th *ramification group* (in the lower numbering) is
$$G_i = \set{\sigma \in G : v_L(\sigma(a) - a) \ge i + 1 \text{ for all } a \in \mathcal{O}_L}.$$

## Remarks

Each $G_i$ is a normal [[subgroup|0X1JXT47GA]] of $G$, and $G_{-1} = G \supseteq G_0 \supseteq G_1 \supseteq \cdots$.
The group $G_0$ is the inertia group, and $G_i = 1$ for $i$ large.
If $p$ is the characteristic of the [[residue field|NJ3APQ8BHH]], then $G_0 / G_1$ is cyclic of order prime to $p$, and $G_i / G_{i+1}$ is an elementary abelian $p$-group for $i \ge 1$.
If $\mathcal{O}_L = \mathcal{O}_K[\alpha]$, then $\sigma \in G_i$ exactly when $v_L(\sigma(\alpha) - \alpha) \ge i + 1$.
Example: for $L = \Q_2(i)$ and $K = \Q_2$, one has $\mathcal{O}_L = \Z_2[i]$ and $v_L(2) = 2$.
For complex conjugation $\sigma$, $v_L(\sigma(i) - i) = v_L(-2i) = 2$, so $\sigma \in G_1$ and $\sigma \notin G_2$.
Non-example: if $L / K$ is unramified and $\sigma \neq 1$, then $\sigma$ acts nontrivially on the residue field, so $v_L(\sigma(a) - a) = 0$ for some $a$ and $\sigma \notin G_0$.
There is also an upper numbering $G^u$, defined through the Herbrand function, which behaves well under quotients.
