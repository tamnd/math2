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

Let $H$ be the [[Hilbert system|1MGMQX43B8]] for propositional logic with modus ponens (MP) as its only rule and with the axiom schemas
$$\begin{aligned} &\text{A1: } \varphi \to (\psi \to \varphi), \\ &\text{A2: } (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \\ &\text{A3: } (\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi). \end{aligned}$$
A derivation of $\varphi$ from a set $\Gamma$ is a finite list of formulas that ends in $\varphi$.
Each line is an instance of a schema, a member of $\Gamma$, or follows by MP from two earlier lines.
We write $\Gamma \vdash_H \varphi$ when such a derivation exists.

Here is a short one, from $\Gamma = \{ p \}$:
$$p, \qquad p \to (q \to p), \qquad q \to p.$$
The first line is a hypothesis, the second is A1, and the third follows by MP.
So $p \vdash_H q \to p$.

We check that $\vdash_H$ is a [[consequence relation|J78Y1M4GND]].

1. Reflexivity.
   If $\varphi \in \Gamma$, the one-line list $\varphi$ is a derivation of $\varphi$ from $\Gamma$.
2. Monotonicity.
   If $\Gamma \subseteq \Delta$, a derivation from $\Gamma$ is also a derivation from $\Delta$, since its hypothesis lines lie in $\Delta$.
3. Cut.
   Let $\Gamma \vdash_H \psi$ for every $\psi \in \Delta$, and let $D$ be a derivation of $\varphi$ from $\Gamma \cup \Delta$.
   Replace each line of $D$ that is a hypothesis $\psi \in \Delta \setminus \Gamma$ by a derivation of $\psi$ from $\Gamma$.
4. The new list still ends in $\varphi$.
   Each inserted line is justified as in its own derivation, and each MP line of $D$ still finds its premises earlier, because each replaced block ends in the same formula.
   So $\Gamma \vdash_H \varphi$.

Two more properties hold.

5. Finitarity.
   A derivation is finite, so it uses a finite set $\Gamma_0 \subseteq \Gamma$ of hypotheses, and it is a derivation from $\Gamma_0$.
6. Structurality.
   Apply a substitution $\sigma$ to every line of a derivation from $\Gamma$.
   Instances of a schema stay instances, hypotheses go into $\sigma[\Gamma]$, and MP steps stay MP steps, so the result is a derivation from $\sigma[\Gamma]$.

## Remarks

Steps 1 to 5 use only the shape of derivations, not the particular axioms.
So derivability in every [[formal system|439M8B4DY2]] of this kind is a finitary consequence relation.
Step 6 needs more: it holds because the axioms are given by schemas, and it fails for a system whose only axiom is the single formula $p$.
The proof of cut needs derivations of any length, and the relation "follows in one step of MP" is reflexive and monotone but fails cut.

By [[soundness|4A84VHDTHV]], $\Gamma \vdash_H \varphi$ implies $\Gamma \models \varphi$, and by the completeness theorem of propositional logic (in the sense of a proof system and a semantics) the converse holds.
So $\vdash_H$ equals [[classical propositional consequence|5X683DYC8S]], although the two relations are defined in very different ways.
In the abstract view, two Hilbert systems with the same consequence relation count as the same logic.

## Explanations

### L1 human

A Hilbert system says which formulas can be proved from given assumptions.
An assumption can be "proved" by writing it down.
Extra assumptions do not spoil a proof, since a proof does not have to use them.
If we have proofs of some lemmas, we can paste them into a longer proof that uses the lemmas.
These three facts are exactly the three rules of a consequence relation.

### L2 human

We paste derivations as in the proof of cut.
Take $\Gamma = \{ p, q \}$ and $\Delta = \{ q \to p \}$.
The short derivation above shows $\Gamma \vdash_H q \to p$, and its lines are $p$, $p \to (q \to p)$, $q \to p$.
A derivation $D$ of $p$ from $\Gamma \cup \Delta$ is $q$, $q \to p$, $p$, the last line by MP.
Replace the hypothesis line $q \to p$ of $D$ by the three lines of the short derivation:
$$q, \qquad p, \qquad p \to (q \to p), \qquad q \to p, \qquad p.$$
Each line is a hypothesis from $\Gamma$, an instance of A1, or follows by MP, so this is a derivation of $p$ from $\Gamma$ alone.

The typical use of cut is to reuse lemmas inside derivations, which is how long derivations are built in practice.
Watch out: the pasted derivation must itself use only hypotheses from $\Gamma$, or the result is not a derivation from $\Gamma$.
