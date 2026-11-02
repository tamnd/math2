---
tag: DWZYGTXKNS
kind: definition
name: Minimum description length
msc: [62B10, 94A17, 68Q30]
defines: 8JV9PPFRG4
uses: [K3AMMSY8DD, 0QB913WM5E]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum_description_length
---

## Definition

Let $D$ be data from a finite or countable set, and let $\mathcal{H}$ be a countable set of hypotheses.
Each hypothesis $H \in \mathcal{H}$ is a [[probability distribution|0QB913WM5E]] $P_H$ on the possible data, as in a [[statistical model|K3AMMSY8DD]].
Fix a prefix code for $\mathcal{H}$, with length $L(H)$ in bits for the codeword of $H$.
Let $L(D \mid H) = -\log_2 P_H(D)$ be the code length of $D$ with the code built from $P_H$.
The *two-part minimum description length* principle selects a hypothesis $H \in \mathcal{H}$ that minimizes
$$L(H) + L(D \mid H).$$

## Remarks

The length $-\log_2 P_H(D)$ is the length, up to rounding, of a Shannon code for $D$ built from $P_H$.
Example: for $n$ coin tosses with $h$ heads, take $\mathcal{H} = \set{\text{fair coin}, \text{coin with } p = h/n}$ with $L(H) = 1$ bit each.
The fair coin costs $1 + n$ bits; the other costs $1 + n\, \mathrm{H}(h/n)$ bits, where $\mathrm{H}$ is the binary entropy, so this toy rule picks it whenever $h \ne n/2$.
This is too generous, because the second hypothesis depends on the data.
A real two-part code must also encode $h$, which costs about $\log_2 (n + 1)$ bits, and then MDL picks the biased coin only when $h/n$ is far enough from $1/2$.
Non-example: minimizing $L(D \mid H)$ alone is maximum likelihood, not MDL, and it ignores the cost of complex hypotheses.
Refined versions of MDL replace the two-part code by a single universal code, such as the normalized maximum likelihood code.
