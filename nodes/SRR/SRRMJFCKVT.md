---
tag: SRRMJFCKVT
kind: definition
name: String diagram
msc: [18M30, 18M05]
defines: 5YHK0VS62A
uses: [M3MSQ3NKAE]
sources:
  - url: https://en.wikipedia.org/wiki/String_diagram
---

## Definition

Let $(\mathcal{C}, \otimes, I)$ be a strict [[monoidal category|M3MSQ3NKAE]].
A *string diagram* in $\mathcal{C}$ is a picture in the strip $\R \times [0, 1]$ with the following parts.

1. Finitely many disjoint boxes, each labelled by a morphism $f \colon A_1 \otimes \cdots \otimes A_m \to B_1 \otimes \cdots \otimes B_n$ of $\mathcal{C}$.
2. Finitely many disjoint wires, each an arc on which the height coordinate is strictly increasing, each labelled by an object of $\mathcal{C}$.
3. Each wire starts at the bottom edge of the strip or at the top of a box. It ends at the top edge of the strip or at the bottom of a box.
4. The wires entering a box labelled $f$, read from left to right, carry $A_1, \ldots, A_m$, and the wires leaving it carry $B_1, \ldots, B_n$.

The *value* of the diagram is a morphism from the tensor product of the bottom labels to the tensor product of the top labels.
To compute it, cut the strip by horizontal lines so that each slice contains at most one box.
Each slice is then the tensor product of identities and one box.
The value is the composite of the slices from bottom to top.

## Remarks

This node reads diagrams from bottom to top; reading from top to bottom or from left to right is also common.
The Joyal–Street theorem says that the value does not depend on the slicing, and is unchanged by deformations of the plane that keep the wires increasing.
An empty region stands for the unit object $I$, so a box with no input wires is a morphism $I \to B$.
Example: a box labelled $f \colon A \to B$ with one wire $A$ below and one wire $B$ above has value $f$.
Placing a box $g \colon C \to D$ to its right gives $f \otimes g$, and stacking a box $h \colon B \to E$ on the wire $B$ above $f$ gives $h \circ f$.
Non-example: a wire labelled $A$ entering a box labelled $f \colon B \to C$ with $B \ne A$ breaks clause 4, so the picture has no value.
By Mac Lane's coherence theorem, every monoidal category is equivalent to a strict one, so string diagrams apply to all monoidal categories.
Braided and symmetric monoidal categories allow wires to cross, and categories with duals allow wires to bend.
