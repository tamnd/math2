---
tag: 1FNHGRQ3YB
kind: concept
name: SKI combinator calculus
msc: [03B40, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/SKI_combinator_calculus
same_as:
  wikidata: Q857813
  wikipedia: SKI combinator calculus
---

## Summary

The SKI combinator calculus is a model of computation built from three constants $\mathbf{S}$, $\mathbf{K}$ and $\mathbf{I}$ and application, without bound variables.
Its rules are $\mathbf{I}\, x \to x$, $\mathbf{K}\, x\, y \to x$ and $\mathbf{S}\, x\, y\, z \to x\, z\, (y\, z)$.
Every term of the [[lambda calculus|BD756KR8FM]] can be translated into it, so it is Turing complete.
It goes back to Moses Schönfinkel and Haskell Curry, and it is the basis of combinatory logic.

## Explanations

### L1 human

The lambda calculus builds functions with variables, as in $\lambda x.\, x$.
Variables cause bookkeeping trouble, such as renaming to avoid clashes.
Combinatory logic removes variables completely and keeps three basic operations.
$\mathbf{I}$ returns its input, $\mathbf{K}$ makes constant functions, and $\mathbf{S}$ passes an argument to two functions and applies one result to the other.
Surprisingly, every program can be written with these three letters alone, and even $\mathbf{I}$ can be built as $\mathbf{S}\, \mathbf{K}\, \mathbf{K}$.
