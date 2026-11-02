---
tag: WH1MR8VHE3
kind: definition
name: Inner model
msc: ["03E45"]
defines: G78W36EGMB
uses: [Y48FA69563, 0YSCSX5YZC, 0HE5WDQ9FJ]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_model
---

## Definition

Work in [[ZF|0HE5WDQ9FJ]], and let $M$ be a [[class|Y48FA69563]].
The class $M$ is an *inner model* if:

1. $M$ is transitive: if $x \in M$ and $y \in x$, then $y \in M$.
2. $M$ contains every [[ordinal|0YSCSX5YZC]].
3. $(M, \in)$ satisfies each axiom of ZF, that is, the relativization $\varphi^M$ holds for each axiom $\varphi$ of ZF.

## Remarks

The universe $V$ and the constructible universe $L$ are inner models.
For $L$, clause 1 holds because each level $L_\alpha$ is transitive, and clause 2 holds because $\alpha \in L_{\alpha + 1}$.
The set $L_{\omega_1}$ is a non-example: it is transitive, but it fails clause 2, since $\omega_1 \notin L_{\omega_1}$.
Clause 3 is a schema, one statement for each axiom, because satisfaction in a proper class is not expressed by a single formula.
A transitive proper class that satisfies ZF contains all ordinals, so some authors drop clause 2 and ask instead that $M$ be a proper class.
Some authors ask for the axioms of ZFC; the name "inner model of ZFC" makes this choice explicit.
