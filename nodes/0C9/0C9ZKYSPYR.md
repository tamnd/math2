---
tag: 0C9ZKYSPYR
kind: statement
role: theorem
name: Kernels are normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0W88CEGQP1, 0CB0DX5BVV]
uses: [0JYTG5K9Y4, 0W88CEGQP1, 0CB0DX5BVV, 08FKQD7NJ3]
formal:
  - system: lean4
    library: mathlib
    decl: MonoidHom.normal_ker
    match: stronger
    adapter: Math2.Match.ker_normal
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Normal subgroups, quotient groups and homomorphisms
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]] and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then the [[kernel|0W88CEGQP1]] $\ker\varphi = \{g \in G : \varphi(g) = e_H\}$ is a [[normal subgroup|0CB0DX5BVV]] of $G$.

## Remarks

The proof is short.
For $g \in G$ and $k \in \ker\varphi$, $\varphi(gkg^{-1}) = \varphi(g) \, e_H \, \varphi(g)^{-1} = e_H$, so $gkg^{-1} \in \ker\varphi$.

### Why each hypothesis is needed

The map $\varphi$ must be a homomorphism.
Let $H_0 = \{e, (1\,2)\}$ in $S_3$, with composition from right to left.
Define $f \colon S_3 \to \{1, -1\}$ by $f(x) = 1$ for $x \in H_0$ and $f(x) = -1$ for the other four elements.
The set $f^{-1}(1) = H_0$ is a subgroup, but it is not normal, because $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3)$.
This $f$ is not a homomorphism: $(1\,3)(2\,3) = (1\,3\,2)$, so $f((1\,3)(2\,3)) = -1$, but $f((1\,3))f((2\,3)) = 1$.

### Consequences

- The [[alternating group|0Z5905Q73D]] $A_n$ is normal in $S_n$, because it is the kernel of the sign homomorphism ([[sign is a homomorphism|0JEJJCB0EX]]).
- $\mathrm{SL}_n(F)$ is normal in $\mathrm{GL}_n(F)$, because it is the kernel of the determinant ([[the special linear group is the kernel of the determinant|556HZEYCQF]]).
- The [[centre|0DZ93493VN]] of $G$ is normal, because it is the kernel of the homomorphism $G \to \operatorname{Aut}(G)$, $g \mapsto c_g$, where $c_g(x) = gxg^{-1}$.
- The [[normal core|0GETX79CJN]] of a subgroup $K$ is normal, because it is the kernel of the action of $G$ on the left cosets of $K$.
- A homomorphism from a [[simple group|0YMYMNQ0QZ]] $G$ is either injective or trivial. Its kernel is normal, so it is $\{e\}$ or $G$, and a trivial kernel means injective ([[injective iff kernel trivial|0N2P0XRTDF]]).

### Converse

The converse is true: each normal subgroup is a kernel.
Let $N \trianglelefteq G$, and let $\pi \colon G \to G/N$, $\pi(g) = gN$, be the projection to the [[quotient group|0KYX2N69J0]].
Then $\pi$ is a homomorphism, and $\pi(g) = N$ exactly when $gN = N$, that is, when $g \in N$.
So $\ker\pi = N$.
Thus the normal subgroups of $G$ are exactly the kernels of the homomorphisms from $G$.

### Generalizations

- The kernel of a [[ring homomorphism|0VTH8KPCG2]] is a two-sided ideal, and each two-sided ideal is a kernel.
- The kernel of a [[linear map|0NRYHJPQG2]] is a subspace, and each subspace is a kernel.
- In universal algebra, the kernel of a homomorphism is a congruence, that is, an equivalence relation compatible with the operations.

## History

Hölder defined quotient groups in 1889, and with them the projection $G \to G/N$ whose kernel is $N$.
Noether stated the isomorphism theorems in general form for modules in 1927, in Mathematische Annalen.

## Explanations

### L1 human

A homomorphism is a map between groups that respects the multiplication.
The kernel is the set of elements that the map sends to the identity.
If an element goes to the identity, then each of its conjugates also goes to the identity.
So the kernel is closed under conjugation, and this is the definition of a normal subgroup.

### L2 human

We check the theorem for the determinant $\det \colon \mathrm{GL}_2(\mathbb{R}) \to \mathbb{R}^\times$.
It is a homomorphism, because $\det(AB) = \det(A)\det(B)$.

1. The kernel is $\mathrm{SL}_2(\mathbb{R})$, the set of matrices with determinant $1$.
2. Let $A \in \mathrm{SL}_2(\mathbb{R})$ and $P \in \mathrm{GL}_2(\mathbb{R})$.
3. Then $\det(PAP^{-1}) = \det(P) \cdot 1 \cdot \det(P)^{-1} = 1$.
4. So $PAP^{-1} \in \mathrm{SL}_2(\mathbb{R})$, and the kernel is normal.

The theorem is the quickest way to prove that a subgroup is normal: find a homomorphism with this subgroup as its kernel.
For $A_n$ in $S_n$, the homomorphism is the sign.

A common error is to think that the image is also normal.
The image of a homomorphism is a subgroup of the target, but it need not be normal.
The inclusion of $\{e, (1\,2)\}$ in $S_3$ is a homomorphism, and its image is not normal in $S_3$.

### L3 human

The theorem and its converse identify normal subgroups with kernels.
The [[first isomorphism theorem|0CXXJNG5B6]] then says that each homomorphic image of $G$ is a quotient $G/N$.
So the normal subgroups of $G$ describe all the homomorphic images of $G$ up to isomorphism.
In the category of groups, the kernel of $\varphi$ is the equaliser of $\varphi$ and the trivial homomorphism.
The kernels in this sense are exactly the inclusions of normal subgroups.
For rings, the same role belongs to two-sided ideals, and a one-sided ideal is in general not a kernel.
