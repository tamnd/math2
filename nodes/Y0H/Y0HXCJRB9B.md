---
tag: Y0HXCJRB9B
kind: concept
name: Trivial, obvious and clearly
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [4M1FGQ0HNZ, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Triviality_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Triviality_(mathematics)
    locator: In mathematical reasoning
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof techniques
---

## Summary

"Trivial", "obvious", `clearly` and related phrases such as "by inspection" and "left to the reader" are [[jargon|4M1FGQ0HNZ]] words that mark a step or a case as easy.
The word "trivial" has two uses.
For an object or a solution, it names the simplest case, such as the zero solution of $A\mathbf{x} = \mathbf{0}$ or the group with one element, and this use is exact.
For a step in a proof, it is a judgement that the step needs no written argument, and this use depends on the reader.
These words matter because a hidden step can hide an error, and a reader must know when to fill the gap.

## Motivation

A [[mathematical proof|0B94TKFQJX]] for experts leaves out steps that every expert can supply.
The writer marks such a step with a word like "trivial", `clearly` or "by inspection", so that the reader knows a step is missing and that it is short.
Used well, the word saves space and keeps the main idea visible.
Used badly, it covers a step that the writer has not checked, and the reader is confused or misled.
A student must learn to read the word as an instruction: "check this, it should take a few lines".

## Notation

These words have no symbols.
The site does not use `obviously`, `clearly` or `it is easy to see` in its own text.
When the site calls a step routine, it also gives the step, or says which earlier result it uses.
The site uses "trivial" in its exact sense, for trivial objects, trivial solutions and trivial cases, and it says what the trivial object is.

## Remarks

### A list of the phrases

| Phrase | Usual meaning |
|---|---|
| trivial (object) | the simplest object with a given structure, such as the [[trivial group|0BNPC9850Y]] $\{e\}$ or the [[empty set|0ECVK59Y03]] |
| trivial (solution) | the simple solution that every equation of the family has, such as $\mathbf{x} = \mathbf{0}$ for $A\mathbf{x} = \mathbf{0}$ |
| trivial (case) | an easy case of a proof, such as a base case or the empty set, that the proof must still cover |
| trivial (step) | the step follows by definition, from a known result in one line, or as a special case of a general fact |
| nontrivial | not the trivial object or solution; or not easy to prove |
| obvious, `clearly` | the writer thinks the step needs no calculation for a reader with the right background |
| by inspection | the answer can be checked at a glance, such as the root $x = 1$ of $x^2 - 3x + 2$ |
| left to the reader, left as an exercise | the step is routine for an expert but longer than an obvious step |
| routine | the step uses only standard methods, with no new idea |

### Examples

1. [[The trivial solution of a homogeneous linear system|V38VZ7RZ7Q]]. Every system $A\mathbf{x} = \mathbf{0}$ has the solution $\mathbf{x} = \mathbf{0}$, and the question is whether a nontrivial one exists.
2. [[The trivial case n = 0 of the sum of the first n odd numbers|F70AX03B4X]]. The base case of an induction is easy, but the proof must still check it.
3. Every integer $N$ has the four trivial divisors $1$, $-1$, $N$ and $-N$. A divisor of $N$ other than these four is nontrivial, and $N > 1$ is prime exactly when it has no nontrivial divisor.
4. The [[Riemann zeta function|1XWBY4N0VT]] has zeros at $-2, -4, -6, \ldots$, called its trivial zeros. Here "trivial" means "known and simple to find", in contrast to the other zeros, which are the subject of the Riemann hypothesis.
5. The statement "every element of the empty set is an even number" is true, because there is no element to check. Such a [[vacuous truth|0V4QXPGJQK]] is a trivial case in the exact sense.

### Non-examples

1. [[The claim that n^2 + n + 41 is obviously prime for every n|DG60A13CSG]]. The claim is called obvious, but it is false at $n = 40$, so the word marks no correct step.
2. The function $y = e^x$ is not a trivial solution of $y' = y$. The trivial solution is $y = 0$, and $e^x$ is a nontrivial solution.
3. [[Fermat's Last Theorem|0Y5X3SDBCZ]] states that $a^n + b^n = c^n$ has no positive integer solutions for $n > 2$. The solution $a = b = c = 0$ is trivial, but the theorem itself is not trivial: its proof took more than 350 years.

### Basic properties

1. The exact use of "trivial" for objects and solutions does not depend on the reader. The zero vector is the trivial solution of $A\mathbf{x} = \mathbf{0}$ for everybody.
2. The use of "trivial" or "obvious" for a step depends on the reader. The integral $\int_0^1 x^2 \, dx = \frac{1}{3}$ is trivial after a course in calculus and is not obvious before one.
3. The use for a step also depends on the context. A proof in analysis may use without comment that every natural number has a successor, while a proof about the Peano axioms must prove or assume it.
4. A trivial case is still a case. A proof by induction or [[by cases|0WCP0PVET6]] is incomplete if it omits it.
5. "Left to the reader" marks a longer step than "obvious". It invites the reader to write a proof, not only to check a line.

### History

The word "trivial" comes from the medieval "trivium", the three basic subjects of grammar, logic and rhetoric, in contrast to the four harder subjects of the "quadrivium".
Writers have used "obvious" in proofs for a long time; Pierre-Simon Laplace used the French "évident".
A common joke among mathematicians says that a theorem becomes trivial once someone has proved it.
A related style, in which a writer calls a claim obvious to stop questions, is called [[proof by intimidation|~2649f267]].

### Common errors

1. A student writes "trivial" for a step that they have not checked. The step may be false, as the polynomial $n^2 + n + 41$ shows.
2. A student skips a trivial case, such as $n = 0$, the empty set or the zero vector. A theorem can fail exactly at the trivial case; for example, "every nonempty set of natural numbers has a least element" is false without the word "nonempty".
3. A student thinks that a step is wrong, or that they are weak, because they cannot see an obvious step at once. The word only claims that the step is short; the reader should write it down.
4. A student confuses "nontrivial" (not the trivial solution) with "difficult". A nontrivial solution can be easy to find, such as $\mathbf{x} = (2, -1)$ for $x + 2y = 0$.

## Explanations

### L1 human

When a mathematician says that something is "trivial" or "obvious", they mean that it is easy, at least for them.
Sometimes "trivial" has an exact meaning: the trivial solution of "$2x = 0$, $3x = 0$" is $x = 0$, the solution with nothing in it.
Other times it only means that the writer did not write a step.
If you meet the word and you do not see why the step holds, take a pencil and do the step.
It is normal to need a few lines for a step that a book calls obvious.

### L2 human

We fill an "obvious" step: "If $n$ is odd, then $n^2$ is `obviously` odd."

1. "Odd" means $n = 2k + 1$ for some integer $k$.
2. We square: $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$.
3. The number $2k^2 + 2k$ is an integer, so $n^2$ has the form $2m + 1$, and $n^2$ is odd.

The step took three lines, which is what "obvious" usually promises: a short check with the definitions.
The typical use of these words is to skip a calculation that the reader can do from the definitions.
A trap: a claim that looks obvious can be false, so test a few cases and then prove it, as the case $n = 40$ of $n^2 + n + 41$ shows.

### L3 human

The two uses of "trivial" behave differently in a formal setting.
The exact use names an object: the trivial group is the terminal and initial object of the category of groups, and the trivial solution of a linear system is the zero of its kernel.
The judgement use has no formal meaning, but proof assistants give a working version of it.
A step is "trivial" for a proof assistant when a standard automation, such as a decision procedure for linear arithmetic or a simplifier, closes it without help.
This shows the dependence on the reader in a precise form: what counts as trivial changes with the automation, just as it changes with the experience of a human reader.
Why some false statements look obvious, and some true ones look hard, is a question for the philosophy and the psychology of mathematics.
