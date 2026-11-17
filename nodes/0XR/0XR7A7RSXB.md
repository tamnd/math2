---
tag: 0XR7A7RSXB
kind: definition
name: Negation
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 029JBBF693
uses: [0ZGC7ZESYN, 5DYNDW9526]
sources:
  - url: https://en.wikipedia.org/wiki/Negation
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
---

## Definition

Let $p$ be a [[proposition|0ZGC7ZESYN]].
The negation of $p$ is the proposition $\neg p$, read "not $p$" or "it is not the case that $p$".
The proposition $\neg p$ is true when $p$ is false, and $\neg p$ is false when $p$ is true.
Its truth table is the following.

| $p$ | $\neg p$ |
|---|---|
| T | F |
| F | T |

For formulas, a valuation $v$ gives $v(\neg\varphi) = $ T exactly when $v(\varphi) = $ F.

## Notation

This sub-area writes $\neg p$.
Other notations are $\sim p$, $p'$ and $\overline{p}$; with truth values $1$ and $0$, the negation is $1 - p$.
For relations, a slash marks the negation, as in $a \neq b$, $x \notin A$ and $a \nmid b$.
In Lean's Mathlib, `Not a` (written `¬a`) is defined as `a → False`.

## Remarks

Negation is the only connective with one input among the usual connectives; $\land$, $\lor$, $\to$, $\leftrightarrow$ and $\oplus$ have two inputs.
The definition uses the [[principle of bivalence|5DYNDW9526]]: the two rows of the table cover all cases.
The proof rules that match the definition are negation introduction (from "$p$ leads to a contradiction" conclude $\neg p$) and negation elimination (from $p$ and $\neg p$ conclude a contradiction).
In Mathlib these rules are the rules of implication applied to `a → False`.
The concept page [[negation|029JBBF693]] gives the laws for negating compound propositions, double negation, the examples and the non-examples.

## Explanations

### L1 human

To negate a sentence, we say that it is not the case.
The negation of "$5$ is prime" is "$5$ is not prime".
The first sentence is true, so its negation is false.
The negation of "$6$ is prime" is "$6$ is not prime", and it is true, because $6 = 2 \times 3$.

### L2 human

We find the truth value of $\neg(\neg p)$ for each value of $p$ with the definition.

1. If $p$ is T, then $\neg p$ is F by the first row, and $\neg(\neg p)$ is T by the second row.
2. If $p$ is F, then $\neg p$ is T by the second row, and $\neg(\neg p)$ is F by the first row.
3. So $\neg\neg p$ has the same truth value as $p$ in both rows.

This computation is the truth-table proof of the [[double negation law|0NFAGWH84K]].

A trap: the computation uses bivalence, since it checks only two rows.
In intuitionistic logic the same definition of $\neg$ as "$p$ leads to a contradiction" does not give $\neg\neg p \to p$.
