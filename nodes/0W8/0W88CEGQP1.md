---
tag: 0W88CEGQP1
kind: concept
name: Kernel of a homomorphism
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
uses: [0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Examples
same_as:
  wikidata: Q574844
  wikipedia: Kernel (algebra)
---

## Summary

Let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]], and let $e_H$ be the identity element of $H$.
The kernel of $\varphi$ is the set $\ker \varphi = \{ g \in G : \varphi(g) = e_H \}$.
It is a subset of the domain $G$.
The kernel is a [[normal subgroup|0CB0DX5BVV]] of $G$, and it measures how far $\varphi$ is from being injective.

## Motivation

A homomorphism can send many elements to the same value.
The kernel collects the elements that go to the identity, and it controls all the other coincidences.
For $a, b \in G$ we have $\varphi(a) = \varphi(b)$ exactly when $a^{-1}b \in \ker \varphi$.
So the kernel alone tells which elements $\varphi$ cannot separate.
For example, reduction modulo $12$ cannot separate $3$ and $15$, because $15 - 3 = 12$ lies in the kernel $12\mathbb{Z}$.

## Notation

We write $\ker \varphi$ for the kernel.
When $H$ is written additively, the kernel is the set of elements that go to $0$.
When $H$ is written multiplicatively, as $\mathbb{R}^\times$ or $\mathbb{C}^\times$, the kernel is the set of elements that go to $1$.
For $g \in G$, the left [[coset|564VVAQTNR]] $g \ker \varphi$ is the set $\{ gk : k \in \ker \varphi \}$.

## Remarks

### Examples

- Reduction modulo $n$, $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, has kernel $n\mathbb{Z}$, the set of multiples of $n$ ([[reduction modulo n|BV08DGBD7C]]).
- The [[determinant|00KDZRW4C0]] $\det \colon \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$ has kernel $\mathrm{SL}_n(\mathbb{R})$, the matrices with determinant $1$ ([[the special linear group as a kernel|556HZEYCQF]]).
- The [[sign|02DKV69ZH0]] $S_n \to \{1, -1\}$ has kernel $A_n$, the even permutations ([[the alternating group as a kernel|TJ6EBSS3S7]]).
- The homomorphism $\mathbb{Z} \to \mathbb{C}^\times$, $n \mapsto i^n$, has kernel $4\mathbb{Z}$ ([[the powers of i|RQMBV42EDX]]).
- Squaring on $\mathbb{R}^\times$, $x \mapsto x^2$, has kernel $\{1, -1\}$ ([[squaring on the nonzero reals|AJ8DC6PBH4]]).
- The map $\mathbb{R} \to \mathbb{C}^\times$, $t \mapsto e^{2\pi i t}$, has kernel $\mathbb{Z}$ ([[the real numbers modulo the integers|FV86TFARY4]]).

### Non-examples

- The subgroup $\{e, (1\,2)\}$ of $S_3$ is not the kernel of any homomorphism, because it is not normal ([[a subgroup of order two in S3 is not a kernel|QEM3BK15Z8]]).
- The set of odd integers is not the kernel of reduction modulo $2$. It is the set of integers that go to $1$, and it does not contain $0$.
- In $S_3$, the set $\{e, (1\,2), (1\,3), (2\,3)\}$ of elements of order at most $2$ is not a kernel. It has $4$ elements, and $4$ does not divide $6$, so by [[Lagrange's theorem|3C53TD]] it is not even a subgroup.

### Basic properties

- The kernel contains $e_G$, because $\varphi(e_G) = e_H$ ([[the preservation lemma|08FKQD7NJ3]]).
- The kernel is a [[subgroup|0X1JXT47GA]]. If $\varphi(a) = \varphi(b) = e_H$, then $\varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1} = e_H$, and the [[subgroup criterion|05N4TQKPH0]] applies.
- The kernel is normal. If $\varphi(k) = e_H$, then $\varphi(gkg^{-1}) = \varphi(g)\varphi(g)^{-1} = e_H$ ([[kernels are normal|0C9ZKYSPYR]]).
- For $a, b \in G$, $\varphi(a) = \varphi(b)$ if and only if $a \ker \varphi = b \ker \varphi$. So each nonempty fibre of $\varphi$ is a coset of the kernel.
- The map $\varphi$ is injective if and only if $\ker \varphi = \{e_G\}$ ([[injectivity and the kernel|0N2P0XRTDF]]).
- The trivial homomorphism $G \to H$ has kernel $G$.
- Each normal subgroup $N$ of $G$ is the kernel of the quotient map $G \to G/N$, $g \mapsto gN$ ([[quotient group|0KYX2N69J0]]).
- The [[first isomorphism theorem|0CXXJNG5B6]] gives $G/\ker \varphi \cong \operatorname{im} \varphi$. For finite $G$ this gives $|G| = |\ker \varphi| \cdot |\operatorname{im} \varphi|$.

### History

Galois used normal subgroups in his letter of 1832 to Auguste Chevalier.
Hölder defined quotient groups in 1889, and the normal subgroup $N$ is the kernel of the map from $G$ onto $G/N$.
Emmy Noether stated the isomorphism theorems in general form for modules in a paper of 1927 in Mathematische Annalen.

### Common errors

- The kernel is a subset of the domain $G$, not of the codomain $H$. For $\det \colon \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$, the kernel is a set of matrices, not a set of numbers.
- The kernel is the set of elements that go to the identity of $H$, and this need not be $0$. The kernel of $\det$ is the set of matrices with determinant $1$, and no matrix in $\mathrm{GL}_n(\mathbb{R})$ has determinant $0$.
- The kernel is never empty, because it contains $e_G$. A homomorphism with "no kernel" has kernel $\{e_G\}$.

## Explanations

### L1 human

A homomorphism often forgets some information.
The kernel is the part that it forgets completely: the elements that it sends to the identity.
Think of a clock with $12$ hours.
Adding $12$ hours, or $24$ hours, does not move the hands.
So the multiples of $12$ form the kernel of the map from whole numbers of hours to positions of the hour hand.
Two numbers of hours give the same position exactly when their difference is in the kernel.

### L2 human

We study $\varphi \colon \mathbb{Z}/12\mathbb{Z} \to \mathbb{Z}/4\mathbb{Z}$, $\varphi(a \bmod 12) = a \bmod 4$.

1. The map is well defined, because $4$ divides $12$. It is a homomorphism, because the remainder modulo $4$ of a sum depends only on the remainders of the summands.
2. The elements of $\mathbb{Z}/12\mathbb{Z}$ that go to $0$ are $0$, $4$ and $8$. So $\ker \varphi = \{0, 4, 8\}$.
3. The elements that go to $1$ are $1$, $5$ and $9$. This is the coset $1 + \ker \varphi$.
4. In the same way, the elements that go to $2$ are $2$, $6$, $10$, and the elements that go to $3$ are $3$, $7$, $11$.
5. The four fibres have $3$ elements each, and $12 = 3 \cdot 4 = |\ker \varphi| \cdot |\operatorname{im} \varphi|$.

The typical use of the kernel is a test for injectivity.
Since $\ker \varphi$ has $3$ elements, the map is not injective.
For instance $1$ and $5$ have the same image, and $5 - 1 = 4$ lies in the kernel.

A trap is the identity of a multiplicative group.
The exponential map $(\mathbb{R}, +) \to (\mathbb{R}_{>0}, \cdot)$ never takes the value $0$.
Its kernel is the set of $x$ with $e^x = 1$, and this set is $\{0\}$.

### L3 human

The kernel of $\varphi$ is the fibre over $e_H$, and the group structure moves this fibre onto every other nonempty fibre.
In universal algebra the kernel of a map is the congruence $\{(a, b) : \varphi(a) = \varphi(b)\}$.
For groups this congruence is fixed by the single class of $e_G$, so a normal subgroup carries the same information.
The kernels of [[ring homomorphisms|0VTH8KPCG2]] are the ideals, and the kernel of a [[linear map|0NRYHJPQG2]] is its null space.

In the [[category of groups|2CX7RPPXA9]], the inclusion $\ker \varphi \to G$ is the equalizer of $\varphi$ and the trivial homomorphism.
The sequence $\{e\} \to \ker \varphi \to G \to \operatorname{im} \varphi \to \{e\}$ is exact.
The normal subgroups of $G$ are exactly the kernels of homomorphisms with domain $G$.
