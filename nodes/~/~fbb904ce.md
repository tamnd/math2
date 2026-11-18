---
tag: ~fbb904ce
kind: example
name: A CTL* formula in neither LTL nor CTL
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [~2b6e0b85]
uses: [~c0b0b2f8, ~4085e024, ~51ed6c24, 1DA0Y6KDF8]
sources:
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: section Syntax
---

## Example

Let $\theta = A\,FGp \vee AG\,EF\,q$, a state formula of [[CTL*|~c0b0b2f8]], with two different atoms $p$ and $q$.
We show that $\theta$ is equivalent to no LTL formula and to no CTL formula.
For CTL we use one cited fact: no CTL formula is equivalent to $A\,FGp$, by Emerson and Halpern, see [[the CTL non-example|~51ed6c24]].

1. Not LTL. Take the structures $M_1$ and $M_2$ of [[the LTL non-example|~4085e024]], with $q$ in place of $p$, and with $p$ false everywhere.
2. Every path has $p$ false forever, so $A\,FGp$ fails at $s_0$ in both. So $\theta$ is equivalent to $AG\,EF\,q$ at $s_0$ in both.
3. By that non-example, $AG\,EF\,q$ holds at $s_0$ in $M_1$ and fails in $M_2$.
4. The two structures have the same set of label words from $s_0$, so every LTL formula has the same value at $s_0$ in both. Hence no LTL formula is equivalent to $\theta$.
5. Not CTL. Suppose that a [[CTL formula|1DA0Y6KDF8]] $\psi$ is equivalent to $\theta$. Let $\psi'$ be $\psi$ with $q$ replaced by $\bot$.
6. By induction on $\psi$, $M, s \models \psi'$ if and only if $M^-, s \models \psi$. Here $M^-$ is $M$ with $q$ removed from every label.
7. In $M^-$ no state has $q$, so $EF\,q$ is false everywhere. Since $AG\,\chi$ at $s$ implies $\chi$ at $s$, $AG\,EF\,q$ is false at every state.
8. So in $M^-$, $\theta$ is equivalent to $A\,FGp$. The value of $A\,FGp$ is the same in $M$ and $M^-$, since $q$ does not occur in it.
9. Hence for all $M$ and $s$: $M, s \models \psi'$ if and only if $M, s \models A\,FGp$. This contradicts the cited fact, so no such $\psi$ exists.

## Remarks

The two atoms must be different.
With one atom, $A\,FGp \vee AG\,EF\,p$ is equivalent to the CTL formula $AG\,EF\,p$.
Indeed, if $AG\,EF\,p$ fails, some reachable state $t$ reaches no $p$-state, and a path through $t$ has $\neg p$ forever after $t$.
So $A\,FGp$ implies $AG\,EF\,p$, and the first disjunct adds nothing.
The example shows that CTL* is strictly more expressive than the union of LTL and CTL.

## Explanations

### L1 human

Take one sentence that only LTL can say, and one that only CTL can say, with different basic facts.
Join them with "or".
The result is a CTL* sentence that neither smaller logic can say.

### L2 human

1. To rule out LTL, make the LTL disjunct false in a pair of structures with the same runs, and use the pair for the CTL disjunct.
2. To rule out CTL, set $q$ false everywhere. The CTL disjunct disappears, and a CTL formula for $\theta$ would become a CTL formula for $A\,FGp$.

A trap: the disjunction with the same atom $p$ twice collapses to a CTL formula, as the remarks show.
