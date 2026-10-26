---
tag: ~bf2debd1
kind: statement
role: theorem
name: Liouville's theorem
aliases: [liouvilles-theorem-complex-analysis]
msc: [30D20]
uses: [~bd6647a1, ~6496bb28]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis)
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis)
    locator: Proof
same_as:
  wikidata: Q576478
  wikipedia: Liouville's theorem (complex analysis)
---

## Statement

Let $f : \mathbb{C} \to \mathbb{C}$ be an [[entire function|~bd6647a1]].
Assume that $f$ is bounded: there is a real number $M$ with $|f(z)| \le M$ for each $z \in \mathbb{C}$.
Then $f$ is constant.

## Remarks

Proof: let $c \in \mathbb{C}$. By [[Cauchy's estimates|~6496bb28]], $|f'(c)| \le M / r$ for each $r > 0$. So $f'(c) = 0$ for each $c$, and $f$ is constant.
For example, $\sin$ is entire and not constant, so it is not bounded on $\mathbb{C}$. On $\mathbb{R}$ it is bounded, which shows that the theorem has no real analogue.
The theorem gives a short proof of the [[fundamental theorem of algebra|~1ba6b207]].

## Explanations

### L1 human

A holomorphic function on the whole plane cannot stay inside a bounded region unless it does not move at all.
Each nonconstant entire function, for example $z$, $e^z$ or $\cos z$, takes values that are as large as you like.
