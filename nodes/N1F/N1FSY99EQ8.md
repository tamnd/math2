---
tag: N1FSY99EQ8
kind: example
name: The conjunction and disjunction fragment of classical logic is not algebraizable
msc: ["03G27"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: CESWST3NWA
    note: the fragment has no theorems, so no set of equivalence formulas exists
uses: [XADWEW9TNP, 09K9MWD2QQ, 0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
  - book: isbn:9781848902077
---

## Example

Let $\vdash$ be the fragment of [[classical logic|09K9MWD2QQ]] in $\land, \lor$: $\Gamma \vdash \varphi$ iff every two-valued valuation that makes all of $\Gamma$ true makes $\varphi$ true.

1. $\vdash$ has no theorems: the valuation that makes every variable false makes every formula in $\land, \lor$ false.
2. $x \nvdash y$ for distinct variables $x, y$: take $x$ true and $y$ false.
3. Suppose $\vdash$ is algebraizable with $K$, $E$ and $\Delta$, as in [[the definition|XADWEW9TNP]].
4. By (A2), $x \approx x \models_K E[\Delta(x, x)]$, so $\models_K E(\delta)$ for each $\delta \in \Delta(x, x)$. By (A1), each such $\delta$ is a theorem. So $\Delta$ is empty, by step 1.
5. Then (A2) says $\models_K x \approx y$, so every algebra in $K$ is trivial.
6. In trivial algebras every equation holds, so (A1) gives $x \vdash y$, against step 2.

So the fragment is not [[algebraizable|CESWST3NWA]].

## Remarks

1. The fragment is complete for [[distributive lattices|0HM0HQCK6N]]: $\Gamma \vdash \varphi$ iff $\bigwedge \Gamma_0 \le \varphi$ in every distributive lattice for some finite $\Gamma_0 \subseteq \Gamma$, with $\Gamma_0 \ne \emptyset$. So it has an algebraic semantics in a looser sense.
2. Steps 4 to 6 show more: the fragment is not even protoalgebraic, since no set $\Delta(x, y)$ satisfies $\vdash \Delta(x, x)$ and $x, \Delta(x, y) \vdash y$.
3. The argument applies to every logic with no theorems in which $x \nvdash y$, such as first-degree entailment.

## Explanations

### L1 human

The logic of "and" and "or" alone has no laws that hold with no premises.
Algebraizability needs some formulas that are always true, to express that two formulas are equal, so this logic cannot be algebraizable.

### L2 human

1. In the full classical logic, $p \leftrightarrow p$ is a theorem, and it expresses the equation $p \approx p$.
2. Without $\to$ and $\lnot$, no formula built from $p$ with $\land$ and $\lor$ is true when $p$ is false.
3. So there is no formula in two variables whose truth means "$p$ equals $q$" and that holds when $p$ and $q$ are equal and false.

The typical use: a logic with no theorems is never algebraizable, and this is the quickest test.
The trap: distributive lattices are the natural algebras of the fragment, but they form an algebraic semantics only in a weak sense, not an equivalent one.
