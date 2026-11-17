---
tag: ~34cfd9ea
kind: example
name: Translating "unless" and "only if" into formulas
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [~5a296a2e]
uses: [~5a296a2e, 0F72FK8EKB, 0NMG7W7Q11, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_form
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Example

We translate two sentences about a real quadratic $x^2 + b x + c$ with the method of [[translating statements into logical form|~5a296a2e]].

Sentence 1: "The quadratic has two distinct real roots unless $b^2 - 4c \leq 0$."
Sentence 2: "The quadratic has two distinct real roots only if $b^2 - 4c > 0$."

1. Dictionary. Let $r$ be "the quadratic has two distinct real roots", let $s$ be "$b^2 - 4c \leq 0$", and let $t$ be "$b^2 - 4c > 0$". Then $t$ is $\neg s$.
2. Sentence 1 has the form "$r$ unless $s$". By the translation table, it becomes $r \lor s$, equivalently $\neg s \to r$.
3. Sentence 2 has the form "$r$ only if $t$". By the translation table, it becomes $r \to t$, that is, $r \to \neg s$.
4. Check the reading of "unless" with a [[truth table|05RSK4Q657]]. The columns of $r \lor s$ and $\neg s \to r$ agree in all four rows.

| $r$ | $s$ | $r \lor s$ | $\neg s$ | $\neg s \to r$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | T | T | T |
| F | T | T | F | T |
| F | F | F | T | F |

5. Truth of sentence 1. If $b^2 - 4c > 0$, the quadratic formula gives the two distinct real roots $\frac{-b \pm \sqrt{b^2 - 4c}}{2}$. So $\neg s \to r$ holds for all $b$ and $c$, and sentence 1 is true.
6. Truth of sentence 2. If $b^2 - 4c \leq 0$, the quadratic has at most one real root, because $x^2 + bx + c = (x + \frac{b}{2})^2 - \frac{b^2 - 4c}{4}$ is then $0$ only at $x = -\frac{b}{2}$ or nowhere. So $s \to \neg r$ holds, and its contrapositive $r \to \neg s$ is sentence 2. Sentence 2 is true.

## Remarks

Together, the two sentences give the [[biconditional|0S6GMNJ62Y]] $r \leftrightarrow \neg s$: two distinct real roots exactly when $b^2 - 4c > 0$.
Sentence 1 alone gives only one direction, because the standard reading of "unless" is the inclusive [[disjunction|0F72FK8EKB]].
In everyday speech, "unless" is often heard as the stronger "if and only if not", which is the [[exclusive or|~777e424f]] $r \oplus s$.
In mathematics, the stronger claim needs its own sentence, as sentence 2 shows here.
If we change sentence 2 to "two distinct real roots if $b^2 - 4c > 0$", the translation becomes $t \to r$, which is the same direction as sentence 1.

## Explanations

### L1 human

"The shop is open unless it is Sunday" means: on a day that is not Sunday, the shop is open.
It says nothing about Sundays.
"The shop is open only if it is not Sunday" means: if the shop is open, then it is not Sunday.
So on Sundays the shop is closed.
The two sentences say different things, and together they say "the shop is open exactly on the days that are not Sunday".

### L2 human

To translate "unless" and "only if", replace each by a standard form before writing symbols.

1. "$p$ unless $q$" becomes "if not $q$, then $p$", so $\neg q \to p$, which equals $p \lor q$.
2. "$p$ only if $q$" becomes "if $p$, then $q$", so $p \to q$.
3. "Not $p$ unless $q$" becomes $\neg p \lor q$, which equals $p \to q$. So "not $p$ unless $q$" and "$p$ only if $q$" have the same translation.

A trap is to translate "unless" as "and not".
"$r$ unless $s$" as $r \land \neg s$ claims that $r$ is true, while the sentence makes no claim when $s$ is true.
