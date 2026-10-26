---
tag: 0WE5BBHGM6
kind: definition
name: Totally bounded set
msc: ["54E35"]
defines: 020Q06TYYH
uses: [063W5JMY85, 0692CGQF00]
sources:
  - url: https://en.wikipedia.org/wiki/Totally_bounded_space
    locator: In metric spaces
---

## Definition

Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $S \subseteq X$.
The set $S$ is totally bounded when for each real $\varepsilon > 0$ there are finitely many sets $A_1, \ldots, A_n \subseteq X$ with $S \subseteq A_1 \cup \cdots \cup A_n$ and $\operatorname{diam}(A_k) < \varepsilon$ for each $k$.
The space $X$ is totally bounded when $X$ itself is a totally bounded set.

## Remarks

Here $\operatorname{diam}$ is the [[diameter|0692CGQF00]].
Each totally bounded set is [[bounded|0P953MG05E]]. The converse is false: an infinite set with the [[discrete metric|0NA4FK7B8S]] is bounded but not totally bounded.
In $\mathbb{R}^n$ with the Euclidean metric, a set is totally bounded if and only if it is bounded.
The [[epsilon-net characterisation|0NMGJJ19HD]] gives an equivalent form with balls.

## Explanations

### L1 human

A totally bounded set can be cut into finitely many small pieces, for each size of piece that you choose.
A bounded set only fits in one big ball, and this is not enough in infinite dimensions.
