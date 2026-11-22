---
tag: FYC7X2HYBH
kind: example
name: Euclid's description of a point
msc: ["00A35", "01A20"]
topics: [BP0WAF23HB]
audience: school
not_instance_of:
  - target: 8ZCZ3HW91Z
    note: the sentence uses the undefined word part, and no proof of the Elements uses it
uses: [8ZCZ3HW91Z, 83WHDAV68J, QMQEJKFEYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Point_(geometry)
    locator: Points in Euclidean geometry
  - url: https://en.wikipedia.org/wiki/Euclid%27s_Elements
    locator: lead section
---

## Example

Book I of [[Euclid's Elements|83WHDAV68J]] opens with a list of definitions.
The first one says, in the usual English rendering, that a point is that which has no part.
We test this sentence against the conditions of a [[mathematical definition|8ZCZ3HW91Z]], and it fails all three.

1. A definition states its definiens in known terms.
   The definiens here uses the word "part", and the *Elements* never says what a part of a geometric figure is.
2. A definition lets us decide, for a given object, whether it has the defined property.
   The sentence gives no test that tells us whether a given object is a point.
3. A definition can be used in proofs, because the term and the definiens can replace each other.
   No proof in the *Elements* uses the sentence; the proofs use the postulates, the common notions and earlier propositions.

So the sentence is a description that guides the reader's picture, not a mathematical definition.

## Remarks

Compare Euclid's definition of a circle: a plane figure bounded by one line, such that all straight lines from one point inside it to the line are equal.
That one is a working definition, and the very first proposition of Book I uses it to show that the triangle it builds has equal sides.
So the trouble is not with Euclid's definitions in general, only with the ones for the most basic words.
The next ones in Book I, which describe a line as length without breadth, fail in the same way, since "breadth" is not defined either.

In 1899 Hilbert took "point" and "line" as [[primitive notions|QMQEJKFEYZ]].
He gave them no definition at all, and his axioms fix how proofs may use them.
Euclid's descriptions still have a job: they tell the reader what to imagine.
A picture and a definition do different work, and only the definition may appear in a proof.

## Explanations

### L1 human

Euclid wrote that a point is something with no parts.
The sentence helps us imagine a point as a tiny dot.
But it gives no way to check anything, because Euclid never says what a "part" is.
His proofs never use the sentence.
So mathematicians today call it a description, and they treat "point" as a word with no definition at all.

### L2 human

Compare "a point has no part" with "a circle is the set of points at a fixed distance $r > 0$ from a fixed point $O$".
The second sentence uses only known terms: point, distance and a number $r$.
It gives a test, since a point $P$ is on the circle exactly when the distance from $O$ to $P$ is $r$.
Proofs use the test.
If $A$ and $B$ are on the circle, then $OA = OB = r$, so the triangle $OAB$ is isosceles.
The first sentence gives no test and no equation, so no proof step can use it.
Watch out: a term without a definition is not a gap in the theory.
Every theory starts from some undefined terms, and its axioms then do the work that a definition would do.
