---
tag: ~aabeab7d
kind: example
name: Double negation of excluded middle in LJT
msc: ["03F05", "03B20"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [~e6a5f260]
uses: [~e8b3934d, Q11N8X99FK, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_excluded_middle
    locator: lead section
---

## Example

We derive $\Rightarrow \neg \neg (p \vee \neg p)$ in Dyckhoff's calculus LJT of the [[definition|~e8b3934d]].
Recall that $\neg A$ is $A \to \bot$, so the goal is $\Rightarrow ((p \vee (p \to \bot)) \to \bot) \to \bot$.
We build the derivation backwards.

1. R${\to}$ reduces the goal to $(p \vee (p \to \bot)) \to \bot \Rightarrow \bot$.
2. L${\vee}{\to}$, with $C = p$, $D = p \to \bot$ and $B = \bot$, reduces it to $p \to \bot, (p \to \bot) \to \bot \Rightarrow \bot$.
3. L${\to}{\to}$ on $(p \to \bot) \to \bot$, with $C = p$, $D = \bot$, $B = \bot$ and $\Gamma = p \to \bot$, gives two premises.
4. The right premise is $\bot, p \to \bot \Rightarrow \bot$, an axiom.
5. The left premise is $\bot \to \bot, p \to \bot \Rightarrow p \to \bot$.
6. R${\to}$ reduces it to $p, \bot \to \bot, p \to \bot \Rightarrow \bot$.
7. L0${\to}$ on $p$ and $p \to \bot$ reduces it to $p, \bot, \bot \to \bot \Rightarrow \bot$, an axiom.

## Remarks

The formula is valid in [[intuitionistic logic|Q11N8X99FK]], although $p \vee \neg p$ is not.
In G3ip, a derivation of the same sequent keeps $(p \vee \neg p) \to \bot$ in the left premise of L${\to}$ and uses it twice.
LJT avoids this: in step 2, the formula $(p \vee \neg p) \to \bot$ is replaced by two smaller implications, and each is used once.
Every step reduces the weight of the sequent, so a backward search in LJT on this goal cannot loop.

## Explanations

### L1 human

The [[law of excluded middle|0RYYK8PG4S]] says "$p$ or not $p$", and intuitionistic logic does not accept it in general.
It does accept that the law cannot be refuted, which is the formula derived here.
The derivation shows this in seven steps, and each step makes the sequent simpler.

### L2 human

At each step, choose a rule whose principal formula is in the antecedent and matches one of the LJT shapes.
In step 3, the principal formula $(p \to \bot) \to \bot$ has an implication as its antecedent, so L${\to}{\to}$ is the rule.
A trap is step 7: L0${\to}$ applies to $p \to \bot$ only because the atom $p$ is in the antecedent, which R${\to}$ provided in step 6.
