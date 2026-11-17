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

Mathematical intuition is the ability to judge, before or without a [[proof|0B94TKFQJX]], that a statement is likely true, that a method will work, or which way to go in a problem.
It rests on experience: on pictures, on physical models, on many worked examples and on patterns seen before.
Intuition is a guide: it chooses conjectures, proof strategies and [[heuristics|6KCEWEP4WA]].
It is also a risk: it fails for infinite sets, for high dimensions, for probability and for objects built to defeat it, and only a proof settles a claim.
The idea matters because research and problem solving need a sense of direction that logic alone does not give, and because a trained intuition is a large part of mathematical skill.

## Motivation

From the axioms and the known theorems, a proof can go in very many directions, and most of them lead nowhere.
Mathematicians do not search blindly: they expect some statements to be true and some methods to work, often before they can say why.
Poincaré stressed that logic is the tool of proof and intuition the tool of invention.
At the same time, the history of analysis in the nineteenth century showed intuition failing again and again: continuous functions without derivatives, curves that fill a square, convergent series of continuous functions with a discontinuous sum.
So the question of intuition has two sides: how to use it, and when to distrust it.

## Remarks

### Kinds of intuition

- Geometric intuition: the use of pictures, such as a graph that crosses an axis or a surface that can be cut and flattened.
- Physical intuition: the use of physical models, such as a soap film that minimizes area or a stretched string that takes the shortest path.
- Algebraic or formal intuition: a sense of which manipulations of formulas will simplify an expression, built from many calculations.
- Logical intuition: the immediate grasp that a simple inference is valid, which Poincaré distinguished from the other kinds.

### Examples

1. [[The intuition behind the intermediate value theorem|2MD1AXJQJV]]: a continuous curve from below the axis to above it must cross the axis. The intuition is right for real numbers, but it hides the completeness of $\mathbb{R}$, and it fails over $\mathbb{Q}$.
2. [[The area of a disc by rearranging sectors|N96C8N6WBH]]: cutting a disc into thin sectors and laying them side by side suggests a rectangle of sides $\pi r$ and $r$, hence the area $\pi r^2$.
3. A symmetric problem has a symmetric answer: the rectangle of greatest area with a given perimeter is a square. Here the intuition is right, and a proof by [[symmetry arguments|H840D9TM2X]] or by the inequality $xy \leq \left(\frac{x + y}{2}\right)^2$ confirms it.
4. Euler's guess of $\sum 1/k^2 = \pi^2/6$ by an [[analogy|7KDT0R1HF2]] between $\frac{\sin x}{x}$ and a polynomial was an intuition, confirmed by later proofs.

### Non-examples

1. [[A rope around the Earth, made 1 metre longer|E60YNV0K8Q]]: intuition says that the rope rises by a tiny amount, but the gap is $\frac{1}{2\pi} \approx 0.16$ metres for every radius.
2. [[A continuous nowhere differentiable function|0RXK2Z808Q]], such as the [[Weierstrass function|01A0MK1730]]: the picture of a continuous curve suggests a smooth curve with corners at a few points, but the function has no derivative at any point.
3. A [[space-filling curve|QPRHC4DZ20]]: a continuous image of a segment can fill a square, against the intuition that a curve has no area.
4. The [[Banach-Tarski paradox|FH250K068Z]] and the [[birthday problem|0NMWG2PHJ0]]: volume and probability behave against intuition, in the first case because of non-measurable pieces, in the second because the number of pairs grows like the square of the number of people.

### Basic properties

1. Intuition gives belief, not proof: a claim supported by intuition alone is a [[conjecture|WMEMMHZ3BH]].
2. Intuition is trained by experience. It improves with examples, with [[non-examples|F3NNR77WKP]] and with the counterexamples that break it.
3. Intuition is local: it is reliable in the settings where it was trained, and it fails in new settings, such as infinite sets or high dimensions.
4. A failure of intuition often points to a hidden hypothesis, which a proof then makes explicit, as completeness in the intermediate value theorem.
5. Intuition and rigour are not opposed. A proof often confirms and sharpens an intuition, and a new proof can create a new intuition.

### Training intuition

- Work many examples by hand, and draw them.
- Look for the reason of each step, not only its correctness.
- Study the standard counterexamples, and ask which intuition each one breaks.
- After each solved problem, ask whether the result was expected, and why (the "look back" step of [[Pólya's four steps|DYD57G2Y5Z]]).
- Estimate an answer before computing it, and compare.

### History

Poincaré wrote on the roles of logic and intuition in mathematics, and a study of his way of working by the psychologist Édouard Toulouse appeared in 1910.
Felix Klein and Poincaré both defended geometric intuition at a time when Weierstrass and others were rebuilding analysis on arithmetic definitions.
The Bourbaki group, from the 1930s, wrote in an axiomatic style with very few pictures.
Later authors, such as William Thurston in "On proof and progress in mathematics" (1994), stressed that understanding and intuition, and not only formal proof, are what mathematicians produce and pass on.

### Common errors

1. Accepting a statement because it "must be true". Intuition gives a conjecture; a proof is still needed.
2. Rejecting a proved result because it is counterintuitive. The intuition must change, not the theorem.
3. Using intuition trained in finite settings for infinite sets, as in "a set is larger than each of its proper subsets".

## Explanations

### L1 human

Intuition is the feeling that something is true before we can show it.
It comes from experience, as a carpenter knows that a shelf will hold before doing any calculation.
In mathematics, it tells us what to try and what to expect.
But it can be wrong.
If we wrap a rope tightly around the Earth and then make it $1$ metre longer, most people think the rope will lift by less than a hair.
In fact it lifts by about $16$ centimetres all around.
So mathematicians use intuition to find ideas, and proofs to check them.

### L2 human

We test an intuition and correct it: "a function that is continuous on $[0, 1]$ is differentiable at most points".

1. The intuition comes from pictures: the graphs we draw are smooth, with a few corners.
2. Test with $|x - \frac{1}{2}|$: continuous, differentiable except at $\frac{1}{2}$. Consistent with the intuition.
3. Test with the Weierstrass function $\sum_{n=0}^{\infty} a^n \cos(b^n \pi x)$ with $0 < a < 1$ and $b$ an odd integer such that $ab > 1 + \frac{3\pi}{2}$: it is continuous, since the series converges uniformly, and Weierstrass proved that it has no derivative at any point.
4. Correction: continuity controls the size of changes, not their rate. A smooth picture is a special case.

The typical use: test an intuition on the standard counterexamples of the field before relying on it.

A trap: correcting an intuition by one counterexample may produce a new false intuition, such as "most continuous functions are smooth"; in a precise sense (Baire category), most continuous functions are nowhere differentiable.

### L3 human

The study of intuition sits between mathematics, psychology and the philosophy of mathematics.
Within mathematics, intuition is often formalized after the fact: the intuition of nearness became topology, the intuition of size became measure, and the intuition of chance became probability theory, each with theorems that test the intuition.
The [[psychology of mathematical invention|XMGGTNSTYC]] studies how intuition works in discovery, the topic [[plausible reasoning and experimental mathematics|DME0TPC348]] treats evidence that is weaker than proof, and the topic [[rigour and the acceptance of proofs|1BTHSHST4M]] treats the passage from an intuitive argument to an accepted proof.
In the philosophy of mathematics, Gödel compared the intuition of mathematical objects to sense perception; this question belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
