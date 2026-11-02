---
tag: 687RGCHBTP
kind: statement
role: theorem
name: Jordan curve theorem
msc: [57N35, 54D05]
uses: [060W5CBZP6, 00ZG9Y9TR4, 0V032VWTHD, 0XPR1E85W0]
about: [00ZG9Y9TR4]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_curve_theorem
same_as:
  wikidata: Q260928
  wikipedia: Jordan curve theorem
---

## Statement

Let $C \subset \R^2$ be a Jordan curve, that is, the image of a [[topological embedding|00ZG9Y9TR4]] $\gamma \colon S^1 \to \R^2$ of the [[circle|060W5CBZP6]] into the [[plane|0XPR1E85W0]].
Then $\R^2 \setminus C$ has exactly two [[connected components|0V032VWTHD]].
One component is bounded and the other is unbounded.
The curve $C$ is the boundary of each component.

## Remarks

For a polygon the theorem is elementary: the parity of the number of crossings of a ray with the polygon tells the two sides apart.
For a general curve, one proof approximates by polygons; another computes with homology, where Alexander duality gives $\tilde H_0(\R^2 \setminus C) \cong \Z$, so there are two components.
The theorem is hard because a Jordan curve can be very irregular, for example nowhere differentiable, or of positive area as an Osgood curve.
The bounded component is called the interior of $C$ and the unbounded one the exterior.
The same holds on the sphere $S^2$, without the words bounded and unbounded.

## Explanations

### L1 human

A closed loop drawn in the plane without crossing itself cuts the plane into an inside and an outside.
To go from a point inside to a point outside, a path must cross the loop.
This seems obvious, but the loop can be extremely wiggly, so the proof is subtle.

### L2 human

The theorem is the first case of the Jordan–Brouwer separation theorem: an embedded $(n-1)$-sphere in $\R^n$ separates it into two components.
Its strengthening in the plane, the Schoenflies theorem, says that the inside is a topological disk.
In higher dimensions this strengthening fails without extra hypotheses, as the Alexander horned sphere shows.
In complex analysis, the theorem gives meaning to "the inside of a contour" in Cauchy's integral theorem.
