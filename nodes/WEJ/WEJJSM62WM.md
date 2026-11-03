---
tag: WEJJSM62WM
kind: definition
name: Ambiguous grammar
msc: [68Q42, 68Q45]
defines: HFD162F9PH
uses: [CTCY2R8Q77, Q56EWEQYE2, 0Y0JGC2K9T]
sources:
  - url: https://en.wikipedia.org/wiki/Ambiguous_grammar
---

## Definition

Let $G = (N, \Sigma, P, S)$ be a [[context-free grammar|CTCY2R8Q77]].
The grammar $G$ is *ambiguous* if some word $w \in L(G)$ has two different leftmost derivations from $S$.
Otherwise $G$ is *unambiguous*.

## Remarks

Equivalently, $G$ is ambiguous if some word of $L(G)$ has two different parse trees, since parse trees, which are [[rooted trees|0Y0JGC2K9T]], correspond one-to-one to leftmost derivations.
Example: the grammar with rules $E \to E + E$ and $E \to a$ is ambiguous.
The word $a + a + a$ has the two leftmost derivations $E \Rightarrow E + E \Rightarrow a + E \Rightarrow a + E + E \Rightarrow a + a + E \Rightarrow a + a + a$ and $E \Rightarrow E + E \Rightarrow E + E + E \Rightarrow a + E + E \Rightarrow a + a + E \Rightarrow a + a + a$.
Non-example: the grammar with rules $E \to E + a$ and $E \to a$ is unambiguous.
Every sentential form contains a single $E$, and a word with $k$ letters $a$ forces $k - 1$ uses of $E \to E + a$ followed by one use of $E \to a$.
A [[context-free language|Q56EWEQYE2]] is *inherently ambiguous* if every context-free grammar that generates it is ambiguous; $\set{a^i b^j c^k : i = j \text{ or } j = k}$ is such a language.
