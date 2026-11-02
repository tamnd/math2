---
tag: KPJED63FT6
kind: definition
name: Growth of algebras
msc: [16P90]
defines: EHY4PYSMGZ
uses: [3CTW1P4HBP, 04C5ZBG1WT, 000AYPA9AJ, 4CMRM3975W, MNP2HBWB5Q]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand–Kirillov_dimension
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $A$ be a finitely generated [[associative algebra|3CTW1P4HBP]] over $k$ with identity.
Let $V \subseteq A$ be a finite-dimensional [[subspace|000AYPA9AJ]] that contains $1$ and generates $A$ as an algebra.
For $n \ge 0$, let $V^n$ be the span of all products $v_1 v_2 \cdots v_n$ with $v_i \in V$, with $V^0 = k$.
The *growth function* of $A$ with respect to $V$ is
$$d_V(n) = \dim_k V^n.$$
For functions $f, g \colon \N \to \N$, write $f \preceq g$ if there is an integer $c \ge 1$ with $f(n) \le g(cn)$ for all $n$, and $f \sim g$ if $f \preceq g$ and $g \preceq f$.
The *growth* of $A$ is the class of $d_V$ under $\sim$.

## Remarks

The growth does not depend on $V$.
If $W$ is another such subspace, then $W \subseteq V^c$ for some $c$, because $W$ is finite-dimensional and $\bigcup_n V^n = A$; so $d_W(n) \le d_V(cn)$, and symmetrically.

The algebra $A$ has *polynomial growth* if $d_V(n) \le C n^r$ for some constants $C, r$.
It has *exponential growth* if $d_V(n) \ge a^n$ for some $a > 1$ and all $n$.
Otherwise it has *intermediate growth*.

Example: for $A = k[x, y]$ and $V = k + kx + ky$, the space $V^n$ has the basis of monomials $x^i y^j$ with $i + j \le n$.
So $d_V(n) = (n+1)(n+2)/2$, and $A$ has polynomial growth.

Non-example of the setting: the field $k(x)$ of rational functions is not a finitely generated $k$-algebra, so no growth function is defined for it in this way.

For a finitely generated [[group|4CMRM3975W]] $G$ with a finite symmetric generating set $S$, take $A = k[G]$, the [[group algebra|MNP2HBWB5Q]], and $V$ the span of $\set{1} \cup S$.
Then $V^n$ has the basis of group elements of word length at most $n$, so the growth of $k[G]$ is the growth of $G$.
