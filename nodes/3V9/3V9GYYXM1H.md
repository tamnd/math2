---
tag: 3V9GYYXM1H
kind: example
name: Moulton plane
msc: [51A35, 51A15]
instance_of: [EC7XT2ZM5S]
uses: [5Z19Y02MME, DANFNN8C4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Moulton_plane
same_as:
  wikidata: Q650995
  wikipedia: Moulton plane
---

## Example

The points of the *Moulton plane* are the points of $\R^2$.
Its lines are of three kinds:

1. the vertical lines $x = c$;
2. the lines $y = m x + b$ with slope $m \ge 0$;
3. for each slope $m < 0$ and each $b \in \R$, the bent line made of the points $(x, m x + b)$ with $x \le 0$ and the points $(x, 2 m x + b)$ with $x \ge 0$.

So lines of negative slope are bent where they cross the $y$-axis, and their slope doubles on the right.
With these lines it is an [[affine plane|EC7XT2ZM5S]]: any two points lie on exactly one line.
For a fixed $m < 0$, the bent lines with parameter $m$ are pairwise parallel, as are the lines of each other slope.
Some authors use another factor than $2$; any positive factor other than $1$ gives a plane with the same properties.

The Moulton plane does not satisfy the affine form of [[Desargues's theorem|5Z19Y02MME]].
Let $O = (-10, -10)$, $A = (-8, -6)$, $B = (-6, 2)$, $C = (-2, -2)$, and $A' = (-7, -4)$, $B' = (-4, 8)$, $C' = (2, 2)$.
Check:

- $A' = O + \tfrac{3}{2}(A - O)$, and likewise for $B'$ and $C'$.
- The lines $OA$, $OB$, $OC$ have slopes $2$, $3$, $1$, so they are ordinary lines; they contain $A'$, $B'$, $C'$.
- $AB$ and $A'B'$ both have slope $4$, and $AC$ and $A'C'$ both have slope $2/3$; these are ordinary distinct lines, so $AB \parallel A'B'$ and $AC \parallel A'C'$.
- $B$ and $C$ lie in $x < 0$ on $y = -x - 4$, so $BC$ is the bent line with $m = -1$, $b = -4$.
- The line through $B'$ and $C'$ is bent with $8 = -4m + b$ and $2 = 4m + b$, so $m = -3/4$ and $b = 5$.

Since $-3/4 \ne -1$, the line $B'C'$ is not parallel to $BC$.
In the Euclidean plane the same data would force $BC \parallel B'C'$.

## Remarks

Add a line at infinity, with one point for each class of parallel lines, to get a [[projective plane|DANFNN8C4Y]].
In it the triangles $ABC$ and $A'B'C'$ are in perspective from $O$, the points $AB \cap A'B'$ and $AC \cap A'C'$ lie on the line at infinity, but $BC \cap B'C'$ is a finite point.
So the three points are not collinear, and the projective completion is a [[non-Desarguesian plane|HYE5FT4M34]].

## Explanations

### L1 human

The Moulton plane is the ordinary plane with a strange rule for lines: lines going downhill bend as they cross the vertical axis, like light entering water.
Uphill and vertical lines stay straight.
Through two points there is still exactly one line, and parallels behave as usual.
But Desargues's theorem, which always works in the ordinary plane, fails here, which shows that this theorem is not a consequence of the incidence axioms alone.
