---
tag: 3VSFM7K70Z
kind: definition
name: Tree automaton
msc: [68Q45, 68Q42]
defines: TQWGW9X8VF
uses: [070R982G4B, SFMYM96C1B]
sources:
  - url: https://en.wikipedia.org/wiki/Tree_automaton
---

## Definition

A *ranked alphabet* is a [[finite set|070R982G4B]] $\mathcal{F}$ of symbols, each with an *arity* in $\N$.
The *terms* over $\mathcal{F}$ are the finite ordered labelled trees built by one rule.
If $f \in \mathcal{F}$ has arity $n$ and $t_1, \ldots, t_n$ are terms, then $f(t_1, \ldots, t_n)$ is a term.
For $n = 0$ this term is written $f$, and $T(\mathcal{F})$ denotes the set of all terms.

A *(nondeterministic bottom-up) finite tree automaton* over $\mathcal{F}$ is a tuple $A = (Q, \mathcal{F}, Q_f, \Delta)$ where:

1. $Q$ is a finite set of states;
2. $Q_f \subseteq Q$ is the set of final states;
3. $\Delta$ is a finite set of rules $f(q_1, \ldots, q_n) \to q$ with $f \in \mathcal{F}$ of arity $n$ and $q_1, \ldots, q_n, q \in Q$.

The automaton *reaches* $q$ on the term $f(t_1, \ldots, t_n)$ when there are states $q_1, \ldots, q_n$ with these properties.
For each $i$, $A$ reaches $q_i$ on $t_i$, and $f(q_1, \ldots, q_n) \to q$ is in $\Delta$.
The automaton *accepts* $t$ when it reaches some state of $Q_f$ on $t$, and its language is the set of accepted terms.

## Remarks

Example: let $\mathcal{F} = \set{0, 1, \land, \lor}$ with $0, 1$ of arity $0$ and $\land, \lor$ of arity $2$, let $Q = \set{q_0, q_1}$ and $Q_f = \set{q_1}$.
Take the rules $0 \to q_0$, $1 \to q_1$, $\land(q_i, q_j) \to q_{\min(i, j)}$ and $\lor(q_i, q_j) \to q_{\max(i, j)}$ for $i, j \in \set{0, 1}$.
By induction on the term, $A$ reaches $q_v$ exactly on the terms with Boolean value $v$, so it accepts the expressions that evaluate to $1$.
Non-example: a rule $\land(q_0) \to q_0$ is not allowed in clause 3, because $\land$ has arity $2$ and the rule lists only one state.
If all symbols have arity $1$ except one of arity $0$, terms are words read from the leaf upwards, and tree automata reduce to [[NFAs|SFMYM96C1B]].
Deterministic bottom-up tree automata recognize the same languages as nondeterministic ones, while deterministic top-down ones recognize fewer.
