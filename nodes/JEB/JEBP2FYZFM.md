---
tag: JEBP2FYZFM
kind: statement
role: theorem
name: Lomonosov's invariant subspace theorem
msc: [47A15, 47B07]
uses: [06GZ956657, M2NEP1K5AE, 0ACX5QT8TE, DCPFVVZZ54]
about: [0ACX5QT8TE, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Lomonosov%27s_invariant_subspace_theorem
same_as:
  wikidata: Q114425616
  wikipedia: Lomonosov's invariant subspace theorem
---

## Statement

Let $X$ be an infinite-dimensional complex [[Banach space|06GZ956657]] and let $K \colon X \to X$ be a nonzero [[compact operator|M2NEP1K5AE]].

1. There is a closed linear subspace $M$ of $X$ with $M \ne \set{0}$ and $M \ne X$ such that $A(M) \subseteq M$ for every bounded linear operator $A \colon X \to X$ with $AK = KA$.
2. In particular, every bounded linear operator $T \colon X \to X$ with $TK = KT$ has a nontrivial closed [[invariant subspace|0ACX5QT8TE]].

## Remarks

Proof idea: let $\mathcal{A}$ be the algebra of operators that commute with $K$, and suppose that it has no common nontrivial closed invariant subspace.
Then the orbit $\set{Ay : A \in \mathcal{A}}$ of every $y \ne 0$ is dense.
A compactness argument with finitely many $A_i \in \mathcal{A}$ and a partition of unity builds a continuous map of a closed ball into itself.
The [[Schauder fixed-point theorem|DCPFVVZZ54]] gives a fixed point.
The fixed point is an eigenvector, with eigenvalue $1$, of a compact operator $L$ that commutes with $K$.
So $K$ has an eigenvalue $\lambda$ on the finite-dimensional space $\ker(L - I)$.
Then $\ker(K - \lambda I)$ is a common invariant subspace, a contradiction.

The infinite dimension is needed in part 1.
On $\C^n$ with $n \ge 2$, the identity $K = I$ is compact and commutes with every operator, and the operators on $\C^n$ have no common nontrivial invariant subspace.

Example: the Volterra operator $(Vf)(x) = \int_0^x f(t)\,dt$ on $L^2[0,1]$ is compact, so every operator that commutes with $V$ has a nontrivial closed invariant subspace.

## Explanations

### L1 human

Compact operators are the operators that are closest to matrices.
The theorem says that a nonzero compact operator always shares a proper closed invariant subspace with every operator that commutes with it.
So any operator that commutes with a nonzero compact operator escapes the [[invariant subspace problem|5RF055GK4N]].

### L2 human

Before this theorem, the invariant subspace problem was known for compact operators and for polynomially compact operators, with long proofs.
Lomonosov's short fixed-point argument covers all of these at once, and in arbitrary complex Banach spaces.
It does not settle the general problem: there are operators on Hilbert space that commute with no nonzero compact operator.
