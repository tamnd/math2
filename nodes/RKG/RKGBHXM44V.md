---
tag: RKGBHXM44V
kind: example
name: Hypothetical syllogism is a derived rule of a Hilbert system
msc: ["03B05", "03F03"]
topics: [H8QZY0RZXZ]
audience: ug1
instance_of: [QPD3X471Q1]
uses: [QPD3X471Q1, 1MGMQX43B8, 7MT8CPCEM4, 9X08XK5RV2]
sources:
  - url: https://en.wikipedia.org/wiki/Hypothetical_syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: lead section
  - book: isbn:9781482237726
---

## Example

A Hilbert system has one rule, modus ponens, but we can show that it already contains the chaining rule "from $\varphi \to \psi$ and $\psi \to \chi$ infer $\varphi \to \chi$" as a shortcut.
We work in the [[Hilbert system|1MGMQX43B8]] $H$ for propositional logic, whose axioms are the instances of
$$\begin{aligned} &\text{A1: } \varphi \to (\psi \to \varphi), \\ &\text{A2: } (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \\ &\text{A3: } (\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi), \end{aligned}$$
and whose only rule is modus ponens (MP).
[[Hypothetical syllogism|7MT8CPCEM4]] is the rule "from $\varphi \to \psi$ and $\psi \to \chi$ infer $\varphi \to \chi$".
We show that it is a derived [[rule of inference|QPD3X471Q1]] of $H$: for all formulas $\varphi, \psi, \chi$, there is a derivation of $\varphi \to \chi$ from the two premises.

1. $\psi \to \chi$ is a premise.
2. $(\psi \to \chi) \to (\varphi \to (\psi \to \chi))$ is the instance of A1 with $\psi \to \chi$ in place of $\varphi$ and $\varphi$ in place of $\psi$.
3. $\varphi \to (\psi \to \chi)$ follows by MP from lines 1 and 2.
4. $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$ is an instance of A2.
5. $(\varphi \to \psi) \to (\varphi \to \chi)$ follows by MP from lines 3 and 4.
6. $\varphi \to \psi$ is a premise.
7. $\varphi \to \chi$ follows by MP from lines 6 and 5.

Each line is a premise, an instance of an axiom schema, or follows by MP from two earlier lines.
So $\{ \varphi \to \psi, \psi \to \chi \} \vdash_H \varphi \to \chi$ for all $\varphi, \psi, \chi$, and the rule is derivable.

The rule also preserves truth.
Let $v$ be a valuation that makes both premises true.
If $\varphi$ is false under $v$, then $\varphi \to \chi$ is true.
If $\varphi$ is true under $v$, then $\psi$ is true by the first premise, $\chi$ is true by the second, and so $\varphi \to \chi$ is true.

## Remarks

Because the rule is derivable, it may be used inside any derivation from hypotheses, as an abbreviation of lines 1 to 7.
A rule that is only admissible, such as [[uniform substitution|DE0GD8BM4M]], may not be used that way.
Applying the [[deduction theorem|9X08XK5RV2]] twice to the derivation gives the theorem
$$\vdash_H (\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi)).$$
The derivation uses only A1, A2 and MP.
So hypothetical syllogism is derivable in every Hilbert system that contains these two schemas, including the usual systems for intuitionistic logic.

## Explanations

### L1 human

Hypothetical syllogism chains two implications.
If rain makes the street wet, and a wet street makes it slippery, then rain makes the street slippery.
The Hilbert system does not have this rule among its basic rules.
The derivation shows that the system reaches the same conclusion in seven small steps, with only its axioms and modus ponens.
So we may add the chaining rule as a shortcut without changing what the system can prove.

### L2 human

Take the concrete instance $\varphi = p$, $\psi = q$, $\chi = r$.
Line 2 becomes $(q \to r) \to (p \to (q \to r))$, an instance of A1.
Line 4 becomes $(p \to (q \to r)) \to ((p \to q) \to (p \to r))$, an instance of A2.
Line 7 becomes $p \to r$, derived from the hypotheses $p \to q$ and $q \to r$.
The typical use of a derived rule is to shorten later derivations: chaining $p \to q$, $q \to r$ and $r \to s$ into $p \to s$ takes two uses of the rule, and each use stands for five lines of axioms and modus ponens.
Watch out for the order of the premises in line 7: modus ponens needs $\varphi \to \psi$ and $(\varphi \to \psi) \to (\varphi \to \chi)$, and line 5 is the second of these.
