---
tag: CX94SNDFX9
kind: definition
name: Supervisory control theory of discrete event systems
msc: [93C65, 68Q45]
defines: NQNMXGHZDR
uses: [W65B6BKZRY, 5MFZ4VNY6D, RABRP2KG81, ZW1M7XG8V4]
sources:
  - url: https://en.wikipedia.org/wiki/Supervisory_control_theory
---

## Definition

Let $\Sigma$ be a finite [[alphabet|RABRP2KG81]] of events, split into disjoint sets $\Sigma_c$ of controllable events and $\Sigma_{uc}$ of uncontrollable events.
Let $\Sigma^*$ be the set of finite strings over $\Sigma$ (the [[Kleene star|ZW1M7XG8V4]]), and let $\varepsilon$ be the empty string.
A *plant* (or generator) is a [[deterministic automaton|W65B6BKZRY]] $G = (Q, \Sigma, \delta, q_0)$ whose transition function $\delta$ may be partial.
The language $L(G)$ of $G$ is the set of strings $s \in \Sigma^*$ for which $\delta(q_0, s)$ is defined.
The prefix closure $\overline{K}$ of a [[language|5MFZ4VNY6D]] $K \subseteq \Sigma^*$ is the set of all prefixes of strings of $K$.

1. A *supervisor* for $G$ is a map $S \colon L(G) \to 2^{\Sigma}$ such that $\Sigma_{uc} \subseteq S(s)$ for every $s \in L(G)$; the set $S(s)$ lists the events enabled after $s$.
2. The *closed-loop language* $L(S/G)$ is defined by recursion: $\varepsilon \in L(S/G)$, and for $s \in \Sigma^*$ and $\sigma \in \Sigma$, $s\sigma \in L(S/G)$ if and only if $s \in L(S/G)$, $s\sigma \in L(G)$ and $\sigma \in S(s)$.
3. A language $K \subseteq \Sigma^*$ is *controllable* with respect to $G$ if $\overline{K}\,\Sigma_{uc} \cap L(G) \subseteq \overline{K}$.

Supervisory control theory is the study of supervisors, closed-loop languages and controllable languages.

## Remarks

The basic result of the theory: for a nonempty language $K \subseteq L(G)$, there is a supervisor $S$ with $L(S/G) = \overline{K}$ if and only if $K$ is controllable.
A union of controllable languages is controllable, so every language $E$ has a largest controllable sublanguage.
It gives the least restrictive supervisor for the specification $E$.

Example: let $\Sigma = \set{a, b}$ with $\Sigma_c = \set{a}$ and $\Sigma_{uc} = \set{b}$, and let $G$ have one state with a loop for each event, so $L(G) = \Sigma^*$.
The language $K = b^*$ is prefix-closed and $K \Sigma_{uc} = b^* b \subseteq K$, so $K$ is controllable.
The supervisor with $S(s) = \set{b}$ for all $s$ disables $a$ and gives $L(S/G) = b^*$.

Non-example: in the same plant, $K = \set{\varepsilon, a}$ is not controllable.
Indeed $b \in \overline{K}\,\Sigma_{uc} \cap L(G)$ but $b \notin \overline{K}$: no supervisor can prevent the uncontrollable event $b$ at the start.
