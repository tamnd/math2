---
tag: JKPSBMX80N
kind: definition
name: Tate–Shafarevich group
msc: [11G05, 11R34, 14H52]
defines: BK9WBMF56G
uses: [427N6S6QQW, MWBDFS2KJ5, BT5V3TSNY6, 9MPCZ3EAJM, 0XTY86BZKY]
sources:
  - url: https://en.wikipedia.org/wiki/Tate%E2%80%93Shafarevich_group
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with algebraic closure $\overline{K}$ and absolute [[Galois group|0XTY86BZKY]] $G_K = \Gal(\overline{K}/K)$, and let $E$ be an [[elliptic curve|427N6S6QQW]] over $K$.
For each [[place|BT5V3TSNY6]] $v$ of $K$, let $K_v$ be the completion of $K$ at $v$.
Fix an embedding $\overline{K} \to \overline{K_v}$; it identifies $G_{K_v}$ with a decomposition subgroup of $G_K$.
Let $H^1(K, E) = H^1(G_K, E(\overline{K}))$ be the first [[Galois cohomology|9MPCZ3EAJM]] group, and similarly $H^1(K_v, E) = H^1(G_{K_v}, E(\overline{K_v}))$.
Let the map below have as components the restrictions, with the product over all places $v$ of $K$.
The *Tate–Shafarevich group* of $E$ over $K$ is
$$\text{Ш}(E/K) = \ker\left( H^1(K, E) \to \prod_{v} H^1(K_v, E) \right).$$

## Remarks

The group $H^1(K, E)$ classifies principal homogeneous spaces of $E$: curves $C$ over $K$ with a simply transitive action of $E$ defined over $K$.
A class is trivial exactly when $C$ has a point over $K$, so $\text{Ш}(E/K)$ consists of the classes of such curves $C$ that have a point over every $K_v$.

Example: Selmer's curve $C \colon 3x^3 + 4y^3 + 5z^3 = 0$ in $\mathbb{P}^2_{\Q}$ has points over $\R$ and over every $\Q_p$, but no point over $\Q$.
It is a principal homogeneous space for its Jacobian $E \colon x^3 + y^3 + 60z^3 = 0$, so it gives a nonzero element of $\text{Ш}(E/\Q)$.

Non-example: let $C$ be a principal homogeneous space of $E$ over $\Q$ with $C(\R) = \emptyset$.
Its class in $H^1(\Q, E)$ has nonzero restriction at the real place, so it is not in $\text{Ш}(E/\Q)$.

The group $\text{Ш}(E/K)$ is a torsion abelian group, and each of its $n$-torsion subgroups is finite, by the finiteness of the [[Selmer group|36YNSTESMQ]].
It is conjectured to be finite; when it is finite, the Cassels–Tate pairing shows that its order is a perfect square.
The letter Ш is the Cyrillic letter sha.
