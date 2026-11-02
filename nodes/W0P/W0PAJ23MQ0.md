---
tag: W0PAJ23MQ0
kind: example
name: Pappus configuration
msc: [05B30, 51A20, 51A30]
instance_of: [Q2QFXPP9EE]
uses: [Q2QFXPP9EE, B6C3J2GJWP]
sources:
  - url: https://en.wikipedia.org/wiki/Pappus_configuration
same_as:
  wikidata: Q7133115
  wikipedia: Pappus configuration
---

## Example

The *Pappus configuration* is a [[configuration|Q2QFXPP9EE]] $(9_3)$ in the projective plane.
Take distinct points $A, B, C$ on a line $g$ and distinct points $a, b, c$ on another line $h$, none of them on both lines.
Let $X = Ab \cap aB$, $Y = Ac \cap aC$ and $Z = Bc \cap bC$.
By [[Pappus's hexagon theorem|B6C3J2GJWP]], $X$, $Y$, $Z$ lie on a line, the Pappus line.

Its $9$ points are $A, B, C, a, b, c, X, Y, Z$.
Its $9$ lines are $g$, $h$, the six lines $Ab$, $aB$, $Ac$, $aC$, $Bc$, $bC$ and the Pappus line.
Check: each line has $3$ of the points, for instance $Ab$ contains $A$, $b$, $X$ and $Bc$ contains $B$, $c$, $Z$.
Each point lies on $3$ lines.
For instance, $A$ lies on $g$, $Ab$, $Ac$, the point $b$ on $h$, $Ab$, $bC$, and $X$ on $Ab$, $aB$ and the Pappus line.
Its incidence graph is the Pappus graph.

## Explanations

### L1 human

Put three points on one line and three on another, and join them crosswise in pairs.
The three crossing points always land on a common line.
The finished picture has $9$ points and $9$ lines, with $3$ points on each line and $3$ lines through each point.
