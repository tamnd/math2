---
tag: WZZ3VC4BVS
kind: example
name: The theory of a model of PA plus not Con(PA) is not true arithmetic
msc: ["03F30", "03F40"]
topics: [QHCRN4JVG0]
audience: grad
not_instance_of:
  - target: DX0KPMH4QZ
    note: "Th(M) is a complete consistent extension of PA, but it contains the false sentence not Con(PA), so it differs from TA."
uses: [DX0KPMH4QZ, HACXBCM7SS, 4PZM5GJTR5, WQ1ZE255SF, 655K8Y7VS8, 1QWN5CV4CG, EQR2AMD0GQ]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: Model-theoretic properties
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
---

## Example

We build a complete consistent theory in $L_A$ that contains $\mathsf{PA}$ and is not [[true arithmetic|DX0KPMH4QZ]].

1. $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent. Otherwise $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA})$, which the [[second incompleteness theorem|4PZM5GJTR5]] forbids, since $\mathsf{PA}$ is consistent.
2. By the [[completeness theorem|WQ1ZE255SF]], $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ has a model $M$.
3. Let $T = \mathrm{Th}(M)$, the set of sentences true in $M$. It is a [[complete theory|655K8Y7VS8]], consistent, and it contains every axiom of $\mathsf{PA}$.
4. $\neg \mathrm{Con}(\mathsf{PA}) \in T$, since $M \models \neg \mathrm{Con}(\mathsf{PA})$.
5. $\mathrm{Con}(\mathsf{PA}) \in \mathrm{TA}$, by [[this example|EQR2AMD0GQ]], so $\neg \mathrm{Con}(\mathsf{PA}) \notin \mathrm{TA}$.
6. By steps 4 and 5, $T \ne \mathrm{TA}$.

So completeness, consistency and the axioms of $\mathsf{PA}$ do not single out $\mathrm{TA}$.

## Remarks

The model $M$ is a [[nonstandard model|1QWN5CV4CG]]: it contains an element $p$ that $M$ believes codes a proof of $0 = S0$.
That element is nonstandard, since no standard number codes such a proof.
Not every nonstandard model of $\mathsf{PA}$ is of this kind: nonstandard models of $\mathrm{TA}$ exist by compactness, and their theory is $\mathrm{TA}$.
$\mathrm{TA}$ is the only complete extension of $\mathsf{PA}$ that is true in $\mathfrak{N}$, and it is the theory of exactly the models elementarily equivalent to $\mathfrak{N}$.
There are $2^{\aleph_0}$ complete consistent extensions of $\mathsf{PA}$ in $L_A$, and $\mathrm{TA}$ is one of them.

## Explanations

### L1 human

Gödel showed that Peano arithmetic cannot rule out the false statement "Peano arithmetic is inconsistent".
So there is a strange model of Peano arithmetic in which that statement holds.
The list of all statements true in that strange model is complete and consistent, like true arithmetic.
It differs from true arithmetic, because it contains a false statement about proofs.

### L2 human

We see what $M \models \neg \mathrm{Con}(\mathsf{PA})$ means.

1. $\neg \mathrm{Con}(\mathsf{PA})$ is $\exists p \, \mathrm{Prf}_{\mathsf{PA}}(p, \ulcorner 0 = S0 \urcorner)$, a $\Sigma_1$ sentence.
2. In $M$ some element $p$ satisfies $\mathrm{Prf}_{\mathsf{PA}}(p, \ulcorner 0 = S0 \urcorner)$.
3. If $p$ were a standard number $n$, then $\mathfrak{N}$ would satisfy the same $\Delta_0$ statement, because $\Delta_0$ formulas with standard parameters have the same truth value in $\mathfrak{N}$ and in $M$.
4. Then $n$ would code a real proof of $0 = S0$, which contradicts the consistency of $\mathsf{PA}$. So $p$ is nonstandard.

The typical use is to show that "complete and consistent extension of $\mathsf{PA}$" does not mean "true".
A trap is to think that $M$ proves a contradiction; $M$ is a structure, and the "proof" coded by $p$ has nonstandard length.
