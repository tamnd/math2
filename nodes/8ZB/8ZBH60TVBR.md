---
tag: 8ZBH60TVBR
kind: example
name: The case analysis of the four colour theorem is not a Book proof
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

The [[four colour theorem|0M406JC8J1]] says that every finite loopless [[planar graph|029JQEK15B]] can be coloured with four colours.
We describe the shape of its proof, and then we check it against each criterion of a [[proof from the Book|A4RJYP79A7]].

1. Suppose the theorem fails. Take a counterexample $G$ with the least number of vertices.
2. A configuration is a small piece of a planar graph. It is reducible if it cannot occur in a least counterexample.
3. A set of configurations is unavoidable if every planar graph of the relevant kind contains one of them.
4. If an unavoidable set consists of reducible configurations, then no least counterexample exists, and the theorem holds.
5. Appel and Haken found such a set in 1976. It had more than a thousand configurations.
6. They checked the reducibility of each configuration by computer, with more than a thousand hours of computer time.
7. Robertson, Sanders, Seymour and Thomas gave a new proof in 1997 with $633$ configurations, again checked by computer.

Now we check the criteria of a Book proof.

- Correctness: the proof is accepted. Gonthier and Werner checked a proof in the Coq proof assistant in 2005.
- Brevity: the criterion fails. The case analysis is too long to check by hand.
- One idea: the plan of steps 1 to 4 is one idea. But the plan needs a long case analysis to carry out.
- Few prerequisites: the plan needs only basic graph theory, but the check needs a computer.
- Explanation: the criterion fails. Each case is verified, but no single reason shows why four colours suffice.

So the proof is correct and it is a [[computer-assisted proof|MC18C7BMFT]], but it is not a Book proof.
This is a statement about the criteria, not a judgement of the value of the proof.

## Remarks

The [[five colour theorem|06C0JBE52D]] shows the contrast.
By Euler's formula, a planar graph has a vertex of degree at most $5$.
For five colours the set $\{$a vertex of degree at most $5\}$ is unavoidable, and each such vertex is reducible by a Kempe chain argument.
So the plan of steps 1 to 4 works with one configuration, and the proof fits on a page.
For four colours a vertex of degree $5$ is not reducible on its own, and the unavoidable set must use larger configurations.

The book of Aigner and Ziegler gives a proof of the five colour theorem.
Alfred Kempe published a short proof of the four colour theorem in 1879, and Percy Heawood found an error in it in 1890.
A short argument with a gap is not a Book proof either, because correctness comes first.

It is an open question whether the four colour theorem has a short proof.
If someone finds one, it would be a candidate for the Book, and the old proof would stay correct.

## Explanations

### L1 human

The four colour theorem says that four colours are always enough to colour a map, with neighbouring countries in different colours.
It is true, but its proof is very long.
The proof splits the problem into hundreds of special cases, and a computer checks each case.
Mathematicians accept the proof.
But nobody can read it in one sitting and see why four colours are enough.
A proof from the Book is short and shows the reason at once, so this proof is not one.

### L2 human

We compare the two colour theorems on one point: the vertex of degree $5$.

1. Let $v$ have neighbours $v_1, \ldots, v_5$ in cyclic order, and colour $G - v$ by the least counterexample assumption.
2. With five colours: if $v_1, \ldots, v_5$ use all five colours, swap two colours on a Kempe chain from $v_1$ or from $v_2$.
3. One of the swaps frees a colour for $v$, so the vertex of degree $5$ is reducible.
4. With four colours: two swaps are needed at the same time, and they can interfere.
5. This interference is the error that Heawood found in Kempe's proof.
6. So a vertex of degree $5$ alone does not give a short proof, and the proof needs a large unavoidable set.

The typical use of the example is to separate the question "is the proof correct?" from the question "is it a Book proof?".
A trap is to read "not a Book proof" as "not a good proof"; the criteria describe form, not worth.
