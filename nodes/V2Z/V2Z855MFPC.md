---
tag: V2Z855MFPC
kind: statement
role: theorem
name: Strong normalization of simply typed lambda calculus
msc: [03B40, 03F05, 68N18]
uses: [2DP940895E, Y9B9CVY6SJ, GYMQHR3PXF, 7NNF74EYDX, A77FER1Q5H]
about: [2DP940895E]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting)
  - url: https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus
---

## Statement

Let $t$ be a term of the [[simply typed lambda calculus|2DP940895E]] with $\Gamma \vdash t : \tau$ for some context $\Gamma$ and type $\tau$.
Then $t$ is strongly normalizing for [[beta reduction|Y9B9CVY6SJ]]: there is no infinite sequence $t = t_0 \to_\beta t_1 \to_\beta t_2 \to_\beta \cdots$.

## Remarks

The standard proof is Tait's method of reducibility.
For each type $\tau$, one defines a set of reducible terms by induction on $\tau$.
At a base type they are the strongly normalizing terms, and at $\sigma \to \tau$ they are the terms that send reducible arguments to reducible results.
One shows that reducible terms are strongly normalizing, and then that every typed term is reducible, by induction on its typing derivation.
A direct induction on terms fails, because substitution can copy subterms and create new redexes; the reducibility sets give a stronger induction hypothesis.

The untyped term $\Omega = (\lambda x.\, x\, x)(\lambda x.\, x\, x)$ reduces to itself forever, and the theorem explains why no type can be given to it.
Strong normalization together with the [[Church–Rosser theorem|7NNF74EYDX]] gives each typed term a unique normal form, so equality of typed terms is decidable by comparing normal forms.
It also shows that some type has no closed term, which gives the consistency of the matching logic.

## Explanations

### L1 human

In the typed calculus every computation stops, whatever order of steps one takes.
Types act as a measure of size that keeps programs from looping.

### L2 human

The theorem is the [[normalization property|GYMQHR3PXF]] in its strongest form for the simply typed calculus.
Through the [[Curry–Howard correspondence|A77FER1Q5H]] it says that every proof in the implication fragment of intuitionistic natural deduction has a normal form.
This is a form of cut elimination.
The price is expressiveness: the typed calculus is not Turing complete, since every typed program halts.
The same reducibility method, with Girard's reducibility candidates, proves strong normalization for System F.
