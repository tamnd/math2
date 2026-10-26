---
tag: 051VYKA1EX
kind: statement
role: lemma
name: Euclid's lemma
msc: [11A05]
uses: [0SN0MAEKYX, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_lemma
    locator: Formulations
same_as:
  wikidata: Q206793
  wikipedia: Euclid's lemma
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]], and let $a$ and $b$ be integers.
If $p \mid a b$, then $p \mid a$ or $p \mid b$.

## Remarks

The hypothesis that $p$ is prime is necessary. For example, $6 \mid 4 \cdot 9$, but $6 \nmid 4$ and $6 \nmid 9$.
A short proof uses [[Bézout's identity|0DQVHMYAGA]]. If $p \nmid a$, then $\gcd(p, a) = 1$, so $p x + a y = 1$ for some integers $x$ and $y$. Multiply by $b$ to see that $p \mid b$.
The [[generalized Euclid's lemma|03BAREW1Z5]] replaces the prime $p$ by an integer that is coprime to $a$.
The lemma is the main step in the proof of the uniqueness part of the [[fundamental theorem of arithmetic|084HH1NDCB]].

## History

The lemma is Proposition 30 of Book VII of the Elements of Euclid.

## Explanations

### L1 human

A prime cannot be split into smaller factors, so it cannot share itself between $a$ and $b$.
If $7$ divides a product $a b$, then $7$ already divides $a$ or $b$.
For example, $7 \mid 14 \cdot 3$ and $7 \mid 14$.
