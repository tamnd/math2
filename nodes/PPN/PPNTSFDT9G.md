---
tag: PPNTSFDT9G
kind: proof
name: Proof that quotients of solvable groups are solvable
msc: [20F16]
proves: 027ZQS04SJ
uses: [0P3KZK0FTV, 096HN851YZ, 0HV9Y7WG5R, 0112DTS464, 0W77CVBCHQ, 0YYWCNTPWR]
sources:
  - url: https://en.wikipedia.org/wiki/Solvable_group
    locator: Properties
---

## Proof

We push a series of $G$ forward along $\varphi$.

1. Since $G$ is [[solvable|0P3KZK0FTV]], it has a [[subnormal series|096HN851YZ]] $\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G$ in which each factor $G_i/G_{i-1}$ is abelian.
2. For $0 \leq i \leq n$, let $K_i = \varphi(G_i)$. The [[image|0112DTS464]] of a subgroup under a [[homomorphism|0HV9Y7WG5R]] is a subgroup, since $\varphi(x)\varphi(y)^{-1} = \varphi(xy^{-1})$.
3. We have $K_0 = \{e\}$, and $K_n = \varphi(G) = K$ because $\varphi$ is surjective.
4. Fix $i$ with $1 \leq i \leq n$. Let $a = \varphi(x) \in K_i$ and $b = \varphi(y) \in K_{i-1}$, with $x \in G_i$ and $y \in G_{i-1}$. Then $aba^{-1} = \varphi(xyx^{-1})$.
5. Since $G_{i-1}$ is [[normal|0W77CVBCHQ]] in $G_i$, we have $xyx^{-1} \in G_{i-1}$. So $aba^{-1} \in K_{i-1}$, and $K_{i-1} \trianglelefteq K_i$.
6. So $\{e\} = K_0 \trianglelefteq \cdots \trianglelefteq K_n = K$ is a subnormal series of $K$.
7. For a group $A$ with normal subgroup $B$, the [[quotient|0YYWCNTPWR]] $A/B$ is abelian if and only if $u^{-1}v^{-1}uv \in B$ for all $u, v \in A$. Indeed, $uvB = vuB$ holds if and only if $(vu)^{-1}uv \in B$.
8. Let $a = \varphi(x)$ and $b = \varphi(y)$ be in $K_i$, with $x, y \in G_i$. Since $G_i/G_{i-1}$ is abelian, step 7 gives $x^{-1}y^{-1}xy \in G_{i-1}$.
9. Then $a^{-1}b^{-1}ab = \varphi(x^{-1}y^{-1}xy) \in K_{i-1}$. By step 7, $K_i/K_{i-1}$ is abelian.
10. So $K$ has a subnormal series with abelian factors, and $K$ is solvable.
11. For a normal subgroup $N$ of $G$, the projection $\pi \colon G \to G/N$, $\pi(g) = gN$, is a surjective homomorphism. By step 10, $G/N$ is solvable.

## Idea

Apply $\varphi$ to each term of a series of $G$. Normality and commutativity modulo the next term are statements about products, and a homomorphism preserves products. So the image series has abelian factors.
