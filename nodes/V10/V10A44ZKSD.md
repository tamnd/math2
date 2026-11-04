---
tag: V10A44ZKSD
kind: proof
name: Proof of Burnside's lemma by double counting
msc: [20B05, "05E18"]
proves: 0Z47M1B2VS
uses: [08JF1K4DW1, 0RGGF8ZS6D, 00F2JFA41J, 0S19CWFZM2, 0ZC7FYE0NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Burnside's_lemma
    locator: Proof
---

## Proof

We count the set $F = \set{(g, x) \in G \times X : g \cdot x = x}$ in two ways. Both $G$ and $X$ are finite, and $X/G$ denotes the set of orbits.

1. For fixed $g$, the pairs $(g, x)$ in $F$ correspond to the points $x \in X^g$, the [[points fixed by $g$|08JF1K4DW1]]. Summing over $g$ gives $\abs{F} = \sum_{g \in G} \abs{X^g}$.
2. For fixed $x$, the pairs $(g, x)$ in $F$ correspond to the elements $g$ of the [[stabiliser|0RGGF8ZS6D]] $G_x$. Summing over $x$ gives $\abs{F} = \sum_{x \in X} \abs{G_x}$.
3. By the [[orbit size formula|0S19CWFZM2]], $\abs{G_x} = \abs{G} / \abs{G \cdot x}$ for each $x$. So $\abs{F} = \abs{G} \sum_{x \in X} \frac{1}{\abs{G \cdot x}}$.
4. The [[orbits partition|0ZC7FYE0NZ]] $X$. So we can split the sum in step 3 into one sum for each [[orbit|00F2JFA41J]] $O \in X/G$.
5. If $x \in O$, then $G \cdot x = O$, since each point lies in exactly one orbit and $x \in G \cdot x$. So the points of $O$ contribute $\sum_{x \in O} \frac{1}{\abs{O}} = 1$.
6. Hence $\sum_{x \in X} \frac{1}{\abs{G \cdot x}} = \abs{X/G}$, and $\abs{F} = \abs{G} \cdot \abs{X/G}$.
7. Comparing with step 1, $\sum_{g \in G} \abs{X^g} = \abs{G} \cdot \abs{X/G}$. Dividing by $\abs{G} \geq 1$ gives $\abs{X/G} = \frac{1}{\abs{G}} \sum_{g \in G} \abs{X^g}$.

## Idea

Count the pairs "group element, point it fixes" once by group elements and once by points. Each orbit of size $k$ has stabilisers of size $\abs{G}/k$ at its $k$ points, so it contributes exactly $\abs{G}$ to the count. Dividing by $\abs{G}$ counts the orbits.
