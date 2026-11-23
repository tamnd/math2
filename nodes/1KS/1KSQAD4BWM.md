---
tag: 1KSQAD4BWM
kind: example
name: ZFC proves Con(PA)
msc: ["03F40", "03E30"]
topics: [HXHHWY3328]
audience: grad
instance_of: [4NBAX3VRQ7]
uses: [4NBAX3VRQ7, 0HE5WDQ9FJ, MPSCREYC3M, 4A84VHDTHV, WP27CABPA4]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
---

## Example

We outline a proof in [[ZFC|0HE5WDQ9FJ]] of the [[consistency statement|4NBAX3VRQ7]] $\mathrm{Con}(\mathsf{PA})$, read in $\mathsf{ZFC}$ through the set $\omega$ of natural numbers.
The plan is to build a model of $\mathsf{PA}$ as a set and to apply soundness.
Each step is a theorem of $\mathsf{ZFC}$.

1. The set $\omega$ exists by the axiom of infinity.
   With the successor map $n \mapsto n \cup \{n\}$, and with addition and multiplication defined by recursion on $\omega$, it is a structure $\mathcal{N}$ for the language $\{0, S, +, \cdot\}$.
2. Satisfaction in a structure that is a set is defined by recursion on the codes of formulas.
   So "$\mathcal{N} \models \varphi[b]$", for a code $\varphi$ and an assignment $b$, is a single formula of set theory.
3. $\mathcal{N}$ satisfies the axioms of $\mathsf{Q}$, by the recursion equations of step 1.
4. Let $\varphi(x, \vec{y})$ be the code of any formula and $\vec{b}$ any parameters.
   One use of separation, applied to the satisfaction formula of step 2, gives the set $A = \{ n \in \omega : \mathcal{N} \models \varphi[n, \vec{b}] \}$.
   If $A$ contains $0$ and is closed under successor, then $A = \omega$, by induction on $\omega$.
   So $\mathcal{N}$ satisfies every induction axiom, for all codes at once.
5. $\mathsf{ZFC}$ proves the [[soundness theorem|4A84VHDTHV]] for $\mathcal{N}$: every formula that has a proof from axioms true in $\mathcal{N}$ is true in $\mathcal{N}$.
   The proof is an induction on the length of the proof.
6. $\mathcal{N} \not\models 0 = S0$, since $0 = \varnothing$ and $S0 = \{\varnothing\}$ are different sets.
7. By steps 3 to 6, no proof of $0 = S0$ from the axioms of [[Peano arithmetic|MPSCREYC3M]] exists.
   This is $\mathrm{Con}(\mathsf{PA})$, read through $\omega$.

## Remarks

The work is done in step 4.
There, one instance of separation and one induction on $\omega$ handle every induction axiom of $\mathsf{PA}$ at the same time.
$\mathsf{PA}$ cannot imitate this, because it has no formula for truth in its own standard model, by [[Tarski's undefinability theorem|YRV6SYK2BY]].

The same pattern, "build a model and apply soundness", proves consistency statements in many places.
It also shows how the second incompleteness theorem limits $\mathsf{ZFC}$.
If $\mathsf{ZFC}$ is consistent, it does not prove $\mathrm{Con}(\mathsf{ZFC})$, so it cannot build a set model of itself in this way.

Much less than $\mathsf{ZFC}$ suffices for $\mathrm{Con}(\mathsf{PA})$.
Second-order arithmetic proves it by the same argument with sets of numbers in place of sets.
[[Gentzen's consistency proof|QPV0HNP22S]] proves it in primitive recursive arithmetic with induction along $\varepsilon_0$.

## Explanations

### L1 human

Set theory can build the whole set of natural numbers as one object.
It can then check that every axiom of arithmetic holds in this object, and that the rules of proof never lead from true statements to false ones.
Since $0 = 1$ is false in this object, no proof from the axioms can end with $0 = 1$.
So set theory proves that arithmetic is consistent.

### L2 human

The proof has three moves.
First, $\mathsf{ZFC}$ builds the model $\omega$ and a truth definition for it.
Second, it checks every axiom of $\mathsf{PA}$ in the model, and the induction axioms all at once by one induction on $\omega$.
Third, it applies soundness, and $0 \ne S0$ in the model gives $\mathrm{Con}(\mathsf{PA})$.
The typical use is the method "one theory proves the consistency of another by building a model of it".
Watch out: the method needs a truth definition for the model, and that is why $\mathsf{PA}$ cannot run it about its own standard model.
