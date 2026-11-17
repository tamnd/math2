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

Let $n \ge 0$ be an integer, and write $\mathsf{T}$ and $\mathsf{F}$ for the two truth values.
A truth function of arity $n$ is a [[Boolean function|0X05GS525E]] $f \colon \set{\mathsf{T}, \mathsf{F}}^n \to \set{\mathsf{T}, \mathsf{F}}$.
An $n$-ary logical connective of classical propositional logic is a symbol $c$ together with a truth function $f_c$ of arity $n$.
For formulas $\varphi_1, \dots, \varphi_n$, the expression $c(\varphi_1, \dots, \varphi_n)$ is again a formula.
Under an assignment of truth values to the propositional variables (a valuation), the value of $c(\varphi_1, \dots, \varphi_n)$ is $f_c(a_1, \dots, a_n)$, where $a_i$ is the value of $\varphi_i$.

## Notation

Connectives of arity $0$, $1$, $2$ and $3$ are called nullary, unary, binary and ternary.
A unary connective is written before its argument, as in $\neg \varphi$.
A binary connective is written between its arguments, as in $\varphi \land \psi$, with brackets around compound arguments.
The usual symbols are $\neg$, $\land$, $\lor$, $\to$, $\leftrightarrow$, $\oplus$, $\uparrow$ and $\downarrow$; the concept page [[logical connective|QS0XVAN9BG]] lists their variants and the conventions of precedence.
In tables, the truth values T and F are also written $1$ and $0$.

## Remarks

Conjunction is the binary connective $\land$ with $f_\land(a, b) = \mathsf{T}$ exactly when $a = b = \mathsf{T}$.
So $p \land q$ is true only when the [[propositions|0ZGC7ZESYN]] $p$ and $q$ are both true.
Negation is the unary connective $\neg$ with $f_\neg(\mathsf{T}) = \mathsf{F}$ and $f_\neg(\mathsf{F}) = \mathsf{T}$.
The constants $\top$ and $\bot$ are the nullary connectives with values $\mathsf{T}$ and $\mathsf{F}$.

The set $\set{\mathsf{T}, \mathsf{F}}^n$ has $2^n$ elements, so there are $2^{2^n}$ truth functions of arity $n$.
Different formulas can have the same truth function: $p \leftrightarrow q$ and $(p \to q) \land (q \to p)$ are both true exactly when $p$ and $q$ have the same value.

The modal operator "it is necessary that" is not a connective in the sense of this definition.
It has no truth function, because the truth of $p$ does not decide whether $p$ is necessary.

## Explanations

### L1 human

A connective is a way to join statements, such as "and" or "or", together with a rule for the truth of the result.
The rule looks only at whether each part is true or false.
For "or", the rule says: the result is false only when both parts are false.
So "$2 > 3$ or $2$ is even" is true, because the second part is true.

### L2 human

We check that "exactly one of $p$, $q$, $r$ is true" defines a ternary connective.

1. The phrase takes three statements as inputs, so its arity is $3$.
2. Whether exactly one input is true depends only on the three truth values, so the result is a function of them.
3. The function is $\mathsf{T}$ on the inputs $\mathsf{T}\mathsf{F}\mathsf{F}$, $\mathsf{F}\mathsf{T}\mathsf{F}$, $\mathsf{F}\mathsf{F}\mathsf{T}$, and $\mathsf{F}$ on the other five inputs.
4. So the phrase is a ternary connective with this truth function.

The typical use of the definition is this test: a phrase is a connective when its result depends only on the truth values of its inputs.
A trap: with two inputs, "exactly one of $p$, $q$ is true" is the exclusive or.
With three inputs it differs from $p \oplus q \oplus r$, which is also true when all three inputs are true.
