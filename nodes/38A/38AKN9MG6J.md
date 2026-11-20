---
tag: 38AKN9MG6J
kind: example
name: Three lines in the plane
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [0JMTY8MF54]
uses: [0RMKABS2S5, 06HTJNCMPA]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Lattice of subspaces
  - url: https://en.wikipedia.org/wiki/Modular_lattice
    locator: Examples
---

## Example

In $\R^2$, let $L_1 = \operatorname{span}((1, 0))$, $L_2 = \operatorname{span}((0, 1))$ and $L_3 = \operatorname{span}((1, 1))$.
Each line has dimension $1$, and two different lines through $0$ meet only in $0$.

1. $L_1 + L_2 = \R^2$, because $(a, b) = (a, 0) + (0, b)$.
2. In the same way, $L_1 + L_3 = \R^2$ and $L_2 + L_3 = \R^2$: for example $(a, b) = (a - b, 0) + (b, b)$.
3. $L_1 \cap L_2 = L_1 \cap L_3 = L_2 \cap L_3 = \set{0}$.
4. $L_1 + L_2 + L_3 = \R^2$, of dimension $2$.

The [[sum of subspaces|0RMKABS2S5]] does not distribute over the intersection:

5. $L_3 \cap (L_1 + L_2) = L_3 \cap \R^2 = L_3$.
6. $(L_3 \cap L_1) + (L_3 \cap L_2) = \set{0} + \set{0} = \set{0}$.
7. Since $L_3 \ne \set{0}$, the two sides differ.

Inclusion-exclusion fails for three subspaces:

8. The formula $\dim L_1 + \dim L_2 + \dim L_3 - \dim(L_1 \cap L_2) - \dim(L_1 \cap L_3) - \dim(L_2 \cap L_3) + \dim(L_1 \cap L_2 \cap L_3)$ gives $1 + 1 + 1 - 0 - 0 - 0 + 0 = 3$.
9. The true value is $\dim(L_1 + L_2 + L_3) = 2$.

## Remarks

For two subspaces, [[Grassmann's formula|06HTJNCMPA]] $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$ holds; this example shows that it does not extend to three.
The subspace lattice is still modular: if $U \subseteq X$, then $X \cap (U + W) = U + (X \cap W)$; the example above has no inclusion among $L_1, L_2, L_3$.
The same three lines show that $\R^2$ has no unique complement: $L_2$ and $L_3$ are both complements of $L_1$.

## Explanations

### L1 human

Three different lines through the origin in the plane are like three spokes.
Any two of them already fill the whole plane.
So counting "1 + 1 + 1" gives too much, because the plane has only dimension $2$.

### L2 human

The lesson is that subspaces do not behave like subsets of a finite set.
For sets, $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ always holds.
For subspaces, the analogue with $+$ fails, as steps 5 to 7 show.
