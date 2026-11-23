---
tag: E6MQS2CJJT
kind: example
name: LTL and CTL as fragments of CTL*
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [Y4XZ94GRXV]
uses: [5MH8WSAWXT, 8S64VZ6A1S, 1DA0Y6KDF8]
sources:
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: section Syntax
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Example

We check that LTL and CTL are fragments of [[CTL*|5MH8WSAWXT]], with the same meaning.

1. An [[LTL formula|8S64VZ6A1S]] $\varphi$ uses $p$, $\neg$, $\wedge$, $X$ and $U$, so it is a CTL* path formula without path quantifiers.
2. On a path $\pi = s_0 s_1 \cdots$, the CTL* clauses for $\varphi$ are the LTL clauses read on the label word $L(s_0) L(s_1) \cdots$.
   This follows by induction on $\varphi$.
3. The LTL meaning at a state $s$ is "every path from $s$ satisfies $\varphi$".
   By clause 2 of the CTL* definition and $A = \neg E \neg$, this is exactly $M, s \models A\varphi$.
   So the LTL formula $\varphi$ corresponds to the CTL* state formula $A\varphi$.
4. A [[CTL formula|1DA0Y6KDF8]] is built with $EX$, $EG$ and $E[\,\cdot \, U \, \cdot\,]$ applied to state formulas.
   Read $EX\Phi$ as $E(X\Phi)$, $EG\Phi$ as $E(G\Phi)$ and $E[\Phi \, U \, \Psi]$ as $E(\Phi \, U \, \Psi)$, and each is a CTL* state formula.
5. The CTL clause for $EG\Phi$ asks for a path with $\Phi$ at every position.
   The CTL* clause for $E(G\Phi)$ asks the same, by clauses 3 and 6 of the definition with $G = \neg F \neg$.
6. The cases $EX$ and $EU$ are the same check.
   So every CTL formula has the same meaning as a CTL* formula.

Some formulas sit in both fragments up to equivalence.
The CTL formula $AG(\mathit{req} \to AF\,\mathit{grant})$ and the LTL formula $G(\mathit{req} \to F\,\mathit{grant})$, embedded as $A\,G(\mathit{req} \to F\,\mathit{grant})$, are equivalent CTL* formulas.

## Remarks

The two fragments are incomparable.
$AG\,EF\,p$ is in CTL but has no LTL equivalent, by [[the LTL non-example|RDRSPX5MM7]], and $A\,FGp$ comes from LTL but has no CTL equivalent, by [[the CTL non-example|NCE59DW7ZA]].
A property that both fragments can express need not look the same in both, as the response formula shows: CTL needs a quantifier in front of each temporal operator, and LTL needs only one in front of everything.

## Explanations

### L1 human

CTL* contains both older logics.
An LTL sentence becomes a CTL* sentence when you put "on every run" in front of it.
A CTL sentence is already a CTL* sentence, since each "some run" or "every run" comes with one time word.

### L2 human

To embed LTL, put $A$ in front of the whole formula.
To embed CTL, read each pair such as $AF$ as $A$ applied to $F$.
Then check the equivalence by unfolding both semantic clauses, as in steps 2, 3 and 5.
Watch out: moving $A$ inside an LTL formula is not always correct.
$AG\,AF\,p$ is equivalent to $A\,GF\,p$, but $AF\,AG\,p$ is strictly stronger than $A\,FG\,p$.
