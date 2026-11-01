---
tag: 3ENQE05H1H
kind: example
name: Lakes of Wada
msc: [54F15, 54G15]
illustrates: [05D5EGMFYV]
uses: [0V3XAMF3C1, 02BH3MCBQB, 0V032VWTHD]
sources:
  - url: https://en.wikipedia.org/wiki/Lakes_of_Wada
same_as:
  wikidata: Q1331442
  wikipedia: Lakes of Wada
---

## Example

The *Lakes of Wada* are three disjoint, connected, open subsets of the [[plane|0V3XAMF3C1]] that all have the same [[boundary|05D5EGMFYV]].
They can be built from a closed square of land with three lakes of water in it.
At step $n$, each lake in turn is extended by a thin canal of open water that winds through the land.
After the step, every point of the remaining land is within distance $2^{-n}$ of each lake.
The canals never meet each other, and the land left after each step is a nonempty compact set, so some land remains at the end.
After all steps, each lake is the union of its stages, so it is [[open|02BH3MCBQB]] and [[connected|0V032VWTHD]].
Every point of the remaining land is a limit of points of each lake, and the lakes are open and disjoint.
So the remaining land is the boundary of each of the three lakes.

## Remarks

The construction works the same way for any finite number of lakes.
In contrast, a simple closed curve in the plane is the common boundary of exactly two regions, by the Jordan curve theorem.
So the common boundary of the Lakes of Wada is not a simple closed curve; it is a continuum of a much wilder kind.
The example is credited to Takeo Wada; an earlier construction of the same kind is due to L. E. J. Brouwer.

## Explanations

### L1 human

Imagine an island with three lakes, and keep digging canals so that the water of each lake comes ever closer to every spot of dry land.
In the end, every point of the shore touches all three lakes at once.
It sounds impossible, because on a map two countries usually meet along a line and three meet only at points.
The example shows that boundaries in the plane can be far wilder than drawn lines.
