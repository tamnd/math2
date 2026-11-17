---
tag: 0N2P0XRTDF
kind: statement
role: theorem
name: A homomorphism is injective iff its kernel is trivial
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0JYTG5K9Y4, 0W88CEGQP1]
uses: [0JYTG5K9Y4, 0W88CEGQP1, 08FKQD7NJ3, 09NWETVTNY]
formal:
  - system: lean4
    library: mathlib
    decl: MonoidHom.ker_eq_bot_iff
    match: stronger
    adapter: Math2.Match.injective_iff_ker
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Image and kernel
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]], let $e_G$ be the identity element of $G$, and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then $\varphi$ is [[injective|09NWETVTNY]] if and only if its [[kernel|0W88CEGQP1]] is $\ker \varphi = \{e_G\}$.

## Remarks

### Why each hypothesis is needed

- The map must be a homomorphism. The map $x \mapsto x^2$ on $(\mathbb{R}, +)$ sends only $0$ to $0$, but it sends $1$ and $-1$ to the same value $1$.
- The domain must be a group, because the proof uses the inverse $a^{-1}$. The map $f \colon (\mathbb{N}, +) \to (\{0, 1\}, \max)$ with $f(0) = 0$ and $f(n) = 1$ for $n \ge 1$ shows this.
- This $f$ respects the operations and sends the identity $0$ to the identity $0$. Only $0$ goes to $0$, but $f(1) = f(2)$.
- The codomain $H$ needs only an identity element and a product. The proof never uses an inverse in $H$.

### Consequences

- For $a, b \in G$, $\varphi(a) = \varphi(b)$ holds if and only if $a^{-1}b \in \ker \varphi$. Steps 4 and 5 of [[the proof|D05NAAC3XK]] give one direction, and $\varphi(b) = \varphi(a)\varphi(a^{-1}b)$ gives the other.
- So $\varphi(a) = \varphi(b)$ if and only if $a \ker \varphi = b \ker \varphi$ ([[left coset|03DEH43F4H]]). Each nonempty fibre $\varphi^{-1}(\{h\})$ is a left coset of $\ker \varphi$.
- Since $\ker \varphi$ is [[normal|0C9ZKYSPYR]], each nonempty fibre is also a right coset of $\ker \varphi$.
- The fibres are in bijection with the elements of $\operatorname{im} \varphi$. So $|\operatorname{im} \varphi| = [G : \ker \varphi]$, the [[index|0DTXBQPA2S]] of the kernel.
- A homomorphism from a [[simple group|0YMYMNQ0QZ]] is trivial or injective, because its kernel is a normal subgroup.
- A homomorphism from $\mathbb{Z}/p\mathbb{Z}$, with $p$ prime, is trivial or injective. By [[Lagrange's theorem|3C53TD]], its kernel has order $1$ or $p$.
- A homomorphism is an [[isomorphism|08MG7H8JW5]] if and only if its kernel is $\{e_G\}$ and its image is $H$.

### Converse

The theorem is an equivalence, so its converse is part of the statement.
A trivial kernel does not give surjectivity.
Doubling $u \mapsto 2u$ on $\mathbb{Z}$ has kernel $\{0\}$, but its image is $2\mathbb{Z}$ ([[doubling on the integers|PVR5EX71PD]]).

### Generalizations

- For a [[ring homomorphism|0VTH8KPCG2]], injectivity holds if and only if the kernel is $\{0\}$. The proof applies to the additive groups.
- For a [[linear map|0NRYHJPQG2]] $T$, injectivity holds if and only if the null space is $\{0\}$.
- For monoid homomorphisms the result fails, as the map $f$ above shows.
- In universal algebra, a map is injective if and only if its kernel congruence $\{(a, b) : \varphi(a) = \varphi(b)\}$ is the equality relation. For groups the classes of this congruence are the cosets of $\ker \varphi$.

## Explanations

### L1 human

For a general function, injectivity needs a check of each pair of points.
For a homomorphism one check is enough: find the elements that go to the identity.
If only the identity goes to the identity, then no two elements go to the same place.
The reason is that two elements with the same image differ by an element of the kernel.
So the test on one fibre gives the answer for all fibres.

### L2 human

We test the homomorphism $\varphi \colon \mathbb{Z} \to \mathbb{Z}$, $\varphi(n) = 3n$.

1. The map is a homomorphism, because $3(m + n) = 3m + 3n$.
2. If $3n = 0$, then $n = 0$. So $\ker \varphi = \{0\}$.
3. By the theorem, $\varphi$ is injective, with no need to compare pairs.

Now we test reduction modulo $3$, $\psi \colon \mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}$.

1. The kernel is $3\mathbb{Z} = \{\dots, -3, 0, 3, 6, \dots\}$, and it is not $\{0\}$.
2. So $\psi$ is not injective. For instance $\psi(0) = \psi(3) = 0$.
3. The fibre over $1$ is $\{\dots, -2, 1, 4, 7, \dots\} = 1 + 3\mathbb{Z}$, a coset of the kernel.

The typical use is a fast proof of injectivity.
For $k \mapsto 2^k \bmod 5$ from $\mathbb{Z}/4\mathbb{Z}$ to $(\mathbb{Z}/5\mathbb{Z})^\times$, the values at $1, 2, 3$ are $2, 4, 3$.
So only $0$ goes to $1$, and the map is injective.
A common error is to apply the test to a map that is not a homomorphism.
The map $x \mapsto x^2$ on $\mathbb{R}$ sends only $0$ to $0$, but it is not injective.

### L3 human

The theorem shows that the kernel controls all the fibres of a homomorphism.
The group $G$ acts on itself by left multiplication, and this action moves the fibre over $e_H$ onto each nonempty fibre.
So the partition of $G$ into fibres is fixed by one normal subgroup, the kernel.
The [[first isomorphism theorem|0CXXJNG5B6]] states this in the form $G/\ker \varphi \cong \operatorname{im} \varphi$.

In the [[category of groups|2CX7RPPXA9]], the [[monomorphisms|Y2NP1JFR86]] are the injective homomorphisms, and these are the maps with trivial kernel.
For monoids the fibre over the identity does not control the other fibres, as the map $f$ above shows.
