---
tag: G55NMADJ6G
kind: definition
name: Induction schema
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
defines: 1QD0KDDGYJ
uses: [329ZG1Z0G5, 2CHENV4DCC, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Peano arithmetic as first-order theory
  - book: isbn:9780521857840
---

## Definition

Let $L$ be a first-order language that contains the constant symbol $0$ and the unary function symbol $S$, for example the [[language of arithmetic|329ZG1Z0G5]].
Let $\varphi$ be a [[formula|2CHENV4DCC]] of $L$ with free variables among $x, y_1, \ldots, y_k$.
Write $\varphi(t)$ for the result of [[substituting|NCDZ969V7X]] the term $t$ for the free occurrences of $x$ in $\varphi$.
The induction axiom for $\varphi$ with respect to $x$ is the sentence
$$\mathrm{Ind}_\varphi := \forall y_1 \cdots \forall y_k\, \Bigl( \bigl( \varphi(0) \land \forall x\,(\varphi(x) \to \varphi(S x)) \bigr) \to \forall x\, \varphi(x) \Bigr).$$
The induction schema of $L$ is the set of all sentences $\mathrm{Ind}_\varphi$, for all formulas $\varphi$ of $L$ and all choices of the variable $x$.
For a set $\Gamma$ of formulas, the $\Gamma$-induction schema $\mathrm{I}\Gamma$ is the set of $\mathrm{Ind}_\varphi$ with $\varphi \in \Gamma$.

## Notation

The variable $x$ is the induction variable, and $y_1, \ldots, y_k$ are the parameters.
Some books write $\varphi(x')$ for $\varphi(S x)$, and some write the instance as a formula with free parameters instead of its universal closure.

## Remarks

The substitutions $\varphi(0)$ and $\varphi(S x)$ cause no capture of variables: $0$ has no variables, and the free occurrences of $x$ in $\varphi$ do not lie in the scope of a quantifier on $x$.
The schema is a decidable set of sentences, since one can check by an algorithm whether a sentence has the displayed form.
In the language of arithmetic, the schema together with the axioms of Robinson arithmetic gives [[Peano arithmetic|Z8YDBW2857]].
The [[concept page|1QD0KDDGYJ]] discusses the schema and its fragments.

## Explanations

### L1 human

The definition gives a recipe that turns each formula into one induction axiom.
Take a property written as a formula; the axiom says: if $0$ has the property, and the property passes from each number to the next, then every number has it.

### L2 human

We form the instance for $\varphi(x, y) := y \le x \lor x < y$, with parameter $y$.

1. $\varphi(0)$ is $y \le 0 \lor 0 < y$.
2. $\varphi(S x)$ is $y \le S x \lor S x < y$.
3. So $\mathrm{Ind}_\varphi$ is $\forall y\,\bigl(((y \le 0 \lor 0 < y) \land \forall x\,(\varphi(x) \to \varphi(S x))) \to \forall x\,(y \le x \lor x < y)\bigr)$.
4. This instance is the main step in the proof in $\mathsf{PA}$ that $<$ is a linear order.

The typical use of the definition is to write down the exact instance before using it in a proof.
A trap is to substitute for $y$ instead of $x$: the schema fixes which variable is the induction variable.
