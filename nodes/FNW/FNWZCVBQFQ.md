---
tag: FNWZCVBQFQ
kind: definition
name: Evaluation strategy
msc: [68N18, 03B40, 68Q55]
defines: MDFT90XEQ8
uses: [BD756KR8FM, Y9B9CVY6SJ, FPD6AN79QX]
sources:
  - url: https://en.wikipedia.org/wiki/Evaluation_strategy
---

## Definition

Let $\Lambda$ be the set of terms of the [[lambda calculus|BD756KR8FM]].
A *reduction strategy* for $\beta$-reduction is a partial map $S \colon \Lambda \to \Lambda$ with these properties.

1. $S(M)$ is defined exactly when $M$ is not in [[beta normal form|FPD6AN79QX]].
2. If $S(M)$ is defined, then $M \to_\beta S(M)$ by one step of [[beta reduction|Y9B9CVY6SJ]].

The strategy computes from $M$ the sequence $M, S(M), S(S(M)), \ldots$, which stops when a normal form is reached.

Two standard strategies are these.
The *normal order* strategy contracts the leftmost outermost redex, the one whose $\lambda$ stands furthest to the left in the written term.
The *applicative order* strategy contracts the leftmost innermost redex, a redex that contains no other redex.

## Remarks

Normalization theorem: if $M$ has a $\beta$-normal form, the normal order strategy reaches it after finitely many steps.

Example: let $\Omega = (\lambda x.\, x\, x)(\lambda x.\, x\, x)$ and $M = (\lambda x.\, y)\, \Omega$.
Normal order contracts the outer redex and gives $y$ in one step.
Applicative order contracts the redex $\Omega$ inside the argument and gets $M$ again, so it never terminates.

Non-example: a map with $S((\lambda x.\, x)\, y) = (\lambda x.\, x)\, y$ is not a reduction strategy.
It fails clause 2, since the only one-step reduct of $(\lambda x.\, x)\, y$ is $y$.

In programming languages, *call-by-name* and *call-by-value* are weak versions of these two strategies: they never reduce inside a $\lambda$-abstraction.
