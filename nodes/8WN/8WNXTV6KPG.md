---
tag: 8WNXTV6KPG
kind: definition
name: Complexity class
msc: [68Q15]
defines: ESPYW94XGR
uses: [YAVW1XHNFH, 5MFZ4VNY6D, 758EYCN27B, T00W8RQT8E, FDNFGKEEJR]
sources:
  - url: https://en.wikipedia.org/wiki/Complexity_class
---

## Definition

Let $\Sigma$ be a finite alphabet.
Fix a model of computation, such as deterministic or nondeterministic [[Turing machines|758EYCN27B]].
Fix a resource measure on it, such as [[time|T00W8RQT8E]] or [[space|FDNFGKEEJR]].
Fix a set $\mathcal{F}$ of functions $\N \to \N$, the allowed bounds.
The *complexity class* given by these data is the set of all [[languages|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ with the following property.
For some $f \in \mathcal{F}$, some machine of the model decides $L$ and uses at most $f(n)$ units of the resource on every input of length $n$.

## Remarks

Example: take deterministic multitape Turing machines, the time measure, and $\mathcal{F} = \set{n \mapsto c n^k + c : c, k \in \N}$.
The class obtained is P, the class of [[decision problems|YAVW1XHNFH]] solvable in polynomial time.

Non-example: the set of all languages $L \subseteq \set{0,1}^*$ is not a complexity class in this sense for any bounds.
It is uncountable, while there are only countably many machines, so it contains undecidable languages.

The word is also used more loosely.
Classes defined by circuits, by oracles, by probabilistic or quantum machines, or by counting problems instead of decision problems are also called complexity classes.
