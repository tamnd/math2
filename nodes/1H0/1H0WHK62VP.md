---
tag: 1H0WHK62VP
kind: example
name: Derivability in a Hilbert system is a consequence relation
msc: ["03B22", "03F03"]
topics: [H8QZY0RZXZ]
audience: ug3
instance_of: [FCXHSC6Z4R]
uses: [J78Y1M4GND, 1MGMQX43B8, 439M8B4DY2, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Consequence_relation
    locator: lead section
  - book: isbn:9781482237726
---

## Example

Let $H$ be the [[Hilbert system|1MGMQX43B8]] for propositional logic with the axiom schemas A1 to A3 and the rule modus ponens (MP).

- A1: $\varphi \to (\psi \to \varphi)$.
- A2: $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$.
- A3: $(\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi)$.

A derivation of $\varphi$ from a set $\Gamma$ of formulas is a finite sequence of formulas that ends in $\varphi$.
Each line is an instance of an axiom schema, a member of $\Gamma$, or follows by MP from two earlier lines.
Put $\Gamma \vdash_H \varphi$ when such a derivation exists.
We check that $\vdash_H$ is a [[consequence relation|J78Y1M4GND]].

1. Reflexivity. If $\varphi \in \Gamma$, the one-line sequence $\varphi$ is a derivation of $\varphi$ from $\Gamma$.
2. Monotonicity. If $\Gamma \subseteq \Delta$, every derivation from $\Gamma$ is a derivation from $\Delta$, since its hypothesis lines lie in $\Delta$.
3. Cut. Let $\Gamma \vdash_H \psi$ for every $\psi \in \Delta$, and let $D$ be a derivation of $\varphi$ from $\Gamma \cup \Delta$.
4. In $D$, replace each line that is a hypothesis $\psi \in \Delta \setminus \Gamma$ by a derivation of $\psi$ from $\Gamma$.
5. The new sequence still ends in $\varphi$. Every line of an inserted derivation is justified as before, and every MP line of $D$ still finds its two premises earlier, since each replaced line now ends in the same formula.
6. So $\Gamma \vdash_H \varphi$.

Two more properties hold.

7. Finitarity. A derivation is finite, so it uses a finite set $\Gamma_0 \subseteq \Gamma$ of hypotheses, and it is a derivation from $\Gamma_0$.
8. Structurality. Applying a substitution $\sigma$ to every line of a derivation from $\Gamma$ gives a derivation from $\sigma[\Gamma]$: instances of a schema stay instances, hypotheses go into $\sigma[\Gamma]$, and MP steps stay MP steps.

## Remarks

Steps 1 to 7 use only the shape of derivations, not the particular axioms, so derivability in every [[formal system|439M8B4DY2]] of this kind is a finitary consequence relation.
Step 8 needs more: it holds because the axioms are given by schemas, and it fails for a system with the single axiom $p$.
The proof of cut needs derivations of arbitrary length: the relation "follows in one step of MP" is reflexive and monotone but fails cut.
By [[soundness|4A84VHDTHV]], $\Gamma \vdash_H \varphi$ implies $\Gamma \models \varphi$, and by the completeness theorem of propositional logic the converse holds.
So $\vdash_H$ is equal to [[classical propositional consequence|5X683DYC8S]], although the two relations are defined in different ways.
Two Hilbert systems with the same consequence relation have the same derivable rules, so they count as the same logic in the abstract view.

## Explanations

### L1 human

A Hilbert system says which formulas can be proved from given assumptions.
An assumption can be "proved" by writing it down.
Extra assumptions do not spoil a proof, since a proof does not have to use them.
If we have proofs of some lemmas, we can paste them into a longer proof that uses the lemmas.
These three facts are exactly the three rules of a consequence relation.

### L2 human

We paste derivations as in the proof of cut.

1. Derivation $D_1$ of $q \to p$ from $\set{p}$: the lines $p$, $p \to (q \to p)$, $q \to p$.
2. Derivation $D$ of $p$ from $\set{q, q \to p}$: the lines $q$, $q \to p$, $p$, the last by MP.
3. Take $\Gamma = \set{p, q}$ and $\Delta = \set{q \to p}$. Replace the hypothesis line $q \to p$ of $D$ by $D_1$.
4. The result is $q$, $p$, $p \to (q \to p)$, $q \to p$, $p$. Each line is a hypothesis from $\Gamma$, an instance of A1, or follows by MP.

The typical use of cut is to reuse lemmas inside derivations, which is how long derivations are built in practice.
A trap is to paste a derivation that uses a hypothesis outside $\Gamma$; the pasted derivation must itself be a derivation from $\Gamma$.
