---
tag: 116FWJPRZK
kind: definition
name: Model checking
msc: [68Q60, 03B44, 03B70]
defines: VNY0VXVZ53
uses: [NGHWZ9Y7ZV, RMJ56ZPA63, F6JA5C5BJX]
sources:
  - url: https://en.wikipedia.org/wiki/Model_checking
---

## Definition

Fix a temporal logic $\mathcal{L}$, such as [[linear temporal logic|RMJ56ZPA63]] or [[computation tree logic|F6JA5C5BJX]], over a set $AP$ of atomic propositions.
The *model checking problem* for $\mathcal{L}$ is the following decision problem.
The input is a finite [[Kripke structure|NGHWZ9Y7ZV]] $M = (S, R, L)$, a state $s \in S$ and a formula $\varphi$ of $\mathcal{L}$.
The question is whether $M, s \models \varphi$.

## Remarks

For CTL the problem can be solved in time $O(\abs{M} \cdot \abs{\varphi})$, where $\abs{M} = \abs{S} + \abs{R}$.
The algorithm labels the states with the subformulas of $\varphi$ that they satisfy, from the innermost subformula outward.
For LTL the problem is [[PSPACE-complete|JWC9CE07Q2]] in the size of $\varphi$, and it can be solved in time $O(\abs{M} \cdot 2^{O(\abs{\varphi})})$ through a [[Büchi automaton|92DM43HQZT]] for $\neg\varphi$.

Example: let $S = \set{s, t}$, $R = \set{(s, t), (t, s)}$, $L(s) = \set{p}$ and $L(t) = \emptyset$.
The only path from $s$ is $s\,t\,s\,t \cdots$, so $M, s \models G F p$ in LTL, while $M, s \not\models G p$, since $p \notin L(t)$.

An input with an infinite state set is not an instance of this problem as defined here; for such systems the question can be undecidable.
