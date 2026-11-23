---
tag: XNMYYT867E
kind: example
name: Similar figures on the sides of a right triangle
msc: ["00A35", "51M04"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [Y896GWYF8A]
uses: [Y896GWYF8A, 0VP3A1290K, 0YF6QXXWB5, 060ZVZBV3E]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_theorem
    locator: Similar figures on the three sides
  - book: isbn:9780691164076
---

## Example

We start from the [[Pythagorean theorem|0VP3A1290K]].
In a right triangle with legs $a$ and $b$ and hypotenuse $c$, the squares on the sides satisfy $a^2 + b^2 = c^2$.
We pose new problems by [[problem posing|Y896GWYF8A]], and we first list the attributes of the theorem.
The triangle has a right angle, the figures on the sides are squares, the figures are built outward, and the relation is between areas.

"What if the figures are not squares, but equilateral triangles?" poses a new question.
Is the area of the equilateral triangle on the hypotenuse the sum of the areas of the equilateral triangles on the legs?
A first attempt uses the $3$-$4$-$5$ triangle and tries to compute the three areas from heights, which brings in $\sqrt{3}$ three times and hides the pattern.
The helping move is to write the area of an equilateral triangle of side $s$ as a constant times $s^2$, namely $\frac{\sqrt{3}}{4} s^2$.
Then the question is whether
$$\frac{\sqrt{3}}{4} a^2 + \frac{\sqrt{3}}{4} b^2 = \frac{\sqrt{3}}{4} c^2,$$
and this follows from $a^2 + b^2 = c^2$ on multiplying by $\frac{\sqrt{3}}{4}$.
For the $3$-$4$-$5$ triangle both sides equal $\frac{25\sqrt{3}}{4}$.

"What if they are semicircles?" gets the same treatment.
A semicircle on a segment of length $s$ has area $\frac{\pi}{8} s^2$, so $\frac{\pi}{8} a^2 + \frac{\pi}{8} b^2 = \frac{\pi}{8} c^2$.

The two answers pose a general question: for which figures does the relation hold?
It holds for any three [[similar|0YF6QXXWB5]] figures placed on the three sides, with the sides as corresponding segments.
Similar figures with corresponding lengths $a$, $b$ and $c$ have areas $k a^2$, $k b^2$ and $k c^2$ for one constant $k$, and $k a^2 + k b^2 = k c^2$.

## Remarks

The general version is Proposition 31 of Book VI of Euclid's *Elements*.
It also gives a proof of the original theorem, by a good choice of figure.
Drop the altitude from the right angle to the hypotenuse.
It cuts the triangle into two triangles that are similar to the whole, with hypotenuses $a$ and $b$.
These two triangles are similar figures on the sides $a$ and $b$, the whole triangle is the similar figure on $c$, and the two parts fill the whole.
So $k a^2 + k b^2 = k c^2$ for the constant $k > 0$ of this family, and so $a^2 + b^2 = c^2$.
The general problem is easier to prove than the special one, an instance of the [[inventor's paradox|FVRKDXBJF6]].

"What if the angle is not a right angle?" poses a different problem.
The [[law of cosines|060ZVZBV3E]] answers it: $c^2 = a^2 + b^2 - 2ab \cos C$, where $C$ is the angle opposite $c$.

## Explanations

### L1 human

The Pythagorean theorem is often drawn with squares on the three sides of a right triangle.
The big square has the same area as the two small squares together.
Now ask what happens if we draw triangles with equal sides instead of squares.
Or half circles?
The same rule holds, and the big shape has the same area as the two small ones.
In fact, it works for any shape, as long as the three shapes are copies of one another at different sizes.

### L2 human

We test the general claim on the $5$-$12$-$13$ right triangle with semicircles.
The check $25 + 144 = 169 = 13^2$ confirms that the triangle has a right angle.
The semicircles on the legs have areas $\frac{\pi}{8} \cdot 25$ and $\frac{\pi}{8} \cdot 144$, with sum $\frac{\pi}{8} \cdot 169$.
The semicircle on the hypotenuse has area $\frac{\pi}{8} \cdot 13^2 = \frac{\pi}{8} \cdot 169$, so the areas agree.
Figures that are not similar fail.
Squares on the legs and an equilateral triangle on the hypotenuse give $25 + 144 = 169$ against $\frac{\sqrt{3}}{4} \cdot 169 \approx 73.2$.
After a theorem, vary one attribute, solve the variant, and look for the general statement that covers all the variants.
Watch out: the three figures must be similar to one another with the sides as corresponding lengths, and rectangles of different proportions on the three sides do not satisfy the relation.
