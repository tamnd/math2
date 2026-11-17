---
tag: 08FKQD7NJ3
kind: statement
role: lemma
name: Homomorphisms preserve identity and inverses
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0JYTG5K9Y4]
uses: [0JYTG5K9Y4, 0VSNX4P2Q0, 0D9NDGE9KP, 00DRK90Z6K]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 1.6
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]] with identity elements $e_G$ and $e_H$.
Let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then the following hold.

1. $\varphi(e_G) = e_H$.
2. $\varphi(a^{-1}) = \varphi(a)^{-1}$ for each $a \in G$.
3. $\varphi(a^n) = \varphi(a)^n$ for each $a \in G$ and each integer $n$.

## Remarks

### Why each hypothesis is needed

- The proof of part 1 cancels $\varphi(e_G)$ in $H$, so $H$ must be a group. The zero map $x \mapsto 0$ on the monoid $(\mathbb{Z}, \cdot)$ respects products, because $0 = 0 \cdot 0$, but it sends the identity $1$ to $0$.
- For the same reason the codomain cannot be any [[monoid|0N6R902FG1]]. The map from the trivial group $\{e\}$ to the monoid $(\{0, 1\}, \cdot)$ with $e \mapsto 0$ respects products, but $0$ is not the identity $1$.
- The map must respect products. The translation $u \mapsto u + 1$ on $(\mathbb{Z}, +)$ sends $0$ to $1$ ([[a translation of the integers|3A3JJPJHQR]]).

### Consequences

- For all $a, b \in G$ we have $\varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1}$.
- The [[image|0S21GNW9ZB]] of $\varphi$ contains $e_H$ and is closed under inverses. Together with closure under products, this makes it a [[subgroup|0X1JXT47GA]] of $H$.
- The [[kernel|0W88CEGQP1]] of $\varphi$ contains $e_G$, so it is never empty.
- If $a$ has finite [[order|0WE2NHZJ7B]] $n$, then $\varphi(a)^n = \varphi(a^n) = \varphi(e_G) = e_H$. So the order of $\varphi(a)$ divides $n$ ([[the divisibility criterion for orders|0F5QC101Q7]]).
- A homomorphism from a [[cyclic group|0KVGH0J5B3]] $\langle g \rangle$ is fixed by $\varphi(g)$, because $\varphi(g^k) = \varphi(g)^k$.
- A bijective homomorphism and its inverse both preserve identities, inverses and powers ([[group isomorphism|08MG7H8JW5]]).

### Converse

The converse is false.
A map that preserves the identity and the inverses need not be a homomorphism.
The map $x \mapsto x^3$ on $(\mathbb{R}, +)$ sends $0$ to $0$ and $-x$ to $-x^3$.
But $(1 + 1)^3 = 8$, while $1^3 + 1^3 = 2$.
Part 3 does not give a homomorphism either.
Let $f(x) = x$ for rational $x$ and $f(x) = 2x$ for irrational $x$.
Then $f(nx) = nf(x)$ for each integer $n$, because $nx$ is irrational when $x$ is irrational and $n \ne 0$.
But $f(\sqrt{2}) + f(1 - \sqrt{2}) = 2\sqrt{2} + 2 - 2\sqrt{2} = 2$, while $f(1) = 1$.

### Generalizations

- For [[ring homomorphisms|0VTH8KPCG2]], the additive part of the lemma holds: $0 \mapsto 0$ and $-a \mapsto -\varphi(a)$. The multiplicative identity need not be preserved: $n \mapsto (n, 0)$ from $\mathbb{Z}$ to $\mathbb{Z} \times \mathbb{Z}$ respects sums and products, but it sends $1$ to $(1, 0)$.
- For [[linear maps|0NRYHJPQG2]], the lemma gives $T(0) = 0$ and $T(-v) = -T(v)$.
- For monoids, part 1 can fail, as the zero map on $(\mathbb{Z}, \cdot)$ shows. So a monoid homomorphism must preserve the identity by definition.

## Explanations

### L1 human

A homomorphism must respect products.
This one rule already forces it to respect the identity and the inverses.
The identity is the only element that does not change when it is multiplied by itself.
The image of the identity has the same property, so it is the identity.
For example, the exponential map turns sums into products.
It sends $0$ to $e^0 = 1$, and it sends $-x$ to $e^{-x} = 1/e^x$.

### L2 human

We compute with the homomorphism $\varphi \colon (\mathbb{Z}, +) \to (\mathbb{C}^\times, \cdot)$, $\varphi(n) = i^n$.

1. The identity of $\mathbb{Z}$ is $0$, and $\varphi(0) = i^0 = 1$. This is the identity of $\mathbb{C}^\times$, as part 1 says.
2. The inverse of $3$ in $\mathbb{Z}$ is $-3$. We get $\varphi(-3) = i^{-3} = i$, and $\varphi(3)^{-1} = (-i)^{-1} = i$. This agrees with part 2.
3. In additive notation the power $a^n$ is the multiple $na$. So part 3 says $\varphi(5 \cdot 2) = \varphi(2)^5$. Both sides are $-1$, because $i^{10} = -1$ and $(-1)^5 = -1$.

The typical use of the lemma is a quick test.
If a map does not send the identity to the identity, then it is not a homomorphism.
For example, no homomorphism $\mathbb{Z} \to \mathbb{Z}$ can send $0$ to $5$.

The trap is the other direction.
A map that sends the identity to the identity can still fail to be a homomorphism.
The map $x \mapsto x^3$ on $(\mathbb{R}, +)$ is an example.

### L3 human

The lemma says that the [[forgetful functor|WV3BPYCHVG]] from groups to monoids is full.
Each map between groups that respects products is a map of monoids, and also a group homomorphism.
The main fact is cancellation: in a group, $xx = x$ forces $x = e$.
In a monoid without cancellation this fails, so monoid homomorphisms are required to preserve the identity.

In universal algebra a group is often given with three operations: the product, the inverse and the constant $e$.
A homomorphism must then preserve all three.
The lemma shows that for groups the last two conditions follow from the first.
For this reason the [[category of groups|2CX7RPPXA9]] is the same whether groups are seen as sets with one operation or with three operations.
