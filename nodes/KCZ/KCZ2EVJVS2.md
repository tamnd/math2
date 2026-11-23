---
tag: KCZ2EVJVS2
kind: example
name: The first-order induction schema is not second-order induction
msc: ["03B16", "03C62"]
topics: [MDHDYV8QZW]
audience: grad
not_instance_of:
  - target: G6X7SZSNC5
    note: the first-order induction schema covers only definable sets, so it has non-standard models, while the second-order axiom is categorical
uses: [G6X7SZSNC5, 0QFT7Z76N5, 1NR3HAWG9D, 1QWN5CV4CG]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Peano arithmetic as first-order theory
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Expressive power
---

## Example

The first-order induction schema looks like the second-order induction axiom, but it is weaker.
It speaks only about the sets that formulas define, and a non-standard model can hide a set from every formula.
Let $L = \set{0, S, +, \cdot}$.
The first-order induction schema has one sentence for each first-order formula $\varphi(x, \bar{y})$ of $L$:
$$\forall \bar{y} \, \big( (\varphi(0, \bar{y}) \land \forall x \, (\varphi(x, \bar{y}) \to \varphi(S(x), \bar{y}))) \to \forall x \, \varphi(x, \bar{y}) \big).$$
First-order [[Peano arithmetic|0QFT7Z76N5]] $\mathrm{PA}$ is this schema together with $S(x) \neq 0$, $S(x) = S(y) \to x = y$ and the recursion equations for $+$ and $\cdot$.
The schema is not a sentence of [[second-order logic|G6X7SZSNC5]], and it does not do the work of the second-order induction axiom:
$$\text{(P3)} \ \forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big).$$
We give a model of $\mathrm{PA}$ in which (P3) is false in the full semantics.
Write $\underline{n}$ for the term $S(S(\cdots S(0)))$ with $n$ copies of $S$.

1. Add a new constant $c$, and let $T = \mathrm{PA} \cup \set{c \neq \underline{n} : n \in \mathbb{N}}$.
2. A finite subset of $T$ names only finitely many $n$.
   The structure $\mathbb{N}$, with $c$ read as a number larger than all of them, is a model of this subset.
3. By the [[compactness theorem|1NR3HAWG9D]] for first-order logic, $T$ has a model $\mathcal{M}$.
4. Let $B = \set{\underline{n}^{\mathcal{M}} : n \in \mathbb{N}}$.
   Then $0^{\mathcal{M}} = \underline{0}^{\mathcal{M}} \in B$, and $S^{\mathcal{M}}(\underline{n}^{\mathcal{M}}) = \underline{n + 1}^{\mathcal{M}} \in B$.
5. The element $c^{\mathcal{M}}$ is not in $B$, because $\mathcal{M}$ satisfies $c \neq \underline{n}$ for every $n$.
6. In the full semantics, $X$ ranges over all subsets of the domain.
   For $X = B$, the hypothesis of (P3) holds by step 4, and the conclusion fails by step 5.
   So $\mathcal{M} \not\models \text{(P3)}$.
7. Every instance of the schema holds in $\mathcal{M}$, since $\mathcal{M}$ is a model of $\mathrm{PA}$.
   If a formula $\varphi(x, \bar{b})$ with parameters $\bar{b}$ in $M$ defined $B$, its instance of the schema would give $B = M$.
   So no such formula defines $B$.

## Remarks

What fails is the range of the induction.
The schema speaks only about the sets that formulas define, and (P3) speaks about all subsets.
Step 7 is a fact about $\mathcal{M}$ that first-order logic cannot see: the standard part of a [[non-standard model of arithmetic|1QWN5CV4CG]] is never definable.
By the upward [[Löwenheim-Skolem theorem|484M0TZ1S7]], $\mathrm{PA}$ also has uncountable models, and none of them is isomorphic to $\mathbb{N}$.
In contrast, every full model of the second-order axioms is isomorphic to $\mathbb{N}$, as [[second-order Peano arithmetic is categorical|CKEG6B25AN]] shows.

## Explanations

### L1 human

The first-order rule of induction is a long list of rules, one for each property that we can write down.
The second-order rule is one rule about every set of numbers, written or not.
A strange model can obey every rule of the list and still contain extra numbers that we never reach from $0$ by adding $1$.
The set of ordinary numbers in that model has no description in the language, so no rule of the list can catch it.
The second-order rule catches it, so the strange model breaks the second-order rule.

### L2 human

We check step 2 for one finite subset.

1. Let $\Gamma_0 = \set{c \neq \underline{0}, c \neq \underline{3}, c \neq \underline{7}} \cup \Delta$, with $\Delta$ a finite set of axioms of $\mathrm{PA}$.
2. Read $c$ as $8$ in $\mathbb{N}$.
   Then $8 \neq 0$, $8 \neq 3$ and $8 \neq 7$.
3. The structure $\mathbb{N}$ satisfies every axiom of $\mathrm{PA}$, so it satisfies $\Delta$.
4. So $(\mathbb{N}, 8)$ is a model of $\Gamma_0$.

Check: $8$ is larger than the largest named number $7$, as step 2 asks.

We use this example to explain why first-order arithmetic has non-standard models, while second-order arithmetic with the full semantics has none.
The trap is to conclude that $\mathcal{M}$ fails some instance of the schema.
It satisfies all of them, and only the second-order axiom fails.
