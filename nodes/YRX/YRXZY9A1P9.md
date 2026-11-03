---
tag: YRXZY9A1P9
kind: statement
role: theorem
name: Dundas–Goodwillie–McCarthy theorem
msc: [19D55, 19D50, 55P42]
uses: [5AWJ6ZEG26, 6RQS843SE5, 2C1M0NWPB0, BAW0T68GWK, GC9026X05J]
about: [5AWJ6ZEG26, 6RQS843SE5]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_Hochschild_homology
---

## Statement

Let $f \colon A \to B$ be a map of connective associative [[ring spectra|BAW0T68GWK]].
Assume that $\pi_0 f \colon \pi_0 A \to \pi_0 B$ is surjective with nilpotent kernel.
Then the square
$$\begin{array}{ccc} K(A) & \xrightarrow{\mathrm{trc}} & TC(A) \\ \downarrow & & \downarrow \\ K(B) & \xrightarrow{\mathrm{trc}} & TC(B) \end{array}$$
is homotopy cartesian.
Here $K$ is the [[K-theory spectrum|2C1M0NWPB0]], $TC$ is [[topological cyclic homology|6RQS843SE5]] and $\mathrm{trc}$ is the [[cyclotomic trace|5AWJ6ZEG26]].

## Remarks

Equivalently, the cyclotomic trace induces an equivalence between the fibers, so relative K-theory equals relative $TC$.
A special case is a surjection of ordinary rings $A \to B$ whose kernel is a nilpotent ideal.
The theorem is an integral version of [[Goodwillie's theorem on relative K-theory|GC9026X05J]], which is the rational statement with cyclic homology.
McCarthy proved the case of simplicial rings and Dundas extended it to ring spectra; the full proof is presented in the book of Dundas, Goodwillie and McCarthy.
Example: Hesselholt and Madsen used it to compute the K-theory of truncated polynomial rings $k[x]/(x^n)$ over a perfect field $k$ of characteristic $p$.
The point is that $TC$ of these rings can be computed.

## Explanations

### L1 human

K-theory is hard to compute, but topological cyclic homology can often be computed by homotopy theory.
The theorem says that if one changes a ring only by a nilpotent piece, then K-theory and topological cyclic homology change by exactly the same amount.
So to compute K-theory of a ring like $k[x]/(x^n)$, it is enough to know K-theory of $k$ and to compute $TC$.

### L2 human

The theorem is the reason that trace methods work.
Combined with results on continuity of K-theory, it gives the K-theory of complete local rings and of $p$-adic integers in terms of $TC$.
