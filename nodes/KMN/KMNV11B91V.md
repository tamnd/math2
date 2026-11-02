---
tag: KMNV11B91V
kind: example
name: Reuleaux triangle
msc: [52A10, 52A38]
instance_of: [B4YD1ZXRVH]
uses: [B4YD1ZXRVH, 060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Reuleaux_triangle
same_as:
  wikidata: Q959203
  wikipedia: Reuleaux triangle
---

## Example

Let $w > 0$, and let $A$, $B$, $C$ be the vertices of an equilateral triangle of side $w$ in the plane.
The *Reuleaux triangle* is the intersection of the three closed discs of radius $w$ centred at $A$, $B$ and $C$.
Its boundary consists of three arcs of [[circles|060W5CBZP6]] of radius $w$: the arc from $B$ to $C$ centred at $A$, and the two similar arcs.
Each arc has angle $\pi/3$.

Its boundary is a [[curve of constant width|B4YD1ZXRVH]] $w$.
Check: take a unit vector $u$ and the two supporting lines orthogonal to $u$.
The arc centred at $A$ consists of the points $A + w v$ with $v$ in an angle $V_A$ of size $\pi/3$.
Its outer normal at $A + w v$ is $v$.
The outer normals of the body at the vertex $A$ are the vectors $-v$ with $v \in V_A$.
These six angles of size $\pi/3$ cover all directions.
So for some vertex, say $A$, one of $u$ and $-u$ lies in $V_A$ and the other is an outer normal at $A$.
Then one supporting line passes through $A$ and the other through a point $A \pm w u$ of the arc centred at $A$.
The distance between the two lines is $w$.

The perimeter is $3 \cdot w \cdot \pi/3 = \pi w$.
The area is the sum of three circular sectors of angle $\pi/3$ minus twice the triangle: $3 \cdot \frac{\pi w^2}{6} - 2 \cdot \frac{\sqrt{3}}{4} w^2 = \frac{\pi - \sqrt{3}}{2} w^2$.

## Explanations

### L1 human

Draw an equilateral triangle and replace each side by an arc of a circle centred at the opposite corner.
The result is a rounded triangle that has the same width in every direction, just like a coin.
It can turn between two parallel boards that stay at a fixed distance, and it is used in some coin shapes and drill designs.
Among all shapes of a given constant width it has the smallest area.
