---
tag: TYER4M561B
kind: example
name: The symmetry group of a rectangle that is not a square
msc: [20B25]
topics: [BAZT8JJ70S]
audience: school
instance_of: [0ZG3Z5JZ85, 0PMRQJVTME]
uses: [0ZG3Z5JZ85, 0J1N3WTKM4, 0YB2NRP0T5]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Symmetry_group
    locator: lead section
---

## Example

Let $a$ and $b$ be positive real numbers with $a \ne b$.
Let $R$ be the rectangle with the vertices $(a, b)$, $(-a, b)$, $(-a, -b)$ and $(a, -b)$, that is, the set of points $(x, y)$ with $|x| \le a$ and $|y| \le b$.
We find its [[symmetry group|0ZG3Z5JZ85]] $\operatorname{Sym}(R)$ and show that it is the [[Klein four-group|0PMRQJVTME]].
Consider the four maps
$$e(x, y) = (x, y), \quad r(x, y) = (-x, -y), \quad h(x, y) = (x, -y), \quad v(x, y) = (-x, y).$$
Here $r$ is the turn by $180^\circ$ about $0$, $h$ is the reflection in the $x$-axis and $v$ is the reflection in the $y$-axis.

1. Each of the four maps changes only the signs of the coordinates, so it keeps all distances. Thus each map is a [[Euclidean isometry|0J1N3WTKM4]].
2. Each map keeps $|x|$ and $|y|$, so it maps $R$ into $R$. Each map is its own inverse, so it also maps $R$ onto $R$. Thus $e, r, h, v \in \operatorname{Sym}(R)$.
3. The largest distance between two points of $R$ is the length of a diagonal, and only the pairs of opposite vertices have this distance. An isometry keeps this property, so each symmetry maps vertices to vertices and opposite vertices to opposite vertices.
4. The vertex $A = (a, b)$ has one neighbour at distance $2a$ and one neighbour at distance $2b$, and $2a \ne 2b$. So when we know the image of $A$, the images of the other three vertices are fixed by these distances.
5. A plane isometry is known when we know the images of three points that are not on one line. By steps 3 and 4, there are at most $4$ symmetries, one for each choice of the image of $A$.
6. The maps $e$, $r$, $h$ and $v$ send $A$ to four different vertices. So $\operatorname{Sym}(R) = \{e, r, h, v\}$.
7. We compute the products. For example, $r(h(x, y)) = r(x, -y) = (-x, y) = v(x, y)$, so $rh = v$. In the same way we get the [[Cayley table|0YB2NRP0T5]] below, where the entry in row $f$ and column $g$ is $fg = f \circ g$.

| $\circ$ | $e$ | $r$ | $h$ | $v$ |
|---|---|---|---|---|
| $e$ | $e$ | $r$ | $h$ | $v$ |
| $r$ | $r$ | $e$ | $v$ | $h$ |
| $h$ | $h$ | $v$ | $e$ | $r$ |
| $v$ | $v$ | $h$ | $r$ | $e$ |

8. The table is symmetric about its main diagonal, so the group is [[abelian|082GHNPJ53]]. Each element is its own inverse, because the diagonal entries are all $e$.

A group of order $4$ in which each element other than $e$ has order $2$ is the Klein four-group, so $\operatorname{Sym}(R)$ is the Klein four-group.

## Remarks

The example shows that a figure can have reflections and a turn by $180^\circ$, but no turn by $90^\circ$.
When $a = b$, the rectangle is a square, step 4 fails, and the symmetry group grows to the [[dihedral group of order 8|054SBCQ93T]].
The four new symmetries are the turns by $90^\circ$ and $270^\circ$ and the reflections in the two diagonals.
The rotation group of $R$ is $\{e, r\}$, so half of the symmetries are rotations.
This agrees with a basic property of symmetry groups: when all symmetries fix one point and one of them is a reflection, half of them are rotations.
The rhombus with vertices $(\pm a, 0)$ and $(0, \pm b)$, with $a \ne b$, has the same symmetry group, with the same four maps.

## Explanations

### L1 human

Take a sheet of paper that is longer than it is wide, and lay it on a table.
There are four ways to put it back on the same spot.
We can leave it, turn it half a turn, flip it from top to bottom, or flip it from left to right.
A quarter turn does not work, because the long side would then point the wrong way.
Doing two of the four moves one after the other always gives one of the four moves.
For example, the two flips together give the half turn.

### L2 human

We check one row of the Cayley table by hand, the row of $h$.

1. $h(e(x, y)) = h(x, y) = (x, -y)$, so $he = h$.
2. $h(r(x, y)) = h(-x, -y) = (-x, y)$, so $hr = v$.
3. $h(h(x, y)) = h(x, -y) = (x, y)$, so $hh = e$.
4. $h(v(x, y)) = h(-x, y) = (-x, -y)$, so $hv = r$.

This gives the row $h, v, e, r$ of the table.
The typical use of this example is as a first group that is abelian but not cyclic: no element has order $4$, so no element generates the group.
A trap is to think that each figure with $4$ symmetries has this group: the four turns of a square pinwheel by $0^\circ$, $90^\circ$, $180^\circ$ and $270^\circ$ form a cyclic group of order $4$.
