---
tag: CA49F5KQGB
kind: definition
name: Logical connective
msc: [03B05]
defines: QS0XVAN9BG
uses: [09K9MWD2QQ, 0ZGC7ZESYN]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_connective
---

## Definition

Let $n \ge 0$ be an integer, and write $\mathsf{T}$ and $\mathsf{F}$ for the two truth values.
An $n$-ary *logical connective* of classical [[propositional logic|09K9MWD2QQ]] is a symbol $c$ with a truth function $f_c \colon \set{\mathsf{T}, \mathsf{F}}^n \to \set{\mathsf{T}, \mathsf{F}}$.
For formulas $\varphi_1, \dots, \varphi_n$, the expression $c(\varphi_1, \dots, \varphi_n)$ is again a formula.
Under a truth assignment, its value is $f_c$ applied to the values of $\varphi_1, \dots, \varphi_n$.

## Remarks

Conjunction $\land$ is a binary connective: $f_\land(a, b) = \mathsf{T}$ exactly when $a = b = \mathsf{T}$.
So $p \land q$ is true only when [[propositions|0ZGC7ZESYN]] $p$ and $q$ are both true.
The modal operator "it is necessary that" is not a connective of classical propositional logic.
It has no truth function: the truth of $p$ does not determine whether $p$ is necessary.
Binary connectives are written in infix form, such as $\varphi \to \psi$.
The set $\set{\neg, \land}$ is functionally complete: every truth function is expressed by a formula built with these two.
The single connective NAND, with $f(a, b) = \mathsf{F}$ exactly when $a = b = \mathsf{T}$, is also functionally complete.
