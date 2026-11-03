---
tag: 6X41CC3QWM
kind: definition
name: Linear complexity of a sequence
msc: [94A55, 94A60, 11B37]
defines: V2C6HQQAHK
uses: [WHX90SGEJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm
---

## Definition

Let $F$ be a field and let $s = (s_0, \dots, s_{N-1})$ be a finite sequence over $F$ with $N \ge 1$.
A [[linear-feedback shift register|WHX90SGEJ5]] of length $L \ge 0$ with coefficients $c_1, \dots, c_L \in F$ *generates* $s$ if
$$s_j + c_1 s_{j-1} + \cdots + c_L s_{j-L} = 0 \quad \text{for all } j \text{ with } L \le j \le N - 1.$$
The *linear complexity* $\Lambda(s)$ is the smallest $L$ such that some register of length $L$ generates $s$.
For an infinite sequence $s = (s_j)_{j \ge 0}$, the linear complexity is the supremum of the linear complexities of its initial segments $(s_0, \dots, s_{N-1})$, $N \ge 1$.

## Remarks

Always $0 \le \Lambda(s) \le N$, because a register of length $N$ generates any sequence of length $N$ with no condition to check.
$\Lambda(s) = 0$ exactly when $s$ is all zeros, by the convention that a register of length $0$ generates only zeros.

Example: over $\F_2$ let $s = (1, 1, 0, 1, 1, 0)$.
The register with $L = 2$ and $c_1 = c_2 = 1$ generates $s$, since $s_j = s_{j-1} + s_{j-2}$ for $j = 2, \dots, 5$.
No register of length $1$ does: from $s_1 = c_1 s_0$ we get $c_1 = 1$ over $\F_2$, and then $s_2$ would be $1$, not $0$.
So $\Lambda(s) = 2$.

Non-example: over $\F_2$ let $s = (0, 0, 1)$.
Any register of length $L \le 2$ starting from the zeros $s_0, \dots, s_{L-1}$ computes $s_2 = -(c_1 s_1 + \cdots) = 0 \ne 1$, so it fails to generate $s$; hence $\Lambda(s) = 3$.

For an infinite periodic sequence, the linear complexity equals the degree of its minimal polynomial, the monic generator of the ideal of polynomials whose recurrence the sequence satisfies.
An m-sequence produced by a register of length $L$ has linear complexity $L$.
Massey showed that if $2\Lambda(s) \le N$, the shortest register generating $s$ is unique.
