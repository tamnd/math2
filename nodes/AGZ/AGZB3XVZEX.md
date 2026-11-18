---
tag: AGZB3XVZEX
kind: example
name: Computing EG p and AF q on a three-state structure
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [F6JA5C5BJX]
uses: [1DA0Y6KDF8, RFQ8DJZNQT, DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
    locator: section Semantics of CTL
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Example

Let $M$ be the [[Kripke structure|RFQ8DJZNQT]] with states $s_0, s_1, s_2$ and edges $s_0 \to s_1$, $s_1 \to s_0$, $s_1 \to s_2$, $s_2 \to s_2$.
Let $L(s_0) = L(s_1) = \set{p}$ and $L(s_2) = \set{q}$.
We compute the sets of states that satisfy $EG\,p$ and $AF\,q$ in [[CTL|1DA0Y6KDF8]].

1. $[\![ EG\,p ]\!]$ is the greatest set $Z \subseteq [\![ p ]\!]$ in which every state has a successor in $Z$.
2. Start with $Z_0 = [\![ p ]\!] = \set{s_0, s_1}$.
3. $s_0$ has the successor $s_1 \in Z_0$, and $s_1$ has the successor $s_0 \in Z_0$. So no state is removed, and $[\![ EG\,p ]\!] = \set{s_0, s_1}$.
4. The witness path for $s_0$ is $s_0 s_1 s_0 s_1 \cdots$.
5. By definition $AF\,q = \neg EG\,\neg q$. Here $[\![ \neg q ]\!] = \set{s_0, s_1}$, and the same computation gives $[\![ EG\,\neg q ]\!] = \set{s_0, s_1}$.
6. So $[\![ AF\,q ]\!] = \set{s_2}$.
7. On the other hand, $[\![ EF\,q ]\!] = \set{s_0, s_1, s_2}$, since $s_2$ is reachable from every state.

## Remarks

The state $s_0$ satisfies $EF\,q$ but not $AF\,q$: reaching $q$ is possible but not forced, because the loop $s_0 s_1$ can repeat forever.
This loop is the reason why $[\![ EG ]\!]$ is a greatest fixed point: a path can stay in the set forever.
Under the fairness assumption "if $s_1 \to s_2$ is enabled infinitely often, it is taken", the state $s_0$ would satisfy $AF\,q$ on fair paths.

## Explanations

### L1 human

A machine moves between two working states, and from the second it may stop for good.
"It can stop" is true at every state.
"It will surely stop" is true only once it has stopped, because it may keep working forever.

### L2 human

To compute $[\![ EG\,\varphi ]\!]$, start with the $\varphi$-states and keep removing those with no successor left in the set.
To compute $[\![ EF\,\varphi ]\!]$, start with the $\varphi$-states and keep adding those with a successor in the set.

1. Here the removal step stops at once, because $s_0$ and $s_1$ point to each other.
2. The adding step for $EF\,q$ adds $s_1$ first, then $s_0$.

A trap: $AF\,q$ is not "$q$ is reachable from all states"; that is $AG\,EF\,q$.
