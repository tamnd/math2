---
tag: 01FPXMTBX1
kind: statement
role: proposition
name: Composition of injections is injective
aliases: [injective-comp]
msc: ["03E20"]
uses: [0PVG1CRAJN, 07HF9YCWPP]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_function
    locator: Other properties
---

## Statement

Let $f \colon A \to B$ and $g \colon B \to C$ be [[injective functions|0PVG1CRAJN]].
Then the [[composition|07HF9YCWPP]] $g \circ f \colon A \to C$ is injective.

## Remarks

Proof: if $g(f(a)) = g(f(a'))$, then $f(a) = f(a')$ because $g$ is injective, and $a = a'$ because $f$ is injective.
A partial converse holds: if $g \circ f$ is injective, then $f$ is injective. The function $g$ need not be injective.

## Explanations

### L1 human

Think of $f$ and $g$ as machines, and of $g \circ f$ as the two machines in a chain.
If neither machine merges two inputs, the chain does not merge two inputs either.
