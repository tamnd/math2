---
tag: 7V5WZPHC1B
kind: definition
name: Calculus of constructions
msc: [03B38, 03B40, 68V15]
defines: TKMY3F6KSA
uses: [M6W6ZB4PPX, Y9B9CVY6SJ, FRK1ZGYB7X]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_constructions
---

## Definition

The *calculus of constructions* is the pure type system with two sorts $*$ (also written $\mathsf{Prop}$) and $\square$ (also written $\mathsf{Type}$), given as follows.
The terms are $t ::= x \mid * \mid \square \mid t\, t \mid \lambda x{:}t.\, t \mid \Pi x{:}t.\, t$.
The typing relation $\Gamma \vdash t : T$ is the least relation closed under these rules, where $s, s_1, s_2$ range over $\set{*, \square}$.

1. Axiom: $\vdash * : \square$.
2. Start and weakening: if $\Gamma \vdash A : s$ and $x$ is a fresh variable, then $\Gamma, x : A \vdash x : A$, and every judgment of $\Gamma$ also holds in $\Gamma, x : A$.
3. Product: if $\Gamma \vdash A : s_1$ and $\Gamma, x : A \vdash B : s_2$, then $\Gamma \vdash \Pi x{:}A.\, B : s_2$, for each of the four pairs $(s_1, s_2)$.
4. Abstraction: if $\Gamma, x : A \vdash b : B$ and $\Gamma \vdash \Pi x{:}A.\, B : s$, then $\Gamma \vdash \lambda x{:}A.\, b : \Pi x{:}A.\, B$.
5. Application: if $\Gamma \vdash f : \Pi x{:}A.\, B$ and $\Gamma \vdash a : A$, then $\Gamma \vdash f\, a : B[a/x]$.
6. Conversion: if $\Gamma \vdash t : A$, $\Gamma \vdash B : s$ and $A$ and $B$ are equal up to [[beta reduction|Y9B9CVY6SJ]], then $\Gamma \vdash t : B$.

## Remarks

Example: $\vdash \lambda P{:}*.\, \lambda x{:}P.\, x : \Pi P{:}*.\, \Pi x{:}P.\, P$.
The check: $P : * \vdash P : *$ by rule 2, so rule 3 with $(*, *)$ gives $P : * \vdash \Pi x{:}P.\, P : *$, and rule 3 with $(\square, *)$ gives $\vdash \Pi P{:}*.\, \Pi x{:}P.\, P : *$.
Rule 4 applied twice gives the term its type.
Since $\Pi x{:}P.\, P$ does not depend on $x$, it is written $P \to P$, and the type reads "every proposition implies itself".

Non-example: $\square$ has no type, since no rule gives $\Gamma \vdash \square : T$.
So one cannot form $\Pi X{:}\square.\, X$, and there is no type of all types; this blocks Girard's paradox.

The four product rules $(*, *)$, $(\square, *)$, $(*, \square)$ and $(\square, \square)$ give terms depending on terms, terms on types, types on terms and types on types.
Dropping some of them gives the other corners of the [[lambda cube|FRK1ZGYB7X]], such as System F with only $(*, *)$ and $(\square, *)$.
