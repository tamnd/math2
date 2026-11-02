---
tag: WH48X83YPJ
kind: concept
name: Internal language
msc: [03G30, 18B25, 03B38]
sources:
  - url: https://en.wikipedia.org/wiki/Categorical_logic
---

## Summary

The internal language of a category with enough structure is a formal language read inside the category.
Its types are the objects of the category, and its terms are interpreted as morphisms.
For a [[topos|6837RS7N82]] it is the Mitchell–Bénabou language, a higher-order [[intuitionistic logic|Q11N8X99FK]]; for a [[Cartesian closed category|BFBNQ36QS8]] it is the simply typed [[lambda calculus|BD756KR8FM]].
It lets one reason about objects of the category as if they were sets, with elements, functions and subsets.
The reasoning then stays valid in the category.
It is one of the main tools of [[categorical logic|NES4B9CWW4]].

## Explanations

### L1 human

Working with diagrams of arrows can be heavy.
The internal language lets one write ordinary-looking statements such as "for every $x$ in $A$ there is $y$ in $B$ with $f(y) = x$" and read them inside a category.
Each such statement is translated into a statement about arrows, such as "$f$ is an epimorphism".
For example, in the topos of sheaves on a space, a statement holds when it holds locally, and the law of excluded middle may fail.
