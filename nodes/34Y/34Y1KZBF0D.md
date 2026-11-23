---
tag: 34Y1KZBF0D
kind: example
name: A bimodal frame that is not a product
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: JA2EBWVW8A
    note: the frame refutes the Church-Rosser formula, which is valid in every product frame
uses: [JA2EBWVW8A, 1GA9KST2HQ, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Multimodal_logic
    locator: Overview
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

From a point $w$, one arrow of type 1 leads to $a$ and one arrow of type 2 leads to $b$, and nothing else happens.
In a grid the two arrows would close into a square, with a corner reached from $a$ by type 2 and from $b$ by type 1.
Here that corner is missing, and one formula detects it.

Let $W = \{w, a, b\}$, $R_1 = \{(w, a)\}$ and $R_2 = \{(w, b)\}$.
This is a bimodal [[Kripke frame|NGHWZ9Y7ZV]], with $\square_1$ along $R_1$ and $\square_2$ along $R_2$.
We show that it refutes $\mathrm{chr} = \lozenge_1 \square_2 p \to \square_2 \lozenge_1 p$, so it is not isomorphic to a [[product frame|JA2EBWVW8A]].

1. Let $V(p) = \emptyset$.
2. The point $a$ has no $R_2$-successor, so $a \models \square_2 p$.
3. Since $w R_1 a$, we get $w \models \lozenge_1 \square_2 p$.
4. The point $b$ has no $R_1$-successor, so $b \not\models \lozenge_1 p$.
5. Since $w R_2 b$, we get $w \not\models \square_2 \lozenge_1 p$.
6. So $\mathrm{chr}$ fails at $w$.
7. The formula $\mathrm{chr}$ is valid in every product frame, by [[commutativity and the Church-Rosser property in product frames|1GA9KST2HQ]].
8. Validity is preserved by isomorphism, so the frame is not isomorphic to a product.
   It does not validate $\mathsf{K} \times \mathsf{K}$ either, since $\mathrm{chr} \in \mathsf{K} \times \mathsf{K}$.

## Remarks

The frame fails the square condition: the arrows from $w$ to $a$ and to $b$ have no common completion $t$ with $a R_2 t$ and $b R_1 t$.
Adding a point $t$ with $a R_2 t$ and $b R_1 t$ repairs this defect.
The result is the product of two two-element chains, with $w = (0, 0)$, $a = (1, 0)$, $b = (0, 1)$ and $t = (1, 1)$.
The frame still validates the fusion $\mathsf{K} \otimes \mathsf{K}$, as every bimodal frame does.

## Explanations

### L1 human

From a starting point, one road leads east and another road leads north.
In a grid, going north from the east point and going east from the north point meet at a common corner.
Here the two roads lead to dead ends, so the corner is missing, and the map is not a grid.

### L2 human

The frame also satisfies $\mathrm{com} = \square_1 \square_2 p \leftrightarrow \square_2 \square_1 p$.
The composition $R_1$ then $R_2$ is empty, because $a$ has no $R_2$-successor.
The composition $R_2$ then $R_1$ is empty, because $b$ has no $R_1$-successor.
So both sides of $\mathrm{com}$ are true at every point, under every valuation.
The typical use of $\mathrm{chr}$ is to show that a given two-dimensional frame cannot be a product.
Watch out: $\mathrm{com}$ alone does not detect products, and this frame passes it while failing $\mathrm{chr}$.
