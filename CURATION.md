# Curation of alignment proposals

This guide tells you how to decide on the proposals of `m2 align`. Read it once from start to end before your first decision. Spec 16.3 and rules A02 to A04 in tamnd/math2-agent have the design.

## What a proposal is

`m2 align <source>` compares each node with the records of an external source, for example Wikidata, the OEIS or zbMATH Open. When a record looks like a node, the aligner writes a proposal. The aligner never changes a node. Only a person decides, and the decision goes into a pull request like any other change.

There are four kinds of proposal:

| Edge | What it says | Example |
|---|---|---|
| `same_as` | The node and the record are the same mathematical object or the same statement. | The node Group and the Wikidata item Q83478. |
| `close_to` | The node and the record are near, but they are not the same. | A node for a theorem on finite groups and a record for the general case. |
| `aligned` | The record is a paper, and the paper states the node. | A zbMATH Open document that proves the statement of the node. |
| `duplicate` | Two nodes of math2 can be one node. | Two concept nodes for the same definition. |

The proposals are in `queues/align/<system>.jsonl`, one file for each external system. The proposals of duplicates are in `queues/dedup.jsonl`. Each file has the proposals in the order of the work: the node that most nodes depend on comes first. Thus start at the top.

## Before you start

1. Get the tools. Install `m2` (README of tamnd/math2-agent) and clone this repository.
2. Know your identity. Each decision records a person: `orcid:` and your ORCID iD, or `github:` and your GitHub login. A bot account or an agent cannot decide, and `m2` refuses such a name.
3. Get the records. A proposal does not store the title or the text of its record, because the licence of a source can forbid it. Run `m2 ingest <source>` for each source that you work on. Then `m2 align queue` can show the titles.

```sh
m2 ingest wikidata
m2 align queue                   # all the proposals, the most central node first
m2 align queue -system wikidata  # the proposals of one system
```

Each line of the queue is one proposal:

```
3f9a0c12b7de  0.962  1H8D2C same_as wikidata:Q83478  group
```

The fields are the id of the proposal, the score from 0 to 1, the tag of the node, the edge, the system and the id of the record, and the title of the record.

## How to decide on one proposal

Do these steps for each proposal. Do not decide on a proposal from the score alone. A high score tells you only that the names and the formulas are near.

1. Open the node file `nodes/<first three characters of the tag>/<tag>.md`. Read the statement, the definitions that it uses and the `notes` section.
2. Open the record at its source. Use the page of the source, not the title in the queue. The table at the end of this guide gives the address of each system.
3. Compare the two. Ask these questions:
   - Is it the same object or the same statement, and not a special case or a generalization?
   - Do the two use the same conventions? Examples: does 0 count as a natural number, is a ring unital, is a graph simple, is a manifold Hausdorff and second countable?
   - Does the record have one meaning? A page that lists several objects, or a disambiguation page, is not a match.
   - For a theorem: are the hypotheses the same? A theorem with one hypothesis more or less is `close_to`, not `same_as`.
4. Decide:
   - All the answers agree: accept the proposal.
   - The two are near, but they differ: accept a `close_to` proposal with a note that tells how they differ. When the proposal is a `same_as` and the two are only near, reject it. If the record is useful, add a `close_to` edge with a note to the node by hand in the same pull request.
   - The two are not related, or you are not sure after the checks: reject the proposal or leave it in the queue for another curator. A rejection is permanent for that node and that record. The aligner does not propose the edge again. Thus reject only when you are sure that the edge is wrong.
5. Run the command:

```sh
m2 align accept -by github:octocat 3f9a0c12b7de
m2 align accept -by github:octocat -note "The record is the finite case only." 8e01d2c4a9b3
m2 align accept -by github:octocat -match weaker 41d7e09a3c55
m2 align reject -by github:octocat 5c7e2b90d1fa
```

`m2 align accept` writes the edge into the node file, records your decision in `registers/crosswalk.reg` with the hash of the record, and removes the proposal from the queue. `m2 align reject` records the decision and removes the proposal.

### Notes for each kind of edge

- `close_to` needs `-note`. Write in one sentence how the node and the record differ. Write the note in your own words. Do not copy text from the record.
- `aligned` needs `-match`, which tells how the paper states the node:

  | Match | The paper states |
  |---|---|
  | `exact` | the statement of the node |
  | `stronger` | more than the node, and the node follows directly |
  | `weaker` | less than the node, for example a special case |
  | `variant` | an equivalent form that needs a short argument |
  | `partial` | a part of the statement only |

- `duplicate` changes no node. When you accept it, you agree that the two nodes are one node. The merge or the retirement of a node is a separate pull request, and it needs the approval of two curators and an entry in the release notes (spec 16.2). When the two nodes are different, write the difference in the notes of both nodes, and reject the proposal.

### An edge that is in a node already

Sometimes a person or an agent writes a `same_as` value into a node without the queue. Check the value with the steps above. When it is correct, record your check:

```sh
m2 align confirm -by github:octocat 3C53TD wikidata
```

When it is wrong, remove the value from the node in your pull request, and write the reason in the pull request.

## Open a pull request

Decide on a group of proposals, for example 20 proposals of one system, and put them in one pull request. Run `m2 check` before you push. Write in the description which proposals you accepted and rejected, and why for each hard case.

If you made a mistake before the merge, use `git restore` on the node files, the register and the queue, and decide again. After the merge, do not change a line of the register. Open an issue that names the proposal, and a curator corrects the node in a new pull request.

## Who can decide and who can merge

| Role | Can |
|---|---|
| any person with an ORCID iD or a GitHub account | decide on proposals and open the pull request |
| a curator of the area of the node | approve and merge the pull request. A new edge needs one curator approval (spec 16.2). |
| two curators of the area | approve the merge, the split or the retirement of nodes after a duplicate |
| an agent or a bot | propose edges only. It never decides, approves or merges. |

The area of a node is its MSC two-digit class or a narrower topic. `registers/reviewers.reg` lists the reviewers and the curators of each area. Do not approve a pull request that has your own decisions in it.

## Time limits

The audit reports the work that waits too long. Both rules are soft (severity S): they do not block a merge, but each audit report shows them.

| Rule | What waits | Limit |
|---|---|---|
| A02 | A `same_as` value that an agent wrote, as the provenance log in `prov/` shows, and that has no decision of a person | 90 days from the write |
| A04 | A proposal in `queues/dedup.jsonl` | 30 days from the date `proposed` of the proposal |

Thus give these items priority. A duplicate pair that waits makes the graph count one thing two times. An agent value that waits can make a wrong link look checked.

Rule A03 also uses your decisions. Each decision has the hash of the record at that time. When the record changes at its source, rule A03 reports the edge, and a person must check it again.

## The address of a record

| System | Address of the id |
|---|---|
| `wikidata` | `https://www.wikidata.org/wiki/<QID>` |
| `oeis` | `https://oeis.org/<A-number>` |
| `stacks` | `https://stacks.math.columbia.edu/tag/<tag>` |
| `kerodon` | `https://kerodon.net/tag/<tag>` |
| `nlab` | `https://ncatlab.org/nlab/show/<page name>` |
| `lmfdb` | `https://www.lmfdb.org/<path>` |
| `zbmath` | `https://zbmath.org/?q=an:<Zbl number>`. For a document id, use the URL of the record. |
| `arxiv` | `https://arxiv.org/abs/<id>` |
| `erdos` | `https://www.erdosproblems.com/<number>` |
| `palomar` | the entry in the Palomar registry |
| `mathlib` | the documentation page of the declaration, which the record gives as its URL |

For a source that is not in this table, the record of `m2 ingest` has the URL.
