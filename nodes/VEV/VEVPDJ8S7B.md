---
tag: VEVPDJ8S7B
kind: concept
name: Curvelet
msc: [42C40, 42C15, 94A08]
sources:
  - url: https://en.wikipedia.org/wiki/Curvelet
same_as:
  wikidata: Q5196075
  wikipedia: Curvelet
---

## Summary

Curvelets are a multiscale system of functions on the plane that are indexed by scale, orientation and position.
At fine scales they are thin needles whose width is roughly the square of their length, a rule called parabolic scaling.
This shape matches smooth curves well, so images that are smooth apart from smooth edges have sparse curvelet expansions.
For such images, the best approximation with $N$ curvelets has squared error of order $N^{-2}(\log N)^3$, while $N$ wavelets give only order $N^{-1}$.

## Explanations

### L1 human

Two-dimensional wavelets are small square blobs, so following a curved edge needs many of them.
Curvelets are long, thin and oriented, like short strokes of a pen.
A smooth edge, seen up close, is almost a straight segment, and a single curvelet aligned with it covers it.
As the scale gets finer, the strokes get thinner faster than they get shorter, and there are more possible directions.
This is why curvelets describe images with clean contours using far fewer terms than wavelets.
