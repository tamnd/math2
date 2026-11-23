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

The induction schema turns each formula into one induction axiom.
Let $L$ be a first-order language that contains the constant symbol $0$ and the unary function symbol $S$, for example the [[language of arithmetic|329ZG1Z0G5]].
Let $\varphi$ be a [[formula|2CHENV4DCC]] of $L$ with free variables among $x, y_1, \ldots, y_k$.
Write $\varphi(t)$ for the result of [[substituting|NCDZ969V7X]] the term $t$ for the free occurrences of $x$ in $\varphi$.
The induction axiom for $\varphi$ with respect to $x$ is the sentence
$$\mathrm{Ind}_\varphi := \forall y_1 \cdots \forall y_k\, \Bigl( \bigl( \varphi(0) \land \forall x\,(\varphi(x) \to \varphi(S x)) \bigr) \to \forall x\, \varphi(x) \Bigr).$$
The induction schema of $L$ is the set of all sentences $\mathrm{Ind}_\varphi$, for all formulas $\varphi$ of $L$ and all choices of the variable $x$.
For a set $\Gamma$ of formulas, the $\Gamma$-induction schema is the set of $\mathrm{Ind}_\varphi$ with $\varphi \in \Gamma$.

## Notation

The variable $x$ is the induction variable, and $y_1, \ldots, y_k$ are the parameters.
Some books write $\varphi(x')$ for $\varphi(S x)$.
Some write the instance as a formula with free parameters instead of its universal closure, which gives the same theory, since a theory proves a formula exactly when it proves its closure.

## Remarks

Each part of the definition has a job.
The premise $\varphi(0)$ is the base, and $\forall x\,(\varphi(x) \to \varphi(S x))$ is the step.
The outer quantifiers $\forall y_1 \cdots \forall y_k$ make the axiom a sentence, and they let the property depend on fixed outside values.

The substitutions cause no capture of variables.
The term $0$ has no variables, and the term $S x$ goes only into free occurrences of $x$, which by definition do not lie in the scope of a quantifier on $x$.

For a small instance, take $\varphi(x) := S x \ne x$, with no parameters.
The axiom is
$$\bigl(S 0 \ne 0 \land \forall x\,(S x \ne x \to S S x \ne S x)\bigr) \to \forall x\,(S x \ne x),$$
and [[this example|855J8368AM]] proves both premises.

A sentence of the form $\bigl(\varphi(0) \land \forall x\,(\varphi(x) \to \varphi(S S x))\bigr) \to \forall x\, \varphi(x)$ is not an instance, because its step jumps by two.
It is also false in the standard model for $\varphi(x) := \exists y\,(x = y + y)$, since $0$ is even and evenness passes from $x$ to $x + 2$, but $1$ is odd.

The schema is a decidable set of sentences, since an algorithm can check whether a sentence has the displayed form.
In the language of arithmetic, the schema together with the axioms of Robinson arithmetic gives [[Peano arithmetic|Z8YDBW2857]].
The [[concept page|1QD0KDDGYJ]] discusses the schema and its fragments.

## Explanations

### L1 human

The definition is a recipe that turns each formula into one induction axiom.
Take a property written as a formula.
The axiom says: if $0$ has the property, and the property passes from each number to the next, then every number has it.

### L2 human

We form the instance for $\varphi(x, y) := y \le x \lor x < y$, with parameter $y$.
The base $\varphi(0, y)$ is $y \le 0 \lor 0 < y$, and the shifted formula $\varphi(S x, y)$ is $y \le S x \lor S x < y$.
So the axiom is
$$\forall y\,\bigl(((y \le 0 \lor 0 < y) \land \forall x\,(\varphi(x, y) \to \varphi(S x, y))) \to \forall x\,(y \le x \lor x < y)\bigr).$$
This instance is the main step in the proof in $\mathsf{PA}$ that $<$ is a linear order.
The typical use of the definition is to write down the exact instance before using it in a proof.
The trap is to substitute for $y$ instead of $x$, since the schema fixes which variable is the induction variable.
