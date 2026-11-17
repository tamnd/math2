---
tag: N96C8N6WBH
kind: example
name: The area of a disc by rearranging sectors
msc: ["00A35", "51M25"]
topics: [X1NSTVGDNQ]
audience: research
instance_of: [4BT08RE4CR]
uses: [4BT08RE4CR, 060W5CBZP6, 0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Area_of_a_circle
    locator: Rearrangement proof
---

## Example

Problem: find the area of a disc of radius $r$, given that its [[circle|060W5CBZP6]] has length $2\pi r$, where $\pi$ is the number [[pi|0C1VYVNV2N]].
We follow geometric [[intuition|4BT08RE4CR]].

1. Cut the disc into $n$ equal sectors, like slices of a cake, with $n$ even.
2. Lay the sectors side by side, alternately with the point up and the point down.
3. The pieces form a strip. Its top and bottom edges are each made of $\frac{n}{2}$ arcs, so each edge has length $\frac{1}{2} \cdot 2\pi r = \pi r$.
4. The slanted sides of the strip are radii, of length $r$.
5. As $n$ grows, the arcs become flatter and the slanted sides become vertical. The strip looks more and more like a rectangle of width $\pi r$ and height $r$.
6. The pieces are the same for each $n$, so the strip has the area of the disc. The intuition concludes: the area of the disc is $\pi r \cdot r = \pi r^2$.

The conclusion is correct, and the picture explains why the area is half the circumference times the radius.
A proof needs one more step: that the area of the limit shape is the limit of the areas.
Here the area is the same for every $n$, and it is squeezed between the areas of inscribed and circumscribed polygons, which both tend to $\pi r^2$.

## Remarks

The squeeze in the last step is Archimedes' method in his Measurement of a Circle: the area lies between the inscribed and circumscribed regular polygons.
For $r = 1$ and $n$ sides, the inscribed polygon has area $\frac{n}{2} \sin \frac{2\pi}{n}$ and the circumscribed polygon has area $n \tan \frac{\pi}{n}$.
For $n = 96$, these are about $3.1394$ and $3.1427$, and the area of the unit disc lies between them.
The same picture fails for a closely related problem: a curve can be approximated by staircases whose length stays fixed while the shape converges, so "the limit of the lengths is the length of the limit" is false for lengths.
The diagonal of a unit square, approximated by staircases of total length $2$, is the standard case: the staircases converge to the diagonal of length $\sqrt{2}$.
So the step "area of the limit equals limit of the areas" needs a reason, and the intuition does not supply it.

## Explanations

### L1 human

Cut a round pizza into many thin slices.
Put the slices in a row, one pointing up, the next pointing down, and so on.
The row looks almost like a rectangle.
Its height is the radius, and its length is half the way around the pizza.
So the area of the pizza is the radius times half the way around, which gives $\pi r^2$.
The thinner the slices, the closer the row is to a real rectangle.

### L2 human

We check the intuition against the polygon bounds for $r = 1$.

1. With $n = 6$, the inscribed hexagon has area $3 \sin 60^\circ = \frac{3\sqrt{3}}{2} \approx 2.598$.
2. With $n = 12$, the inscribed polygon has area $6 \sin 30^\circ = 3$.
3. With $n = 96$, it has area $48 \sin 3.75^\circ \approx 3.1394$.
4. The circumscribed polygons give $6 \tan 30^\circ \approx 3.464$, then $12 \tan 15^\circ \approx 3.215$, then $96 \tan 1.875^\circ \approx 3.1427$.
5. Both sequences approach $\pi \approx 3.1416$, the value that the rearrangement predicts for $\pi r^2$ with $r = 1$.

The typical use: an intuitive rearrangement gives the formula, and two-sided bounds turn it into a proof.

A trap: the staircase approximation to a diagonal looks just as convincing, and it gives the wrong length $2$ instead of $\sqrt{2}$.
