---
tag: DE0GD8BM4M
kind: example
name: Uniform substitution is admissible but not derivable
msc: ["03B05", "03F03"]
topics: [H8QZY0RZXZ]
audience: ug2
instance_of: [QPD3X471Q1]
uses: [QPD3X471Q1, 1MGMQX43B8, 4A84VHDTHV, WQ1ZE255SF]
sources:
  - url: https://en.wikipedia.org/wiki/Admissible_rule
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Rule_of_inference
    locator: lead section
  - book: isbn:9781447145578
---

## Example

We work in the [[Hilbert system|1MGMQX43B8]] $H$ for propositional logic with the axiom schemas A1 to A3 and the rule modus ponens (MP).
A substitution $\sigma$ assigns to each propositional variable $p$ a formula $\sigma(p)$, and $\sigma(\varphi)$ is the result of replacing every variable $p$ in $\varphi$ by $\sigma(p)$, all at the same time.
Uniform substitution is the [[rule of inference|QPD3X471Q1]] "from $\varphi$ infer $\sigma(\varphi)$", for every formula $\varphi$ and every substitution $\sigma$.

Uniform substitution is admissible in $H$: if $\vdash_H \varphi$, then $\vdash_H \sigma(\varphi)$.

1. Let $\chi_1, \dots, \chi_m$ be a derivation of $\varphi$ in $H$ without hypotheses.
2. Substitution commutes with the connectives: $\sigma(\alpha \to \beta) = \sigma(\alpha) \to \sigma(\beta)$ and $\sigma(\neg \alpha) = \neg \sigma(\alpha)$.
3. If $\chi_i$ is the instance of A1 with $\alpha, \beta$ for $\varphi, \psi$, then by step 2, $\sigma(\chi_i)$ is the instance of A1 with $\sigma(\alpha), \sigma(\beta)$. The same holds for A2 and A3.
4. If $\chi_i$ follows by MP from $\chi_j$ and $\chi_k = \chi_j \to \chi_i$, then $\sigma(\chi_k) = \sigma(\chi_j) \to \sigma(\chi_i)$, so $\sigma(\chi_i)$ follows by MP from $\sigma(\chi_j)$ and $\sigma(\chi_k)$.
5. So $\sigma(\chi_1), \dots, \sigma(\chi_m)$ is a derivation of $\sigma(\varphi)$ in $H$.

Uniform substitution is not derivable in $H$.

6. Take the instance with $\varphi = p$ and $\sigma(p) = q$, that is, "from $p$ infer $q$".
7. Suppose $\set{p} \vdash_H q$. By [[soundness|4A84VHDTHV]] of $H$, every valuation that makes $p$ true makes $q$ true.
8. The valuation with $v(p)$ true and $v(q)$ false makes $p$ true and $q$ false, a contradiction.
9. So $q$ has no derivation from the hypothesis $p$, and the rule is not derivable.

## Remarks

The two parts fit together because $p$ is not a theorem of $H$, so the instance of step 6 never applies to a theorem.
Admissibility speaks only about theorems, while derivability speaks about arbitrary hypotheses.

Classical propositional logic is structurally complete: every admissible rule that is closed under substitution is derivable.
Proof: suppose the rule $\varphi_1, \dots, \varphi_n / \psi$ is not derivable.
By the completeness theorem, some valuation $v$ makes all $\varphi_i$ true and $\psi$ false.
Fix a variable $q$ and let $\tau(p) = q \to q$ if $v(p)$ is true and $\tau(p) = \neg (q \to q)$ if $v(p)$ is false.
By induction on formulas, every valuation gives $\tau(\alpha)$ the value $v(\alpha)$, for every formula $\alpha$.
So each $\tau(\varphi_i)$ is a tautology, hence a theorem, while $\tau(\psi)$ is false under every valuation, hence not a theorem.
Since the rule is closed under substitution, $\tau(\varphi_1), \dots, \tau(\varphi_n) / \tau(\psi)$ is an instance, and the rule is not admissible.
Uniform substitution is not closed under substitution in this sense, so it is no counterexample.

Intuitionistic propositional logic is not structurally complete.
The Kreisel-Putnam rule $\neg p \to (q \vee r) \,/\, (\neg p \to q) \vee (\neg p \to r)$ is admissible there, but the corresponding implication is not an intuitionistic theorem, so the rule is not derivable.

## Explanations

### L1 human

Suppose a system proves "$p$ implies $p$".
Then it also proves "$q$ implies $q$", and "(rain) implies (rain)", because the proof did not depend on what $p$ means.
So renaming letters in a proved formula gives another proved formula; this is why substitution is admissible.
But from the mere assumption "$p$" we cannot conclude "$q$": the two letters may stand for unrelated statements.
So substitution is not a rule that may be used under assumptions.

### L2 human

We substitute in a concrete derivation, the five-line derivation of $p \to p$, with $\sigma(p) = q \wedge r$ written as a formula of $\neg, \to$ by $\neg (q \to \neg r)$.

1. The lines of the original derivation are instances of A2 and A1 and two uses of MP, all with $p$ and $p \to p$ as parts.
2. Applying $\sigma$ to each line replaces every $p$ by $\neg (q \to \neg r)$.
3. Each new line is again an instance of the same schema, or follows by MP from the same two lines.
4. The last line is $\neg (q \to \neg r) \to \neg (q \to \neg r)$, a theorem.

The typical use of the admissibility of substitution is to treat proved formulas as schemas.
A trap is to apply substitution to a hypothesis inside a derivation, which turns the hypothesis $p$ into the unrelated $q$.
