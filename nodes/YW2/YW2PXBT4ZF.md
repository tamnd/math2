---
tag: YW2PXBT4ZF
kind: definition
name: Black hole
msc: [83C57]
defines: YHJ0PDNY8T
uses: [63ZKC7AFX2, 3HTF65XMF7, KZWG5F0TSB, E4TDQZ7DDV, R8KDE9QYNP]
sources:
  - url: https://en.wikipedia.org/wiki/Black_hole
---

## Definition

Let $(M, g)$ be a time-oriented [[spacetime|63ZKC7AFX2]] that is [[asymptotically flat|3HTF65XMF7]] at null infinity.
So there is a conformal compactification $(\tilde M, \tilde g)$ of $(M, g)$, as in a [[Penrose diagram|E4TDQZ7DDV]], whose boundary contains future null infinity $\mathcal{I}^+$.
Let $J^-(\mathcal{I}^+)$ be the [[causal past|KZWG5F0TSB]] of $\mathcal{I}^+$ in $\tilde M$: the set of points from which some future-directed causal curve reaches $\mathcal{I}^+$.
The *black hole region* of $(M, g)$ is
$$\mathcal{B} = M \setminus J^-(\mathcal{I}^+).$$
The spacetime *contains a black hole* if $\mathcal{B}$ is nonempty.
If $\Sigma$ is a [[Cauchy surface|R8KDE9QYNP]] of $M$, a *black hole at the time* $\Sigma$ is a connected component of $\mathcal{B} \cap \Sigma$.

## Remarks

Example: the Schwarzschild spacetime of mass $m$ in ingoing [[Eddington–Finkelstein coordinates|SG9GAYQT4R]], with $r > 0$.
From a point with $r > 2m$, an outgoing radial light ray reaches $\mathcal{I}^+$.
From a point with $r \le 2m$, every future-directed causal curve has $r$ non-increasing, so it never reaches $\mathcal{I}^+$.
Hence $\mathcal{B} = \set{0 < r \le 2m}$, and its boundary is the sphere $r = 2m$.

Non-example: in Minkowski space, from every point a light ray goes out to $\mathcal{I}^+$, so $J^-(\mathcal{I}^+) \supseteq M$ and $\mathcal{B}$ is empty.

The boundary of $\mathcal{B}$ in $M$ is the [[event horizon|D8NZ32Z3SQ]].
Many texts add a further condition, such as strong asymptotic predictability, to obtain good properties of black holes, for example in the [[Hawking area theorem|42EQ4G6978]].
The definition is global in time: deciding whether a point lies in $\mathcal{B}$ requires knowing the whole future of the spacetime.
