---
tag: 0HEF46RPEK
kind: statement
role: proposition
name: Union of open sets is open
msc: ["54E35"]
uses: [0A26X79RTB, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Open_set
    locator: Properties
---

## Statement

Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $(U_i)_{i \in I}$ be a family of [[open subsets|01ZQQDCERP]] of $X$, indexed by any set $I$.
Then the [[union|05GK32H72H]] $\bigcup_{i \in I} U_i$ is open in $X$.

## Remarks

Proof: let $x$ be in the union. Then $x \in U_j$ for some $j \in I$, and there is $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U_j$. This ball is also in the union. Then use [[open sets of a metric space|0A26X79RTB]].
The family can be infinite, and even uncountable.
In a general [[topological space|0CNQXVBHCX]], this property is one of the axioms.

## Explanations

### L1 human

Each point of the union lies in one of the open sets, and that set already gives a small ball about the point.
For example, the union of the intervals $(1/n, 1)$ for $n \ge 2$ is the open interval $(0, 1)$.
