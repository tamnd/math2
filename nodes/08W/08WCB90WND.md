---
tag: 08WCB90WND
kind: statement
role: theorem
name: Hall's marriage theorem
msc: [05D15]
sources:
  - url: https://en.wikipedia.org/wiki/Hall's_marriage_theorem
    locator: Statement
same_as:
  wikidata: Q536640
  wikipedia: Hall's marriage theorem
---

## Statement

Let $\mathcal{F} = (S_1, \dots, S_n)$ be a finite family of finite sets.
A transversal of $\mathcal{F}$ is an injective function $f : \{1, \dots, n\} \to \bigcup_i S_i$ with $f(i) \in S_i$ for every $i$.
Then $\mathcal{F}$ has a transversal if and only if $\left| \bigcup_{i \in I} S_i \right| \ge |I|$ for every $I \subseteq \{1, \dots, n\}$.

## Remarks

The condition on all subfamilies is the marriage condition. It is clearly necessary, because $f$ maps $I$ injectively into $\bigcup_{i \in I} S_i$.
A transversal is also called a system of distinct representatives. The sets $S_i$ may repeat in the family.
The theorem is equivalent to [[Hall's theorem for bipartite graphs|0X2GJPNPFN]].

## History

Philip Hall proved the theorem in 1935.
The name marriage theorem comes from a 1950 paper by Halmos and Vaughan.

## Explanations

### L1 human

Each of $n$ people has a list of acceptable partners, and we want to give each person a different partner from the list.
This is possible exactly when every group of $k$ people has at least $k$ names on their lists together.
