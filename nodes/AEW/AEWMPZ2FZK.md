---
tag: AEWMPZ2FZK
kind: example
name: A CTL* formula in neither LTL nor CTL
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [Y4XZ94GRXV]
uses: [5MH8WSAWXT, RDRSPX5MM7, NCE59DW7ZA, 1DA0Y6KDF8]
sources:
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: section Syntax
---

## Example

Let $\theta = A\,FGp \vee AG\,EF\,q$, a state formula of [[CTL*|5MH8WSAWXT]] with two different atoms $p$ and $q$.
We show that $\theta$ is equivalent to no LTL formula and to no CTL formula.
For CTL we cite one fact: no CTL formula is equivalent to $A\,FGp$, by Emerson and Halpern, as discussed in [[the CTL non-example|NCE59DW7ZA]].

1. To rule out LTL, take the structures $M_1$ and $M_2$ of [[the LTL non-example|RDRSPX5MM7]], with $q$ in place of $p$, and with $p$ false everywhere.
2. Every path has $p$ false forever, so $A\,FGp$ fails at $s_0$ in both structures.
   So at $s_0$ the formula $\theta$ has the value of $AG\,EF\,q$.
3. By that non-example, $AG\,EF\,q$ holds at $s_0$ in $M_1$ and fails at $s_0$ in $M_2$.
4. The two structures have the same set of label words from $s_0$, so every LTL formula has the same value at $s_0$ in both.
   Hence no LTL formula is equivalent to $\theta$.
5. To rule out CTL, suppose that a [[CTL formula|1DA0Y6KDF8]] $\psi$ is equivalent to $\theta$, and let $\psi'$ be $\psi$ with $q$ replaced by $\bot$.
6. Let $M^-$ be $M$ with $q$ removed from every label.
   By induction on $\psi$, $M, s \models \psi'$ if and only if $M^-, s \models \psi$.
7. In $M^-$ no state has $q$, so $EF\,q$ is false everywhere.
   Since $AG\,\chi$ at $s$ implies $\chi$ at $s$, the formula $AG\,EF\,q$ is false at every state of $M^-$.
8. So in $M^-$ the formula $\theta$, and hence $\psi$, has the value of $A\,FGp$.
   The value of $A\,FGp$ is the same in $M$ and in $M^-$, since $q$ does not occur in it.
9. Hence $M, s \models \psi'$ if and only if $M, s \models A\,FGp$, for all $M$ and $s$.
   This contradicts the cited fact, so no such $\psi$ exists.

## Remarks

The example shows that CTL* is strictly more expressive than LTL and CTL together: a disjunction of one formula from each side already escapes both.

The two atoms must be different.
With one atom, $A\,FGp \vee AG\,EF\,p$ is equivalent to the CTL formula $AG\,EF\,p$.
Why does the first disjunct add nothing?
If $AG\,EF\,p$ fails, some reachable state $t$ reaches no $p$-state, so a path through $t$ has $\neg p$ forever after $t$, and $A\,FGp$ fails too.
So $A\,FGp$ implies $AG\,EF\,p$, and the disjunction collapses.

## Explanations

### L1 human

Take one sentence that only LTL can say and one that only CTL can say, about different basic facts.
Join them with "or".
The result is a CTL* sentence that neither smaller logic can say.

### L2 human

The method has two halves.
To rule out LTL, make the LTL disjunct false in a pair of structures with the same runs, and let the CTL disjunct tell the pair apart.
To rule out CTL, set $q$ false everywhere, so that the CTL disjunct disappears and a CTL formula for $\theta$ would become a CTL formula for $A\,FGp$.
Watch out: the disjunction with the same atom $p$ twice collapses to a CTL formula, as the remarks show.
