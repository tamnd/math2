---
tag: 1QWN5CV4CG
kind: example
name: Non-standard model of arithmetic
msc: [03H15, 03C62]
instance_of: [MVCH6N9SNW]
illustrates: [1NR3HAWG9D]
uses: [0QFT7Z76N5, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
same_as:
  wikidata: Q3318130
  wikipedia: Non-standard model of arithmetic
---

## Example

Let $\mathsf{PA}$ be first-order [[Peano arithmetic|0QFT7Z76N5]] in the language with $0$, $S$, $+$, $\cdot$ and $<$.
A *non-standard model of arithmetic* is a [[model|MVCH6N9SNW]] of $\mathsf{PA}$ that is not isomorphic to the standard model $\N$ of the [[natural numbers|0MWKJ44V5A]].

Such a model exists.
Add a new constant symbol $c$, and let $T = \mathsf{PA} \cup \set{c > \underline{n} : n \in \N}$, where $\underline{n}$ is the term $S S \cdots S 0$ with $n$ copies of $S$.
Every finite subset of $T$ mentions only finitely many $n$, so it has a model: $\N$ with $c$ read as a large enough number.
By the [[compactness theorem|1NR3HAWG9D]], $T$ has a model $M$.
In $M$ the element $c^M$ is greater than the value of every numeral, so it is not of the form $\underline{n}^M$.
In a model isomorphic to $\N$ every element is the value of a numeral, so $M$ is a non-standard model of $\mathsf{PA}$.
By the downward Löwenheim–Skolem theorem, $M$ can be taken countable.

## Remarks

Every non-standard model $M$ starts with a copy of $\N$, the values of the numerals, followed by the non-standard elements.
The order type of every countable non-standard model of $\mathsf{PA}$ is $\omega + (\omega^* + \omega) \cdot \eta$, where $\omega^*$ is the reversed order of $\N$ and $\eta$ is the order type of $\Q$.
By [[Tennenbaum's theorem|W6D5ZJAY9D]], no countable non-standard model of $\mathsf{PA}$ has computable addition or multiplication.

## Explanations

### L1 human

The axioms of arithmetic, written in first-order logic, do not pin down the natural numbers.
There are other structures that satisfy every one of the axioms but contain "infinite" numbers larger than $0, 1, 2, \ldots$.
The compactness theorem builds one by asking for a number bigger than each ordinary number, one at a time.
Inside such a model, the infinite numbers look like ordinary numbers: each has a successor, a predecessor, and so on.
