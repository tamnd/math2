---
tag: 0HGVCWQGY3
kind: statement
role: theorem
name: Pigeonhole principle
aliases: [dirichlet-box-principle]
msc: ["05A05", "00A35"]
topics: [GB14W4SYPK]
audience: school
about: [0EPAT51DXQ, 09NWETVTNY, 05099E1NMJ]
uses: [05099E1NMJ, 0EPAT51DXQ, 09NWETVTNY]
formal:
  - system: lean4
    library: mathlib
    decl: Finset.exists_ne_map_eq_of_card_lt_of_maps_to
    match: exact
history:
  first_stated: "Jean Leurechon, 1622, in the form that two people have the same number of hairs"
  notes: "Dirichlet used the principle in 1834 and in his approximation theorem, and German texts call it the Schubfachprinzip (drawer principle)."
sources:
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: History
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_basics_pigeonhole.ptx#L6
    locator: source/s_basics_pigeonhole.ptx:6
same_as:
  wikidata: Q188276
  wikipedia: Pigeonhole principle
---

## Statement

If you put more objects than there are boxes into the boxes, then some box receives at least two objects.

Let $A$ and $B$ be [[finite sets|070R982G4B]], with numbers of elements $|A|$ and $|B|$ as in [[cardinality of a finite set|05099E1NMJ]].
Let $f : A \to B$ be a [[function|0EPAT51DXQ]], and assume that $|A| > |B|$.
Then there are elements $a \neq a'$ of $A$ with $f(a) = f(a')$.
Equivalently, $f$ is not [[injective|09NWETVTNY]].

The everyday form takes $|A| = n + 1$ and $|B| = n$: if $n + 1$ objects go into $n$ boxes, then some box holds at least two objects.
Here $A$ is the set of objects, $B$ is the set of boxes, and $f(a)$ is the box of the object $a$.
The [[proof|E0R6P2FMCM]] compares the size of the image of $f$ with the size of $B$.

## Remarks

### A first use: five points in a square

Put five points anywhere in a closed square of side $1$.
We claim that two of them are at distance at most $\tfrac{\sqrt{2}}{2}$.
Cut the square into four closed squares of side $\tfrac{1}{2}$ by the two lines through its center, and let these be the boxes.
A point on a cutting line lies in two small squares, and we put it in either one.
Five points in four boxes give two points $P$ and $Q$ in one small square, and two points of that square are at most its diagonal apart:
$$|PQ| \le \sqrt{\left(\tfrac{1}{2}\right)^2 + \left(\tfrac{1}{2}\right)^2} = \tfrac{\sqrt{2}}{2}.$$
Check: the four corners and the center are five points whose smallest distance is exactly $\tfrac{\sqrt{2}}{2}$, so the bound cannot be improved.

### Choosing the boxes is the skill

The principle itself is a one-line count, so every application is really a choice of boxes.
You must decide what the objects are, what the boxes are, and why two objects in one box give the conclusion.
In the square problem, two boxes would also work as a count, but two points in a $\tfrac{1}{2} \times 1$ rectangle can be $\tfrac{\sqrt{5}}{2}$ apart, which is too weak.
A good rule is to make the boxes as small as the conclusion needs and as few as the count allows.
For example, suppose that no head has more than $999\,999$ hairs.
Then a city with more than a million people has two people with the same number of hairs, since the boxes are the hair counts $0, 1, \dots, 999\,999$, exactly a million of them.
The [[applications of the pigeonhole principle|5EAFG80VX6]] show four harder choices of boxes.

### Why each hypothesis is needed

The strict inequality $|A| > |B|$ is the whole point.
For $A = B = \{1, 2\}$, the identity map is injective, so equal sizes never force a collision.

Finiteness matters when "more" is read as "a proper superset".
The set $\mathbb{N}$ is a proper superset of the set $E$ of even numbers, but $n \mapsto 2n$ is an injective map from $\mathbb{N}$ to $E$, as in [[Hilbert's hotel|0N3Y8G340X]].
For infinite sets the right notion of size is cardinality, and then "larger" already means "no injection".

The map must be defined on all of $A$, which means that every object goes into a box.
If only two of three objects are placed in two boxes, the placed objects can go into different boxes.

### What it gives you

The first consequence is a counting fact: there is no injection from a set of size $m$ to a set of size $n < m$, so the [[number of injections|0X0N833FF8]] from $A$ to $B$ is $0$ when $|A| > |B|$.
A second consequence is that a map $f : A \to B$ between finite sets with $|A| = |B|$ is injective exactly when it is surjective.
This is the step behind the proof that [[a finite integral domain is a field|0EBE031B8E]]: multiplication by a nonzero element is injective, so it is surjective, so $1$ is a multiple of that element.
In number theory, [[Dirichlet's approximation theorem|04JAY9DGB7]] has a [[proof by boxes of fractional parts|Q4PTS4BYNG]].
In combinatorics, the [[Erdős-Szekeres theorem|0SNJM8HSD3]] has a [[proof by boxes of pairs of lengths|22G1VPJW6Y]].

### The converse

Read one way, the converse is true for finite sets: if every function $f : A \to B$ fails to be injective, then $|A| > |B|$.
Indeed, if $|A| = m \le n = |B|$, we list $A = \{a_1, \dots, a_m\}$ and $B = \{b_1, \dots, b_n\}$, and the map $a_i \mapsto b_i$ is injective.
Read the other way, the converse is false: one non-injective map says nothing about the sizes.
The constant map from $\{1, 2\}$ to $\{1, 2\}$ is not injective, and $|A| = |B|$.

### Generalizations

The [[generalized pigeonhole principle|0BY7GN3449]] counts more carefully: when $n$ objects go into $k$ boxes, some box holds at least $\lceil n/k \rceil$ objects.
The [[infinite pigeonhole principle|0FS3RHF6KE]] puts infinitely many objects into finitely many boxes and finds a box with infinitely many.
There is also a measure form: if measurable subsets of a region of area $1$ have total area more than $1$, then two of them overlap in a set of positive area.
[[Blichfeldt's theorem|A3FTHW4NES]] is a result of this kind.

### Watch out

The principle proves that two objects share a box, but it does not say which box or which objects.
A student who answers "the two people born in January" has misread it: among $13$ people, the shared month may be any month.
A second slip is to count the boxes wrong.
Among $n$ people at a party, the possible numbers of friends present are $0, 1, \dots, n - 1$, which is $n$ boxes for $n$ people, so the plain count fails.
The fix is to notice that $0$ and $n - 1$ cannot both occur, which leaves $n - 1$ boxes.

### Try it

Show that among any $11$ integers, two have a difference divisible by $10$.
Use the $10$ last digits as boxes: two of the integers end in the same digit, and their difference ends in $0$.

Show that if you choose $6$ numbers from $\{1, 2, \dots, 10\}$, two of them add up to $11$.
The five pairs $\{1, 10\}, \{2, 9\}, \{3, 8\}, \{4, 7\}, \{5, 6\}$ are the boxes, and six numbers in five boxes put both numbers of one pair in your choice.

## History

Jean Leurechon stated a form of the principle in 1622: two people must have the same number of hairs on their heads.
Peter Gustav Lejeune Dirichlet used the principle in 1834, and he used it again to prove his approximation theorem.
The name "Dirichlet's box principle" comes from his use.
German texts call it the Schubfachprinzip, the drawer principle.

## Explanations

### L1 human

If there are more letters than mailboxes, and every letter goes into a mailbox, then some mailbox gets two letters.
The reason is plain counting: if each mailbox held at most one letter, there would be at most as many letters as mailboxes.
For example, among any $13$ people, two have their birthdays in the same month, because there are only $12$ months.
The principle tells us that two such people exist.
It does not tell us which two they are.

### L2 human

Here is a problem from number theory: among any $n + 1$ numbers chosen from $\{1, 2, \dots, 2n\}$, two are consecutive.
The objects are the chosen numbers.
The boxes are the $n$ pairs
$$\{1, 2\}, \{3, 4\}, \dots, \{2n - 1, 2n\}.$$
Each number lies in exactly one pair, so the map that sends a number to its pair is a function from the chosen set to the set of pairs.
There are $n + 1$ chosen numbers and $n$ pairs, so two chosen numbers lie in one pair, and the two numbers of a pair are consecutive.
Check with $n = 3$: any $4$ numbers from $\{1, \dots, 6\}$ contain two consecutive ones, while the $3$ numbers $1, 3, 5$ do not.
The example shows the typical use: the boxes are built so that "same box" means exactly the property that you want, and the count is the last and easiest step.

### L3 human

In the language of functions, the principle says that there is no injection from a finite set to a smaller one.
This is the same fact that makes the number of elements of a finite set well defined, so the principle sits at the base of finite combinatorics.
In Mathlib the statement for finite sets is `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`, and the version for finite types is `Fintype.exists_ne_map_eq_of_card_lt`.

The principle is the start of Ramsey theory: a large structure split into a few classes has a class with a lot of structure, as in the [[theorem on friends and strangers|0NYM0ZGAK9]] and [[Ramsey's theorem|00TQV3F5S4]].
In number theory it gives Dirichlet's approximation theorem and Thue's lemma, and in transcendence theory it gives Siegel's lemma and the [[auxiliary functions|X01V173DZD]] built from it.
The other methods of [[counting, invariant and extremal arguments|GB14W4SYPK]], such as [[double counting|0F8YBHF2W3]] and the [[averaging argument|HXP9VMXV8S]], refine the same count: they compare a total with the number of places it is spread over.
