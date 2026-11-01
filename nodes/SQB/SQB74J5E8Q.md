---
tag: SQB74J5E8Q
kind: statement
role: theorem
name: Auslander–Buchsbaum formula
msc: [13D05, 13C15]
uses: [MZ02BKPHJA, 0670T59HGE, 05QY1VEBYD, MR9QCH1PNA, M2RADBFW99]
about: [MR9QCH1PNA, M2RADBFW99]
sources:
  - url: https://en.wikipedia.org/wiki/Auslander–Buchsbaum_formula
same_as:
  wikidata: Q4822773
  wikipedia: Auslander–Buchsbaum formula
---

## Statement

Let $(R, \mathfrak{m})$ be a commutative [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]].
Let $M$ be a nonzero [[finitely generated|05QY1VEBYD]] $R$-module of finite [[projective dimension|MR9QCH1PNA]].
Then
$$\operatorname{pd}_R M + \operatorname{depth} M = \operatorname{depth} R,$$
where $\operatorname{depth}$ is the [[depth|M2RADBFW99]] with respect to $\mathfrak{m}$.

## Remarks

One proof goes by induction on $\operatorname{depth} R$, using a minimal free resolution of $M$.
When the depths are positive, one divides by an element of $\mathfrak{m}$ that is a non-zero-divisor on both $R$ and $M$.
Example: for $R = K[\![x, y]\!]$, which has depth $2$, the residue field $K$ has projective dimension $2$ and depth $0$, and $R/(x)$ has projective dimension $1$ and depth $1$.
The hypothesis $\operatorname{pd}_R M < \infty$ is needed: for $R = K[x]/(x^2)$ and $M = K$, the depths are $0$ and $0$, but $\operatorname{pd}_R K = \infty$.
In particular, a finitely generated module of finite projective dimension has projective dimension at most $\operatorname{depth} R$.

## Explanations

### L1 human

For a finitely generated module of finite projective dimension over a local ring, two numbers add up to a constant.
The projective dimension counts how complicated the module is homologically.
The depth counts how much room the module has for regular sequences.
The more depth a module has, the shorter its resolution.

### L2 human

The formula is the main link between resolutions and regular sequences.
Over a [[regular local ring|63XXTF6B5M]], every finitely generated module has finite projective dimension, so the formula always applies there.
It shows that a module of finite projective dimension over a Cohen–Macaulay local ring is maximal Cohen–Macaulay exactly when it is free.
