---
tag: E2CBFNAVZY
kind: statement
role: theorem
name: Craig interpolation theorem
msc: [03C40, 03B10]
uses: [DKFGQTRYZE, 1HK0VYWTV7, WDVVEYD6AT]
about: [1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
same_as:
  wikidata: Q1052021
  wikipedia: Craig interpolation
---

## Statement

Let $\varphi$ and $\psi$ be first-order [[sentences|DKFGQTRYZE]] in a language with equality.
Assume that $\varphi \models \psi$, in the sense of [[logical consequence|1HK0VYWTV7]].
Then there is a first-order sentence $\theta$ with $\varphi \models \theta$ and $\theta \models \psi$.
Moreover, every relation, function and constant symbol of $\theta$ occurs in both $\varphi$ and $\psi$.

## Remarks

The sentence $\theta$ is called an interpolant.
One proof uses a cut-free [[sequent calculus|W72CA3R9MP]] and builds $\theta$ by induction on a cut-free proof of $\varphi \to \psi$.
Another proof is model-theoretic and uses the [[compactness theorem|1NR3HAWG9D]].
Example: $P(c) \land Q(c) \models P(c) \lor R(c)$, and $\theta = P(c)$ is an interpolant in the common symbols $P$ and $c$.
When $\varphi$ and $\psi$ share no symbols, $\theta$ is a sentence of pure equality, such as $\forall x \, (x = x)$ or its negation.
The propositional version holds too, with $\theta$ built from the common variables and the constants $\top$ and $\bot$.
William Craig proved the theorem in 1957.

## Explanations

### L1 human

Suppose one statement implies another.
The theorem says that there is a middle statement, using only the vocabulary the two have in common, that carries the implication.
So the reason for the implication can always be expressed in the shared language.

### L2 human

Craig interpolation is a basic structural property of first-order logic.
It implies the [[Beth definability theorem|RJBDSA2ETP]]: an implicitly definable relation is explicitly definable.
It is closely related to Robinson's joint consistency theorem.
Many other logics fail to have it, so it is also used to compare logics.
