---
tag: HZCFTQDRA5
kind: statement
role: theorem
name: Soundness of a Hilbert system for propositional logic
msc: ["03B05"]
topics: [H8QZY0RZXZ]
audience: ug2
about: [4A84VHDTHV, 1MGMQX43B8, 09K9MWD2QQ]
uses: [4A84VHDTHV, 1MGMQX43B8, 05006AJ7DZ, 05RSK4Q657, 0Y0MQYST0M, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Soundness
    locator: lead section
  - book: isbn:9781482237726
  - book: isbn:9781447145578
history:
  notes: "Post proved in 1921 that the theorems of the propositional calculus of Principia Mathematica are exactly the tautologies; one half of this result is soundness."
---

## Statement

The formulas are built from the variables $p_1, p_2, p_3, \ldots$ with the connectives $\lnot$ and $\to$.
Let $\mathsf{H}$ be the [[Hilbert system|1MGMQX43B8]] with the three axiom schemas
$$\text{(A1) } \varphi \to (\psi \to \varphi), \qquad \text{(A2) } (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \qquad \text{(A3) } (\lnot\varphi \to \lnot\psi) \to (\psi \to \varphi),$$
where $\varphi$, $\psi$, $\chi$ range over all formulas, and with [[modus ponens|0Y0MQYST0M]] as the only rule.
Let $\Gamma$ be a set of formulas.
A derivation from $\Gamma$ is a finite list $\varphi_1, \ldots, \varphi_n$ in which each $\varphi_i$ is an axiom, a member of $\Gamma$, or follows by modus ponens from $\varphi_j$ and $\varphi_k = (\varphi_j \to \varphi_i)$ with $j, k < i$.
We write $\Gamma \vdash_{\mathsf{H}} \varphi$ when some derivation from $\Gamma$ ends with $\varphi$.
A valuation is a function $v$ from the variables to $\set{\mathsf{T}, \mathsf{F}}$, extended to all formulas by the [[truth tables|05RSK4Q657]] of $\lnot$ and $\to$.
We write $\Gamma \models \varphi$ when every valuation that makes all members of $\Gamma$ true makes $\varphi$ true.

**Theorem.** For every set $\Gamma$ of formulas and every formula $\varphi$, if $\Gamma \vdash_{\mathsf{H}} \varphi$, then $\Gamma \models \varphi$.

In particular, for $\Gamma = \varnothing$: every theorem of $\mathsf{H}$ is a [[tautology|05006AJ7DZ]].

## Remarks

### Why each hypothesis is needed

- The axioms must be tautologies. If the schema $(\varphi \to \psi) \to (\psi \to \varphi)$ is added, its instance $(p_1 \to p_2) \to (p_2 \to p_1)$ becomes a theorem, and the valuation $p_1 = \mathsf{F}$, $p_2 = \mathsf{T}$ makes it false.
- The rule must keep truth. [[A system with the rule of affirming the consequent|5WQDFMR91G]] derives $p_1$ from $\set{p_1 \to p_2, \; p_2}$, and the valuation $p_1 = \mathsf{F}$, $p_2 = \mathsf{T}$ refutes this.
- The semantics must be the two-valued one. In the three-element Heyting algebra $\set{0, \tfrac12, 1}$, the instance of A3 with $\varphi = p_1$, $\psi = p_2$ takes the value $\tfrac12$ when $p_1 = \tfrac12$ and $p_2 = 1$. So $\mathsf{H}$ is not sound for that semantics.

### Consequences

- $\mathsf{H}$ is [[consistent|VM8TQ70CVJ]]: a formula and its negation are never both tautologies, so they are never both theorems.
- $\mathsf{H}$ is [[Post consistent|WK2P0E82B4]]: the valuation with $p_1 = \mathsf{F}$ shows that $p_1$ is not a tautology, so it is not a theorem.
- Unprovability is shown by one valuation. For example $(p_1 \to p_2) \to p_1$ is not a theorem, since $p_1 = \mathsf{F}$, $p_2 = \mathsf{F}$ makes it false.
- A satisfiable set $\Gamma$ is consistent; the [[satisfiable set of three formulas|WTRZG7SQM2]] is an instance.

### Converse

The converse, "if $\Gamma \models \varphi$, then $\Gamma \vdash_{\mathsf{H}} \varphi$", is also true, but it is a different and harder theorem.
It is the completeness of [[the propositional calculus|JDK63589SA]] for truth tables, and its strong form uses the [[compactness theorem|1NR3HAWG9D]] of propositional logic.
"Complete" here means complete for a semantics, not the completeness of a theory.

### Generalizations

- The same proof works for every Hilbert system whose axioms are tautologies and whose rules keep truth under each valuation.
- For first-order logic the same induction on derivations shows that every derivable formula is true in every [[structure|983GZBQYT4]], under every assignment that makes the hypotheses true. The quantifier rules need their side conditions.
- For intuitionistic or modal logic, the valuations are replaced by Heyting algebras, Kripke models or frames, and the axioms are checked there.

## History

Emil Post proved in 1921 that the theorems of the propositional calculus of *Principia Mathematica* are exactly the tautologies.
The half "every theorem is a tautology" is the soundness of that system, and the other half is its completeness for truth tables.

## Explanations

### L1 human

A proof in this system starts from some fixed laws and from some assumptions, and it uses one rule: from "$A$" and "if $A$ then $B$", conclude "$B$".
The theorem says that this kind of proof never goes wrong.
Each fixed law is true however we choose true and false for the letters.
The rule turns true statements into true statements.
So, step by step, every line of a proof from true assumptions is true.

### L2 human

We check one derivation line by line against the valuation $v$ with $p_1 = \mathsf{T}$, $p_2 = \mathsf{F}$, for $\Gamma = \set{p_1}$.

1. $p_1$ is a member of $\Gamma$, and $v(p_1) = \mathsf{T}$.
2. $p_1 \to (p_2 \to p_1)$ is an instance of A1. Its value is $\mathsf{T} \to (\mathsf{F} \to \mathsf{T}) = \mathsf{T} \to \mathsf{T} = \mathsf{T}$.
3. Modus ponens on lines 1 and 2 gives $p_2 \to p_1$. Its value is $\mathsf{F} \to \mathsf{T} = \mathsf{T}$.

Every line is true under $v$, as the theorem predicts, and the same holds for every valuation with $p_1 = \mathsf{T}$.
The typical use is the reverse direction: to show $\Gamma \nvdash_{\mathsf{H}} \varphi$, find one valuation that makes $\Gamma$ true and $\varphi$ false.
A trap is to check only the formulas of $\Gamma$ and the last line; soundness is a statement about every line, and the induction needs it.

### L3 human

The proof is an induction on derivations, and it only needs two facts: the axioms are valid and the rule keeps truth.
In algebraic terms a valuation is a homomorphism from the formula algebra to the two-element Boolean algebra, and soundness says that every such homomorphism sends each theorem to $1$.
The same pattern proves soundness of [[natural deduction|6KT3BJZ7D1]], of the [[sequent calculus|W72CA3R9MP]], and of first-order Hilbert systems, which together with [[Gödel's completeness theorem|WQ1ZE255SF]] gives the equality of $\vdash$ and $\models$.
