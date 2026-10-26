---
tag: 0C9ZKYSPYR
kind: statement
role: proposition
name: The kernel is a normal subgroup
msc: [20A05]
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
