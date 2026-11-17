---
tag: MSMXVPKRN1
kind: example
name: A dimension count predicts the lines on surfaces in space
msc: ["14N10", "00A35"]
topics: [DME0TPC348]
audience: research
instance_of: [VCQQNJ3SEZ]
uses: [VCQQNJ3SEZ, CYPA882RB9, 36X2WTHYCB, VQK5HQFYEM, KDEVJ69P10]
sources:
  - url: https://en.wikipedia.org/wiki/Cubic_surface
    locator: 27 lines on a cubic surface
  - url: https://en.wikipedia.org/wiki/Grassmannian
    locator: lead section
---

## Example

We predict how many lines lie on a surface of degree $d$ in complex projective space $\mathbb{P}^3$, by a dimension count.
The count is a [[heuristic argument|VCQQNJ3SEZ]]: it gives the expected answer for a general surface.

1. The parameters. The lines in $\mathbb{P}^3$ form the [[Grassmannian|CYPA882RB9]] $G(2,4)$, which has [[dimension|36X2WTHYCB]] $4$. For example, a line not meeting a fixed line is the graph of a linear map $\mathbb{C}^2 \to \mathbb{C}^2$, with $4$ entries.
2. The conditions. A surface of degree $d$ is the zero set of a homogeneous polynomial $F$ of degree $d$. Restricted to a line with coordinates $(s : t)$, $F$ becomes a binary form of degree $d$, with $d + 1$ coefficients. The line lies on the surface exactly when all $d + 1$ coefficients vanish.
3. The expected dimension. The family of lines on the surface has expected dimension $4 - (d + 1) = 3 - d$.
4. The predictions. For $d = 1$ (a plane): a $2$-dimensional family. For $d = 2$ (a quadric): a $1$-dimensional family. For $d = 3$ (a cubic): finitely many lines. For $d \geq 4$: no lines on a general surface.
5. The facts. A plane contains a $2$-dimensional family of lines. A smooth quadric contains two $1$-dimensional families, its two rulings. A smooth [[cubic surface|KDEVJ69P10]] contains exactly [[$27$ lines|VQK5HQFYEM]]. A general surface of degree $d \geq 4$ contains no line.

So the count predicts the dimension correctly in every degree.

## Remarks

The count of step 3 gives a dimension, not a number.
The number $27$ for cubics needs more work: Arthur Cayley and George Salmon found it in 1849, and today it is computed with the Chern classes of a bundle on the Grassmannian.
The count predicts the general case only.
Special surfaces can have more lines: the Fermat quartic $x^4 + y^4 + z^4 + w^4 = 0$ has dimension count $-1$, and it contains $48$ lines.
For such special surfaces the $d + 1$ conditions of step 2 are not independent.

## Explanations

### L1 human

A line in space can be moved in $4$ independent ways, so lines form a $4$-dimensional family.
To lie on a surface of degree $3$, a line must satisfy $4$ conditions.
Four freedoms minus four conditions leaves no freedom, so we expect only finitely many lines.
Indeed, a smooth cubic surface contains exactly $27$ lines.
For degree $4$ there are $5$ conditions, more than the $4$ freedoms, so a typical such surface contains no line.

### L2 human

We check step 2 for the quadric $F = xw - yz$ in $\mathbb{P}^3$.

1. Take the line $\ell$ of points $(s : t : \lambda s : \lambda t)$ for a fixed $\lambda$.
2. Then $F = s \cdot \lambda t - t \cdot \lambda s = 0$ for all $(s : t)$, so all $3$ coefficients of the binary form vanish, and $\ell$ lies on the quadric.
3. As $\lambda$ varies, these lines form a $1$-dimensional family, as step 3 predicts for $d = 2$.

The typical use: before computing the solutions of a system, count parameters and conditions to know what to expect.
A trap: the count assumes the conditions are independent; for special data they can be dependent, and the true dimension is larger.
