---
tag: Y6C40MHZZC
kind: definition
name: Structure
msc: [03C07]
defines: 983GZBQYT4
uses: [WDVVEYD6AT, 0BSJ7RQ9BW, 0EPAT51DXQ, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]]: a set of function symbols, relation symbols and constant symbols.
Each function symbol and each relation symbol has an arity $n \ge 1$.
An $L$-structure $\mathcal{M}$ consists of the following data.

1. A nonempty [[set|0BSJ7RQ9BW]] $M$, the domain or universe of $\mathcal{M}$.
2. For each $n$-ary function symbol $f$ of $L$, a [[function|0EPAT51DXQ]] $f^{\mathcal{M}} \colon M^n \to M$, where $M^n$ is the [[Cartesian product|09CEDJYBKP]] of $n$ copies of $M$.
3. For each $n$-ary relation symbol $R$ of $L$, a subset $R^{\mathcal{M}} \subseteq M^n$.
4. For each constant symbol $c$ of $L$, an element $c^{\mathcal{M}} \in M$.

The objects $f^{\mathcal{M}}$, $R^{\mathcal{M}}$ and $c^{\mathcal{M}}$ are the interpretations of the symbols in $\mathcal{M}$.

## Remarks

Example: let $L = \set{+, -, 0}$ with $+$ binary, $-$ unary and $0$ a constant.
The integers $\Z$ with addition, negation and the number $0$ form an $L$-structure, because each symbol receives a function of the right arity on $\Z$ or an element of $\Z$.

Non-example: for the same signature, the natural numbers $\N$ with $x \mapsto -x$ do not form an $L$-structure, because $x \mapsto -x$ is not a function from $\N$ to $\N$.

A structure is often written as a tuple, such as $(\Z, +, -, 0)$.
Some authors, and the Mathlib library, allow the empty set as domain.

## Explanations

### L1 human

A structure gives a meaning to each symbol of a formal language.
The symbol $<$ alone says nothing; in the structure $(\Q, <)$ it means the usual order of the rational numbers.
Once each symbol has a meaning, each sentence of the language becomes true or false in the structure.
