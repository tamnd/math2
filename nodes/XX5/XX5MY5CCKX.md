---
tag: XX5MY5CCKX
kind: definition
name: Enriched category
msc: [18D20]
defines: BPH9SJ30Y0
uses: [M3MSQ3NKAE, A2DE66937D, SC6FD5F4J0, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Enriched_category
---

## Definition

Let $(\mathcal{V}, \otimes, I, \alpha, \lambda, \rho)$ be a [[monoidal category|M3MSQ3NKAE]].
A *$\mathcal{V}$-enriched category* (or $\mathcal{V}$-category) $\mathcal{C}$ consists of:

1. a class $\mathrm{Ob}(\mathcal{C})$ of objects;
2. for each pair of objects $a, b$, an object $\mathcal{C}(a, b)$ of $\mathcal{V}$, the hom-object;
3. for each triple $a, b, c$, a morphism $M_{a,b,c} \colon \mathcal{C}(b, c) \otimes \mathcal{C}(a, b) \to \mathcal{C}(a, c)$ of $\mathcal{V}$, the composition;
4. for each object $a$, a morphism $j_a \colon I \to \mathcal{C}(a, a)$ of $\mathcal{V}$, the identity.

These data satisfy, for all objects $a, b, c, d$:

1. associativity: $M_{a,b,d} \circ (M_{b,c,d} \otimes \id) = M_{a,c,d} \circ (\id \otimes M_{a,b,c}) \circ \alpha$ as morphisms $(\mathcal{C}(c, d) \otimes \mathcal{C}(b, c)) \otimes \mathcal{C}(a, b) \to \mathcal{C}(a, d)$;
2. units: $M_{a,b,b} \circ (j_b \otimes \id) = \lambda$ and $M_{a,a,b} \circ (\id \otimes j_a) = \rho$ as morphisms $I \otimes \mathcal{C}(a, b) \to \mathcal{C}(a, b)$ and $\mathcal{C}(a, b) \otimes I \to \mathcal{C}(a, b)$.

## Remarks

Example: for $\mathcal{V} = (\mathbf{Set}, \times, \set{*})$, a $\mathcal{V}$-category is a locally small [[category|A2DE66937D]]; for $\mathcal{V} = (\mathbf{Ab}, \otimes, \Z)$, it is a [[preadditive category|SC6FD5F4J0]].
Example: let $\mathcal{V} = [0, \infty]$, with a morphism $x \to y$ exactly when $x \ge y$, tensor product $+$ and unit $0$.
A $\mathcal{V}$-category is a set $X$ with numbers $d(x, y)$ such that $d(y, z) + d(x, y) \ge d(x, z)$ (composition) and $0 \ge d(x, x)$ (identities), so every [[metric space|0VKD1TP7F3]] is one.
Non-example: on $\R$, the function $d(x, y) = (x - y)^2$ does not give a $[0, \infty]$-category: composition fails, since $d(0, 1) + d(1, 2) = 2$ is less than $d(0, 2) = 4$.
The associativity and unit axioms are automatic in this example, because $[0, \infty]$ is a preorder.
