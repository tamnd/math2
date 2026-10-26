---
tag: ~3adaef07
kind: definition
name: Finite field
msc: ["12E20"]
defines: ~ad558515
uses: [~92ce2090]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Properties
---

## Definition

A finite field is a [[field|~92ce2090]] $F$ whose underlying set is finite.
The order of $F$ is its number of elements $|F|$.

## Remarks

For each prime number $p$, the ring $\mathbb{Z}/p\mathbb{Z}$ is a [[finite field|~8f6e07c0]] of order $p$.
The [[order of a finite field is a prime power|~fd12b179]] $p^n$, where $p$ is the characteristic.
The field $\mathbb{F}_2[x]/(x^2 + x + 1)$ is a finite field of order $4$. It is not $\mathbb{Z}/4\mathbb{Z}$, which is not a field.
Finite fields are used in number theory, algebraic geometry, cryptography and coding theory.

## Explanations

### L1 human

A finite field is a finite set where you can add, subtract, multiply and divide by nonzero elements, with the usual rules.
The simplest ones are the integers modulo a prime.
