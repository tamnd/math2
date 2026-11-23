---
tag: 8ZBH60TVBR
kind: example
name: The case analysis of the four color theorem is not a Book proof
aliases: [the-case-analysis-of-the-four-colour-theorem-is-not-a-book-proof]
msc: ["00A35", "05C15"]
topics: [1BTHSHST4M]
audience: ug2
instance_of: [MC18C7BMFT]
not_instance_of:
  - target: A4RJYP79A7
    note: the proof is correct, but it fails the criteria of brevity and of explanation, because it rests on a computer check of hundreds of cases
uses: [A4RJYP79A7, MC18C7BMFT, 0M406JC8J1, 06C0JBE52D, 029JQEK15B]
sources:
  - url: https://en.wikipedia.org/wiki/Four_color_theorem
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Four_color_theorem
    locator: History
  - url: https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK
    locator: Outline
---

## Example

The [[four color theorem|0M406JC8J1]] says that every finite loopless [[planar graph|029JQEK15B]] can be colored with four colors so that the two ends of each edge get different colors.
We describe the shape of its proof, and then we check it against the criteria of a [[proof from the Book|A4RJYP79A7]].

1. Suppose the theorem fails, and take a counterexample $G$ with the least number of vertices.
2. A configuration is a small piece of a planar graph, and it is reducible if it cannot occur in a least counterexample.
3. A set of configurations is unavoidable if every planar graph of the relevant kind contains one of them.
4. If some unavoidable set consists of reducible configurations, then no least counterexample exists, and the theorem holds.
5. Kenneth Appel and Wolfgang Haken found such a set in 1976, with more than a thousand configurations.
   They checked the reducibility of each configuration by computer, with more than a thousand hours of computer time.
6. Neil Robertson, Daniel Sanders, Paul Seymour and Robin Thomas gave a new proof in 1997 with $633$ configurations, again checked by computer.

Now the criteria.
The proof is correct and accepted, and Georges Gonthier and Benjamin Werner checked a version of it in the Coq proof assistant in 2005.
The plan of steps 1 to 4 is a single idea and needs only basic graph theory.
But carrying out the plan takes a case analysis too long to check by hand, so the test of brevity fails.
The test of explanation fails too: each case is verified, but no single reason shows why four colors suffice.
So the proof is a correct [[computer-assisted proof|MC18C7BMFT]], and it is not a Book proof.
That is a statement about the criteria, not a judgment of the value of the proof.

## Remarks

The [[five color theorem|06C0JBE52D]] shows the contrast.
By Euler's formula, every planar graph has a vertex of degree at most $5$, so the single configuration "a vertex of degree at most $5$" is unavoidable.
For five colors that configuration is reducible by a Kempe chain argument, so the plan of steps 1 to 4 works with one configuration and the proof fits on a page.
For four colors a vertex of degree $5$ is not reducible on its own, and the unavoidable set must use larger configurations.
Aigner and Ziegler include a short proof of a five color theorem in their book.

Alfred Kempe published a short proof of the four color theorem in 1879, and Percy Heawood found an error in it in 1890.
A short argument with a gap is not a Book proof either, since correctness comes first.
Whether the four color theorem has a short proof is an open question.
If someone finds one, it would be a candidate for the Book, and the old proof would stay correct.

## Explanations

### L1 human

The four color theorem says that four colors are always enough to color a map so that neighboring countries get different colors.
It is true, but its proof is very long.
The proof splits the problem into hundreds of special cases, and a computer checks each case.
Mathematicians accept the proof, but nobody can read it in one sitting and see why four colors are enough.
A proof from the Book is short and shows the reason at once, so this proof is not one.

### L2 human

We compare the two color theorems at a vertex $v$ of degree $5$, with neighbors $v_1, \dots, v_5$ in cyclic order around $v$.
By the choice of a least counterexample, $G - v$ has a coloring, and we try to extend it to $v$.
With five colors, suppose the neighbors use all five colors, with $v_i$ colored $i$.
Look at the vertices colored $1$ or $3$ that can be reached from $v_1$ along such vertices, which is a Kempe chain.
If this chain does not reach $v_3$, swap colors $1$ and $3$ on it, and color $1$ is free for $v$.
If it does reach $v_3$, it forms with $v$ a closed curve that separates $v_2$ from $v_4$, so the chain of colors $2$ and $4$ from $v_2$ cannot reach $v_4$, and swapping it frees color $2$.
With four colors the five neighbors repeat a color, and one may need two such swaps at once, which can interfere.
That interference is exactly where Kempe's proof of 1879 failed, as Heawood showed.
So a vertex of degree $5$ alone does not give a short proof, and the proof needs a large unavoidable set.
The typical use of the example is to separate the question "is the proof correct?" from the question "is it a Book proof?".
Watch out: "not a Book proof" does not mean "not a good proof", since the criteria describe form and not worth.
