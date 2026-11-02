---
tag: BCETMS8K3X
kind: statement
role: theorem
name: Arthur–Selberg trace formula
msc: [11F72, 11F70, "22E55"]
uses: [BDAWKPBNQP, SEH68BA1QQ, VY0HXD3GC4, Z2CP530WDE, 0DEBXAJ5SA, 3C73HND6XA]
about: [3C73HND6XA]
sources:
  - url: https://en.wikipedia.org/wiki/Arthur%E2%80%93Selberg_trace_formula
same_as:
  wikidata: Q4800826
  wikipedia: Arthur–Selberg trace formula
---

## Statement

Let $F$ be a number field with [[adele ring|SEH68BA1QQ]] $\mathbb A$, and let $G$ be a connected reductive group over $F$.
Let $G(\mathbb A)^1$ be the common kernel of the maps $x \mapsto \abs{\chi(x)}$ for the rational characters $\chi$ of $G$, and assume that $G(F) \backslash G(\mathbb A)^1$ is compact.
Let $R$ be the right regular representation of $G(\mathbb A)^1$ on $L^2(G(F) \backslash G(\mathbb A)^1)$.
For a smooth compactly supported function $f$ on $G(\mathbb A)^1$, let $R(f) = \int f(y) R(y) \, dy$, with a fixed [[Haar measure|VY0HXD3GC4]].
Then $R(f)$ is a [[trace class operator|Z2CP530WDE]].
Its trace is given by
$$\sum_{\pi} m(\pi) \operatorname{tr} \pi(f) = \sum_{\gamma} \operatorname{vol}\big(G_\gamma(F) \backslash G_\gamma(\mathbb A)^1\big) \int_{G_\gamma(\mathbb A) \backslash G(\mathbb A)^1} f(x^{-1} \gamma x) \, dx.$$
Here $\pi$ runs over the irreducible unitary representations of $G(\mathbb A)^1$, and $m(\pi)$ is the multiplicity of $\pi$ in $R$.
The index $\gamma$ runs over representatives of the [[conjugacy classes|0DEBXAJ5SA]] of $G(F)$, and $G_\gamma$ is the centralizer of $\gamma$.
Both sides equal $\operatorname{tr} R(f)$.

## Remarks

This compact-quotient case is the direct generalisation of the [[Selberg trace formula|BDAWKPBNQP]].
The proof writes $R(f)$ as an integral operator with kernel $K(x, y) = \sum_{\gamma \in G(F)} f(x^{-1} \gamma y)$ and integrates the kernel over the diagonal.
Grouping the terms by conjugacy class gives the geometric side; the discrete decomposition of $L^2$ gives the spectral side.
For general $G$, such as $\mathrm{GL}_n$ with $n \ge 2$, the quotient is not compact and $R(f)$ is not trace class.
Arthur's trace formula then replaces both sides by truncated distributions $J_{\mathrm{geom}}(f) = J_{\mathrm{spec}}(f)$, which contain extra terms from the continuous spectrum and from non-semisimple conjugacy classes.
The spectral side encodes [[automorphic forms|3C73HND6XA]], the geometric side encodes orbital integrals, and comparing the formulas for two groups is the main tool for proving cases of Langlands functoriality.

## Explanations

### L1 human

The formula computes one number, the trace of an operator on functions on an adelic quotient, in two ways.
One way lists the automorphic representations with their multiplicities.
The other way lists the conjugacy classes of rational elements of the group, weighted by volumes and integrals.
Equating them turns questions about automorphic forms into questions about conjugacy classes, which are often easier.

### L2 human

The Selberg trace formula is the case of a cocompact Fuchsian group, seen through the real place only.
Jacquet and Langlands used a trace formula comparison to relate automorphic forms on $\mathrm{GL}_2$ and on a quaternion algebra.
The stabilization of the trace formula, completed with the fundamental lemma, allowed Arthur to classify the automorphic representations of classical groups.
