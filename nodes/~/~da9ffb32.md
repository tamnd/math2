---
tag: ~da9ffb32
kind: example
name: An Euler diagram is not an existential graph
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: ug1
not_instance_of:
  - target: ~1a686a01
    note: an Euler diagram shows classes as regions and inclusion as nesting; it has no sheet of assertion, no cut for negation, no line of identity for individuals and no rules of transformation
uses: [~1a686a01, ~566128b7, 0KCT6DPXJK]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_diagram
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Existential_graph
    locator: lead section
---

## Example

Draw three circles: a circle "squares" inside a circle "rectangles", and the circle "rectangles" inside a circle "parallelograms".
This Euler diagram shows the premises of [[Barbara|AC6XQ4KRNT]], "all rectangles are parallelograms" and "all squares are rectangles".
It also shows the conclusion: the circle "squares" lies inside the circle "parallelograms".
We check that this diagram is not an [[existential graph|~1a686a01]].

1. In an existential graph, a closed curve is a cut, and it denies what it contains. In the Euler diagram, a closed curve is a class, and it denies nothing.
2. In an existential graph, the letters on the sheet are asserted propositions or predicates attached to lines. In the Euler diagram, the labels name classes, and the diagram asserts relations between the classes by the position of the curves.
3. An existential graph of the beta system shows individuals by lines of identity. The Euler diagram has no lines and shows no individual.
4. The existential graphs have rules of inference: erasure, insertion, iteration, deiteration and the double cut. The Euler diagram has no rules; the conclusion is read off the picture.
5. So the Euler diagram fails each defining feature of an existential graph.

The two notations also differ in what they can say.

6. The beta graph of "all rectangles are parallelograms" is a cut containing the spot "rectangle" and a second cut with the spot "parallelogram", joined by one line. With $R$ for rectangles and $G$ for parallelograms, it reads $\neg \exists x\,(R(x) \land \neg G(x))$.
7. The Euler diagram cannot show "some rectangle is a rhombus" alone. Two overlapping curves also suggest that some rectangles are not rhombuses and some rhombuses are not rectangles, unless a convention says that a region can be empty.

## Remarks

The example shows the difference between a diagram of classes and a diagram of statements.
Euler diagrams and the [[Venn diagrams|0KCT6DPXJK]] that improved them are tools for [[syllogistic|~566128b7]], where every statement is a relation between classes.
Venn diagrams draw all regions and mark the empty ones by shading, which fixes the problem of step 7; they still have no negation of a whole statement and no relations between individuals.
Existential graphs treat negation, conjunction and quantification as operations on statements, and so they reach full first-order logic.
The two kinds of diagram agree on monadic statements: each Venn diagram of three classes can be translated into a beta graph, with one cut for each shaded region and one line on the sheet for each cross.

## Explanations

### L1 human

An Euler diagram is a picture of groups: one circle for each group, and one circle inside another when every member of the first group is in the second.
An existential graph is a picture of sentences: a loop around a sentence means "not".
In the Euler diagram, the circle of squares inside the circle of rectangles says "all squares are rectangles".
In an existential graph, a loop around "square" would say "there is no square", which is a very different claim.
So the same drawing, a curve inside a curve, means different things in the two notations.

### L2 human

We translate the Euler diagram of the example into a beta graph.

1. "Squares inside rectangles" means $\forall x\,(Q(x) \to R(x))$ with $Q$ for squares and $R$ for rectangles.
2. Rewrite as $\neg \exists x\,(Q(x) \land \neg R(x))$.
3. Draw a cut, put the spot $Q$ in it, put a second cut inside the first with the spot $R$, and join $Q$ and $R$ by a line.
4. Do the same for "rectangles inside parallelograms", with a new pair of cuts.

The typical use of the translation is to move from a picture of classes to a picture that the rules of inference can act on.
The trap is to read a curve of an Euler diagram as a cut: a curve around a label in an Euler diagram does not deny anything.
