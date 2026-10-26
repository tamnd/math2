---
tag: 0X2T63GFQQ
kind: statement
role: proposition
name: Countable intersection of dense open sets is dense
msc: ["54E52"]
uses: [0D5KR33H7X, 0D198GPMTJ, 0DRKT1QJR7]
sources:
  - url: https://en.wikipedia.org/wiki/Baire_space
    locator: Definition
---

## Statement

Let $X$ be a [[Baire space|0D5KR33H7X]] and let $(U_n)_{n \in \mathbb{N}}$ be a sequence of open subsets of $X$, each [[dense|0D198GPMTJ]] in $X$.
Then $\bigcap_{n} U_n$ is dense in $X$.

## Remarks

Proof: let $F_n = X \setminus U_n$. Each $F_n$ is closed, and $\operatorname{int} F_n = X \setminus \overline{U_n} = \emptyset$. Thus $\operatorname{int} \bigcup_n F_n = \emptyset$. Its complement $\bigcap_n U_n$ therefore has closure $X$.
The converse also holds, so this property characterises Baire spaces.
In $\mathbb{R}$, for an enumeration $q_1, q_2, \ldots$ of $\mathbb{Q}$, the sets $U_n = \mathbb{R} \setminus \{q_n\}$ are open and dense. Their intersection is the set of irrational numbers, which is dense.
The intersection need not be open.

## Explanations

### L1 human

Each dense open set leaves out only a thin closed set.
In a Baire space, removing countably many thin sets still leaves a set that is everywhere.
