---
tag: EQ9DND41TR
kind: example
name: Intuitionistic logic is explosive
msc: ["03B20", "03B53"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [TTKZGJEEK7]
not_instance_of:
  - target: C7YWCR87QJ
    note: in intuitionistic logic every formula follows from a formula and its negation, so the logic is not paraconsistent
uses: [TTKZGJEEK7, Q11N8X99FK, PAQ4ZX2TX1, 029JBBF693, 35VKJY77TY]
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_explosion
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: Intuitionistic Logic (SEP entry)
---

## Example

In [[intuitionistic logic|Q11N8X99FK]], $\neg A$ abbreviates $A \to \bot$, and the rule ex falso lets us infer any formula from $\bot$.
We derive $q$ from $p$ and $\neg p$ in [[natural deduction|PAQ4ZX2TX1]].

1. $p$. This is the first premise.
2. $\neg p$, that is $p \to \bot$. This is the second premise.
3. $\bot$. This follows from lines 2 and 1 by $\to$-elimination.
4. $q$. This follows from line 3 by ex falso.

So $p, \neg p \vdash_{\mathrm{IL}} q$, and the same four lines work for every pair of formulas $\varphi$, $\psi$ in place of $p$, $q$.
Hence intuitionistic consequence is [[explosive|TTKZGJEEK7]].

The same result holds in [[Kripke semantics|35VKJY77TY]].
If $w \Vdash \neg p$, then no world above $w$ forces $p$, and $w$ itself is above $w$.
So no world forces both $p$ and $\neg p$, and the consequence holds vacuously.

## Remarks

Intuitionistic logic rejects excluded middle but keeps explosion.
So a logic can be non-classical and still explosive; paraconsistency is a separate property.
If we remove ex falso, we get minimal logic, where $p, \neg p \vdash \bot$ but $p, \neg p \nvdash q$ for a variable $q$ distinct from $p$; see [[ex falso is not a theorem of minimal logic|T2SXPH67RQ]].
Minimal logic is not strongly paraconsistent, because the contradiction still proves every negated formula $\neg q$.

## Explanations

### L1 human

In intuitionistic logic, "not $p$" means "$p$ leads to absurdity".
If we have both $p$ and "not $p$", then we have an absurdity.
The rule ex falso says that an absurdity proves anything.
So a contradiction still proves every statement.

### L2 human

Take $p$ to be "$2 = 3$" and $q$ to be "every prime is odd".
From $2 = 3$ and $2 \neq 3$, the elimination rule for $\to$ gives $\bot$.
Ex falso then gives "every prime is odd", which is false.
The derivation is valid because its premises can never both hold.
A trap is to think that rejecting excluded middle also blocks explosion; the two laws are independent.
