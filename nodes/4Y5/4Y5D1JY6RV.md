---
tag: 4Y5D1JY6RV
kind: example
name: Propositional logic as an institution
msc: ["03B22", "03C95", "03B05"]
topics: [H8QZY0RZXZ]
audience: grad
instance_of: [RQXV7PM2WT]
uses: [RQXV7PM2WT, 09K9MWD2QQ, 28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Institution_(computer_science)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Propositional_calculus
    locator: lead section
---

## Example

We define the institution of classical [[propositional logic|09K9MWD2QQ]], an instance of the [[abstract logical systems|RQXV7PM2WT]] given by institutions.

- Signatures: a signature is a set $\Sigma$ of propositional variables, and a signature morphism $\sigma \colon \Sigma \to \Sigma'$ is any function.
- Sentences: $\mathrm{Sen}(\Sigma)$ is the set of formulas built from the variables in $\Sigma$ with $\neg$ and $\wedge$. For $\sigma \colon \Sigma \to \Sigma'$, $\mathrm{Sen}(\sigma)$ replaces each variable $p$ by $\sigma(p)$.
- Models: $\mathrm{Mod}(\Sigma)$ is the set of valuations $v \colon \Sigma \to \set{0, 1}$, seen as a category with only identity morphisms. For $\sigma \colon \Sigma \to \Sigma'$, the reduct of $v' \in \mathrm{Mod}(\Sigma')$ is $v'|_\sigma = v' \circ \sigma$.
- Satisfaction: $v \models_\Sigma \varphi$ when the truth tables give $\varphi$ the value $1$ under $v$.

We check the conditions.

1. $\mathrm{Sen}$ is a [[functor|28NQ0KRHD3]]: replacing by the identity changes nothing, and replacing by $\sigma$ and then by $\tau$ is replacing by $\tau \circ \sigma$.
2. $\mathrm{Mod}$ is a functor on $\mathbf{Sign}^{\mathrm{op}}$: $v'|_{\mathrm{id}} = v'$, and for $\sigma \colon \Sigma \to \Sigma'$ and $\tau \colon \Sigma' \to \Sigma''$ we have $v''|_{\tau \circ \sigma} = v'' \circ \tau \circ \sigma = (v''|_\tau)|_\sigma$.
3. Satisfaction condition: for every $\varphi \in \mathrm{Sen}(\Sigma)$ and $v' \in \mathrm{Mod}(\Sigma')$, the value of $\sigma(\varphi)$ under $v'$ equals the value of $\varphi$ under $v' \circ \sigma$. We prove this by induction on $\varphi$.
4. For a variable $p$, both values are $v'(\sigma(p))$.
5. For $\neg \psi$, $\sigma(\neg \psi) = \neg \sigma(\psi)$, and both values are $1$ minus the common value for $\psi$ given by the induction hypothesis.
6. For $\psi \wedge \chi$, $\sigma(\psi \wedge \chi) = \sigma(\psi) \wedge \sigma(\chi)$, and both values are the minimum of the common values for $\psi$ and $\chi$.
7. So $v' \models_{\Sigma'} \sigma(\varphi) \iff v'|_\sigma \models_\Sigma \varphi$.

A computation with a non-injective morphism.

8. Let $\Sigma = \set{p, q}$, $\Sigma' = \set{r}$, and $\sigma(p) = \sigma(q) = r$.
9. Let $\varphi = p \wedge \neg q$. Then $\sigma(\varphi) = r \wedge \neg r$.
10. For $v'(r) = 1$, the reduct is $p \mapsto 1, q \mapsto 1$; $\varphi$ gets $1 \wedge 0 = 0$, and $r \wedge \neg r$ gets $0$.
11. For $v'(r) = 0$, the reduct is $p \mapsto 0, q \mapsto 0$; $\varphi$ gets $0$, and $r \wedge \neg r$ gets $0$. The condition holds in both cases.
12. Yet $\varphi$ is satisfiable over $\Sigma$, by $p \mapsto 1, q \mapsto 0$, while $\sigma(\varphi)$ is not. The valuation $p \mapsto 1, q \mapsto 0$ is not the reduct of any $\Sigma'$-model.

## Remarks

Step 12 shows that translation does not reflect consequence: $\set{p} \not\models_\Sigma q$, but $\set{\sigma(p)} \models_{\Sigma'} \sigma(q)$, since both are $r$.
Translation along an injective morphism reflects consequence, because then every $\Sigma$-valuation is a reduct: extend it arbitrarily to the variables outside the image.
For $\Sigma = \emptyset$, $\mathrm{Sen}(\Sigma)$ is empty, since every formula contains a variable; adding the constants $\top$ and $\bot$ changes this.
The same pattern, with Kripke models in place of valuations, gives institutions for intuitionistic and modal propositional logic.

## Explanations

### L1 human

Renaming the letters of a formula should not change whether it is true, provided the truth values move with the letters.
If $p$ is renamed $r$, then "$\neg p$ is true when $p$ is false" becomes "$\neg r$ is true when $r$ is false".
The satisfaction condition says exactly this.
When two letters are merged into one, some formulas change their meaning: "$p$ and not $q$" becomes "$r$ and not $r$", which is never true.

### L2 human

We check the satisfaction condition for a renaming that adds a new letter.

1. Let $\Sigma = \set{p, q}$, $\Sigma' = \set{p, q, s}$, and let $\sigma$ be the inclusion.
2. Let $\varphi = \neg (p \wedge q)$, so $\sigma(\varphi) = \neg (p \wedge q)$, the same formula over the larger signature.
3. Let $v'$ give $p \mapsto 1$, $q \mapsto 1$, $s \mapsto 0$. Then $\sigma(\varphi)$ gets $\neg 1 = 0$.
4. The reduct $v'|_\sigma$ forgets $s$, so it gives $p \mapsto 1$, $q \mapsto 1$, and $\varphi$ gets $0$. Both sides agree.

The typical use of this institution is as the simplest test case for a general construction.
A trap is to let $\mathrm{Mod}(\sigma)$ go from $\Sigma$-models to $\Sigma'$-models; a $\Sigma$-valuation does not say what to do with $s$.
