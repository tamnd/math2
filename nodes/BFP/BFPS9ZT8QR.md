---
tag: BFPS9ZT8QR
kind: definition
name: Operational semantics
msc: [68Q55, 68N15]
defines: N8SGDCGJTW
uses: [05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_semantics
---

## Definition

Let $L$ be a language given by a grammar.
Let $\mathcal{C}$ be a set of configurations, such as programs or pairs $\langle p, s \rangle$ of a program $p$ and a state $s$.
Let $\mathcal{F} \subseteq \mathcal{C}$ be a subset of final configurations.
A *small-step operational semantics* of $L$ is a [[binary relation|05AVARPXA2]] $\to$ on $\mathcal{C}$, called the transition relation.
It is defined as the least relation closed under a set of inference rules that follow the syntax of $L$.
No final configuration has a transition.
A program $p$ *evaluates* to a final configuration $c$ if $p \to^* c$, where $\to^*$ is the reflexive transitive closure of $\to$.
A *big-step operational semantics* is instead a relation $p \Downarrow v$ between configurations and final configurations.
It is again the least relation closed under a set of inference rules.

## Remarks

Example: take the expressions $e ::= n \mid e + e$ with numerals $n$, and let the final configurations be the numerals.
Take three rules.
First, $n_1 + n_2 \to n$, where $n$ is the sum of $n_1$ and $n_2$.
Second, if $e_1 \to e_1'$ then $e_1 + e_2 \to e_1' + e_2$.
Third, if $e_2 \to e_2'$ then $n_1 + e_2 \to n_1 + e_2'$.
Then $(1 + 2) + 4 \to 3 + 4 \to 7$, by the second rule and then the first.
The matching big-step rules are $n \Downarrow n$, and $e_1 + e_2 \Downarrow n$ if $e_1 \Downarrow n_1$, $e_2 \Downarrow n_2$ and $n$ is the sum of $n_1$ and $n_2$.

Non-example: adding the rule $n \to n$ for every numeral $n$ breaks the condition that final configurations have no transitions.
With it, $7 \to 7 \to 7 \to \cdots$, so a finished computation could still step forever, and termination could no longer be read off the relation.

A configuration $c \notin \mathcal{F}$ with no transition is *stuck*.
For deterministic languages the small-step and big-step forms usually agree: $p \to^* v$ with $v$ final if and only if $p \Downarrow v$.
