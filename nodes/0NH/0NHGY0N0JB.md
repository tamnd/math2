---
tag: 0NHGY0N0JB
kind: statement
role: theorem
name: Fundamental theorem of calculus
msc: [26A42]
uses: [063H5KJC69, 0XYAFCN0PT, 0BW9N5CDSB]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
    locator: Formal statements
same_as:
  wikidata: Q1217677
  wikipedia: Fundamental theorem of calculus
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be continuous.
Then the function $F(x) = \int_a^x f(t) \, dt$ is differentiable on $(a, b)$, with $F'(x) = f(x)$.
If $G$ is continuous on $[a, b]$ and $G' = f$ on $(a, b)$, then
$$\int_a^b f(x) \, dx = G(b) - G(a).$$

## Remarks

The first part is the [[first fundamental theorem|063H5KJC69]]. The second part is the [[second fundamental theorem|0XYAFCN0PT]].
Together they say that differentiation and integration are inverse operations.
The theorem reduces the computation of integrals to the search for [[antiderivatives|0BW9N5CDSB]].

## History

James Gregory published the first statement and proof of a geometric form of the theorem.
Isaac Barrow proved a more general version. Isaac Newton and Gottfried Leibniz then built the calculus around it.

## Explanations

### L1 human

The fundamental theorem connects the two main ideas of calculus.
The derivative of an area function is the height of the graph, and an integral is a change in an antiderivative.
