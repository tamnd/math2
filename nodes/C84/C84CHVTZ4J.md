---
tag: C84CHVTZ4J
kind: definition
name: Injective resolution
msc: [18G10, 18G05, 13D02]
defines: ZW3W6FX4PW
uses: [Y9CZ3MTNF1, 5QRFTBF4PG, JB7ZBFBA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_module
---

## Definition

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]] and let $X$ be an object of $\mathcal{A}$.
An *injective resolution* of $X$ is a sequence of objects and morphisms
$$0 \to X \xrightarrow{\eta} I^0 \xrightarrow{d^0} I^1 \xrightarrow{d^1} I^2 \to \cdots$$
such that:

1. every $I^n$ is an [[injective object|5QRFTBF4PG]];
2. the sequence is [[exact|JB7ZBFBA9C]].

## Remarks

Example: over $\Z$, the sequence $0 \to \Z \to \Q \to \Q/\Z \to 0$ is an injective resolution of $\Z$.
It is exact, and $\Q$ and $\Q/\Z$ are divisible groups, which are [[injective modules|85H7PRHDPZ]] over $\Z$.
Non-example: $0 \to \Z \xrightarrow{\cdot 2} \Z \to \Z/2\Z \to 0$ is exact, but $\Z$ is not an injective $\Z$-module, since it is not divisible, so clause 1 fails.
One writes the resolution as the cochain complex $I^\bullet$ with the map $\eta$; then $H^0(I^\bullet) \cong X$ and $H^n(I^\bullet) = 0$ for $n > 0$.
If $\mathcal{A}$ has enough injectives, every object has an injective resolution; this holds for modules over any ring, since every module embeds into an injective module.
