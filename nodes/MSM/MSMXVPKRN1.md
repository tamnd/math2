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

A smooth cubic surface in space contains exactly $27$ lines, while a general surface of degree $4$ contains none.
A simple count of freedoms against conditions predicts the difference before any hard work.
We work in complex projective space $\mathbb{P}^3$ and ask how many lines lie on a surface of degree $d$.
The count is a [[heuristic argument|VCQQNJ3SEZ]]: it predicts the answer for a general surface, and it proves nothing.

1. We count the freedoms.
   The lines in $\mathbb{P}^3$ form the [[Grassmannian|CYPA882RB9]] $G(2, 4)$, which has [[dimension|36X2WTHYCB]] $4$.
   For example, a line that misses a fixed line is the graph of a linear map $\mathbb{C}^2 \to \mathbb{C}^2$, and such a map has $4$ entries.
2. We count the conditions.
   A surface of degree $d$ is the zero set of a homogeneous polynomial $F$ of degree $d$.
   On a line with coordinates $(s : t)$, the polynomial $F$ becomes a binary form of degree $d$, which has $d + 1$ coefficients.
   The line lies on the surface exactly when all $d + 1$ coefficients vanish.
3. We subtract.
   If the conditions are independent, the lines on the surface form a family of dimension
$$4 - (d + 1) = 3 - d.$$
4. We read off the predictions.
   A plane ($d = 1$) should carry a $2$-dimensional family of lines, and a quadric ($d = 2$) a $1$-dimensional family.
   A cubic ($d = 3$) should carry finitely many lines, and a general surface with $d \ge 4$ should carry none.
5. We compare with the theorems.
   A plane contains a $2$-dimensional family of lines, and a smooth quadric contains two $1$-dimensional families, its two rulings.
   A smooth [[cubic surface|KDEVJ69P10]] contains exactly [[27 lines|VQK5HQFYEM]], and a general surface of degree $d \ge 4$ contains no line.

So the count predicts the right dimension in every degree.

## Remarks

### A dimension is not a number

The count says that a cubic has finitely many lines, and it does not say how many.
Arthur Cayley and George Salmon found the number $27$ in 1849.
Today the number is computed with Chern classes of a vector bundle on the Grassmannian, which turns the heuristic count into a proof.
So the heuristic told mathematicians where to look, and a separate argument supplied the answer.

### When the conditions are dependent

The count predicts the general case only.
The Fermat quartic $x^4 + y^4 + z^4 + w^4 = 0$ has expected dimension $3 - 4 = -1$, so the count predicts no lines, yet it contains $48$ lines.
On this special surface the $5$ conditions of step 2 are not independent for some lines.
A negative expected dimension means "no solutions for general data", not "no solutions ever".

### Watch out

The count assumes that the conditions cut the freedoms down one at a time.
For special data this fails, as the Fermat quartic shows, and the true dimension can be larger than the count.
Before you use the count as evidence for a specific surface, check that the surface is general in the needed sense.

### Try it

How many conditions must a line satisfy to lie on a surface of degree $5$, and what does the count predict?
It must satisfy $6$ conditions, so the expected dimension is $4 - 6 = -2$, and a general quintic surface contains no line.

The lines through a fixed point of $\mathbb{P}^3$ form a family of dimension $2$.
How many of them should lie on a general cubic surface through that point?
A line through the point already meets the surface there, so it needs only $3$ more conditions, and $2 - 3 = -1$ predicts none for a general point of the surface.

## Explanations

### L1 human

A line in space can be moved in $4$ independent ways, so the lines form a $4$-dimensional family.
To lie on a surface of degree $3$, a line must satisfy $4$ conditions.
Four freedoms minus four conditions leaves no freedom, so we expect only finitely many lines.
Indeed, a smooth cubic surface contains exactly $27$ lines.
For degree $4$ there are $5$ conditions, more than the $4$ freedoms, so a typical such surface contains no line.
The count is a guide and not a proof, and special surfaces can break it.

### L2 human

We check step 2 for the quadric $F = xw - yz$ in $\mathbb{P}^3$.
Fix a number $\lambda$ and take the line $\ell_\lambda$ of points $(s : t : \lambda s : \lambda t)$.
Substitute into $F$:
$$F(s, t, \lambda s, \lambda t) = s \cdot \lambda t - t \cdot \lambda s = 0.$$
This holds for every $(s : t)$, so all $3$ coefficients of the binary form vanish, and $\ell_\lambda$ lies on the quadric.
As $\lambda$ varies, the lines $\ell_\lambda$ form a $1$-dimensional family, as step 4 predicts for $d = 2$.
The typical use is to count parameters and conditions before solving a system, so that you know what size of answer to expect.
Watch out: the count assumes independent conditions, and for special data the true dimension can be larger.
