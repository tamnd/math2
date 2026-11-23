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

Compute $e^{\pi\sqrt{163}}$ with $29$ significant digits, and the result prints as
$$262537412640768744.00000000000.$$
It looks like an integer.
The number is called Ramanujan's constant, and it is not an integer.
We compare a careless claim about it with the method of [[experimental mathematics|BPEPTN0TT9]].

1. The claim.
   A careless reader of the $29$-digit value concludes that $e^{\pi\sqrt{163}}$ is the integer $262537412640768744$.
2. The missing test.
   The method requires a test at higher precision.
   With $30$ significant digits the value is $262537412640768743.999999999999$, and the last digit already differs from the integer.
3. The full value.
   With more digits,
   $$e^{\pi\sqrt{163}} = 262537412640768743.99999999999925007\ldots,$$
   and the distance to the integer is about $7.5 \cdot 10^{-13}$.
4. The conclusion.
   The number is not an integer.
   The claim of step 1 came from a single computation at a precision that was too low.

So step 1 is not an experiment in the sense of the method: it detected a relation and skipped the test.
Steps 2 and 3 are the missing test, and they refute the claim.
Agreement to $29$ digits was evidence, and it was not a proof.

## Remarks

### Why the match is so close

The near miss has a reason.
The number $163$ is a [[Heegner number|QA745HVAFV]], and the [[j-invariant|FEC2XH822R]] gives $j\left(\tfrac{1 + \sqrt{-163}}{2}\right) = -640320^3$.
The expansion of $j$ then gives
$$e^{\pi\sqrt{163}} = 640320^3 + 744 - 196884\, e^{-\pi\sqrt{163}} + \cdots,$$
with much smaller further terms.
Here $640320^3 + 744 = 262537412640768744$, and $196884\, e^{-\pi\sqrt{163}} = 7.4992740\ldots \cdot 10^{-13}$, which matches step 3.
So the coincidence is itself a theorem, and the exact statement is an approximation, not an equality.

### The joke and the law

In April 1975 Martin Gardner claimed in his *Scientific American* column, as an April Fools' joke, that the number is an integer.
The example is an instance of Richard Guy's second law of small numbers: two numbers that look equal need not be equal; see [[the strong law of small numbers|8AFXPXCE3N]].
The [[Borwein integrals|A2KSJSQSF6]] are a second instance.

### Watch out

To decide how many digits a test needs, count them.
The integer part has $18$ digits, and the distance to the nearest integer is about $7.5 \cdot 10^{-13}$, so the first twelve decimals are all $9$.
A computation with $18 + 12 = 30$ correct significant digits is the first one that can show the difference.
A safe test uses many more, and it also checks that the computation itself is accurate to that precision.

Ordinary floating point, with about $16$ significant digits, is far too coarse.
It gives $2.6253741264076826 \cdot 10^{17}$, about $500$ away from the integer, because a tiny error in the exponent $\pi\sqrt{163} \approx 40.1$ is multiplied by the size of the result.

### Try it

The number $67$ is also a Heegner number, with $j\left(\tfrac{1 + \sqrt{-67}}{2}\right) = -5280^3$.
Predict the integer near $e^{\pi\sqrt{67}}$.
It is $5280^3 + 744 = 147197952000 + 744 = 147197952744$, and the true value $147197952743.99999866\ldots$ misses it by about $1.3 \cdot 10^{-6}$.

## Explanations

### L1 human

A calculator that shows $29$ digits says that $e^{\pi\sqrt{163}}$ is a whole number.
A calculator with one more digit shows $\ldots 743.999999999999$ instead of $\ldots 744$.
The number is extremely close to a whole number, but it is not one.
The lesson: never trust a match without checking it with more digits.

### L2 human

We check the integer part of the prediction.
First $640320^2 = 410009702400$.
Then $640320^3 = 410009702400 \cdot 640320 = 262537412640768000$.
Adding $744$ gives $262537412640768744$, the integer that the careless reader saw.
The typical use: before calling a number an integer or a rational, compute it with at least twice the digits that suggested the match.
