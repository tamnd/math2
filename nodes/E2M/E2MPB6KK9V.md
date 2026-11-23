---
tag: E2MPB6KK9V
kind: example
name: The concept image of a function as a formula
msc: ["97C30", "97I20"]
topics: [VHGA6J4NZK]
audience: ug1
instance_of: [C5S2X0WDJ8]
uses: [C5S2X0WDJ8, 0EPAT51DXQ]
sources:
  - url: https://doi.org/10.1080/0020739830140305
    locator: pages 293-305
---

## Example

A student has met many functions in school, such as $f(x) = 2x + 1$, $g(x) = x^2$ and $h(x) = \sin x$, and each was given by one formula.
The student forms the [[concept image|C5S2X0WDJ8]] "a function is a formula in $x$".
The concept definition of a [[function|0EPAT51DXQ]] from $\mathbb{R}$ to $\mathbb{R}$ is a rule that assigns to each real number $x$ exactly one real number $f(x)$.
We test the image on three objects.

1. Let $F(x) = x^2$ for $x \neq 0$ and $F(0) = 1$.
   Each $x$ has exactly one value, so $F$ is a function by the definition, but the image hesitates because $F$ is not one formula.
2. Let $G(x) = 5$ for all $x$.
   Each $x$ has exactly one value, so $G$ is a function, but the image hesitates because the formula has no $x$ in it.
3. Let $H(x) = 1$ if $x$ is rational and $H(x) = 0$ if $x$ is irrational.
   Each $x$ has exactly one value, so $H$ is a function, but the image rejects it because no school-style formula gives it.

In each case the definition accepts a function that the image rejects or doubts, so the image conflicts with the definition.

## Remarks

Shlomo Vinner (1983) studied the images of function held by students who had learned the set definition, and found that many judged examples by formulas and graphs.
The object $G$ shows that the issue is not "having a formula": $5$ is a formula, but it does not visibly use $x$.
The image is useful in many calculations, and it fails exactly when the student must decide whether an object is a function at all.
If the student instead pictures a function as a graph that passes the vertical line test, $F$ and $G$ pass, and only $H$, whose graph cannot be drawn, still causes trouble.

## Explanations

### L1 human

Most functions in school are given by a formula, like $x^2$ or $2x + 1$.
So students come to think that a function is the same thing as a formula.
But a function only needs to give one answer for each input.
"Give $1$ for rational numbers and $0$ for irrational numbers" is a function, even with no formula of the usual kind.

### L2 human

To work on this image in class, first state it ("a function is a formula") and the definition ("exactly one output for each input") side by side.
Then give objects that satisfy the definition but not the image: a function by cases, a constant function and a function with no formula.
Ask the student to decide each case by the definition.
Watch out for "it is a function because the teacher says so": the aim is that the student checks the definition and so adds the new cases to the image.
