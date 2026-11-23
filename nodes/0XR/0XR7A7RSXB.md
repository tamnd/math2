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

Negation turns a proposition into the proposition that denies it.
Let $p$ be a [[proposition|0ZGC7ZESYN]].
The negation of $p$ is the proposition $\neg p$, read "not $p$" or "it is not the case that $p$".
The proposition $\neg p$ is true when $p$ is false, and false when $p$ is true:

| $p$ | $\neg p$ |
|---|---|
| T | F |
| F | T |

For formulas, a valuation $v$ satisfies $v(\neg\varphi) = \mathrm{T}$ exactly when $v(\varphi) = \mathrm{F}$.

## Notation

We write $\neg p$.
Other books write $\sim p$, $p'$ or $\overline{p}$, and with truth values $1$ and $0$ the negation is $1 - p$.
For relations a slash marks the negation, as in $a \ne b$, $x \notin A$ and $a \nmid b$.
In Lean's Mathlib, `Not a`, written `¬a`, is defined as `a → False`.

## Remarks

The definition has one input and two rows, and the two rows cover all cases only because of the [[principle of bivalence|5DYNDW9526]].
For example, "$6$ is prime" is F, so "$6$ is not prime" is T.
A proposed negation that does not swap the value in every case is not a negation: "$n < 0$" and "$n > 0$" are both F at $n = 0$, so neither negates the other.

The proof rules match the table.
Negation introduction concludes $\neg p$ when the assumption $p$ leads to a contradiction, and negation elimination concludes a contradiction from $p$ and $\neg p$.
In Mathlib both are rules of implication applied to `a → False`, and both are valid in intuitionistic logic.
The concept page [[negation|029JBBF693]] gives the laws for negating compound statements, double negation and the worked examples.

## Explanations

### L1 human

To negate a sentence, say that it is not the case.
The negation of "$5$ is prime" is "$5$ is not prime".
The first sentence is true, so its negation is false.
The negation of "$6$ is prime" is "$6$ is not prime", and it is true, because $6 = 2 \times 3$.

### L2 human

Use the table twice to find $\neg\neg p$.
If $p$ is T, the first row makes $\neg p$ F, and then the second row makes $\neg\neg p$ T.
If $p$ is F, the second row makes $\neg p$ T, and then the first row makes $\neg\neg p$ F.
So $\neg\neg p$ has the same value as $p$ in both rows, which is the truth-table proof of the [[double negation law|0NFAGWH84K]].
Watch out: the computation checks only two rows, so it uses bivalence.
In intuitionistic logic, where $\neg p$ means "$p$ leads to a contradiction", $\neg\neg p \to p$ is not provable.
