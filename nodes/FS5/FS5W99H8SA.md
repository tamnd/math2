---
tag: FS5W99H8SA
kind: definition
name: Encoding of data
msc: [68Q01, 68P30, 03D10]
defines: EV03FVHX37
uses: [SEVFW9PNMC, D9FCP61J44, 09NWETVTNY]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel_numbering
---

## Definition

Let $A$ be a set and let $\Sigma$ be an [[alphabet|SEVFW9PNMC]], with $\Sigma^*$ the set of [[strings|D9FCP61J44]] over $\Sigma$.
An *encoding* of $A$ over $\Sigma$ is an [[injective function|09NWETVTNY]] $e \colon A \to \Sigma^*$.
The string $e(a)$ is the code of $a$, often written $\langle a \rangle$.
A *decoding* for $e$ is a map $d \colon \Sigma^* \to A \cup \set{\bot}$ with $d(e(a)) = a$ for every $a \in A$, where $\bot$ marks strings that are not codes.

## Remarks

Every encoding has a decoding, since $e$ is injective; in computability one also asks that $e$ and a decoding be computable.
Example: the binary numeral without leading zeros, with $0$ written as $0$, is an encoding of $\N$ over $\set{0, 1}$.
It is injective, since a numeral without leading zeros determines its value and the value determines the numeral.
Non-example: the map $\N \to \set{0,1}^*$ that sends $n$ to its last binary digit is not an encoding, since $1$ and $3$ both get the string $1$.
Codes of pairs are often built by concatenation with a separator, for example $\langle a, b \rangle = \langle a \rangle \# \langle b \rangle$ over $\Sigma \cup \set{\#}$.
A [[Gödel numbering|MFJXPAF0R0]] is an encoding into $\N$ instead of $\Sigma^*$, and binary numerals turn one into the other.
