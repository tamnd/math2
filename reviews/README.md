# Fidelity reviews

A fidelity review is a statement by a person. It says that a Lean statement says what the informal statement of a node says. Spec 10.6 in tamnd/math2-agent has the design.

The kernel checks that a proof proves a Lean statement. It does not check that the Lean statement is the correct statement. A review checks that. One review that counts gives the binding the fidelity level F2. Two reviews that count, by reviewers with no shared affiliation, give F3. E5 needs F2.

`m2 review` shows what you need to review a binding, and it writes the review for you. You can also write a review by hand, as the sections below tell.

## What you sign

A review says: I read the informal statement with the hash h1, and the Lean statement with the elaborated-type hash h2, with the definition of each constant that it uses. The Lean statement says what the informal statement says, up to the conventions that I list.

A `not-faithful` review is as useful as a positive review. It sends the binding back with the class of the fault and your notes.

## Who can review

- A person with an ORCID iD or a GitHub login. An agent cannot review (rule V03).
- You cannot review a binding that you wrote. The author of a binding is in `registers/bindings.reg` (rule V02).
- Your review counts only when you have a record in `registers/reviewers.reg`. Add the record in the pull request of your first review. The fields are in `registers/README.md`.

## Start as a reviewer

1. Do the practice set in [PRACTICE.md](PRACTICE.md). It has 20 items with the answers, and it takes about 20 minutes.
2. Find a binding to review. After `m2 build`, `m2 review queue -reviewer github:octocat -area 20` lists the bindings at F1 that wait for a review, in an area of MSC2020. The nodes that more nodes use come first. The list leaves out the bindings that you wrote.
3. Do the review with `m2 review`, as in the next section.
4. In the pull request of your first review, add your record to `registers/reviewers.reg`. The fields are in `registers/README.md`. Without the record, your review does not count.
5. Sign the commit, as in "Sign the commit".

After the merge, the site has a page for you at `reviewers/SLUG/`, with each review that you did. The slug is your reviewer id with each character that is not a letter, a digit or a hyphen changed to a hyphen, for example `github-octocat`. `m2 review export github:octocat` writes the same list as text that you can put in a CV or a report. Each line has the date, the review id, the node and the verdict. Give `-json` for JSON.

## With m2 review

1. Install the m2 toolchain and run `m2 build`, as in the next section.
2. Run `m2 review TAG`. The command shows the review packet: the statement section and the Lean statement side by side, the Lean statement without notation, each constant of the Lean statement with its type and the nodes that bind it, the battery report and the reviews of the binding. When the node has more than one Lean binding, give the declaration with `-decl`.
3. Read the packet and the definitions, as in "How to review".
4. Write the review:

   ```sh
   m2 review -reviewer github:octocat -verdict faithful -dry-run 3C53TD
   m2 review -reviewer github:octocat -verdict faithful-with-conventions -convention "the order of a finite group is Nat.card" -commit 3C53TD
   ```

   Give `-convention` once for each convention, and `-class` for the verdict `not-faithful`. `-notes` adds your notes. `-dry-run` checks the review and changes no file. Without `-dry-run`, the command copies the two hashes from the build, gives the review the next id, adds it to the review file and adds the id to the binding. `-commit` commits the two files with `git commit -S`, so your key signs the commit. You can set `M2_REVIEWER` instead of `-reviewer`.

The command refuses the review when you wrote the binding, when the reviewer is not a person, or when the statement changed after the last build.

## Before you start

1. Install the m2 toolchain from tamnd/math2-agent. Use the version that the check workflow pins.
2. Run `m2 build` in the root of the repository.
3. Run `m2 status TAG` for the node. Copy these values from the output:
   - the statement hash, from the line `statement hash`;
   - the declaration that the kernel checks, from the line `binding`. When the binding has an adapter, you review the adapter;
   - the type hash of that declaration, from the line `type hash`.

## How to review

1. Read the statement section of the node. Also read the definitions of the nodes that it links to.
2. Open the declaration in the Lean source, at the Mathlib commit in `lean/lake-manifest.json`. Read the statement and the definition of each constant in it. Do not read only the name.
3. Compare the two. Look for these faults (spec 10.5):

   | Class | Fault |
   |---|---|
   | `M-hyp-missing` | A hypothesis of the informal statement is not in the Lean statement. |
   | `M-hyp-extra` | The Lean statement has a hypothesis that the informal statement does not have. |
   | `M-quant` | The order or the scope of the quantifiers is wrong. |
   | `M-vacuous` | The hypotheses cannot be true together. |
   | `M-junk` | A junk value makes the statement trivially true or false, for example division by zero or natural subtraction. |
   | `M-def` | A constant means something different from the informal notion. |
   | `M-type` | The carrier is wrong, for example ℕ for ℤ or an off-by-one `Fin n`. |
   | `M-conv` | A convention is different, for example ℕ with 0, or `⊆` for `⊂`. |
   | `M-weak` | The Lean statement is a special case. |
   | `M-strong` | The Lean statement is stronger, and it is false. |
   | `M-context` | The statement depends on local notation or instances. |
   | `M-tamper` | The proof environment changes a constant in the statement. |

4. Give one verdict:
   - `faithful`: the two statements say the same thing.
   - `faithful-with-conventions`: they say the same thing when you use the conventions that you list. A convention that changes the meaning is an `M-conv` fault, not a convention.
   - `not-faithful`: give the class of the fault and explain it in the notes.

An undergraduate statement takes about 3 minutes. If you need much more time, write in the notes what was difficult.

## The review file

The reviews of the node with the tag `3C53TD` are in `reviews/3C/3C53TD.yaml`. The directory is the first two characters of the tag. The file has a list under the key `reviews`. Add your review at the end of the list. Do not change or remove a review. A new review replaces an old review.

```yaml
reviews:
  - id: r-3C53TD-01
    reviewer: github:octocat
    date: 2026-12-01
    decl: Math2.Match.lagrange
    statement_hash: "blake3:..."
    type_hash: "blake3:..."
    verdict: faithful-with-conventions
    conventions: [the order of a finite group is Nat.card]
    notes: The adapter reads the theorem for a finite group G and a subgroup H.
```

| Field | Value |
|---|---|
| `id` | `r-`, the tag, `-` and the next number of the file, for example `r-3C53TD-02` |
| `reviewer` | `orcid:` and your ORCID iD, or `github:` and your GitHub login, as in `registers/reviewers.reg` |
| `date` | the date of the review, `YYYY-MM-DD` |
| `decl` | the declaration that you read: the adapter when the binding has one |
| `statement_hash` | the statement hash from `m2 status` |
| `type_hash` | the type hash from `m2 status` |
| `verdict` | `faithful`, `faithful-with-conventions` or `not-faithful` |
| `conventions` | the conventions, for the verdict `faithful-with-conventions` |
| `class` | the class of the fault, for the verdict `not-faithful` only |
| `notes` | free text |

The schema is `schema/review.v1.json`.

Then add the id to the field `fidelity_reviews` of the binding in the node file:

```yaml
formal:
  - system: lean4
    library: mathlib
    decl: Subgroup.card_subgroup_dvd_card
    match: stronger
    adapter: Math2.Match.lagrange
    fidelity_reviews: [r-3C53TD-01]
```

## The monthly re-review sample

Each month, a maintainer draws a sample of 1% of the bindings at F2 and 0.5% of the bindings at F3 (spec 10.8). A different reviewer reviews each binding in the sample again, blind. The results give the measured disagreement of each level, by area.

```sh
m2 build
m2 review sample -month 2026-11 -write
git commit -S -m "Draw the re-review sample of 2026-11" registers/samples.reg
```

`m2 review sample` writes the seed of the draw. With the same seed and the same build, anyone can draw the same sample again. The draw gives each binding to a registered reviewer who did not write the binding and has no review of it. It takes a reviewer with an area of the node first, then a reviewer with no affiliation of the first reviewers, then the reviewer with the fewest re-reviews in the month.

The reviewer of a sample does the review as in "How to review", but starts with `m2 review -blind TAG`. The packet then does not show the reviews of the binding. The review files are public, thus do not open the review file of the node before you write your verdict. The re-review is a normal review: if it agrees, it counts for the binding as a second review.

```sh
m2 review measure 2026-11
```

`m2 review measure` shows each sample as done, open or with no reviewer, and the rate of disagreement of each level, in all areas and in each top-level MSC2020 class. A re-review with the verdict `not-faithful` disagrees. Fix the binding as for any other `not-faithful` review.

## Sign the commit

Each commit that changes `reviews/` must have a signature that GitHub verifies. The check workflow fails on a pull request with an unsigned review commit. Set up a GPG or an SSH signing key as in the GitHub documentation "Signing commits", and commit with `git commit -S`.

## Check your review

```sh
python .github/scripts/check_reviews.py
m2 build
m2 status 3C53TD
```

`check_reviews.py` checks the file against the schema, the id, the node and your record in the register. `m2 status` shows your review with the state `counts`. Any other state tells you why the review does not count.

## When a review becomes stale

The review is bound to the two hashes. If the statement section of the node changes, or a Mathlib bump changes the elaborated type of the declaration, a hash changes. The review then has the state `stale`. It does not count, and the binding goes down to its level without the review (rule F02). `m2 audit` reports it. A new review with the new hashes is necessary.

Rule V04 also asks for a new review when a review is older than 24 months and the node or a node that it uses changed after the review.
