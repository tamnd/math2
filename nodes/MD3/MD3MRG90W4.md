---
tag: MD3MRG90W4
kind: concept
name: Extremal principle
aliases: [extremal-principle]
msc: ["00A35", "05D99"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: school
uses: [01BX15HSRR, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%E2%80%93Gallai_theorem
    locator: Kelly's proof
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: Example applications
  - url: https://en.wikipedia.org/wiki/Oskar_Perron
    locator: lead section
---

## Summary

The extremal principle is a proof method: among all objects of a given kind, consider one that is largest or smallest for a chosen quantity.
The quantity may be a length, a distance, a number of elements or a sum.
The extremal object often has the property we want, because an object without it could be improved, against the choice.
So a typical proof has two parts: the extremal object exists, and any failure of the property gives a better object, a contradiction.
The first part is the trap of the method.
In a finite nonempty set an extremum always exists, but in an infinite set it must be proved, for example by the [[well-ordering principle|01BX15HSRR]].

## Motivation

Many problems ask for an object with a property, such as a line through exactly two points of a set.
A search over all objects may be long, or impossible when the family is infinite.
The extremal principle replaces the search by one well-chosen candidate.
Among the candidates, the extremal one is the most constrained: nothing in the set beats it.
So a small change that would improve it cannot exist, and this fact often forces the property.

## Remarks

### Examples

- Sylvester-Gallai: a finite set of points in the plane, not all on one line, has a line through exactly two of its points. Kelly's proof takes a point and a line through two other points at the least positive distance; this line contains exactly two points. See the [[Sylvester-Gallai theorem|T3GGJN70P2]].
- Erdős-Szekeres: every sequence of $(r - 1)(s - 1) + 1$ distinct real numbers has an increasing subsequence of length $r$ or a decreasing one of length $s$. The [[proof by the pigeonhole principle|22G1VPJW6Y]] labels each term with the length of the longest increasing subsequence ending there. See the [[Erdős-Szekeres theorem|0SNJM8HSD3]].
- Euler's theorem: if every vertex of a finite connected graph has even degree, the graph has an [[Eulerian circuit|05NWGBHKSZ]]. One proof takes a longest trail and shows that it is closed and uses every edge, as in the [[proof by a longest trail|JSB2RB25Y8]].
- Leaves of a tree: a finite [[tree|062D9KXJB1]] with at least two vertices has at least two [[leaves|EA8S0JHXMP]]. The two ends of a longest path are leaves, because a further neighbor of an end would extend the path or close a cycle. The same idea gives a [[long cycle|NT7GFT7H6T]] in a graph of large minimum degree.
- Least counterexample: every integer greater than $1$ is a product of [[primes|0SN0MAEKYX]]. If not, take the least integer $n$ that is not; then $n$ is not prime, so $n = ab$ with $1 < a, b < n$, and $a$ and $b$ are products of primes, so $n$ is one too.
- Non-crossing matchings: $n$ red and $n$ blue points in the plane, no three on a line, can be joined in red-blue pairs by $n$ segments that do not cross. A matching of least total length has no crossing, as [[this example|H58TWAEXBW]] shows.

### Non-examples

- Perron's paradox: "let $N$ be the largest positive integer; if $N > 1$ then $N^2 > N$, so $N = 1$". The step that fails is the existence of $N$, as [[this example|HJ3C7DFQBK]] shows.
- The integer lattice $\mathbb{Z}^2$: every line through two lattice points contains infinitely many, so the Sylvester-Gallai conclusion fails. Kelly's argument breaks at the start. The distance from $(0, 0)$ to the line $x - ny = 1$, which passes through the lattice points $(1, 0)$ and $(n + 1, 1)$, is $1/\sqrt{1 + n^2}$. So the positive distances have no least value.
- A function on an open interval: the function $f(x) = x$ on $(0, 1)$ has no largest value. An argument that starts "take $x$ with $f(x)$ largest" proves nothing here, because the [[extreme value theorem|0WS1A8E2P9]] needs a closed and bounded interval.

### Basic properties

- Every nonempty finite set of real numbers has a least and a greatest element.
- Every nonempty set of natural numbers has a [[least element|0AANKKNHS4]], by the well-ordering principle. Such a set need not have a [[greatest element|0XR2QK49V6]].
- A continuous real function on a closed and bounded interval takes a largest and a smallest value. More generally, a continuous real function on a nonempty [[compact space|0TVJZYB6SH]] does.
- In a partial order, a maximal element is one with nothing above it, and it need not be a greatest element. Many extremal proofs need only a [[maximal element|072G59HW59]], such as a path that cannot be extended.
- The extremal principle and [[infinite descent|0EFYCFHYFG]] are two forms of one idea. A proof by least counterexample shows that a least counterexample would have a smaller one. Infinite descent shows that every counterexample has a smaller one, which is impossible in the natural numbers.

### When it applies

The method fits when the objects carry a numerical quantity, and a failure of the property allows a local change that moves the quantity in one direction.
Typical quantities are the length of a path, the number of elements of a set, a distance, and a total length.

### The steps

1. Choose the family of objects and a quantity on it, such as a length or a distance.
2. Prove that an object with the largest or smallest value exists. In a finite nonempty family this is automatic.
3. Take such an object, and suppose it lacks the property.
4. Build from it an object with a better value. This contradicts the choice of step 2, so the object has the property.

### When it fails

The method fails when the extremum does not exist, as in Perron's paradox and the lattice $\mathbb{Z}^2$.
It also fails when the change of step 4 does not improve the quantity strictly.
Then the new object may tie with the old one, and no contradiction appears.

### Related methods

The [[pigeonhole principle|0HGVCWQGY3]] often works together with an extremal choice, as in the proof of the Erdős-Szekeres theorem.
A [[monovariant|TP3GC5J08D]] is the dynamic form of the same idea: a quantity that moves in one direction must stop at an extremal state.
An [[averaging argument|HXP9VMXV8S]] compares an object with the mean, while the extremal principle compares it with the best.

### History

James Joseph Sylvester posed the problem of ordinary lines in 1893, and Tibor Gallai published a proof in 1944.
Leroy Milton Kelly gave the proof by least distance, which Aigner and Ziegler call "simply the best" of the many proofs.
Paul Erdős and George Szekeres proved their theorem on monotone subsequences in 1935.
Oskar Perron gave his paradox as a warning that an optimization problem may have no solution, so a proof must not assume one.

### Common errors

- To take a largest or smallest object in an infinite family without a proof that it exists.
- To build an object that is only as good as the extremal one, not strictly better. Then no contradiction appears.
- To choose a quantity that the local change does not control, so that step 4 cannot be carried out.
- To confuse a maximal element with a greatest element in a partial order, or to claim that the extremal object is unique.

## Explanations

### L1 human

To prove that something exists, look at the most extreme candidate: the longest, the shortest, the largest, the closest.
Suppose this candidate lacked the property we want.
Often we could then change it a little and get a candidate that is even more extreme.
That is impossible, because we chose the most extreme one.
So the extreme candidate has the property.
There is one catch: the most extreme candidate must exist, and in an endless family it may not.

### L2 human

We prove that a finite tree with at least two vertices has at least two leaves.

1. A path in a finite graph uses each vertex at most once, so it has at most as many vertices as the graph. The tree has an edge, so paths of positive length exist.
2. So a longest path $P = v_0 v_1 \cdots v_k$ exists, with $k \ge 1$.
3. Suppose $v_0$ has a neighbor $w$ other than $v_1$.
4. If $w$ is not on $P$, then $w v_0 v_1 \cdots v_k$ is a longer path, against the choice of $P$.
5. If $w = v_j$ with $j \ge 2$, then $v_0 v_1 \cdots v_j v_0$ is a cycle, but a tree has no cycle.
6. So $v_0$ has degree $1$ and is a leaf. The same steps at $v_k$ show that $v_k$ is a leaf, and $v_0 \neq v_k$.

The typical use is to take a longest path and examine its ends.
The trap is step 1: in an infinite tree, such as the path on the integers, there is no longest path, and indeed that tree has no leaf.

### L3 human

The extremal principle is a use of the existence of extrema in an ordered set.
For finite sets this is induction on size; for the natural numbers it is the well-ordering principle; for continuous functions it is compactness.
In set theory, Zorn's lemma gives maximal elements in partial orders where every chain has an upper bound, and many existence proofs of algebra rest on it, such as the existence of a basis of a vector space.
In analysis, the direct method of the calculus of variations proves that a minimizer exists before it uses the minimizer, which is the lesson of Perron's paradox.
In combinatorics, extremal choices start many proofs in graph theory and in discrete geometry, such as Kelly's proof of the [[Sylvester-Gallai theorem|T3GGJN70P2]].
In this sub-area, the method sits beside [[invariants|8NQ190278Y]], [[monovariants|TP3GC5J08D]] and [[parity arguments|H9JT1XNDKQ]] as a standard tool for existence and impossibility.
