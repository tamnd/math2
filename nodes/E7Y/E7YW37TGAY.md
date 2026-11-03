---
tag: E7YW37TGAY
kind: definition
name: Type inference
msc: [68N15, 68N18, 03B40]
defines: 6NY149HDKS
uses: [AVVQEG0MRJ, 2DP940895E, NCDZ969V7X, RJJ9D0WF53]
sources:
  - url: https://en.wikipedia.org/wiki/Type_inference
---

## Definition

Let a [[type system|AVVQEG0MRJ]] be given by a typing relation $\Gamma \vdash t : \tau$ between contexts, terms and types.
*Type inference*, also called *type reconstruction*, is the following computational problem.
The input is a context $\Gamma$ and a term $t$, possibly without type annotations.
The task is to decide whether some type $\tau$ satisfies $\Gamma \vdash t : \tau$, and if so to output one such $\tau$.

Suppose that types may contain type variables.
A type $\tau$ of $t$ in $\Gamma$ is *principal* if every type of $t$ in $\Gamma$ is a [[substitution|NCDZ969V7X]] instance of $\tau$.
That is, it arises from $\tau$ by putting types in place of its type variables.

## Remarks

Example: in the Curry-style [[simply typed lambda calculus|2DP940895E]] with type variables, take $t = \lambda f.\, \lambda x.\, f\, x$ and the empty context.
Give $f$ the type $\alpha$ and $x$ the type $\beta$; the application $f\, x$ forces $\alpha = \beta \to \gamma$.
So $t$ has the principal type $(\beta \to \gamma) \to \beta \to \gamma$, and each other type, such as $(\mathsf{b} \to \mathsf{b}) \to \mathsf{b} \to \mathsf{b}$, is a substitution instance of it.
For this calculus the constraints are equations between types, and first-order [[unification|RJJ9D0WF53]] solves them, so inference is decidable.

Non-example: the term $\lambda x.\, x\, x$ has no type in the simply typed calculus.
Inference reaches the equation $\alpha = \alpha \to \beta$, which fails the occurs check of unification, and the algorithm reports that there is no type.

Type inference differs from *type checking*, which is the problem of deciding $\Gamma \vdash t : \tau$ for a given $\tau$.
For the Curry-style System F, J. B. Wells proved that both problems are undecidable.
