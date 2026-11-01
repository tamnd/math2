---
tag: X74VY86TSX
kind: concept
name: Rack and quandle
msc: [57K12, 20N02]
sources:
  - url: https://en.wikipedia.org/wiki/Racks_and_quandles
same_as:
  wikidata: Q7279807
  wikipedia: Racks and quandles
---

## Summary

A rack is a set with a [[binary operation|0M418FE7BB]] that distributes over itself and acts on the set by bijections.
A quandle is a rack in which every element $a$ satisfies $a \triangleleft a = a$.
The model example is conjugation in a group, $a \triangleleft b = a b a^{-1}$, which keeps the properties of conjugation and forgets the group multiplication.
The three quandle axioms match the three Reidemeister moves of knot diagrams, so each knot has a fundamental quandle, which is a strong knot invariant.

## Explanations

### L1 human

In a group, conjugating $b$ by $a$ moves $b$ to $a b a^{-1}$.
A quandle keeps only this operation and its basic rules.
Knot theory uses quandles by giving a label to each arc of a knot diagram.
At each crossing, the label of the arc that passes under changes by the operation with the label of the arc that passes over.
The rules of a quandle are exactly the rules that make this labelling unchanged by the usual moves of knot diagrams.
