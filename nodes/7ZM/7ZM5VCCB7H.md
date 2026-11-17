---
tag: 7ZM5VCCB7H
kind: example
name: Ramanujan's constant is not an integer
msc: ["11Y60", "11F03"]
topics: [DME0TPC348]
audience: ug2
not_instance_of:
  - target: BPEPTN0TT9
    note: a match accepted at one precision without a test at higher precision is a numerical coincidence, not an experimental result
uses: [BPEPTN0TT9, QA745HVAFV, FEC2XH822R]
sources:
  - url: https://en.wikipedia.org/wiki/Heegner_number
    locator: Almost integers and Ramanujan's constant
  - url: https://en.wikipedia.org/wiki/Experimental_mathematics
    locator: Tools and techniques
---

## Example

The number $e^{\pi\sqrt{163}}$ is called Ramanujan's constant.
We compare a careless claim about it with the method of [[experimental mathematics|BPEPTN0TT9]].

1. The claim. A computation with $29$ significant digits prints $262537412640768744.00000000000$. A careless reader concludes that $e^{\pi\sqrt{163}}$ is the integer $262537412640768744$.
2. The missing test. The method requires a test at higher precision. With $30$ significant digits the value is $262537412640768743.999999999999$, and the last digit already differs from the integer.
3. The full value. With $60$ digits, $e^{\pi\sqrt{163}} = 262537412640768743.99999999999925007\ldots$. The distance to the integer is about $7.5 \cdot 10^{-13}$.
4. The conclusion. The number is not an integer. The claim of step 1 came from a single computation at a precision that was too low.

So step 1 is not an experiment in the sense of the method: it detected a relation and skipped the test.
Steps 2 and 3 are the missing test, and they refute the claim.

## Remarks

The near miss has a reason.
The number $163$ is a [[Heegner number|QA745HVAFV]], and the [[j-invariant|FEC2XH822R]] gives $j\left(\tfrac{1 + \sqrt{-163}}{2}\right) = -640320^3$.
The expansion of $j$ then gives $e^{\pi\sqrt{163}} = 640320^3 + 744 - 196884\, e^{-\pi\sqrt{163}} + \cdots$, with much smaller further terms.
Here $640320^3 + 744 = 262537412640768744$, and $196884\, e^{-\pi\sqrt{163}} = 7.4992740\ldots \cdot 10^{-13}$, which matches step 3.
So the coincidence is itself a theorem, and the exact statement is an approximation, not an equality.

In April 1975 Martin Gardner claimed in his column, as an April Fools' joke, that the number is an integer.
The example is an instance of Richard Guy's second law of small numbers: two numbers that look equal need not be equal.
The [[Borwein integrals|A2KSJSQSF6]] are a second instance.

## Explanations

### L1 human

A calculator that shows $29$ digits says that $e^{\pi\sqrt{163}}$ is a whole number.
A calculator with one more digit shows $\ldots 743.999999999999$ instead of $\ldots 744$.
The number is extremely close to a whole number, but it is not one.
The lesson: never trust a match without checking it with more digits.

### L2 human

We decide how many digits a test needs.

1. The integer part has $18$ digits.
2. The distance to the nearest integer is about $7.5 \cdot 10^{-13}$, so the twelve decimals after the point are all $9$.
3. A computation with $18 + 12 = 30$ correct significant digits is the first one that can show the difference.
4. A safe test uses many more, for example $40$ digits, and it also checks that the computation itself is accurate to that precision.

The typical use: before calling a number an integer or a rational, compute it with at least twice the digits that suggested the match.
A trap: the floating point numbers of most programs carry about $16$ significant digits, and with them $e^{\pi\sqrt{163}}$ looks like an integer.
