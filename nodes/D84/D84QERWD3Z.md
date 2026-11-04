---
tag: D84QERWD3Z
kind: proof
name: Proof that stabilisers of points in the same orbit are conjugate
msc: [20B05]
proves: 05BM304NRX
uses: [0YSE802YCQ, 0RGGF8ZS6D, 0D6WHTTH7T]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Fixed points and stabilizer subgroups
---

## Proof

We prove the two inclusions between $G_{g \cdot x}$ and $g G_x g^{-1}$. Let $e$ be the identity of $G$, and let $y = g \cdot x$.

1. Let $h \in G$. By the axioms of an [[action|0YSE802YCQ]], $(g^{-1} h g) \cdot x = g^{-1} \cdot (h \cdot (g \cdot x)) = g^{-1} \cdot (h \cdot y)$.
2. Suppose $h \in G_y$, the [[stabiliser|0RGGF8ZS6D]] of $y$. Then step 1 gives $(g^{-1} h g) \cdot x = g^{-1} \cdot y = g^{-1} \cdot (g \cdot x) = e \cdot x = x$.
3. So $g^{-1} h g \in G_x$, and $h = g (g^{-1} h g) g^{-1} \in g G_x g^{-1}$. Thus $G_y \subseteq g G_x g^{-1}$.
4. Conversely, let $k \in G_x$ and $h = g k g^{-1}$. Then $h \cdot y = (g k g^{-1}) \cdot (g \cdot x) = (g k) \cdot x = g \cdot (k \cdot x) = g \cdot x = y$.
5. So $h \in G_y$, and $g G_x g^{-1} \subseteq G_y$.
6. By steps 3 and 5, $G_{g \cdot x} = g G_x g^{-1}$, a [[conjugate subgroup|0D6WHTTH7T]] of $G_x$.

## Idea

To fix $g \cdot x$, an element may first move it back to $x$ with $g^{-1}$, fix $x$, and then move it forward again with $g$. So the stabiliser of $g \cdot x$ is the stabiliser of $x$ seen through the relabelling $g$.
