---
tag: NFFK6YR3EV
kind: definition
name: Variable-length code
msc: [94A45, 94A29]
defines: BACPE6MVPZ
uses: [RABRP2KG81, 1P6EP01HZF, ZW1M7XG8V4, 09NWETVTNY]
sources:
  - url: https://en.wikipedia.org/wiki/Variable-length_code
---

## Definition

Let $\mathcal{X}$ be a finite or countable set, the source [[alphabet|RABRP2KG81]].
Let $\mathcal{D}$ be a finite set with at least two elements, the code alphabet.
Let $\mathcal{D}^+$ be the set of nonempty finite [[strings|1P6EP01HZF]] over $\mathcal{D}$.
A *variable-length code* for $\mathcal{X}$ over $\mathcal{D}$ is a map $C \colon \mathcal{X} \to \mathcal{D}^+$.
The strings $C(x)$ are its *codewords*, and $\abs{C(x)}$ is the length of the codeword of $x$.
The *extension* of $C$ is the map $C^* \colon \mathcal{X}^* \to \mathcal{D}^*$ on the [[Kleene stars|ZW1M7XG8V4]] given by $C^*(x_1 x_2 \cdots x_k) = C(x_1) C(x_2) \cdots C(x_k)$.

## Remarks

The code $C$ is *non-singular* when $C$ is [[injective|09NWETVTNY]], *uniquely decodable* when $C^*$ is injective, and a *prefix code* when no codeword is a proper prefix of another codeword.
Every prefix code is uniquely decodable, and every uniquely decodable code is non-singular.
For a random source symbol $X$ with law $p$, the expected length of $C$ is $L(C) = \sum_x p(x) \abs{C(x)}$.

Example: $C(a) = 0$, $C(b) = 10$, $C(c) = 11$ over $\mathcal{D} = \set{0, 1}$ is a prefix code.
A string such as $10011$ is decoded from the left: $10$ is a codeword, then $0$, then $11$, giving $bac$.

Non-example: $C(a) = 0$, $C(b) = 1$, $C(c) = 01$ is non-singular but not uniquely decodable, because $C^*(ab) = 01 = C^*(c)$.

## Explanations

### L1 human

A variable-length code writes each source symbol as a string of code letters, of a length that may depend on the symbol.
