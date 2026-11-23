---
tag: DT8R2PB0P7
kind: example
name: A while program as a PDL program
msc: ["03B45", "68Q60"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [VJ78A0Q22R]
uses: [VJ78A0Q22R, H1M6RSBJ5H]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_logic_(modal_logic)
    locator: Language
---

## Example

In [[propositional dynamic logic|VJ78A0Q22R]] the loop $\mathbf{while}\ p\ \mathbf{do}\ a$ is the regular program below.
$$\omega = (p ? ; a)^* ; \neg p ?$$
It says: test $p$ and do $a$, as often as you like, and at the end check that $p$ is false.
Let $W = \{0, 1, 2, 3\}$, $R_a = \{(0, 1), (1, 2), (2, 2), (3, 3)\}$ and $V(p) = \{0, 1, 3\}$.
We compute the relation $R_\omega$ step by step.

1. The test $p ?$ keeps the $p$-worlds and does not move, so $R_{p ?} = \{(0, 0), (1, 1), (3, 3)\}$.
2. The program $p ? ; a$ is a test followed by an $a$-step.
   From $0$, $1$ and $3$ the $a$-steps go to $1$, $2$ and $3$, so $R_{p ? ; a} = \{(0, 1), (1, 2), (3, 3)\}$.
3. The star adds the identity and the chains.
   The only chain of two steps is $0, 1, 2$, which gives $(0, 2)$, so $R_{(p ? ; a)^*} = \{(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (1, 2), (0, 2)\}$.
4. The test $\neg p ?$ keeps only world $2$, so $R_{\neg p ?} = \{(2, 2)\}$.
5. A pair is in $R_\omega$ when a pair of step 3 is followed by $(2, 2)$, so it must end in $2$.
   The pairs of step 3 that end in $2$ are $(0, 2)$, $(1, 2)$ and $(2, 2)$.

So the loop has the following relation:
$$R_\omega = \{(0, 2), (1, 2), (2, 2)\}$$
Check: from $0$ the loop runs twice and stops at $2$, from $1$ it runs once, and from $2$ it does not run at all.

## Remarks

World $3$ has no $\omega$-successor, because $p$ stays true along $3, 3, 3, \dots$ and the loop never stops.
So $[\omega] \bot$ holds at $3$, while $\langle \omega \rangle \top$ fails there.
This is how $\mathsf{PDL}$ expresses termination: $\langle \omega \rangle \top$ says that some run of the loop ends.

The formula $[\omega] \neg p$ holds in every model, since every pair of $R_\omega$ ends with a $\neg p ?$-step.
In the language of [[Hoare logic|H1M6RSBJ5H]] this is the triple $\{\top\} \, \mathbf{while}\ p\ \mathbf{do}\ a \, \{\neg p\}$, the familiar fact that a while loop exits with its condition false.
If we change $R_a$ so that $3 R_a 2$ instead of $3 R_a 3$, then world $3$ also reaches $2$, and $R_\omega$ gains the pair $(3, 2)$.

## Explanations

### L1 human

A while loop repeats a step as long as a condition holds.
Here the condition is $p$ and the step is $a$.
Starting in world $0$, the condition holds, so we step to $1$.
It still holds, so we step to $2$, where it fails, and the loop stops.
In world $3$ the step leads back to $3$, where the condition still holds, so the loop runs forever.

### L2 human

We check $[\omega] \neg p$ at every world of the model.
At $0$, at $1$ and at $2$, the only $\omega$-successor is $2$, and $2$ is not a $p$-world, so the formula holds.
At $3$ there is no $\omega$-successor, so the formula holds because there is nothing to check.
This is the typical use of the translation: a property of a loop becomes a formula, and the induction axiom of $\mathsf{PDL}$ proves it.
Watch out: $[\omega] \neg p$ does not say that the loop stops, since it also holds at world $3$, where the loop runs forever.
