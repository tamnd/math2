---
tag: D1YQW43N3K
kind: concept
name: Machine-assisted mathematical discovery
aliases: [automated-conjecturing, ai-assisted-mathematics, computer-generated-conjectures]
msc: ["00A35", "68T05", "68T20", "68V30"]
topics: [DME0TPC348]
audience: research
uses: [BPEPTN0TT9, R2T42N5XGK, WMEMMHZ3BH, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Graffiti_(program)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ramanujan_machine
    locator: lead section
  - url: https://en.wikipedia.org/wiki/AlphaEvolve
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Experimental_mathematics
    locator: Tools and techniques
  - url: https://arxiv.org/abs/2511.02864
    locator: abstract
---

## Summary

Machine-assisted discovery uses programs that propose new [[conjectures|WMEMMHZ3BH]], formulas or objects, not only data for a person to read.
Every proposal still needs a check: a formula needs a [[proof|0B94TKFQJX]], and an object needs an independent test.

Here is a small version of a problem that machines have worked on.
A [[cap set|B7SKJ1GP5P]] in $\mathbb{F}_3^n$ is a set of vectors with entries $0, 1, 2$ such that no three distinct vectors $x, y, z$ satisfy $x + y + z = 0$ modulo $3$.
In dimension $2$ the set $\{(0,0), (0,1), (1,0), (1,1)\}$ is a cap set.
Check the four triples:
$$(0,0) + (0,1) + (1,0) = (1,1), \quad (0,0) + (0,1) + (1,1) = (1,2),$$
$$(0,0) + (1,0) + (1,1) = (2,1), \quad (0,1) + (1,0) + (1,1) = (2,2),$$
and none of the sums is $(0,0)$.
In dimension $8$ the largest known cap set had $496$ vectors.
In December 2023 a team at Google DeepMind reported in *Nature* that their system FunSearch had found one with $512$ vectors.
Anyone can check such a claim with a short program that tests all triples, without trusting the system that found the set.

The main forms of machine-assisted discovery are conjecture generators, which test many candidate statements against data, and search systems, which look for objects that beat a known bound.
Since about 2021, systems based on machine learning and on large language models have joined them.
The field extends [[experimental mathematics|BPEPTN0TT9]] from the search for one identity to searches over large spaces of statements and objects, and it changes fast, so every claim below carries its date.

## Motivation

[[Forming conjectures|R2T42N5XGK]] is a search through many candidate statements, and a person can examine only a few.
A program can test millions of candidates against a table of data and report the ones that survive.
Many problems also ask for an object, such as a packing, a coloring or an algorithm, that beats a known bound.
Such problems have a cheap check and a huge search space, and that combination suits a machine.

The same features create risks.
A program that tests many candidates finds some that fit the data by chance, as the [[strong law of small numbers|8AFXPXCE3N]] predicts.
A system that writes text can state results that it has not established, or present known results as new.
So the method needs explicit rules for checking its claims.

## Notation

Four terms are used below.
A conjecture generator takes a database of objects and a list of invariants, and outputs inequalities or identities between invariants that hold on the whole database.
A search with an evaluator takes a scoring function on candidate objects, such as the size of a set with a property, and proposes candidates that raise the score.
A candidate is verified when an independent program checks it, for example by testing all triples of a proposed cap set.
A claim is proved when a proof is written and checked by experts, or checked by a proof assistant.

## Remarks

### Conjecture generators

Siemion Fajtlowicz wrote the program Graffiti at the University of Houston in the mid-1980s.
It proposed inequalities between invariants of graphs, and other mathematicians proved many of them.
Fan Chung proved in 1988 a Graffiti conjecture that the average distance in a graph is at most its independence number.

In 2021 a group at the Technion described the Ramanujan Machine in *Nature*.
Its algorithms propose continued fractions for constants such as $\pi$, $e$ and values of the zeta function, and some of the proposed formulas were later proved.
Also in 2021, Alex Davies and coauthors reported in *Nature* that models trained on data suggested a relation between invariants of knots, which led to a theorem, and suggested progress on a conjecture about Kazhdan-Lusztig polynomials.

### Search systems

Adam Zsolt Wagner showed in 2021 that a simple reinforcement learning method can construct graphs that refute several published conjectures in graph theory.
FunSearch (Google DeepMind, *Nature*, December 2023) paired a language model with an evaluator and evolved programs whose output is a cap set; the dimension $8$ result is in the Summary.

AlphaEvolve (Google DeepMind, May 2025) works in the same way at a larger scale.
It found a way to multiply two $4 \times 4$ matrices of complex numbers with $48$ multiplications of numbers, against $49$ for two rounds of the [[Strassen algorithm|3CVWXDS4JQ]], since $7 \cdot 7 = 49$.
It also found $593$ spheres that touch a central sphere in dimension $11$, which raised the lower bound for the [[kissing number|B408FZYXF9]] from $592$.
In November 2025 Bogdan Georgiev, Javier Gómez-Serrano, Terence Tao and Adam Zsolt Wagner reported tests of AlphaEvolve on $67$ problems from analysis, combinatorics, geometry and number theory.

### What it is not

The proof of the [[Robbins conjecture|X74S395RZD]] by the prover EQP in 1996 is [[automated theorem proving|A51M1KK9DJ]]: the program proved a statement that people had posed, and it discovered no statement.
A computer proof that checks all cases of a finite problem settles a known question; its status is part of [[computer-assisted proof and verification|54HCSZ6NBT]].
A lookup in the OEIS retrieves known results and proposes nothing new; see [[mathematical databases|956TNX0HG9]].

### The rules you can use

A formula proposed by a machine has the status of a conjecture, with the tests of any experimental result: more precision, new data and a proof.
A construction can often be verified completely by a short independent program, and the check turns it into a theorem about one object, such as a lower bound.
The evaluator decides what a search can find, and a badly chosen score gives useless or misleading output.
A claim that a problem is "solved" needs a literature search, because a system may reproduce a known result and a list of open problems may be out of date.

### Watch out

A formula that a program reports is a pattern that fits finite data, and a pattern that holds in many cases is not a proof.

A solution announced before a literature search can be old.
In October 2025 Kevin Weil, a vice president at OpenAI, posted that GPT-5 had found solutions to ten unsolved Erdős problems.
Thomas Bloom, who maintains the site erdosproblems.com, replied that the problems were listed as open only because he did not know of solutions, and that GPT-5 had found existing papers that solved them.
The post was deleted.

An improved bound is not a proof of optimality: $593$ touching spheres in dimension $11$ say nothing about the upper bound.

### History

Douglas Lenat's program AM explored concepts of elementary number theory in the 1970s.
Graffiti began in the mid-1980s.
Simon Plouffe found the BBP formula for $\pi$ with an integer relation search in 1995, an early formula found by a program.
The Ramanujan Machine, the work of Davies and coauthors, and the work of Wagner appeared in 2021, FunSearch in December 2023 and AlphaEvolve in May 2025.

### Try it

Is $\{(0,0), (1,1), (2,2)\}$ a cap set in $\mathbb{F}_3^2$?
No, since $(0,0) + (1,1) + (2,2) = (3,3) = (0,0)$ modulo $3$, so the three vectors lie on a line.

How many triples must a program test to verify a proposed cap set of $512$ vectors?
It must test $\binom{512}{3} = 22238720$ triples, which a computer does in seconds.

## Explanations

### L1 human

Computers can now suggest new mathematics, not only do arithmetic.
Some programs look at many examples and guess rules that connect them.
Other programs search for clever objects, such as a better way to multiply small tables of numbers.
In 2025 one program found a way to multiply two $4 \times 4$ tables of complex numbers with $48$ multiplications instead of $49$.
Every suggestion still has to be checked: a guessed rule needs a proof, and a found object needs an independent test.

### L2 human

We follow the checks that a claimed improvement of a bound should pass.
The claim is a configuration of $593$ unit spheres that touch a central unit sphere in $\mathbb{R}^{11}$, given as $593$ vectors, the centers of the touching spheres.
First, each vector must have length $2$, so that each sphere touches the central one.
Second, any two vectors must be at distance at least $2$, so that no two spheres overlap.
Both checks are finite, and with exact or interval arithmetic they are rigorous.
Third, the literature must confirm that the best earlier configuration had $592$ spheres.
If all three checks pass, the kissing number in dimension $11$ is at least $593$, and nothing is claimed about the upper bound.

The typical use: a construction comes with data that anyone can check, whatever the method that found it.
Watch out for floating point coordinates, which can hide a tiny overlap, so the second check needs exact arithmetic or a safe margin.

### L3 human

The systems differ in what they search.
Conjecture generators search a space of statements and test them on data, so their risk is overfitting, the formal side of the strong law of small numbers.
Search systems with evaluators search a space of objects or programs, and the evaluator certifies their output, so their risk lies in the choice of the problem and the score.
Language models can propose both statements and proofs, and their output needs the strongest checks.

The checks fall into three kinds.
Constructions are verified by independent computation.
Proofs are verified by experts or by a proof assistant; see [[mathematical software and formalization|F3F5GGYHMM]].
Novelty is verified by a literature search.
The software belongs to [[tools of experimental mathematics|KY55MDRBEY]], and the acceptance of computer proofs to [[rigor and the acceptance of proofs|1BTHSHST4M]].
