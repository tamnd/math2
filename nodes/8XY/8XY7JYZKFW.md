---
tag: 8XY7JYZKFW
kind: topic
name: Proof interpretations and conservation results
msc: ["03F10", "03F25"]
topics: [DYJ0KGTPMR]
---

## Summary

Classical arithmetic proves that every program halts or does not halt, and intuitionistic arithmetic does not.
Yet for many simple statements the two theories agree, and a classical proof of "for every $x$ there is a $y$" still contains a way to compute $y$.
The topic, a part of [[mathematical logic|DYJ0KGTPMR]], explains why, and how to get the computation out.

The first tool is a translation.
The double-negation translation of Gödel and Gentzen, from 1933, sends classical proofs to intuitionistic ones, and Friedman's A-translation then recovers witnesses for $\Pi^0_2$ sentences.
The second tool is a functional interpretation.
Gödel's Dialectica interpretation of 1958 reads each theorem of arithmetic as a statement about higher-type functionals in system T, and Spector's bar recursion extends it to analysis.
Proof mining applies these interpretations to proofs in analysis and extracts explicit bounds.

The results that come out are conservation theorems: a strong theory proves no new sentences of some simple kind.
Interpretability is a different relation between theories, and the topic keeps the two apart.

## Remarks

### Reading order

1. [[Double-negation translation|HGJVM49PA4]]: you learn how classical proofs become intuitionistic ones, and why PA is consistent if HA is.
2. [[Friedman's A-translation|6CCK0TT69P]]: you learn to extract witnesses, and you see why PA and HA prove the same $\Pi^0_2$ sentences.
3. [[Gödel's system T|A4WR995XZP]]: you meet the primitive recursive functionals of finite type, which serve as the witnesses below.
4. [[Dialectica interpretation|HZ17ES9PDY]]: you learn Gödel's reading of arithmetic in system T, and how it extracts programs from proofs.
5. [[No-counterexample interpretation|4BCD1EM542]]: you see Kreisel's reading of classical theorems as games against counterexamples.
6. [[Bar recursion|8CCG6F2FAT]]: you see how Spector's extension of system T handles classical analysis.
7. [[Proof mining|XR1JXQG1CD]]: you see the interpretations at work on real proofs in analysis, with explicit bounds as the output.
8. [[Conservation theorems|TNZ995J8AP]]: you get the general picture, with WKL0, ACA0 and PA as examples, and three methods of proof.
9. [[Parsons's theorem|2VYJXZZDGB]]: you learn why the provably total functions of $\mathrm{I}\Sigma_1$ are the primitive recursive ones.
10. [[Interpretability between theories|8H03GRMDYG]]: you learn relative interpretations, and why they give equiconsistency but not conservation.
11. [[Herbrand analysis|MESZ87G9ET]]: you learn to read primitive recursive witnesses directly off proofs of $\Sigma_1$ formulas in $\mathrm{I}\Sigma_1$.

### Prerequisites

- The topic [[structural proof theory|R10RMQCJQX]], for sequent calculus, natural deduction and cut elimination.
- The topic [[formal arithmetic and its fragments|QHCRN4JVG0]], for PA, $\mathrm{I}\Sigma_1$ and primitive recursive arithmetic.
- The area [[type theory and constructive mathematics|K6P3NSQEZ3]], for Heyting arithmetic and realizability.
