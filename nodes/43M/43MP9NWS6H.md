---
tag: 43MP9NWS6H
kind: concept
name: Quotient category
msc: [18A32, 18A05]
specializes: [A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_category
same_as:
  wikidata: Q7272896
  wikipedia: Quotient category
---

## Summary

A quotient category is obtained from a [[category|A2DE66937D]] by declaring some parallel morphisms equal.
The identification must be an [[equivalence relation|0G8VEZ3WTK]] on each set of morphisms that is compatible with composition, called a congruence.
Quotient categories are how one builds homotopy categories, where homotopic maps become equal.

## Explanations

### L1 human

Keep all the objects, but glue some arrows together.
For this to make sense, gluing $f$ to $f'$ must also glue $g \circ f$ to $g \circ f'$, so that composition still works on the glued arrows.
The main example is the homotopy category of topological spaces, where two continuous maps become the same arrow when one can be deformed into the other.
For a small example, a monoid is a category with one object, and a quotient of that category is a quotient monoid.
Gluing integers of the same parity turns $\Z$ under addition into $\Z/2\Z$.
