---
tag: HQKGRZ1PRP
kind: example
name: The four unary connectives
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
instance_of: [QS0XVAN9BG]
uses: [QS0XVAN9BG, CA49F5KQGB, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Truth_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_connective
    locator: lead section
---

## Example

A unary [[logical connective|QS0XVAN9BG]] has a truth function $f \colon \{\mathrm{T}, \mathrm{F}\} \to \{\mathrm{T}, \mathrm{F}\}$, by the [[definition|CA49F5KQGB]].
We list all such functions and check that there are exactly four.

1. The domain $\{\mathrm{T}, \mathrm{F}\}$ has $2$ elements, and $f$ chooses one of $2$ values at each.
   So there are $2 \cdot 2 = 4$ functions.
2. The table lists the four functions with their values at T and at F, and a formula for each.

| Name | $f(\mathrm{T})$ | $f(\mathrm{F})$ | Formula |
|---|---|---|---|
| constant true | T | T | $p \lor \neg p$ |
| identity | T | F | $p$ |
| negation | F | T | $\neg p$ |
| constant false | F | F | $p \land \neg p$ |

3. The formula $p \lor \neg p$ is T at $p$ = T by its first disjunct, and T at $p$ = F by its second disjunct.
   So it gives the first function.
4. The formula $p \land \neg p$ is F at $p$ = T by its second conjunct, and F at $p$ = F by its first conjunct.
   So it gives the last function.

So each unary truth function is expressed with $p$, $\neg$, $\land$ and $\lor$.

## Remarks

### Negation is the only interesting one

The two constant functions ignore their input, and the identity returns its input unchanged.
So [[negation|029JBBF693]] is the only one of the four that is not constant and changes the value.
That is why logic books name only one unary connective.

### The count in general

The same count for two inputs gives $2^4 = 16$ binary connectives, listed in [[logical connective|QS0XVAN9BG]].
For $n$ inputs the count is $2^{2^n}$.
In a logic with three truth values there are $3^3 = 27$ unary truth functions instead of $4$.

## Explanations

### L1 human

A switch that acts on one light can do four things.
It can always turn the light on, always turn it off, leave it as it is, or flip it.
A unary connective does the same with one truth value.
"Not" is the flip: it turns true into false and false into true.

### L2 human

Count the symmetric ternary connectives, those whose value does not change under any swap of two inputs.

1. A symmetric truth function of three inputs depends only on the number $k$ of true inputs.
2. The number $k$ is one of $0, 1, 2, 3$, so there are $4$ classes of inputs.
3. A symmetric function chooses T or F for each class, so there are $2^4 = 16$ of them.
4. The majority function, which is T for $k = 2, 3$, is one of these.

Such counts show how many connectives a language could have, before we choose a small set of them.
Watch out: the count $2^{2^n}$ grows very fast, $256$ for $n = 3$, so lists of connectives by name stop at $n = 2$.
