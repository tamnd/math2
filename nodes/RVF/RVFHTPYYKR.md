---
tag: RVFHTPYYKR
kind: definition
name: Kleene star
msc: [68Q45, 68R15]
defines: ZW1M7XG8V4
uses: [5VRS8PJEFT, D9FCP61J44]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene_star
---

## Definition

Let $\Sigma$ be an alphabet and let $L \subseteq \Sigma^*$ be a [[formal language|5VRS8PJEFT]].
Define $L^0 = \set{\varepsilon}$, where $\varepsilon$ is the empty [[string|D9FCP61J44]], and $L^{n+1} = L^n L = \set{uv : u \in L^n, v \in L}$ for $n \ge 0$.
The *Kleene star* of $L$ is
$$L^* = \bigcup_{n \ge 0} L^n.$$
So $w \in L^*$ exactly when $w = w_1 w_2 \cdots w_k$ for some $k \ge 0$ and $w_1, \dots, w_k \in L$.

## Remarks

Example: for $L = \set{ab}$, $L^* = \set{\varepsilon, ab, abab, ababab, \dots}$.
The string $abab$ is in $L^2$, with $w_1 = w_2 = ab$, so it is in $L^*$.
Non-example: $aba \notin L^*$, since every member of $L^*$ has even length.
Edge cases: $\emptyset^* = \set{\varepsilon}$, since $\emptyset^0 = \set{\varepsilon}$ and $\emptyset^n = \emptyset$ for $n \ge 1$.
The *Kleene plus* is $L^+ = \bigcup_{n \ge 1} L^n$, and $L^* = L^+ \cup \set{\varepsilon}$.
For an alphabet $\Sigma$, viewed as the language of strings of length $1$, $\Sigma^*$ is the set of all strings over $\Sigma$.
$L^*$ is the smallest language that contains $\varepsilon$ and $L$ and is closed under concatenation.
