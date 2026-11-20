---
tag: NFR5YGX6MS
kind: definition
name: Finitely axiomatizable theory
defines: JR6XPJ7X56
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
uses: [92SWXST1ZM, DKFGQTRYZE, MVCH6N9SNW, MEC3ZMC4F1]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: A basic elementary class
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Definition

Let $L$ be a signature and let $T$ be an $L$-[[theory|92SWXST1ZM]].

1. $T$ is *finitely axiomatizable* when there is a finite set $F$ of $L$-[[sentences|DKFGQTRYZE]] such that $T$ and $F$ have the same [[models|MVCH6N9SNW]], that is, $\operatorname{Mod}(T) = \operatorname{Mod}(F)$.
2. A class $K$ of $L$-structures is a *basic elementary class* when $K = \operatorname{Mod}(F)$ for a finite set $F$ of $L$-sentences.

Replacing $F$ by the conjunction of its members, one may take $F$ to be a single sentence.

## Notation

Some books write $\mathrm{EC}$ for the basic elementary classes and $\mathrm{EC}_\Delta$ for the [[elementary classes|MEC3ZMC4F1]].

## Remarks

Example: the theory of fields is finitely axiomatizable, by the conjunction of the field axioms.

Non-example: the theory $\set{\lambda_n : n \ge 2}$ of infinite sets, with $\lambda_n$ saying "there are at least $n$ elements", is not finitely axiomatizable, because each finite subset has a finite model.

Since $T$ and $F$ have the same models, they have the same consequences, and $T$ is finitely axiomatizable exactly when $\operatorname{Mod}(T)$ is a basic elementary class.

## Explanations

### L1 human

A theory is finitely axiomatizable when finitely many of its statements, possibly new ones, already say everything that it says.

### L2 human

We check that the theory $T = \set{\forall x \, \forall y \, (x = y)} \cup \set{\neg\lambda_n : n \ge 2}$ is finitely axiomatizable.

1. Every model of $\forall x \, \forall y \, (x = y)$ has one element, so it satisfies $\neg\lambda_n$ for every $n \ge 2$.
2. So $\operatorname{Mod}(T) = \operatorname{Mod}(\set{\forall x \, \forall y \, (x = y)})$, and $F = \set{\forall x \, \forall y \, (x = y)}$ works.

A trap is to count the axioms in a given presentation; an infinite presentation may have a finite equivalent.
