---
tag: 0JYF6PTKEW
kind: statement
role: lemma
name: Lifting-the-exponent lemma
aliases: [lte-lemma]
msc: [11A51]
uses: [04VCPS30ZE]
sources:
  - url: https://en.wikipedia.org/wiki/Lifting-the-exponent_lemma
    locator: Statements
same_as:
  wikidata: Q97704248
  wikipedia: Lifting-the-exponent lemma
---

## Statement

Let $p$ be an odd prime, let $x$ and $y$ be integers with $p \nmid x$, $p \nmid y$ and $p \mid x - y$, and let $n$ be a positive integer.
Then $\nu_p(x^n - y^n) = \nu_p(x - y) + \nu_p(n)$, where $\nu_p$ is the [[p-adic valuation|04VCPS30ZE]].

## Remarks

For $p = 2$ the formula needs a stronger hypothesis. If $x$ and $y$ are odd and $4 \mid x - y$, then $\nu_2(x^n - y^n) = \nu_2(x - y) + \nu_2(n)$.
For $p = 2$, odd $x$ and $y$, and even $n$, the general formula is $\nu_2(x^n - y^n) = \nu_2(x - y) + \nu_2(x + y) + \nu_2(n) - 1$.
For example, $\nu_3(10^9 - 1) = \nu_3(9) + \nu_3(9) = 4$, and indeed $10^9 - 1 = 3^4 \cdot 37 \cdot 333667$.

## History

Édouard Lucas had some of the ideas by 1878. Mihai Manea published the modern form in 2006.

## Explanations

### L1 human

When $p$ divides $x - y$, the lemma tells you exactly how many factors $p$ are in $x^n - y^n$.
You add the factors $p$ of $x - y$ and the factors $p$ of $n$.
Olympiad problems often use the lemma.
