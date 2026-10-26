---
tag: 03MTBVG3VE
kind: statement
role: theorem
name: de Moivre's formula
msc: [33B10]
uses: [04R3CY41VJ, 0WM7DJCM6G]
sources:
  - url: https://en.wikipedia.org/wiki/De_Moivre%27s_formula
    locator: lead section
same_as:
  wikidata: Q190556
  wikipedia: De Moivre's formula
---

## Statement

For every real number $x$ and every integer $n$,
$$(\cos x + i \sin x)^n = \cos(n x) + i \sin(n x).$$

## Remarks

Proof: by [[Euler's formula|04R3CY41VJ]], the left side is $(e^{i x})^n = e^{i n x}$, which is the right side.
For $n = 2$, comparing real and imaginary parts gives $\cos 2x = \cos^2 x - \sin^2 x$ and $\sin 2x = 2 \sin x \cos x$.
For non-integer exponents $n$, the formula fails in general.

## Explanations

### L1 human

Raising a point of the unit circle to the power $n$ multiplies its angle by $n$.
For example, $\cos(\pi/4) + i \sin(\pi/4)$ points at $45$ degrees, and its fourth power points at $180$ degrees, so it is $-1$.
