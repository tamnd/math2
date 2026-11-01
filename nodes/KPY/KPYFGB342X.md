---
tag: KPYFGB342X
kind: definition
name: Hecke character
msc: [11R42, 11R56]
defines: R65XKHN4D1
uses: [MWBDFS2KJ5, 9GHD9MXNYV, 0JYTG5K9Y4, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Hecke_character
---

## Definition

Let $K$ be a [[number field|MWBDFS2KJ5]], let $I_K$ be its idele group and let $C_K = I_K / K^\times$ be its [[idele class group|9GHD9MXNYV]].
A *Hecke character* of $K$ is a continuous [[group homomorphism|0JYTG5K9Y4]]
$$\chi \colon I_K \to \C^\times$$
such that $\chi(a) = 1$ for every $a \in K^\times$.
Equivalently, it is a continuous homomorphism $C_K \to \C^\times$.

## Remarks

Example: the idele norm $\abs{x} = \prod_v \abs{x_v}_v$ is continuous and multiplicative, and $\abs{a} = 1$ for $a \in K^\times$ by the product formula; so it is a Hecke character, and so is $\abs{\cdot}^s$ for every $s \in \C$.
Non-example: for $K = \Q$, the map $x \mapsto \abs{x_\infty}$ that keeps only the real component is a continuous homomorphism, but it sends the rational number $2$ to $2 \neq 1$.
Some authors call $\chi$ a Hecke character only when $\abs{\chi(x)} = 1$ for all $x$, and call the general case a quasi-character or Größencharakter.
Every Hecke character is a unitary one times $\abs{\cdot}^\sigma$ for a real number $\sigma$.
The Hecke characters of $\Q$ of finite order correspond to the primitive [[Dirichlet characters|7XB5VJKDPG]].
