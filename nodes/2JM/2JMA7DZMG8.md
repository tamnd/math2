---
tag: 2JMA7DZMG8
kind: concept
name: Associativity equation
msc: [39B52, 20N02]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Associative_property
---

## Summary

The associativity equation is the [[functional equation|SRAN4EKWS0]] $F(F(x, y), z) = F(x, F(y, z))$ for an unknown binary operation $F$ on a set.
Its solutions are exactly the associative [[binary operations|0M418FE7BB]], so it turns the algebraic law of [[associativity|0K8F7PVDMX]] into a problem about unknown functions.
On a real interval, its continuous solutions that are strictly increasing in each variable are the operations $F(x, y) = g^{-1}(g(x) + g(y))$ with $g$ continuous and strictly monotone.
So, up to a change of scale, every such operation on an interval is ordinary addition.

## Explanations

### L1 human

Associativity says that brackets do not matter when one combines three things.
The equation asks which formulas $F(x, y)$ have this property.
Addition $x + y$ is the basic solution, and every regular solution on an interval is addition in disguise, after a change of scale $g$.
For example, $F(x, y) = x + y + xy$ on $(-1, \infty)$ is associative, because $1 + F(x, y) = (1 + x)(1 + y)$.
