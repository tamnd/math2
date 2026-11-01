---
tag: X122TKFP9G
kind: definition
name: Error-correcting code
msc: [94B25, 94B05]
defines: TAE6K8NQ46
uses: [0BBTH3YSZA, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Error_correction_code
---

## Definition

Let $A$ be a [[finite set|0BBTH3YSZA]] with at least two elements, the alphabet, and let $n$ be a positive integer.
For words $x, y \in A^n$, the Hamming distance $d(x, y)$ is the number of positions $i$ with $x_i \ne y_i$.
A code of length $n$ over $A$ is a [[subset|0BJR9QR08E]] $C \subseteq A^n$ with at least two elements; its elements are the codewords.
The minimum distance of $C$ is $d(C) = \min \set{d(x, y) : x, y \in C,\ x \ne y}$.
For an integer $t \ge 0$, the code $C$ is $t$-error-correcting if for each word $y \in A^n$ there is at most one codeword $c \in C$ with $d(c, y) \le t$.

## Remarks

The code $C$ is $t$-error-correcting if and only if $d(C) \ge 2t + 1$.
One direction uses the triangle inequality of the Hamming distance: if $d(c, y) \le t$ and $d(c', y) \le t$, then $d(c, c') \le 2t$.
Example: the binary repetition code $C = \set{000, 111}$ has $d(C) = 3$, so it is $1$-error-correcting.
A word with at most one $1$ is within distance $1$ of $000$ only, and a word with at least two $1$'s is within distance $1$ of $111$ only.
Non-example: $C = \set{000, 011}$ is not $1$-error-correcting, because $001$ is at distance $1$ from both codewords.
A code with $M$ codewords, length $n$ and minimum distance $d$ is called an $(n, M, d)$ code.
When $A$ is a finite field and $C$ is a subspace of $A^n$, the code is a linear code.
