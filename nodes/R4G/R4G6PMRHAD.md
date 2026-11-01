---
tag: R4G6PMRHAD
kind: definition
name: Projective resolution
msc: [13D02, 18G10]
defines: HK2AA1YSQ2
uses: [0B1261B5ED, 0NZ8JA25WK, BFFA03GE3V, JB7ZBFBA9C, 0DZ9DKAKZR]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(algebra)
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $M$ be an [[$R$-module|0NZ8JA25WK]].
A *projective resolution* of $M$ is an [[exact sequence|JB7ZBFBA9C]] of $R$-modules
$$\cdots \to P_2 \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \xrightarrow{\varepsilon} M \to 0$$
in which every $P_i$ is a [[projective module|BFFA03GE3V]].
It is a *free resolution* if every $P_i$ is a [[free module|0DZ9DKAKZR]].
It has *length* $n$ if $P_n \ne 0$ and $P_i = 0$ for all $i > n$.

## Remarks

Every module has a free resolution: take a free module $F_0$ mapping onto $M$, then a free module mapping onto the kernel, and repeat.
Example: over $\Z$, the sequence $0 \to \Z \xrightarrow{\cdot n} \Z \to \Z/n\Z \to 0$ is a free resolution of length $1$, since multiplication by $n \ne 0$ is injective and its image $n\Z$ is the kernel of the reduction map.
Over $R = \Z/4\Z$, the module $\Z/2\Z$ has the free resolution $\cdots \to R \xrightarrow{\cdot 2} R \xrightarrow{\cdot 2} R \to \Z/2\Z \to 0$, which never stops.
Non-example: $0 \to \Z \xrightarrow{\cdot 4} \Z \to \Z/2\Z \to 0$ is not a resolution, because it is not exact at the middle $\Z$.
The kernel of the reduction is $2\Z$, but the image of multiplication by $4$ is $4\Z$.
One often writes the resolution as the complex $P_\bullet$ together with the map $\varepsilon \colon P_0 \to M$; then $H_0(P_\bullet) \cong M$ and $H_i(P_\bullet) = 0$ for $i > 0$.
