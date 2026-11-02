---
tag: CTVSGWNB19
kind: example
name: Euclidean tilings by convex regular polygons
msc: [52C20, 05B45]
instance_of: [GKJK293DXS]
uses: [01KJJ9A400, WFRGSBFZGV]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_tilings_by_convex_regular_polygons
same_as:
  wikidata: Q2995026
  wikipedia: Euclidean tilings by convex regular polygons
---

## Example

Consider [[tilings|GKJK293DXS]] of the plane whose tiles are convex [[regular polygons|01KJJ9A400]].
The tiling is edge-to-edge if two tiles that meet share either one full edge or one vertex.
The interior angle of a regular $n$-gon is $(n-2)\pi/n$.
A tiling by copies of a single regular $n$-gon is called *regular*.
At each vertex of such a tiling some number $k \ge 3$ of tiles meet, so $k(n-2)\pi/n = 2\pi$, which gives $(n-2)(k-2) = 4$.
The only solutions are $(n, k) = (3, 6), (4, 4), (6, 3)$.
So there are exactly three regular tilings.
They use equilateral triangles, six at each vertex; squares, four at each vertex; and regular hexagons, three at each vertex.
In particular, regular pentagons do not tile the plane edge-to-edge, since $3 \cdot 3\pi/5 < 2\pi < 4 \cdot 3\pi/5$.

## Remarks

An edge-to-edge tiling by regular polygons is *semiregular*, or Archimedean, if it uses more than one kind of polygon and its symmetries map any vertex to any other vertex.
There are exactly eight semiregular tilings.
One of them has at each vertex a triangle, a square, a hexagon and a square, in this cyclic order; the angles add up to $\pi/3 + \pi/2 + 2\pi/3 + \pi/2 = 2\pi$.
The three regular and the eight semiregular tilings are all [[periodic|WFRGSBFZGV]].

## Explanations

### L1 human

Which regular shapes can cover a floor with no gaps, all meeting edge to edge?
The corners meeting at a point must add up to a full turn of $360^\circ$.
Triangles have $60^\circ$ corners, squares $90^\circ$ and hexagons $120^\circ$, and these divide $360^\circ$ evenly.
No other regular polygon works on its own, which is why floors use these three shapes so often.
Mixing several regular shapes gives eight more patterns in which every corner looks the same.
