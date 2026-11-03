---
tag: Y6WKTA2PFT
kind: statement
role: theorem
name: Rural hospitals theorem
msc: [91B68]
uses: [X201T4TP0Y, CHWQVJ9F5K]
about: [X201T4TP0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Rural_hospitals_theorem
same_as:
  wikidata: Q65119854
  wikipedia: Rural hospitals theorem
---

## Statement

Let $D$ be a finite set of doctors and $H$ a finite set of hospitals, where each hospital $h$ has a capacity $q_h \ge 1$.
Each doctor has a strict ranking of the hospitals she finds acceptable, and each hospital has a strict ranking of the doctors it finds acceptable.
A *matching* assigns each doctor to at most one hospital she finds acceptable and each hospital to at most $q_h$ doctors it finds acceptable.
A doctor $d$ and a hospital $h$, acceptable to each other and not matched together, *block* a matching if two things hold.
First, $d$ is unmatched or prefers $h$ to her hospital.
Second, $h$ has a free position or prefers $d$ to one of its doctors.
A matching is *stable* if no pair blocks it.
Then:

1. the set of matched doctors is the same in every stable matching;
2. each hospital is assigned the same number of doctors in every stable matching;
3. if a hospital $h$ has a free position in some stable matching, then $h$ gets the same set of doctors in every stable matching.

## Remarks

The first two parts reduce to the one-to-one case by splitting each hospital into $q_h$ copies with the same preferences.
In the one-to-one case, compare a stable matching $\mu$ with the doctor-optimal stable matching $\mu_D$ from the [[Gale–Shapley algorithm|CHWQVJ9F5K]].
Every doctor matched in $\mu$ is matched in $\mu_D$, and every hospital position filled in $\mu_D$ is filled in $\mu$.
Counting the matched pairs in both matchings then gives equality.
The third part, proved by Alvin Roth, needs the stronger argument that a hospital with a vacancy cannot gain or lose doctors without creating a blocking pair.
Example: if a rural hospital fails to fill its positions in the stable matching produced by a centralised clearinghouse, no other stable matching would give it more doctors.
The result also holds for the [[stable marriage problem|X201T4TP0Y]] with unequal numbers of men and women or incomplete lists: the same people are single in every stable matching.

## Explanations

### L1 human

In a match between doctors and hospitals there can be several stable outcomes.
The theorem says they all fill the same number of positions at each hospital, and the same doctors find jobs.
A hospital that is short of doctors in one stable outcome is short, with exactly the same doctors, in all of them.
So changing to a different stable outcome cannot help an unpopular hospital.

### L2 human

The theorem answered a policy question about the medical residency match in the United States: whether a different stable matching rule could send more doctors to rural hospitals.
It is a basic structural fact of two-sided matching, closely tied to the lattice of stable matchings and to the optimality of deferred acceptance.
