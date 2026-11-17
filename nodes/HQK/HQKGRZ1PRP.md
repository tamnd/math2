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

A unary [[logical connective|QS0XVAN9BG]] has a truth function $f \colon \set{\mathsf{T}, \mathsf{F}} \to \set{\mathsf{T}, \mathsf{F}}$, by the [[definition|CA49F5KQGB]].
We list all such functions and check that there are exactly four.

1. The domain $\set{\mathsf{T}, \mathsf{F}}$ has $2$ elements, and $f$ chooses one of $2$ values at each. So there are $2 \cdot 2 = 4$ functions.
2. The four functions, with their values at $\mathsf{T}$ and at $\mathsf{F}$, are listed in the table.

| Name | $f(\mathsf{T})$ | $f(\mathsf{F})$ | Formula |
|---|---|---|---|
| constant true | T | T | $p \lor \neg p$ |
| identity | T | F | $p$ |
| negation | F | T | $\neg p$ |
| constant false | F | F | $p \land \neg p$ |

3. The formula $p \lor \neg p$ is true at $p = \mathsf{T}$ (first disjunct) and at $p = \mathsf{F}$ (second disjunct), so it gives the first function.
4. The formula $p \land \neg p$ is false at $p = \mathsf{T}$ (second conjunct) and at $p = \mathsf{F}$ (first conjunct), so it gives the last function.

So each unary truth function is expressed by $p$, $\neg p$ and the connectives $\land$ and $\lor$.

## Remarks

The example shows that [[negation|029JBBF693]] is the only unary connective that is of real interest.
The two constant functions ignore their input, and the identity returns its input.
Among the four, negation is the only one that is not constant and changes the value.

The same count for two inputs gives $2^4 = 16$ binary connectives, listed on the page [[logical connective|QS0XVAN9BG]].
For $n$ inputs the count is $2^{2^n}$.
In a logic with three truth values there are $3^3 = 27$ unary truth functions instead of $4$.

## Explanations

### L1 human

A switch that acts on one light can do four things.
It can always turn the light on, always turn it off, leave it as it is, or flip it.
A unary connective does the same with one truth value.
"Not" is the flip: it turns true into false and false into true.

### L2 human

We count the symmetric ternary connectives: those whose value does not change under any swap of two inputs.

1. A symmetric truth function of three inputs depends only on the number $k$ of true inputs.
2. The number $k$ is one of $0, 1, 2, 3$, so there are $4$ classes of inputs.
3. A symmetric function chooses $\mathsf{T}$ or $\mathsf{F}$ for each class, so there are $2^4 = 16$ of them.
4. The majority function, which is $\mathsf{T}$ for $k = 2, 3$, is one of these.

The typical use of such counts is to see how many connectives a language could have, before choosing a small set of them.
A trap: the count $2^{2^n}$ grows very fast, $256$ for $n = 3$, so a list of connectives by name stops at $n = 2$.
