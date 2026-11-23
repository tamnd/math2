---
tag: CA49F5KQGB
kind: definition
name: Logical connective
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
defines: QS0XVAN9BG
uses: [0ZGC7ZESYN, 0X05GS525E]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_connective
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Truth_function
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 1.1
---

## Definition

A logical connective is a way to build a formula from formulas, together with a rule that gives the truth value of the result from the truth values of the parts.
Let $n \ge 0$ be an integer, and write T and F for the two truth values.
A truth function of arity $n$ is a [[Boolean function|0X05GS525E]] $f \colon \{\mathrm{T}, \mathrm{F}\}^n \to \{\mathrm{T}, \mathrm{F}\}$.
An $n$-ary logical connective of classical propositional logic is a symbol $c$ together with a truth function $f_c$ of arity $n$.
For formulas $\varphi_1, \dots, \varphi_n$, the expression $c(\varphi_1, \dots, \varphi_n)$ is again a formula.
Under an assignment of truth values to the propositional variables, called a valuation, the value of $c(\varphi_1, \dots, \varphi_n)$ is $f_c(a_1, \dots, a_n)$, where $a_i$ is the value of $\varphi_i$.

## Notation

Connectives of arity $0$, $1$, $2$ and $3$ are called nullary, unary, binary and ternary.
A unary connective is written before its argument, as in $\neg \varphi$.
A binary connective is written between its arguments, as in $\varphi \land \psi$, with brackets around compound arguments.
The usual symbols are $\neg$, $\land$, $\lor$, $\to$, $\leftrightarrow$, $\oplus$, $\uparrow$ and $\downarrow$.
The concept page [[logical connective|QS0XVAN9BG]] lists their variants and the conventions of precedence.

## Remarks

Conjunction is the binary connective $\land$ with $f_\land(a, b) = \mathrm{T}$ exactly when $a = b = \mathrm{T}$.
So $p \land q$ is true only when the [[propositions|0ZGC7ZESYN]] $p$ and $q$ are both true.
Negation is the unary connective $\neg$ with $f_\neg(\mathrm{T}) = \mathrm{F}$ and $f_\neg(\mathrm{F}) = \mathrm{T}$.
The constants $\top$ and $\bot$ are the nullary connectives with values T and F.

The set $\{\mathrm{T}, \mathrm{F}\}^n$ has $2^n$ elements, so there are $2^{2^n}$ truth functions of arity $n$.
Different formulas can have the same truth function.
For example, $p \leftrightarrow q$ and $(p \to q) \land (q \to p)$ are both true exactly when $p$ and $q$ have the same value.

The modal operator "it is necessary that" is not a connective in the sense of the definition.
It has no truth function, because the truth of $p$ does not decide whether $p$ is necessary.

## Explanations

### L1 human

A connective is a way to join statements, such as "and" or "or", together with a rule for the truth of the result.
The rule looks only at whether each part is true or false.
For "or", the rule says: the result is false only when both parts are false.
So "$2 > 3$ or $2$ is even" is true, because the second part is true.

### L2 human

Check that "exactly one of $p$, $q$, $r$ is true" defines a ternary connective.

1. The phrase takes three statements as inputs, so its arity is $3$.
2. Whether exactly one input is true depends only on the three truth values, so the result is a function of them.
3. The function is T on the inputs TFF, FTF and FFT, and F on the other five inputs.
4. So the phrase is a ternary connective with this truth function.

A phrase is a connective exactly when its result depends only on the truth values of its inputs.
Watch out: with two inputs, "exactly one of $p$, $q$ is true" is the exclusive or.
With three inputs it differs from $p \oplus q \oplus r$, which is also true when all three inputs are true.
