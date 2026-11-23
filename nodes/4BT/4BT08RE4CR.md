---
tag: 4BT08RE4CR
kind: concept
name: Mathematical intuition
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: research
uses: [0B94TKFQJX, 6KCEWEP4WA, 5V35SGEN1T]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_intuition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9
    locator: Character
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Proof
---

## Summary

Mathematical intuition is the ability to judge, before a proof, that a statement is likely true, that a method will work, or which way to go.
It is the guide that chooses what to try, and it is also a risk, because it can be wrong and only a proof settles a claim.

Here is intuition at work on a real problem: what is the area of a disc of radius $r$, if you know that its circumference is $2\pi r$?
A first attempt with squares on graph paper gives only an estimate, and no formula.
The helping move is a picture.
Cut the disc into many thin sectors, like slices of a cake, and lay them in a row, point up and point down in turn.
The row looks almost like a rectangle whose height is the radius $r$ and whose length is half the circumference, $\pi r$.
So intuition says
$$\text{area} = \pi r \cdot r = \pi r^2.$$
The answer is right, and the picture even explains it.
But the picture skips a step: the area of the limit shape need not be the limit of the areas, and a proof must supply a reason, as [[the area of a disc by rearranging sectors|N96C8N6WBH]] does with polygons inside and outside the disc.

Intuition rests on experience: on pictures, physical models, many worked examples and patterns seen before.
What it gives is a belief and a direction, not a [[proof|0B94TKFQJX]], and it can fail for infinite sets, for high dimensions, for probability, and for objects built to defeat it.

## Motivation

From the axioms and the known theorems, a proof could go in very many directions, and most of them lead nowhere.
Mathematicians do not search blindly: they expect some statements to be true and some methods to work, often before they can say why.
Poincaré stressed that logic is the tool of proof and intuition the tool of invention, and every [[heuristic|6KCEWEP4WA]] needs intuition to decide which move fits.

At the same time, nineteenth-century analysis showed intuition failing again and again.
Continuous functions turned out to have no derivative anywhere, curves turned out to fill a square, and convergent series of continuous functions turned out to have discontinuous sums.
So intuition raises two questions: how to use it, and when to distrust it.

## Notation

Books separate several kinds of intuition.
Geometric intuition uses pictures, such as a graph that crosses an axis.
Physical intuition uses models, such as a soap film that makes its area small or a string that takes the shortest path.
Formal intuition is a sense of which manipulations of a formula will simplify it, built from many calculations.
Poincaré also spoke of an intuition of pure number, the immediate grasp that a simple step, such as induction, is valid.

## Remarks

### A picture that hides a hypothesis

A continuous curve that starts below the axis and ends above it must cross the axis.
That is the [[intermediate value theorem|00KAFBR32E]], and intuition accepts it at once.
Over the rational numbers the same statement fails: $f(x) = x^2 - 2$ is continuous on $[0, 2] \cap \mathbb{Q}$, with $f(0) = -2$ and $f(2) = 2$, and it has no rational zero.
The pictures over $\mathbb{R}$ and over $\mathbb{Q}$ look the same, so the intuition rests on a property that the eye cannot see, the [[completeness of the real numbers|E3CPZNJZNG]].
[[The intuition behind the intermediate value theorem|2MD1AXJQJV]] works this out.

### A sense of scale that fails

A rope lies tightly around the equator, and you make it $1$ meter longer and raise it evenly all around.
Intuition says that the gap is microscopic, since $1$ meter is tiny next to $40\,000$ kilometers.
Write the circumference as $C = 2\pi R$, and the extra length gives
$$2\pi (R + h) - 2\pi R = 2\pi h = 1, \qquad h = \frac{1}{2\pi} \approx 0.16 \text{ meters}.$$
The radius cancels, so the gap is the same for a tennis ball and for the Earth.
Intuition answered a question about proportions, and the problem asked about an absolute change; [[the rope around the Earth|E60YNV0K8Q]] gives the details.

### More failures, and what they teach

The graph of a continuous function looks smooth with a few corners, but the [[Weierstrass function|01A0MK1730]] is continuous and has no derivative at any point.
A curve seems to have no area, but a [[space-filling curve|QPRHC4DZ20]] is a continuous image of a segment that fills a square.
Probability defeats intuition in the [[birthday problem|0NMWG2PHJ0]], since the number of pairs of people grows like the square of the number of people.

Each failure points to a hidden assumption.
A proof then makes the assumption explicit, as completeness in the intermediate value theorem.
Intuition is local: it is reliable where it was trained and unreliable in new settings, such as infinite sets or high dimensions.

### Intuition that guides

Intuition is often right, and then it saves a great deal of work.
A symmetric problem suggests a symmetric answer: the rectangle of largest area with perimeter $4$ should be the unit square.
The inequality $xy \le \left( \frac{x + y}{2} \right)^2$, which is $(x - y)^2 \ge 0$ in disguise, confirms it, and [[symmetry arguments|H840D9TM2X]] explain it.
Euler guessed $\sum 1/k^2 = \pi^2/6$ by treating $\frac{\sin x}{x}$ as a polynomial, an intuition by [[analogy|7PBNK2E6DC]] that later proofs confirmed.

### Training intuition

Intuition grows with experience, and some habits help it grow.
Work many examples by hand and draw them, and study the standard counterexamples, asking which intuition each one breaks.
Estimate an answer before you compute it, and compare.
After each problem, ask whether the result was expected and why, which is the "looking back" phase of [[Pólya's four steps|DYD57G2Y5Z]].

### Watch out

Do not accept a statement because it "must be true".
Intuition gives a [[conjecture|WMEMMHZ3BH]], and a proof is still needed.

Do not reject a proved result because it surprises you either: then the intuition must change, not the theorem.
A common case is the finite intuition that a set is larger than each of its proper subsets.
It fails for infinite sets: the even numbers are a proper subset of the natural numbers, and $n \mapsto 2n$ matches the two sets one to one.

### History

Poincaré wrote on the roles of logic and intuition in mathematics, and the psychologist Édouard Toulouse published a study of Poincaré's way of working in 1910.
Felix Klein and Poincaré both defended geometric intuition while Weierstrass and others rebuilt analysis on arithmetic definitions.
The Bourbaki group, from the 1930s, wrote in an axiomatic style with very few pictures.
William Thurston, in "On proof and progress in mathematics" (1994), argued that what mathematicians produce and pass on is understanding, and not only formal proofs.

### Try it

You raise the rope around a ball of radius $10$ centimeters by adding $1$ meter; what is the gap?
The same $\frac{1}{2\pi} \approx 0.16$ meters, because the radius cancels.

Your intuition says that a continuous function on $[0, 1]$ with $f(0) = 0$ and $f(1) = 1$ takes the value $\frac{1}{2}$; is that right, and what does it use?
It is right by the intermediate value theorem, and it uses the completeness of $\mathbb{R}$.

## Explanations

### L1 human

Intuition is the feeling that something is true before we can show it.
It comes from experience, as a carpenter knows that a shelf will hold before doing any calculation.
In mathematics it tells us what to try and what to expect, but it can be wrong.
If a rope fits tightly around the Earth and we make it $1$ meter longer, most people think it lifts by less than a hair.
In fact it lifts by about $16$ centimeters all around.
So mathematicians use intuition to find ideas and proofs to check them.

### L2 human

Test the intuition that a continuous function on $[0, 1]$ is differentiable at most points.
It comes from pictures, since the graphs we draw are smooth with a few corners.
The function $|x - \frac{1}{2}|$ agrees with it: it is continuous, with one corner at $\frac{1}{2}$.
Now take the Weierstrass function
$$W(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x), \qquad 0 < a < 1, \quad b \text{ an odd integer}, \quad ab > 1 + \frac{3\pi}{2}.$$
It is continuous, because the series converges uniformly, and Weierstrass proved that it has no derivative at any point.
So continuity controls the size of changes, not their rate, and a smooth picture is a special case.
Test an intuition on the standard counterexamples of the field before you rely on it.
Watch out: one counterexample can breed a new false intuition, such as "most continuous functions are smooth", while in the sense of Baire category most continuous functions are nowhere differentiable.

### L3 human

Mathematics often formalizes an intuition after the fact.
The intuition of nearness became topology, the intuition of size became measure theory, and the intuition of chance became probability theory, each with theorems that test the intuition.
The [[psychology of mathematical invention|XMGGTNSTYC]] studies how intuition works in discovery, [[plausible reasoning and experimental mathematics|DME0TPC348]] treats evidence weaker than proof, and [[rigor and the acceptance of proofs|1BTHSHST4M]] treats the passage from an intuitive argument to an accepted proof.
Gödel compared the intuition of mathematical objects to sense perception, a question that belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
