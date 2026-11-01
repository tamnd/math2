---
tag: KFYW0WN9AD
kind: definition
name: Completion of a valued field
msc: [12J10, 13J10]
defines: W168DS966V
uses: [ZFW9Q3WTAQ, 08EWT7J0SC, 0QZMTN5AXX, 0G4J7Z7WPJ]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_field
---

## Definition

Let $K$ be a field with an absolute value $\abs{\cdot}$, that is, a [[normed field|ZFW9Q3WTAQ]], with the metric $d(x, y) = \abs{x - y}$.
A *completion* of $(K, \abs{\cdot})$ is a field $\widehat{K}$ with an absolute value $\norm{\cdot}$, together with a field homomorphism $\iota \colon K \to \widehat{K}$, such that:

1. $\norm{\iota(x)} = \abs{x}$ for all $x \in K$.
2. $\widehat{K}$ is a [[complete metric space|08EWT7J0SC]] for the metric $(a, b) \mapsto \norm{a - b}$.
3. The image $\iota(K)$ is dense in $\widehat{K}$.

## Remarks

A completion exists and is unique up to a unique isomorphism of fields that preserves the absolute values and commutes with the maps from $K$.
One construction: the [[Cauchy sequences|0QZMTN5AXX]] in $K$ form a ring under termwise operations.
The sequences tending to $0$ form a maximal ideal, and the quotient is a field.
The absolute value of the class of $(x_n)$ is $\lim_n \abs{x_n}$.
As a metric space it is the [[completion of the metric space|0G4J7Z7WPJ]] $K$.
Example: $\R$ with the usual absolute value and the inclusion $\Q \to \R$ is a completion of $\Q$; clause 3 holds because every real number is a limit of rationals.
Example: for a prime $p$, the [[p-adic numbers|BT6T702C28]] $\Q_p$ are the completion of $\Q$ for the [[p-adic absolute value|WGN82TCEF2]].
Non-example: the inclusion $\Q \to \C$ satisfies clauses 1 and 2 for the usual absolute values but fails clause 3, since the closure of $\Q$ in $\C$ is $\R$.
For a [[non-Archimedean absolute value|1H5F1BP6XS]], the completion has the same value group and the same residue field as $K$.
