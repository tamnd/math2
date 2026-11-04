---
tag: C3G4ZEM72Z
kind: proof
name: Proof that subgroups of solvable groups are solvable
msc: [20F16]
proves: 05Y0F9M0TS
uses: [0P3KZK0FTV, 096HN851YZ, 0N0PXCTYA7, 0ZTGMDNVTB, 0W77CVBCHQ, 0YYWCNTPWR, 0HV9Y7WG5R, 0Z424HK8CQ, 0CXXJNG5B6, 0C9ZKYSPYR]
sources:
  - url: https://en.wikipedia.org/wiki/Solvable_group
    locator: Properties
---

## Proof

We intersect a series of $G$ with $H$.

1. Since $G$ is [[solvable|0P3KZK0FTV]], it has a [[subnormal series|096HN851YZ]] $\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G$ in which each factor $G_i/G_{i-1}$ is abelian.
2. For $0 \leq i \leq n$, let $H_i = H \cap G_i$. It is a [[subgroup|0N0PXCTYA7]] of $H$, since an [[intersection of subgroups is a subgroup|0ZTGMDNVTB]]. Also $H_0 = \{e\}$ and $H_n = H$.
3. Fix $i$ with $1 \leq i \leq n$. Define $\varphi_i \colon H_i \to G_i/G_{i-1}$ by $\varphi_i(h) = hG_{i-1}$. Since $h \in G_i$, this lands in the [[quotient group|0YYWCNTPWR]] $G_i/G_{i-1}$.
4. The map $\varphi_i$ is a [[homomorphism|0HV9Y7WG5R]], because $(hk)G_{i-1} = (hG_{i-1})(kG_{i-1})$ for $h, k \in H_i$.
5. Its [[kernel|0Z424HK8CQ]] is $\{h \in H_i : h \in G_{i-1}\} = H \cap G_{i-1} = H_{i-1}$.
6. [[The kernel is a normal subgroup|0C9ZKYSPYR]] of the domain. So $H_{i-1} \trianglelefteq H_i$, and $\{e\} = H_0 \trianglelefteq \cdots \trianglelefteq H_n = H$ is a subnormal series of $H$.
7. By the [[first isomorphism theorem|0CXXJNG5B6]], $H_i/H_{i-1}$ is isomorphic to the image of $\varphi_i$, which is a subgroup of $G_i/G_{i-1}$.
8. A subgroup of an abelian group is abelian, and a group isomorphic to an abelian group is abelian. So $H_i/H_{i-1}$ is abelian.
9. So $H$ has a subnormal series with abelian factors, and $H$ is solvable.

## Idea

Cut the series of $G$ down to $H$ by intersecting each term with $H$. Each new factor embeds into the old factor at the same place. A subgroup of an abelian group is abelian, so the new factors are abelian too.
