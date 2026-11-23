---
tag: 2MD1AXJQJV
kind: example
name: The intuition behind the intermediate value theorem and the completeness it hides
msc: ["00A35", "26A15"]
topics: [X1NSTVGDNQ]
audience: research
instance_of: [4BT08RE4CR]
uses: [4BT08RE4CR, 00KAFBR32E, E3CPZNJZNG, 0DZGSDHD92]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Proof
---

## Example

A continuous curve that starts below the horizontal axis and ends above it must cross the axis.
This is the [[intermediate value theorem|00KAFBR32E]], and [[intuition|4BT08RE4CR]] accepts it at once.
We test what the intuition uses.

1. The statement over the reals says: if $f \colon [a, b] \to \mathbb{R}$ is continuous and $f(a) < 0 < f(b)$, then $f(c) = 0$ for some $c$ in $[a, b]$.
2. The same statement over the rationals says: if $f \colon [a, b] \cap \mathbb{Q} \to \mathbb{Q}$ is continuous and $f(a) < 0 < f(b)$, then $f(c) = 0$ for some rational $c$.
3. We test it with $f(x) = x^2 - 2$ on $[0, 2] \cap \mathbb{Q}$, which is continuous because it is a polynomial, with $f(0) = -2 < 0$ and $f(2) = 2 > 0$.
4. A zero would be a rational $c$ with $c^2 = 2$, and by the [[irrationality of the square root of 2|0DZGSDHD92]] there is none, so the statement fails over $\mathbb{Q}$.
5. The two pictures look the same, because the graph of $x^2 - 2$ over $\mathbb{Q}$ is the real graph with the irrational points removed, and the eye cannot see the missing points.
6. So the intuition uses a property of $\mathbb{R}$ that $\mathbb{Q}$ lacks, and the proof names it.
   Let $c = \sup \{ x \in [a, b] : f(x) < 0 \}$, which exists by the [[completeness of the real numbers|E3CPZNJZNG]].
   Continuity rules out both $f(c) < 0$ and $f(c) > 0$, so $f(c) = 0$.

The intuition was right for $\mathbb{R}$, and it guided the search for a proof.
The proof then found the hypothesis that the intuition had hidden.

## Remarks

The intermediate value theorem is in fact equivalent to completeness: an ordered field in which every continuous function on an interval has the intermediate value property is complete.
Bolzano gave a proof in 1817 from a form of the least upper bound property, when many authors still took the statement as evident from geometry.

The example shows a common pattern.
An intuition based on a picture is right, but it rests on an unstated property of the setting, and it fails when the setting changes.
It also fails when a hypothesis changes: the function with $f(x) = -1$ for $x < 1$ and $f(x) = 1$ for $x \ge 1$ is not continuous, and it jumps over $0$ on $[0, 2]$.

## Explanations

### L1 human

If you walk from the bottom of a valley to the top of a hill without jumping, you pass every height in between.
This is the intermediate value theorem, and it feels obvious.
But it depends on the line having no gaps.
If only fractions were allowed as positions, there would be a gap at the point whose square is $2$.
A path could then go from below sea level to above it without ever being exactly at sea level.
So the picture uses a fact about real numbers, and that fact must be stated and proved.

### L2 human

We can find the gap in $\mathbb{Q}$ by bisection on $f(x) = x^2 - 2$.
Since $f(1) = -1 < 0$ and $f(2) = 2 > 0$, we start with $[1, 2]$.
Then the midpoints give
$$f(1.5) = 0.25 > 0, \qquad f(1.25) = -0.4375 < 0, \qquad f(1.375) = -0.109375 < 0,$$
so the interval shrinks to $[1, 1.5]$, then $[1.25, 1.5]$, then $[1.375, 1.5]$.
Each step halves the interval, and every endpoint is rational.
The intervals shrink to one real number, $\sqrt{2}$, which is not rational.
Bisection turns the intuition into an algorithm, and the existence of the limit of the endpoints is exactly completeness.
Watch out: the endpoints form a Cauchy sequence of rationals with no rational limit, and checking only the sign changes does not reveal this.
