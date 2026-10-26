---
tag: 0J6AKYZQT8
kind: statement
role: proposition
name: Associativity of composition
aliases: [composition-is-associative]
msc: ["03E20"]
uses: [07HF9YCWPP]
sources:
  - url: https://en.wikipedia.org/wiki/Function_composition
    locator: Properties
---

## Statement

Let $f \colon A \to B$, $g \colon B \to C$ and $h \colon C \to D$ be [[functions|0XHDTE5YMZ]].
Then
$$h \circ (g \circ f) = (h \circ g) \circ f.$$

## Remarks

Both sides send each $a \in A$ to $h(g(f(a)))$, so they are equal.
Because of this law, one can write $h \circ g \circ f$ without brackets.
With the [[identity functions|0FSNQ0GNCC]], the functions from a set to itself form a monoid under composition.

## Explanations

### L1 human

When three machines are chained, it does not matter which two you connect first.
The input passes through $f$, then $g$, then $h$ in both cases.
