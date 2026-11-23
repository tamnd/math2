---
tag: F8BP8S0RYG
kind: example
name: The fallacy of the undistributed middle
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
not_instance_of:
  - target: MZBNX2T6Q6
    note: the form AAA-2 has an instance with true premises and a false conclusion (rectangles, squares, parallelograms), so the conclusion does not follow and the argument is not a valid syllogism
  - target: AC6XQ4KRNT
    note: the middle term is the predicate of both premises, so the form is AAA-2 and not AAA-1; it is also invalid
uses: [MZBNX2T6Q6, AC6XQ4KRNT, KSJ9W29KXQ, S4BTTGFR6J, 0KCT6DPXJK, J7KFCFQRBT]
sources:
  - url: https://en.wikipedia.org/wiki/Fallacy_of_the_undistributed_middle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
---

## Example

The form is AAA in the second figure: all $P$ are $M$, all $S$ are $M$, so all $S$ are $P$.
An instance: all squares are parallelograms, all rectangles are parallelograms, so all rectangles are squares.
We show that the argument has the shape of a categorical syllogism but is not valid.

1. The conclusion has subject $S$ (rectangles) and predicate $P$ (squares), and $M$ (parallelograms) occurs in both premises, so there are exactly three [[terms|KSJ9W29KXQ]].
2. $M$ is the predicate of both premises, so the [[figure|S4BTTGFR6J]] is the second and the mood is AAA.
3. The predicate of an A proposition is not distributed, so $M$ is distributed in neither premise, and the first rule of validity fails.
4. For a countermodel, take the rectangle $R$ with sides $1$ and $2$.
5. Every square and every rectangle is a parallelogram, so both premises are true.
6. $R$ is a rectangle and not a square, because its sides differ, so the conclusion is false.
7. A [[Venn diagram|0KCT6DPXJK]] shows the gap.
   The premises shade $S \bar M P$, $\bar S \bar M P$ and $S \bar M \bar P$, but the conclusion needs $S M \bar P$ to be empty, and nothing shades it; $R$ lies there.

Since one instance has true premises and a false conclusion, the conclusion does not follow from the premises.

## Remarks

The premises only say that $S$ and $P$ both lie inside $M$.
Two sets inside a common set can stand in any relation to each other: equal, nested, overlapping or disjoint.
The error is close to [[affirming the consequent|J7KFCFQRBT]]: for an $x$ in $S$ we know "$x \in M$" and "if $x \in P$ then $x \in M$", and the argument concludes "$x \in P$".

Small changes repair the form.
Reverse the major premise to "all $M$ are $P$" and the form becomes [[Barbara|AC6XQ4KRNT]].
Replace the minor premise by "no $S$ is $M$" and the form becomes Camestres (AEE-2), which validly concludes "no $S$ is $P$".

## Explanations

### L1 human

"All cats have four legs, and all dogs have four legs, so all dogs are cats" is wrong, and everybody sees it.
The same mistake is harder to see with true sentences: "all squares are parallelograms, all rectangles are parallelograms, so all rectangles are squares".
Both premises only say that squares and rectangles belong to the big family of parallelograms.
Being in the same family does not make one group part of the other, and a rectangle twice as long as it is wide shows it.

### L2 human

The fallacy often appears in a proof about numbers.

1. A student claims that every number divisible by $6$ is divisible by $4$.
2. The "argument" is: every number divisible by $4$ is even, and every number divisible by $6$ is even.
3. The middle term "even numbers" is the predicate of both premises, so the form is AAA-2 and the middle term is undistributed.
4. The number $6$ is divisible by $6$ and even, but not divisible by $4$, so the claim is false.

If the middle term is never distributed, the form is invalid, and this check takes seconds.
The trap is that an invalid form can still have a true conclusion in one instance: "every multiple of $12$ is a multiple of $4$" follows the same pattern and is true.
