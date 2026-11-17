---
tag: T6WDA860PA
kind: example
name: The rearrangement picture for the Pythagorean theorem
msc: ["00A35", "51M04"]
topics: [1BTHSHST4M]
audience: school
instance_of: [V6ESFEFKJC]
uses: [V6ESFEFKJC, 0VP3A1290K]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_theorem
    locator: Rearrangement proofs
  - url: https://en.wikipedia.org/wiki/Proof_without_words
    locator: lead section
---

## Example

Let $T$ be a right triangle with legs $a > 0$ and $b > 0$ and hypotenuse $c$.
The [[Pythagorean theorem|0VP3A1290K]] says that $a^2 + b^2 = c^2$.
The picture shows two squares of side $a + b$, each with four copies of $T$ inside.
In the first square the four triangles leave a tilted square of side $c$ uncovered.
In the second square they form two rectangles and leave a square of side $a$ and a square of side $b$ uncovered.
We check each fact that the eye reads from the picture, in coordinates.

1. Let $Q$ be the square with corners $(0, 0)$, $(a + b, 0)$, $(a + b, a + b)$ and $(0, a + b)$. Its area is $(a + b)^2$.
2. First picture: let $P_1 = (a, 0)$, $P_2 = (a + b, a)$, $P_3 = (b, a + b)$ and $P_4 = (0, b)$. These four points lie on the four sides of $Q$.
3. The corner triangle at $(0, 0)$ has vertices $(0, 0)$, $P_1$, $P_4$. Its legs lie on the sides of $Q$ and have lengths $a$ and $b$, so it is a copy of $T$. The same check works at the other three corners: for example, the triangle at $(a + b, 0)$ has the legs from $(a, 0)$ to $(a + b, 0)$ and from $(a + b, 0)$ to $(a + b, a)$, of lengths $b$ and $a$.
4. Each side of the quadrilateral $P_1 P_2 P_3 P_4$ is the hypotenuse of one corner triangle. Each corner triangle is a copy of $T$, so each side has length $c$.
5. The angle at $P_1$ is a right angle: the vectors $P_4 - P_1 = (-a, b)$ and $P_2 - P_1 = (b, a)$ have dot product $-ab + ab = 0$. The same computation works at $P_2$, $P_3$ and $P_4$.
6. So $P_1 P_2 P_3 P_4$ is a square of side $c$. The four triangles and this square cover $Q$ with no overlap, so $(a + b)^2 = 4 \cdot \frac{ab}{2} + c^2$.
7. Second picture: put two copies of $T$ together along the hypotenuse to make an $a \times b$ rectangle. Place one such rectangle on $[0, a] \times [0, b]$ and the other on $[a, a + b] \times [b, a + b]$.
8. The uncovered part of $Q$ is the square $[a, a + b] \times [0, b]$ of side $b$ and the square $[0, a] \times [b, a + b]$ of side $a$. So $(a + b)^2 = 4 \cdot \frac{ab}{2} + a^2 + b^2$.
9. Steps 6 and 8 give $4 \cdot \frac{ab}{2} + c^2 = 4 \cdot \frac{ab}{2} + a^2 + b^2$. We subtract $2ab$ from both sides and get $c^2 = a^2 + b^2$.
10. Check with $a = 3$ and $b = 4$: $(3 + 4)^2 = 49$, and $49 - 4 \cdot 6 = 25 = 5^2$, so $c = 5$.

## Remarks

The example shows that the picture rests on several facts that the eye accepts at once.
Steps 3 to 6 are the facts of the first picture, and steps 7 and 8 are the facts of the second picture.
Area is additive, congruent figures have equal areas, and the area of a rectangle is the product of its sides.

Step 5 is the place where Euclidean geometry enters.
In the plane with coordinates, the dot product shows the right angle.
In the classical proof, the angle at $P_1$ is $180°$ minus the two acute angles of $T$, and these two angles add up to $90°$ because the angles of a triangle add up to $180°$.
That fact needs the [[parallel postulate|2PC3XY0PYZ]], and on a sphere the Pythagorean theorem fails.

The algebra of step 6 alone also gives a proof: $(a + b)^2 = a^2 + 2ab + b^2$, so $c^2 = (a + b)^2 - 2ab = a^2 + b^2$.
This version uses only the first picture and the expansion of a square.
When $a = b$, the second picture has two equal squares, and the first picture has a tilted square whose corners are the midpoints of the sides of $Q$.

## Explanations

### L1 human

Take four equal right triangles with short sides $3$ and $4$ and long side $5$.
Put them in the corners of a $7 \times 7$ frame, so that their long sides make a tilted square in the middle.
The middle square has area $5 \times 5 = 25$.
Now slide the same four triangles into two rectangles of size $3 \times 4$.
The empty space is now a $3 \times 3$ square and a $4 \times 4$ square, with area $9 + 16 = 25$.
The triangles cover the same area in both frames, so the empty space is the same: $25 = 9 + 16$.

### L2 human

We check the picture for $a = 1$ and $b = 2$, so that $c^2$ should be $5$.

1. The big square has side $3$ and area $9$.
2. Each triangle has area $\frac{1 \cdot 2}{2} = 1$, so the four triangles have area $4$.
3. First picture: the tilted square has corners $(1, 0)$, $(3, 1)$, $(2, 3)$ and $(0, 2)$. Its side from $(1, 0)$ to $(3, 1)$ has length $\sqrt{4 + 1} = \sqrt{5}$, so its area is $5$, and $4 + 5 = 9$.
4. Second picture: the uncovered squares have areas $1^2 = 1$ and $2^2 = 4$, and $4 + 1 + 4 = 9$.
5. So both pictures account for the area $9$, and $c^2 = 5 = 1^2 + 2^2$.

The typical use of the picture is to explain the theorem in a first course, before or instead of Euclid's longer proof.
A trap is to assume that the middle figure is a square because it looks like one.
Step 5 of the example proves the right angles, and without it the argument has a gap.
