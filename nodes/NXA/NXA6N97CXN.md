---
tag: NXA6N97CXN
kind: statement
role: theorem
name: Lieb's square ice constant
msc: [82B23, 05A16, 82B20]
uses: [45HEVXM7RD]
about: [45HEVXM7RD]
sources:
  - url: https://en.wikipedia.org/wiki/Lieb%27s_square_ice_constant
same_as:
  wikidata: Q17097221
  wikipedia: Lieb's square ice constant
---

## Statement

For $N \ge 1$, consider the $N \times N$ square grid on a torus.
Let $f(N)$ be the number of orientations of its edges such that every vertex has exactly two incoming and two outgoing edges.
Then
$$\lim_{N \to \infty} f(N)^{1/N^2} = \left( \frac{4}{3} \right)^{3/2} = \frac{8 \sqrt{3}}{9} = 1.5396\ldots$$

## Remarks

The orientations counted are the configurations of the [[six-vertex model|45HEVXM7RD]] with all weights equal to $1$.
Lieb proved the formula in 1967 by writing $f(N)$ through a [[transfer matrix|EXX6S3K5Z5]] and finding its largest eigenvalue with the [[Bethe ansatz|S92G5M6X41]].
Pauling's 1935 estimate gives $4 \cdot \frac{6}{16} = \frac{3}{2}$: each vertex allows $6$ of the $16$ orientations of its four edges, and there are two edges per vertex.
The exact constant is a little larger than this estimate.
The same constant governs the growth of the number of proper $3$-colourings of the faces of the square grid, since such colourings correspond to ice configurations.

## Explanations

### L1 human

Count the ways to put arrows on the edges of a big square grid, closed up into a torus, so that every vertex has two arrows in and two out.
The number grows like $W^{N^2}$, and Lieb found the exact value $W = (4/3)^{3/2}$.
It measures the leftover entropy of ice at zero temperature in a flat model.

### L2 human

This was the first exact solution of a six-vertex model, and it opened the way to the general solution of ice-type models.
The method, a transfer matrix diagonalized by the Bethe ansatz, became a standard tool for [[exactly solvable models|DVQ0PVHKY1]].
The correspondence with $3$-colourings makes the result also a theorem of enumerative combinatorics.
