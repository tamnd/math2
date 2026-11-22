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

A textbook writes "`clearly`, $n^2 + n$ is even for every integer $n$" and moves on.
The word promises that the step is short, not that it is absent.
Here the step is two lines: $n^2 + n = n(n + 1)$, and one of two consecutive integers is even, so the product is even.

"Trivial", "obvious", `clearly`, "by inspection" and "left to the reader" are [[jargon|4M1FGQ0HNZ]] words that mark a step or a case as easy.
The word "trivial" has two uses.
For an object or a solution, it names the simplest case, such as the zero solution of $A\mathbf{x} = \mathbf{0}$ or the group with one element, and this use is exact.
For a step in a proof, it is a judgment that the step needs no written argument, and this use depends on the reader.

## Motivation

A [[mathematical proof|0B94TKFQJX]] written for experts leaves out steps that every expert can supply.
The writer marks such a step with a word like "trivial" or "by inspection", so that the reader knows a step is missing and that it is short.
Used well, the word saves space and keeps the main idea in view.
Used badly, it covers a step that the writer never checked, and then the reader is misled.
So you should read each of these words as an instruction: "check this, it should take a few lines".

## Notation

These words have no symbols.
The site does not use `obviously`, `clearly` or `it is easy to see` in its own text; when it calls a step routine, it also gives the step or names the result that it uses.
The site uses "trivial" only in its exact sense, for trivial objects, solutions and cases, and it says what the trivial object is.

## Remarks

### Filling in the opening step

Go back to "$n^2 + n$ is even" and write the missing lines.
Factor first:
$$n^2 + n = n(n + 1).$$
Of the two consecutive integers $n$ and $n + 1$, one is even.
If $n = 2k$, the product is $2k(n + 1)$, and if $n + 1 = 2k$, the product is $2kn$; both are even.
Check: $n = 5$ gives $25 + 5 = 30$, and $n = -4$ gives $16 - 4 = 12$.
The step needs two lines and one fact about parity, which is what `clearly` usually promises.

### Two meanings of "trivial"

The same word does two different jobs, and the noun after it tells you which.
In "the system $A\mathbf{x} = \mathbf{0}$ has the trivial solution", the word names one object, $\mathbf{x} = \mathbf{0}$, and every reader agrees on it, as [[the trivial solution of a homogeneous linear system|V38VZ7RZ7Q]] shows.
In "the proof of the lemma is trivial", the word judges a piece of work, and the judgment depends on the reader.
The integral $\int_0^1 x^2 \, dx = \frac{1}{3}$ is trivial after a calculus course and is not obvious before one.

When "trivial" sits before an object word (group, solution, zero, divisor, case), read it as exact.
Every integer $N$ has the four trivial divisors $1$, $-1$, $N$ and $-N$, and $N > 1$ is prime exactly when it has no other divisor.
The [[Riemann zeta function|1XWBY4N0VT]] has its trivial zeros at $-2, -4, -6, \ldots$, which are simple to find, unlike the zeros that the Riemann hypothesis is about.
When it sits before a word for work (proof, step, check), read it as a judgment and fill the gap.

### What the phrases promise

The phrases form a scale of effort.
"By inspection" promises a check at a glance, such as the root $x = 1$ of $x^2 - 3x + 2$, since $1 - 3 + 2 = 0$.
"Obvious" and `clearly` promise a few lines from the definitions.
"Routine" promises standard methods with no new idea, and the work may be long.
"Left to the reader" or "left as an exercise" promises a step that an expert can do, but it may take a page.
"Nontrivial" has two readings again: "not the trivial object", as in a nontrivial solution, or "hard to prove", as in a nontrivial theorem.

### Trivial cases still count

A trivial case is easy, but a proof must still cover it.
[[The trivial case n = 0 of the sum of the first n odd numbers|F70AX03B4X]] shows a base case of one line that the induction cannot do without.
A [[vacuous truth|0V4QXPGJQK]], such as "every element of the empty set is even", is a trivial case in the exact sense, and a theorem can turn on it.
"Every set of natural numbers has a least element" is false, and it fails exactly at the trivial case, the empty set.

### When the words hide a gap

[[The claim that n^2 + n + 41 is obviously prime for every n|DG60A13CSG]] calls a false statement obvious, since $40^2 + 40 + 41 = 41^2$.
The word cannot make a false step true, so it marks no correct step at all.
Calling a claim obvious to stop questions has its own name, [[proof by intimidation|D8A1K052XV]].

The exact sense can be misapplied too.
The function $y = e^x$ is not the trivial solution of $y' = y$; the trivial solution is $y = 0$.
For [[Fermat's Last Theorem|0Y5X3SDBCZ]], the solution $a = b = c = 0$ of $a^n + b^n = c^n$ is trivial, but the theorem itself, which excludes positive solutions for $n > 2$, is not.

### Watch out

The first error is to write "trivial" for a step that you have not checked.
Test the claim on a few cases, then write the lines, as the case $n = 40$ of $n^2 + n + 41$ shows.

The second error is to think that you are weak because you cannot see an obvious step at once.
The word only claims that the step is short, and it is normal to need a few lines on paper.

The third error is to read "nontrivial" as "difficult".
The nontrivial solution $(x, y) = (2, -1)$ of $x + 2y = 0$ takes one second to find.

### History

The English word "trivial" goes back to the Latin "trivialis", which meant "commonplace", from "trivium", a place where three roads meet.
In medieval schools the "trivium" was also the name of the three basic subjects, grammar, logic and rhetoric.

### Try it

First, fill the step "`clearly`, the product of three consecutive integers is divisible by $3$".
Among $n$, $n + 1$, $n + 2$ the remainders modulo $3$ are $0$, $1$, $2$ in some order, so one factor is a multiple of $3$, and so is the product.

Second, say which meaning of "trivial" is used in "the kernel of an injective homomorphism is trivial".
It is the exact one: the kernel is the trivial subgroup $\{e\}$.

## Explanations

### L1 human

When a mathematician says that something is "trivial" or "obvious", they mean that it is easy, at least for them.
Sometimes "trivial" has an exact meaning: the trivial solution of "$2x = 0$ and $3x = 0$" is $x = 0$, the answer that is always there.
Other times it only means that the writer skipped a step.
If you meet the word and you do not see why the step holds, take a pencil and do the step.
It is normal to need a few lines for a step that a book calls obvious.

### L2 human

Fill the step "if $n$ is odd, then $n^2$ is `obviously` odd".
"Odd" means $n = 2k + 1$ for some integer $k$, so square it:
$$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.$$
The number $2k^2 + 2k$ is an integer, so $n^2$ has the form $2m + 1$, and $n^2$ is odd.
Check: $n = 7$ gives $49 = 2 \cdot 24 + 1$.
The step took three lines and used only the definition, which is what "obvious" should mean in a written proof.
Watch out: a claim that looks obvious can be false, so test it before you fill it in.

### L3 human

The two uses of "trivial" behave differently in a formal setting.
The exact use names an object: the trivial group is both an initial and a terminal object in the category of groups, and the trivial solution of a linear system is the zero vector of its kernel.
The judgment use has no formal meaning, but proof assistants give it a working version.
A step is trivial for a proof assistant when standard automation, such as a decision procedure for linear arithmetic or a simplifier, closes it without help.
This makes the dependence on the reader precise: what counts as trivial changes with the automation, just as it changes with the experience of a human reader.
