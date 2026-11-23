---
tag: WHW13HJB3F
kind: example
name: The theory of groups is recursively axiomatizable
msc: ["03B25", "20A15"]
topics: [FBWW4J1XWG]
audience: grad
instance_of: [3ANXZC3BEG]
uses: [3ANXZC3BEG, RX9MB386C5, PPGD5KW8JC, TN9G24VABN, WQ1ZE255SF]
sources:
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Some undecidable theories
  - book: isbn:9780122384523
    locator: Section 2.6
---

## Example

The theory of groups is the simplest case of a [[recursively axiomatizable theory|3ANXZC3BEG]]: its axioms are three fixed sentences.
Let $L = \{ \cdot, {}^{-1}, e \}$ be the signature of groups, with a binary function symbol, a unary function symbol and a constant symbol.
Let $T_{\mathrm{grp}}$ be the set of the three axioms of the [[elementary theory of groups|RX9MB386C5]], which say that $\cdot$ is associative, that $e$ is a two-sided identity, and that $x^{-1}$ is a two-sided inverse of $x$.
$$\forall x \forall y \forall z \, ((x \cdot y) \cdot z = x \cdot (y \cdot z)), \quad \forall x \, (x \cdot e = x \land e \cdot x = x), \quad \forall x \, (x \cdot x^{-1} = e \land x^{-1} \cdot x = e)$$
We check the definition and then see what it gives and what it does not give.

1. The signature is finite.
   Code its three symbols, the logical symbols and the variables $v_0, v_1, \dots$ by natural numbers, so that each string has a Gödel number.
2. The axiom set $T_{\mathrm{grp}}$ has three members.
   A program decides membership by comparing a given string with the three axioms, symbol by symbol, so $T_{\mathrm{grp}}$ is a [[computable set|PPGD5KW8JC]].
3. So $T_{\mathrm{grp}}$ is a recursive axiomatization of itself.
4. A program can list all derivations from $T_{\mathrm{grp}}$ and print their last lines, so the set $\operatorname{Thm}(T_{\mathrm{grp}})$ is [[computably enumerable|TN9G24VABN]].
5. By [[Gödel's completeness theorem|WQ1ZE255SF]] and soundness, $\operatorname{Thm}(T_{\mathrm{grp}})$ is the set of sentences true in every group.
   So the sentences true in all groups can be listed by a machine.
6. The theory is not complete.
   Let $\sigma$ be $\forall x \forall y \, (x \cdot y = y \cdot x)$.
   The group $(\mathbb{Z}, +)$ satisfies $\sigma$.
7. In the symmetric group $S_3$, composing from right to left, $(1\,2)(1\,3) = (1\,3\,2)$ but $(1\,3)(1\,2) = (1\,2\,3)$.
   Check: in the first product, $1 \mapsto 3$ by $(1\,3)$ and then $3 \mapsto 3$ by $(1\,2)$, so $1 \mapsto 3$, as $(1\,3\,2)$ says.
   So $S_3$ does not satisfy $\sigma$.
8. By soundness, step 6 gives $T_{\mathrm{grp}} \nvdash \neg \sigma$, and step 7 gives $T_{\mathrm{grp}} \nvdash \sigma$.

## Remarks

A recursive axiomatization gives a list of the theorems, not a test for them.
The set $\operatorname{Thm}(T_{\mathrm{grp}})$ is in fact not decidable, by a theorem of Tarski that the [[elementary theory of groups|RX9MB386C5]] describes.
Since the theory is not complete, the result that complete recursively axiomatizable theories are decidable does not apply.

The picture changes when we change the axioms.
If we add $\sigma$, we get the abelian groups, still with finitely many axioms, and this theory is decidable by [[Szmielew's theorem|Y0753DF5R9]].
It is still not complete: $\exists x \, (\neg\, x = e \land x \cdot x = e)$ holds in $\mathbb{Z}/2\mathbb{Z}$ and fails in $(\mathbb{Z}, +)$.
If we add the infinitely many sentences $\tau_n = \forall x \, (x^n = e \to x = e)$ for $n \ge 2$, we get the torsion-free groups.
This axiom set is still decidable by a test of shape, but [[no finite set of axioms does the job|APF4KHZ976]].
If we try to axiomatize the torsion groups, no set of sentences at all works, by [[applications of first-order compactness|PES0S9XQZ5]].

## Explanations

### L1 human

The rules of a group are three short sentences.
A computer can check whether a given sentence is one of these three by comparing letters.
So a computer can check any proof written from these rules, and it can list every theorem about all groups, one by one.
But the list does not settle every question.
The sentence "any two elements commute" is true in some groups and false in others, so neither it nor its opposite is a theorem.

### L2 human

We decide membership in the torsion-free axioms $\{ \tau_n : n \ge 2 \}$.
Fix the spelling of powers with brackets to the left: $x^2 = (x \cdot x)$ and $x^{n+1} = (x^n \cdot x)$.
Take the following string.
$$\tau = \forall x \, (((x \cdot x) \cdot x) = e \to x = e)$$
The program checks that $\tau$ starts with $\forall x$ and that the rest has the form $(t = e \to x = e)$, here with $t = ((x \cdot x) \cdot x)$.
It counts the occurrences of $x$ in $t$, which gives $n = 3$, builds $x^3 = ((x \cdot x) \cdot x)$, and compares it with $t$.
They agree and $3 \ge 2$, so $\tau = \tau_3$ is an axiom.
For the string $\forall x \, ((x \cdot (x \cdot x)) = e \to x = e)$ the comparison fails, so the answer is "no", although in every group this string says the same thing as $\tau_3$.

The typical use is the first step of an incompleteness or undecidability proof: check that the axioms form a decidable set.
Watch out: finitely many axioms do not give a decidable theory, and the theory of groups shows it.
