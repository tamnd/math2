---
tag: W8XEZR3VKQ
kind: statement
role: lemma
name: Tube lemma
msc: [54D30, 54B10]
uses: [0CQHFPGJ45, 0TVJZYB6SH, 0GBG8B49AA, 02BH3MCBQB]
about: [0TVJZYB6SH, 0GBG8B49AA]
sources:
  - url: https://en.wikipedia.org/wiki/Tube_lemma
same_as:
  wikidata: Q3830116
  wikipedia: Tube lemma
---

## Statement

Let $X$ and $Y$ be [[topological spaces|0CQHFPGJ45]], with $Y$ [[compact|0TVJZYB6SH]], and give $X \times Y$ the [[product topology|0GBG8B49AA]].
Let $x_0 \in X$, and let $N$ be an [[open set|02BH3MCBQB]] of $X \times Y$ with $\set{x_0} \times Y \subseteq N$.
Then there is an open set $W \subseteq X$ with $x_0 \in W$ and $W \times Y \subseteq N$.

## Remarks

For each $y \in Y$, there is a basic open box $U_y \times V_y \subseteq N$ that contains $(x_0, y)$.
The sets $V_y$ cover the compact space $Y$, so finitely many $V_{y_1}, \ldots, V_{y_n}$ cover it.
Then $W = U_{y_1} \cap \cdots \cap U_{y_n}$ is open, contains $x_0$, and satisfies $W \times Y \subseteq N$.

The lemma gives the proof that the [[product of two compact spaces is compact|09ZKE5XQ74]].
It also shows that the projection $X \times Y \to X$ is a [[closed map|00FSJTXPJM]] when $Y$ is compact.

Compactness of $Y$ is necessary.
Let $X = Y = \R$, $x_0 = 0$, and $N = \set{(x, y) : \abs{xy} < 1}$.
Then $\set{0} \times \R \subseteq N$, but for any $\varepsilon > 0$ the point $(\varepsilon / 2, 4 / \varepsilon)$ lies in $(-\varepsilon, \varepsilon) \times \R$ and not in $N$.

## Explanations

### L1 human

Picture $X \times Y$ with $X$ horizontal and $Y$ vertical, and a vertical slice $\set{x_0} \times Y$ inside an open set $N$.
The lemma says that a whole vertical tube around the slice also fits inside $N$, as long as $Y$ is compact.
Without compactness, $N$ can get thinner and thinner as you go up, and no tube fits.

### L2 human

The tube lemma is the key step in the proof that a finite product of compact spaces is compact.
A more general form says that if $A \subseteq X$ and $B \subseteq Y$ are compact and $A \times B \subseteq N$ with $N$ open, then there are open $U \supseteq A$ and $V \supseteq B$ with $U \times V \subseteq N$.
This general form is often used to show that compact sets in Hausdorff spaces can be separated by open sets.
