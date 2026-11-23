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

We want the area of a disc of radius $r$, given that its [[circle|060W5CBZP6]] has length $2\pi r$, where $\pi$ is the number [[pi|0C1VYVNV2N]].
We follow geometric [[intuition|4BT08RE4CR]].

1. We cut the disc into $n$ equal sectors, like slices of a cake, with $n$ even.
2. We lay the sectors side by side, point up and point down in turn.
3. The pieces form a strip whose top and bottom edges are each made of $\frac{n}{2}$ arcs, so each edge has length $\frac{1}{2} \cdot 2\pi r = \pi r$.
4. The slanted sides of the strip are radii, of length $r$.
5. As $n$ grows, the arcs become flatter and the slanted sides become upright, so the strip looks more and more like a rectangle of width $\pi r$ and height $r$.
6. The pieces are the same as the disc for every $n$, so the strip has the area of the disc, and intuition concludes that the area is $\pi r \cdot r = \pi r^2$.

The conclusion is correct, and the picture explains why the area is half the circumference times the radius.
A proof needs one more step, because the area of a limit shape need not be the limit of the areas.
Here the area of the strip is the same for every $n$, and it lies between the areas of the regular polygons inscribed in the disc and circumscribed around it, which both tend to $\pi r^2$.

## Remarks

The squeeze in the last step is the method of Archimedes in *Measurement of a Circle*: the area lies between the inscribed and the circumscribed regular polygons.
For $r = 1$ and $n$ sides, the inscribed polygon has area $\frac{n}{2} \sin \frac{2\pi}{n}$ and the circumscribed polygon has area $n \tan \frac{\pi}{n}$.
For $n = 96$ these are about $3.1394$ and $3.1427$, and the area of the unit disc lies between them.

The same kind of picture fails for lengths.
Staircases from one corner of a unit square to the opposite corner all have total length $2$, and as the steps get smaller they approach the diagonal, which has length $\sqrt{2}$.
So "the length of the limit is the limit of the lengths" is false, and the step "the area of the limit is the limit of the areas" needs a reason that the picture does not supply.

## Explanations

### L1 human

Cut a round pizza into many thin slices.
Put the slices in a row, one pointing up, the next pointing down, and so on.
The row looks almost like a rectangle, whose height is the radius and whose length is half the way around the pizza.
So the area of the pizza is the radius times half the way around, which is $\pi r^2$.
The thinner the slices, the closer the row comes to a real rectangle.

### L2 human

We check the intuition against the polygon bounds for $r = 1$.
The inscribed polygons with $6$, $12$ and $96$ sides have areas
$$3 \sin 60^\circ \approx 2.598, \qquad 6 \sin 30^\circ = 3, \qquad 48 \sin 3.75^\circ \approx 3.1394.$$
The circumscribed polygons with the same numbers of sides have areas
$$6 \tan 30^\circ \approx 3.464, \qquad 12 \tan 15^\circ \approx 3.215, \qquad 96 \tan 1.875^\circ \approx 3.1427.$$
Both sequences approach $\pi \approx 3.1416$, the value that the rearrangement predicts for $\pi r^2$ with $r = 1$.
An intuitive rearrangement gives the formula, and two-sided bounds turn it into a proof.
Watch out: the staircase picture for the diagonal of a square looks just as convincing, and it gives the wrong length $2$ instead of $\sqrt{2}$.
