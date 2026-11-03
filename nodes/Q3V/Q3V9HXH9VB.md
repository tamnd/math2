---
tag: Q3V9HXH9VB
kind: definition
name: System F
msc: [03B40, 03B38, 68N18]
defines: SVNYKTGQ48
uses: [2DP940895E, Y9B9CVY6SJ]
sources:
  - url: https://en.wikipedia.org/wiki/System_F
---

## Definition

Fix countable sets of term variables $x, y, \dots$ and type variables $\alpha, \beta, \dots$.
The types of *System F* are $\tau ::= \alpha \mid \tau \to \tau \mid \forall \alpha.\, \tau$, where $\forall \alpha$ binds $\alpha$.
The terms are $t ::= x \mid \lambda x{:}\tau.\, t \mid t\, t \mid \Lambda \alpha.\, t \mid t\, [\tau]$.
A context $\Gamma$ is a finite list of distinct term variables with types.
The typing relation $\Gamma \vdash t : \tau$ is the least relation closed under two groups of rules.
The first group is the variable, abstraction and application rules of the [[simply typed lambda calculus|2DP940895E]], and the second is the following.

1. Type abstraction: if $\Gamma \vdash t : \tau$ and $\alpha$ is not free in any type of $\Gamma$, then $\Gamma \vdash \Lambda \alpha.\, t : \forall \alpha.\, \tau$.
2. Type application: if $\Gamma \vdash t : \forall \alpha.\, \tau$ and $\sigma$ is a type, then $\Gamma \vdash t\, [\sigma] : \tau[\sigma/\alpha]$.

Reduction is [[beta reduction|Y9B9CVY6SJ]] for terms, $(\lambda x{:}\sigma.\, t)\, u \to t[u/x]$, together with beta reduction for types, $(\Lambda \alpha.\, t)\, [\sigma] \to t[\sigma/\alpha]$.

## Remarks

Example: $\vdash \Lambda \alpha.\, \lambda x{:}\alpha.\, x : \forall \alpha.\, \alpha \to \alpha$.
The check: $x : \alpha \vdash x : \alpha$, so the abstraction rule gives $\vdash \lambda x{:}\alpha.\, x : \alpha \to \alpha$, and $\alpha$ is not free in the empty context, so rule 1 applies.
The Church numerals have type $\forall \alpha.\, (\alpha \to \alpha) \to \alpha \to \alpha$; for example $2 = \Lambda \alpha.\, \lambda f{:}\alpha \to \alpha.\, \lambda x{:}\alpha.\, f\,(f\, x)$.

Non-example: in the context $x : \alpha$, rule 1 does not give $\Lambda \alpha.\, x : \forall \alpha.\, \alpha$, because $\alpha$ is free in the type of $x$.
Without this side condition, $x$ would get every type, and the system would type terms such as $(\Lambda \alpha.\, x)\, [\beta \to \beta]$ that misuse $x$.

The type $\forall \alpha.\, \alpha$ has no closed term; under Curry–Howard it is falsity, and this is the consistency of the corresponding logic.
