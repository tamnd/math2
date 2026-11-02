---
tag: THX29SKKPB
kind: definition
name: Spectral triple
msc: [58B34, 46L87]
defines: FTQMQR3YS7
uses: [HM2HHE3J51, BMDG4JQPEH, KRJX5RA0PW, 0NEGN5CRSC, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_triple
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] and let $B(H)$ be the [[algebra of bounded operators|BMDG4JQPEH]] on $H$.
Let $A$ be a unital $*$-subalgebra of $B(H)$.
Let $D$ be a densely defined [[unbounded|KRJX5RA0PW]] [[self-adjoint operator|0NEGN5CRSC]] on $H$ with domain $\operatorname{dom} D$.
The triple $(A, H, D)$ is a *spectral triple* if:

1. for every $a \in A$, the operator $a$ maps $\operatorname{dom} D$ into itself, and the commutator $[D, a] = Da - aD$ on $\operatorname{dom} D$ extends to a bounded operator on $H$;
2. the resolvent $(D - \lambda I)^{-1}$ is a [[compact operator|M2NEP1K5AE]] for one, and then for every, $\lambda \in \C \setminus \R$.

## Remarks

Example: let $A = C^\infty(S^1)$ act on $H = L^2(S^1)$ by multiplication and let $D = -i \, d/d\theta$ on the Sobolev space of functions with square-integrable derivative.
The functions $e_n(\theta) = e^{in\theta}$, $n \in \Z$, form an orthonormal basis of eigenvectors with $D e_n = n e_n$, so $(D - i)^{-1}$ has eigenvalues $1/(n - i) \to 0$ and is compact.
For $f \in A$ the product rule gives $[D, f] = -i f'$, which is multiplication by a bounded function.
More generally, smooth functions on a compact Riemannian spin manifold, acting on square-integrable spinors, with the [[Dirac operator|3DXGJTEQZH]], form a spectral triple.

Non-example: if $H$ is infinite-dimensional and $D = 0$, every commutator is $0$, so clause 1 holds.
But $(D - i I)^{-1} = i I$ is not compact, so clause 2 fails.

Often $A$ is a dense $*$-subalgebra of a C*-algebra, and $A$ acts on $H$ through a faithful $*$-representation.
A spectral triple is called even if there is a self-adjoint unitary $\gamma$ on $H$ that commutes with $A$ and anticommutes with $D$.
For two states $\varphi$ and $\psi$ of the norm closure of $A$, Connes' distance formula is
$$d(\varphi, \psi) = \sup \set{ \abs{\varphi(a) - \psi(a)} : a \in A, \ \|[D, a]\| \le 1 }.$$
It recovers the geodesic distance when $\varphi$ and $\psi$ are evaluations at two points of a manifold.
