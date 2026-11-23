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

Let $M$ be the [[Kripke structure|RFQ8DJZNQT]] with states $s_0$, $s_1$, $s_2$ and edges $s_0 \to s_1$, $s_1 \to s_0$, $s_1 \to s_2$ and $s_2 \to s_2$.
Let $L(s_0) = L(s_1) = \{p\}$ and $L(s_2) = \{q\}$.
We compute the sets of states that satisfy $EG\,p$, $AF\,q$ and $EF\,q$ in [[CTL|1DA0Y6KDF8]].

1. The set $[\![ EG\,p ]\!]$ is the greatest set $Z \subseteq [\![ p ]\!]$ in which every state has a successor in $Z$.
   We start with $Z_0 = [\![ p ]\!] = \{s_0, s_1\}$ and remove states that have no successor left in the set.
2. The state $s_0$ has the successor $s_1 \in Z_0$, and $s_1$ has the successor $s_0 \in Z_0$.
   So no state is removed, and $[\![ EG\,p ]\!] = \{s_0, s_1\}$, with the witness path $s_0 s_1 s_0 s_1 \cdots$ for $s_0$.
3. By definition $AF\,q = \neg EG\,\neg q$.
   Here $[\![ \neg q ]\!] = \{s_0, s_1\}$, and the computation of step 2 gives $[\![ EG\,\neg q ]\!] = \{s_0, s_1\}$.
   So $[\![ AF\,q ]\!] = \{s_2\}$.
4. For $EF\,q$ we start with $\{s_2\}$ and add states with a successor in the set.
   First $s_1$ joins, because $s_1 \to s_2$, and then $s_0$ joins, because $s_0 \to s_1$.
   So $[\![ EF\,q ]\!] = \{s_0, s_1, s_2\}$.

## Remarks

The state $s_0$ satisfies $EF\,q$ but not $AF\,q$.
Reaching $q$ is possible, but it is not forced, because the loop $s_0 s_1$ can repeat forever.
This loop is also why $[\![ EG\,\varphi ]\!]$ is a greatest [[fixed point|DBD64TH52D]]: a path may stay in the set forever, so we start from everything allowed and only remove.

Change one edge and the answers move.
If we delete $s_1 \to s_0$ and add $s_0 \to s_0$, then $s_1$ has only the successor $s_2$, so $s_1$ leaves $[\![ EG\,p ]\!]$ and enters $[\![ AF\,q ]\!]$, while $s_0$ stays in $[\![ EG\,p ]\!]$ through its loop.
Under the fairness assumption "if $s_1 \to s_2$ is enabled infinitely often, it is taken", the original $s_0$ satisfies $AF\,q$ on fair paths.

## Explanations

### L1 human

A machine moves between two working states, and from the second it may stop for good.
"It can stop" is true at every state.
"It will surely stop" is true only once it has stopped, because it may keep working forever.

### L2 human

To compute $[\![ EG\,\varphi ]\!]$, start with the $\varphi$-states and keep removing those with no successor left in the set.
To compute $[\![ EF\,\varphi ]\!]$, start with the $\varphi$-states and keep adding those with a successor in the set.
Here the removal for $EG\,p$ stops at once, because $s_0$ and $s_1$ point to each other, and the adding for $EF\,q$ takes two rounds.
Watch out: $AF\,q$ is not "$q$ is reachable from all states"; that is $AG\,EF\,q$, which holds at every state here.
