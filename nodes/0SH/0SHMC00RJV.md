---
tag: 0SHMC00RJV
kind: definition
name: Split polynomial
msc: [12F05]
defines: 0JVSNJCN68
uses: [0Q9EZS90GY, 00EHX6FWC0]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_field
    locator: Definition
---

## Definition

Let $L$ be a [[field|0QA8CHH8MG]] and let $f \in L[x]$ be nonzero.
The polynomial $f$ splits over $L$ if there are $c, a_1, \dots, a_n \in L$ with
$$f = c \, (x - a_1)(x - a_2) \cdots (x - a_n).$$

## Remarks

Then $c$ is the leading coefficient of $f$, $n = \deg f$, and $a_1, \dots, a_n$ are the [[roots|00EHX6FWC0]] of $f$, not necessarily distinct.
The polynomial $x^2 - 2$ splits over $\mathbb{R}$, but not over $\mathbb{Q}$.
The polynomial $x^2 + 1$ splits over $\mathbb{C}$, but not over $\mathbb{R}$.
Over an [[algebraically closed field|02SJG1HC32]], every nonzero polynomial splits.

## Explanations

### L1 human

A polynomial splits when you can factor it completely into linear factors.
Then you can read all its roots from the factors.
