---
records:
    - id: 3TECBHQ4AA
      kind: problem-set
      title: IMO 2011 Shortlist
      date: "2011"
      expressions:
        - key: e1
          kind: edition
          date: "2011"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: 2011-sl
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
    - id: 3TED83HAME
      kind: preprint
      title: Evolutionary paths under catastrophes
      creators:
        - name: Rinaldo B. Schinazi
          role: author
      date: "2021-11-15"
      msc:
        - code: 60-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: q-bio.PE
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2021-11-15"
          ids:
            arxiv: "2111.07760"
      scope:
        value: out
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2111.07760"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to out
---
