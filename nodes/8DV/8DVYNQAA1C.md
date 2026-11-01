---
tag: 8DVYNQAA1C
kind: definition
name: Free product
msc: ["20E06"]
defines: TM7QS7P7X9
uses: [G5S1M9, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Free_product
---

## Definition

Let $(G_i)_{i \in I}$ be a family of [[groups|G5S1M9]], with $G_i \cap G_j = \emptyset$ for $i \ne j$ after relabelling.
A *reduced word* is a finite sequence $(g_1, \ldots, g_m)$, with $m \ge 0$, such that:

1. each $g_k$ is a non-identity element of some $G_{i_k}$;
2. consecutive letters lie in different groups: $i_k \ne i_{k+1}$ for $1 \le k < m$.

The *free product* $\mathop{\ast}_{i \in I} G_i$ is the set of reduced words.
The product of two words is their concatenation followed by reduction.
To reduce, replace two adjacent letters of the same $G_i$ by their product in $G_i$, and delete the letter if it is the identity.
Repeat until the word is reduced.
For two groups it is written $G * H$.

## Remarks

The product is well defined and associative, the empty word is the identity, and each $G_i$ embeds as the words of length at most $1$.
Equivalently, $\mathop{\ast}_i G_i$ is the coproduct of the $G_i$ in the category of groups.
That is, for every group $K$ and [[homomorphisms|0JYTG5K9Y4]] $\varphi_i \colon G_i \to K$, there is a unique homomorphism $\mathop{\ast}_i G_i \to K$ restricting to each $\varphi_i$.
Example: $\Z * \Z$ is the free group of rank $2$.
With generators $a$ of the first factor and $b$ of the second, its reduced words are the reduced words in $a^{\pm 1}, b^{\pm 1}$.
Another example: $\Z/2 * \Z/3$ is isomorphic to the [[modular group|VEKV1EM77B]] $PSL_2(\Z)$.
Non-example: the direct product $\Z \times \Z$ is not the free product $\Z * \Z$.
In $\Z \times \Z$ the element $a b a^{-1} b^{-1}$ is the identity, while in $\Z * \Z$ it is a reduced word of length $4$.
Given presentations $G = \langle S \mid R \rangle$ and $H = \langle T \mid Q \rangle$ with $S \cap T = \emptyset$, one has $G * H = \langle S \cup T \mid R \cup Q \rangle$.
