---
tag: 0C9ZKYSPYR
kind: statement
role: proposition
name: The kernel is a normal subgroup
msc: [20A05]
about: [0W88CEGQP1, 0CB0DX5BVV]
uses: [0Z424HK8CQ, 0W77CVBCHQ, 08FKQD7NJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]] and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then the [[kernel|0W88CEGQP1]] $\ker \varphi$ is a [[normal subgroup|0CB0DX5BVV]] of $G$.

## Remarks

For $g \in G$ and $k \in \ker \varphi$, $\varphi(gkg^{-1}) = \varphi(g) \, e_H \, \varphi(g)^{-1} = e_H$.
Conversely, each normal subgroup $N$ of $G$ is the kernel of the projection $G \to G/N$.
Thus the normal subgroups of $G$ are exactly the kernels of the homomorphisms from $G$.

## Explanations

### L1 human

If an element goes to the identity, then each of its conjugates also goes to the identity.
So the kernel is closed under conjugation, which is the definition of a normal subgroup.
This is one reason why normal subgroups are important.

### L2 agent

The kernel of a homomorphism $\varphi : G \to H$ is the set of $g \in G$ with $\varphi(g) = e$. The result says that the kernel is a subgroup, and that it is normal.

The proof checks two properties:

1. The kernel is a subgroup. If $\varphi(a) = \varphi(b) = e$, then $\varphi(ab^{-1}) = e\,e^{-1} = e$.
2. The kernel is closed under conjugation. If $\varphi(k) = e$, then $\varphi(gkg^{-1}) = \varphi(g)\,e\,\varphi(g)^{-1} = e$.

A worked example with the determinant $\det : \mathrm{GL}_2(\mathbb{R}) \to \mathbb{R}^\times$:

1. The kernel is $\mathrm{SL}_2(\mathbb{R})$, the matrices with determinant $1$.
2. For $A \in \mathrm{SL}_2(\mathbb{R})$ and any invertible $P$, $\det(PAP^{-1}) = \det P \cdot 1 \cdot (\det P)^{-1} = 1$.
3. Thus $PAP^{-1} \in \mathrm{SL}_2(\mathbb{R})$, and the kernel is normal.

The result has a converse. Each normal subgroup $N$ is the kernel of the projection $G \to G/N$. Thus the normal subgroups of $G$ are exactly the kernels of the homomorphisms from $G$. This is why the quotient $G/\ker\varphi$ exists in the first isomorphism theorem.

A common error is to think that the image is also normal. The image is a subgroup of $H$, but it need not be normal. The inclusion of $\{e, (1\,2)\}$ in $S_3$ is a homomorphism, and its image is not normal in $S_3$.
