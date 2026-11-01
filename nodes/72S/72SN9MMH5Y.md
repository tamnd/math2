---
tag: 72SN9MMH5Y
kind: definition
name: Absolute neighborhood retract
msc: [54C55, 54C15]
defines: DK3MT3HYX5
uses: [091GJ3FYD7, 0QT00PB5G2, 0ZCK8DQYN1, 02BH3MCBQB, 0VGFHTM75Y, 0X52TNMTCJ]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_neighborhood_retract
---

## Definition

Let $Y$ be a topological space and $A \subseteq Y$.
A *retraction* of $Y$ onto $A$ is a [[continuous|0VGFHTM75Y]] map $r \colon Y \to A$ with $r(a) = a$ for all $a \in A$.

Let $X$ be a [[metrizable space|091GJ3FYD7]].
$X$ is an *absolute neighborhood retract* (ANR) if the following holds for every metrizable space $Y$.
Let $h$ be any [[homeomorphism|0QT00PB5G2]] of $X$ onto a [[closed|0ZCK8DQYN1]] subset $h(X)$ of $Y$.
Then there is an [[open|02BH3MCBQB]] set $U \subseteq Y$ with $h(X) \subseteq U$ and a retraction of $U$ onto $h(X)$.
$X$ is an *absolute retract* (AR) if one can always take $U = Y$.

## Remarks

Some authors define these classes for compact metrizable spaces only, or for other classes of spaces; the definition above is for metrizable spaces.
Equivalently, $X$ is an ANR if every continuous map $f \colon A \to X$ from a closed subset $A$ of a metrizable space $Y$ extends to a continuous map on some open set $U \supseteq A$.

Example: $X = [0, 1]$ is an AR.
Given $h$ as above, the map $h^{-1} \colon h(X) \to [0, 1]$ is continuous on the closed set $h(X)$, and by the [[Tietze extension theorem|0X52TNMTCJ]] it extends to a continuous $g \colon Y \to [0, 1]$.
Then $r = h \circ g$ is a retraction of $Y$ onto $h(X)$.

Non-example: $X = \set{0} \cup \set{1/n : n \ge 1}$, a closed subset of $Y = \R$, with $h$ the inclusion.
Any open $U \supseteq X$ contains an interval $(-\varepsilon, \varepsilon)$.
A retraction $r \colon U \to X$ would map this connected interval onto a connected subset of $X$ that contains $0$ and $1/n$ for large $n$, which is impossible.
