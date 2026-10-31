---
records:
    - id: N0E1JWRFEV
      kind: problem-set
      title: Kvant 2010, no. 1
      date: "2010"
      expressions:
        - key: e1
          kind: edition
          date: "2010"
          structure: N0E1JWRFEV/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2010-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: N0EVQ46HBR
      kind: preprint
      title: Property B for random non-uniform hypergraphs
      creators:
        - name: Grzegorz Ryn
          role: author
        - name: Jakub Kozik
          role: author
      date: "2026-10-05"
      msc:
        - code: 05-XX
          from: arxiv
        - code: 60-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: cs.DM
        - system: arxiv
          code: math.CO
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-05"
          ids:
            arxiv: "2610.07379"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.07379"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.07379"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
