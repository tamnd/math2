---
tag: 8WBY6R28CR
kind: example
name: Representations of sl2
msc: [17B10, 81R05]
illustrates: [J1EFY61K87]
uses: [1ZAT1Z967A, TZAZ163QGK, HFW8642GBK, C5W8BE1DRY, 92EXQ237Q6]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_theory_of_semisimple_Lie_algebras
---

## Example

Let $\mathfrak{g} = \mathfrak{sl}_2(\C)$, the [[special linear Lie algebra|1ZAT1Z967A]] of complex $2 \times 2$ matrices of trace zero, with basis
$$e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad f = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad h = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},$$
so that $[h, e] = 2e$, $[h, f] = -2f$ and $[e, f] = h$.
For each integer $n \ge 0$, let $V_n$ have basis $v_0, \dots, v_n$, and put $v_{-1} = v_{n+1} = 0$.
Define
$$h v_k = (n - 2k) v_k, \qquad f v_k = (k + 1) v_{k+1}, \qquad e v_k = (n - k + 1) v_{k-1}.$$
This is a [[representation|TZAZ163QGK]] of dimension $n + 1$.
Check of $[e, f] = h$ on $v_k$: $(ef - fe) v_k = \big( (k + 1)(n - k) - k(n - k + 1) \big) v_k = (n - 2k) v_k$.
Check of $[h, e] = 2e$ on $v_k$: $(he - eh) v_k = (n - k + 1)\big( (n - 2k + 2) - (n - 2k) \big) v_{k-1} = 2 e v_k$; the relation $[h, f] = -2f$ is checked the same way.

The classification: each $V_n$ is [[irreducible|HFW8642GBK]] with [[highest weight|C5W8BE1DRY]] $n$, and each finite-dimensional irreducible $\mathfrak{g}$-module is isomorphic to exactly one $V_n$.
By [[Weyl's theorem|92EXQ237Q6]], every finite-dimensional $\mathfrak{g}$-module is a direct sum of copies of the $V_n$.

## Remarks

The module $V_n$ is realised on homogeneous polynomials of degree $n$ in $x, y$, with $e = x \partial_y$, $f = y \partial_x$ and $h = x \partial_x - y \partial_y$.
For $n = 1$ this is the defining representation on $\C^2$, and $V_2$ is the adjoint representation.
Irreducibility: a nonzero submodule contains an eigenvector of $h$, hence some $v_k$.
Applying $e$ and $f$ then gives all basis vectors, since the coefficients $k + 1$ and $n - k + 1$ are nonzero for $0 \le k \le n$.
Tensor products decompose by the Clebsch–Gordan rule $V_m \otimes V_n \cong V_{m+n} \oplus V_{m+n-2} \oplus \dots \oplus V_{\abs{m-n}}$.
These are the derivatives of the representations of $SU(2)$ described in [[representation theory of SU(2)|9V6PRD1Z90]].

## Explanations

### L1 human

The Lie algebra $\mathfrak{sl}_2$ is the smallest simple Lie algebra, and its representations are the model for all others.
For each dimension $n + 1$ there is exactly one irreducible representation.
In a good basis, $h$ is diagonal with entries $n, n - 2, \dots, -n$, while $e$ moves up the list and $f$ moves down.
In physics this is the theory of angular momentum, where $V_n$ has spin $n/2$.
