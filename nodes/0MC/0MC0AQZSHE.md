---
tag: 0MC0AQZSHE
kind: statement
role: proposition
name: A finite abelian group is cyclic iff its exponent equals its order
msc: [20K01]
uses: [0FCCTFA275, 0B85Q41RP6, 071DDFVG4J, 07CQR9BW3R, 0JPYSD5E0B]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Finitely_generated_abelian_group
    locator: Invariant factor decomposition
  - url: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
    locator: Structure
---

## Statement

Let $G$ be a finite [[abelian group|082GHNPJ53]].
Then $G$ is [[cyclic|0KVGH0J5B3]] if and only if the [[exponent|0ZDW0H0VX4]] of $G$ equals $|G|$.

## Remarks

If $G$ is cyclic with generator $g$, then the order of $g$ is $|G|$, so the exponent is $|G|$.
For the converse, write $G \cong \mathbb{Z}/k_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/k_u\mathbb{Z}$ with $1 < k_1 \mid k_2 \mid \cdots \mid k_u$, by the [[classification|07CQR9BW3R]]. The exponent is $k_u$ and the order is $k_1 \cdots k_u$, so they are equal only when $u \leq 1$.
The abelian condition is necessary: $S_3$ has exponent $6$ and order $6$, but it is not cyclic.
For example, $(\mathbb{Z}/n\mathbb{Z})^\times$ is cyclic if and only if $\lambda(n) = \varphi(n)$.

## Explanations

### L1 human

In a cyclic group, one element has order equal to the size of the group.
For a finite abelian group, it is enough that the exponent equals the size.
Then the group is cyclic.
