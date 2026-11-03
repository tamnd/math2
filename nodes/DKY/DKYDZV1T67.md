---
tag: DKYDZV1T67
kind: definition
name: Lempel–Ziv coding
msc: [68P30, 94A29]
defines: GQBX1XFNG2
uses: [1P6EP01HZF, RABRP2KG81, 9DMSG5HAQX, DT0QXJE705]
sources:
  - url: https://en.wikipedia.org/wiki/LZ77_and_LZ78
---

## Definition

Let $\mathcal{X}$ be a finite [[alphabet|RABRP2KG81]] and let $x = x_1 x_2 \cdots x_n$ be a [[string|1P6EP01HZF]] over $\mathcal{X}$.
*Lempel–Ziv coding* names two [[algorithms|9DMSG5HAQX]] that encode $x$ by references to earlier parts of $x$.

1. *LZ78.* Parse $x$ into phrases $w_1, w_2, \dots, w_c$ with $x = w_1 w_2 \cdots w_c$. Each phrase $w_k$ is the shortest prefix of the unparsed rest of $x$ that differs from $w_1, \dots, w_{k-1}$. Only the last phrase may repeat an earlier one. Then $w_k = w_j a$ for some $j < k$, where $w_0$ is the empty string, and some $a \in \mathcal{X}$. The code of $x$ is the list of pairs $(j, a)$, with $j$ written in about $\log_2 k$ bits.
2. *LZ77.* Encode $x$ from left to right. At the current position, find the longest string that starts here and also starts at an earlier position within a fixed window. Output the triple (distance back to that position, length of the match, next symbol), and advance past the match and the next symbol.

## Remarks

Example: the LZ78 parsing of $x = 1011010100010$ is $1, 0, 11, 01, 010, 00, 10$.
The pairs are $(0,1), (0,0), (1,1), (2,1), (4,0), (2,0), (1,0)$; for instance $010 = w_4 0$ with $w_4 = 01$.
Non-example: the cut $1, 0, 1, 1, \dots$ is not the LZ78 parsing, since its third phrase $1$ repeats $w_1$ although it is not the last phrase.
For a [[stationary|DT0QXJE705]] ergodic source on a finite alphabet, the number of bits per symbol of LZ78 tends to the entropy rate almost surely, as $n \to \infty$.
Decoding is simple: the decoder rebuilds the same list of phrases as it reads the pairs.
