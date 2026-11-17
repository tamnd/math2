---
tag: ~cccf2ee4
kind: example
name: A statement and its converse are not opposites
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
not_instance_of:
  - target: ~4442a383
    note: the two A propositions have the subject and the predicate exchanged, so they are not corners of one square, and all four combinations of truth values occur, so no relation of the square holds between them
uses: [~4442a383, ~566128b7]
sources:
  - url: https://en.wikipedia.org/wiki/Square_of_opposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Converse_(logic)
    locator: lead section
---

## Example

Consider the two sentences "all $S$ are $P$" and "all $P$ are $S$".
We show that they stand in none of the four relations of the [[square of opposition|~4442a383]].

1. The corners of one square all have the same subject term and the same predicate term. The first sentence has subject $S$, and the second has subject $P$, so they are not two corners of one square.
2. Each relation of the square excludes some pair of truth values. Contradictories exclude (true, true) and (false, false); contraries exclude (true, true); subcontraries exclude (false, false); subalternation excludes (true, false).
3. Both true: let $S$ and $P$ both be the squares. Then "all squares are squares" is true twice.
4. First true, second false: let $S$ be the squares and $P$ the rectangles. "All squares are rectangles" is true, and "all rectangles are squares" is false, as the rectangle with sides $1$ and $2$ shows.
5. First false, second true: let $S$ be the rectangles and $P$ the squares. This is step 4 with the roles exchanged.
6. Both false: let $S$ be the even numbers and $P$ the multiples of $3$. "All even numbers are multiples of $3$" is false because of $2$, and "all multiples of $3$ are even" is false because of $3$.
7. All four pairs of truth values occur, and every term in steps 3 to 6 is non-empty. So no relation of the square holds, in the traditional or in the modern reading.

## Remarks

The second sentence is the converse of the first.
The example shows that a statement and its converse are logically independent: knowing the truth value of one tells nothing about the other.
This is the syllogistic form of a common error in proofs, the confusion of a theorem with its converse.
The situation changes for E and I: "no $S$ is $P$" and "no $P$ is $S$" are equivalent, and so are "some $S$ is $P$" and "some $P$ is $S$".
For these propositions conversion is valid, and the converse is the same corner of the square in another wording.

## Explanations

### L1 human

"All squares are rectangles" is true, but "all rectangles are squares" is false.
Swapping the two groups can change a true sentence into a false one.
It can also change a false sentence into a true one, or keep both true or both false.
So the two sentences are not opposites of each other in any sense of the square: knowing one tells us nothing about the other.

### L2 human

We show the independence with sets.

1. "All $S$ are $P$" says $S \subseteq P$, and "all $P$ are $S$" says $P \subseteq S$.
2. Both hold exactly when $S = P$.
3. Exactly the first holds when $S$ is a proper subset of $P$.
4. Exactly the second holds when $P$ is a proper subset of $S$.
5. Neither holds when each set has an element outside the other, as for the even numbers and the multiples of $3$.

The typical use of this check is to see that a proof of $S \subseteq P$ says nothing about $P \subseteq S$; set equality needs both.
The trap is to treat "all $P$ are $S$" as the negation of "all $S$ are $P$": the negation is "some $S$ is not $P$".
