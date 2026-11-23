---
tag: Q0MPGREG1B
kind: example
name: A natural deduction derivation of a quantifier swap
msc: ["03F03", "03B10"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [6KT3BJZ7D1]
uses: [PAQ4ZX2TX1]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: First and higher-order extensions
  - book: isbn:9781447145578
    locator: Chapter 3
---

## Example

We derive $\exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$ with no open assumptions, by the rules of [[natural deduction|PAQ4ZX2TX1]].
In words: if one $x$ is related to every $y$, then every $y$ is related to some $x$.
The derivation is the following tree.
$$\dfrac{\dfrac{\dfrac{[\exists x\, \forall y\, R(x,y)]^1 \qquad \dfrac{\dfrac{[\forall y\, R(u,y)]^2}{R(u,v)}\,{\forall}\mathrm{E}}{\exists x\, R(x,v)}\,{\exists}\mathrm{I}}{\exists x\, R(x,v)}\,{\exists}\mathrm{E}^2}{\forall y\, \exists x\, R(x,y)}\,{\forall}\mathrm{I}}{\exists x\, \forall y\, R(x,y) \to \forall y\, \exists x\, R(x,y)}\,{\to}\mathrm{I}^1$$
We check each node, from the leaves down.

1. $[\exists x\, \forall y\, R(x, y)]^1$ is an assumption with label 1.
2. $[\forall y\, R(u, y)]^2$ is an assumption with label 2.
   It has the form $\varphi[u/x]$ for $\varphi = \forall y\, R(x, y)$, and $u$ is substitutable for $x$ in $\varphi$.
3. $R(u, v)$ follows by ${\forall}\mathrm{E}$ from node 2, with the term $v$.
4. $\exists x\, R(x, v)$ follows by ${\exists}\mathrm{I}$ from node 3, since $R(x, v)[u/x] = R(u, v)$.
5. $\exists x\, R(x, v)$ follows by ${\exists}\mathrm{E}^2$ from nodes 1 and 4, and label 2 is discharged.
   The eigenvariable $u$ is not free in $\exists x\, \forall y\, R(x, y)$, not free in the conclusion $\exists x\, R(x, v)$, and not free in assumption 1.
6. $\forall y\, \exists x\, R(x, y)$ follows by ${\forall}\mathrm{I}$ from node 5, with eigenvariable $v$.
   The only open assumption is assumption 1, and $v$ is not free in it or in $\forall y\, \exists x\, R(x, y)$.
7. The implication follows by ${\to}\mathrm{I}^1$, which discharges label 1.

No assumption is open, so $\vdash_{\mathsf{ND}} \exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$.

## Remarks

### What the example shows

The derivation uses each quantifier rule once and no classical rule, so the formula is also a theorem of intuitionistic logic.
The two eigenvariables play opposite roles.
The variable $u$ names the one object that the assumption promises, and $v$ is an arbitrary object chosen after $u$.
The same formula has a [[closed tableau|NRJC4R4BGR]] and a sequent derivation in the [[sequent calculus|W72CA3R9MP]], which show the same fact in two other systems.

### The converse fails

The converse $\forall y\, \exists x\, R(x, y) \to \exists x\, \forall y\, R(x, y)$ has no derivation.
Read $R(x, y)$ as $y < x$ in the [[structure|983GZBQYT4]] $(\mathbb{N}, <)$.
Every $y$ has a larger $x$, so the antecedent is true, and no $x$ is larger than every $y$, so the consequent is false.
By [[soundness|4A84VHDTHV]], no derivation exists.
The natural try shows where it breaks.
It aims for $\forall y\, R(u, y)$ by ${\forall}\mathrm{I}$ on $v$, and it gets $R(u, v)$ from $\exists x\, R(x, v)$ by ${\exists}\mathrm{E}$ with eigenvariable $u$.
But then the conclusion $R(u, v)$ of ${\exists}\mathrm{E}$ contains $u$, which the condition forbids.

## Explanations

### L1 human

The formula says: "if one person loves everybody, then everybody is loved by somebody".
The derivation names the person $u$ who loves everybody.
It then takes any person $v$, notes that $u$ loves $v$, and concludes that somebody loves $v$.
Because $v$ was arbitrary, everybody is loved by somebody.
The other direction is false: everybody may have a mother without one mother for all.

### L2 human

To build the derivation, work from the goal upward.

1. The goal is an implication, so assume its antecedent and aim for $\forall y\, \exists x\, R(x, y)$.
2. The new goal is universal, so aim for $\exists x\, R(x, v)$ with a new variable $v$.
3. The assumption is existential, so start an ${\exists}\mathrm{E}$ with a new variable $u$ and the assumption $\forall y\, R(u, y)$.
4. From that assumption, ${\forall}\mathrm{E}$ and ${\exists}\mathrm{I}$ reach $\exists x\, R(x, v)$, which does not mention $u$.

The order of steps 2 and 3 does not matter here, because $v$ does not occur in assumption 2.
Watch out: if you take $u$ and $v$ to be the same variable, node 4 becomes $\exists x\, R(x, u)$, and ${\exists}\mathrm{E}$ would conclude a formula that contains its own eigenvariable.
