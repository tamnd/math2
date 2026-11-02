---
tag: MBE83FTRBG
kind: example
name: Penrose tiling
msc: [52C23, 52C20, 05B45]
instance_of: [GKJK293DXS]
uses: [WFRGSBFZGV, Z3FCJZF6WK, 0SC8T7548D]
sources:
  - url: https://en.wikipedia.org/wiki/Penrose_tiling
same_as:
  wikidata: Q585688
  wikipedia: Penrose tiling
---

## Example

A *Penrose tiling* is a [[tiling|GKJK293DXS]] of the plane by copies of two prototiles that obey matching rules.
Roger Penrose introduced these tilings in the 1970s.
In the rhombus version, the prototiles are two rhombi with sides of length $1$.
The thick rhombus has angles $72^\circ$ and $108^\circ$, and the thin rhombus has angles $36^\circ$ and $144^\circ$.
The matching rules mark the edges of the rhombi and allow two tiles to meet along an edge only when the marks agree.
In the kite and dart version, the two prototiles are a convex kite and a non-convex dart, again with matching rules.

The two prototiles with their matching rules admit tilings of the whole plane, and none of these tilings is [[periodic|WFRGSBFZGV]].
So each version is an [[aperiodic set of prototiles|Z3FCJZF6WK]].
In every Penrose tiling the ratio of the number of thick to thin rhombi, counted in large disks, tends to the [[golden ratio|0SC8T7548D]] $\varphi = (1 + \sqrt{5})/2$.
Since $\varphi$ is irrational, this ratio cannot come from a periodic tiling, whose ratio would be the rational ratio within one period.

## Remarks

The matching rules are needed.
Without them, a thick rhombus is already a parallelogram that tiles the plane periodically, and a kite and a dart fit together into a rhombus that tiles periodically.
There are uncountably many different Penrose tilings, and every finite patch of one of them appears in every other one.
Some Penrose tilings have a global fivefold rotational symmetry about one point, which no periodic tiling of the plane can have.

## Explanations

### L1 human

A Penrose tiling covers the plane with just two shapes, yet the pattern never repeats.
You can slide it in any direction, and it never lands exactly on itself.
Still, it is highly ordered: patches with fivefold symmetry, like small stars, appear again and again.
The two kinds of tiles occur in the proportion of the golden ratio, about $1.618$ to $1$.
