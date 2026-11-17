---
tag: 0JYTG5K9Y4
kind: concept
name: Group homomorphism
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Examples
  - book: isbn:9780471433347
    locator: Section 1.6
same_as:
  wikidata: Q868169
  wikipedia: Group homomorphism
inventory: [JJGY7QTXXR]
---

## Summary

Let $G$ and $H$ be [[groups|G5S1M9]].
A group homomorphism from $G$ to $H$ is a map $\varphi \colon G \to H$ such that $\varphi(ab) = \varphi(a)\varphi(b)$ for all $a, b \in G$.
In this equation the product $ab$ is computed in $G$, and the product $\varphi(a)\varphi(b)$ is computed in $H$.
No other condition is needed, because such a map also [[preserves the identity and the inverses|08FKQD7NJ3]].
Homomorphisms are the maps that compare two groups, and the kernels, images, quotients and isomorphisms of group theory are all defined with them.

## Motivation

Many groups come in pairs that behave in the same way.
Take an integer and keep only its parity.
An even number plus an odd number is odd, and two odd numbers add to an even number.
So the parity of a sum depends only on the parities of the two summands.
The map $n \mapsto (-1)^n$ from $(\mathbb{Z}, +)$ to the group $\{1, -1\}$ under multiplication records this fact: $(-1)^{m+n} = (-1)^m (-1)^n$.
Logarithm tables use the same pattern in the other direction: the logarithm turns a product of positive numbers into a sum.
A homomorphism is a map that carries the operation of one group to the operation of another group.
With such a map, a computation in one group gives information about the other group.

## Notation

We write $\varphi \colon G \to H$, and $e_G$ and $e_H$ for the identity elements.
When a group is written additively, the condition changes its form.
For $\varphi \colon (\mathbb{Z}, +) \to (\mathbb{Z}, +)$ it reads $\varphi(a + b) = \varphi(a) + \varphi(b)$.
For $\exp \colon (\mathbb{R}, +) \to (\mathbb{R}_{>0}, \times)$ it reads $\exp(a + b) = \exp(a)\exp(b)$.
The set of all homomorphisms from $G$ to $H$ is written $\operatorname{Hom}(G, H)$.
A homomorphism from $G$ to itself is an endomorphism.
Some books call an injective homomorphism a [[monomorphism|Y2NP1JFR86]] and a surjective homomorphism an [[epimorphism|RVXDSY04KG]].

## Remarks

### Examples

- Reduction modulo $n$, the map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $u \mapsto u \bmod n$, is a homomorphism. The sum of two remainders is the remainder of the sum, after reduction ([[reduction modulo n|BV08DGBD7C]]).
- The [[determinant|00KDZRW4C0]] $\det \colon \mathrm{GL}_n(F) \to F^\times$ is a homomorphism, because $\det(AB) = \det(A)\det(B)$ ([[determinant as a homomorphism|0YZ3T5Q7XN]]).
- The [[sign of a permutation|02DKV69ZH0]] $\operatorname{sgn} \colon S_n \to \{1, -1\}$ is a homomorphism, because the sign of a product is the product of the signs ([[sign is a homomorphism|0JEJJCB0EX]]).
- The [[exponential function|0J0FCWV32D]] is a homomorphism from $(\mathbb{R}, +)$ to $(\mathbb{R}_{>0}, \times)$, because $e^{a+b} = e^a e^b$ ([[the exponential map|7GEXM87S0H]]).
- For all groups $G$ and $H$, the map $g \mapsto e_H$ is a homomorphism, because $e_H = e_H e_H$. It is the trivial homomorphism.
- Doubling, $u \mapsto 2u$ on $(\mathbb{Z}, +)$, is a homomorphism, because $2(u + v) = 2u + 2v$ ([[doubling on the integers|PVR5EX71PD]]).

### Non-examples

- The translation $u \mapsto u + 1$ on $(\mathbb{Z}, +)$ is not a homomorphism. The condition fails for $a = b = 0$: the left side is $1$ and the right side is $2$ ([[a translation of the integers|3A3JJPJHQR]]).
- The map $x \mapsto x^2$ on $(\mathbb{R}, +)$ is not a homomorphism. For $a = b = 1$ we get $(1 + 1)^2 = 4$, but $1^2 + 1^2 = 2$.
- The squaring map $g \mapsto g^2$ on the [[symmetric group|0515A6D2Y1]] $S_3$ is not a homomorphism. Compose from right to left: for $a = (1\,2)$ and $b = (1\,3)$ we get $ab = (1\,3\,2)$, so $(ab)^2 = (1\,2\,3)$, but $a^2 b^2 = e$.
- The map $\mathbb{Z}/2\mathbb{Z} \to \mathbb{Z}$ with $0 \mapsto 0$ and $1 \mapsto 1$ is not a homomorphism. In $\mathbb{Z}/2\mathbb{Z}$ we have $1 + 1 = 0$, which goes to $0$, but $1 + 1 = 2$ in $\mathbb{Z}$.

### Basic properties

- A homomorphism sends $e_G$ to $e_H$, sends $a^{-1}$ to $\varphi(a)^{-1}$, and sends $a^n$ to $\varphi(a)^n$ for each integer $n$ ([[the preservation lemma|08FKQD7NJ3]]).
- The composite of two homomorphisms $\varphi \colon G \to H$ and $\psi \colon H \to K$ is a homomorphism. The reason is $\psi(\varphi(ab)) = \psi(\varphi(a)\varphi(b)) = \psi(\varphi(a))\psi(\varphi(b))$.
- The [[kernel|0W88CEGQP1]] $\ker \varphi$ is a [[normal subgroup|0CB0DX5BVV]] of $G$ ([[kernels are normal|0C9ZKYSPYR]]).
- The [[image|0S21GNW9ZB]] $\operatorname{im} \varphi$ is a [[subgroup|0X1JXT47GA]] of $H$.
- The map $\varphi$ is injective if and only if $\ker \varphi = \{e_G\}$ ([[injectivity and the kernel|0N2P0XRTDF]]).
- If $a$ has finite [[order|0WE2NHZJ7B]] $n$, then the order of $\varphi(a)$ divides $n$. The reason is $\varphi(a)^n = \varphi(a^n) = e_H$, together with [[the divisibility criterion for orders|0F5QC101Q7]].
- A homomorphism from a [[cyclic group|0KVGH0J5B3]] $\langle g \rangle$ is fixed by its value at $g$. The reason is $\varphi(g^k) = \varphi(g)^k$ for each integer $k$.
- The [[first isomorphism theorem|0CXXJNG5B6]] gives $G/\ker \varphi \cong \operatorname{im} \varphi$.

### History

The word comes from the Greek words homos, "same", and morphe, "shape".
Hölder defined quotient groups in 1889, and each quotient group $G/N$ is the image of the homomorphism $g \mapsto gN$.
Eilenberg and Mac Lane introduced categories in 1945, and groups with their homomorphisms became a standard example of a category.

### Common errors

- It is not enough to check that $\varphi(e_G) = e_H$. The map $x \mapsto x^2$ on $(\mathbb{R}, +)$ sends $0$ to $0$, but it is not a homomorphism.
- The operations on the two sides can be different. For the exponential map the condition is $e^{a+b} = e^a e^b$, and not $e^{a+b} = e^a + e^b$.
- A value at a generator does not always give a homomorphism. A homomorphism $\mathbb{Z}/2\mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}$ with $1 \mapsto 1$ would send $0 = 1 + 1$ to $1 + 1 = 2$, but it must send $0$ to $0$.

## Explanations

### L1 human

A homomorphism is a translation from one group to another group that keeps the rule of combination.
Combining two elements and then translating gives the same result as translating first and then combining.
Here is a small instance.
Send each whole number to the word "even" or the word "odd".
The numbers $3$ and $5$ are both odd, and their sum $8$ is even.
The rule "odd plus odd is even" predicts this without the actual sum.
So the parity map is a homomorphism from the integers to a group with two elements.

### L2 human

We study the map $\varphi \colon \mathbb{Z}/6\mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}$, $\varphi(a \bmod 6) = a \bmod 3$.

1. The map is well defined. If $a \equiv b \pmod 6$, then $6$ divides $a - b$. Since $3$ divides $6$, also $3$ divides $a - b$, so $a \equiv b \pmod 3$.
2. The map is a homomorphism. The class of $a + b$ modulo $6$ goes to $(a + b) \bmod 3$, and this is $(a \bmod 3) + (b \bmod 3)$ in $\mathbb{Z}/3\mathbb{Z}$.
3. We list the values: $0 \mapsto 0$, $1 \mapsto 1$, $2 \mapsto 2$, $3 \mapsto 0$, $4 \mapsto 1$ and $5 \mapsto 2$.
4. The elements that go to $0$ are $0$ and $3$. So the kernel is $\{0, 3\}$.
5. Each element of $\mathbb{Z}/3\mathbb{Z}$ is a value. So the map is surjective.

The typical use of a homomorphism is to move a question to a simpler group.
For example, the [[sign|02DKV69ZH0]] sends each transposition to $-1$.
So a product of an odd number of transpositions has sign $-1$, and it is never the identity permutation.

A trap is a formula that is not well defined.
The rule $a \bmod 6 \mapsto a \bmod 4$ does not define a map on $\mathbb{Z}/6\mathbb{Z}$.
The integers $0$ and $6$ give the same class modulo $6$, but $0 \bmod 4 = 0$ and $6 \bmod 4 = 2$.
Before we check the homomorphism condition, we must check that the formula gives one value for each class.

### L3 human

Group homomorphisms are the morphisms of the [[category of groups|2CX7RPPXA9]].
The same idea appears for each algebraic structure: [[ring homomorphisms|0VTH8KPCG2]] preserve sums and products, and [[linear maps|0NRYHJPQG2]] preserve sums and scalar multiples.
For groups, a map of the underlying [[monoids|0N6R902FG1]] or even of the underlying semigroups is already a group homomorphism, because cancellation forces the identity and the inverses to be preserved.
A homomorphism from $G$ to the group of permutations of a set $X$ is the same thing as a [[group action|0WCY42EV9V]] of $G$ on $X$.
A homomorphism from $G$ to $\mathrm{GL}_n(F)$ is a linear representation of $G$.

When $A$ is an abelian group, $\operatorname{Hom}(G, A)$ is a group under the pointwise product $(\varphi\psi)(g) = \varphi(g)\psi(g)$.
Each homomorphism from $G$ to an abelian group factors through the [[abelianisation|0AQZV0905N]] of $G$.
The [[first isomorphism theorem|0CXXJNG5B6]] says that each homomorphism is a quotient map followed by an injective map.
This splits the study of homomorphisms into the study of [[normal subgroups|0CB0DX5BVV]] and the study of subgroups.
