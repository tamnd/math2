---
tag: JP0RVCPF38
kind: example
name: Non-standard proofs in a model of PA + ¬Con(PA)
msc: ["03F40", "03C62"]
topics: [HXHHWY3328]
audience: grad
instance_of: [NB2BCZR40F]
uses: [NB2BCZR40F, 4PZM5GJTR5, WQ1ZE255SF, VM8TQ70CVJ, 1QWN5CV4CG, 4NBAX3VRQ7]
sources:
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: lead section
  - book: isbn:9780521857840
---

## Example

There is a model of Peano arithmetic in which the formula "some number codes a proof of $0 = S0$" is true, although $0 = S0$ is false there.
The witness is a number that no numeral names, and it is a proof only inside the model.

Let $\mathrm{Con}(\mathsf{PA}) := \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$ be the [[consistency statement|4NBAX3VRQ7]] of Peano arithmetic.
We show that $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ has a model $\mathcal{M}$, and that every witness in $\mathcal{M}$ of $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$ is non-standard.

1. The structure $\mathbb{N}$ is a model of $\mathsf{PA}$, so $\mathsf{PA}$ is [[consistent|VM8TQ70CVJ]].
2. By the [[second incompleteness theorem|4PZM5GJTR5]], $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$.
3. A theory $T$ does not prove $\varphi$ exactly when $T + \neg \varphi$ is consistent.
   So $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent.
4. By [[Gödel's completeness theorem|WQ1ZE255SF]], this theory has a model $\mathcal{M}$.
5. Since $\mathcal{M} \models \neg \mathrm{Con}(\mathsf{PA})$, it satisfies $\exists y \, \mathrm{Prf}_{\mathsf{PA}}(y, \ulcorner 0 = S0 \urcorner)$.
   Choose $b \in \mathcal{M}$ with $\mathcal{M} \models \mathrm{Prf}_{\mathsf{PA}}(b, \ulcorner 0 = S0 \urcorner)$.
6. Let $m \in \mathbb{N}$.
   By step 1, $m$ does not code a proof of $0 = S0$, so by representability $\mathsf{Q} \vdash \neg \mathrm{Prf}_{\mathsf{PA}}(\underline{m}, \ulcorner 0 = S0 \urcorner)$.
7. The model $\mathcal{M}$ satisfies the axioms of $\mathsf{Q}$, so $\mathcal{M} \models \neg \mathrm{Prf}_{\mathsf{PA}}(\underline{m}, \ulcorner 0 = S0 \urcorner)$.
   So $b$ is not the value of $\underline{m}$ in $\mathcal{M}$.
8. Step 7 holds for every $m \in \mathbb{N}$, so $b$ is a non-standard element, and $\mathcal{M}$ is a [[non-standard model|1QWN5CV4CG]] of $\mathsf{PA}$.

## Remarks

The element $b$ is a "proof" of $0 = S0$ only from inside $\mathcal{M}$.
Read through the coding, it is a sequence of non-standard length, and some of its lines are non-standard "formulas" that are not real formulas.
So $\mathcal{M} \models \mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$ while $\mathcal{M} \models \neg (0 = S0)$.
The [[provability predicate|NB2BCZR40F]] is faithful in $\mathbb{N}$, but not in every model of $\mathsf{PA}$.

Change the sentence and the picture changes.
For $0 = 0$, which has a real proof with some code $p$, the standard number $p$ is a witness in every model, because $\mathsf{Q}$ proves $\mathrm{Prf}_{\mathsf{PA}}(\underline{p}, \ulcorner 0 = 0 \urcorner)$.
So non-standard witnesses are needed only for sentences that have no real proof.

Watch out: $\mathcal{M}$ is not a "wrong" model.
It satisfies every axiom of $\mathsf{PA}$, and it differs from $\mathbb{N}$ only in which $\Sigma_1$ sentences it makes true.
This is also why the theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent but not [[ω-consistent|4S29X1GTV4]].

## Explanations

### L1 human

There are number systems that obey all the rules of Peano arithmetic and also contain "infinite" numbers beyond $0, 1, 2, \ldots$.
In one such system, the statement "there is a proof that $0 = 1$" is true.
The proof that it points to is an infinite number, which the system takes for a proof.
No ordinary number is such a proof, because Peano arithmetic is consistent.

### L2 human

The argument has four moves.
We start from the consistency of $\mathsf{PA}$, which holds because $\mathbb{N}$ is a model.
The second incompleteness theorem lets us add $\neg \mathrm{Con}(\mathsf{PA})$ without a contradiction, and the completeness theorem gives a model $\mathcal{M}$.
In $\mathcal{M}$ we pick a witness $b$ to the false claim of provability.
Representability then shows that $b$ differs from the value of every numeral $\underline{0}, \underline{1}, \underline{2}, \ldots$.
This is the standard way to see why $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ does not give $T \vdash \varphi$.
