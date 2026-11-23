---
tag: QHY889QBEC
kind: example
name: Archimedes' lever argument for the volume of the sphere
msc: ["01A20", "51M25", "70C20"]
topics: [DME0TPC348]
audience: ug2
instance_of: [THJV0NFPDQ]
uses: [THJV0NFPDQ, P9CM4GQ2T0, 0HNK6KT05K]
sources:
  - url: https://en.wikipedia.org/wiki/The_Method_of_Mechanical_Theorems
    locator: Volume of a sphere
  - url: https://en.wikipedia.org/wiki/Archimedes_Palimpsest
    locator: lead section
---

## Example

Archimedes found the volume of a ball by hanging its slices on a lever, and his account of the method was lost until Johan Ludvig Heiberg identified it in 1906 in a palimpsest.
Take the middle slice of a ball of radius $r$ and the matching slice of a cone: together they have area $2\pi r^2$, and hung at distance $2r$ they balance a slice of a cylinder of area $4\pi r^2$ at distance $r$.
We follow the whole [[physical argument|THJV0NFPDQ]] for the volume of a [[sphere|P9CM4GQ2T0]] of radius $r$, in modern notation.

1. We place three solids along the axis $0 \le x \le 2r$.
   The ball has its center at $x = r$, the cone has its apex at $x = 0$ and radius $x$ at height $x$, and the cylinder has radius $2r$.
2. We compute the slices at $x$.
   The ball's slice is a disc of squared radius $r^2 - (x - r)^2 = 2rx - x^2$, the cone's slice has radius $x$, and the cylinder's slice has radius $2r$, so the areas are
$$\pi(2rx - x^2), \qquad \pi x^2, \qquad 4\pi r^2.$$
3. The ball slice and the cone slice together have area
$$\pi(2rx - x^2) + \pi x^2 = 2\pi r x.$$
4. We use the $x$-axis as a lever with its fulcrum at $x = 0$, and we extend it to the other side.
   We hang the ball slice and the cone slice at distance $2r$ on the other side, and we leave the cylinder slice where it is, at distance $x$.
5. We compare the moments, mass times distance, with mass taken as area.
   The hung slices give $2\pi r x \cdot 2r = 4\pi r^2 x$, and the cylinder slice gives $4\pi r^2 \cdot x$, so each pair of slices balances.
6. Archimedes concluded that the whole ball and cone, hung at distance $2r$, balance the whole cylinder.
   The cylinder acts at its [[center of mass|0HNK6KT05K]], at distance $r$.
7. The cylinder has volume $\pi (2r)^2 \cdot 2r = 8\pi r^3$, and the cone has volume $\tfrac13 \pi (2r)^2 \cdot 2r = \tfrac83 \pi r^3$, so the balance reads
$$2r\left(V + \tfrac83 \pi r^3\right) = r \cdot 8\pi r^3.$$
8. Dividing by $2r$ gives $V + \tfrac83 \pi r^3 = 4\pi r^3$, so
$$V = \tfrac43 \pi r^3.$$

Steps 4 to 6 use the law of the lever for plane slices, and step 6 treats a solid as the sum of its slices.
Both are physical assumptions, so the argument finds the volume without proving it.

## Remarks

### What Archimedes said about it

Archimedes described the argument in a letter to Eratosthenes, now called "The Method of Mechanical Theorems".
He wrote there that the mechanical method gives an indication of a result but not a demonstration of it.
He proved the volume of the sphere by the method of exhaustion in "On the Sphere and Cylinder".
So Archimedes himself treated the lever as a way to find the answer and geometry as the way to prove it.

### How the argument becomes a proof

In modern terms, step 5 for every $x$ gives an equality of integrals:
$$\int_0^{2r} 2r \cdot 2\pi r x \, dx = \int_0^{2r} x \cdot 4\pi r^2 \, dx.$$
Both sides equal $8\pi r^4$, and the left side is $2r$ times the volume of ball and cone together.
With the integral as a definition of volume, the physical step 6 is replaced by a theorem, and the argument becomes a proof.
The result says that the ball has $\tfrac23$ of the volume of the cylinder of radius $r$ and height $2r$ around it, and Plutarch reports that Archimedes asked for this figure on his tomb.

### Watch out

Step 6 does not follow from step 5 without a theory of limits or integrals.
Infinitely many balanced pairs of slices do not balance as solids unless the slices fill the solids in a controlled way.
That is exactly the step that Archimedes would not count as proof.

### Try it

Check step 5 at $x = r/2$.
The hung slices have area $2\pi r \cdot \tfrac{r}{2} = \pi r^2$ and moment $2\pi r^3$, and the cylinder slice has moment $4\pi r^2 \cdot \tfrac{r}{2} = 2\pi r^3$, so they balance.

## Explanations

### L1 human

Archimedes imagined cutting a ball, a cone and a cylinder into thin slices.
He hung the slices of the ball and the cone at one end of a balance and kept the slices of the cylinder spread along the other side.
Every pair of slices balanced, so he concluded that the whole solids balance too.
The balance told him the volume of the ball, $\tfrac43 \pi r^3$.
He did not count this as a proof, and he proved the result separately by geometry.

### L2 human

We check step 5 at the middle slice, $x = r$.
The ball slice is the largest disc, of radius $r$, and the cone slice also has radius $r$, so together
$$\pi r^2 + \pi r^2 = 2\pi r^2, \qquad \text{moment at distance } 2r: \ 2\pi r^2 \cdot 2r = 4\pi r^3.$$
The cylinder slice has area $4\pi r^2$ at distance $r$, so its moment is $4\pi r^3$, and the moments agree.
The typical use of the lever is to turn an unknown volume into a comparison with volumes already known, here the cone and the cylinder.
Watch out: a check at single slices confirms the identity of step 3, and it does not justify adding up infinitely many slices.
