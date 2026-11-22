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

In $\mathbb{R}^2$, take the three lines through the origin
$$L_1 = \operatorname{span}((1, 0)), \qquad L_2 = \operatorname{span}((0, 1)), \qquad L_3 = \operatorname{span}((1, 1)).$$
Each line has dimension $1$.
We compute their [[sums|0RMKABS2S5]] and intersections, and then test two rules that hold for sets.

1. Any two of the lines meet only in $0$. For example, a vector $t(1, 1)$ of $L_3$ lies in $L_1$ only when its second entry $t$ is $0$. In the same way $L_1 \cap L_2 = L_2 \cap L_3 = \{0\}$.
2. Any two of the lines sum to the whole plane. For $L_1$ and $L_2$ this is $(a, b) = (a, 0) + (0, b)$.
3. For $L_1$ and $L_3$ we put the second entry into $L_3$ first:
$$(a, b) = (a - b, 0) + b(1, 1).$$
4. For $L_2$ and $L_3$ we put the first entry into $L_3$ first: $(a, b) = (0, b - a) + a(1, 1)$. So $L_1 + L_2 + L_3 = \mathbb{R}^2$ as well, of dimension $2$.
5. Distributivity fails. On one side, $L_3 \cap (L_1 + L_2) = L_3 \cap \mathbb{R}^2 = L_3$. On the other side, $(L_3 \cap L_1) + (L_3 \cap L_2) = \{0\} + \{0\} = \{0\}$. Since $L_3 \ne \{0\}$, the two sides differ.
6. Inclusion-exclusion fails. The formula that counts the elements of a union of three finite sets, applied to dimensions, gives
$$\dim L_1 + \dim L_2 + \dim L_3 - \dim(L_1 \cap L_2) - \dim(L_1 \cap L_3) - \dim(L_2 \cap L_3) + \dim(L_1 \cap L_2 \cap L_3) = 1 + 1 + 1 - 0 - 0 - 0 + 0 = 3.$$
7. The true value is $\dim(L_1 + L_2 + L_3) = \dim \mathbb{R}^2 = 2$.

## Remarks

For two subspaces, [[Grassmann's formula|06HTJNCMPA]] $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$ holds, and here it gives $1 + 1 - 0 = 2$ for every pair.
The example shows that the formula has no three-term version.
The reason is that the sum of $L_1$ and $L_2$ already contains $L_3$, so $L_3$ adds nothing new, while its pairwise intersections with $L_1$ and $L_2$ are $0$ and do not record this.

The lattice of subspaces is not distributive, but it is still modular: if $U \subseteq X$, then $X \cap (U + W) = U + (X \cap W)$.
The three lines do not contradict this, because none of them contains another.
The same lines show that a subspace has many complements: $L_2$ and $L_3$ both satisfy $L_1 + L = \mathbb{R}^2$ and $L_1 \cap L = \{0\}$.
They also show that pairwise trivial intersections do not make a sum of three subspaces direct, since $(1, 1) = (1, 0) + (0, 1) + 0 = 0 + 0 + (1, 1)$.

What changes with other numbers?
Any three distinct lines through the origin of a plane give the same picture, because any two distinct lines through the origin span the plane.
Over the field $\mathbb{F}_2$, the three lines are the only lines of $\mathbb{F}_2^2$, and their union is the whole plane.

## Explanations

### L1 human

Picture three different straight lines through one point of a sheet of paper, like three spokes of a wheel.
Any two of them already let you reach every point of the sheet: walk along one spoke, then parallel to the other.
So counting "one direction for each line" gives $1 + 1 + 1 = 3$, but the sheet has only $2$ directions.
The third line brings nothing new once the first two are there.

### L2 human

The lesson is that subspaces do not behave like subsets of a finite set.
For sets, the rule $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ always holds, and so does inclusion-exclusion for sizes.
For subspaces, the same rules with $+$ in place of $\cup$ and dimension in place of size fail, as steps 5 to 7 show.
So when you compute the dimension of a sum of three or more subspaces, do not use a formula with pairwise intersections.
Instead, join spanning lists of all the pieces and find the rank of the joined list, which here is the rank $2$ of the vectors $(1, 0)$, $(0, 1)$ and $(1, 1)$.
