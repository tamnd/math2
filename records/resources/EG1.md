---
records:
    - id: EG1EKN6C64
      kind: monograph
      title: Holomorphic Curves in Low Dimensions
      creators:
        - name: Chris Wendl
          role: author
      date: "2018"
      expressions:
        - key: e1
          kind: edition
          date: "2018"
          ids:
            doi: 10.1007/978-3-319-91371-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783319913698"
                    - "9783319913711"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-91371-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: EG1XXNSTXX
      kind: preprint
      title: Persistent Gaussian Perturbations Prevent Oversmoothing in Recurrent Graph Neural Networks
      creators:
        - name: Mostafa Haghir Chehreghani
          role: author
      date: "2026-07-30"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.AI
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: math.IT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-07-30"
          ids:
            arxiv: "2607.28185"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2607.28185"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
