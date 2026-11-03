---
tag: PP2CAZ7QKE
kind: object
name: Peaucellier–Lipkin linkage
msc: [70B15, 51M15]
uses: [YXST7NGMTC]
sources:
  - url: https://en.wikipedia.org/wiki/Peaucellier%E2%80%93Lipkin_linkage
same_as:
  wikidata: Q388067
  wikipedia: Peaucellier–Lipkin linkage
---

## Description

The *Peaucellier–Lipkin linkage* is a planar linkage that turns motion on a circle into motion on an exact straight line.
It is built from these bars, joined by revolute joints, with two fixed pivots $O$ and $C$ at distance $r$.

1. Two bars of length $\ell$ join $O$ to two joints $A$ and $B$.
2. Four bars of length $s < \ell$ form a rhombus $A P B Q$.
3. One bar of length $r$ joins $C$ to $P$.

Check: by symmetry $O$, $P$ and $Q$ lie on the perpendicular bisector of $AB$; with $M$ the midpoint of $AB$,
$$\abs{OP} \cdot \abs{OQ} = \abs{OM}^2 - \abs{MP}^2 = (\ell^2 - \abs{AM}^2) - (s^2 - \abs{AM}^2) = \ell^2 - s^2.$$
So $Q$ is the image of $P$ under the [[inversion|YXST7NGMTC]] in the circle of centre $O$ and radius $\sqrt{\ell^2 - s^2}$.
By bar 3, $P$ moves on the circle of centre $C$ and radius $r$, which passes through $O$.
Inversion maps a circle through the centre of inversion to a straight line, so $Q$ moves on a straight line, perpendicular to $OC$.

## Remarks

It was the first planar linkage known to draw an exact straight line.
It is named after Charles-Nicolas Peaucellier and Yom Tov Lipman Lipkin, who found it independently.
Without bar 3, the joint $Q$ traces the inverse of any curve traced by $P$, so the linkage is a mechanical inversor.

## Explanations

### L1 human

Before this linkage, machines could only draw straight lines approximately with rods and hinges.
This device of seven bars draws a perfectly straight line while one of its joints goes round a circle.
The trick is geometric: the device keeps the product of two distances constant, which is exactly what inversion in a circle does.
