---
tag: E874NARWPV
kind: concept
name: Monomial order
msc: [13P10, 06A05]
sources:
  - url: https://en.wikipedia.org/wiki/Monomial_order
same_as:
  wikidata: Q934509
  wikipedia: Monomial order
---

## Summary

A monomial order is a total order on the monomials of a polynomial ring that is compatible with multiplication and has no infinite descending chains.
It singles out a leading term in every nonzero polynomial, which is what makes the [[multivariate division algorithm|T8EN3CAEQF]] and [[Gröbner bases|C83KPT47R0]] work.
Common examples are the lexicographic order, the graded lexicographic order and the graded reverse lexicographic order.

## Explanations

### L1 human

For polynomials in one variable, terms are ordered by degree, and the leading term is the one of highest degree.
With several variables, there is no single natural choice, so one fixes a rule that compares any two monomials, such as $x^2 y$ and $x y^3$.
The rule must respect multiplication: if $u$ comes before $v$, then $wu$ comes before $wv$.
It must also make $1$ the smallest monomial, so that repeatedly cancelling leading terms always stops.
In the lexicographic order with $x > y$, one compares the powers of $x$ first, so $x^2 y > x y^3$.
