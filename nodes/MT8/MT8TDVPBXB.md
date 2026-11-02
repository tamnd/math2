---
tag: MT8TDVPBXB
kind: concept
name: Model theory of algebraically closed fields
msc: [12L12, 03C60, 03C10]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraically_closed_field
---

## Summary

This part of model [[theory|92SWXST1ZM]] studies the first-order theory $\mathrm{ACF}$ of [[algebraically closed fields|0PF6TM8TWT]] in the language of rings.
It also studies the completions $\mathrm{ACF}_p$, one for each characteristic $p$.
The theory $\mathrm{ACF}$ admits [[quantifier elimination|7FDDXV3JK7]].
Each $\mathrm{ACF}_p$ is [[complete|655K8Y7VS8]] and decidable, and categorical in every uncountable cardinality.
These facts give the [[Lefschetz principle|SKTMN14X5P]] and short proofs of results in algebra, such as the [[Ax–Grothendieck theorem|M2XAN2HGZH]].
It is also the basic example of a [[strongly minimal theory|PNGY60EBDJ]].

## Explanations

### L1 human

Model theory asks which statements about a mathematical structure can be written with "for all", "there exists", and the symbols $+$, $\cdot$, $0$, $1$, $=$.
For algebraically closed fields, every such statement is equivalent to a statement without "for all" and "there exists", that is, to a combination of polynomial equations and inequations.
For example, "there is $x$ with $a x^2 + b x + c = 0$" is equivalent to "$a \ne 0$, or $b \ne 0$, or $c = 0$".
As a consequence, a statement of this kind that holds in the complex numbers holds in every algebraically closed field of characteristic $0$.
This lets one move results from $\C$ to other fields and back.
