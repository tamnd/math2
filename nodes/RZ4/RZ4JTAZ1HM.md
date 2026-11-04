---
tag: RZ4JTAZ1HM
kind: proof
name: Proof of the identity theorem by connectedness
msc: [30C15]
proves: 0YBVKMYX0W
uses: [097KNJFJ7V, 0DG0Z72CQD, 0K83KEJ43P, 0D939CMME7]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_theorem
    locator: Proof
---

## Proof

1. Let $D$, $f$, $g$, $S$ and $z_0$ be as in the statement. Let $h = f - g$. It is [[holomorphic|0DG0Z72CQD]] on $D$, and $S$ is its set of zeros.
2. Let $A$ be the set of $z \in D$ such that $h = 0$ on some open disc with center $z$ contained in $D$.
3. $A$ is open. If $h = 0$ on $\set{w : \abs{w - z} < r}$ and $\abs{w - z} < r$, then $h = 0$ on the disc with center $w$ and radius $r - \abs{w - z}$.
4. $D \setminus A$ is open. Let $z \in D \setminus A$. By the [[isolated zeros theorem|0K83KEJ43P]] at $z$, case 1 fails, so case 2 holds.
5. After shrinking the radius of case 2, there is $r > 0$ with $\set{w : \abs{w - z} < r} \subseteq D$ and $h(w) \ne 0$ for $0 < \abs{w - z} < r$.
6. Let $w$ satisfy $0 < \abs{w - z} < r$. Since $h(w) \ne 0$, $w \notin A$. Also $z \notin A$. So the disc of step 5 lies in $D \setminus A$.
7. $z_0 \in A$. By assumption, each disc with center $z_0$ contains a point $w \ne z_0$ with $h(w) = 0$. So case 2 of the isolated zeros theorem fails at $z_0$.
8. Hence case 1 holds at $z_0$: $h = 0$ on a disc with center $z_0$. Shrinking it so that it lies in $D$ shows $z_0 \in A$.
9. By steps 3, 4 and 6, $D = A \cup (D \setminus A)$ with both sets open and disjoint. Since the [[domain|097KNJFJ7V]] $D$ is [[connected|0D939CMME7]], one of them is empty.
10. By step 8, $A$ is not empty. So $A = D$, and $h = 0$ on $D$. That is, $f(z) = g(z)$ for each $z \in D$.

## Idea

The set of points near which $f - g$ vanishes identically is open by definition. By the isolated zeros theorem its complement is also open, and the accumulation point lies in it. A connected set cannot split into two disjoint nonempty open parts, so the set is all of $D$.
