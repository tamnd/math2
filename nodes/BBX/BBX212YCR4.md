---
tag: BBX212YCR4
kind: proof
name: Proof that Peano arithmetic is not finitely axiomatizable by reflection
msc: ["03F30", "03F40"]
topics: [QHCRN4JVG0]
audience: grad
proves: M5WNB181T7
uses: [HACXBCM7SS, T70PYM1F36, ME9J33BFNC, 4PZM5GJTR5, 4A84VHDTHV, 0J0XBKG64S]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_principle
    locator: For arithmetic
  - book: isbn:9780521857840
---

## Proof

We put a finite axiomatization inside one fragment $\mathsf{I}\Sigma_n$ and show that this fragment would prove its own consistency.
We cite two lemmas without proof.
Lemma 1 says that $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{I}\Sigma_n)$ for each $n \ge 1$; its proof uses a truth formula for $\Sigma_n$ formulas inside $\mathsf{PA}$.
Lemma 2 is the [[second incompleteness theorem|4PZM5GJTR5]]: if $T$ is consistent, recursively axiomatized and proves every axiom of $\mathsf{PA}$, then $T$ does not prove $\mathrm{Con}(T)$.
We argue by [[contradiction|0J0XBKG64S]].

1. Suppose a finite set $F$ of sentences has the same theorems as [[Peano arithmetic|HACXBCM7SS]].
2. Each $\sigma \in F$ is a theorem of $\mathsf{PA}$, so it has a proof from finitely many axioms of $\mathsf{PA}$.
   Since $F$ is finite, one finite set $A$ of axioms of $\mathsf{PA}$ proves every $\sigma \in F$.
3. Induction for $\varphi$ is equivalent to induction for a prenex form of $\varphi$, by the [[prenex normal form theorem|ME9J33BFNC]].
   A prenex formula is $\Sigma_k$ for some $k$, after a vacuous quantifier in front if needed.
4. Let $n \ge 1$ be at least each such $k$ for the induction axioms in $A$.
   Then the [[fragment|T70PYM1F36]] $\mathsf{I}\Sigma_n$ proves all axioms in $A$.
5. By steps 2 and 4, $\mathsf{I}\Sigma_n$ proves every $\sigma \in F$, so it proves every theorem of $\mathsf{PA}$.
6. By Lemma 1, $\mathrm{Con}(\mathsf{I}\Sigma_n)$ is a theorem of $\mathsf{PA}$, so by step 5 it is a theorem of $\mathsf{I}\Sigma_n$.
7. $\mathsf{I}\Sigma_n$ is consistent, because its axioms are true in $\mathfrak{N}$ and [[soundness|4A84VHDTHV]] applies.
8. $\mathsf{I}\Sigma_n$ is recursively axiomatized, and by step 5 it proves every axiom of $\mathsf{PA}$.
9. By Lemma 2 with steps 7 and 8, $\mathsf{I}\Sigma_n$ does not prove $\mathrm{Con}(\mathsf{I}\Sigma_n)$.
   This contradicts step 6.

So no such $F$ exists, and $\mathsf{PA}$ is not finitely axiomatizable.

## Idea

A finite set of axioms can mention only finitely many induction axioms, so it fits inside one fragment $\mathsf{I}\Sigma_n$.
$\mathsf{PA}$ can see that each fragment is consistent, because it has a truth formula for $\Sigma_n$ formulas.
If the fragment proved all of $\mathsf{PA}$, it would see its own consistency, and Gödel's second theorem forbids that.
The whole proof is this clash between finite size and self-reflection.

## Variants

One can use $\mathsf{I}\Sigma_{n+1} \vdash \mathrm{Con}(\mathsf{I}\Sigma_n)$ in place of Lemma 1.
Then step 6 goes through $\mathsf{I}\Sigma_{n+1}$, which is part of $\mathsf{PA}$.

The same argument shows that $\mathsf{PA}$ is essentially reflexive: for every sentence $\varphi$, $\mathsf{PA} + \varphi$ proves the consistency of $\mathsf{I}\Sigma_n + \varphi$.
Repeating the proof with $\mathsf{PA} + \varphi$ in place of $\mathsf{PA}$ shows that no consistent extension of $\mathsf{PA}$ in $L_A$ is finitely axiomatizable.

A model-theoretic route builds, for each $n$, a model of $\mathsf{I}\Sigma_n$ in which some axiom of $\mathsf{I}\Sigma_{n+1}$ fails.
Then no $\mathsf{I}\Sigma_n$ proves all of $\mathsf{PA}$, and step 5 fails directly, with no appeal to consistency statements.
