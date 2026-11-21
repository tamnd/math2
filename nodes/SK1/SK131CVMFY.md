---
tag: SK131CVMFY
kind: example
name: A field and its affine group are bi-interpretable
aliases: [field-and-affine-group-bi-interpretable, affine-group-bi-interpretation]
msc: ["03C07", "03C60", "20A15"]
topics: [SZRM3N6BXW]
audience: research
instance_of: [KHZ1E7RMMQ]
uses: [ZA0RN56STN, C8NGHRR1ND, G6GMSEZDB1, TJ9G1SBBJP, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Bi-interpretability
  - url: https://en.wikipedia.org/wiki/Morley_rank
    locator: Examples
---

## Example

Let $K$ be a [[field|04C5ZBG1WT]] with at least $3$ elements, and fix $c_0 \in K$ with $c_0 \neq 0$ and $c_0 \neq 1$.
Let $G$ be the [[affine group|G6GMSEZDB1]] of pairs $(a, b)$ with $a \neq 0$, with product $(a, b)(c, d) = (a c, a d + b)$, as a pure group.
Let $t = (1, 1)$, $s = (c_0, 0)$, $A = \set{(1, b) : b \in K}$ and $H = \set{(c, 0) : c \neq 0}$.

- $\Gamma$ defines $K$ in $G$ over $t$, with domain $A$ and coordinate map $f_\Gamma(1, b) = b$, as in [[this example|C8NGHRR1ND]].
- $\Delta$ defines $G$ in $K$ without parameters, with domain $\set{(x_1, x_2) : x_1 \neq 0}$, the product formula $z_1 = x_1 y_1 \wedge z_2 = x_1 y_2 + x_2$, and $f_\Delta(a, b) = (a, b)$.

### The checks

We check that $(\Gamma, \Delta)$ is a [[bi-interpretation|ZA0RN56STN]] over the parameters $t$ and $s$.

1. $\Delta$ is a definition. The formulas copy the definition of the product, so $f_\Delta$ is an isomorphism onto $G$.
2. The [[centralizer|TJ9G1SBBJP]] of $s$ is $H$. We have $(c, d)\, s = (c c_0, d)$ and $s\, (c, d) = (c_0 c, c_0 d)$. These are equal exactly when $(1 - c_0) d = 0$, that is, $d = 0$.
3. Conjugation. For $h = (a, 0)$ we get $h\, t\, h^{-1} = (1, a)$, by the first computation of the example above.
4. Composite in $K$. A pair $(a, b) \in K^2$ is in its domain when $(a, b) \in A$, that is, $a = 1$. It maps to $f_\Gamma(1, b) = b$. The graph is defined by $x_1 = 1 \wedge y = x_2$, without parameters.
5. Composite in $G$. A pair $(x, y) \in A^2$ with $x = (1, a)$, $y = (1, b)$ and $a \neq 0$ maps to $f_\Delta(a, b) = (a, b)$.
6. Its graph. For $h = (a, 0)$, we get $y\, h = (1, b)(a, 0) = (a, b)$. By steps 2 and 3, $h$ is the unique element of $C_G(s)$ with $h t h^{-1} = x$.
7. So the graph is defined by $x t = t x \wedge y t = t y \wedge x \neq e \wedge \exists h \, (h s = s h \wedge h t h^{-1} = x \wedge g = y h)$.

So $K$ and $G$ are bi-interpretable with the parameters $t$ and $s$.

## Remarks

The parameters are needed for this bi-interpretation: the domain $A$ of $\Gamma$ is $\emptyset$-definable, as the set of commutators $g h g^{-1} h^{-1}$, but $t$ is not, since every element of $A \setminus \set{e}$ is a conjugate of $t$.

For $K$ algebraically closed, the bi-interpretation computes the rank of $G$.
The definable sets of $G$ and of $K^\times \times K$ in $K$ correspond, so $G$ has Morley rank $2$, the Morley rank of $K^2$.

For $K = \mathbb{F}_2$ there is no $c_0$, but every $x \neq e$ in $A$ is $t$, so $a = 1$ in step 5.
Then the graph is defined by $x = t \wedge g = y$, and so every field is bi-interpretable with its affine group.

## Explanations

### L1 human

The maps $x \mapsto a x + b$ of a line form a group.
From this group we can rebuild the numbers: the shifts $x \mapsto x + b$ stand for the numbers $b$.
From the numbers we can rebuild the group, as pairs $(a, b)$.
The round trips are rules of the group and of the numbers, so the group and the field carry the same information.

### L2 human

We follow one group element through the round trip in $G$, for $K = \mathbb{Q}$ and $c_0 = 2$.

1. Take $g = (3, 4)$. Under $\Delta$, it is the pair $(3, 4)$ of numbers.
2. Under $\Gamma$, the numbers $3$ and $4$ are the shifts $x = (1, 3)$ and $y = (1, 4)$.
3. The element $h = (3, 0)$ commutes with $s = (2, 0)$, and $h t h^{-1} = (1, 3) = x$.
4. Then $y h = (1, 4)(3, 0) = (3, 4) = g$, so the graph formula holds at $(x, y, g)$.

The typical use is to transfer model theoretic invariants, such as Morley rank, between a group and a field.
A trap is to drop the condition $x \neq e$: the pair $(0, b)$ is not in the domain of $\Delta$.
