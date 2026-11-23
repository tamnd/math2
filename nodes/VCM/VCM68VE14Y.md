---
tag: VCM68VE14Y
kind: example
name: Double negation of excluded middle in LJT
msc: ["03F05", "03B20"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [BZ59F5GBRR]
uses: [KP5KA51FC4, Q11N8X99FK, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_excluded_middle
    locator: lead section
---

## Example

We derive $\Rightarrow \neg \neg (p \vee \neg p)$ in Dyckhoff's calculus LJT of the [[definition|KP5KA51FC4]].
Since $\neg A$ is $A \to \bot$, the goal is $\Rightarrow ((p \vee (p \to \bot)) \to \bot) \to \bot$.
We build the derivation backwards, from the goal.

1. R${\to}$ reduces the goal to $(p \vee (p \to \bot)) \to \bot \Rightarrow \bot$.
2. L${\vee}{\to}$, with $C = p$, $D = p \to \bot$ and $B = \bot$, reduces it to $p \to \bot, (p \to \bot) \to \bot \Rightarrow \bot$.
3. L${\to}{\to}$ on $(p \to \bot) \to \bot$, with $C = p$, $D = \bot$, $B = \bot$ and $\Gamma = p \to \bot$, gives two premises.
4. The right premise is $\bot, p \to \bot \Rightarrow \bot$, an axiom.
5. The left premise is $\bot \to \bot, p \to \bot \Rightarrow p \to \bot$.
6. R${\to}$ reduces it to $p, \bot \to \bot, p \to \bot \Rightarrow \bot$.
7. L0${\to}$ on $p$ and $p \to \bot$ reduces it to $p, \bot, \bot \to \bot \Rightarrow \bot$, an axiom.

The derivation uses five rules: R${\to}$, L${\vee}{\to}$, L${\to}{\to}$, R${\to}$ and L0${\to}$.
Check: the two leaves both have $\bot$ in the antecedent, so both are axioms $\bot, \Gamma \Rightarrow C$.

## Remarks

The formula is valid in [[intuitionistic logic|Q11N8X99FK]], although $p \vee \neg p$ itself is not.
In G3ip, a derivation of the same sequent keeps $(p \vee \neg p) \to \bot$ in the left premise of L${\to}$ and uses it twice.
LJT avoids the second use.
In step 2 the formula $(p \vee \neg p) \to \bot$ is replaced by two smaller implications, and each of them is principal only once.

The weights confirm that the search cannot loop.
With the LJT weights, $w(p) = w(\bot) = 1$ and $w(A \vee B) = w(A \to B) = w(A) + w(B) + 1$, so $w(\neg p) = 3$ and $w(p \vee \neg p) = 5$.
The formula $(p \vee \neg p) \to \bot$ then has weight $5 + 1 + 1 = 7$, and step 2 replaces it by formulas of weights $3$ and $5$.
Check: $w(p \to \bot) = 1 + 1 + 1 = 3$ and $w((p \to \bot) \to \bot) = 3 + 1 + 1 = 5$, both less than $7$.

What changes for $\Rightarrow p \vee \neg p$?
R${\vee}$ must pick a disjunct, and both $\Rightarrow p$ and $\Rightarrow p \to \bot$ fail, the second because $p \Rightarrow \bot$ has no rule to apply.
So LJT, like intuitionistic logic, rejects excluded middle but accepts its double negation.

## Explanations

### L1 human

The [[law of excluded middle|0RYYK8PG4S]] says "$p$ or not $p$", and intuitionistic logic does not accept it in general.
It does accept that the law cannot be refuted, which is the formula derived here.
The derivation takes five rule steps, and each step makes the sequent simpler.

### L2 human

At each step, choose the rule that fits the principal formula.
In step 2 the antecedent of the implication is a disjunction, so L${\vee}{\to}$ applies.
In step 3 the principal formula $(p \to \bot) \to \bot$ has an implication as its antecedent, so L${\to}{\to}$ applies.
A trap is step 7.
L0${\to}$ applies to $p \to \bot$ only because the atom $p$ is in the antecedent, and R${\to}$ put it there in step 6.
