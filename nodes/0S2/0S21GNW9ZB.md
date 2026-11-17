---
tag: 0S21GNW9ZB
kind: concept
name: Image of a homomorphism
aliases: [range-of-a-homomorphism]
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
uses: [0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Image and kernel
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: Image of a subset
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: Inverse image
---

## Summary

Let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
The image of $\varphi$ is the set $\operatorname{im} \varphi = \{ \varphi(g) : g \in G \}$.
It is a subset of the codomain $H$, and it is a [[subgroup|0X1JXT47GA]] of $H$.
The map $\varphi$ is surjective exactly when $\operatorname{im} \varphi = H$.

## Motivation

A homomorphism $\varphi \colon G \to H$ need not reach every element of $H$.
The image is the part of $H$ that $\varphi$ reaches.
It is a group in its own right, and it is a copy of a quotient of $G$.
The [[first isomorphism theorem|0CXXJNG5B6]] makes this exact: $G/\ker \varphi \cong \operatorname{im} \varphi$.
So the image shows which quotients of $G$ appear inside $H$.

## Notation

We write $\operatorname{im} \varphi$ or $\varphi(G)$ for the image.
For a subset $K$ of $G$, we write $\varphi(K) = \{ \varphi(k) : k \in K \}$.
For a subset $L$ of $H$, we write $\varphi^{-1}(L) = \{ g \in G : \varphi(g) \in L \}$ for the [[preimage|0FGCFY1AZX]] of $L$.
The notation $\varphi^{-1}(L)$ does not require $\varphi$ to have an inverse map.
We write $H \le G$ when $H$ is a subgroup of $G$, and $N \trianglelefteq G$ when $N$ is a [[normal subgroup|0CB0DX5BVV]] of $G$.

## Remarks

### Examples

- The homomorphism $\mathbb{Z} \to \mathbb{C}^\times$, $n \mapsto i^n$, has image $\{1, i, -1, -i\}$ ([[the powers of i|~cd8789f9]]).
- Squaring on $\mathbb{R}^\times$ has image $\mathbb{R}_{>0}$, the positive real numbers ([[squaring on the nonzero reals|~67d7458f]]).
- Doubling on $\mathbb{Z}$ has image $2\mathbb{Z}$, the even integers ([[doubling on the integers|PVR5EX71PD]]).
- The [[determinant|00KDZRW4C0]] $\mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$ has image $\mathbb{R}^\times$. For $t \ne 0$, the diagonal matrix with entries $t, 1, \dots, 1$ has determinant $t$.
- For $K \le G$, the inclusion $K \to G$, $k \mapsto k$, has image $K$.
- For $n \ge 2$, the [[sign|02DKV69ZH0]] $S_n \to \{1, -1\}$ has image $\{1, -1\}$, because a transposition has sign $-1$.

### Non-examples

- The set of squares $\{0, 1, 4, 9, \dots\}$ is not the image of any homomorphism $\mathbb{Z} \to \mathbb{Z}$, because it is not a subgroup ([[the squares are not an image|~6418f6dd]]).
- The set of negative real numbers is not the image of any homomorphism into $\mathbb{R}^\times$, because it does not contain the identity $1$.
- The odd integers are not the image of any homomorphism into $(\mathbb{Z}, +)$, because they do not contain $0$.

### Basic properties

- The image is a subgroup of $H$. It contains $e_H = \varphi(e_G)$, and $\varphi(a)\varphi(b)^{-1} = \varphi(ab^{-1})$ lies in it ([[subgroup criterion|05N4TQKPH0]]).
- If $K \le G$, then $\varphi(K) \le H$. The proof is the same as for the image, with $a, b \in K$.
- If $L \le H$, then $\varphi^{-1}(L) \le G$. It contains $e_G$, and if $\varphi(a), \varphi(b) \in L$, then $\varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1} \in L$.
- The preimage $\varphi^{-1}(L)$ contains $\ker \varphi = \varphi^{-1}(\{e_H\})$, because $e_H \in L$.
- If $L \trianglelefteq H$, then $\varphi^{-1}(L) \trianglelefteq G$. For $\varphi(a) \in L$ and $g \in G$, we get $\varphi(gag^{-1}) = \varphi(g)\varphi(a)\varphi(g)^{-1} \in L$.
- If $N \trianglelefteq G$, then $\varphi(N) \trianglelefteq \operatorname{im} \varphi$. Each element of $\operatorname{im} \varphi$ is some $\varphi(g)$, and $\varphi(g)\varphi(n)\varphi(g)^{-1} = \varphi(gng^{-1}) \in \varphi(N)$.
- So if $\varphi$ is surjective and $N \trianglelefteq G$, then $\varphi(N) \trianglelefteq H$.
- The image of an [[abelian group|082GHNPJ53]] is abelian, and the image of a [[cyclic group|0KVGH0J5B3]] $\langle g \rangle$ is the cyclic group $\langle \varphi(g) \rangle$.
- If $G$ is finite, then $|\operatorname{im} \varphi| = |G| / |\ker \varphi|$, so $|\operatorname{im} \varphi|$ divides $|G|$ ([[first isomorphism theorem|0CXXJNG5B6]]).

### History

Hölder defined quotient groups in 1889.
Emmy Noether stated the isomorphism theorems in general form for modules in a paper of 1927 in Mathematische Annalen.
In the modern form of the first of these theorems, the image of a homomorphism is isomorphic to the quotient of the domain by the kernel.

### Common errors

- The image of a normal subgroup is normal in the image, but not always in $H$. The inclusion of $N = \{e, (1\,2)\}$ into $S_3$ sends the normal subgroup $N$ of $N$ to a subgroup that is [[not normal in S3|XD0WBC1MWB]].
- The image need not be the whole codomain. Doubling on $\mathbb{Z}$ has image $2\mathbb{Z}$, and $1$ is not in it.
- The image lies in $H$, and the kernel lies in $G$. Their orders are linked by $|G| = |\ker \varphi| \cdot |\operatorname{im} \varphi|$ for finite $G$, not by an inclusion.

## Explanations

### L1 human

The image of a homomorphism is the set of all its values.
Think of a shadow of an object on a wall.
The shadow is the part of the wall that the object reaches.
The image is the part of the target group that the homomorphism reaches.
It is always a group again: it contains the identity, and it contains the product and the inverses of its elements.

### L2 human

We study the homomorphism $\varphi \colon \mathbb{Z}/6\mathbb{Z} \to \mathbb{Z}/6\mathbb{Z}$, $\varphi(x) = 2x$.

1. The map is a homomorphism, because $2(x + y) = 2x + 2y$.
2. The values are $0 \mapsto 0$, $1 \mapsto 2$, $2 \mapsto 4$, $3 \mapsto 0$, $4 \mapsto 2$ and $5 \mapsto 4$.
3. So $\operatorname{im} \varphi = \{0, 2, 4\}$ and $\ker \varphi = \{0, 3\}$. The orders satisfy $6 = 2 \cdot 3$.
4. For the subgroup $K = \{0, 2, 4\}$, we get $\varphi(K) = \{0, 4, 2\}$, because $2 \cdot 4 = 8 = 2$ in $\mathbb{Z}/6\mathbb{Z}$.
5. For the subgroup $L = \{0, 3\}$, the equation $2x = 3$ has no solution modulo $6$, because $2x$ is even. So $\varphi^{-1}(L) = \varphi^{-1}(\{0\}) = \{0, 3\}$.
6. For the subgroup $L = \{0, 2, 4\}$, each $x$ satisfies $2x \in L$. So $\varphi^{-1}(L) = \mathbb{Z}/6\mathbb{Z}$.

The typical use of the image is to find a copy of a quotient of $G$ inside $H$.
Here $\operatorname{im} \varphi = \{0, 2, 4\}$ is a copy of $(\mathbb{Z}/6\mathbb{Z})/\{0, 3\}$.

The trap is normality.
In an abelian group such as $\mathbb{Z}/6\mathbb{Z}$, each subgroup is normal, so the trap does not appear.
In $S_3$, compose permutations from right to left.
The homomorphism $\mathbb{Z}/2\mathbb{Z} \to S_3$ with $1 \mapsto (1\,2)$ is well defined, because $(1\,2)(1\,2) = e$.
The domain is abelian, so all its subgroups are normal.
But the image $\{e, (1\,2)\}$ is not normal in $S_3$: $(1\,3)(1\,2)(1\,3) = (2\,3)$.

### L3 human

The image of $\varphi$ is the smallest subgroup of $H$ through which $\varphi$ factors.
In the [[category of groups|2CX7RPPXA9]], each homomorphism factors as a surjective map onto its image followed by an injective inclusion.
In this category the [[epimorphisms|RVXDSY04KG]] are exactly the surjective homomorphisms.

The maps $K \mapsto \varphi(K)$ and $L \mapsto \varphi^{-1}(L)$ give a bijection between the subgroups of $G$ that contain $\ker \varphi$ and the subgroups of $\operatorname{im} \varphi$.
For the quotient map $G \to G/N$ this is the [[correspondence theorem|0S9ZVZ34MD]].
The bijection preserves normality, but normality in $\operatorname{im} \varphi$ is weaker than normality in $H$.
