---
tag: QFS48Z21YT
kind: definition
name: Associator
msc: [17A01, 17D05]
defines: RT4YV20367
uses: [60W3THKGA7]
sources:
  - url: https://en.wikipedia.org/wiki/Associator
---

## Definition

Let $A$ be a [[nonassociative algebra|60W3THKGA7]] over a commutative ring $R$.
The *associator* of $x, y, z \in A$ is the element
$$(x, y, z) = (xy)z - x(yz)$$
of $A$.

## Remarks

The map $(x, y, z) \mapsto (x, y, z)$ is $R$-trilinear.
The algebra $A$ is associative if and only if all associators vanish.
For all $a, b, c, d \in A$ the Teichmüller identity holds:
$$a(b, c, d) + (a, b, c)d = (ab, c, d) - (a, bc, d) + (a, b, cd).$$
It follows by expanding both sides.
Example: in $\R^3$ with the cross product, $(e_1, e_1, e_2) = (e_1 \times e_1) \times e_2 - e_1 \times (e_1 \times e_2) = 0 - (-e_2) = e_2$.
In an associative algebra, such as the $2 \times 2$ real matrices, every associator is $0$.
Some authors write $[x, y, z]$ instead of $(x, y, z)$.
