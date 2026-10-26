---
tag: 0Q2MVQ7JMT
kind: definition
name: Internal direct product
msc: ["20E34"]
defines: 0VBZH90R1A
uses: [0YP7WYXF9V, 0W77CVBCHQ, 0NS1YTGM19]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_product_of_groups
    locator: Algebraic structure
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $H$ and $K$ be [[normal subgroups|0CB0DX5BVV]] of $G$.
The group $G$ is the internal direct product of $H$ and $K$ when $H \cap K = \{e\}$ and $HK = G$.

## Remarks

In this case, $hk = kh$ for all $h \in H$ and $k \in K$, because $hkh^{-1}k^{-1}$ lies in $H \cap K$.
Then the map $(h, k) \mapsto hk$ is an [[isomorphism|08MG7H8JW5]] from the [[direct product|00HF4RJ5QN]] $H \times K$ to $G$.
Also, each element of $G$ is a product $hk$ with $h \in H$ and $k \in K$ in exactly one way.
For example, $\mathbb{Z}/6\mathbb{Z}$ is the internal direct product of $\{0, 3\}$ and $\{0, 2, 4\}$.

## Explanations

### L1 human

Sometimes a group already contains two subgroups that behave like the two factors of a direct product.
They meet only in the identity, they fill the group together, and they are both normal.
Then the group is the direct product of these subgroups, up to isomorphism.
