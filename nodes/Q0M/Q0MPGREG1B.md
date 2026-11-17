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

We derive $\exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$ with no open assumptions, using the rules of the [[definition|PAQ4ZX2TX1]].
The derivation is the following tree.
$$\dfrac{\dfrac{\dfrac{[\exists x\, \forall y\, R(x,y)]^1 \qquad \dfrac{\dfrac{[\forall y\, R(u,y)]^2}{R(u,v)}\,{\forall}\mathrm{E}}{\exists x\, R(x,v)}\,{\exists}\mathrm{I}}{\exists x\, R(x,v)}\,{\exists}\mathrm{E}^2}{\forall y\, \exists x\, R(x,y)}\,{\forall}\mathrm{I}}{\exists x\, \forall y\, R(x,y) \to \forall y\, \exists x\, R(x,y)}\,{\to}\mathrm{I}^1$$
We check each step.

1. $[\exists x\, \forall y\, R(x, y)]^1$ is an assumption with label 1.
2. $[\forall y\, R(u, y)]^2$ is an assumption with label 2. It has the form $\varphi[u/x]$ for $\varphi = \forall y\, R(x, y)$, and $u$ is substitutable for $x$ in $\varphi$.
3. $R(u, v)$ follows by ${\forall}\mathrm{E}$ from step 2, with the term $t = v$.
4. $\exists x\, R(x, v)$ follows by ${\exists}\mathrm{I}$ from step 3: with $\varphi = R(x, v)$ and $t = u$ we have $\varphi[u/x] = R(u, v)$.
5. $\exists x\, R(x, v)$ follows by ${\exists}\mathrm{E}$ from steps 1 and 4, and it discharges label 2. The eigenvariable $u$ is not free in $\exists x\, \forall y\, R(x, y)$, not free in $\exists x\, R(x, v)$, and not free in assumption 1.
6. $\forall y\, \exists x\, R(x, y)$ follows by ${\forall}\mathrm{I}$ from step 5, with $\varphi = \exists x\, R(x, y)$ and eigenvariable $v$. The only open assumption is assumption 1, and $v$ is not free in it or in $\forall y\, \exists x\, R(x, y)$.
7. The implication follows by ${\to}\mathrm{I}$, which discharges label 1.
8. No assumption is open, so $\vdash_{\mathsf{ND}} \exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$.

## Remarks

The derivation uses no classical rule, so the formula is also a theorem of intuitionistic logic.
The converse $\forall y\, \exists x\, R(x, y) \to \exists x\, \forall y\, R(x, y)$ has no derivation.
Read $R(x, y)$ as $y < x$ in the structure $(\mathbb{N}, <)$.
Every $y$ has a larger $x$, so the antecedent is true, and no $x$ is larger than every $y$, so the consequent is false.
By [[soundness|4A84VHDTHV]], no derivation exists.
An attempt to derive the converse fails at ${\forall}\mathrm{I}$: the witness $u$ for $\exists x\, R(x, v)$ depends on $v$, and the condition on $u$ in ${\exists}\mathrm{E}$ blocks the step.
The same formula has a [[closed tableau|NRJC4R4BGR]], which shows the same fact in another system.

## Explanations

### L1 human

The formula says: "if one person loves everybody, then everybody is loved by somebody".
The derivation names the person $u$ who loves everybody.
It then takes any person $v$, notes that $u$ loves $v$, and concludes that somebody loves $v$.
Because $v$ was arbitrary, everybody is loved by somebody.

### L2 human

To build the derivation, work from the goal upward.

1. The goal is an implication, so assume its antecedent and aim for $\forall y\, \exists x\, R(x, y)$.
2. The new goal is universal, so aim for $\exists x\, R(x, v)$ with a new variable $v$.
3. The assumption is existential, so open the box of ${\exists}\mathrm{E}$ with a new variable $u$ and the assumption $\forall y\, R(u, y)$.
4. Inside the box, ${\forall}\mathrm{E}$ and ${\exists}\mathrm{I}$ reach $\exists x\, R(x, v)$, which does not mention $u$.

The order of steps 2 and 3 does not matter here, because $v$ does not occur in assumption 2.
A trap is to take $u$ and $v$ to be the same variable: then the result of ${\exists}\mathrm{E}$ would mention its own eigenvariable.
