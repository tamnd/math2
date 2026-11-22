---
tag: RF12XC7AY0
kind: example
name: A three-point model of incidence geometry
aliases: [point-line-and-incidence-as-primitive-notions]
msc: ["00A35", "51A05"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [QMQEJKFEYZ]
uses: [QMQEJKFEYZ, CSXT0BG2CM, 0SJ3RX9TXA]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_geometry
    locator: Incidence structures
  - url: https://en.wikipedia.org/wiki/Primitive_notion
    locator: Examples
---

## Example

In [[incidence geometry|CSXT0BG2CM]], "point", "line" and "lies on" are [[primitive notions|QMQEJKFEYZ]].
We take three axioms about them.

1. (I1) For two distinct points, exactly one line contains both.
2. (I2) Every line contains at least two points.
3. (I3) There are three points that do not all lie on one line.

A *model* is an interpretation of the primitive notions in which all three axioms are true.
We build one with three points and check each axiom.

1. Let the points be the letters $A$, $B$ and $C$.
2. Let the lines be the three [[sets|0SJ3RX9TXA]]
   $$\{A, B\}, \qquad \{A, C\}, \qquad \{B, C\}.$$
3. Let "the point $P$ lies on the line $\ell$" mean $P \in \ell$.
4. Check I1.
   For distinct points $X$ and $Y$, the line $\{X, Y\}$ contains both.
   Every line has exactly two elements, so any other line that contained $X$ and $Y$ would equal $\{X, Y\}$.
5. Check I2: every line has exactly two elements.
6. Check I3: no line contains all three of $A$, $B$ and $C$, since no line has three elements.

So the three letters and three pairs form a model, and every theorem proved from I1, I2 and I3 holds in it.

## Remarks

The model shows what the axioms do not say.
Its lines have two points each, so I1, I2 and I3 do not prove "every line contains at least three points".
Any two of its lines meet in exactly one point, for example $\{A, B\} \cap \{A, C\} = \{A\}$, so the axioms do not prove that parallel lines exist.

The Euclidean plane is another model of I1, I2 and I3, with infinitely many points on each line.
A theorem from the three axioms holds in both models, because its proof uses only the axioms.
In the three-point model the words "point" and "line" mean nothing beyond the interpretation, and any three objects would serve in place of the letters.

## Explanations

### L1 human

Imagine a game with three tokens, called $A$, $B$ and $C$.
We call each token a "point", and each pair of tokens a "line".
The rules say that two points always share exactly one line, that each line has at least two points, and that not all points share one line.
All three rules hold in this tiny game.
So the rules of geometry can describe things that look nothing like drawings.

### L2 human

We use the model to show that I1, I2 and I3 do not prove the statement "every line has at least three points".
Suppose that such a proof existed.
Each step of it would use only the axioms, so the statement would hold in every model of the axioms.
But in the three-point model the line $\{A, B\}$ has only two points.
So the statement fails in a model, and no proof of it exists.
The typical use of a small model is exactly this: it shows that an axiom system does not prove a statement.
Watch out: it does not show that the negation is provable either, because in the Euclidean plane every line has infinitely many points.
