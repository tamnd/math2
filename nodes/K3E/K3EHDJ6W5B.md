---
tag: K3EHDJ6W5B
kind: proof
name: Proof of the orbit-stabiliser theorem
msc: [20B05]
proves: 0E2HSCKZ6C
uses: [0YSE802YCQ, 00F2JFA41J, 0RGGF8ZS6D, 05FD317V2W, 04QEBF8S49, 05N4TQKPH0]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Orbit–stabilizer theorem
---

## Proof

We prove that $g \cdot x = h \cdot x$ exactly when $g G_x = h G_x$. Let $e$ be the identity of $G$, and let $H = G_x$ be the [[stabiliser|0RGGF8ZS6D]] of $x$.

The set $H$ is a subgroup of $G$, by the [[subgroup criterion|05N4TQKPH0]]. First, $e \cdot x = x$, so $e \in H$. If $a, b \in H$, then $b^{-1} \cdot x = b^{-1} \cdot (b \cdot x) = e \cdot x = x$. So $(a b^{-1}) \cdot x = a \cdot (b^{-1} \cdot x) = x$, and $a b^{-1} \in H$.

1. Let $g, h \in G$. By the axioms of an [[action|0YSE802YCQ]], $g \cdot x = h \cdot x$ implies $(g^{-1} h) \cdot x = g^{-1} \cdot (h \cdot x) = g^{-1} \cdot (g \cdot x) = e \cdot x = x$. So $g^{-1} h \in H$.
2. Conversely, if $g^{-1} h \in H$, then $h \cdot x = (g g^{-1} h) \cdot x = g \cdot ((g^{-1} h) \cdot x) = g \cdot x$. So $g \cdot x = h \cdot x$ if and only if $g^{-1} h \in H$.
3. Next, if $g^{-1} h = k \in H$, then $h = g k$. Each element of $h H$ is $g k k'$ with $k' \in H$, and $k k' \in H$. So $h H \subseteq g H$.
4. In the same way, $h^{-1} g = k^{-1} \in H$ gives $g H \subseteq h H$. So $g^{-1} h \in H$ implies $g H = h H$.
5. Conversely, if $g H = h H$, then $h = h e \in h H = g H$. So $h = g k$ for some $k \in H$, and $g^{-1} h = k \in H$.
6. By steps 2 to 5, $g \cdot x = h \cdot x$ if and only if the [[left cosets|05FD317V2W]] $g H$ and $h H$ are equal.
7. Define $\Phi(g H) = g \cdot x$. By the direction "equal cosets give equal points" of step 6, the value does not depend on the representative $g$. So $\Phi$ is well defined.
8. By the other direction of step 6, $\Phi(g H) = \Phi(h H)$ implies $g H = h H$. So $\Phi$ is injective.
9. Each point of the [[orbit|00F2JFA41J]] $G \cdot x$ has the form $g \cdot x = \Phi(g H)$. So $\Phi$ maps the set of left cosets of $H$ onto $G \cdot x$.
10. Hence $\Phi$ is a bijection from the set of left cosets of $G_x$ to $G \cdot x$. By the [[definition of the index|04QEBF8S49]], $\abs{G \cdot x} = [G : G_x]$.

## Idea

Two group elements move $x$ to the same point exactly when they differ by an element that fixes $x$. That is the same as lying in the same left coset of the stabiliser. So the points of the orbit match the cosets one to one.
