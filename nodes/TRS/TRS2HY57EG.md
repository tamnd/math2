---
tag: TRS2HY57EG
kind: statement
role: theorem
name: Craig interpolation for propositional logic
aliases: [propositional-interpolation-theorem]
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
about: [1HK0VYWTV7]
uses: [TT7WT5HPN9, H31CS3HK5P, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Proof of Craig's interpolation theorem
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: lead section
---

## Statement

When one formula implies another, a third formula that uses only their shared variables sits between them.

Let $\varphi$ and $\psi$ be [[propositional formulas|TT7WT5HPN9]], in a language with the constants $\top$ and $\bot$.
Write $\operatorname{var}(\chi)$ for the set of variables that occur in a formula $\chi$.
Assume that $\varphi \models \psi$, in the sense of [[logical consequence|1HK0VYWTV7]].
Then there is a formula $\theta$ with the following three properties.

1. $\varphi \models \theta$.
2. $\theta \models \psi$.
3. $\operatorname{var}(\theta) \subseteq \operatorname{var}(\varphi) \cap \operatorname{var}(\psi)$.

Such a formula $\theta$ is an interpolant of $\varphi$ and $\psi$.
Let $\vec q$ list the variables of $\varphi$ that do not occur in $\psi$.
One interpolant is $\bigvee_{c} \varphi[c/\vec q\,]$, where $c$ runs over all ways to replace each $q_i$ by $\top$ or $\bot$; the [[proof|NV2BJQJGB4]] checks this.

## Remarks

### Why each hypothesis is needed

The hypothesis $\varphi \models \psi$ is needed: properties 1 and 2 together give $\varphi \models \psi$.
For example $p$ and $q$ have no interpolant, since $p \not\models q$.

The constants $\top$ and $\bot$ are needed when $\varphi$ and $\psi$ share no variable.
For example $p \land \neg p \models q$, and an interpolant may contain no variable at all.
Without constants there is no formula without variables, and so no interpolant.
With them, $\theta = \bot$ works.
In a language without constants, the theorem needs an extra case.
When no variable is shared, the conclusion is that $\varphi$ is unsatisfiable or $\psi$ is a tautology.

### What it gives you

If $\varphi \models \psi$ and the two formulas share no variable, then $\varphi$ is unsatisfiable or $\psi$ is a [[tautology|05006AJ7DZ]].
The interpolant has no variables, so it is equivalent to $\top$ or to $\bot$.
If it is $\bot$, then $\varphi \models \bot$, and if it is $\top$, then $\top \models \psi$.

The interpolant $\bigvee_c \varphi[c/\vec q\,]$ is the strongest one: it implies every other interpolant.
Dually, let $\vec r$ list the variables of $\psi$ that do not occur in $\varphi$; then $\bigwedge_c \psi[c/\vec r\,]$ is the weakest interpolant.

Beth definability for propositional logic follows.
Suppose that $\varphi(p, \vec s)$ and $\varphi(p', \vec s)$ together imply $p \leftrightarrow p'$, with $p'$ a new variable.
Then $\varphi(p, \vec s) \land p \models \varphi(p', \vec s) \to p'$, and an interpolant is a formula $\theta(\vec s)$ in the variables $\vec s$ alone.
The two halves give $\varphi(p, \vec s) \models p \to \theta$ and, after renaming $p'$ to $p$, $\varphi(p, \vec s) \models \theta \to p$.
So $p$ is defined by $\theta$ wherever $\varphi$ holds.

### The converse

The converse holds: if a formula $\theta$ has properties 1 and 2, then $\varphi \models \psi$, because logical consequence is transitive.
So $\varphi \models \psi$ if and only if an interpolant exists.

### Generalizations

The [[Craig interpolation theorem|E2CBFNAVZY]] for first-order logic replaces variables by relation, function and constant symbols; see also the [[interpolation theorem|6P3KG89G4J]].
Lyndon's form adds polarity: each variable that occurs positively in $\theta$ occurs positively in $\varphi$ and in $\psi$, and the same holds for negative occurrences.
Interpolation also holds for intuitionistic propositional logic and for the modal logic K, with proofs through cut-free sequent calculi.

## History

William Craig proved the interpolation theorem for first-order logic in 1957.
Roger Lyndon proved the stronger form with polarity in 1959.
The propositional case is the special case of formulas without quantifiers.

## Explanations

### L1 human

Suppose one rule about some letters forces another rule about other letters.
The theorem says that the reason can be stated using only the letters that the two rules share.
For example, "p and q" forces "q or r".
The shared letter is q, and the middle rule "q" carries the implication: "p and q" gives "q", and "q" gives "q or r".

### L2 human

We find an interpolant for $\varphi = p \land (p \to q)$ and $\psi = q \lor r$.
First, $\varphi \models \psi$: if $\varphi$ is true, then $p$ and $p \to q$ are true, so $q$ is true, and so $q \lor r$ is true.
The shared variables are $\operatorname{var}(\varphi) \cap \operatorname{var}(\psi) = \{ q \}$, and the variable $p$ occurs only in $\varphi$.
We replace $p$ by each constant:
$$\varphi[\top/p] = \top \land (\top \to q) \equiv q, \qquad \varphi[\bot/p] = \bot \land (\bot \to q) \equiv \bot.$$
The interpolant is $\varphi[\top/p] \lor \varphi[\bot/p]$, which is equivalent to $q \lor \bot$, that is, to $q$.
Check: $\varphi \models q$ by the first computation, and $q \models q \lor r$, and the only variable of $q$ is shared.

The typical use is to explain an implication in the common language of two systems, as in model checking.
Watch out: do not forget property 3.
The formula $\varphi$ itself has properties 1 and 2, but it mentions $p$, so it is not an interpolant.

### L3 human

Interpolation says that the consequence relation splits along the shared vocabulary.
The strongest consequence of $\varphi$ without the variables $\vec q$ is the formula $\exists \vec q\, \varphi$.
In propositional logic this quantifier is the finite disjunction of the statement.
Algebraically, interpolation corresponds to the amalgamation property of the class of Boolean algebras.
The same link between interpolation and amalgamation holds for many varieties of algebras of logic.
The interpolant built by elimination of variables can be exponentially longer than $\varphi$.
In [[propositional proof complexity|CBAF7J051K]], feasible interpolation extracts small interpolants from short refutations, which ties lower bounds for proof systems to lower bounds for circuits.
In first-order logic the corresponding statement is the [[Craig interpolation theorem|E2CBFNAVZY]].
Its proofs use cut elimination in the [[sequent calculus|W72CA3R9MP]] or the [[compactness theorem|1NR3HAWG9D]].
It implies Beth's definability theorem and Robinson's joint consistency theorem.
