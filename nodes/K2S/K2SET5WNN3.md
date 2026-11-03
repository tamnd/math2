---
tag: K2SET5WNN3
kind: definition
name: Pre-Lie algebra
msc: [17D25, 17A30]
defines: KFD5TWA8W5
uses: [60W3THKGA7, RT4YV20367, 6Z35W744KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Pre-Lie_algebra
---

## Definition

Let $k$ be a field.
A *(left) pre-Lie algebra* over $k$ is a vector space $A$ over $k$ with a bilinear product $(x, y) \mapsto x \triangleright y$ such that
$$(x \triangleright y) \triangleright z - x \triangleright (y \triangleright z) = (y \triangleright x) \triangleright z - y \triangleright (x \triangleright z)$$
for all $x, y, z \in A$.

## Remarks

In terms of the [[associator|RT4YV20367]] $(x, y, z) = (x \triangleright y) \triangleright z - x \triangleright (y \triangleright z)$, the condition says $(x, y, z) = (y, x, z)$.
A *right* pre-Lie algebra asks instead for symmetry in the last two arguments.
In a pre-Lie algebra, the commutator $[x, y] = x \triangleright y - y \triangleright x$ is a Lie bracket, so a pre-Lie algebra is [[Lie-admissible|6Z35W744KQ]].

Example: $A = k[t]$ with $a \triangleright b = a b'$, where $'$ is the derivative.
Then $(a \triangleright b) \triangleright c - a \triangleright (b \triangleright c) = a b' c' - a (b' c' + b c'') = -a b c''$, which is symmetric in $a$ and $b$.
Every associative algebra is pre-Lie, since its associator is zero.

Non-example: a Lie algebra $\mathfrak{g}$ with $x \triangleright y = [x, y]$.
Using the Jacobi identity, the difference of the two sides of the condition equals $[[x, y], z]$.
For $\mathfrak{g} = \mathfrak{sl}_2$ with $[e, f] = h$ and $[h, e] = 2e$, take $x = e$, $y = f$, $z = e$: the difference is $[h, e] = 2e \neq 0$ when the characteristic of $k$ is not $2$.
