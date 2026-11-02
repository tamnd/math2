---
tag: BJQTEPEZ9G
kind: concept
name: Asymptotic expansion
msc: [41A60, "30E15", "34E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_expansion
same_as:
  wikidata: Q752726
  wikipedia: Asymptotic expansion
---

## Summary

An asymptotic expansion of a function $f$ near a point is a formal series $\sum a_n \varphi_n$ in a scale of functions that shrink one after another.
Every partial sum must approximate $f$ with an error smaller than its last term.
The series need not converge.
Asymptotic expansions describe special functions, integrals and solutions of differential equations for large or small parameters.
They are closely tied to the theory of [[divergent series|0NBRP6093V]] and to [[Borel summation|8DJPSYSHGJ]].

## Explanations

### L1 human

Think of an approximation that gets better in stages: first a rough main term, then a correction, then a smaller correction.
An asymptotic expansion lists all these stages at once.
Each stage is guaranteed to help when the variable is close enough to the limit point, even if adding infinitely many stages does not converge.
For example, as $x \to \infty$, the function $\frac{1}{x - 1}$ has the expansion $\frac{1}{x} + \frac{1}{x^2} + \frac{1}{x^3} + \cdots$.
The [[Stirling series|K29QYWB6A5]] for $\ln \Gamma(z)$ is an expansion of this kind that diverges for every $z$ and is still very accurate.
