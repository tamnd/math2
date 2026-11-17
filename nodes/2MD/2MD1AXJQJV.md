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

The picture: a continuous curve that starts below the horizontal axis and ends above it must cross the axis.
This is the [[intermediate value theorem|00KAFBR32E]], and [[intuition|4BT08RE4CR]] finds it true at once.
We test what the intuition uses.

1. The statement: if $f \colon [a, b] \to \mathbb{R}$ is continuous with $f(a) < 0 < f(b)$, then $f(c) = 0$ for some $c \in [a, b]$.
2. The same statement over the rationals: if $f \colon [a, b] \cap \mathbb{Q} \to \mathbb{Q}$ is continuous with $f(a) < 0 < f(b)$, then $f(c) = 0$ for some rational $c$.
3. Test it with $f(x) = x^2 - 2$ on $[0, 2] \cap \mathbb{Q}$. Then $f(0) = -2 < 0$ and $f(2) = 2 > 0$, and $f$ is continuous, being a polynomial.
4. A zero would be a rational $c$ with $c^2 = 2$. By the [[irrationality of the square root of 2|0DZGSDHD92]], there is none. So the statement fails over $\mathbb{Q}$.
5. The two pictures look the same: the graph of $x^2 - 2$ over $\mathbb{Q}$ is the real graph with the irrational points removed, and the eye cannot see the missing points.
6. So the intuition uses a property of $\mathbb{R}$ that $\mathbb{Q}$ lacks. The proof names it: let $c = \sup \{ x \in [a, b] : f(x) < 0 \}$, which exists by the [[completeness of the real numbers|E3CPZNJZNG]], and continuity rules out both $f(c) < 0$ and $f(c) > 0$.

The intuition was right for $\mathbb{R}$, and it guided the search for a proof; the proof then found the hidden hypothesis.

## Remarks

The intermediate value theorem is equivalent to completeness: an ordered field in which every continuous function on an interval has the intermediate value property is complete.
Bolzano gave a proof in 1817 from a form of the least upper bound property, at a time when many authors regarded the statement as evident from geometry.
The example shows a typical pattern: an intuition based on a picture is right, but it rests on an unstated property of the setting, and it fails when the setting changes.
The same intuition fails for functions that are not continuous: $f(x) = -1$ for $x < 1$ and $f(x) = 1$ for $x \geq 1$ jumps over $0$ on $[0, 2]$.

## Explanations

### L1 human

If we walk from the bottom of a valley to the top of a hill without jumping, we must pass every height in between.
This is the intermediate value theorem, and it feels obvious.
But it depends on the line having no gaps.
If we allowed only fractions as positions, there would be gaps, for example at the point whose square is $2$.
A path could then go from below sea level to above it without ever being exactly at sea level.
So the "obvious" picture uses a fact about real numbers, which needs to be stated and proved.

### L2 human

We locate the gap in $\mathbb{Q}$ by bisection on $f(x) = x^2 - 2$.

1. $f(1) = -1 < 0$ and $f(2) = 2 > 0$, so we look in $[1, 2]$.
2. $f(1.5) = 0.25 > 0$: the interval becomes $[1, 1.5]$.
3. $f(1.25) = -0.4375 < 0$: the interval becomes $[1.25, 1.5]$.
4. $f(1.375) = -0.109375 < 0$: the interval becomes $[1.375, 1.5]$.
5. Each step halves the interval, and all endpoints are rational. The intervals shrink to the single real number $\sqrt{2}$, which is not rational.

The typical use: bisection turns the intuition into an algorithm, and the existence of the limit of the endpoints is exactly completeness.

A trap: the endpoints of the intervals form a Cauchy sequence of rationals, and its convergence in $\mathbb{Q}$ fails; checking only the sign changes does not show this.
