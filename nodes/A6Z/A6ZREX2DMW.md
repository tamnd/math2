---
tag: A6ZREX2DMW
kind: definition
name: Selmer group
msc: [11G05, 11R34, 14H52]
defines: 36YNSTESMQ
uses: [427N6S6QQW, MWBDFS2KJ5, BT5V3TSNY6, 9MPCZ3EAJM, 0XTY86BZKY, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Selmer_group
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with absolute [[Galois group|0XTY86BZKY]] $G_K$.
Let $\phi \colon E \to E'$ be an isogeny of [[elliptic curves|427N6S6QQW]] over $K$.
That is, $\phi$ is a nonconstant morphism over $K$ that is also a [[group homomorphism|0JYTG5K9Y4]].
Let $E[\phi] = \ker(\phi \colon E(\overline{K}) \to E'(\overline{K}))$, a finite $G_K$-module.
For each [[place|BT5V3TSNY6]] $v$ of $K$, let $\delta_v \colon E'(K_v) \to H^1(K_v, E[\phi])$ be the connecting map of the [[Galois cohomology|9MPCZ3EAJM]] sequence of $0 \to E[\phi] \to E \xrightarrow{\phi} E' \to 0$ over the completion $K_v$.
The *$\phi$-Selmer group* of $E$ over $K$ is
$$\mathrm{Sel}^{(\phi)}(E/K) = \set{\xi \in H^1(K, E[\phi]) : \mathrm{res}_v(\xi) \in \delta_v(E'(K_v)) \text{ for every place } v \text{ of } K},$$
where $\mathrm{res}_v \colon H^1(K, E[\phi]) \to H^1(K_v, E[\phi])$ is restriction.
For an integer $n \ge 2$, the *$n$-Selmer group* $\mathrm{Sel}^{(n)}(E/K)$ is the case $\phi = [n] \colon E \to E$.

## Remarks

Equivalently, $\mathrm{Sel}^{(\phi)}(E/K)$ is the kernel of $H^1(K, E[\phi]) \to \prod_v H^1(K_v, E)$.
There is an exact sequence
$$0 \to E'(K)/\phi(E(K)) \to \mathrm{Sel}^{(\phi)}(E/K) \to \text{Ш}(E/K)[\phi] \to 0,$$
where $\text{Ш}(E/K)$ is the [[Tate–Shafarevich group|BK9WBMF56G]].
The Selmer group is finite and effectively computable, which bounds the rank of $E(K)$.

Example: for $E \colon y^2 = x^3 - x$ over $\Q$ and $n = 2$, one has $E(\Q) = \set{O, (0, 0), (1, 0), (-1, 0)}$ and $2E(\Q) = \set{O}$.
So $E(\Q)/2E(\Q)$ has order $4$, and by the exact sequence $\mathrm{Sel}^{(2)}(E/\Q)$ has order at least $4$.

Non-example: a class of $H^1(\Q, E[2])$ whose restriction to $H^1(\R, E[2])$ does not come from $E(\R)$ fails the local condition at the real place, so it is not in $\mathrm{Sel}^{(2)}(E/\Q)$.
