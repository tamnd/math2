---
tag: ENY0GKRJS8
kind: concept
name: Functions of proof
aliases: [roles-of-proof, role-of-proof, purposes-of-proof]
msc: ["00A35", "97E50"]
topics: [N4P3E53HM0]
audience: ug1
uses: [0B94TKFQJX, GD2JBXJV5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - book: isbn:9781108439534
    locator: Introduction
---

## Summary

A [[mathematical proof|0B94TKFQJX]] does more than remove doubt, and two correct proofs of one statement can do quite different jobs.
The *functions of proof* are these jobs, as they appear in the practice of mathematics.
Michael de Villiers named five of them in 1990.
*Verification* shows that a statement is true.
*Explanation* shows why it is true.
*Communication* passes the result and its reasons to other people, who can then check and use them.
*Discovery* finds new results while a statement is being proved.
*Systematization* places the result in a deductive system of axioms, definitions and theorems.

## Motivation

Mathematicians often prove statements that they already believe.
They may have checked a million cases by computer, or an expert may have told them it is true.
If the only purpose of a proof were to remove doubt, such proofs would add nothing, and yet mathematicians value them, and they value new proofs of old theorems too.
So proof must do more than verify.

Take the formula $1 + 2 + \cdots + n = n(n + 1)/2$.
A proof by induction checks it, but it needs the formula in advance and gives no hint of where it came from.
Writing the sum forwards and backwards and adding,
$$\begin{aligned} S &= 1 + 2 + \cdots + n, \\ S &= n + (n - 1) + \cdots + 1, \end{aligned}$$
gives $n$ columns that each add to $n + 1$, so $2S = n(n + 1)$, and the formula appears in front of you.
The list of functions names this difference, and it explains why a teacher may choose one proof over another.

## Notation

Some authors write "roles of proof" or "purposes of proof" for the same idea.
The word "verification" here means a proof that establishes truth in every case, not a check of finitely many cases.
Some authors split explanation into "proofs that prove" and "proofs that explain", a phrase used in the literature on mathematics education.

## Remarks

### One statement, two proofs

The [[two proofs of the sum formula|D6G69GNKPC]] are the standard example.
Both verify the formula for all $n$.
The pairing proof also explains it: the sum is $n$ copies of the average term $\tfrac{n + 1}{2}$.
The same pairing then gives the sum of any arithmetic progression, which is a small act of discovery.
The induction proof serves verification, and it is the better tool when the answer is known and only needs checking.

The same contrast appears in the statement that $6$ divides $n^3 - n$ for every integer $n$.
Checking the six residues of $n$ modulo $6$ verifies it.
The factorization $n^3 - n = (n - 1) n (n + 1)$ explains it, as the L2 explanation shows in full.

### Proof as discovery

A proof often proves more than you asked for.
In [[Varignon's theorem|2TRG8VNJ4H]] the midpoints $K, L, M, N$ of the sides of a quadrilateral $ABCD$ form a parallelogram.
The vector proof computes
$$L - K = \tfrac{1}{2}(B + C) - \tfrac{1}{2}(A + B) = \tfrac{1}{2}(C - A) = M - N,$$
and it never uses that $ABCD$ is convex.
So a student who drew only convex figures learns from the proof that dented quadrilaterals work too.
The proof also shows that each side of the parallelogram is parallel to a diagonal of $ABCD$ and half as long.

### Proof as systematization and communication

Systematization places results in one deductive order and shows what each one needs.
When the [[group axioms are read as an axiom system|MRQW28BQ7D]], the proof that the identity is unique uses only the identity axiom, so the result holds in every monoid as well.
The proofs of Euclidean geometry from [[Hilbert's axioms|KM1FB8XZ2R]] do the same on a large scale, inside one [[axiomatic system|GD2JBXJV5Z]].

Communication is what lets a community check a proof.
Andrew Wiles announced a proof of Fermat's Last Theorem in 1993, and a gap was found while the written proof was being checked.
Wiles, working partly with Richard Taylor, closed the gap in 1994.
The gap was found because the proof was written out for other people to check.

### What it is not

A [[numerical check|MYFZVEQ96K]] of a formula for $n = 1$ to $100$ is not a proof.
It gives confidence for the cases it covers and verifies nothing beyond them.
An appeal to authority, such as "a famous mathematician says so", may persuade, but it neither verifies nor explains.
A drawing of one triangle suggests a result, but it says nothing about the triangles that were not drawn.

### Watch out

Conviction and verification are different things.
People can be convinced by evidence that is not a proof, as the polynomial $n^2 + n + 41$ shows: it is prime for $n = 0$ to $39$, and at $n = 40$ it equals $41^2$.
People can also doubt a correct proof because it is long or because a computer did part of it.

A second trap is to think that a proof that does not explain is not a proof.
Checking $n^3 - n$ modulo $6$ case by case is complete and correct.
Its function is verification, and that is enough to make the statement a theorem.

### History

Michael de Villiers listed verification, explanation, systematization, discovery and communication in his 1990 article "The role and function of proof in mathematics" in the journal *Pythagoras*.
Gila Hanna discussed these functions, and the difference between proofs that prove and proofs that explain, in "Proof, explanation and exploration: an overview" in *Educational Studies in Mathematics* in 2000.
The contrast between knowing that a statement holds and knowing why it holds is much older, and it goes back to Aristotle.
The proof of the [[four color theorem|0M406JC8J1]] by Kenneth Appel and Wolfgang Haken in 1976 rested on a large computer check, and it started a debate on whether a check that no person can read in full counts as a proof.

### Try it

First, which function does a proof by contradiction that $\sqrt{2}$ is irrational mainly serve, and does it also explain?
It verifies, and it explains in part: it shows that a fraction $p/q$ in lowest terms with $p^2 = 2q^2$ would force both $p$ and $q$ to be even.

Second, give a proof of $1 + 3 + 5 + \cdots + (2n - 1) = n^2$ that explains.
Stack the odd numbers as L-shaped layers: the layers of sizes $1, 3, 5, \ldots$ build squares of sides $1, 2, 3, \ldots$, since going from side $k - 1$ to side $k$ adds $2k - 1$ unit squares.

## Explanations

### L1 human

A proof does more than show that a fact is true.
It can also show why the fact is true, and that helps you remember it and use it.
For example, $1 + 2 + 3 + 4 = 10$, and you can see why by pairing $1$ with $4$ and $2$ with $3$: two pairs, each with sum $5$.
The same pairing works for any list $1, 2, \ldots, n$, so it explains the general formula.
A proof can also lead to new facts, and it lets other people check the work.

### L2 human

Here is one statement with two proofs, and the question of what each proof does.
The statement is that $n^3 - n$ is divisible by $6$ for every integer $n$.

Proof A works case by case.
The value of $n^3 - n$ modulo $6$ depends only on $n$ modulo $6$, so six cases cover every integer.
For $n = 0, 1, 2, 3, 4, 5$ the values are
$$0, \quad 0, \quad 6, \quad 24, \quad 60, \quad 120,$$
and all of them are divisible by $6$.

Proof B factors the expression.
$$n^3 - n = (n - 1) \, n \, (n + 1),$$
a product of three consecutive integers.
Among three consecutive integers one is divisible by $3$ and at least one is even, so the product is divisible by $2 \cdot 3 = 6$, because $2$ and $3$ are coprime.

Both proofs verify the statement.
Proof B also explains it, since it shows where the $2$ and the $3$ come from, and it points to a generalization.
The product of $k$ consecutive positive integers is divisible by $k!$, because if the largest of them is $n$, then $n \ge k$ and
$$\frac{n(n - 1) \cdots (n - k + 1)}{k!} = \binom{n}{k}$$
is an integer.
Watch out: Proof A is not worse as a proof.
It is complete, and its function is verification.

### L3 human

The list of functions describes practice, and it is used mainly in [[mathematics education|9622VKAWMZ]].
Its message for teaching is that students who are already convinced still need a reason to prove, and explanation, discovery and systematization supply one.
In research the same distinctions drive the search for new proofs of known theorems, such as the many proofs of quadratic reciprocity or of the infinitude of primes.

Proofs checked by computer, and proofs written for proof assistants such as Lean, separate the functions sharply.
A formal proof gives very strong verification, but it may communicate little to a human reader and explain less.
The question of what makes a proof explanatory belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
When a community accepts a proof is the subject of [[rigor and the acceptance of proofs|1BTHSHST4M]].
The [[methodology of mathematics|3FJ3XMV9KD]] places these functions within the wider cycle of conjecture, test and proof.
