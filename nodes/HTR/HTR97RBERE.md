---
tag: HTR97RBERE
kind: example
name: The paradoxes of strict implication
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [5JW54NP52K]
uses: [5JW54NP52K, JS8W7PA6JK, G989VP2NGP, 05006AJ7DZ, NGHWZ9Y7ZV, CN7HK9K1B6]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

"A square has five corners" is impossible, so in every possible world it is false.
Then in every possible world "if a square has five corners, then the moon is cheese" is true, and the first sentence strictly implies the second.
We write the [[strict implication|5JW54NP52K]] of $p$ and $q$ as $\square(p \to q)$, without Lewis's fishhook symbol.
We derive four theorems of $\mathsf{K}$ that look paradoxical when $\square(p \to q)$ is read as "$p$ entails $q$".

1. $\neg p \to (p \to q)$ is a [[tautology|05006AJ7DZ]].
2. RM of [[normal modal logic K|JS8W7PA6JK]] applied to step 1 gives $\mathsf{K} \vdash \square\neg p \to \square(p \to q)$.
3. $q \to (p \to q)$ is a tautology.
4. RM applied to step 3 gives $\mathsf{K} \vdash \square q \to \square(p \to q)$.
5. $(p \wedge \neg p) \to q$ is a tautology, so [[necessitation|G989VP2NGP]] gives $\mathsf{K} \vdash \square((p \wedge \neg p) \to q)$.
6. $q \to (p \vee \neg p)$ is a tautology, so necessitation gives $\mathsf{K} \vdash \square(q \to (p \vee \neg p))$.
7. Step 2 says that an impossible proposition, one with $\square\neg p$, strictly implies every proposition.
8. Step 4 says that a necessary proposition is strictly implied by every proposition.
9. Steps 5 and 6 say that a contradiction strictly implies everything, and everything strictly implies a tautology.

## Remarks

The example shows that strict implication repeats, one level up, the paradoxes of material implication.
For material implication, a false $p$ implies every $q$, and a true $q$ is implied by every $p$.
For strict implication, "false" becomes "impossible" and "true" becomes "necessary".
Lewis introduced strict implication to avoid the paradoxes of material implication, and these theorems show that the repair is only partial.

In a [[Kripke model|NGHWZ9Y7ZV]], $\square(p \to q)$ at $w$ says that every successor with $p$ has $q$.
If no successor has $p$, the condition holds vacuously, which is step 2 on frames.
The derivations use only RM and necessitation, so they work in every normal modal logic.
The logic of all [[neighborhood frames|CN7HK9K1B6]] has neither RM nor necessitation, and there none of steps 2, 4, 5 and 6 need hold.

## Explanations

### L1 human

"$p$ strictly implies $q$" means "it is impossible that $p$ is true and $q$ is false".
If $p$ is itself impossible, for example "a square has five corners", then this always holds.
So "a square has five corners" strictly implies "the moon is made of cheese".
Also, if $q$ is necessary, for example "$2 + 2 = 4$", then every statement strictly implies it.
These results are correct in the logic, but they surprise people who read "implies" as "is relevant to".

### L2 human

We check step 2 on a small model.

1. Take $W = \{ 1, 2 \}$, $R = \{ (1, 2) \}$, $V(p) = \varnothing$ and $V(q) = \varnothing$.
2. At $1$, the only successor $2$ lacks $p$, so $\square\neg p$ is true at $1$.
3. At $2$, the formula $p \to q$ is true, since $p$ is false.
   So $\square(p \to q)$ is true at $1$.
4. So at $1$, the impossible $p$ strictly implies the false $q$, as step 2 predicts.

You meet these theorems in the discussion of relevance logics, which reject them.
Watch out: the paradoxes are theorems of every normal modal logic, so no choice of a class of Kripke frames removes them.
