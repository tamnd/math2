---
tag: Z9KYS2C3D9
kind: proof
name: Proof that the naive satisfaction schema is inconsistent
msc: ["03A05"]
topics: [6Q4JJ2MMV8]
audience: grad
proves: TD48630JFF
uses: [B20TDZV9WW, MFJXPAF0R0, 0RYYK8PG4S]
methods: [0J0XBKG64S]
sources:
  - url: https://plato.stanford.edu/entries/self-reference/
    locator: "Self-Reference and Paradox, 1.1 Semantic Paradoxes"
---

## Proof

1. Let $\eta(v)$ be the formula $\neg \mathrm{Sat}(v, v)$. It has exactly one free variable $v$.
2. Let $h$ be the code of $\eta$, by the fixed [[Gödel numbering|MFJXPAF0R0]]. So $\ulcorner \eta \urcorner$ is the numeral $\underline{h}$.
3. The [[naive satisfaction schema|B20TDZV9WW]] for $\eta$ is $\forall y\,(\mathrm{Sat}(\underline{h}, y) \leftrightarrow \neg \mathrm{Sat}(y, y))$.
4. Instantiate $y$ by the closed term $\underline{h}$. This gives $\mathrm{Sat}(\underline{h}, \underline{h}) \leftrightarrow \neg \mathrm{Sat}(\underline{h}, \underline{h})$.
5. Assume $\mathrm{Sat}(\underline{h}, \underline{h})$. Step 4 gives $\neg \mathrm{Sat}(\underline{h}, \underline{h})$, a contradiction.
6. So $\neg \mathrm{Sat}(\underline{h}, \underline{h})$ holds, by negation introduction from step 5.
7. Step 4, from right to left, and step 6 give $\mathrm{Sat}(\underline{h}, \underline{h})$ by modus ponens.
8. Steps 6 and 7 give a sentence and its negation. So the schema is inconsistent.

## Idea

The formula $\neg \mathrm{Sat}(v, v)$ expresses "heterological".
Applied to its own code, the schema says that it is true of itself if and only if it is not.
This is the diagonal step of Cantor's argument.

## Variants

1. The proof does not use the [[law of excluded middle|0RYYK8PG4S]], so the schema is inconsistent in intuitionistic logic too.
2. In the standard model, the same steps show that no arithmetical formula $\mathrm{Sat}(x, y)$ satisfies the schema for arithmetical formulas.
