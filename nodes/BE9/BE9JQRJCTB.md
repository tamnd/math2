---
tag: BE9JQRJCTB
kind: definition
name: Context-free language
msc: [68Q45, 68Q42]
defines: Q56EWEQYE2
uses: [CTCY2R8Q77, 5MFZ4VNY6D, 18WVBDCS38]
sources:
  - url: https://en.wikipedia.org/wiki/Context-free_language
---

## Definition

Let $\Sigma$ be a finite alphabet.
A [[formal language|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ is *context-free* if $L = L(G)$ for some [[context-free grammar|CTCY2R8Q77]] $G$ with terminal alphabet $\Sigma$.

## Remarks

Example: $L = \set{a^n b^n : n \ge 0}$ is context-free, since the grammar with rules $S \to aSb$ and $S \to \varepsilon$ generates it.
Every [[regular language|18WVBDCS38]] is context-free: a grammar with rules of the forms $A \to aB$, $A \to a$ and $A \to \varepsilon$ generates it.
Non-example: $\set{a^n b^n c^n : n \ge 0}$ is not context-free; no context-free grammar generates it.
The intersection of the context-free languages $\set{a^n b^n c^m}$ and $\set{a^m b^n c^n}$ is this language, so the class is not closed under intersection.
