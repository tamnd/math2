---
tag: MNSCEZVVS3
kind: definition
name: Regular expression
msc: [68Q45]
defines: 4DMYF2PR4Q
uses: [RABRP2KG81, 5MFZ4VNY6D, ZW1M7XG8V4]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_expression
---

## Definition

Let $\Sigma$ be an [[alphabet|RABRP2KG81]].
The *regular expressions* over $\Sigma$ are the formulas given by these rules:

1. $\emptyset$ and $\varepsilon$ are regular expressions;
2. each letter $a \in \Sigma$ is a regular expression;
3. if $r$ and $s$ are regular expressions, then so are $(r + s)$, $(rs)$ and $(r^*)$.

Each regular expression $r$ denotes a [[formal language|5MFZ4VNY6D]] $L(r) \subseteq \Sigma^*$, defined by recursion:
$L(\emptyset) = \emptyset$, $L(\varepsilon) = \set{\varepsilon}$, $L(a) = \set{a}$, $L(r + s) = L(r) \cup L(s)$, $L(rs) = \set{uv : u \in L(r),\ v \in L(s)}$, and $L(r^*) = L(r)^*$, the [[Kleene star|ZW1M7XG8V4]] of $L(r)$.

## Remarks

Example: over $\Sigma = \set{a, b}$, $r = ((a + b)^*)a$ is a regular expression by rules 2 and 3.
Its language is the set of words ending with $a$: $L((a + b)^*)$ is all of $\Sigma^*$, and concatenation with $L(a) = \set{a}$ appends a final $a$.
Non-example: $a^n b^n$ with a variable exponent $n$ is not a regular expression, since no rule introduces exponents that vary; in fact no regular expression denotes $\set{a^n b^n : n \ge 0}$.
Common notations write $r \mid s$ or $r \cup s$ for $r + s$, and $r^+$ for $r r^*$.
Brackets are usually dropped with the convention that star binds tighter than concatenation, which binds tighter than union.
