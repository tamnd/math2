---
tag: MJEFQRRCS3
kind: definition
name: Dependent type
msc: [03B38, 68N15, 03F55]
defines: M6W6ZB4PPX
uses: [Q48KGV33AH, 2DP940895E]
sources:
  - url: https://en.wikipedia.org/wiki/Dependent_type
---

## Definition

Work in a [[type theory|Q48KGV33AH]] with judgments $\Gamma \vdash A\ \mathsf{type}$ and $\Gamma \vdash a : A$.
Here the context $\Gamma$ is a list of typed variables, in which each type may mention the earlier variables.
A *dependent type*, or *type family*, over a type $A$ is a type $B(x)$ with $\Gamma, x : A \vdash B(x)\ \mathsf{type}$, in which the variable $x$ may occur.
For each term $a$ with $\Gamma \vdash a : A$ it gives a type $B(a)$, obtained by substituting $a$ for $x$.
Such a family gives two type formers.

1. The *dependent function type* $\Pi_{x : A} B(x)$ has terms $\lambda x.\, b$ with $\Gamma, x : A \vdash b : B(x)$; applying $f : \Pi_{x : A} B(x)$ to $a : A$ gives $f\, a : B(a)$.
2. The *dependent pair type* $\Sigma_{x : A} B(x)$ has terms $(a, b)$ with $a : A$ and $b : B(a)$.

## Remarks

Example: let $\mathsf{Vec}(n)$ be the type of lists of natural numbers of length $n$, for $n : \N$.
It is a type family over $\N$, since for each $n$ it gives a type.
The function that builds a list of $n$ zeros has type $\Pi_{n : \N} \mathsf{Vec}(n)$: applied to $3$ it gives $(0, 0, 0) : \mathsf{Vec}(3)$, whose type depends on the argument.
The type $\Sigma_{n : \N} \mathsf{Vec}(n)$ is the type of lists of any length, each paired with its length.

Non-example: in the [[simply typed lambda calculus|2DP940895E]] a type cannot mention a term, so $\mathsf{Vec}(n)$ cannot be formed there.

If $B$ does not depend on $x$, then $\Pi_{x : A} B$ is the function type $A \to B$ and $\Sigma_{x : A} B$ is the product type $A \times B$.
Under Curry–Howard, a term of $\Pi_{x : A} B(x)$ is a proof of "for all $x$ in $A$, $B(x)$".
A term of $\Sigma_{x : A} B(x)$ is a proof of "there is $x$ in $A$ with $B(x)$" that names a witness.
