---
tag: RA808VJGHJ
kind: example
name: The formula x:p → x:(p ∧ p) is not a theorem of the logic of proofs
msc: ["03B45", "03F45"]
topics: [CQM9SRN8PM]
audience: research
not_instance_of:
  - target: 5HKWCXEFG1
    note: the formula fails in a Fitting model, so it is not a law of the logic of proofs, although its forgetful projection is an S4 theorem
uses: [5HKWCXEFG1, 6BQ71KQ6QT]
sources:
  - book: isbn:9781108424912
    locator: "Artemov and Fitting, Justification Logic: Reasoning with Reasons"
---

## Example

A proof of "it rains" is a text that ends with "it rains", and the same text does not end with "it rains and it rains".
So a proof $x$ of $p$ need not be a proof of $p \wedge p$, and we show that [[the logic of proofs|5HKWCXEFG1]] does not prove $x{:}p \to x{:}(p \wedge p)$.

### Fitting models

A Fitting model for $\mathsf{LP}$ is a [[Kripke model|6BQ71KQ6QT]] $(W, R, V)$ with $R$ reflexive and transitive, and an evidence function $\mathcal{E}$ that maps a term and a formula to a set of worlds.
The evidence function must satisfy the following closure conditions.

- Application: $\mathcal{E}(s, \varphi \to \psi) \cap \mathcal{E}(t, \varphi) \subseteq \mathcal{E}(s \cdot t, \psi)$.
- Sum: $\mathcal{E}(s, \varphi) \cup \mathcal{E}(t, \varphi) \subseteq \mathcal{E}(s + t, \varphi)$.
- Checker: $\mathcal{E}(t, \varphi) \subseteq \mathcal{E}(!t, t{:}\varphi)$.
- Constants: $\mathcal{E}(c, A) = W$ for each constant $c$ and axiom $A$.
- Monotonicity: $w \in \mathcal{E}(t, \varphi)$ and $w R v$ give $v \in \mathcal{E}(t, \varphi)$.

Then $w \models t{:}\varphi$ when $w \in \mathcal{E}(t, \varphi)$ and $v \models \varphi$ for all $v$ with $w R v$.
$\mathsf{LP}$ is sound for these models.

### The countermodel

Take $W = \{w\}$, $R = \{(w, w)\}$ and $V(p) = \{w\}$.
Let $\mathcal{E}$ be the smallest evidence function that satisfies the closure conditions and has $w \in \mathcal{E}(x, p)$.

1. The smallest such function exists, since an intersection of evidence functions with the closure conditions has them too.
2. No closure condition has a proof variable as its output term, since the outputs are $s \cdot t$, $s + t$, $!t$ and constants.
3. So the only pair with the variable $x$ in $\mathcal{E}$ is $(x, p)$, and $\mathcal{E}(x, p \wedge p) = \emptyset$.
4. $w \in \mathcal{E}(x, p)$, and $p$ is true at $w$, the only successor of $w$, so $w \models x{:}p$.
5. $w \notin \mathcal{E}(x, p \wedge p)$, so $w \not\models x{:}(p \wedge p)$.
6. So $x{:}p \to x{:}(p \wedge p)$ fails at $w$, and by soundness it is not a theorem of $\mathsf{LP}$.

## Remarks

The forgetful projection $\square p \to \square(p \wedge p)$ is an $\mathsf{S4}$ theorem.
It has the realization $x{:}p \to (c \cdot x){:}(p \wedge p)$ with $c{:}(p \to (p \wedge p))$, which is an $\mathsf{LP}$ theorem.
So a modal theorem can have both provable and unprovable realizations, and the realization theorem only promises one provable one.
A justification has a fixed target, and a proof of $p$ is not automatically a proof of an equivalent formula.
In the same way, $x{:}p \to x{:}(p \vee q)$ and $x{:}(p \wedge q) \to x{:}(q \wedge p)$ fail.

## Explanations

### L1 human

A proof of "it rains" is a text that ends with "it rains".
The same text does not end with "it rains and it rains".
To get a proof of the longer sentence, we must add a line.
The logic of proofs keeps track of such added lines.

### L2 human

Choose the smallest evidence function that contains the pair you need.
Check that the formula to be refuted asks for evidence that the closure conditions do not create.
Then read off the failure at a single reflexive world.

The typical use of minimal evidence functions is to show that a formula of justification logic is not provable.
Watch out: one cannot set $\mathcal{E}(c \cdot x, p \wedge p) = \emptyset$ in the same way, because the application condition forces $w$ into it when $c$ is a constant for $p \to (p \wedge p)$.
